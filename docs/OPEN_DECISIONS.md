# Offene Entwicklungsentscheidungen

Stand: 22.10.2026. Nur offene Punkte; bestätigte Entscheidungen stehen in [README](../README.md) und [Quellenregister](concepts/SOURCES_AND_DECISIONS.md). Zuständigkeiten sind vorgeschlagene Rollen, noch keine benannten Verantwortlichen.

## Vor dem ersten fachlich abnehmbaren DOCX

| ID | Benötigte Entscheidung / Material | Zuständigkeit | Blockiert |
| --- | --- | --- | --- |
| D01 | Akzeptierte Word-Zielvorlage, problematisches bisheriges DOCX, Word-Version und typische manuelle Änderungen; fachlichen Abnehmer benennen. | Sales / Projekt | Template, Layout und belastbare Word-Abnahme. |
| D02 | Pflichtinhalte, Sprachen, Reisearten und Inhalte des ersten MVP festlegen. | Sales / Projekt | Vollständiges Mapping und repräsentative Testfälle. |
| D03 | Regeln für Reisetage, Zeitzonen, Transporte, Check-in/out sowie offene/stornierte/unvollständige Leistungen und fehlende Daten. | Sales / Entwicklung | Fachlich korrekte automatische Darstellung. |

## Vor Integration und Betrieb

| ID | Benötigte Entscheidung / Material | Zuständigkeit | Blockiert |
| --- | --- | --- | --- |
| D04 | Stack, Ausführungsort, Benutzerzugriff, Produktions-Nezasa-Zugang, Dokumentübergabe und Speicherung/Aufbewahrung wählen. Vorhandene weitere Prototypen benennen. | Entwicklung / IT / Projekt | Finale Anwendung, privater Azure-Netzpfad und Betrieb. |
| D05 | Verbindliche Package-Referenz, Mandanten-Namespace, Kardinalität und Vorrang bei mehreren Modulen bestätigen. | Fachverantwortung / Nezasa / Entwicklung | Reale Querverweise; synthetische Beispiele sind keine Zuordnungsvorlage. |
| D06 | Inhaltsumfang, Bildobjekt-Vertrag, genehmigtes Testbild, Sprachen, Pflege und Freigabe bestimmen; Schema/Publisher umsetzen. | Fachverantwortung / Entwicklung | Veröffentlichbare Inhalts-Releases und vollständiger IT-Abnahmetest. |
| D07 | Subscription/Region, Netzwerk, Identitäten, Betriebskontakte, Budget, Aufbewahrung und RPO/RTO bestätigen. | IT | Produktive Azure-Einrichtung nach [IT-Entwurf](AZURE_IT_SETUP.md). |
| D08 | Unterstützten Nezasa-Datenvertrag und Umgang mit Änderungen festlegen; technische Fehlerprotokollierung und Supportablauf definieren. | Entwicklung / IT | Belastbarer Produktionsadapter und Fehlerdiagnose. |

## Vor Pilotabschluss

| ID | Benötigte Entscheidung / Material | Zuständigkeit | Blockiert |
| --- | --- | --- | --- |
| D09 | Vergleichsreisen, Ausgangsaufwand, Qualitätsmassstab und Messverfahren vereinbaren. | Sales / Projekt | Nachweis der geschätzten 50-%-Ersparnis. |

Fixture-Analyse, technische Prototypen und unabhängige Arbeiten können weiterlaufen. Fehlende Entscheidungen nicht als bereits bestätigte Regeln implementieren.

Spätere Themen: Personalisierung, weitere Kanäle, Rückführung manueller Word-Änderungen und Abgrenzung zu „Beyond PDF“ liegen im [Konzept](concepts/PROJECT_VISION.md). Sie blockieren den derzeitigen Entwicklungsstart nicht.

Die alten Q-/C-Referenzen sind im [Quellenregister](concepts/SOURCES_AND_DECISIONS.md) auf diese Liste abgebildet.
