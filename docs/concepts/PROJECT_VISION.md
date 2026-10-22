# Projektvision und fachlicher Hintergrund

Zusammenfassung von S1/S2; aufgenommen am 22.10.2026. [Herkunft und spätere Entscheidungen](SOURCES_AND_DECISIONS.md). Diese Seite beschreibt Kontext, keine freigegebene Implementierungsspezifikation. Der aktuelle Lieferumfang steht im [MVP](../MVP.md).

## Problem

Individuelle Touring-Reisen verbinden mehrere Tage, Orte, Hotels, Transportabschnitte und Sonderbedingungen. Eine reine Wiedergabe der Buchungsstruktur erklärt die Reise aus Kundensicht nicht immer ausreichend.

Das Konzept beschreibt einen instabilen HTML-to-Word-Export aus Nezasa: Tabellen, Abstände und Absatzformate erschweren schon kleine Änderungen. Die regelmässig zu entfernende „Check-in / Check-out“-Zeile ist das namensgebende Beispiel. Der bestehende Export dient als Problembeschreibung, nicht als Zielvorlage.

Das ursprüngliche Ziel von bis zu 80 % weniger Finalisierungsaufwand ist nicht gemessen. Die spätere Management-Einschätzung geht zunächst von ungefähr 50 % aus; siehe [MVP](../MVP.md). Ein Zeitgewinn darf nicht auf Kosten fehlender Reiseinformationen bewertet werden.

## Begriffe

| Begriff | Bedeutung |
| --- | --- |
| Travel Docs / Reiseablauf | Hauptunterlagen für Vorbereitung, Buchungsbestätigung und Orientierung während der gesamten Reise. |
| Reisedossier | Travel Docs zusammen mit Tickets, Vouchern, Reservierungen und weiteren Bestätigungen. |
| Travel Agent / Sales | Prüft, korrigiert, ergänzt und finalisiert die Word-Unterlagen. |
| Redaktionelle Inhalte | Ergänzende Bilder und Hinweise mit nachvollziehbarer Quelle; sie ändern keine Buchungsfakten. |
| Beyond PDF | Zurückgestellte Vision einer zentralen Lösung für B2B, B2C, Groups und weitere Beteiligte. |

## Fachliches Beispiel: ein Reisetag

Ein Gast übernachtet in A, reist morgens nach B und übernachtet dort. Eine Überschrift nur mit B kann den Ablauf unverständlich machen. Das Konzept schlägt „A nach B“ vor, abgeleitet aus Transporten, Zeitpunkten und Übernachtungen.

Dies ist ein Regelbeispiel, kein Algorithmus: Mehrere Transporte, Rundreisen, Tagesausflüge, Nachtfahrten und fehlende Zeitangaben brauchen eigene Entscheidungen. Ebenso sind mehrere Zimmer desselben Hotels nicht automatisch doppelte Leistungen.

## Langfristige Verantwortlichkeiten

| Bereich | Gedachte Aufgabe |
| --- | --- |
| Buchungsdaten | Gebuchte Leistungen strukturiert bereitstellen; Nezasa zuerst. |
| Analyse und Anreicherung | Daten konsolidieren, Lücken/Widersprüche erkennen, zusätzliche Inhalte und später AI-Prüfungen ergänzen. |
| Personalisierung | Informationsdichte und Darstellung am Kundenkontext ausrichten. |
| Bearbeitung und Kontrolle | Word-Draft erzeugen und durch Travel Agents finalisieren. |
| Ausspielung | Finalisierte Inhalte passend zu PDF, E-Mail, Website oder App bereitstellen. |

Diese Verantwortlichkeiten begründen keine Microservices, Datenbank oder bestimmte Bibliothek. Die Anwendung soll erweiterbar bleiben, ohne die Zukunftsvision vorzeitig umzusetzen.

Spätere Quellenideen sind Karten, Bilder, saisonale Informationen, ST-Inhalte, zusätzliche Prüfkriterien, Kundenprofile und eine mobile Website. Konkrete Drittanbieterintegrationen und Regeln sind nicht beschlossen.

## Ungelöste Zukunftsfragen

Word soll frei bearbeitbar sein; für weitere Kanäle wird zugleich konsistenter Inhalt angestrebt. Wie manuelle Änderungen in eine gemeinsame Datenbasis zurückfliessen, ist ungelöst. Ein DOCX-Roundtrip oder eine Synchronisation ist nicht zugesagt.

Nach dem operativ nutzbaren MVP soll der weitere Ausbau besprochen werden. Die organisatorische Abgrenzung zu „Beyond PDF“ bleibt offen. Historische Monatspläne aus den Konzepten wurden nicht als aktuelle Roadmap übernommen.
