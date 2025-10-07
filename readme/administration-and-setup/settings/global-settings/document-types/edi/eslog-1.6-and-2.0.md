# eSLOG 1.6 e 2.0

### Versioni di Fattura eSLOG Supportate

Attualmente, **le versioni di fattura eSLOG 1.6 e 2.0** sono supportate.

Per la documentazione ufficiale di eSLOG, puoi fare riferimento a [questo link](https://epos.si/en/eslog).

Entrambe le versioni di eSLOG sono abilitate per impostazione predefinita.

### Passaggi per Modificare la Configurazione di eSLOG

**Configura eSLOG:**

* Naviga su **Impostazioni → Impostazioni Globali → Tipi di Documento → Fattura**.
*   Clicca su **E-Doc**.\


    <figure><img src="../../../../../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>
* Apparirà un elenco di tutti gli e-doc disponibili.
*   Individua la versione di eSLOG che desideri modificare.\


    <figure><img src="../../../../../.gitbook/assets/image (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### **Configurazione della Trasformazione e del Percorso XML:**

Nelle **impostazioni di trasformazione**, puoi definire il percorso per localizzare informazioni specifiche all'interno del file XML e salvarle in una nuova struttura, facilitando l'accesso ai dati. **Nota:** Se utilizzi questa funzionalità, devi utilizzare i nuovi percorsi XML creati, non i percorsi XML originali, nella **Anteprima** e nel **Percorso di Estrazione**.

#### **Passaggi per Modificare il File di Trasformazione:**

1. Apri la **Trasformazione**.
2. Crea una nuova bozza cliccando sull'**icona della matita**.
3. Seleziona la bozza appena creata.
4. Crea un nuovo campo o modifica uno esistente.
5. Imposta il percorso desiderato per l'estrazione dei dati.
6. Clicca su **Salva**.

### Configurazione dell'Anteprima PDF

La **Configurazione dell'Anteprima PDF** viene utilizzata per generare una versione leggibile dall'utente del documento. Puoi personalizzarla con HTML per soddisfare le tue esigenze.

#### **Passaggi per Modificare il File di Anteprima:**

1. Apri l'**Anteprima**.
2. Crea una nuova bozza cliccando sull'**icona della matita**.
3. Seleziona la bozza appena creata.
4. Crea un nuovo campo o modifica uno esistente.
5. Imposta il percorso desiderato per l'estrazione dei dati.
6. Clicca su **Salva**.

### Configurazione dei Percorsi di Estrazione

La **Configurazione dei Percorsi di Estrazione** viene utilizzata per estrarre dati e popolare i campi nella **schermata di validazione**, come la tabella delle fatture o i campi configurati nel layout della fattura.

#### **Passaggi per Modificare i Percorsi di Estrazione**:

1. Apri i **Percorsi di Estrazione**.
2. Crea una nuova bozza cliccando sull'**icona della matita**.
3. Seleziona la bozza appena creata.
4. Crea un nuovo campo o modifica uno esistente.
5.  Il lato sinistro rappresenta il **DocBits field ID**, che può essere trovato in **Impostazioni → Impostazioni Globali → Tipi di Documento → Fattura → Campi**.\


    <figure><img src="../../../../../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>
6. Il lato destro rappresenta il **percorso al campo** creato nella Trasformazione.
7. Clicca su **Salva**.
