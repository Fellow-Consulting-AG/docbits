# Configurazione dei Dati Fuzzy con i Dati Principali

## **Panoramica**

Ogni tipo di documento ha le proprie configurazioni predefinite e deve essere impostato separatamente. Mentre questo esempio spiega la configurazione per le **Fatture**, lo stesso processo si applica a tutti i tipi di documenti.

## Per configurare i Dati Fuzzy, vai a:

Impostazioni → Impostazioni Globali → Tipi di Documento → Fattura → Campi → Impostazioni Dati Principali → Ricerca Dati Principali

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fhnn2NcPGzVkUO0mLQWTy%252Fimage.png%3Falt%3Dmedia%26token%3De2f87385-fc48-4149-9bef-ca917a7328bd\&width=768\&dpr=4\&quality=100\&sign=116ee1da\&sv=2)

## **Ricerche Predefinite**

Ci sono **quattro gruppi di ricerca predefiniti** per le fatture:

1. **Dati Aziendali**
2. **Intestazione Ordine di Acquisto**
3. **Fornitore**
4. **Codice Fiscale**

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F4VxYFu8M62dXi6qGsPl3%252Fimage.png%3Falt%3Dmedia%26token%3Db2bc4690-805b-4b19-aa89-73f315889d88\&width=768\&dpr=4\&quality=100\&sign=835f513a\&sv=2)

Ogni gruppo contiene campi specifici. Clicca su un gruppo per **espanderlo** e visualizzare i campi. I gruppi di ricerca predefiniti sono contrassegnati con un tag **"Predefinito"**.

## **Stato Configurazione Ricerca**

* Le **configurazioni attive** sono contrassegnate con un tag **"Attivato"**.
* Le **configurazioni disattivate** sono contrassegnate con un tag **"Disattivato"**.

## **Prerequisito: Importare i Dati Principali**

Per far funzionare correttamente i Dati Fuzzy, è necessario importare i **dati principali** pertinenti. Senza questo, il sistema non ha dati di riferimento da utilizzare. Ecco come importare i dati principali:

{% content-ref url="../../../infor-integration-and-configuration/importing-customer-master-data/" %}
[importing-customer-master-data](../../../infor-integration-and-configuration/importing-customer-master-data/)
{% endcontent-ref %}

## **Gestione dei Gruppi di Ricerca**

Ogni gruppo di ricerca è **attivato per impostazione predefinita** ma può essere modificato cliccando sui tre punti:

* **Disattiva** → Disattiva un gruppo. _(Disponibile solo per i gruppi attivati)_
* **Attiva** → Attiva un gruppo. _(Disponibile solo per i gruppi disattivati)_
* **Duplica** → Crea una copia che può essere modificata senza influenzare l'originale.
* **Visualizza** → Mostra informazioni come il **tipo di documento** a cui appartiene e la **tabella di ricerca** che utilizza. _(Disponibile solo per i gruppi predefiniti)_
* **Modifica** → Disponibile per i gruppi **non predefiniti**. Consente di modificare i dettagli del gruppo.
* **Elimina** → Rimuove completamente il gruppo. _(Solo per i gruppi non predefiniti)_

## **Creazione di una Nuova Configurazione di Ricerca**

Ci sono **due modi** per creare una configurazione di ricerca:

1.  **Duplica una ricerca esistente**

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FZUlPcWGrx1oITQS3tgZP%252Fimage.png%3Falt%3Dmedia%26token%3D59fb300d-836e-40d0-84b7-4a405cf7f321\&width=768\&dpr=4\&quality=100\&sign=3442db8f\&sv=2)

    * Questo copia tutte le informazioni e i campi da un gruppo esistente.
    * È sufficiente fornire un **nuovo nome**.
2.  **Crea una ricerca da zero**

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FNbEpo2p5Q8D1d7DUchBF%252Fimage.png%3Falt%3Dmedia%26token%3D401314b5-44d0-47df-b3e6-69fea83cce82\&width=768\&dpr=4\&quality=100\&sign=1d0ce322\&sv=2)

    * Clicca su **"Crea Configurazione di Ricerca"**.
    * Compila i dettagli richiesti:
      * **Nome Configurazione**
      * **Tabella di Ricerca** (Tabella Dati Principali da utilizzare)
      * **Gestore Conflitti** (Scegli uno: Miglior Punteggio, Nessun Risultato, Primo Risultato)
      * **Tipo Contesto** (Intestazione o Riga) necessita contesto
      * **Corrispondenza Totale** (Opzione casella di controllo) necessita contesto

## **Gestione dei Campi All'interno di un Gruppo di Ricerca**

Ogni gruppo contiene campi che possono essere **aggiunti, rimossi, modificati o visualizzati**, a seconda che siano campi predefiniti o campi personalizzati.

### **Campi Predefiniti**

*   Contrassegnati con un tag **"Predefinito"**.

    <div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fh37McVpB0tBo5wqiAttR%252Fimage.png%3Falt%3Dmedia%26token%3Dcabce083-83a5-4881-a64f-88a8757df49b&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=b3739019&#x26;sv=2" alt="" width="375"></div>
* **Possono essere solo visualizzati**, non modificati o eliminati.

### **Campi Non Predefiniti**

* **Possono essere modificati o eliminati** cliccando sui tre punti e selezionando **Modifica** o **Rimuovi**.

### **Aggiunta di un Nuovo Campo**

**Nota:** Puoi creare campi all'interno di configurazioni di ricerca predefinite.

Per aggiungere un nuovo campo all'interno di un gruppo:

1.  Clicca su **"Crea"** all'interno del gruppo pertinente.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FvmIXTEQQHKKNbvTJj1b4%252Fimage.png%3Falt%3Dmedia%26token%3D8569867b-9f5b-4865-90bd-f2e41e846979\&width=768\&dpr=4\&quality=100\&sign=603cb7df\&sv=2)
2. Fornisci i seguenti dettagli:
   * **Campo di Ricerca** → Nome colonna dalla tabella di ricerca dei dati principali.
   * **Campo di Convalida** → Campo DocBits corrispondente.
   * **Campo Genitore** → _(Ulteriori dettagli necessari)_
   * **Operatore di Ricerca** → Scegli uno:
     * Smart
     * Contiene
     * Esatto
     * Inizia con
     * Termina con
   * **Caselle di Controllo:**
     * **Attivazione Automatica** → Quando abilitato, se un altro campo in una diversa configurazione di ricerca condivide la stessa colonna, questo campo si aggiornerà **automaticamente** ogni volta che l'altro campo viene aggiornato
     * **Ricercabile** → Abilita il campo come campo **Dati Fuzzy**, consentendo ricerche nella ricerca dei dati principali (icona blu nella schermata di convalida).

## **Passo Finale: Aggiungere i Campi al Layout**

Dopo aver configurato i campi dei Dati Fuzzy, **assicurati di aggiungerli al layout utilizzando il Generatore di Layout**. Se i campi non vengono aggiunti al layout, non saranno disponibili per l'uso.

{% content-ref url="../../settings/global-settings/document-types/layout-manager/" %}
[layout-manager](../../settings/global-settings/document-types/layout-manager/)
{% endcontent-ref %}
