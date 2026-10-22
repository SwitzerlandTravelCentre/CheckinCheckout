# Grenze zwischen Entwicklungs-Fetcher und Anwendung

Der [integrierte Fetcher](../components/nezasa-fetcher/README.md) erzeugt ausschliesslich lokale JSON-Testdaten. Die finale Anwendung wird ihren eigenen Abruf integrieren und direkt Word erzeugen, gegebenenfalls mit anderer technischer Umsetzung. Diese Trennung ist durch den Nutzer bestätigt (S7).

~~~text
Entwicklung: Fetcher -> Nezasa API -> lokales JSON
             -> separate Bereinigung -> öffentliche Testdaten

Finale Anwendung: integrierter Abruf -> Verarbeitung -> editierbares Word
~~~

Ein manueller JSON-Export ist kein erforderlicher Produktionsschritt. Der Fetcher implementiert keine fachliche Aufbereitung, Inhaltsanreicherung oder Word-Erzeugung. Aktueller Gesamtstand und Umfang: [README](../README.md) und [MVP](MVP.md).

## Zuständigkeit der Unterlagen

| Thema | Verbindlicher Einstieg für den aktuellen lokalen Stand |
| --- | --- |
| Runtime, Einrichtung, Start und Tests ab Repository-Wurzel | [DEVELOPMENT.md](DEVELOPMENT.md) |
| API, Eingaben, Antwortprüfung, Dateispeicherung und Fehler | [Technische Referenz](../components/nezasa-fetcher/docs/TECHNICAL_SPECIFICATION.md) |
| Quellstand und lokale Änderungen | [UPSTREAM.md](../components/nezasa-fetcher/UPSTREAM.md) |
| Bereinigte Beispielbuchungen und ihre Grenzen | [examples/nezasa](../examples/nezasa/README.md) |

Die Komponente ist eine eingebettete Quellkopie; ein normaler Clone genügt. Es gibt keine automatische Synchronisation mit NezasaToWord.

## Betrieb und Verifikation

- Die aktualisierte API funktioniert laut Nutzerbestätigung (S7). Diese Bestätigung ist von den Offline-Tests zu unterscheiden; ein zusätzlicher Live-API-Test und ein interaktiver GUI-Test wurden hier nicht durchgeführt.
- Der Arbeitsplatz benötigt HTTPS-Zugriff auf den freigegebenen `<channel>.tripbuilder.app`. Zugangsdaten werden intern bereitgestellt. Nezasa-Basic-Auth und Azure-Entra-Zugriff sind getrennte Authentifizierungswege.
- Exporte können im Desktop-/OneDrive-Verzeichnis oder Benutzerverzeichnis liegen und enthalten reale Buchungsdaten. Die Eignung dieser Ablage ist betrieblich zu klären; Roh-Exporte gehören nicht ins öffentliche Git.
- Die GUI meldet Fehler, führt aber kein dauerhaftes technisches Logging. Logging und Supportablauf der finalen Anwendung bleiben zu definieren.
- Der Fetcher richtet keine Azure-Ressourcen ein. Für die finale Anwendung müssen Host, Zugriffsweg und Berechtigungen gesondert festgelegt werden; siehe [offene Entscheidungen](OPEN_DECISIONS.md) und [Azure IT-Setup](AZURE_IT_SETUP.md).
