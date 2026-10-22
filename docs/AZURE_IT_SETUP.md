# Azure-Grundstruktur für IT-Support

Stand: 22.10.2026. Technischer Einrichtungsvorschlag für das Projekt Check In Check Out.

## Auftrag und Status

**Bestätigt durch den Nutzer (S5):** Eine von STC bereitgestellte Azure-Umgebung wird benötigt. Die Anwendung soll daraus Bilddaten, Hinweise und JSON-Dateien mit Querverweisen beziehen, beispielsweise die Zuordnung einer Referenz zu einem Package.

**Vorschlag dieses Dokuments:** Azure Blob Storage als gemeinsame Inhaltsablage mit getrennten Umgebungen, kontrollierter Veröffentlichung und lesendem Anwendungszugriff. Dies ist eine konkrete Basis zur Einrichtung durch IT, aber noch keine produktiv bereitgestellte Infrastruktur. Anwendungs-Hosting und Nezasa-Anbindung werden damit nicht festgelegt.

Die fachliche Ablagestruktur und der vorgeschlagene JSON-Vertrag stehen in [CONTENT_STRUCTURE.md](CONTENT_STRUCTURE.md). Synthetische Beispiele liegen unter [examples/content](../examples/content/README.md).

## Ressourcen pro Umgebung

Mindestens dev und prod getrennt aufsetzen. Eine zusätzliche test-Umgebung kann nach demselben Muster ergänzt werden. Bestehende STC-Landing-Zone, Netzwerk- und Namensstandards haben Vorrang vor den folgenden Namensbeispielen.

| Ressource | Namensbeispiel | Zweck / Einstellungsvorschlag |
| --- | --- | --- |
| Resource Group | rg-stc-cico-dev / rg-stc-cico-prod | Eigene Ressourcengruppe je Umgebung. |
| Storage Account | stcicocntdev<suffix> / stcicocntprd<suffix> | Allgemeiner StorageV2-Account, Standard, Block Blobs, Hot als Startpunkt; Namen global eindeutig, nur Kleinbuchstaben/Ziffern und ohne Platzhalterzeichen anlegen. |
| Redundanz | je Account | Dev: LRS als Startvorschlag; Prod: ZRS prüfen, sofern Zielregion und STC-Vorgaben dies unterstützen. IT dokumentiert Auswahl und Kosten. |
| Container | content-drafts | Redaktion und Vorprüfung; die Anwendung erhält darauf keinen Zugriff. |
| Container | content-published | Freigegebene, gemeinsam versionierte Inhaltspakete und aktiver Release-Verweis. |
| Private Endpoint | pe-cico-<env>-blob | Zugriff auf den Blob-Dienst aus dem freigegebenen Netzwerk. |
| Private DNS | privatelink.blob.core.windows.net | Bestehende zentrale Zone nutzen oder mit IT verknüpfen; Auflösung für Anwendung, Admins und Publisher sicherstellen. |
| Anwendungsidentität | mi-cico-<env>-reader | Managed Identity bei unterstütztem Azure-Hosting; andernfalls Entra-Workload-Identität passend zum späteren Host festlegen. |
| Publisher-Identität | id-cico-<env>-publisher | Eigene Identität für den kontrollierten Veröffentlichungsprozess. |
| Monitoring | bestehender oder dedizierter Log-Analytics-Workspace | Storage-Diagnose, Azure-Monitor-Alarme und zuständige IT-Alarmgruppe. |
| Key Vault | nur bei benötigten externen Secrets | Beispielsweise Nezasa-Zugang; nicht für einen Storage-Account-Schlüssel als Standardzugang. |

Tags: project=checkincheckout, environment, businessOwner, technicalOwner, costCenter und dataClassification. Konkrete Werte von IT / Fachverantwortung eintragen.

Hierarchischen Namespace (HNS) für diese Ablage **nicht aktivieren**: Die vorgeschlagenen Ordner sind Blob-Namenspräfixe; es werden keine Data-Lake-Funktionen benötigt. Blob-Versionierung wird bei HNS derzeit nicht unterstützt. [Microsoft: Blob versioning](https://learn.microsoft.com/en-us/azure/storage/blobs/versioning-overview)

## Zugriff und Netz

Vorgeschlagene Basiskonfiguration:

- HTTPS erzwingen, minimale TLS-Version 1.2 setzen.
- Anonymen Blob-Zugriff deaktivieren; beide Container privat.
- Static Website deaktiviert lassen.
- Shared-Key-Zugriff deaktivieren; Authentifizierung über Microsoft Entra ID.
- Öffentlichen Netzwerkzugriff deaktivieren und Private Endpoint für blob einrichten.
- Anwendung, Redaktion und Publisher müssen einen funktionierenden Netzwerkpfad und DNS-Auflösung besitzen, bevor diese Konfiguration abgenommen wird.

Entra-Authentifizierung und RBAC sind getrennt von der Netzwerkerreichbarkeit zu prüfen. [Microsoft: Entra-Zugriff](https://learn.microsoft.com/en-us/azure/storage/blobs/authorize-access-azure-active-directory), [Shared Key deaktivieren](https://learn.microsoft.com/en-us/azure/storage/common/shared-key-authorization-prevent)

Private Endpoints allein deaktivieren den öffentlichen Endpunkt nicht. Die Anwendung verwendet weiterhin den regulären Blob-Service-Hostnamen; DNS muss ihn im zugelassenen Netz auf die private IP auflösen. Bei Zugriff aus dem Firmennetz sind passende VPN-/ExpressRoute-Verbindungen und DNS-Weiterleitung erforderlich. [Microsoft: Private Endpoints](https://learn.microsoft.com/en-us/azure/storage/common/storage-private-endpoints)

**Abhängigkeit vom Anwendungsstandort:** Läuft die Anwendung später ausserhalb des angebundenen Azure-/Firmennetzes, braucht sie einen definierten privaten Zugang oder einen authentifizierten Backend-Dienst mit Zugriff auf die Ablage. Direkter Browserzugriff auf den Storage ist nicht Teil dieses Basisentwurfs. Diese Frage muss vor produktiver Einrichtung des Zugriffswegs entschieden werden.

## Berechtigungen

Zuweisungen auf Container-Ebene vornehmen, soweit möglich. Dev- und Prod-Identitäten trennen.

| Identität / Gruppe | content-drafts | content-published |
| --- | --- | --- |
| Anwendung | Keine | Storage Blob Data Reader |
| Redaktion | Storage Blob Data Contributor | Optional Storage Blob Data Reader |
| Publisher | Storage Blob Data Reader | Storage Blob Data Contributor |
| IT-Betrieb | Bei Bedarf Reader; Schreibzugriff für Wiederherstellung zeitlich begrenzt | Ebenso |
| Infrastruktur-Deployment | Nur erforderliche Management-Rechte | Datenzugriff nicht automatisch mitgeben |

Die Azure-Rolle „Contributor“ auf einer Ressource ersetzt keine Blob-Datenrolle. Redaktion kann beispielsweise Azure Storage Explorer mit Entra-Anmeldung verwenden, sofern der Netzwerkzugang eingerichtet ist. Der Publisher darf freigegebene Inhalte schreiben; die Rolle erzwingt keine Unveränderlichkeit. Dass veröffentlichte Release-Dateien nicht überschrieben werden, muss der Veröffentlichungsprozess durchsetzen. Keine gesperrte WORM-Retention ohne separat geklärten Bedarf aktivieren. [Microsoft: Entra und Datenrollen](https://learn.microsoft.com/en-us/azure/storage/blobs/authorize-access-azure-active-directory)

## Ablage und Veröffentlichung

~~~text
Storage Account je Umgebung
├── content-drafts
│   └── workspaces/<workspace-id>/...
└── content-published
    ├── control/current.json
    └── releases/<release-id>/
        ├── manifest.json
        ├── catalog.json
        ├── mappings.json
        └── images/<asset-id>/<dateiname>
~~~

Ein Release umfasst gemeinsam alle Bilder, Hinweise und Zuordnungen. Keine getrennten „latest“-Dateien je Inhaltstyp verwenden.

1. Redaktion erstellt oder aktualisiert einen Entwurf in content-drafts.
2. Fachverantwortung prüft Texte, Zuordnungen, Bildrechte und Sprachversionen.
3. Publisher prüft JSON-Vertrag, eindeutige IDs, gültige Referenzen, Dateiexistenz, Prüfsummen und unterstützte Dateiformate.
4. Publisher lädt ein vollständiges neues Release unter einer noch unbenutzten release-id hoch. Dateischreibzugriffe sollen create-only erfolgen.
5. Nach erfolgreicher Prüfung wird allein control/current.json auf das neue Release umgestellt. Bei bestehender Datei mit ETag / If-Match arbeiten; einen Konflikt nicht still überschreiben.
6. Anwendung liest den Verweis einmal je Erzeugungsvorgang und verwendet ausschliesslich dieses Release. Release-ID im internen Erzeugungsprotokoll erfassen.
7. Rollback: current.json kontrolliert auf ein vorheriges, vollständig vorhandenes und erneut geprüftes Release zurücksetzen.

Das Umschalten eines einzelnen Verweises vermeidet einen unvollständigen Mix mehrerer Releases. Es ist keine atomare Transaktion über mehrere Blobs. Optimistische Konkurrenzkontrolle über ETags muss durch den Publisher implementiert werden. Ein Azure-Upload allein bietet keinen fachlichen Freigabeprozess. [Microsoft: Parallelzugriffe und ETags](https://learn.microsoft.com/en-us/azure/storage/blobs/concurrency-manage)

## Wiederherstellung und Aufbewahrung

Vorgeschlagene Startwerte zur Bestätigung durch IT: Blob-Versionierung an, Blob Soft Delete 30 Tage, Container Soft Delete 30 Tage. Versionen und Soft Delete unterstützen die Wiederherstellung nach Überschreiben oder Löschen; sie erzeugen zusätzlichen Speicherbedarf. [Microsoft: Versionierung](https://learn.microsoft.com/en-us/azure/storage/blobs/versioning-overview), [Container Soft Delete](https://learn.microsoft.com/en-us/azure/storage/blobs/soft-delete-container-overview)

Zusätzlich eine unabhängige, kontrollierte Wiederherstellungsmöglichkeit für freigegebene Releases festlegen, etwa die bestehende STC-Backup-Lösung. Eine nur im selben Account vorhandene Version ist keine unabhängige Sicherung. Azure-Ressourcen können gegen versehentliches Löschen mit einem passenden Management-Lock geschützt werden; dies ersetzt keinen Schutz vor Löschen einzelner Blobs.

Keine pauschale Lifecycle-Löschung aktiver oder referenzierter Releases konfigurieren. Alte Releases erst entfernen, wenn Aufbewahrungsdauer, Rollback-Fenster und Bedarf zur Reproduktion älterer Dokumente berücksichtigt sind. Konkrete RPO-/RTO-Ziele sind mit dem Betrieb festzulegen und durch einen Restore-Test nachzuweisen.

## Betrieb und Monitoring

IT richtet Diagnoseeinstellungen für den Blob-Dienst und Azure-Monitor-Alarme ein. Benötigt werden ein Empfänger und ein kurzer Runbook-Verweis pro Alarm. [Microsoft: Blob-Monitoring](https://learn.microsoft.com/en-us/azure/storage/blobs/monitor-blob-storage)

| Beobachtung | Behandlungsvorschlag |
| --- | --- |
| Häufung 401/403 | Identität, Datenrolle, Token und Netzwerkzugriff prüfen. |
| Häufung 404 | Release-Verweis, Pfade und Veröffentlichungsprotokoll prüfen. |
| 5xx, Verfügbarkeit oder hohe Latenz | Storage-Metriken und Azure Service Health prüfen; Anwendung mit begrenzten Wiederholungen. |
| Ungültiges Mapping / fehlender Pflichtinhalt | Fachverantwortung und Publisher informieren; Anwendung meldet einen bearbeitbaren Fehler. |
| Speicher-/Kostenanstieg | Release-Mengen, Versionen, Log-Aufbewahrung und Datenabrufe prüfen. |

Konkrete Alarmgrenzen und Budgets nach Volumen und Betriebszeit festlegen. Infrastruktur-Monitoring ersetzt keine fachliche Prüfung der Zuordnungen. Logs enthalten technische IDs und Release-Referenzen, keine Buchungs-JSONs, Kundennamen oder Zugangstoken.

## Einrichtungsreihenfolge und IT-Abnahme

1. Subscription, Region, Kostenstelle, Betriebsverantwortliche und Anwendungs-Netzpfad bestimmen.
2. Resource Groups, Storage Accounts, Container und Tags über den STC-Infrastrukturprozess reproduzierbar anlegen.
3. Private Endpoint, DNS und Zugang für IT / Redaktion / Publisher / Anwendung herstellen.
4. Entra-Identitäten und Container-Rollen zuweisen; öffentliche und Shared-Key-Zugriffe deaktivieren.
5. Versionierung, Soft Delete, Monitoring, Budget und Wiederherstellung einrichten.
6. Ein vollständiges synthetisches Probe-Release veröffentlichen.
7. Folgende Prüfungen protokollieren:

| Test | Erwartung |
| --- | --- |
| Anwendung liest veröffentlichten Inhalt | current.json, manifest.json, Katalog, Mapping und Testbild erreichbar. |
| Anwendung schreibt oder liest drafts | Zugriff verweigert. |
| Redaktion schreibt in published | Zugriff verweigert. |
| Zugriff anonym / über Account-Key | Zugriff verweigert. |
| Externer Zugriff ohne genehmigten Netzpfad | Zugriff verweigert. |
| Falscher SHA-256 oder fehlende Datei | Release wird vor Aktivierung abgelehnt. |
| Doppelte / unbekannte Package-Referenz | Validierung meldet einen Fehler; keine zufällige Zuordnung. |
| Gleichzeitige Aktivierung | ETag-Konflikt erkannt. |
| Rollback und Wiederherstellung | Vorheriger Inhalt wieder lesbar; Ablauf und Dauer dokumentiert. |
| Anwendung in dev versucht prod zu lesen | Zugriff verweigert. |

Die semantischen Tests benötigen den späteren Publisher / Anwendungsadapter; sie sind nicht allein durch Azure-Konfiguration erfüllt.

## Bestehender Nezasa-Fetcher

Der [integrierte Desktop-Fetcher](FETCHER_INTEGRATION.md) nutzt separat Nezasa Booking API v1.13 mit Basic Auth. IT stellt API-Benutzer, freigegebenen Distribution Channel und HTTPS-Ausgang zu dessen tripbuilder.app-Host bereit. JSON wird lokal gespeichert; Azure ist noch nicht angebunden. Entra-Rechte ersetzen die Nezasa-Zugangsdaten nicht.

## Übergabe von IT an Entwicklung

IT liefert pro Umgebung: Subscription-/Tenant-ID, Resource-Group-Name, Region, Storage-Endpoint, Container-Namen, Identitätsreferenzen, RBAC-Scopes, Netz-/DNS-Anleitung, Betriebs- und Alarmkontakte sowie dokumentierte Restore-Methode. Diese Details gehören in die interne STC-Betriebsdokumentation; Secrets und interne Infrastrukturdetails nicht im öffentlichen Git hinterlegen.

Vorgeschlagene Anwendungskonfiguration ohne Secrets:

~~~text
CONTENT_BLOB_ENDPOINT=https://<account>.blob.core.windows.net
CONTENT_CONTAINER=content-published
CONTENT_CURRENT_BLOB=control/current.json
~~~

Keine produktiven Zugangsdaten im Repository. Diese Dokumentation hat keine Azure-Ressourcen erstellt und keinen Deployment-Vorgang ausgelöst.
