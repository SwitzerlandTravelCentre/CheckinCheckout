# Inhaltsstruktur und Querverweise

Stand: 22.10.2026. **Vorgeschlagener Vertrag v1**, fachlich noch zu bestätigen. Ergänzung zu [Azure IT-Setup](AZURE_IT_SETUP.md).

## Datenbereiche

| Inhalt | Ort | Zweck |
| --- | --- | --- |
| Bilder | releases/<release-id>/images/<asset-id>/<datei> | Stabile Referenz auf eine konkrete Bildversion. |
| Hinweise | catalog.json, Abschnitt hints | Sprachabhängige redaktionelle Hinweise; keine Kundendaten. |
| Packages | catalog.json, Abschnitt packages | Interne, quellsystemunabhängige Package-IDs. |
| Querverweise | mappings.json | Explizite Zuordnung einer Nezasa-Referenz zu einem internen Package. |
| Integritätsdaten | manifest.json | Dateiliste, SHA-256, Schema- und Release-Version. |
| Aktive Freigabe | control/current.json | Verweis auf genau ein gültiges Release. |

Buchungs-JSONs, Kundendaten, generierte DOCX/PDF und Secrets gehören nicht in diese Inhaltscontainer. Falls ihre Speicherung später benötigt wird, sind separate Ressourcen, Rollen und Aufbewahrungsregeln festzulegen. Nezasa-JSONs bleiben unverändert; die Anreicherung findet in einer getrennten internen Verarbeitung statt.

## IDs und Dateien

IDs sind dauerhaft, technisch und unabhängig von Anzeigenamen, etwa pkg-demo-classic, hint-demo-arrival und img-demo-lake. Produkt-, Hotel- oder Package-Namen sind keine Schlüssel.

Dateipfade verwenden Kleinbuchstaben, Ziffern, Bindestriche und Schrägstriche. Keine absoluten Pfade, ".."-Segmente, SAS-Tokens oder beliebige externe URLs im Katalog. Pfade im Manifest und Bildkatalog sind relativ zur jeweiligen Release-Wurzel.

JSON-Dateien: UTF-8, Content-Type application/json. Bilder: passender MIME-Type; zunächst JPEG/PNG. Keine ungeprüften aktiven Dateiformate. Bildquelle, Nutzungsrecht, gültige Einsatzgrenzen und Alternativtexte je Sprache im Katalog pflegen. Vor Veröffentlichung muss der Publisher eine echte Bilddatei samt Prüfsumme prüfen.

## Querverweis: welche Referenz gehört zu welchem Package?

Ein Mapping-Schlüssel besteht aus:

- sourceSystem: zunächst nezasa.
- sourceNamespace: Datenraum / Mandant. Vorgeschlagener Wert aus data.attributes.tourOperator; tatsächliche Eindeutigkeit mit Nezasa bestätigen.
- referenceType: der genaue semantische Pfad, etwa booking.templateRefId oder booking.modules[].refId.
- referenceValue: exakter String aus der Buchung; nicht über Name oder Teilstring vergleichen.

Dazu gehört genau eine interne packageId. **Offen:** Welche Nezasa-Referenz das Package verbindlich identifiziert. Die Beispiele enthalten sowohl Template- als auch Modulreferenzen. Ihre fachliche Bedeutung und Kardinalität sind noch zu bestätigen; gleich aussehende IDs sind kein Beweis für das gleiche Package.

Vorgeschlagene Auflösung: explizites Modul-Mapping vor Template-Fallback. Unterschiedliche Module einer Buchung werden einzeln zugeordnet; ein Treffer darf nicht pauschal alle Module ersetzen. Mehrdeutige oder widersprüchliche Einträge sind ein Validierungsfehler. Ohne Treffer keine Zuordnung raten; die Anwendung gibt einen sichtbaren Hinweis zur manuellen Bearbeitung aus. Diese Vorrangregel ist ein Vorschlag, keine aus Nezasa abgeleitete Garantie.

## Inhaltssprache und Darstellung

hints enthalten lokalisierte title- und body-Werte sowie einen stabilen fachlichen Typ. Für v1 einfacher Text; Formatierung übernimmt das spätere DOCX-Template. Fachlich verbindliche Daten wie gebuchte Zeiten und Leistungen werden nicht durch Hinweise überschrieben.

Vorgeschlagenes Sprachverhalten: Sprache der Buchung exakt verwenden. Für verpflichtende Hinweise führt eine fehlende Übersetzung zur manuellen Klärung; optionale Hinweise dürfen mit sichtbarer Diagnose fehlen. Kein stiller Sprachwechsel. Weitere Fallback-Regeln sind fachlich festzulegen.

packages verweisen über hintIds und imageIds auf den Katalog. Reihenfolge in diesen Listen ist die vorgeschlagene Darstellungsreihenfolge. Auswahlregeln nach Reisedatum, Saison, Zielgruppe oder Komponententyp sind noch kein Teil des Basisvertrags.

## Mindestvalidierung bei Freigabe

- Unterstützte schemaVersion und gleiche releaseId in Manifest, Katalog und Mapping.
- Eindeutige IDs je Bereich; gültige Package-, Hinweis- und Bildreferenzen.
- Jeder vollständige Mapping-Schlüssel ist eindeutig.
- Jedes Bild und jede im Manifest genannte Datei existiert und erfüllt SHA-256 und Content-Type.
- Alle vom Release benötigten Dateien sind im Manifest erfasst, ausser manifest.json selbst.
- current.json nennt eine existierende Manifest-Datei und deren SHA-256.
- Keine personenbezogenen Inhalte, produktiven Tokens oder unzulässigen Pfade in Inhaltsdaten.
- Erforderliche Übersetzungen und Bildrechte sind vorhanden.

Pro Verarbeitungsvorgang einmal current.json laden, dann Manifest und alle Inhalte aus genau diesem Release lesen. Bei fehlerhafter Integrität Vorgang mit klarer Diagnose anhalten. Ein optionaler Cache wird nach Release-ID geführt, nicht als unabhängiger „neuester“ Stand je Datei. Offline-Fallback auf einen früheren Stand muss bewusst freigegeben und protokolliert werden.

## Rollenverteilung

IT stellt Storage, Netz, Identitäten, Rollen, Wiederherstellung und Monitoring bereit. Fachverantwortliche pflegen Inhalte und bestätigen Referenzbedeutung, Sprachregeln und Bildrechte. Entwicklung implementiert Abruf, Validierung, Mapping, Cache und Fehlerbehandlung. Ein technischer Publisher setzt den Freigabeablauf um; seine konkrete Oberfläche und technische Umsetzung sind noch offen.

Siehe [synthetisches Beispiel](../examples/content/README.md). Die Beispieldateien zeigen den Vertragsentwurf und sind noch keine Schema-validierte Produktionsschnittstelle.
