# Check In Check Out

Aus Nezasa-Buchungen editierbare Word-Reiseunterlagen für Sales / Travel Agents erstellen. Dieses Repository enthält Entwicklungscode, bereinigte Testdaten und die dafür nötige Dokumentation.

## Aktueller Stand · 26.10.2026

| Bereich | Stand |
| --- | --- |
| MVP-Ziel | B2C: direkter Nezasa-Abruf in der finalen Anwendung → strukturiertes DOCX → manuelle Finalisierung in Word. Termin: **Ende Dezember 2026**. |
| Rollen | Anwendungsentwicklung, IT-Betrieb und fachliche Abnahme durch B2C. Inhaltspflege und Freigabeablauf sind noch zu konkretisieren. |
| Vorhandener Code | Python-/Tkinter-Fetcher für JSON-Testdaten, mit Offline-Tests. Die API funktioniert laut Nutzerbestätigung. |
| Anwendungsstand | Export-Prototypen und interne Tests sind laut Projektangaben vorhanden; eine Word-Inhaltsvorlage dient der weiteren fachlichen Prüfung. Anwendungscode ist in diesem Repository nicht enthalten. Operative Abnahme und dokumentierte technische Übergabe stehen aus. |
| Fetcher-Rolle | Ausschliesslich Entwicklung; erzeugt nur JSON und wird final nicht benötigt. |
| Azure | Schlanke Ergänzung für redaktionelle Texte und Bilder. Nezasa bleibt die Hauptquelle; keine manuelle Pflege von Buchungsfakten auf Azure. Bereitstellung noch nicht bestätigt. |
| Nächste fachliche Grundlage | Aktuellen Template-Export fachlich prüfen und durch B2C freigeben; verbleibende Pflichtinhalte/Sprachen sowie Tages- und Statusregeln bestätigen. |

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

## Aktuelle Inhaltsarchitektur

Die Anwendung liest Nezasa und ergänzt ausschliesslich ausgewählte redaktionelle Variablen. Inhalte werden nach Produkt, Saison und Anreise ausgewählt; spätere Drittquellen können einzelne Ergänzungsfelder übernehmen. [Quellen, Auswahlregeln und Grenzen](docs/CONTENT_STRUCTURE.md). Die öffentlichen v1-Beispiele zeigen weiterhin nur den früheren Release-Vertrag, keine fertige Implementierung dieser Regeln.

## Testdaten sofort finden

- [Buchung 01](examples/nezasa/booking_example_01.json): 2 Reisende, 14 Komponenten.
- [Buchung 02](examples/nezasa/booking_example_02.json): 4 Reisende, 23 Komponenten.
- [Buchung 03](examples/nezasa/booking_example_03.json): Englisch, 5 Reisende mit Kindern, 19 Komponenten.
- [Buchung 04](examples/nezasa/booking_example_04.json): Englisch, 2 Reisende, 17 Komponenten.
- [Buchung 05](examples/nezasa/booking_example_05.json): Französisch, 4 Reisende mit Kindern, 4 Komponenten.
- [Buchung 06](examples/nezasa/booking_example_06.json): Deutsch, 3 Reisende, 8 Komponenten und Zahlungstransaktion.
- [Inhalts-Release](examples/content/README.md): synthetischer Katalog und Package-Mapping, getrennt von den Buchungsbeispielen.

Alle sechs Buchungen enthalten auch offene Leistungen. Preise und personenbezogene Angaben sind synthetisch; die Dateien sind keine Referenz für kaufmännische Berechnungen. Reale Fetcher-Exporte und Zugangsdaten gehören nicht ins öffentliche Git.
