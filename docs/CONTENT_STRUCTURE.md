# Inhaltsstruktur und Querverweise

Stand: 26.10.2026. Fachliches Zielkonzept nach S14–S15; konkrete Schnittstellen und Betrieb sind noch abzustimmen. Ergänzung zu [Azure IT-Setup](AZURE_IT_SETUP.md).

## Nezasa als Hauptquelle, Azure als Ergänzung

Die Anwendung liest das Nezasa-Buchungs-JSON als zentralen Quelldatensatz. Azure liefert nur wiederverwendbare redaktionelle Texte und Bilder für ausdrücklich benannte Ergänzungsfelder. Keine Buchungs-JSONs, Kundendaten, Preise oder separat gepflegten Tagesprogramme auf Azure ablegen. Fehlende Buchungsfakten werden sichtbar behandelt und nicht in einer zweiten Datenquelle nachgepflegt.

| Ergänzungsfeld | Inhalt / Pflegeumfang |
| --- | --- |
| welcome_text | Allgemeines Willkommen mit gezielten Varianten; logischer Name, endgültige Word-Bindung noch zu bestätigen. |
| preparations | Wiederverwendbare Vorbereitungshinweise einschliesslich allgemeiner Anreisehinweise. |
| hero_image | Redaktionelles Hauptmotiv mit Saisonversionen. |
| day.destination.description, day.destination.image_url | Ortsbeschreibung und Ortsbild nur bei Bedarf; keine Kopie der gebuchten Orte. |
| day.day_description | Optionaler redaktioneller Baustein; der konkrete Tagesablauf wird weiterhin aus der Buchung abgeleitet. |
| item.image_url | Optionales Leistungsbild; keine zweite Pflege der Leistung. |

Buchungsnummer, Gäste, gebuchte Hotels/Leistungen, Termine, Preise, Tickets und Reservierungsinformationen kommen aus Nezasa. Auch Adressen, Check-in/out, inkludierte Leistungen und Betreiberangaben sind gemäss Quellenentscheidung dort zu verarbeiten; die tatsächliche Feldverfügbarkeit und Semantik müssen geprüft werden. Fehlende Felder begründen keine automatische Azure-Erweiterung. Kartenlinks sind für eine Drittquelle vorgesehen; die verlässliche Buchungsquelle für Kontakte ist noch zu bestätigen.

## Einfache Inhaltsstruktur

Allgemeine Basis je Sprache + kleine Produktdateien mit ausschliesslich abweichenden Feldern. Saison und Anreise sind Varianten innerhalb eines Inhaltsdokuments, keine separaten Produktkopien. Bilder haben einen eigenen Katalog; eine schlanke Referenzzuordnung verbindet bestätigte Quellreferenzen mit dem Inhaltsprofil. Technische Schemas und Tests bleiben beim Consumer; Versions- und Prüfinformationen werden automatisch erzeugt.

Weitere Orts-/Leistungsbausteine erst anlegen, wenn sie benötigt werden. Dauerhafte IDs verwenden und Inhalte wiederverwenden. Ein zweites Buchungssystem, eine zusätzliche Inhaltsdatenbank oder ein KI-Dienst auf Azure sind für diese Ablage nicht erforderlich.

## Produkt- und Variantenregeln

- Grand Train Tour: enthält laut Fachdefinition GEX und BEX.
- Kürzere Panoramareise: GEX und/oder BEX ohne Grand Train Tour.
- Packages ohne Panoramazüge: One Center; Ski ist ein Merkmal ohne Züge.
- Grand Tour: Autoreise ohne Züge.
- GoldenPass/Gotthard ohne GEX/BEX müssen als Auswahlfälle möglich sein; ihre konkrete Produktzuordnung ist noch zu bestätigen.

Textauswahl: allgemeine Basis → allgemeine Saison → allgemeine Anreise → allgemeine Kombination → Produktbasis → Produktsaison → Produktanreise → Produktkombination. Nur vorhandene Felder überschreiben. Damit hat das Produkt Vorrang vor allgemeinen Varianten; innerhalb einer Ebene hat Anreise Vorrang vor Saison und die kombinierte Variante den höchsten Vorrang. Vorbereitungen nach stabiler Themen-ID zusammenführen, nicht doppelt anhängen.

Fehlt eine passende Variante, bleibt der allgemeinere Inhalt erhalten. Fehlende Sprachversionen nicht still übersetzen. Saison-Grenzen, Reisen über mehrere Saisons und die verlässliche Quelle des Anreisegebiets sind offen; Sprache oder Nationalität ersetzen keine Anreiseinformation. Die Produktauswahl darf niemals einen Reservierungsstatus oder eine Abfahrtszeit erfinden.

Bildauswahl: GEX vor BEX vor GoldenPass. Gotthard danach ist vorläufig. Ohne Zug erhalten Auto-/Skireisen ihr eigenes Motiv; sonst Zermatt vor Luzern vor neutralem Schweiz-Bild. Zuerst das Motiv bestimmen, dann dessen Saisonversion oder Standard wählen. Ein fehlendes GEX-Saisonbild führt nicht zu einem anderen Motiv. Europa/Übersee beeinflusst keine Bilder.

## Lesen und später Quellen ersetzen

1. Nezasa lesen und den Auswahlkontext aus verlässlichen Daten ableiten.
2. Einen freigegebenen Inhaltsstand laden und nur die passenden Ergänzungen auswählen.
3. Ausschliesslich die erlaubten Ergänzungsfelder setzen. Buchungsfakten bleiben unverändert.

Die Anwendung hält die Quelle je Ergänzungsfeld austauschbar. Beispielsweise kann später eine Drittquelle die Ortsbeschreibung liefern, während das Willkommen weiterhin aus Azure kommt. Logischer Variablenname und erwarteter Typ bleiben gleich. Priorität und Ausfallfallback werden je Feld festgelegt; Drittanbieter-Inhalte nicht zusätzlich manuell nach Azure kopieren. Diese Erweiterbarkeit ist ein Architekturauftrag, noch keine implementierte Drittanbieter-Anbindung.

## Einordnung der öffentlichen Beispiele

Die folgenden Pfade und [synthetischen Beispieldateien](../examples/content/README.md) beschreiben weiterhin den früheren **Vertragsentwurf v1**. Sie zeigen Release-Integrität und Referenzen, nicht die Umsetzung der oben beschriebenen Variantenregeln. Bestehende Fixtures bleiben unverändert; eine neue produktive Vertragsversion muss mit dem Consumer abgestimmt werden.


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

Dateipfade verwenden Kleinbuchstaben, Ziffern, Bindestriche und Schrägstriche sowie Punkte für Dateiendungen. Keine absoluten Pfade, ".."-Segmente, SAS-Tokens oder beliebige externe URLs im Katalog. Pfade im Manifest und Bildkatalog sind relativ zur jeweiligen Release-Wurzel.

JSON-Dateien: UTF-8, Content-Type application/json. Bilder: passender MIME-Type; zunächst JPEG/PNG. Keine ungeprüften aktiven Dateiformate. Bildquelle, Nutzungsrecht, gültige Einsatzgrenzen und Alternativtexte je Sprache im Katalog pflegen. Vor Veröffentlichung muss der Publisher eine echte Bilddatei samt Prüfsumme prüfen.

## Querverweis: welche Referenz gehört zu welchem Package?

Ein Mapping-Schlüssel besteht aus:

- sourceSystem: zunächst nezasa.
- sourceNamespace: Datenraum / Mandant. Vorgeschlagener Wert aus data.attributes.tourOperator; tatsächliche Eindeutigkeit mit Nezasa bestätigen.
- referenceType: der genaue semantische Pfad, etwa booking.templateRefId oder booking.modules[].refId.
- referenceValue: exakter String aus der Buchung; nicht über Name oder Teilstring vergleichen.

referenceType ist ein semantischer Bezeichner, kein ausführbarer JSON-Pfad. Für die vorhandenen Beispiele ist die technische Entsprechung:

| Bezeichner / Feld | JSON-Pfad in der Buchung |
| --- | --- |
| booking.templateRefId | data.attributes.templateRefId |
| booking.modules[].refId | data.attributes.modules[].refId |
| Vorgeschlagener sourceNamespace | data.attributes.tourOperator |

Diese Zuordnung erklärt die Schreibweise; sie bestätigt noch keine fachliche Package-Semantik.

Dazu gehört genau eine interne packageId. **Offen:** Welche Nezasa-Referenz das Package verbindlich identifiziert. Die Beispiele enthalten sowohl Template- als auch Modulreferenzen. Ihre fachliche Bedeutung und Kardinalität sind noch zu bestätigen; gleich aussehende IDs sind kein Beweis für das gleiche Package.

Vorgeschlagene Auflösung: explizites Modul-Mapping vor Template-Fallback. Unterschiedliche Module einer Buchung werden einzeln zugeordnet; ein Treffer darf nicht pauschal alle Module ersetzen. Mehrdeutige oder widersprüchliche Einträge sind ein Validierungsfehler. Ohne Treffer keine Zuordnung raten; die Anwendung gibt einen sichtbaren Hinweis zur manuellen Bearbeitung aus. Diese Vorrangregel ist ein Vorschlag, keine aus Nezasa abgeleitete Garantie.

## Inhaltssprache und Darstellung

hints enthalten lokalisierte title- und body-Werte sowie einen stabilen fachlichen Typ. Für v1 einfacher Text; Formatierung übernimmt das spätere DOCX-Template. Fachlich verbindliche Daten wie gebuchte Zeiten und Leistungen werden nicht durch Hinweise überschrieben.

Vorgeschlagenes Sprachverhalten: Sprache der Buchung exakt verwenden. Für verpflichtende Hinweise führt eine fehlende Übersetzung zur manuellen Klärung; optionale Hinweise dürfen mit sichtbarer Diagnose fehlen. Kein stiller Sprachwechsel. Weitere Fallback-Regeln sind fachlich festzulegen.

packages verweisen über hintIds und imageIds auf den Katalog. Reihenfolge in diesen Listen ist die vorgeschlagene Darstellungsreihenfolge. Die oben beschriebenen fachlichen Variantenregeln sind in diesen v1-Dateien noch nicht implementiert.

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

Siehe [synthetisches Beispiel](../examples/content/README.md). Die Beispieldateien zeigen den Vertragsentwurf und sind noch keine Schema-validierte Produktionsschnittstelle. Die Offline-Tests prüfen Dateiintegrität und Referenzen dieses Beispiels; ein Produktionsvalidator fehlt. Das Bildobjekt ist noch nicht konkret spezifiziert und images ist leer. Die fiktiven Mappings sind unabhängig von den Buchungsfixtures. Siehe [D05–D06](OPEN_DECISIONS.md) für die fehlenden Grundlagen.
