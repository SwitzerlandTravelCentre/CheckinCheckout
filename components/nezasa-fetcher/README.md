# Nezasa JSON-Fetcher

Entwicklungstool zum Abrufen von JSON-Testdaten aus Nezasa. Die finale CheckinCheckout-Anwendung integriert ihren Abruf selbst und erzeugt direkt Word; dieser Desktop-Fetcher gehört nicht zum Produktionsablauf.

| Aufgabe | Einstieg |
| --- | --- |
| Einrichten, starten und offline testen | [Entwicklungsanleitung](../../docs/DEVELOPMENT.md) |
| API, Eingaben, Dateiablage und Fehler verstehen | [Technische Referenz](docs/TECHNICAL_SPECIFICATION.md) |
| Code ändern | [app/nezasa_fetch_ui.py](app/nezasa_fetch_ui.py) |
| Vorhandene Testdaten nutzen | [Nezasa-Beispiele](../../examples/nezasa/README.md) |
| Projektgrenze und Betrieb einordnen | [Fetcher-Integration](../../docs/FETCHER_INTEGRATION.md) |
| Herkunft und lokale Änderungen nachvollziehen | [UPSTREAM.md](UPSTREAM.md) |
| Daten für das öffentliche Repository vorbereiten | [SECURITY.md](SECURITY.md) |

Der Fetcher speichert reale Buchungsdaten lokal. Er anonymisiert weder Personen noch Preise. Öffentliche Beispiele werden separat bereinigt; keine Roh-Exporte oder Zugangsdaten ins Git übernehmen.
