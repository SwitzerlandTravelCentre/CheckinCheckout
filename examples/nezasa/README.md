# Nezasa-Beispielbuchungen

Zwei Nutzerexporte, am 22.10.2026 für das öffentliche Repository bereinigt. Sie dienen Parser-, Mapping- und Dokumentgenerierungsarbeit. Originaldateien liegen ausserhalb des Repositorys und wurden nicht verändert. [Zur Beispielübersicht](../README.md).

## Passendes Beispiel auswählen

| Datei | Reisende | Komponenten nach `included[].attributes.type` | Komponentenstatus |
| --- | --- | --- | --- |
| [booking_example_01.json](booking_example_01.json) | 2 | 6 accommodation, 5 activity, 2 baseService, 1 upsell-item (14 gesamt) | 12 Booked, 2 Open |
| [booking_example_02.json](booking_example_02.json) | 4 | 12 accommodation, 5 activity, 2 baseService, 4 upsell-item (23 gesamt) | 21 Booked, 2 Open |

Beide Beispiele sind deutsch (`lang=de`), enthalten genau ein Modul und haben auf Buchungsebene `bookingState=BookingCompleted`. Daraus darf **nicht** abgeleitet werden, dass jede einzelne Leistung bestätigt ist: Beide enthalten Komponenten mit `status=Open`. Die fachliche Darstellung dieser Fälle ist noch festzulegen.

## Feldpfade für den Einstieg

| Information | Beobachteter JSON-Pfad / Beziehung |
| --- | --- |
| Buchungshülle | `data.type` ist `booking`; `data.id` identifiziert die Buchung. |
| Reisezeitraum und Sprache | `data.attributes.startDate`, `endDate`, `lang` |
| Reisende / Hauptkontakt | `data.attributes.pax.paxInfo[]` / `data.attributes.pax.contact` |
| Template und Module | `data.attributes.templateRefId` / `data.attributes.modules[]` |
| Komponentenverknüpfung | `data.relationships.components.data[]` über `type` und `id` mit `included[]` verbinden. |
| Leistungsart und Status | `included[].attributes.type` / `included[].attributes.status`; `included[].type` ist die Ressourcenart `component`. |
| Leistungsdetails | Je Komponente etwa `startDateTime`, `endDateTime`, `room`, `startLocation`, `remarks` unter `attributes`; nicht überall vorhanden. |

In beiden Dateien sind die Komponentenreferenzen vollständig auflösbar; es gibt keine doppelten Komponenten-IDs oder unverbundenen Einträge in `included`. Reihenfolge, Datumsinterpretation und fachliche Gruppierung für Word sind damit noch nicht festgelegt.

## Bereinigung und Nutzungslimits

- Namen, Geburtsdaten, Alter, Kundenkontakte und sensible Buchungs-/Fall-/Komponenten-/Zahlungsreferenzen wurden durch konsistente Testdaten ersetzt. Die Originale waren in Zimmerzuordnungen nicht vollständig anonymisiert.
- Direkte URLs verwenden `booking.example.invalid`, strukturierte E-Mail-Adressen `example.invalid`; Zugangstoken wurden entfernt. Allgemeine Hotelkontakte in Beschreibungen sind erhalten.
- Undurchsichtige `productExternalRefId`-Payloads und Promo-Codes wurden synthetisch ersetzt. Diese Payloads sind keine gültigen Lieferantenanfragen.
- Reiseinformationen, Hotel-/Produktnamen, Status und Währungen sind erhalten. Reale Referenzbedeutungen lassen sich daraus nicht ableiten.
- 125 bzw. 212 nichtnullige Geld-/Prozentwerte wurden durch Fantasiewerte ersetzt; 37 bzw. 58 Nullwerte blieben erhalten. Zahlen und Strings behalten ihren ursprünglichen Datentyp. **Summen, Margen und Stornostaffeln sind nicht rechnerisch abgestimmt** und eignen sich nicht für Finanztests.

Bei der Bereinigung wurden Schlüssel samt Reihenfolge, Container, Array-Längen und skalare Datentypen gegen die Originale geprüft. Personen- und Komponentenbeziehungen blieben konsistent; die Originale blieben laut SHA-256-Prüfung unverändert. Der [Offline-Test](../../tests/test_nezasa_fetcher.py) prüft heute den Export beider Dateien ohne Struktur- oder Wertänderung.

## Noch nicht durch Beispiele abgedeckt

Andere Buchungssprachen, mehrere Module, andere Leistungsarten sowie fehlende oder widersprüchliche Beziehungen sind durch diese beiden realitätsnahen Fixtures nicht belegt. Ungültige API-Antworten werden separat in den Fetcher-Tests simuliert. Es gibt kein erwartetes DOCX als Vergleichsdatei und keine fachlich bestätigte Package-Zuordnung. Das [Inhaltsbeispiel](../content/README.md) verwendet eigene fiktive Referenzen.
