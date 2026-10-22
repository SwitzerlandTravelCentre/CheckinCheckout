# Synthetisches Inhaltsrelease

Kleines, eigenständiges Beispiel zum vorgeschlagenen [Inhaltsvertrag](../../docs/CONTENT_STRUCTURE.md) und [Azure-Setup](../../docs/AZURE_IT_SETUP.md). Es ist lokal gespeichert und wurde nicht auf Azure veröffentlicht. [Zur Beispielübersicht](../README.md).

| Datei | Zweck |
| --- | --- |
| [control/current.json](control/current.json) | Aktives Release `demo-001`; Pfad und SHA-256 des Manifests. |
| [manifest.json](releases/demo-001/manifest.json) | Liste und SHA-256 von Katalog und Mapping; Dateipfade relativ zur Release-Wurzel. |
| [catalog.json](releases/demo-001/catalog.json) | Ein Package und ein optionaler Hinweis in Deutsch und Englisch; Bildliste leer. |
| [mappings.json](releases/demo-001/mappings.json) | Eine fiktive Modulreferenz, die dem Beispiel-Package zugeordnet ist. |

Leseablauf: `current.json` → Manifest und dessen Prüfsumme → aufgeführte Dateien und deren Prüfsummen → referenzierte Package-/Hinweis-IDs prüfen. Alle Inhalte eines Vorgangs stammen aus demselben Release. Der Manifestpfad in `current.json` ist relativ zur Inhaltswurzel; die Dateipfade im Manifest sind relativ zum Release-Verzeichnis.

## Grenzen des Beispiels

- Die Mapping-Referenz ist **nicht mit den Nezasa-Beispielbuchungen verknüpft**. Die fachliche Nezasa-Referenz für Packages und die Auflösungsregel sind noch zu bestätigen.
- `referenceType=booking.modules[].refId` ist ein semantischer Bezeichner im Vertragsentwurf, kein direkt ausführbarer JSON-Pfad. Im Nezasa-Beispiel liegen Module unter `data.attributes.modules[]`.
- Keine Bilddatei ist enthalten. Für den Bildabruf-/IT-Abnahmetest muss ein genehmigtes Testbild samt Rechten, Alternativtexten und Manifesteintrag ergänzt werden.
- Ein formales JSON Schema, ein automatisierter Publisher und der Anwendungsadapter fehlen noch. `schemaVersion=1.0` kennzeichnet den Entwurf und bedeutet keine freigegebene Produktionsschnittstelle.

Die bestehenden Pfade, Referenzen und SHA-256-Prüfsummen wurden lokal geprüft. Werden Katalog, Mapping oder Bilddateien geändert, muss zuerst das Manifest aktualisiert werden; danach dessen Prüfsumme in `current.json`. Unveränderte Beispiel-JSONs benötigen keine Neuberechnung.
