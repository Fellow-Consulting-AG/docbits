# ZUGFeRD 1.0, 2.1 und 2.3

{% embed url="https://youtu.be/AxrHNEmmXtg" %}
DocBits E-Invoice Tutorial: Process XRechnung / ZUGFeRD (Factur-X), Validate Data & Automate Workflows
{% endembed %}

## **Unterstützte Versionen von ZUGFeRD**

Derzeit unterstützte Versionen von ZUGFeRD sind:

* **1.0**
* **2.1** (konform mit FACTUR-X 1.0.05)
* **2.3** (konform mit FACTUR-X 1.07.2)

#### Standardaktivierung und -änderung

Der ZUGFeRD-Standard ist standardmäßig immer aktiv, kann aber bei Bedarf angepasst werden.

### **Schritte zum Anpassen der ZUGFeRD-Einstellungen:**

1. Navigieren Sie zu **Einstellungen → Globale Einstellungen → Dokumenttypen → Rechnung**.
2.  Klicken Sie auf **E-Doc**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/zugferd_1.png)
3. Es erscheint eine Liste aller verfügbaren E-Docs.
4.  Suchen Sie die **ZUGFeRD**-Version, die Sie ändern möchten.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/zugferd_2.png)

## **Extraction Transformation und XML-Pfad-Konfiguration:**

In den Einstellungen der **Extraction Transformation** können Sie den Pfad definieren, um bestimmte Informationen innerhalb der XML-Datei zu finden und sie in einer neuen Struktur zu speichern, wodurch der Zugriff auf die Daten erleichtert wird.\
<mark style="color:red;">**Hinweis**</mark>: Wenn Sie diese Funktionalität verwenden, müssen Sie in der **Preview** und im **Extraction Path** die neu erstellten XML-Pfade verwenden, nicht die ursprünglichen XML-Pfade.

### **Schritte zum Anpassen der Extraction Transformation Datei:**

1. Öffnen Sie die **Extraction Transformation**.
2. Erstellen Sie einen neuen Entwurf, indem Sie auf das **Stiftsymbol** klicken.
3. Wählen Sie den neu erstellten Entwurf aus.
4. Erstellen Sie entweder ein neues Feld oder bearbeiten Sie ein bestehendes.
5. Legen Sie den gewünschten Pfad für die Datenextraktion fest.
6. Klicken Sie auf **Speichern**.

### Wichtige Hinweise:

* Die **Preview-Datei** wird nur für **FACTUR-X** verwendet, nicht für **ZUGFeRD**. ZUGFeRD verwendet das originale **PDF**.

## Preview PDF Konfiguration

Die **Preview PDF Konfiguration** wird verwendet, um eine für Benutzer lesbare Version des Dokuments zu erzeugen. Sie können sie mit HTML an Ihre Bedürfnisse anpassen.

### **Schritte zum Anpassen der Preview-Datei:**

1. Öffnen Sie die **Preview**.
2. Erstellen Sie einen neuen Entwurf, indem Sie auf das **Stiftsymbol** klicken.
3. Wählen Sie den neu erstellten Entwurf aus.
4. Erstellen Sie entweder ein neues Feld oder bearbeiten Sie ein bestehendes.
5. Legen Sie den gewünschten Pfad für die Datenextraktion fest.
6. Klicken Sie auf **Speichern**.

## Extraction Paths Konfiguration

Die **Extraction Paths Konfiguration** wird verwendet, um Daten zu extrahieren und Felder im **Validierungsbildschirm** zu befüllen, wie z. B. die Rechnungstabelle oder Felder, die im Rechnungslayout konfiguriert sind.

### **Schritte zum Anpassen** **der Extraction Paths**:

1. Öffnen Sie die **Extraction Paths**.
2. Erstellen Sie einen neuen Entwurf, indem Sie auf das **Stiftsymbol** klicken.
3. Wählen Sie den neu erstellten Entwurf aus.
4. Erstellen Sie ein neues Feld oder bearbeiten Sie ein bestehendes.
5.  Die linke Seite steht für die **DocBits Feld-ID**, welche Sie finden unter **Einstellungen → Globale Einstellungen → Dokumenttypen → Rechnung → Felder**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/zugferd_3.png)

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/zugferd_4.png)
6. Die rechte Seite steht für den **Pfad zu dem Feld**, das in der Extraction Transformation erstellt wurde.
7. Klicken Sie auf **Speichern**.

Durch das Befolgen dieser Schritte stellen Sie eine genaue Datenextraktion und Validierung für ZUGFeRD-Rechnungen sicher.
