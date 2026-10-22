# Nezasa-Beispielbuchungen

Sechs Nutzerexporte, am 22.10.2026 für das öffentliche Repository bereinigt. Sie dienen Parser-, Mapping- und Dokumentgenerierungsarbeit. Originaldateien liegen ausserhalb des Repositorys und wurden nicht verändert. [Zur Beispielübersicht](../README.md).

## Passendes Beispiel auswählen

| Datei | Sprache / Reisende | Komponenten nach `included[].attributes.type` | Komponentenstatus |
| --- | --- | --- | --- |
| [booking_example_01.json](booking_example_01.json) | de / 2 | 6 accommodation, 5 activity, 2 baseService, 1 upsell-item (14 gesamt) | 12 Booked, 2 Open |
| [booking_example_02.json](booking_example_02.json) | de / 4 | 12 accommodation, 5 activity, 2 baseService, 4 upsell-item (23 gesamt) | 21 Booked, 2 Open |
| [booking_example_03.json](booking_example_03.json) | en / 5, davon 2 Kinder | 10 accommodation, 7 activity, 2 baseService (19 gesamt) | 12 Booked, 7 Open |
| [booking_example_04.json](booking_example_04.json) | en / 2 | 7 accommodation, 8 activity, 2 baseService (17 gesamt) | 8 Booked, 9 Open |
| [booking_example_05.json](booking_example_05.json) | fr / 4, davon 2 Kinder | 1 accommodation, 2 activity, 1 baseService (4 gesamt) | 3 Booked, 1 Open |
| [booking_example_06.json](booking_example_06.json) | de / 3 | 3 accommodation, 2 activity, 2 baseService, 1 upsell-item (8 gesamt) | 4 Booked, 4 Open |

Beispiel 05 ist ein kleiner französischer Familienfall. Beispiel 06 enthält zusätzlich eine Zahlungstransaktion mit Beträgen als Strings. Die englischen Beispiele erweitern die Zimmer-/Reisendenkonstellationen.

Alle Beispiele enthalten genau ein Modul und haben `bookingState=BookingCompleted`. Daraus darf **nicht** abgeleitet werden, dass jede einzelne Leistung bestätigt ist: Alle enthalten auch Komponenten mit `status=Open`. Die fachliche Darstellung ist noch festzulegen.

## Feldpfade für den Einstieg

| Information | Beobachteter JSON-Pfad / Beziehung |
| --- | --- |
| Buchungshülle | `data.type` ist `booking`; `data.id` identifiziert die Buchung. |
| Reisezeitraum und Sprache | `data.attributes.startDate`, `endDate`, `lang` |
| Reisende / Hauptkontakt | `data.attributes.pax.paxInfo[]` / `data.attributes.pax.contact` |
| Template und Module | `data.attributes.templateRefId` / `data.attributes.modules[]`; ein Modul muss nicht in jedem Beispiel eine refId haben. |
| Komponentenverknüpfung | `data.relationships.components.data[]` über `type` und `id` mit `included[]` verbinden. |
| Leistungsart und Status | `included[].attributes.type` / `included[].attributes.status`; `included[].type` ist die Ressourcenart `component`. |
| Leistungsdetails | Je Komponente etwa `startDateTime`, `endDateTime`, `room`, `startLocation`, `remarks` unter `attributes`; nicht überall vorhanden. |
| Zahlungstransaktionen | `data.attributes.payment.transactions[]`; in Beispiel 06 enthalten `amount.amount` und `amount.value` numerische Strings. |

Komponentenreferenzen sind vollständig auflösbar; keine doppelten Komponenten-IDs oder unverbundenen Einträge in `included`. Personen bleiben über ihre Referenzen konsistent den Zimmern zugeordnet. Reihenfolge, Datumsinterpretation und fachliche Gruppierung für Word sind noch nicht festgelegt.

## Bereinigung und Nutzungslimits

Für alle Beispiele wurden Kundennamen, Geburtsdaten, Kontakte, sensible Buchungs-/Fall-/Komponenten-/Zahlungsreferenzen und zugangstragende Links ersetzt. Direkte URLs verwenden `booking.example.invalid`, strukturierte E-Mails `example.invalid`. Undurchsichtige Lieferanten-Payloads sind synthetisch und keine gültigen Lieferantenanfragen.

Die ursprünglichen Beispiele 01–02 bleiben unverändert. Bei ihnen sind Reiseinformationen, Hotel-/Produktnamen und allgemeine Hotelkontakte in Beschreibungen erhalten.

Die zusätzlichen Beispiele **03–06** sind weitergehend synthetisiert:

- Auch Mitarbeiterdaten, Organisationen, Lieferantenkontakte, Template-/Modul-/Produktreferenzen und personenbezogene Tags sind ersetzt. Wiederholte IDs bleiben konsistent.
- Freitexte wie Beschreibungen, Bemerkungen, Reisetitel und Angebotsnamen sind durch sprachpassende Beispieltexte ersetzt. Hotel-/Produktnamen, Kategorien, Leistungsarten und Status bleiben als Entwicklungskontext erhalten.
- Reise-, Buchungs-, Zahlungs- und Stornodaten sind je Buchung einheitlich um ganze Wochen verschoben. Dauern, Reihenfolge, Wochentage und Zeitoffsets bleiben erhalten; **keine Referenz für reale Saisonverfügbarkeit**.
- Personen haben synthetische Namen, Geburtsdaten und Alterswerte; Erwachsene/Kinder bleiben unterscheidbar, Alter und Geburtsdatum passen zum synthetischen Reisebeginn. Nationalität und Kundenanschrift sind ebenfalls synthetisch.
- Alle nichtnulligen strukturierten Finanzwerte sind verändert, einschliesslich Wechselkursen und numerischen Zahlungsstrings. Nullwerte und skalare Datentypen bleiben erhalten. Identische Finanzwerte werden innerhalb derselben Kategorie und Datei konsistent ersetzt.

| Beispiel | Veränderte Finanzwerte | Erhaltene Nullwerte |
| --- | --- | --- |
| 01 | 125 | 37 |
| 02 | 212 | 58 |
| 03 | 192 | 47 |
| 04 | 174 | 59 |
| 05 | 36 | 17 |
| 06 | 94 | 17 |

Die Fantasiewerte sind unabhängig gewählt und nicht rückrechenbar skaliert. **Summen, Margen, Wechselkurse und Stornostaffeln sind nicht rechnerisch abgestimmt.** Diese Fixtures eignen sich nicht für Finanzberechnungen oder reale Buchungs-/Leistungsberechtigung.

## Prüfungen und Abdeckung

Bei der Bereinigung wurden Schlüssel samt Reihenfolge, Container, Array-Längen und skalare Datentypen gegen die Originale geprüft. Bekannte ursprüngliche Personen-/Referenzwerte, direkte URLs und E-Mails wurden auf verbleibende Vorkommen geprüft; bei 03–06 zusätzlich alle nichtnulligen Finanzwerte auf Änderung sowie Personen-/Zimmerzuordnungen und synthetisches Alter. Die Originale blieben laut SHA-256 unverändert.

Der [Offline-Test](../../tests/test_nezasa_fetcher.py) prüft den Export aller sechs Dateien ohne Struktur- oder Wertänderung. [Repository-Tests](../../tests/test_repository.py) prüfen Beziehungen und Dokumentlinks.

Deutsch, Englisch und Französisch sind enthalten; mehrere Module, weitere Leistungsarten sowie fehlende oder widersprüchliche Beziehungen werden durch diese Beispiele nicht vollständig abgedeckt. Ungültige API-Antworten werden separat simuliert. Es gibt kein erwartetes DOCX und keine fachlich bestätigte Package-Zuordnung. Das [Inhaltsbeispiel](../content/README.md) verwendet eigene fiktive Referenzen.
