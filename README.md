# Check In Check Out

Aus Nezasa-Buchungen editierbare Word-Reiseunterlagen für Sales / Travel Agents erstellen. Dieses Repository enthält Entwicklungscode, bereinigte Testdaten und die dafür nötige Dokumentation.

## Aktueller Stand · 22.10.2026

| Bereich | Stand |
| --- | --- |
| MVP-Ziel | Direkter Nezasa-Abruf in der finalen Anwendung → strukturiertes DOCX → manuelle Finalisierung in Word. Termin: **Ende Dezember 2026**. |
| Vorhandener Code | Python-/Tkinter-Fetcher für JSON-Testdaten, mit Offline-Tests. Die API funktioniert laut Nutzerbestätigung. |
| Noch zu bauen | Finale Anwendung mit eigenem Abruf, Verarbeitung, Inhaltsintegration und DOCX-Erzeugung. Ihr Stack ist offen. |
| Fetcher-Rolle | Ausschliesslich Entwicklung; erzeugt nur JSON und wird final nicht benötigt. |
| Azure | STC-Inhaltsablage für Bilder, Hinweise und Querverweise angefordert. Konkreter Entwurf vorhanden, noch nicht bereitgestellt. |
| Nächste fachliche Grundlage | Akzeptierte Word-Zielvorlage, Pflichtinhalte/Sprachen sowie Tages- und Statusregeln festlegen. |

Die aktuelle Grundlage ist in [MVP](docs/MVP.md) konkretisiert; die Herkunft der Entscheidungen steht im [Quellenregister](docs/concepts/SOURCES_AND_DECISIONS.md).

## Schnell einsteigen

1. [Entwicklungsstart](docs/DEVELOPMENT.md): Einrichtung, Tests, Code-Einstieg und Arbeitsablauf.
2. [Beispielkatalog](examples/README.md): passende JSONs direkt öffnen; Grenzen der Testdaten erkennen.
3. [Offene Entscheidungen](docs/OPEN_DECISIONS.md): sehen, was den nächsten Umsetzungsschritt tatsächlich blockiert.

| Aufgabe | Gezielt weiterlesen |
| --- | --- |
| Nezasa-JSON verstehen | [Buchungsbeispiele](examples/nezasa/README.md), [Fetcher-Verhalten](components/nezasa-fetcher/docs/TECHNICAL_SPECIFICATION.md) |
| Inhalte / Package-Zuordnung integrieren | [Inhaltsvertrag – Entwurf](docs/CONTENT_STRUCTURE.md), [Inhaltsbeispiel](examples/content/README.md) |
| Azure einrichten | [IT-Einrichtungsgrundlage](docs/AZURE_IT_SETUP.md) |
| Mit einem AI-Coder arbeiten | [AGENTS.md](AGENTS.md) |
| Fachlichen Hintergrund nachlesen | [Konzepte und Quellen](docs/concepts/README.md) |
| Review-Ergebnis nachvollziehen | [Repository-Review](docs/reviews/2026-10-22.md) |

## Testdaten sofort finden

- [Buchung 01](examples/nezasa/booking_example_01.json): 2 Reisende, 14 Komponenten.
- [Buchung 02](examples/nezasa/booking_example_02.json): 4 Reisende, 23 Komponenten.
- [Buchung 03](examples/nezasa/booking_example_03.json): Englisch, 5 Reisende mit Kindern, 19 Komponenten.
- [Buchung 04](examples/nezasa/booking_example_04.json): Englisch, 2 Reisende, 17 Komponenten.
- [Buchung 05](examples/nezasa/booking_example_05.json): Französisch, 4 Reisende mit Kindern, 4 Komponenten.
- [Buchung 06](examples/nezasa/booking_example_06.json): Deutsch, 3 Reisende, 8 Komponenten und Zahlungstransaktion.
- [Inhalts-Release](examples/content/README.md): synthetischer Katalog und Package-Mapping, getrennt von den Buchungsbeispielen.

Alle sechs Buchungen enthalten auch offene Leistungen. Preise und personenbezogene Angaben sind synthetisch; die Dateien sind keine Referenz für kaufmännische Berechnungen. Reale Fetcher-Exporte und Zugangsdaten gehören nicht ins öffentliche Git.
