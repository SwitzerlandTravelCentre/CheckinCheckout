# Quellen und Entscheidungsverlauf

Aufgenommen: 22.10.2026. Zuletzt abgeglichen: 26.10.2026. Aktuelle Nutzerentscheidungen haben Vorrang vor älteren Dokumenten. Aktueller Stand: [README](../../README.md); offene Implementierungsentscheidungen: [OPEN_DECISIONS](../OPEN_DECISIONS.md).

**Kennzeichnung:** Nutzerentscheidung = bestätigter Scope; Quellenmaterial = Kontext mit möglichem Altersrisiko; Vorschlag = noch abzustimmen; Codebeobachtung = implementiertes Verhalten, keine Garantie über alle Serverantworten.

## Quellenregister

| ID | Quelle | Verwendbarer Inhalt / Grenze |
| --- | --- | --- |
| S1 | Im Chat gelieferter Text „Key Components and Vision Check In Check Out“. Ursprungsdatum unbekannt. | Problem, Travel Docs, Schichten, spätere Phasen, 80-%-Ziel und Beyond PDF on hold. Alter Juli-Termin abgelöst. |
| S2 | KonzeptCheckinCheckOut.pdf, 75 Seiten, vom Nutzer bereitgestellt. | S. 1–7 Konzept/Roadmap; S. 8–9 Call vom 22.12.2025 als Hintergrund; S. 11–17 bisheriger Reiseablauf; S. 18–75 historischer JSON-Abdruck. Enthält sensible Daten, liegt nicht im öffentlichen Git. |
| S3 | [Confluence-Ordner Nezasa](https://switzerlandtravelcentre.atlassian.net/wiki/spaces/Nezasa/folder/428081154). | Link erhalten; Inhalt nicht zugänglich und nicht ausgewertet. Keine Anforderungen daraus abgeleitet. |
| S4 | Nutzer bestätigt JSON-Exporte und liefert zwei Buchungen. | [Bereinigte Fixtures](../../examples/nezasa/README.md); Struktur erhalten, Kundendaten/Referenzen/Preise ersetzt. Kein vollständiger API-Vertrag. |
| S5 | Nutzer fordert eigene STC-Azure-Umgebung für Bilder, Hinweise und Querverweise. | Bedarf bestätigt; [Ressourcen](../AZURE_IT_SETUP.md) und [Inhaltsvertrag](../CONTENT_STRUCTURE.md) bleiben Vorschläge. |
| S6 | Nutzer ordnet [NezasaToWord](https://github.com/SwitzerlandTravelCentre/NezasaToWord) als Fetcher ein und beauftragt Integration. | Quellkopie von Commit 2920216ffbdd647cf6e5f06caaec79b0cb45db3c eingebunden, danach lokal angepasst. [Herkunft](../../components/nezasa-fetcher/UPSTREAM.md). |
| S7 | Nutzer aktualisiert API-Status, trennt Fetcher/finale Anwendung und nennt Jahresendtermin. | API funktioniert laut Nutzer; Fetcher nur JSON-Testdaten; finale Anwendung integriert Abruf und erzeugt direkt Word; MVP Ende Dezember 2026. |
| S8 | Vom Nutzer vorgelegte Management-Antwort und anschliessende Klärung. | Aufwand ca. 10–30, vereinzelt 45 Minuten; zunächst ca. 50 % weniger Nacharbeit als ungemessene Einschätzung. Technisches Logging ist nicht mit Jira-Projektarbeit gleichzusetzen. |
| S9 | Nutzer beauftragt umfassendes Repository-Review und entwicklungsorientierte Verdichtung. | Aktive Entwicklungsunterlagen, Beispielindex und Konzeptkontext trennen; menschliche und AI-Entwicklung unterstützen. |

S10: Am 22.10.2026 liefert der Nutzer vier weitere Buchungs-JSONs und beauftragt Anonymisierung, fiktive Preise und Veröffentlichung als Beispiele. Sie sind als Beispiele 03–06 ergänzt; bestehende Beispiele unverändert. Der [Beispielkatalog](../../examples/nezasa/README.md) dokumentiert Abdeckung, synthetisierte Inhalte und Prüfungen.

S11: Anwendungsentwicklung, IT-Bereitstellung und fachliche Abnahme sind getrennte Rollen. Die Bereitstellung der Infrastruktur ist nicht bestätigt. Personen- und Dienstleisternamen werden in der öffentlichen Dokumentation nicht geführt.

S12: Managementunterlagen sind auf Nutzeranweisung vom 23.10.2026 vertraulich und von der Veröffentlichung ausgeschlossen. Öffentliche Entwicklungsdokumente enthalten keine internen Vertrags-, Kosten-, Personal- oder Abstimmungsdetails.

S13: Ergänzter Entwicklungsstand: Export-Prototypen und interne Tests sind laut Nutzerangaben vorhanden; ein aktueller Template-Export liegt vor. Anwendungscode und Template-Datei sind hier nicht abgelegt. Eine operative Abnahme ist nicht bestätigt. Der Hinweis korrigiert die frühere pauschale Aussage, die Anwendung sei noch vollständig zu bauen; die Original-Artefakte wurden nicht technisch geprüft.

S14 (26.10.2026, Nutzerentscheidung): Nezasa bleibt die zentrale Datei. Azure enthält nur ausdrücklich abgegrenzte redaktionelle Ergänzungen; keine zweite Pflege von Buchungsfakten. Allgemeine Anreisehinweise gehören zu Preparation. Basisinhalte und gezielte Produkt-/Saison-/Anreisevarianten vermeiden Doppelpflege. Drittquellen können später einzelne Ergänzungsfelder übernehmen; keine manuelle Spiegelung ihrer Inhalte auf Azure. Begründung: geringer Pflegeaufwand und austauschbare Inhaltsquellen. Ersetzt den zuvor offenen allgemeinen Inhaltsumfang aus S5; konkrete Betriebs- und Freigabefragen bleiben offen.

S15 (26.10.2026, Nutzerentscheidung): Grand Tour ist die Autoreise ohne Züge, Grand Train Tour enthält GEX und BEX. Hero-Priorität: GEX, BEX, GoldenPass; ohne Zug Auto-/Skimotiv für diese Reisearten, sonst Zermatt, Luzern, neutrales Schweiz-Bild. Saisonversion vor Standard desselben Motivs; Anreisegebiet verändert keine Bilder. Gotthard nach GoldenPass bleibt eine vorläufige Einordnung. Details und Grenzen im [Inhaltskonzept](../CONTENT_STRUCTURE.md).

S16 (26.10.2026, Nutzerentscheidung): Öffentliche Updates enthalten nur konzeptionelle Informationen ohne Personen- oder Dienstleisternamen. Managementunterlagen, lokale Upload-Pakete, interne Kommunikation und vertrauliche Details werden nicht veröffentlicht.

S8 verweist auf einen [Arbeitsprozess in Confluence](https://switzerlandtravelcentre.atlassian.net/wiki/x/AgDlIQ) und SharePoint. Das sind Nutzerangaben zu Ablageorten; die Inhalte wurden nicht geprüft.

S2s bisheriger Reiseablauf ist ausdrücklich keine Benchmark/Zielvorlage. Der historische JSON-Abdruck mit Reisezeitraum 2024 ist keine direkt ausführbare Fixture. Für Entwicklung die maschinenlesbaren Beispiele aus S4 verwenden.

## Abgelöste und eingeordnete Aussagen

| Frühere Referenz | Einordnung heute |
| --- | --- |
| C01: Februar vs. Juli, Zieljahr unklar | S7 ersetzt beide Termine durch Ende Dezember 2026. |
| C02: Folgephasen März/April/Mai | Nur historische Planung; keine aktive Roadmap. |
| C03: bisherigen Export reparieren oder neu erzeugen | S7: finale Anwendung ruft selbst ab und erzeugt neues Word. |
| C04: Word-Freiheit vs. gemeinsame Datenwahrheit | Rückführung manueller Änderungen für spätere Kanäle ungelöst; [Vision](PROJECT_VISION.md). |
| C05: Check In Check Out vs. Beyond PDF | MVP priorisiert; spätere organisatorische Abgrenzung offen. |
| C06: Quellenalter | Dokumentdatum beweist keine Aktualität; aktive Fixtures und aktuelle Entscheidungen vorziehen. |
| 80 % vs. 50 % | Älteres langfristiges Ziel vs. aktuelle erste Schätzung; weder gemessen noch Abnahmegrenze. |
| Word im Upstream „on hold“ | Betrifft frühere Fetcher-Experimente, nicht den CheckinCheckout-MVP. |
| API unbestätigt / kein Anwendungscode | Durch Integration (S6) und Nutzerbestätigung (S7) überholt. S13 ergänzt: Export-Prototypen und überarbeitete Versionen sind laut Projektangaben vorhanden. Anwendungscode fehlt in diesem Repository; eine operative Abnahme ist noch nicht bestätigt. |

## Herkunft der aktuellen Entscheidungen

Alle folgenden Einträge wurden am 22.10.2026 aufgenommen:

- **S4:** JSON als Eingangsform und zwei Beispiele bestätigt. Rohdaten wegen öffentlichem Git nur bereinigt übernommen.
- **S5:** Azure-Inhaltsquelle angefordert. Konkrete Bereitstellung und Vertrag noch zu bestätigen.
- **S6:** Fetcher als eingebettete Quellkopie integriert, ohne automatische Upstream-Synchronisation.
- **S7:** Entwicklungswerkzeug und finale Anwendung getrennt; API funktionsfähig bestätigt und Jahresendtermin festgelegt. Ersetzt C01/C03 sowie die offenen Teile von Q02/Q03.
- **S8:** Aktuelle Nutzenschätzung und Abgrenzung von Fehleranzeigen, technischem Logging und Projektverfolgung aufgenommen.
- **S9:** Dokumentation auf kurzen Entwicklungsstart und aufgabenbezogene Referenzen reduziert; Konzepte separat zugänglich.

Neue Entscheidungen mit Datum, Quelle, Begründung und abgelöster Aussage ergänzen. Vorschläge erst nach tatsächlicher Klärung als entschieden markieren.

## Alte Fragen weiterhin auffinden

| Alte IDs | Heutiger Ort |
| --- | --- |
| Q01, Q09, Q10, Q14 | D04: vorhandene Komponenten, Stack, Hosting, Zugriff und Dokumentübergabe. |
| Q02, Q03 | Durch S7 geklärt; Produktionsadapter/Betrieb unter D04/D08. |
| Q04, Q08 | D01: Word-Beispiele, Zielvorlage, Arbeitsumgebung und Abnahme. |
| Q05 | D02: Inhalte, Sprachen, Reisearten. |
| Q06, Q07 | D03: fachliche Regeln und Status. |
| Q11 | Termin geklärt (S7); Nutzenmessung D09. |
| Q12 | Zukunftskontext in PROJECT_VISION; kein aktueller MVP-Blocker. |
| Q13 | D07: IT-Rahmen. |
| Q15 | D05: Package-Referenz und mehrere Module. |
| Q16 | D06: Inhaltsverantwortung und Freigabe. |
| Q17 | D02/D06: Inhaltsumfang; D07: Aufbewahrung, RPO/RTO und Budget. |
