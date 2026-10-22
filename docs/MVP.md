# MVP: Umfang und Abnahme

Stand: 22.10.2026. Bestätigter Zielweg und Termin aus [S7](concepts/SOURCES_AND_DECISIONS.md); die fachlichen Details und Abnahmeszenarien unten sind noch abzustimmen.

## Ergebnis

Bis **Ende Dezember 2026** soll Sales / Travel Agents aus einer Nezasa-Buchung direkt ein sauber strukturiertes, bearbeitbares Word-Dokument erhalten. Die Anwendung integriert den Abruf selbst. Der separate Fetcher dient ausschliesslich der Beschaffung von JSON-Testdaten.

Travel Docs erklären die gesamte Reise vor und während der Reise: Hotels, Leistungen, Tagesabläufe, Zeiten sowie relevante Hinweise und Reservierungsinformationen. Ergänzende Tickets und Voucher können zum Reisedossier gehören; deren automatische Beschaffung ist nicht als MVP-Pflicht beschlossen.

## Umfang

| Bereich | Arbeitsgrundlage |
| --- | --- |
| Buchungsquelle | Nezasa; API-Funktion durch Nutzer bestätigt. Produktionsadapter der finalen Anwendung noch zu bauen. |
| Ausgabe | Neues, editierbares DOCX. Zielvorlage, Formatvorlagen und unterstützte Word-Umgebung offen. |
| Verarbeitung | Gebuchte Leistungen und tatsächlichen Reiseablauf korrekt darstellen; Regelkatalog offen. |
| Kontrolle | Travel Agent prüft, ergänzt und finalisiert in Word. |
| Redaktionelle Inhalte | Azure als Quelle für Bilder, Hinweise und Querverweise angefordert; benötigte Inhaltsarten im ersten MVP noch festzulegen. |
| Weitere Templates | Optionaler Konzeptvorschlag, keine Pflicht. |
| Personalisierung / weitere Kanäle | Zukunftskontext; nicht aus der Vision in den MVP übernehmen. |

Stack, Oberfläche und Betriebsmodell der finalen Anwendung sind noch nicht beschlossen. Die aktuellen Implementierungen und Beispiele sind in [README](../README.md) verzeichnet.

## Fachliche Leitplanken

- Gebucht, offen, inkludiert und bezahlt sind unterschiedliche Aussagen. Keine davon aus einer anderen ableiten.
- Buchungsfakten und redaktionelle Ergänzungen unterscheidbar halten.
- Fehlende Daten nicht durch erfundene Zeiten, Leistungen oder Reservierungen ersetzen.
- Zimmer-/Reisendenzuordnungen erhalten; ähnliche Leistungen sind nicht automatisch Dubletten.
- Der alte Nezasa-Word-Export zeigt Probleme, ist keine Zielvorlage.
- Freie Änderungen in Word müssen praktikabel bleiben. Ein Rückimport in andere Kanäle ist nicht beschlossen.

## Vorgeschlagene Abnahme

| Fall | Nachweis nach fachlicher Konkretisierung |
| --- | --- |
| Inhalt | Relevante Hotels, Leistungen und Reisetage gegen einen geprüften Quelldatensatz abgleichen. |
| Status / Lücken | Offene, stornierte oder unvollständige Leistungen sowie fehlende Angaben nach abgestimmter Regel kennzeichnen oder behandeln. |
| Reisetag | Ein Fall A → B zeigt Transport und Übernachtung verständlich; Regeln für Zeitzonen und Nachtfahrten sind festgelegt. |
| Check-in / Check-out | Problem am bisherigen Export reproduzieren und die fachlich gewünschte Darstellung nachweisen. |
| Word-Bearbeitung | Hinweise verlängern, Text hinzufügen/entfernen, speichern und erneut öffnen; Tabellen, Absätze und Seitenfluss bleiben nutzbar. |
| Operativer Ablauf | Ein Travel Agent kann das erzeugte Dokument prüfen und reisefertig finalisieren. |
| Effizienz | Vergleichbare Reisen vor/nach Einführung bearbeiten; Zeit und Qualität dokumentieren. |

Benötigte Entscheidungen mit Zuständigkeit und Auswirkung: [OPEN_DECISIONS](OPEN_DECISIONS.md).

## Nutzenschätzung

Aktuelle Einschätzung aus der Management-Antwort (S8): heute ca. 10–30 Minuten Nachbearbeitung, in Einzelfällen 45 Minuten; zunächst ungefähr **50 % weniger Aufwand** durch sauberes Word. Daraus ergeben sich rechnerisch meist 5–15 Minuten Ersparnis. Dies ist ungemessen und keine Abnahmegrenze. Die früher genannten bis zu 80 % bleiben im [Konzeptkontext](concepts/PROJECT_VISION.md).
