# Come Creare l'Accesso al Database per un Utente Specifico dell'Organizzazione

### **1. Accedere a Docbits** <a href="#id-1.-login-to-the-docbits" id="id-1.-login-to-the-docbits"></a>

1. Vai alla pagina di accesso della tua applicazione.
2. Inserisci le tue credenziali (nome utente e password) per accedere.

### **2. Accedere alle Impostazioni** <a href="#id-2.-access-the-settings" id="id-2.-access-the-settings"></a>

1. Una volta effettuato l'accesso, individua l'icona **Impostazioni** (ingranaggio ⚙️) nella barra laterale sinistra.
2. Clicca su **Impostazioni** per aprire il pannello di configurazione del sistema.

### **3. Aprire il Modulo di Elaborazione Documenti** <a href="#id-3.-open-the-document-processing-module" id="id-3.-open-the-document-processing-module"></a>

1. Nelle **Impostazioni**, individua la sezione **Elaborazione Documenti**.
2. Sotto **Elaborazione Documenti**, trova e clicca sull'opzione **Modulo**.
   * Questo aprirà la pagina di configurazione del modulo pertinente dove potrai procedere con la creazione dell'utente per il database.

<figure><img src="../../../../../.gitbook/assets/docbits_db_access_creation.png" alt="Docbits Db Access Creation"><figcaption></figcaption></figure>

### 4. Passaggi per Abilitare e Accedere all'Utente Documenti AI e Database: <a href="#id-4.-steps-to-enable-and-access-the-ai-document-and-database-user" id="id-4.-steps-to-enable-and-access-the-ai-document-and-database-user"></a>

1. **Attivare Funzionalità**:
   * Usa gli interruttori sulla destra per abilitare o disabilitare funzionalità specifiche:
     * **Magazzino Documenti AI**: Attiva questo per abilitare l'accesso alle funzionalità relative all'AI.
     * **Accesso DB**: Attiva questo per concedere l'accesso al database all'utente.

<figure><img src="../../../../../.gitbook/assets/image (1) (1) (1) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

2. **Credenziali del Database**:
   * La dashboard fornisce i seguenti dettagli di connessione al database:
     * **Nome utente**: Viene visualizzato un nome utente univoco.
     * **Password**: Assicurati che la password sia archiviata o copiata in modo sicuro.
     * **Database**: È il nome del Database.
     * **Host**: Nome Host.
     * **Porta**: È la Porta.
     * **Modalità SSL:** La connessione richiede `sslmode=require` per una comunicazione sicura.
3. **Copiare le Credenziali**:
   * Usa le icone di copia accanto a ogni campo per copiare rapidamente le credenziali da utilizzare nel tuo client database o applicazione.
4. **Connessione tramite DBeaver:**
   *   Connettersi tramite Host

       * scegli PostgreSQL

       <figure><img src="../../../../../.gitbook/assets/image (2) (1) (1) (2) (1) (1).png" alt=""><figcaption></figcaption></figure>

       * Compila le informazioni richieste

       <figure><img src="../../../../../.gitbook/assets/image (4) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

       * passa alla scheda SSL e seleziona Usa SSL. Scorri verso il basso fino alla modalità SSL e seleziona require

       <figure><img src="../../../../../.gitbook/assets/image (3) (1) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>
   *   Connettersi tramite URL

       * Compila le informazioni richieste:
         - sostituisci Host con le informazioni host fornite
         - sostituisci Porta con le informazioni porta fornite
         - sostituisci Database con le informazioni database fornite
         - per Nome utente seleziona le informazioni nome utente fornite
         - per Password seleziona le informazioni password fornite

       <figure><img src="../../../../../.gitbook/assets/image (5) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>
5. **Testare la Connessione**:
   * Clicca sul pulsante **"Test Connessione"** per assicurarti che le credenziali e i dettagli di connessione siano corretti.
   * Se il test ha esito positivo, procedi con la connessione.
6. **Esplorare il Database**:
   * Una volta connesso, naviga alla sezione **schema** o **tabelle** nel tuo client database.
   * Controlla le tabelle disponibili.
