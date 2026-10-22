# Technische Referenz: Nezasa JSON-Fetcher

Beschreibt die lokale Implementierung in [app/nezasa_fetch_ui.py](../app/nezasa_fetch_ui.py), keinen vollständigen Nezasa-Datenvertrag. Einrichtung und Testbefehle stehen zentral in der [Entwicklungsanleitung](../../../docs/DEVELOPMENT.md).

## Eingaben und Aufruf

Tkinter-Oberfläche mit Distribution Channel, API-Benutzername, Booking ID, maskiertem Passwort und „Fetch & Save JSON“. Alle Felder sind erforderlich.

| Eingabe | Verarbeitung in der GUI |
| --- | --- |
| Distribution Channel | Kleinbuchstaben; nur `a-z`, `0-9` und `-` bleiben erhalten. |
| Booking ID | Leerraum entfernen, Kleinbuchstaben; nur `a-z`, `0-9`, `_` und `-` bleiben erhalten. |
| Benutzername | Führenden und nachfolgenden Leerraum entfernen. |
| Passwort | Unverändert einschliesslich Leerzeichen übergeben. |

`NEZASA_API_USERNAME` und `NEZASA_DISTRIBUTION_CHANNEL` können beim Programmstart Werte vorbelegen. Das Passwort wird zur Laufzeit eingegeben und bleibt nach einem Abruf im maskierten Feld; es wird nicht als Konfiguration gespeichert. Die Bereinigung von Channel und ID erfolgt in `on_fetch`; direkte Aufrufer der Hilfsfunktionen müssen passende Werte übergeben.

## API-Aufruf und Antwortprüfung

| Eigenschaft | Implementiertes Verhalten |
| --- | --- |
| Methode und URL | `GET https://{channel}.tripbuilder.app/bookings/v1.13/{booking_id}`; kein `/api/`-Segment |
| Header | `Accept: application/vnd.api+json` |
| Authentifizierung | HTTP Basic Auth; keine OAuth-Client-Zugangsdaten |
| Timeout | `timeout=30` an requests; kein Gesamtzeitlimit für den vollständigen Export |
| Erfolg | Ausschliesslich HTTP 200, parsebares JSON und bestandene Mindestprüfung |

Die Mindestprüfung verlangt ein Objekt ohne `errors`-Feld sowie `data` als Objekt mit `type="booking"`, passender angefragter `id` als String und `attributes` als Objekt. Falls vorhanden, muss `included` ein Array sein. Es werden keine fachlichen Status, Beziehungen, Pflichtinhalte oder Preise validiert; insbesondere prüft der Code nicht, ob jede Leistung bestätigt ist. Zusätzliche Felder bleiben erhalten.

## Ausgabe und Ersetzen

Ausgabename: `booking_<bereinigte_booking_id>.json`. Die erste vorhandene Verzeichnisoption wird verwendet:

1. `%USERPROFILE%\Desktop`
2. `%USERPROFILE%\OneDrive\Desktop`
3. `%OneDrive%\Desktop`, falls gesetzt
4. Benutzerverzeichnis als Fallback

Es gibt keinen „Speichern unter“-Dialog. Die JSON-Werte werden ohne Mapping gespeichert: UTF-8, Einrückung mit zwei Leerzeichen, abschliessender Zeilenumbruch. Ursprüngliche HTTP-Antwortbytes und Formatierung werden nicht erhalten.

`save_booking_json` schreibt eine temporäre Datei im Zielverzeichnis, führt `flush` und `fsync` aus und ersetzt das Ziel mit `os.replace`. Ein erfolgreicher erneuter Export ersetzt dieselbe Datei. Bei Serialisierungs-, Schreib- oder Ersetzungsfehlern bleibt der bisherige Export erhalten; im `finally`-Block wird die temporäre Datei entfernt. Dieser Ablauf bietet keine Versionshistorie oder Sicherung. Die Antwortprüfung erfolgt vor dem Aufruf der Speicherfunktion in `fetch_booking_json`.

## Fehler und Diagnose

Die GUI zeigt Fehler als Meldungsfenster; dauerhaftes technisches Logging ist nicht implementiert.

| Fehler | Anzeige / erster Prüfpunkt |
| --- | --- |
| Fehlende requests-Abhängigkeit | Installationshinweis; vollständigen Befehl aus der Entwicklungsanleitung nutzen. |
| Netzwerkfehler | Fehlermeldung mit Exception-Text; Erreichbarkeit prüfen. |
| HTTP 401 | Passwort, Benutzer und BookingAPI-Rolle prüfen. |
| HTTP 404 | Booking ID und Channel prüfen; verwendete URL wird angezeigt. |
| Anderer HTTP-Status | Statuscode und bis zu 800 Zeichen Antworttext. |
| Ungültiges JSON | Meldung und bis zu 800 Zeichen Antworttext. |
| Ungültige Buchungshülle oder abweichende ID | Meldung; keine neue Ausgabedatei. |
| Speicherfehler | Exception-Text; Zielverzeichnis, Zugriffsrechte und Dateisperren prüfen. |

Erfolg wird mit dem gespeicherten Pfad gemeldet. Antwortauszüge, URLs und Exception-Texte können sensible Angaben enthalten; Supportmaterial vor Weitergabe bereinigen.

## Grenzen und Prüfungen

- HTTP-Aufruf und Speichern laufen synchron im GUI-Thread; die Oberfläche kann währenddessen blockieren.
- Keine automatischen Wiederholungen, Batchverarbeitung, Azure-Anbindung, Word-/PDF-Erzeugung oder automatische Anonymisierung.
- Lokale Exporte können Personen-, Kontakt-, Preis- und Zugangsinformationen enthalten. Sie bleiben ausserhalb des öffentlichen Git; siehe [SECURITY.md](../SECURITY.md).
- [Offline-Tests](../../../tests/test_nezasa_fetcher.py) prüfen Abrufparameter, Antwort-/Fehlerfälle, Passwortübergabe, Erhalt der Beispieldaten und Schutz vorhandener Dateien bei Fehlern. Sie ersetzen keinen interaktiven GUI- oder Live-API-Test.
