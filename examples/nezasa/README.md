# Nezasa-Beispielbuchungen

Stand: 22.10.2026. Zwei vom Nutzer bereitgestellte JSON-Exporte aus Nezasa, für das öffentliche Repository bereinigt. Die Originaldateien sind unverändert und wurden nicht ins Repository übernommen.

| Datei | Reisende | Komponenten | Geld-/Prozentwerte ersetzt | URLs ersetzt |
| --- | --- | --- | --- | --- |
| [booking_example_01.json](booking_example_01.json) | 2 | 14 | 125 | 16 |
| [booking_example_02.json](booking_example_02.json) | 4 | 23 | 212 | 28 |

## Anonymisierung

Die Originale waren nicht durchgängig anonymisiert: In Zimmerzuordnungen waren noch ausgeschriebene Namen vorhanden, obwohl sie auf Buchungsebene teilweise gekürzt waren.

- Kundennamen, Geburtsdaten, Anschrift, Telefonnummer und strukturierte E-Mail-Adressen ersetzt. Alter passend zum synthetischen Geburtsdatum und Reisebeginn angepasst. Wiederholte Personen und der Hauptkontakt erhalten konsistente Testdaten anhand der bestehenden pax-Referenz.
- Buchungs-, Fall-, Komponenten-, Lieferantenbuchungs- und Zahlungsreferenzen synthetisch ersetzt. Komponentenbeziehungen bleiben konsistent.
- Direkte URLs auf booking.example.invalid und strukturierte E-Mail-Adressen auf example.invalid umgestellt. Buchungsreferenzen in URL-Pfaden und Queries ersetzt; Zugangstoken entfernt.
- Undurchsichtige productExternalRefId-Payloads synthetisch ersetzt: Sie können eingebettete Preise und interne Referenzen enthalten. Trennzeichen, Tokenlängen und Zeichenklassen bleiben erhalten; diese Payloads sind keine gültigen Lieferantenanfragen.
- Vorhandene Promo-Codes und deren Titel durch Beispielwerte ersetzt.
- Fachliche Reiseinformationen, Zeiten, Hotel- und Produktnamen, Beschreibungen, Status und Währungen erhalten. Allgemeine Hotelkontaktdaten in Hotelbeschreibungen bleiben bestehen.

## Fiktive Preise

Alle nichtnulligen Geldbeträge und vorhandenen Prozentwerte wurden durch unabhängig gewählte Fantasiewerte ersetzt, ohne rückrechenbaren Skalierungsfaktor. Wiederholte identische Zahlenwerte werden pro Datei konsistent ersetzt. Der Datentyp bleibt erhalten, auch bei Zahlungsbeträgen als String.

37 beziehungsweise 58 Nullwerte bleiben erhalten, um kostenlose Leistungen und leere Betragsanteile abzubilden. Die Fantasiewerte sind **keine kaufmännisch abgestimmte Kalkulation**: Summen, Margen, Prozentsätze und Stornostaffeln müssen nicht zusammenpassen. Die Beispiele dienen Struktur-, Mapping- und Dokumentgenerierungsarbeit, nicht der Validierung von Preisberechnungen.

## Durchgeführte Prüfungen

- JSON erneut eingelesen; jeden Schlüssel samt Reihenfolge, alle Container, Array-Längen und skalaren Datentypen mit dem Original verglichen. Keine Normalisierung und keine zusätzlichen Metadaten im JSON.
- Jeder nichtnullige Geld-/Prozentwert ist verändert.
- Bekannte ursprüngliche personenbezogene Werte und Buchungsreferenzen sind entfernt; direkte E-Mails und URLs verwenden ausschliesslich .invalid.
- Komponentenverknüpfungen und Namen/Geburtsdaten/Alter wiederholter Reisender sind konsistent.
- Originaldateien per SHA-256 vor und nach Verarbeitung verglichen: unverändert.

Die Beispiele belegen beobachtete Exportstrukturen, keinen vollständigen oder versionierten Nezasa-API-Vertrag. Die absichtlich veränderten Inhalte dürfen nicht zur Rekonstruktion echter Buchungen verwendet werden.
