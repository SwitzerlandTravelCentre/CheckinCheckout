"""Offline integration checks; no credentials, API requests or GUI windows."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock, patch

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "nezasa_fetcher", ROOT / "components/nezasa-fetcher/app/nezasa_fetch_ui.py"
)
fetcher = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(fetcher)


class FetcherIntegrationTests(unittest.TestCase):
    def response(self, status=200, payload=None):
        response = Mock(status_code=status, text="synthetic error response")
        response.json.return_value = payload
        return response

    def client(self, response):
        client = Mock()
        client.RequestException = OSError
        client.get.return_value = response
        return client

    def test_booking_request_and_full_payload(self):
        payload = {"data": {"type": "booking", "id": "demo-id", "attributes": {}}, "included": [], "extra": {"note": "äöü"}}
        client = self.client(self.response(payload=payload))
        with patch.object(fetcher, "load_requests_modules", return_value=(client, lambda u, p: (u, p))):
            actual = fetcher.fetch_booking_json("demo-channel", "demo-id", "demo-user", "fake-password")
        self.assertIs(actual, payload)
        client.get.assert_called_once_with(
            "https://demo-channel.tripbuilder.app/bookings/v1.13/demo-id",
            headers={"Accept": "application/vnd.api+json"},
            auth=("demo-user", "fake-password"), timeout=30,
        )

    def test_http_failures(self):
        for status, message in [(401, "Unauthorized"), (404, "Not Found"), (500, "HTTP 500")]:
            with self.subTest(status=status):
                client = self.client(self.response(status))
                with patch.object(fetcher, "load_requests_modules", return_value=(client, Mock())):
                    with self.assertRaisesRegex(RuntimeError, message):
                        fetcher.fetch_booking_json("demo", "demo", "user", "fake")

    def test_invalid_json(self):
        response = self.response()
        response.json.side_effect = ValueError("not JSON")
        client = self.client(response)
        with patch.object(fetcher, "load_requests_modules", return_value=(client, Mock())):
            with self.assertRaisesRegex(RuntimeError, "not valid JSON"):
                fetcher.fetch_booking_json("demo", "demo", "user", "fake")

    def test_network_failure(self):
        client = self.client(None)
        client.get.side_effect = OSError("synthetic timeout")
        with patch.object(fetcher, "load_requests_modules", return_value=(client, Mock())):
            with self.assertRaisesRegex(RuntimeError, "before a response"):
                fetcher.fetch_booking_json("demo", "demo", "user", "fake")

    def test_example_exports_preserve_all_json_data(self):
        examples = sorted((ROOT / "examples/nezasa").glob("booking_example_*.json"))
        self.assertEqual(len(examples), 2)
        for source in examples:
            with self.subTest(example=source.name), tempfile.TemporaryDirectory() as temp:
                payload = json.loads(source.read_text(encoding="utf-8"))
                destination = Path(temp) / "nested" / source.name
                client = self.client(self.response(payload=payload))
                with patch.object(fetcher, "load_requests_modules", return_value=(client, Mock())), patch.object(
                    fetcher, "build_output_path", return_value=destination
                ):
                    output = fetcher.fetch_and_save("demo", payload["data"]["id"], "user", "fake")
                self.assertEqual(output, destination)
                self.assertEqual(json.loads(output.read_text(encoding="utf-8")), payload)

    def test_failed_fetch_does_not_write_a_file(self):
        with tempfile.TemporaryDirectory() as temp:
            destination = Path(temp) / "booking_demo.json"
            with patch.object(fetcher, "fetch_booking_json", side_effect=RuntimeError("synthetic failure")), patch.object(
                fetcher, "build_output_path", return_value=destination
            ):
                with self.assertRaises(RuntimeError):
                    fetcher.fetch_and_save("demo", "demo", "user", "fake")
            self.assertFalse(destination.exists())


    def test_password_is_passed_without_modification(self):
        app = fetcher.NezasaFetchApp.__new__(fetcher.NezasaFetchApp)
        for name, value in [
            ("channel_entry", "demo"), ("username_entry", "demo-user"),
            ("booking_entry", "demo-id"), ("password_entry", " password with spaces "),
        ]:
            setattr(app, name, Mock(get=Mock(return_value=value)))
        with patch.object(fetcher, "fetch_and_save", return_value=Path("demo.json")) as call, patch.object(
            fetcher.messagebox, "showinfo"
        ):
            app.on_fetch()
        self.assertEqual(call.call_args.kwargs["password"], " password with spaces ")

    def test_invalid_booking_responses_do_not_replace_existing_export(self):
        payloads = [
            None, [], {}, {"errors": []},
            {"data": {"type": "hotel", "id": "demo", "attributes": {}}},
            {"data": {"type": "booking", "id": "wrong", "attributes": {}}},
            {"data": {"type": "booking", "id": "demo"}},
            {"data": {"type": "booking", "id": "demo", "attributes": []}},
            {"data": {"type": "booking", "id": "demo", "attributes": {}}, "included": {}},
        ]
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "booking_demo.json"
            previous = b'{"previous": "valid export"}'
            for payload in payloads:
                with self.subTest(payload=payload):
                    target.write_bytes(previous)
                    client = self.client(self.response(payload=payload))
                    with patch.object(fetcher, "load_requests_modules", return_value=(client, Mock())), patch.object(
                        fetcher, "build_output_path", return_value=target
                    ):
                        with self.assertRaises(RuntimeError):
                            fetcher.fetch_and_save("demo", "demo", "user", "fake")
                    self.assertEqual(target.read_bytes(), previous)

    def test_write_failure_preserves_previous_export_and_cleans_temp(self):
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "booking_demo.json"
            previous = b'{"previous": "valid export"}'
            target.write_bytes(previous)
            with patch.object(fetcher.json, "dump", side_effect=OSError("simulated write failure")):
                with self.assertRaises(OSError):
                    fetcher.save_booking_json({"new": "value"}, target)
            self.assertEqual(target.read_bytes(), previous)
            self.assertEqual(list(Path(temp).iterdir()), [target])

    def test_replace_failure_preserves_previous_export_and_cleans_temp(self):
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "booking_demo.json"
            previous = b'{"previous": "valid export"}'
            target.write_bytes(previous)
            with patch.object(fetcher.os, "replace", side_effect=PermissionError("simulated lock")):
                with self.assertRaises(PermissionError):
                    fetcher.save_booking_json({"new": "value"}, target)
            self.assertEqual(target.read_bytes(), previous)
            self.assertEqual(list(Path(temp).iterdir()), [target])

    def test_successful_save_replaces_previous_export(self):
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "booking_demo.json"
            target.write_text('{"previous": true}', encoding="utf-8")
            payload = {"data": {"type": "booking", "id": "demo", "attributes": {"note": "äöü"}}}
            fetcher.save_booking_json(payload, target)
            self.assertEqual(json.loads(target.read_text(encoding="utf-8")), payload)
            self.assertEqual(list(Path(temp).iterdir()), [target])

if __name__ == "__main__":
    unittest.main()
