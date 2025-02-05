# e-SLOG 1.6 und 2.0

## Unterstützte eSLOG Rechnungsversionen

Derzeit werden **eSLOG Rechnungsversionen 1.6 und 2.0** unterstützt.

Offizielle eSLOG Dokumentation finden Sie [hier](https://epos.si/en).

Beide eSLOG-Versionen sind standardmäßig aktiviert.

### Schritte zur Modifizierung der eSLOG-Konfiguration

**eSLOG konfigurieren:**

* Navigieren Sie zu **Einstellungen → Globale Einstellungen → Dokumenttypen → Rechnung**.
*   Klicken Sie auf **E-Doc**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FctcfxakxpfAcknvIueSQ%252Fimage.png%3Falt%3Dmedia%26token%3Dca599f1e-323d-4b61-99af-760f5f51a75d\&width=768\&dpr=4\&quality=100\&sign=3eee1abc\&sv=2)
* Eine Liste aller verfügbaren e-Dokumente wird angezeigt.
*   Suchen Sie die eSLOG-Version, die Sie modifizieren möchten.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FzWM10W6vAigJ44spm4ai%252Fimage.png%3Falt%3Dmedia%26token%3Db61fe4e5-517b-47da-89ca-13a53d370abf\&width=768\&dpr=4\&quality=100\&sign=9d2c40e3\&sv=2)

### **Transformation und XML-Pfadkonfiguration:**

In den **Transformationseinstellungen** können Sie den Pfad definieren, um spezifische Informationen innerhalb der XML-Datei zu lokalisieren und in einer neuen Struktur zu speichern, um den Zugriff auf die Daten zu erleichtern. **Hinweis:** Wenn Sie diese Funktionalität nutzen, müssen Sie die neu erstellten XML-Pfade verwenden, nicht die ursprünglichen XML-Pfade, in der **Vorschau** und im **Extraktionspfad**.

#### **Schritte zur Modifizierung der Transformationsdatei:**

1. Öffnen Sie die **Transformation**.
2. Erstellen Sie einen neuen Entwurf, indem Sie auf das **Stift-Symbol** klicken.
3. Wählen Sie den neu erstellten Entwurf aus.
4. Erstellen Sie entweder ein neues Feld oder modifizieren Sie ein bestehendes.
5. Setzen Sie den gewünschten Pfad für die Datenextraktion.
6. Klicken Sie auf **Speichern**.

### Vorschau-PDF-Konfiguration

Die **Vorschau-PDF-Konfiguration** wird verwendet, um eine lesbare Version des Dokuments zu erstellen. Sie können sie mit HTML anpassen, um Ihren Bedürfnissen gerecht zu werden.

#### **Schritte zur Modifizierung der Vorschau-Datei:**

1. Öffnen Sie die **Vorschau**.
2. Erstellen Sie einen neuen Entwurf, indem Sie auf das **Stift-Symbol** klicken.
3. Wählen Sie den neu erstellten Entwurf aus.
4. Erstellen Sie entweder ein neues Feld oder modifizieren Sie ein bestehendes.
5. Setzen Sie den gewünschten Pfad für die Datenextraktion.
6. Klicken Sie auf **Speichern**.

### Konfiguration der Extraktionspfade

Die **Konfiguration der Extraktionspfade** wird verwendet, um Daten zu extrahieren und Felder im **Validierungsbildschirm** auszufüllen, wie z.B. die Rechnungstabelle oder Felder, die im Rechnungslayout konfiguriert sind.

#### **Schritte zur Modifizierung der Extraktionspfade:**

1. Öffnen Sie die **Extraktionspfade**.
2. Erstellen Sie einen neuen Entwurf, indem Sie auf das **Stift-Symbol** klicken.
3. Wählen Sie den neu erstellten Entwurf aus.
4. Erstellen Sie ein neues Feld oder modifizieren Sie ein bestehendes.
5.  Die linke Seite repräsentiert die **DocBits-Feld-ID**, die Sie in **Einstellungen → Globale Einstellungen → Dokumenttypen → Rechnung → Felder** finden können.\


    <figure><img src="../../../../../.gitbook/assets/e-SLOG 1.6 und 2.0  (1).jpg" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/e-SLOG 1.6 und 2.0 1 (1).jpg" alt=""><figcaption></figcaption></figure>
6. Die rechte Seite repräsentiert den **Pfad zum Feld**, das in der Transformation erstellt wurde.
7. Klicken Sie auf **Speichern**.
