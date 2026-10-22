# Beispiele für die Entwicklung

Alle hier abgelegten Daten sind für das öffentliche Repository bereinigt oder vollständig synthetisch. Für Offline-Arbeit ist kein API-Zugang erforderlich.

| Aufgabe | Einstieg | Was enthalten ist |
| --- | --- | --- |
| Nezasa-Struktur verstehen, Parser beginnen | [Buchung 01](nezasa/booking_example_01.json) | 2 Reisende, 14 Komponenten; kleineres Beispiel. |
| Weitere Zimmer-/Leistungskonstellationen verarbeiten | [Buchung 02](nezasa/booking_example_02.json) | 4 Reisende, 23 Komponenten; mehr Unterkunftskomponenten und Zusatzleistungen. |
| Feldpfade und Grenzen der Buchungsbeispiele verstehen | [Nezasa-Lesehilfe](nezasa/README.md) | Struktur, Status, Anonymisierung und nicht abgedeckte Fälle. |
| Inhaltsabruf und Release-Prüfung entwickeln | [Inhaltsrelease](content/README.md) | Freigabezeiger, Manifest, Katalog und fiktives Package-Mapping. |
| Vorhandenen JSON-Export offline prüfen | [Fetcher-Tests](../tests/test_nezasa_fetcher.py) | HTTP-Simulation, vollständiger JSON-Roundtrip und Fehlerfälle. |

Die beiden Buchungen und das Inhaltsrelease sind **unabhängige Beispiele**. Die fiktive Mapping-Referenz des Inhaltsrelease passt nicht automatisch zu den Buchungen. Ein gemeinsames End-to-End-Beispiel muss später ausdrücklich erstellt werden.

Es gibt noch kein freigegebenes DOCX-Template und kein erwartetes Word-Ausgabedokument als Testreferenz. Die Buchungen sind keine vollständige Nezasa-Schemaspezifikation. Preise sind fiktiv und rechnerisch nicht abgestimmt.

## Umgang mit Beispielen

- Bestehende Buchungs-JSONs unverändert verwenden: Schlüssel, Datentypen, Container und Array-Reihenfolge erhalten. Abgeleitete Modelle getrennt erzeugen.
- Neue Fälle separat ergänzen und ihren Testzweck sowie ihre Grenzen dokumentieren. Fehlende Fälle nicht durch Umdeuten vorhandener Daten ersetzen.
- Reale Fetcher-Ausgaben zunächst ausserhalb des Repositorys halten und vollständig bereinigen; der Fetcher anonymisiert selbst nicht.
- Die [Git-Ignore-Regeln](../.gitignore) erlauben nur ausdrücklich aufgeführte JSON-Beispiele. Neue geprüfte Fixtures, Schemas oder Ausgabereferenzen benötigen eine gezielte Ausnahme; keine pauschale Freigabe von Rohdaten.

Weiter: [Entwicklungsablauf](../docs/DEVELOPMENT.md), [offene Entscheidungen](../docs/OPEN_DECISIONS.md).
