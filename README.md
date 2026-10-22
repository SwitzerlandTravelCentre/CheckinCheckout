# Check In Check Out

Code der einzelnen Komponenten und gemeinsame Projektdokumentation für die Erstellung von Reiseunterlagen bei Switzerland Travel Centre.

## Aktueller Arbeitsstand

Kontextaufnahme, Stand 22.10.2026. Noch kein Anwendungscode und kein festgelegter Technologie-Stack. Die vorliegenden Quellen können veraltet sein; diese Dokumentation ist eine nachvollziehbare Arbeitsgrundlage, keine freigegebene Implementierungsspezifikation.

Der bisher beschriebene unmittelbare Fokus ist ein sauberer, stabil editierbarer DOCX-Export aus Nezasa für den operativen Einsatz durch Sales / Travel Agents. Die umfassendere Vision umfasst Anreicherung, Qualitätsprüfung, Personalisierung und weitere Ausgabekanäle. „Beyond PDF“ ist im gelieferten Kontext **on hold**.

## Einstieg für Entwickler

1. [Projektkontext](docs/PROJECT_CONTEXT.md): Problem, Begriffe, fachliche Leitplanken und Architekturvision.
2. [Vorläufiger MVP-Rahmen](docs/MVP.md): Umfang, vorgeschlagene Abnahmeszenarien und technische Klärungen.
3. [Quellen und offene Fragen](docs/SOURCES_AND_OPEN_QUESTIONS.md): Herkunft, Widersprüche und fehlende Entscheidungen.
4. [Nezasa-Beispielbuchungen](examples/nezasa/README.md): zwei bereinigte JSON-Exporte mit fiktiven Preisen.
5. [Azure-Basis für IT](docs/AZURE_IT_SETUP.md): Ressourcen, Zugriffsrollen, Betrieb und Abnahme.
6. [Inhaltsstruktur](docs/CONTENT_STRUCTURE.md): Bilder, Hinweise und Package-Querverweise.
7. [AGENTS.md](AGENTS.md): Arbeitsregeln für AI-Coder.

Neue Informationen werden in diese Dokumente eingearbeitet. Überholte Aussagen werden mit ihrer Ablösung nachvollziehbar gehalten; ungeklärte Angaben werden nicht zu Anforderungen hochgestuft.

## Repository

Quelle: https://github.com/SwitzerlandTravelCentre/CheckinCheckout

Die Aufteilung des späteren Codes in Komponenten wird festgelegt, sobald Implementierungsumfang und Schnittstellen geklärt sind. Fachliche Schichten allein legen weder Verzeichnisstruktur noch Deployment-Struktur fest.
