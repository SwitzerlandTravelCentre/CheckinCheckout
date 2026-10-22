"""Offline checks for this repository's examples and documentation, not a production schema."""
from collections import Counter
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import unittest
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "examples/content"


class RepositoryIntegrityTests(unittest.TestCase):
    def read_json(self, path):
        return json.loads(path.read_text(encoding="utf-8"))

    def safe_file(self, root, relative):
        self.assertIsInstance(relative, str, "Release paths must be strings")
        self.assertRegex(relative, r"^[a-z0-9][a-z0-9./-]*$", f"Unsafe path: {relative!r}")
        self.assertFalse(
            any(part in ("", ".", "..") for part in relative.split("/")),
            f"Unsafe path segment: {relative!r}",
        )
        self.assertFalse(PurePosixPath(relative).is_absolute(), f"Absolute path: {relative}")
        resolved = (root / relative).resolve()
        self.assertTrue(
            resolved.is_relative_to(root.resolve()),
            f"Path escapes its content root: {relative}",
        )
        self.assertTrue(resolved.is_file(), f"Missing release file: {relative}")
        return resolved

    def demo_release(self):
        current = self.read_json(CONTENT / "control/current.json")
        release_id = current["releaseId"]
        self.assertRegex(release_id, r"^[a-z0-9][a-z0-9-]*$", "Invalid release ID")
        manifest_path = self.safe_file(CONTENT, current["manifestPath"])
        expected_root = (CONTENT / "releases" / release_id).resolve()
        self.assertEqual(
            manifest_path, expected_root / "manifest.json",
            "current.json must select the manifest of its declared release",
        )
        return current, manifest_path, self.read_json(manifest_path)

    def test_relative_markdown_links_resolve(self):
        ignored = {".git", ".venv", "venv", "node_modules", "__pycache__"}
        inline = re.compile(r'!?\[[^\]\n]*\]\(\s*(?:<([^>]+)>|([^\s)]+))')
        definition = re.compile(r'^\s{0,3}\[[^\]]+\]:\s*(?:<([^>]+)>|(\S+))')
        checked = 0
        for directory, folders, files in os.walk(ROOT):
            folders[:] = [name for name in folders if name not in ignored]
            for name in sorted(files):
                if not name.endswith(".md"):
                    continue
                document = Path(directory) / name
                fence = None
                for number, line in enumerate(document.read_text(encoding="utf-8").splitlines(), 1):
                    marker = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
                    if marker:
                        run = marker.group(1)
                        if fence is None:
                            fence = run
                        elif run[0] == fence[0] and len(run) >= len(fence):
                            fence = None
                        continue
                    if fence is not None:
                        continue
                    links = list(inline.finditer(line))
                    reference = definition.match(line)
                    if reference:
                        links.append(reference)
                    for link in links:
                        target = link.group(1) or link.group(2)
                        parsed = urlsplit(target)
                        if parsed.scheme or parsed.netloc or not parsed.path:
                            continue
                        path = Path(unquote(parsed.path))
                        if path.is_absolute():
                            continue
                        checked += 1
                        with self.subTest(document=str(document.relative_to(ROOT)), line=number, target=target):
                            self.assertTrue(
                                (document.parent / path).exists(),
                                f"{document.relative_to(ROOT)}:{number}: missing link target {target}",
                            )
        self.assertGreater(checked, 0, "No local Markdown links were checked")

    def test_booking_component_relationships_resolve_uniquely(self):
        fixtures = sorted((ROOT / "examples/nezasa").glob("booking_example_*.json"))
        self.assertEqual(len(fixtures), 6, "Expected all six published booking examples")
        for fixture in fixtures:
            with self.subTest(fixture=fixture.name):
                booking = self.read_json(fixture)
                included = Counter((item["type"], item["id"]) for item in booking["included"])
                self.assertTrue(included, f"{fixture.name}: no included resources")
                self.assertTrue(
                    all(count == 1 for count in included.values()),
                    f"{fixture.name}: duplicate included resource identities",
                )
                references = booking["data"]["relationships"]["components"]["data"]
                self.assertTrue(references, f"{fixture.name}: no component relationships")
                keys = [(item["type"], item["id"]) for item in references]
                self.assertEqual(len(keys), len(set(keys)), f"{fixture.name}: duplicate component relationships")
                for key in keys:
                    self.assertEqual(included[key], 1, f"{fixture.name}: unresolved component {key}")

    def test_demo_release_integrity_and_manifest_coverage(self):
        current, manifest_path, manifest = self.demo_release()
        self.assertEqual(
            hashlib.sha256(manifest_path.read_bytes()).hexdigest(), current["manifestSha256"],
            "current.json has an outdated manifest checksum",
        )
        release_root = manifest_path.parent
        self.assertEqual(current["schemaVersion"], "1.0", "Review the draft fixture contract when its version changes")
        self.assertEqual(manifest["schemaVersion"], current["schemaVersion"], "Manifest schema version differs")
        self.assertEqual(manifest["releaseId"], current["releaseId"], "Manifest release ID differs")
        declared = set()
        for entry in manifest["files"]:
            relative = entry["path"]
            self.assertNotIn(relative, declared, f"Duplicate manifest path: {relative}")
            self.assertNotEqual(relative, "manifest.json", "Manifest must not include itself")
            declared.add(relative)
            path = self.safe_file(release_root, relative)
            self.assertEqual(
                hashlib.sha256(path.read_bytes()).hexdigest(), entry["sha256"],
                f"Outdated checksum for {relative}",
            )
            if path.suffix == ".json":
                self.assertEqual(entry["contentType"], "application/json", f"Incorrect MIME type for {relative}")
                document = self.read_json(path)
                self.assertEqual(document["schemaVersion"], current["schemaVersion"], f"{relative}: schema version differs")
                self.assertEqual(document["releaseId"], current["releaseId"], f"{relative}: release ID differs")
        actual = {
            path.relative_to(release_root).as_posix()
            for path in release_root.rglob("*")
            if path.is_file() and path != manifest_path
        }
        self.assertEqual(declared, actual, "Manifest must cover every release file except itself")
        self.assertTrue({"catalog.json", "mappings.json"}.issubset(declared), "Release lacks catalog or mappings")

    def test_catalog_ids_and_package_references(self):
        _, manifest_path, _ = self.demo_release()
        catalog = self.read_json(manifest_path.parent / "catalog.json")
        ids = {}
        for collection in ("packages", "hints", "images"):
            values = [item["id"] for item in catalog[collection]]
            self.assertEqual(len(values), len(set(values)), f"Duplicate IDs in {collection}")
            ids[collection] = set(values)
        self.assertTrue(ids["packages"], "Demo catalog must include a package")
        for package in catalog["packages"]:
            for field, collection in (("hintIds", "hints"), ("imageIds", "images")):
                for reference in package[field]:
                    self.assertIn(reference, ids[collection], f"{package['id']}: unresolved {field} reference {reference}")

    def test_mapping_keys_are_unique_and_packages_exist(self):
        _, manifest_path, _ = self.demo_release()
        catalog = self.read_json(manifest_path.parent / "catalog.json")
        mappings = self.read_json(manifest_path.parent / "mappings.json")["mappings"]
        package_ids = {package["id"] for package in catalog["packages"]}
        seen = set()
        self.assertTrue(mappings, "Demo release must include a mapping")
        for mapping in mappings:
            key = tuple(mapping[field] for field in (
                "sourceSystem", "sourceNamespace", "referenceType", "referenceValue"
            ))
            self.assertNotIn(key, seen, f"Duplicate complete mapping key: {key}")
            seen.add(key)
            self.assertIn(mapping["packageId"], package_ids, f"Mapping references unknown package: {mapping['packageId']}")


if __name__ == "__main__":
    unittest.main()
