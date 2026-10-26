# Offene Entwicklungsentscheidungen

Stand: 26.10.2026. Nur offene Punkte; bestätigte Entscheidungen stehen in [README](../README.md) und [Quellenregister](concepts/SOURCES_AND_DECISIONS.md). Zuständigkeiten werden ausschliesslich als Rollen beschrieben. Die fachliche Abnahme liegt bei B2C; operative Inhaltspflege und Freigabeablauf bleiben zu konkretisieren.

## Vor dem ersten fachlich abnehmbaren DOCX

| ID | Benötigte Entscheidung / Material | Zuständigkeit | Blockiert |
| --- | --- | --- | --- |
| D01 | Aktuelle Word-Inhaltsvorlage prüfen und als Zielvorlage freigeben; Word-Version, typische manuelle Änderungen und Abnahmekriterien mit B2C bestätigen. Template-Datei ist noch nicht im Repository. | B2C / Projekt | Template, Layout und belastbare Word-Abnahme. |
| D02 | Pflichtinhalte, Sprachen, Reisearten und Inhalte des ersten MVP festlegen. | Sales / Projekt | Vollständiges Mapping und repräsentative Testfälle. |
| D03 | Regeln für Reisetage, Zeitzonen, Transporte, Check-in/out sowie offene/stornierte/unvollständige Leistungen und fehlende Daten. | Sales / Entwicklung | Fachlich korrekte automatische Darstellung. |

## Vor Integration und Betrieb

| ID | Benötigte Entscheidung / Material | Zuständigkeit | Blockiert |
| --- | --- | --- | --- |
| D04 | Vorhandenen Lösungsstand technisch übergeben: Stack, Ausführungsort, Benutzerzugriff, Produktions-Nezasa-Zugang, Dokumentübergabe und Speicherung/Aufbewahrung dokumentieren und für den Betrieb bestätigen. | Entwicklung / IT / Projekt | Finale Anwendung, privater Azure-Netzpfad und Betrieb. |
| D05 | Verbindliche Package-Referenz, Mandanten-Namespace, Kardinalität und Vorrang bei mehreren Modulen bestätigen. | Fachverantwortung / Nezasa / Entwicklung | Reale Querverweise; synthetische Beispiele sind keine Zuordnungsvorlage. |
| D06 | Ergänzungsfelder sind abgegrenzt (S14). Konkrete Texte/Bilder, Sprachen, Pflege, Freigabe und endgültigen Datenvertrag bestätigen; produktiven Abruf/Validierung umsetzen. | Fachverantwortung / Entwicklung | Veröffentlichbare Inhalts-Releases und vollständiger IT-Abnahmetest. |
| D07 | Subscription/Region, Netzwerk, Identitäten, Betriebskontakte, Budget, Aufbewahrung und RPO/RTO bestätigen. | IT | Produktive Azure-Einrichtung nach [IT-Entwurf](AZURE_IT_SETUP.md). |
| D08 | Unterstützten Nezasa-Datenvertrag und Umgang mit Änderungen festlegen; technische Fehlerprotokollierung und Supportablauf definieren. | Entwicklung / IT | Belastbarer Produktionsadapter und Fehlerdiagnose. |
| D10 | Saison-Grenzen, Reisen über mehrere Saisons, verlässliche Anreisequelle und fehlende Werte festlegen; vorläufige Gotthard-Bildpriorität bestätigen. | Fachverantwortung / Entwicklung | Eindeutige Inhalts- und Bildauswahl. |
| D11 | Bei Anbindung einer Drittquelle: Zuständigkeit je Ergänzungsfeld, Nutzungsrechte, Rückgabeformat und Ausfallfallback bestimmen. | Entwicklung / Fachverantwortung | Nur die jeweilige spätere Drittquellenintegration. |

## Vor Pilotabschluss

| ID | Benötigte Entscheidung / Material | Zuständigkeit | Blockiert |
| --- | --- | --- | --- |
| D09 | Vergleichsreisen, Ausgangsaufwand, Qualitätsmassstab und Messverfahren vereinbaren. | Sales / Projekt | Nachweis der geschätzten 50-%-Ersparnis. |

Fixture-Analyse, technische Prototypen und unabhängige Arbeiten können weiterlaufen. Fehlende Entscheidungen nicht als bereits bestätigte Regeln implementieren.

Spätere Themen: Personalisierung, weitere Kanäle, Rückführung manueller Word-Änderungen und Abgrenzung zu „Beyond PDF“ liegen im [Konzept](concepts/PROJECT_VISION.md). Sie blockieren den derzeitigen Entwicklungsstart nicht.

Die alten Q-/C-Referenzen sind im [Quellenregister](concepts/SOURCES_AND_DECISIONS.md) auf diese Liste abgebildet.
