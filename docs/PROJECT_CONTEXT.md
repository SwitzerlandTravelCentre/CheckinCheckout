# Projektkontext

Stand: 22.10.2026. Quellen: S1, S2, S4, S5 und S6 aus [Quellen und offene Fragen](SOURCES_AND_OPEN_QUESTIONS.md). Alle Aussagen sind aus dem gelieferten Kontext konsolidiert; ihre heutige Gültigkeit muss bei Bedarf bestätigt werden.

## Problem und Nutzen

Individuelle Touring-Reisen umfassen mehrere Tage, Destinationen, Hotels, Transportabschnitte, Zeitfenster und Sonderbedingungen. Das erschwert eine vollständige automatisierte Darstellung und erfordert menschliche Bearbeitung.

Der beschriebene Nezasa-Word-Export erzeugt Formatierungsprobleme und hohen Nachbearbeitungsaufwand. S2 beschreibt einen HTML-to-Word-Export, dessen Tabellen, Abstände und Absatzformate schon bei kleinen Änderungen instabil werden. Eine regelmässig manuell zu entfernende „Check-in / Check-out“-Zeile ist namensgebendes Beispiel dieses Problems (S2, S. 5).

Ziel ist ein sauberer DOCX-Export mit grundlegenden Struktur- und Darstellungsregeln. Die erwartete Reduktion des manuellen Finalisierungsaufwands um ungefähr 80 % ist ein **Nutzenziel**, kein gemessener Erfolg und keine bereits definierte Abnahmegrenze. Ausgangswert und Messverfahren fehlen.

## Begriffe und Beteiligte

| Begriff | Bedeutung im gelieferten Kontext |
| --- | --- |
| Travel Docs / Reiseablauf | Zentrale Reiseunterlagen für die gesamte Reise: Vorbereitung und Buchungsbestätigung vor Abreise, Orientierung und Referenz während der Reise. |
| Reisedossier | Travel Docs zusammen mit ergänzenden Tickets, Vouchern, Reservierungen und weiteren Bestätigungen. |
| Travel Agent | Prüft, ergänzt, korrigiert und finalisiert die Unterlagen. Aktiver Bearbeiter im Human-in-the-loop-Prozess. |
| Sales | Vorgesehene operative Nutzergruppe des MVP. Genaue Rollen und Berechtigungen sind offen. |
| Nezasa | Buchungssystem und vorgesehene erste Datenquelle. Bestehender Fetcher mit Booking API v1.13 / Basic Auth übernommen (S6); Tenant-Freigabe bleibt zu prüfen. |
| Beyond PDF | Breitere, derzeit zurückgestellte Vision eines zentralen Systems für konsistente Unterlagen über B2B, B2C, Groups und weitere Beteiligte. |

Kunden sollen erkennen können, welche Hotels und Leistungen gebucht sind, welche Abläufe und Zeiten gelten und was zusätzlich zu buchen oder zu reservieren ist. Aussagen zu inkludierten, bezahlten und nicht gebuchten Leistungen dürfen nicht gleichgesetzt werden.

## Fachliche Leitplanken aus den Quellen

- Strukturierte Buchungsdaten sind das verbindliche Grundgerüst.
- Menschliche Finalisierung ist ein Kernelement, insbesondere bei individuell zusammengestellten Reisen.
- Gute automatische Erzeugung muss mit freier operativer Bearbeitung in Word vereinbar sein.
- Travel Docs sollen den tatsächlichen Reiseverlauf aus Kundensicht erklären; reine Wiedergabe der technischen Datenanordnung genügt nicht.
- Ergänzende Inhalte und Buchungsfakten brauchen eine nachvollziehbare Herkunft.
- Die langfristige Architektur soll austauschbare Komponenten und zusätzliche Quellsysteme ermöglichen.

### Beispiel: Darstellung eines Reisetags

Ein Gast übernachtet in A, reist am nächsten Morgen nach B und übernachtet dort. Eine Tagesüberschrift mit ausschliesslich dem Ziel- oder Hotelort kann verwirren. S2 (S. 3-4) beschreibt eine Darstellung wie „A nach B“, abgeleitet aus Transporten, Zeitpunkten und Übernachtungen.

Dies ist ein fachliches Regelbeispiel. Prioritäten bei mehreren Transporten, Rundreisen, fehlenden Zeiten, Tagesausflügen und Nachtfahrten sind noch nicht definiert. Daraus lässt sich kein fertiger Algorithmus ableiten.

## Bestätigte Eingangsform

Am 22.10.2026 bestätigt der Nutzer: Buchungen werden als JSON aus Nezasa bezogen (S4). Zwei strukturerhaltend bereinigte Exporte liegen unter [examples/nezasa](../examples/nezasa/README.md). S6 ergänzt den vorhandenen [Fetcher](FETCHER_INTEGRATION.md) mit GET /bookings/v1.13/{booking_id} und Basic Auth. Aktueller Serververtrag und tatsächliche Berechtigungen bleiben unabhängig zu bestätigen.

## Bestätigter Infrastrukturbedarf

S5: STC benötigt eine eigene Azure-Bereitstellung, aus der die Anwendung Bilder, Hinweise und JSON-Querverweise (beispielsweise Referenz zu Package) liest. Die [IT-Basisstruktur](AZURE_IT_SETUP.md) und der [Inhaltsvertrag](CONTENT_STRUCTURE.md) konkretisieren dies als technischen Vorschlag. Azure ist bestätigt; Blob Storage, Netzkonfiguration, Rollen und der konkrete Inhaltsvertrag sind noch keine freigegebenen Implementierungsentscheidungen.

## Zielarchitektur als fachliches Modell

Die Schichten beschreiben Verantwortlichkeiten, keine bereits beschlossenen Services oder Deployments.

| Schicht | Verantwortung | Einordnung |
| --- | --- | --- |
| Buchungsdaten | Gebuchte Leistungen bereitstellen; im Zielbild strukturierte Extraktion und versionierte Ablage mit Buchungsreferenz. | Nezasa zuerst; Datenvertrag und Persistenz offen. |
| Analyse und Anreicherung | Daten konsolidieren, Regeln anwenden, Lücken und Widersprüche erkennen; später Drittinhalte ergänzen und AI-gestützte Prüfungen ermöglichen. | Für MVP nur einfache Regeln beschrieben. |
| Personalisierung | Informationsdichte, Priorisierung, Tonalität und Template anhand des Kundenkontexts steuern. | Zukunftskontext. |
| Bearbeitung und Kontrolle | Editierbaren Word-Draft erzeugen; Travel Agent prüft und finalisiert. | Kern der unmittelbaren Arbeitsrichtung. |
| Ausspielung | Finalisierte Inhalte kanalgeeignet als PDF, E-Mail, Website oder App bereitstellen. | Breiter Ausbau später; MVP-Auslieferung noch zu klären. |

Logischer Zielablauf: Buchungsdaten → Verarbeitung und Regeln → gegebenenfalls Anreicherung / Personalisierung → DOCX-Draft → menschliche Finalisierung → Ausgabe.

S2 betrachtet Word als kontrollierte Ableitung einer gemeinsamen Datenbasis. **Offen ist, wie manuelle Word-Änderungen für weitere Kanäle übernommen werden.** Weder ein DOCX-Roundtrip noch eine Synchronisation oder ein verbindliches finales Datenmodell sind beschlossen. Die langfristige Konsistenz aller Kanäle ist ein Ziel, keine gelöste Eigenschaft.

## Zukunftskontext und Abgrenzung

S1 beschreibt spätere Phasen für Architekturdefinition, erweiterte Analyse und Anreicherung sowie Personalisierung und eine mobile Website. S2 nennt beispielhaft Karten, Bilder, ST-Inhalte, saisonale Informationen, 10-15 Prüfkriterien und drei Kundenprofil-Drafts mit unterschiedlichem Orientierungsbedarf. Diese Beispiele sind keine freigegebenen aktuellen Integrationen, Regelkataloge oder Personalisierungsvorgaben.

Der zunächst nutzbare MVP für Sales hat Vorrang. Die weitere Projektentwicklung soll danach in einem breiteren Kontext besprochen werden. „Beyond PDF“ bleibt gemäss S1 on hold; die genaue organisatorische Abgrenzung zur langfristigen Check-In-Check-Out-Vision ist offen.
