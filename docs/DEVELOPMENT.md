# Entwicklungsstart

Lesezeit für den Einstieg: README → diese Seite → passende [Beispiele](../examples/README.md). Umfang und Abnahmeentwurf stehen in [MVP](MVP.md); konkrete Blockaden in [OPEN_DECISIONS](OPEN_DECISIONS.md).

## Lokal starten

Befehle ab Repository-Wurzel in PowerShell. Verwende Python **3.12 mit Tkinter** als geprüfte Entwicklungsbasis (lokal geprüft: 3.12.14). Der Stack der finalen Anwendung ist damit nicht festgelegt.

~~~powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r components/nezasa-fetcher/requirements.txt
.\.venv\Scripts\python.exe -B -m unittest discover -s tests -v
~~~

Die Tests verwenden Standardbibliothek und Tkinter, simulieren HTTP und öffnen kein Fenster. Sie benötigen weder Nezasa-Zugang noch Azure. Fehlt Tkinter, die Python-Installation entsprechend ergänzen.

Für einen bewusst ausgelösten echten Testdatenexport:

~~~powershell
.\.venv\Scripts\python.exe components/nezasa-fetcher/app/nezasa_fetch_ui.py
~~~

Channel, API-Benutzer, Buchungs-ID und Passwort werden in der GUI eingegeben. Benutzer und Channel können über NEZASA_API_USERNAME und NEZASA_DISTRIBUTION_CHANNEL vorbelegt werden. Das Passwort bleibt eine Laufzeiteingabe. Ablage und Fehlerverhalten: [Fetcher-Referenz](../components/nezasa-fetcher/docs/TECHNICAL_SPECIFICATION.md).

## Wo arbeite ich?

| Pfad | Zweck |
| --- | --- |
| [components/nezasa-fetcher/app/nezasa_fetch_ui.py](../components/nezasa-fetcher/app/nezasa_fetch_ui.py) | Vorhandener API-Client, minimale Antwortprüfung, Dateiausgabe und GUI. |
| [tests/test_nezasa_fetcher.py](../tests/test_nezasa_fetcher.py) | Abrufvertrag, Fehlerfälle, Passwortübergabe und verlustfreies Speichern der Beispiele. |
| [tests/test_repository.py](../tests/test_repository.py) | Lokale Dokumentlinks, Beispielbeziehungen und Integrität des synthetischen Inhalts-Releases. |
| [examples/](../examples/README.md) | Bereinigte Buchungen und separat erfundene Inhaltsdaten; keine vollständigen Produktfixtures. |
| [docs/CONTENT_STRUCTURE.md](CONTENT_STRUCTURE.md) | Vorgeschlagener Vertrag für redaktionelle Inhalte und Package-Zuordnung. |
| [docs/AZURE_IT_SETUP.md](AZURE_IT_SETUP.md) | Technische IT-Einrichtungsgrundlage, keine vorhandene Bereitstellung. |
| [docs/concepts/](concepts/README.md) | Hintergrund, Quellen und frühere Aussagen; bei Bedarf lesen. |

Die finale Anwendung hat noch keinen Codeordner. Neue Komponenten erst mit einer konkreten Aufgabe und Schnittstelle anlegen; die fachlichen Schichten sind keine Vorgabe für mehrere Services.

## Zwei Arbeitsabläufe

~~~text
Entwicklung: Fetcher → Nezasa API → lokales JSON → separate Bereinigung → Testfixture

Zielanwendung: eigener Nezasa-Abruf → Verarbeitung + freigegebene Inhalte
              → DOCX → Prüfung und Bearbeitung durch Travel Agent
~~~

Ein manueller JSON-Export ist kein notwendiger Produktionsschritt. Der bestehende Python-Client ist eine nachvollziehbare Referenz für den Abruf, keine Vorgabe für die spätere Implementierung.

## Mit den Daten arbeiten

- Zuerst eine [Beispielbuchung](../examples/nezasa/README.md) wählen. Komponenten über die Ressourcenbeziehungen auflösen; mehrere Zimmer im selben Hotel nicht automatisch zusammenfassen.
- Gesamtstatus und Leistungsstatus getrennt behandeln. Alle sechs Beispiele enthalten Booked und Open; Deutsch, Englisch und Französisch sowie Kinder und Zahlungstransaktionen sind abgedeckt.
- Kalenderdaten, Zeitstempel und Zeitzonen nicht ungeprüft gleichsetzen. Tageszuordnung und Darstellung brauchen abgestimmte Regeln.
- Erweiterte Inhalte getrennt von den Quelldaten verarbeiten; keine Fixtures durch Anreicherung umschreiben.
- Das [Inhaltsbeispiel](../examples/content/README.md) demonstriert nur den vorgeschlagenen Release-Vertrag. Es ist nicht mit den Buchungsbeispielen verknüpft.
- Es gibt noch kein Ziel-DOCX, keine Bildfixture, keinen vollständigen Nezasa-Schemavertrag und keinen produktiven Publisher.

## Nächste sinnvolle Umsetzung

1. Sales liefert eine akzeptierte Zielvorlage und bestätigt Pflichtinhalte sowie Status-/Tagesregeln ([D01–D03](OPEN_DECISIONS.md)).
2. Einen kleinen, repräsentativen Reiseablauf als überprüfbaren Input/Output-Fall definieren.
3. Stack und Laufzeit für die finale Anwendung wählen ([D04](OPEN_DECISIONS.md)); ersten Weg vom Abruf zum DOCX umsetzen.
4. Redaktionelle Inhalte nach bestätigter Referenzsemantik anbinden ([D05–D06](OPEN_DECISIONS.md)).
5. Word-Bearbeitbarkeit mit Sales prüfen und den Finalisierungsaufwand im Pilot messen.

Das ist eine empfohlene Reihenfolge, keine freigegebene Sprintplanung. Fixture-Analyse und unabhängige technische Arbeit können sofort erfolgen.

## Prüfung vor Übergabe

~~~powershell
.\.venv\Scripts\python.exe -B -m unittest discover -s tests -v
git diff --check
~~~

Dokument-/Fixture-Prüfungen laufen mit demselben Testbefehl. Sie prüfen keine fachliche Vollständigkeit und garantieren keine Anonymisierung beliebiger neuer Daten. Bei Word-Implementierung kommen fachliche und visuelle Abnahmen hinzu. Bisherige Prüfergebnisse und Laufzeitgrenzen stehen im [Review](reviews/2026-10-22.md).
