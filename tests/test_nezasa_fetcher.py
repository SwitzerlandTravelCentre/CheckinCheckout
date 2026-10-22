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
        payload = {"data": {"id": "demo"}, "included": [], "extra": {"note": "äöü"}}
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
        for source in sorted((ROOT / "examples/nezasa").glob("booking_example_*.json")):
            with self.subTest(example=source.name), tempfile.TemporaryDirectory() as temp:
                payload = json.loads(source.read_text(encoding="utf-8"))
                destination = Path(temp) / "nested" / source.name
                client = self.client(self.response(payload=payload))
                with patch.object(fetcher, "load_requests_modules", return_value=(client, Mock())), patch.object(
                    fetcher, "build_output_path", return_value=destination
                ):
                    output = fetcher.fetch_and_save("demo", "demo", "user", "fake")
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


if __name__ == "__main__":
    unittest.main()
