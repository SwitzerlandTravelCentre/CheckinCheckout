# Integration Nezasa-Fetcher

Stand: 22.10.2026. S6: Der Nutzer ordnet [NezasaToWord](https://github.com/SwitzerlandTravelCentre/NezasaToWord) als Fetcher für den Aufbau und den Export der Nezasa-JSONs ein und verlangt die Integration in CheckinCheckout.

## Übernommener Stand

Die Komponente liegt unter [components/nezasa-fetcher](../components/nezasa-fetcher/README.md). Es ist eine eingebettete Quellkopie, kein Git-Submodul und keine automatische Synchronisation. Sie kann nach einem normalen Clone dieses Repositorys ohne weiteren Git-Schritt gestartet werden.

Upstream: SwitzerlandTravelCentre/NezasaToWord, Branch main, Commit 2920216ffbdd647cf6e5f06caaec79b0cb45db3c. Die sieben übernommenen Dateien sind in [UPSTREAM.md](../components/nezasa-fetcher/UPSTREAM.md) mit Git-Blob-Hashes dokumentiert und unverändert importiert. Das Originalrepository bleibt separat bestehen.

## Einordnung im Projekt

~~~text
Booking ID + Distribution Channel + API-Zugang
    -> Nezasa Booking API
    -> lokaler JSON-Export (Fetcher)
    -> spätere Verarbeitung / Mapping
    + freigegebene Azure-Inhalte
    -> spätere DOCX-Erzeugung und manuelle Finalisierung
~~~

Der erste Schritt ist als vorhandener Python-/Tkinter-Prototyp integriert. Azure-Inhaltsabruf, fachliches Mapping, Word-/PDF-Erzeugung und ein automatisierter Gesamtworkflow sind noch nicht implementiert. Die bisherige Aussage „kein Anwendungscode“ ist damit überholt.

Upstream beschreibt Word-Erzeugung ausdrücklich als pausiert. Das beschreibt den dortigen Implementierungsstand und ersetzt nicht die dokumentierte langfristige CheckinCheckout-Produktvision. Der aktuelle Integrationsschritt ergänzt ausschliesslich den vorhandenen Fetcher.

## Einrichtung und Start ab Repository-Wurzel

Benötigt werden Python 3, Tkinter und requests. Eine von IT unterstützte Python-Version verwenden. Upstream legt keine genaue unterstützte Mindestversion fest; geprüft wurde mit dem bereitgestellten Python-3.12.14-Runtime.

~~~powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r components/nezasa-fetcher/requirements.txt
.\.venv\Scripts\python.exe components/nezasa-fetcher/app/nezasa_fetch_ui.py
~~~

Einzugeben sind Distribution Channel, API-Benutzer, Booking ID und API-Passwort. Optional werden Benutzername und Channel über NEZASA_API_USERNAME und NEZASA_DISTRIBUTION_CHANNEL vorbelegt. Passwörter werden zur Laufzeit eingegeben, nicht in diesem Repository gespeichert.

Die [Upstream-README](../components/nezasa-fetcher/README.md) enthält Startbefehle relativ zur Komponentenwurzel. Die oben genannten Befehle gelten von der CheckinCheckout-Wurzel aus.

## Beobachteter Abrufvertrag

Der geprüfte Quellcode implementiert:

| Eigenschaft | Wert |
| --- | --- |
| Methode | GET |
| URL | https://{distribution-channel}.tripbuilder.app/bookings/v1.13/{booking_id} |
| Header | Accept: application/vnd.api+json |
| Authentifizierung | HTTP Basic Auth |
| Request-Timeout | 30 Sekunden, an requests übergeben |
| Erfolg | HTTP 200, JSON wird eingelesen und neu serialisiert gespeichert |
| Fehler | Spezifische Meldungen für 401/404; sonst Status/Antwortauszug, Netzwerk- und JSON-Fehler |
| Datei | booking_<booking_id>.json |

Dies ist der Vertrag des übernommenen Clients, keine eigenständige Bestätigung des heutigen Nezasa-Serververtrags oder der tatsächlichen Berechtigungen im STC-Tenant. Die Upstream-Dokumentation nennt die BookingAPI-Rolle; IT muss den Zugang für den vorgesehenen Channel prüfen. Entra-Zugriff für Azure Storage und Nezasa-Basic-Auth sind getrennte Authentifizierungswege.

## Ausgabe und Weiterverarbeitung

Die GUI sucht Desktop-Verzeichnisse in der Reihenfolge USERPROFILE/Desktop, USERPROFILE/OneDrive/Desktop, OneDrive/Desktop und fällt auf das Benutzerverzeichnis zurück. Der ermittelte Pfad kann innerhalb von OneDrive liegen; IT muss die Zulässigkeit der Ablage von Buchungsdaten bestätigen. Ein erneuter Export derselben ID überschreibt die bestehende Datei.

Die Antwort wird ohne fachliches Mapping als JSON gespeichert. Einlesen und erneutes Serialisieren erhalten die JSON-Daten, aber nicht die ursprünglichen HTTP-Antwortbytes oder Formatierung. Der Fetcher anonymisiert nicht, verändert keine Preise und prüft kein vollständiges Buchungsschema.

Neue reale Exporte bleiben ausserhalb des öffentlichen Git. Die bereinigten [Beispieldateien](../examples/nezasa/README.md) sind bewusst von echten Fetcher-Ausgaben getrennt.

## IT-Betrieb und Grenzen

- Arbeitsplatz benötigt HTTPS-Ausgang zu dem freigegebenen <channel>.tripbuilder.app. Das ist unabhängig vom privaten Netzwerkzugang zur vorgeschlagenen Azure-Inhaltsablage.
- API-Benutzer und Channel werden von IT / Nezasa freigegeben; Secrets über interne Verfahren bereitstellen.
- Keine Azure-Dienste, Uploads oder automatischen Jobs werden durch diesen Desktop-Client eingerichtet.
- Die GUI führt den HTTP-Aufruf synchron aus und kann währenddessen blockieren; sie hat keine automatische Wiederholungs- oder Batchlogik.
- Fehlermeldungen können Antwortauszüge enthalten. Screenshots und Supportmeldungen vor Weitergabe auf Kunden- und Zugangsdaten prüfen.
- Die Vorgaben zur kleinen Dateiliste und zur Pause von Word-Experimenten in der importierten Spezifikation beschreiben Upstream; für dieses Gesamtprojekt gelten die eigenen Projektunterlagen.

## Prüfung und spätere Updates

~~~powershell
.\.venv\Scripts\python.exe -B -m unittest discover -s tests -v
~~~

Tests simulieren HTTP und prüfen Abrufparameter, Fehlerfälle sowie den Export der anonymisierten Beispiele ohne Struktur-/Wertänderung. Kein echter Nezasa-Zugriff und kein interaktiver GUI-Test sind Bestandteil dieser Prüfung.

Prüfung bei der Integration am 22.10.2026: Alle sieben importierten Dateien entsprechen ihren Upstream-Git-Blob-Hashes. Sechs Offline-Tests erfolgreich, einschliesslich beider Beispiel-Exporte. Der normale unittest-Dateiimport war in der lokalen Agenten-Laufzeit durch einen Dateizugriffsfehler blockiert; dieselben Testfälle wurden mit in den Speicher geladenem Quellcode ausgeführt. GUI-Start und Live-Zugriff sind nicht verifiziert. Git-Ignore-Regeln für Rohbuchungen und Secrets sowie lokale Dokumentlinks geprüft.

Für Updates neuen Upstream-Commit auswählen, Änderungen und mögliche Secrets prüfen, die sieben Dateien kontrolliert übernehmen, UPSTREAM.md aktualisieren und Offline-Tests ausführen. Lokale Änderungen an übernommenen Dateien dokumentieren; keinen automatischen Merge von unbekannten Upstream-Ständen vornehmen.
