# Ricerca dei dati master

## Panoramica

La "Ricerca dei dati master" nelle tue Impostazioni di Elaborazione dei documenti consente un approccio completo e integrato alla gestione e convalida dei dati dei documenti, sincronizzandoli con il tuo sistema ERP Infor. Ecco come aiuta a snellire la convalida e il miglioramento dell'elaborazione dei documenti all'interno del tuo ambiente ERP:

1. **Gestione centralizzata dei dati**: Questa funzionalità funge da archivio centrale in cui è possibile archiviare e gestire dati provenienti da varie fonti come fornitori, indirizzi dei clienti, codici fiscali e altro. Fornisce un unico punto di riferimento per tutti i dati master, garantendo coerenza e accuratezza in tutta l'organizzazione.
2. **Convalida rispetto ai dati ERP**: Sincronizzando i dati master, come le informazioni del fornitore, da Infor a DocBits, puoi convalidare automaticamente i dati estratti dai documenti rispetto ai tuoi dati ERP. Ciò garantisce che le informazioni elaborate (come nomi dei fornitori, indirizzi e codici fiscali) corrispondano ai dati presenti nel tuo sistema ERP, riducendo al minimo errori e discrepanze.
3. **Favorisce l'automazione**: Disporre di un solido sistema di ricerca dei dati master aiuta ad automatizzare l'elaborazione dei documenti in arrivo. Ad esempio, gli ordini di acquisto o le fatture possono essere verificati automaticamente per la correttezza dei dati del fornitore, approvati se corrispondono oppure contrassegnati per revisione se vengono rilevate discrepanze.
4. **Migliora l'integrità dei dati**: Aggiornamenti regolari dal tuo sistema ERP alla Ricerca dei dati master assicurano che i dati utilizzati per l'elaborazione dei documenti siano aggiornati. Questo riduce il rischio di elaborare documenti basandosi su informazioni obsolete, migliorando così l'integrità complessiva delle transazioni aziendali.
5. **Efficienza nell'elaborazione dei documenti**: Con i dati master collegati direttamente e continuamente aggiornati, l'elaborazione dei documenti diventa più efficiente. I documenti possono essere classificati e instradati automaticamente in base ai criteri specifici impostati nei dati master, come termini specifici del fornitore o normative fiscali applicabili a diversi tipi di transazioni.

{% hint style="info" %}
Vedi qui come [importare i dati master](../../../infor-integration-and-configuration/importing-customer-master-data/)
{% endhint %}

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/master_data_lookup_1.png)

## **Accesso alla Ricerca dei dati master**

Per accedere alla sezione **Ricerca dei dati master**, vai a:\
**Impostazioni → Elaborazione dei documenti → Ricerca dei dati master**

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_mater_data_lookup.png)

## **Impostazioni**

Per accedere alle impostazioni della **Ricerca dei dati master**, fai clic su **Impostazioni** nell’angolo in basso a sinistra della schermata **Ricerca dei dati master**.\
Sono disponibili le seguenti opzioni di configurazione:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/master_data_lookup_2.png)

### **BOD del fornitore**

* **Consenti la sincronizzazione di più account fornitore**:
  * **Abilitato**:\
    Un singolo fornitore può avere più elementi `<FinancialParty>` nel BOD (Business Object Document), spesso a causa di più IBAN o conti finanziari associati. Quando questa impostazione è abilitata, tutte le voci `<FinancialParty>` del fornitore verranno estratte e salvate nella tabella dei fornitori, consentendo di archiviare più attributi finanziari.
  * **Disabilitato**:\
    Verrà estratto solo l'ultimo elemento `<FinancialParty>` trovato per il fornitore nel BOD. Eventuali attributi finanziari precedenti (ad esempio IBAN aggiuntivi) verranno ignorati e solo i dati dell'ultima occorrenza verranno salvati nella tabella dei fornitori.

### **Eliminazione dell'ordine di acquisto**

*   **Elimina ordine di acquisto dopo**: Specifica quando eliminare gli ordini di acquisto chiusi. Dopo l'intervallo di tempo selezionato, i record verranno rimossi automaticamente.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/master_data_lookup_3.png)
