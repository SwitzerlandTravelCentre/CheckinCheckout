# Vorläufiger MVP-Rahmen

Stand: 22.10.2026. Dies ist eine aus S1/S2 abgeleitete Arbeitsgrundlage, keine bestätigte Sprintplanung oder freigegebene Spezifikation. Quellen und Klärungen: [Quellen und offene Fragen](SOURCES_AND_OPEN_QUESTIONS.md).

## Unmittelbares Ergebnis

Sales / Travel Agents können aus Nezasa-Buchungsdaten ein sinnvoll strukturiertes, Word-natives und stabil editierbares DOCX erhalten und im Tagesgeschäft finalisieren. Der operative Nutzen liegt in weniger Layoutreparatur und einfacherer Bearbeitung.

Ob eine bestehende DOCX-Datei verbessert oder ein neues DOCX aus strukturierten Daten erzeugt wird, ist **nicht entschieden**. Die Quellen verwenden sowohl „Export enhancements“ als auch eine Erzeugung aus Buchungsdaten. Die Eingangsform JSON aus Nezasa ist inzwischen bestätigt (S4); der konkrete DOCX-Erzeugungsweg bleibt zu klären.

## Beschriebener Umfang

| ID | Arbeitsanforderung | Herkunft und Status |
| --- | --- | --- |
| M01 | Nezasa als erste Quelle für Buchungsdaten verwenden. | S1/S2; JSON durch S4 bestätigt, Zugriff und versionierter Datenvertrag offen. |
| M02 | Ein in Word bearbeitbares DOCX mit tragfähiger Struktur erzeugen. | S1 und S2; Zielvorlage und technische Definition von „Word-native“ offen. |
| M03 | Die Darstellung des Reiseablaufs durch einfache Regeln verbessern. | S1 allgemein, S2 mit Reisetag-Beispiel; exakter MVP-Regelkatalog offen. |
| M04 | Prüfung, Korrekturen und freie Ergänzungen durch Travel Agents ermöglichen. | S1 und S2; Word als Arbeitsfläche. |
| M05 | Einfachen Weg von einer Buchungsreferenz zum Word-Dokument anbieten. | S2, S. 6: Buchungsnummer eingeben → Dokument erhalten; konkrete Oberfläche noch unbestätigt. |
| M06 | Mehrere Basis-Templates unterstützen. | In S2 ausdrücklich optional; kein Pflichtumfang. |

Kein aktiver Liefertermin ist aus den Quellen ableitbar: „Ende Juli“ in S1 widerspricht „Ende Februar“ in S2; ein eindeutiges Zieljahr fehlt.

## Vorschlag für prüfbare Abnahmeszenarien

Die folgenden Szenarien konkretisieren die Probleme für eine spätere Abstimmung. Sie sind **Vorschläge**, keine bereits genehmigten Kriterien.

| Szenario | Vorgeschlagenes erwartetes Verhalten |
| --- | --- |
| Buchungsinhalt | Relevante gebuchte Hotels, Leistungen und Reisetage lassen sich gegen einen geprüften Quelldatensatz abgleichen; keine erfundenen Leistungen oder stillen Statusänderungen. Die genaue Auswahl relevanter Felder muss definiert werden. |
| Normaler Textumbau | Einen Hinweis verlängern, Text ergänzen oder entfernen und anschliessend speichern / erneut öffnen, ohne beschädigte Tabellen oder unlesbare Überlagerungen. |
| Seitenfluss | Mehrtägige Reisen und längere Leistungsbeschreibungen bleiben lesbar; normale Seitenumbrüche sind zulässig. |
| Check-in / Check-out | Das im bestehenden Export beschriebene Problem ist reproduzierbar erfasst und behoben. Ob die Zeile entfernt, korrigiert oder bedingt angezeigt werden soll, muss fachlich entschieden werden. |
| Reise A nach B | Ein abgestimmter Testfall zeigt den Transporttag nachvollziehbar, ohne ihn nur als Hotelaufenthalt in B darzustellen. |
| Fehlende oder widersprüchliche Daten | Keine erfundenen Ersatzangaben; gewünschte Warnung, Blockierung oder Markierung wird vorab festgelegt. |
| Menschliche Finalisierung | Travel Agent kann Inhalte fachlich prüfen, ändern und reisefertig speichern. |
| Effizienz | Manuellen Finalisierungsaufwand mit der bisherigen Arbeitsweise an vergleichbaren Reisen messen. Die ca. 80 % bleiben bis dahin ein Nutzenziel. |

Benötigt werden eine akzeptierte Zielvorlage, anonymisierte oder synthetische repräsentative Buchungen und fachliche Abnahme durch die vorgesehenen Nutzer.

## Aktuelle Beispielbasis

S4 bestätigt JSON-Exporte aus Nezasa und liefert zwei konkrete Beispiele. Bereinigte Kopien liegen unter [examples/nezasa](../examples/nezasa/README.md). Struktur und Datentypen bleiben erhalten; Kundendaten, sensible Referenzen und Preise sind synthetisch. Die Exporte ersetzen keinen vollständigen API-Vertrag.

## Hinweise aus dem historischen JSON-Beispiel

S2, S. 18-75 enthält einen nummerierten JSON-Abdruck. Er ist keine Schema-Dokumentation und keine direkt ausführbare Fixture.

Beobachtete Strukturhinweise:

- Eine Booking-Ressource mit Identität, Attributen und Komponentenbeziehungen; ein „included“-Bereich enthält Komponenten.
- Reisezeitraum, Sprache, Module und Referenzen sowie Komponenten mit Typ, Status und Zeitangaben.
- Beispielsweise Unterkunft, Aktivität, Basisleistung und Zusatzleistung; die vollständige Typenmenge ist nicht belegt.
- Zimmer- und Reisendenzuordnung, Lieferantenreferenzen, Buchungsreferenzen und Voucher-Verweise.
- Verschiedene Zeitdarstellungen: Kalenderdaten, UTC und explizite Offsets. Verbindliche Zeitzonen- und Tageszuordnung fehlen.
- Gebuchte und offene Komponenten kommen im Beispiel vor. Ihre Sichtbarkeit und Formulierung im Kundendokument müssen geklärt werden.

Folgerungen für die spätere Umsetzung, noch keine bestätigten API-Eigenschaften:

- Beziehungsschlüssel und Zimmerzuordnung berücksichtigen; mehrere Zimmer desselben Hotels nicht ohne Regel als Dubletten behandeln.
- Buchungsreferenz und API-ID nicht ohne Prüfung gleichsetzen.
- Reisezeitraum, Hotelzeiten und Transportzeiten semantisch unterscheiden.
- Die zwei maschinenlesbaren Beispiele aus S4 für die Mapping-Arbeit verwenden; den vollständigen und versionierten Datenvertrag weiterhin klären.
- Rohdaten enthalten Personen-, Kontakt-, Preis- und potenziell zugangstragende Linkinformationen. Nur bewusst ausgewählte Daten in Kundenausgabe, Logs und Testmaterial übernehmen.

## Noch nicht festgelegt

Azure als STC-betriebene Inhaltsquelle für Bilder, Hinweise und JSON-Querverweise ist inzwischen bestätigt (S5). Siehe [IT-Basisstruktur](AZURE_IT_SETUP.md); ihre technischen Details sind Vorschläge. Stack, Bibliotheken, Anwendungs-Hosting, Datenbank, Authentifizierung, API-Endpunkte, konkrete Berechtigungen, Aufbewahrung, Template-Format, DOCX-Styles, unterstützte Word-Versionen und Sprachen bleiben offen. Ob alle Inhaltsarten bereits im ersten MVP gebraucht werden, ist noch zu klären. Aus dieser Dokumentation lässt sich keine vorhandene Integration oder fertige Software ableiten.
