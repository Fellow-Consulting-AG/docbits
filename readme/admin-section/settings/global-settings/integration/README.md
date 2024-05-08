# Integration

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 08.39.14.png" alt=""><figcaption></figcaption></figure>

## API-Schlüssel

* **Schlüssel**: Dies ist der eindeutige Bezeichner, den externe Anwendungen verwenden, um auf die API von Docbits zuzugreifen. Er ist entscheidend für die Authentifizierung von Anfragen, die von anderen Softwareanwendungen an Docbits gestellt werden.
* Hier können je nach spezifischem Bedarf und Sicherheitsprotokollen Aktionen wie Anzeigen, Neugenerieren oder Kopieren des API-Schlüssels durchgeführt werden.

## SSO (Single Sign-On) Service Provider-Einstellungen

* **Entity-ID**: Dies ist der Bezeichner für Docbits als Dienstanbieter in der SSO-Konfiguration. Er identifiziert Docbits eindeutig innerhalb des SSO-Frameworks.
* **SLO (Single Logout) URL**: Die URL, an die SSO-Sitzungen gesendet werden, um sich gleichzeitig von allen über SSO verbundenen Anwendungen abzumelden.
* **SSO-URL**: Die URL, die für das Initiieren des Single Sign-On-Prozesses verwendet wird.
* Aktionen wie "Zertifikat herunterladen" und "Metadaten herunterladen" stehen zur Verfügung, um die erforderlichen Sicherheitszertifikate und Metadateninformationen für die Einrichtung und Aufrechterhaltung der SSO-Integration zu erhalten.

{% hint style="info" %}
Siehe [SSO-Einrichtung](../../../setup/sso-configuration.md)
{% endhint %}

## Identity Service Provider-Einstellungen

* **Mandanten-ID**: Diese kann verwendet werden, wenn Docbits mit Cloud-Diensten integriert, die eine Mandantenkennung erfordern, um Daten zu verwalten und auf Konfigurationen zuzugreifen, die spezifisch für das Unternehmen sind, das Docbits verwendet.
* **Datei hochladen**: Ermöglicht es dem Administrator, Konfigurationsdateien oder andere erforderliche Dateien hochzuladen, die die Integration mit einem Identitätsanbieter erleichtern.
* **Konfigurieren**: Ein Button zum Anwenden oder Aktualisieren der Einstellungen nach Änderungen oder dem Hochladen neuer Konfigurationen.

{% @jira/embed url="https://fellowpro.atlassian.net/browse/DOCB-2488" %}
