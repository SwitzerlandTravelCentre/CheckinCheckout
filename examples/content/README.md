# Beispiel für Inhaltsablage

Synthetischer Entwurf für [Inhaltsstruktur](../../docs/CONTENT_STRUCTURE.md) und [IT-Einrichtung](../../docs/AZURE_IT_SETUP.md). Enthält keine echten Nezasa-Package-Zuordnungen.

- control/current.json verweist auf releases/demo-001/manifest.json.
- manifest.json enthält SHA-256 für catalog.json und mappings.json.
- catalog.json enthält ein Beispiel-Package und einen Hinweis in Deutsch und Englisch.
- mappings.json zeigt eine fiktive Modulreferenz.
- Der Bildbereich ist bewusst leer: Bilddateien, Rechte und Alternativtexte werden später gemeinsam ergänzt. Für den IT-Abnahmetest ist ein genehmigtes Testbild zu ergänzen und das Manifest neu zu erzeugen.

Die relativen Pfade und Prüfsummen dieses Mini-Releases sind lokal geprüft. Es wurde nicht auf Azure veröffentlicht. Ein formales JSON Schema, ein automatisierter Publisher und der Anwendungsadapter sind noch zu implementieren.
