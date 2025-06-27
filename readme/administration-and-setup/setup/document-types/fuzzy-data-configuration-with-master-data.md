# Fuzzy Data Konfiguration mit Masterdaten

## **Überblick**

Jeder Dokumententyp hat seine eigenen Standardkonfigurationen und muss separat eingerichtet werden. Während dieses Beispiel die Einrichtung für **Rechnungen** erläutert, gilt derselbe Prozess für alle Dokumententypen.

## Um Fuzzy-Daten zu konfigurieren, navigieren Sie zu:

Einstellungen → Globale Einstellungen → Dokumententypen → Rechnung → Felder → Masterdateneinstellungen → Masterdaten nachschlagen

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fhnn2NcPGzVkUO0mLQWTy%252Fimage.png%3Falt%3Dmedia%26token%3De2f87385-fc48-4149-9bef-ca917a7328bd\&width=768\&dpr=4\&quality=100\&sign=116ee1da\&sv=2)

## **Standardnachschlagen**

Es gibt **vier Standardnachschlagegruppen** für Rechnungen:

1. **Firmendaten**
2. **Kopf der Bestellung**
3. **Lieferant**
4. **Steuercode**

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F4VxYFu8M62dXi6qGsPl3%252Fimage.png%3Falt%3Dmedia%26token%3Db2bc4690-805b-4b19-aa89-73f315889d88\&width=768\&dpr=4\&quality=100\&sign=835f513a\&sv=2)

Jede Gruppe enthält spezifische Felder. Klicken Sie auf eine Gruppe, um sie zu **erweitern** und die Felder anzuzeigen. Standardnachschlagegruppen sind mit einem **"Standard" Tag** gekennzeichnet.

## **Status der Nachschlagekonfiguration**

* **Aktive Konfigurationen** sind mit einem **"Aktiviert" Tag** markiert.
* **Deaktivierte Konfigurationen** sind mit einem **"Deaktiviert" Tag** markiert.

## **Voraussetzung: Import von Masterdaten**

Damit Fuzzy-Daten korrekt funktionieren, müssen die relevanten **Masterdaten** importiert werden. Ohne dies hat das System keine Referenzdaten zur Verwendung. Hier erfahren Sie, wie Sie Masterdaten importieren:

{% content-ref url="../../../setup/importing-customer-master-data/" %}
[importing-customer-master-data](../../../setup/importing-customer-master-data/)
{% endcontent-ref %}

## **Verwalten von Nachschlagegruppen**

Jede Nachschlagegruppe ist standardmäßig **aktiviert**, kann jedoch durch Klicken auf die drei Punkte geändert werden:

* **Deaktivieren** → Deaktiviert eine Gruppe. _(Nur für aktivierte Gruppen verfügbar)_
* **Aktivieren** → Aktiviert eine Gruppe. _(Nur für deaktivierte Gruppen verfügbar)_
* **Duplizieren** → Erstellt eine Kopie, die modifiziert werden kann, ohne das Original zu beeinflussen.
* **Anzeigen** → Zeigt Informationen wie den **Dokumententyp**, zu dem es gehört, und die **Nachschlagetabelle**, die verwendet wird. _(Nur für Standardgruppen verfügbar)_
* **Bearbeiten** → Verfügbar für **nicht standardmäßige** Gruppen. Ermöglicht das Ändern von Gruppendetails.
* **Löschen** → Entfernt die Gruppe vollständig. _(Nur für nicht standardmäßige Gruppen)_

## **Erstellen einer neuen Nachschlagekonfiguration**

Es gibt **zwei Möglichkeiten**, eine Nachschlagekonfiguration zu erstellen:

1.  **Duplizieren einer vorhandenen Nachschlagegruppe**\


    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FZUlPcWGrx1oITQS3tgZP%252Fimage.png%3Falt%3Dmedia%26token%3D59fb300d-836e-40d0-84b7-4a405cf7f321\&width=768\&dpr=4\&quality=100\&sign=3442db8f\&sv=2)

    * Dies kopiert alle Informationen und Felder aus einer vorhandenen Gruppe.
    * Es muss nur ein **neuer Name** angegeben werden.
2.  **Erstellen einer Nachschlagegruppe von Grund auf neu**\


    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FNbEpo2p5Q8D1d7DUchBF%252Fimage.png%3Falt%3Dmedia%26token%3D401314b5-44d0-47df-b3e6-69fea83cce82\&width=768\&dpr=4\&quality=100\&sign=1d0ce322\&sv=2)

    * Klicken Sie auf **"Nachschlagekonfiguration erstellen"**.
    * Füllen Sie die erforderlichen Details aus:
      * **Konfigurationsname**
      * **Nachschlagetabelle** (Zu verwendende Masterdatentabelle)
      * **Konflikthandler** (Wählen Sie einen: Beste Punktzahl, Keine Rückgabe, Erste Rückgabe)
      * **Kontexttyp** (Kopf oder Zeile) benötigt Kontext
      * **Alles finden** (Kontrollkästchenoption) benötigt Kontext

## **Verwalten von Feldern innerhalb einer Nachschlagegruppe**

Jede Gruppe enthält Felder, die je nachdem, ob es sich um Standardfelder oder benutzerdefinierte Felder handelt, **hinzugefügt, entfernt, bearbeitet oder angezeigt** werden können.

### **Standardfelder**

*   Gekennzeichnet mit einem **"Standard" Tag**.\


    <div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fh37McVpB0tBo5wqiAttR%252Fimage.png%3Falt%3Dmedia%26token%3Dcabce083-83a5-4881-a64f-88a8757df49b&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=b3739019&#x26;sv=2" alt="" width="375"></div>
* **Kann nur angezeigt**, nicht bearbeitet oder gelöscht werden.

### **Nicht-Standardfelder**

* Können durch Klicken auf die drei Punkte und Auswahl von **Bearbeiten** oder **Entfernen** **bearbeitet oder gelöscht** werden.

### **Hinzufügen eines neuen Feldes**

**Hinweis:** Sie können Felder innerhalb von Standard-Nachschlagekonfigurationen erstellen.

Um ein neues Feld innerhalb einer Gruppe hinzuzufügen:

1.  Klicken Sie innerhalb der relevanten Gruppe auf **"Erstellen"**.\


    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FvmIXTEQQHKKNbvTJj1b4%252Fimage.png%3Falt%3Dmedia%26token%3D8569867b-9f5b-4865-90bd-f2e41e846979\&width=768\&dpr=4\&quality=100\&sign=603cb7df\&sv=2)
2. Geben Sie die folgenden Details an:
   * **Nachschlagefeld** → Spaltenname aus der Masterdaten-Nachschlagetabelle.
   * **Validierungsfeld** → Entsprechendes DocBits-Feld.
   * **Übergeordnetes Feld** → _(Weitere Details erforderlich)_
   * **Suchoperator** → Wählen Sie einen:
     * Smart
     * Enthält
     * Genau
     * Beginnt mit
     * Endet mit
   * **Kontrollkästchen:**
     * **Automatischer Auslöser** → Wenn aktiviert, wird dieses Feld automatisch aktualisiert, wenn ein anderes Feld in einer anderen Nachschlagekonfiguration dieselbe Spalte teilt.
     * **Durchsuchbar** → Aktiviert das Feld als **Fuzzy-Daten**-Feld, das Suchen im Masterdaten-Nachschlagen ermöglicht (blaues Symbol im Validierungsbildschirm).

## **Letzter Schritt: Hinzufügen von Feldern zum Layout**

Nachdem Sie die Fuzzy-Datenfelder konfiguriert haben, **stellen Sie sicher, dass Sie sie mithilfe des Layout-Editors zum Layout hinzufügen**. Wenn Felder nicht zum Layout hinzugefügt werden, stehen sie nicht zur Verfügung.\


{% content-ref url="../../settings/global-settings/document-types/layout-manager/" %}
[layout-manager](../../settings/global-settings/document-types/layout-manager/)
{% endcontent-ref %}
