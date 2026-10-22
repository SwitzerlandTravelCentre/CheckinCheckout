# Herkunft der Komponente

- Quelle: [SwitzerlandTravelCentre/NezasaToWord](https://github.com/SwitzerlandTravelCentre/NezasaToWord)
- Upstream-Branch: `main`
- Übernommener Commit: `2920216ffbdd647cf6e5f06caaec79b0cb45db3c`
- Aufgenommen am: 22.10.2026
- Methode: eingebettete Quellkopie, kein Submodul und keine automatische Synchronisation.

## Lokale Änderungen

- Passwort einschliesslich Leerzeichen unverändert übergeben.
- Abhängigkeitshinweis auf die zentrale Setup-Anleitung korrigiert; Modulbeschreibung macht keine Zusage zum Leistungsstatus.
- Minimale Buchungshülle und angefragte ID vor dem Speichern prüfen.
- Export über temporäre Datei mit atomarem Ersetzen speichern.
- README und technische Spezifikation für den Entwicklungs-Fetcher konsolidiert. Die lokale Spezifikation beschreibt den aktuellen Code; frühere Upstream-Dateilimits und Verbesserungsvorschläge sind keine Projektvorgaben.
- Projektintegration und Setup sind in [FETCHER_INTEGRATION.md](../../docs/FETCHER_INTEGRATION.md) und [DEVELOPMENT.md](../../docs/DEVELOPMENT.md) dokumentiert; Tests liegen im Hauptrepository.

## Ursprüngliche Upstream-Dateien

Diese Git-Blob-Hashes identifizieren den ursprünglichen Import. Sie sind keine Prüfsummen des inzwischen geänderten lokalen Stands.

| Datei | Upstream Git-Blob-SHA |
| --- | --- |
| app/nezasa_fetch_ui.py | 398eb29b42ee5093627b406eaae79fe9c6010bd2 |
| docs/TECHNICAL_SPECIFICATION.md | 99a94cddc06f4b18cb227360302c4de617c9f9d8 |
| .gitignore | 961675878f681c91e84ec0ee5796d553748172f1 |
| .gitattributes | 5be0da3683b7f201d74f81290a3597643a7fd8f8 |
| README.md | fba9acb7a053b188f46ebf8dad0cdbc01657ffd7 |
| SECURITY.md | f71446e99405b96258b8d0cd2dc2f81c49999942 |
| requirements.txt | 0eb8cae7f9083d1b4e70d94cbd6ac82cd63476d9 |

Bei späteren Updates einen konkreten Upstream-Commit auswählen, Unterschiede einschliesslich lokaler Korrekturen prüfen, Herkunft aktualisieren und Offline-Tests ausführen. Keine automatische Übernahme eines unbekannten Upstream-Stands.
