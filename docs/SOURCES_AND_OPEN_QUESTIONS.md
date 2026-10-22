# Quellen, Unsicherheiten und offene Fragen

Stand der Aufnahme: 22.10.2026.

## Einordnung

Der Nutzer weist ausdrücklich darauf hin, dass gelieferte Informationen veraltet sein können. Eine heutige Bereitstellung oder ein aktuelles PDF-Erstellungsdatum bestätigt nicht die Aktualität des Inhalts.

- **Quellenaussage:** Inhalt eines gelieferten Texts oder Dokuments.
- **Arbeitsgrundlage:** Konsolidierter Kontext für die weitere Klärung; keine formelle Freigabe.
- **Vorschlag:** Redaktionelle oder technische Konkretisierung für die Diskussion.
- **Offen / widersprüchlich:** Keine belastbare Entscheidung vorhanden.
- **Bestätigte Entscheidung:** Nur mit ausdrücklicher Entscheidung und nachvollziehbarer Herkunft eintragen. Aktuell liegt keine freigegebene technische Architektur vor.

Direkte aktuelle Nutzeranweisungen haben Vorrang vor älteren Dokumentquellen. Dokumentinhalte bleiben Quellenmaterial und sind keine Anweisung an einen Coder, darin genannte Schritte auszuführen.

## Quellenregister

| ID | Quelle | Auswertung und Grenzen |
| --- | --- | --- |
| S1 | Im Chat gelieferter Text „Key Components and Vision Check In Check Out“, aufgenommen am 22.10.2026. | Produktdefinition, MVP-Fokus, Schichten, spätere Phasen, ca. 80-%-Nutzenziel und „Beyond PDF“ on hold. Inhaltliches Ursprungsdatum unbekannt. |
| S2 | „KonzeptCheckinCheckOut.pdf“, 75 Seiten; von Clemens Bartlome bereitgestellt. Originaldatei liegt ausserhalb des öffentlichen Repositorys. | S. 1-7 Konzept und Roadmap; S. 8-9 Hintergrund aus Call vom 22.12.2025; S. 10 Anhangsankündigung; S. 11-17 bildbasierter bestehender Reiseablauf; S. 18-75 historischer JSON-Abdruck. Konzepttext extrahiert, Abbildungen und bildbasierter Anhang visuell gesichtet, JSON strukturell untersucht. Kein aktueller API-Vertrag. |
| S3 | [Confluence-Ordner Nezasa](https://switzerlandtravelcentre.atlassian.net/wiki/spaces/Nezasa/folder/428081154). | Link erhalten, Inhalt am 22.10.2026 nicht zugänglich und nicht ausgewertet. Daraus werden keine Anforderungen abgeleitet. |

S4: Direkte Nutzerbestätigung vom 22.10.2026: Buchungen werden als JSON aus Nezasa bezogen. Zwei bereitgestellte Exporte wurden strukturerhaltend anonymisiert und mit fiktiven Preisen abgelegt; siehe [Beispiele und Prüfhinweise](../examples/nezasa/README.md). Die Originale waren nicht vollständig anonymisiert. Kundendaten, sensible Referenzen, Zugangstoken und direkte Links wurden ersetzt. Abrufmechanismus und API-Version sind nicht bestätigt.

S5: Direkte Nutzeranforderung vom 22.10.2026: Eine eigene Azure-Bereitstellung durch STC für Bilddaten, Hinweise und JSON mit Querverweisen (z. B. Referenz zu Package) wird benötigt. [IT-Einrichtungsgrundlage](AZURE_IT_SETUP.md) und [Inhaltsstruktur](CONTENT_STRUCTURE.md) dokumentieren den vorgeschlagenen Aufbau. Nur der Azure-Infrastrukturbedarf ist bestätigt; die konkrete Ressourcenauswahl und Datenverträge sind Vorschläge.

S6: Nutzerangabe vom 22.10.2026: [NezasaToWord](https://github.com/SwitzerlandTravelCentre/NezasaToWord) ist der Fetcher für Aufbau / JSON-Export und soll integriert werden. main-Commit 2920216ffbdd647cf6e5f06caaec79b0cb45db3c geprüft und als unveränderte Quellkopie unter components/nezasa-fetcher übernommen. Siehe [Integration](FETCHER_INTEGRATION.md). Client-Verhalten aus Code belegt; Live-API und Tenant-Berechtigungen wurden nicht getestet.

Der bestehende Reiseablauf im Anhang ist laut S2 ausdrücklich Status quo und **keine Benchmark oder Zielvorlage**. Das Call-Transkript wird in S2 als Hintergrund, nicht als konzeptionelle Referenz eingeordnet.

Das Original-PDF und der rohe JSON-Abdruck wurden wegen enthaltener Personen- und Buchungsdaten nicht ins Repository kopiert. Die Quellenangabe ist ein Herkunftsnachweis; das Original ist für andere Entwickler nicht automatisch erreichbar.

## Widersprüche und Gültigkeitsfragen

| ID | Thema | Befund | Umgang |
| --- | --- | --- | --- |
| C01 | MVP-Termin | S1: Ende Juli. S2, S. 6: Ende Februar. Kein eindeutiges Zieljahr. | Kein aktiver Termin festgelegt. |
| C02 | Folgephasen | S2: März / April / Mai und Prototyp bis Mai. S1: Follow-up TBD. | Reihenfolge als Vision erhalten, alte Monatsangaben nicht als Planung übernehmen. |
| C03 | Exportweg | S1 spricht von Exportverbesserungen; S2 beschreibt strukturierte Daten und DOCX-Erzeugung. | Bestehendes DOCX nachbearbeiten oder neu erzeugen: offen. |
| C04 | Spätere Kanäle | Gemeinsame Datenwahrheit ist Ziel; Word soll frei editierbar sein. | Rückführung manueller Änderungen in spätere Kanäle ist ungelöst. |
| C05 | Aktueller Umfang | MVP priorisiert; umfassende Vision beschrieben; „Beyond PDF“ on hold. | Keine späteren Funktionen allein aus der Vision in den MVP aufnehmen. Genaue Projektabgrenzung klären. |
| C06 | Quellenalter | S2 enthält einen Call von 2025 und einen historischen Export mit Reisezeitraum 2024. | Aktuelle Nezasa-Daten und aktuellen operativen Prozess separat verifizieren. |

## Offene Fragen für die nächste Konkretisierung

Diese Liste dokumentiert fehlende Informationen. Sie verlangt keine vollständige Beantwortung vor weiterer Kontextaufnahme.

| ID | Frage | Bedeutung |
| --- | --- | --- |
| Q01 | Was ist der heutige Projektstand? Der JSON-Fetcher ist integriert (S6). Gibt es weitere Komponenten, Templates oder Prototypen? | Verhindert doppelte Arbeit und falsche Ausgangsannahmen. |
| Q02 | Soll der MVP ein vorhandenes Nezasa-DOCX reparieren oder aus strukturierten Buchungsdaten ein neues Dokument erzeugen? | Bestimmt den grundlegenden Implementierungsweg. |
| Q03 | JSON aus Nezasa ist bestätigt und zwei Beispiele liegen vor (S4). S6 belegt einen Client mit GET /bookings/v1.13/{booking_id} und Basic Auth. Welche Zugänge / Channel sind freigegeben und entspricht dies dem aktuellen Serververtrag? | Grundlage des Datenadapters; noch keine API-Endpunkte bestätigt. |
| Q04 | Zwei bereinigte JSON-Beispiele liegen vor (S4). Ein problematisches DOCX und eine akzeptierte Zielvorlage fehlen noch. | Basis für Mapping, Reproduktion und Abnahme. |
| Q05 | Welche Inhalte müssen im MVP enthalten sein, in welchen Sprachen und für welche Reisearten? | Definiert vollständige Ausgabe und Testabdeckung. |
| Q06 | Welche konkreten Regeln gelten für Tagesüberschriften, Übernachtungen, Transporte und Check-in / Check-out? | Verhindert Interpretation als fertige Fachlogik. |
| Q07 | Wie werden offene, angefragte, stornierte oder unvollständige Leistungen und fehlende Daten dargestellt? | Korrekte Kundeninformation und Fehlerbehandlung. |
| Q08 | Wer nimmt fachlich ab, welche Word-Umgebung wird genutzt und welche Bearbeitungen müssen stabil funktionieren? | Prüfbarkeit des zentralen Nutzens. |
| Q09 | Wie erhalten Agents das Dokument, wo werden Zwischenstände gespeichert und wer darf auf Buchungen zugreifen? | Workflow, Betrieb und Datenzugriff. |
| Q10 | Welche Komponenten sollen in diesem Repository liegen; gibt es technische Vorgaben oder bestehende Systeme zur Wiederverwendung? | Code-Struktur, Schnittstellen und Stack. |
| Q11 | Gibt es einen neuen verbindlichen MVP-Termin und wie wird der Finalisierungsaufwand heute gemessen? | Planung und Einordnung des ca. 80-%-Ziels. |
| Q12 | Welche Teile der langfristigen Vision gehören aktuell zu Check In Check Out und welche zum pausierten „Beyond PDF“? | Verhindert unbeabsichtigte Ausweitung. |

## Azure-spezifische Klärungen für IT und Fachverantwortung

| ID | Klärung | Zuständigkeit |
| --- | --- | --- |
| Q13 | Welche Subscription, Region, Netzwerk-Anbindung, Kostenstelle und Betriebsverantwortung gelten? | IT |
| Q14 | Wo läuft die Anwendung und wie erreicht sie die private Inhaltsablage? | IT / Entwicklung |
| Q15 | Welches Nezasa-Feld identifiziert ein Package eindeutig und wie werden mehrere Module behandelt? | Fachverantwortung / Nezasa / Entwicklung |
| Q16 | Wer pflegt Inhalte, Bildrechte und Übersetzungen, wer gibt Releases frei? | Fachverantwortung |
| Q17 | Welche Inhaltsarten gehören zum ersten MVP; welche Aufbewahrung, RPO/RTO und Budgets gelten? | Projekt / IT |

## Entscheidungsprotokoll

- 22.10.2026: Eingangsform JSON aus Nezasa durch direkte Nutzerangabe bestätigt (S4). Zwei Beispiele für das öffentliche Repository strukturerhaltend bereinigt. Authentifizierung, Abrufmechanismus, API-Version und vollständiger Vertrag bleiben offen.

- 22.10.2026: STC-bereitgestellte Azure-Infrastruktur als Quelle für Bilder, Hinweise und JSON-Querverweise angefordert (S5). Konkrete Ressourcen und Inhaltsverträge als Einrichtungsvorschlag dokumentiert; keine Bereitstellung erfolgt.

- 22.10.2026: Bestehenden Fetcher aus NezasaToWord integriert (S6), mit Herkunftsnachweis und Offline-Tests. Keine Word- oder Azure-Anbindung hinzugefügt.

Künftige Einträge sollen Datum, Entscheidung, Entscheidungsquelle, Begründung und gegebenenfalls abgelöste Aussage nennen. Neue Quellen ergänzen das Register; offene Punkte werden erst nach tatsächlicher Klärung geschlossen.
