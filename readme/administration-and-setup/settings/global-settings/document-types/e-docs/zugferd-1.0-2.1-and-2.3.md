# ZUGFeRD 1.0, 2.1 e 2.3

## **Versioni supportate di ZUGFeRD**

Le versioni attualmente supportate di ZUGFeRD sono:

* **1.0**
* **2.1** (conforme a FACTUR-X 1.0.05)
* **2.3** (conforme a FACTUR-X 1.07.2)

#### Attivazione e modifica dello standard

Lo standard ZUGFeRD è sempre attivo per impostazione predefinita, ma puoi modificarlo se necessario.

### **Passaggi per modificare le Impostazioni di ZUGFeRD:**

1. Vai a **Impostazioni → Impostazioni globali → Tipi di documenti → Fattura**.
2.  Clicca su **E-Doc**.\\

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/zugferd_1.png)
3. Apparirà un elenco di tutti gli e-doc disponibili.
4.  Individua la versione di **ZUGFeRD** che vuoi modificare.\\

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/zugferd_2.png)

## **Configurazione di Extraction Transformation e percorso XML:**

Nelle **impostazioni di Extraction Transformation**, puoi definire il percorso per individuare informazioni specifiche all'interno del file XML e salvarle in una nuova struttura, facilitando l'accesso ai dati.\
**Nota:** Se utilizzi questa funzionalità, devi usare i nuovi percorsi XML creati, non i percorsi XML originali, in **Preview** e **Extraction Path**.

### **Passaggi per modificare il file di Extraction Transformation:**

1. Apri **Extraction Transformation**.
2. Crea una nuova bozza cliccando sull'**icona della matita**.
3. Seleziona la bozza appena creata.
4. Crea un nuovo campo o modifica uno esistente.
5. Imposta il percorso desiderato per l'estrazione dei dati.
6. Clicca **Risparmiare**.

### Note importanti:

* Il **file di Preview** è utilizzato solo per **FACTUR-X** e non per **ZUGFeRD**. ZUGFeRD userà il **PDF** originale.

## Preview PDF Configuration

La **Preview PDF Configuration** è utilizzata per generare una versione del documento leggibile dall'utente. Puoi personalizzarla con HTML per adattarla alle tue esigenze.

### **Passaggi per modificare il file di Preview:**

1. Apri **Preview**.
2. Crea una nuova bozza cliccando sull'**icona della matita**.
3. Seleziona la bozza appena creata.
4. Crea un nuovo campo o modifica uno esistente.
5. Imposta il percorso desiderato per l'estrazione dei dati.
6. Clicca **Risparmiare**.

## Configurazione di Extraction Paths

La **Configurazione di Extraction Paths** è utilizzata per estrarre i dati e popolare i campi nella **schermata di validazione**, come la tabella della Fattura o i campi configurati nel layout della Fattura.

### **Passaggi per modificare** **Extraction Paths**:

1. Apri **Extraction Paths**.
2. Crea una nuova bozza cliccando sull'**icona della matita**.
3. Seleziona la bozza appena creata.
4. Crea un nuovo campo o modifica uno esistente.
5.  La parte sinistra rappresenta l'**ID del campo DocBits**, che si trova in **Impostazioni → Impostazioni globali → Tipi di documenti → Fattura → Campi**.\\

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/zugferd_3.png)

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/zugferd_4.png)
6. La parte destra rappresenta il **percorso al campo** creato in Extraction Transformation.
7. Clicca **Risparmiare**.

Seguendo questi passaggi, puoi garantire un'estrazione dei dati e una validazione accurate per le Fatture ZUGFeRD.
