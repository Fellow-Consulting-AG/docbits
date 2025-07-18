# Email in entrata

## Attivazione dell'Email in entrata per l'Elaborazione dei documenti

Per iniziare a utilizzare l'email in entrata per l'elaborazione dei documenti, segui questi passaggi:

1. **Vai alle Impostazioni**: Inizia navigando nel menu **Impostazioni** dell'app.
2. **Seleziona Elaborazione dei documenti**: Sotto le impostazioni, scegli **Elaborazione dei documenti** per accedere alle opzioni di configurazione correlate.
3. **Apri Moduli**: Nella sezione Elaborazione dei documenti, fai clic su **Moduli**.
4. **Scorri fino al Tipo di documento**: Scorri verso il basso fino a trovare **Tipo di documento**.
5. **Attiva l'Email in entrata**: Trova **Email in entrata** e attivala attivando l'interruttore.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/inbound_emails_1.png)

## Configurazione dell'Email in entrata per l'Importazione dei documenti

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/inbound_emails_2.png)

Dopo aver attivato l'email in entrata, configura le impostazioni per controllare come vengono importati i documenti. Ecco come:

1. **Torna all'Elaborazione dei documenti**: Nelle impostazioni, naviga verso **Elaborazione dei documenti**.
2.  **Seleziona Importazione**: Scegli **Importazione** per accedere alle impostazioni dell'email in entrata.

    Vedrai le seguenti opzioni:

    * **Campo Email**: Questo campo visualizza un indirizzo email unico, generato dal sistema, basato sul tuo ID organizzazione. Il formato è `org_id@environment.inbound.docbits.com`. Invia o inoltra email con documenti a questo indirizzo per l'importazione automatizzata.
    * **Importazione del documento solo da e-mail predefinite**: Attiva questa opzione per limitare le importazioni alle email ricevute solo da indirizzi specifici e predefiniti.
    * **Rispondere a questa e-mail se l'importazione non può essere effettuata**: Attiva questa opzione se desideri che il sistema risponda automaticamente quando un tentativo di importazione fallisce.
3. **Risparmiare Impostazioni**: Dopo aver configurato queste opzioni, fai clic su **Risparmiare** per applicarle.

## E-mail predefinite

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/inbound_emails_3.png)

Quando l'opzione **Importazione del documento solo da e-mail predefinite** è abilitata, puoi gestire quali indirizzi email sono autorizzati a inviare documenti all'email in entrata.

1. **Inserisci Email Autorizzate**: Nel campo **Metti e-mail qui**, digita ogni indirizzo email che desideri autorizzare.
2. **Assegna a Sotto-organizzazione (Opzionale)**:
   * Se non viene selezionata alcuna sotto-organizzazione, il documento sarà assegnato all'organizzazione principale.
   * Se viene selezionata una sotto-organizzazione, il documento sarà diretto solo a quella sotto-organizzazione.
3. **Aggiungi Email**: Fai clic su **Aggiungi** per salvare ogni email nell'elenco degli indirizzi autorizzati.
4. **Cancellare Email**: Per rimuovere un'email autorizzata, fai clic su **Cancellare** accanto all'entrata dell'email.

Con questa configurazione, i documenti provenienti da indirizzi email non autorizzati verranno ignorati, garantendo che solo fonti specifiche possano inviare documenti per l'importazione.

## **Rispondere a questa e-mail se l'importazione non può essere effettuata**

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/inbound_emails_4.png)

Se abiliti **Rispondere a questa e-mail se l'importazione non può essere effettuata**, appare un campo aggiuntivo dove puoi inserire un indirizzo email. Questo indirizzo email riceverà una notifica se un tentativo di importazione di documenti fallisce, permettendoti di rimanere informato su eventuali problemi nel processo di importazione.

1. **Abilita Notifica di Fallimento**: Attiva **Rispondere a questa e-mail se l'importazione non può essere effettuata**.
2. **Inserisci Email di Notifica**: Nel nuovo campo, inserisci l'indirizzo email dove desideri ricevere le notifiche di fallimento.

Con questa funzione abilitata, eventuali tentativi di importazione falliti attiveranno una risposta automatica all'email specificata, aiutandoti a risolvere rapidamente i problemi di importazione.

**Dopo aver configurato tutte le impostazioni, non dimenticare di fare clic su Risparmiare per applicare le tue modifiche.**
