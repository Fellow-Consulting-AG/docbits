# Elenco dei valori

## Panoramica

La funzione **Elenco dei valori** consente di creare e gestire set di valori predefiniti. Questo è particolarmente utile per configurare i menu a discesa nella sezione [**Campi**](../global-settings/document-types/fields/), che possono essere utilizzati in seguito nella **Validazione dei campi**.

Questi elenchi possono essere personalizzati per diverse sotto-organizzazioni e supportano più lingue, offrendo flessibilità attraverso **DocBits**.

## Come Accedere?

Puoi accedere all'**Elenco dei valori** navigando su **Impostazioni → Elaborazione dei documenti → Elenco dei valori**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_list_of_values.png)

## Come Aggiungere o Cancellare un Elenco

### Creare un Nuovo Elenco di Valori

1.  Clicca su **Nuovo** nell'angolo in alto a destra dello schermo.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_1.png)
2. Inserisci un **Nome** per il tuo elenco.
3. _(Opzionale)_ Seleziona una **Sotto-organizzazione** per la quale l'elenco dovrebbe essere attivo.
4.  Clicca su **Risparmiare** per creare l'elenco.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_2.png)

### Come Cancellare un Elenco

Per cancellare un elenco, clicca sull'icona del cestino accanto all'elenco corrispondente.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_13.png)

<mark style="color:red;">**Nota**</mark>: L'elenco verrà cancellato immediatamente. Gli elenchi contrassegnati con il tag [**Standard**](list-of-values.md#elenchi-e-righe-definiti-dal-sistema) non possono essere cancellati.

## Come Aggiungere, Modificare o Rimuovere Valori da un Elenco Esistente

Puoi gestire i valori in un **Elenco dei valori** esistente utilizzando uno dei seguenti metodi:

* [**Aggiungere valori manualmente**](list-of-values.md#aggiungere-valori-manualmente) – Inserisci i valori singolarmente tramite l'interfaccia.
* [**Importare valori da un file CSV**](list-of-values.md#importare-valori-da-un-file-csv) – Carica un file CSV per aggiungere più valori contemporaneamente.

### Aggiungere Valori Manualmente

1.  Clicca sull'elenco che desideri modificare.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_3.png)
2.  Clicca su **Azioni**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_4.png)
3.  Clicca su **Aggiungi riga**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_5.png)

Ora puoi specificare più proprietà per ogni voce:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_6.png)

**Valore**: Questo è il modo in cui l'elemento verrà memorizzato internamente all'interno di **DocBits**. Rimane lo stesso in tutte le lingue e funge anche da testo di visualizzazione predefinito durante la validazione dei campi se non viene specificata alcuna etichetta per la lingua selezionata.

**Etichetta**: Questo è il testo visualizzato nella schermata di validazione, in base alla lingua selezionata. Se non è disponibile alcuna etichetta per la lingua attiva in DocBits, il sistema predefinirà la visualizzazione del **Valore**.

**Lingua**: Specifica la lingua in cui verrà visualizzata l'etichetta.\
Una spiegazione più dettagliata può essere trovata [qui](list-of-values.md#aggiungere-traduzioni-ai-tuoi-valori).

**Sotto-organizzazioni**: Specifica per quale **sotto-organizzazione** la riga dovrebbe essere attiva. Se lasciata vuota, la riga sarà disponibile per tutte le organizzazioni.

**Sinonimi**: Qui puoi specificare valori aggiuntivi che aiutano a formare il tuo documento.\
Ad esempio, se **EUR** è il tuo **valore** principale, puoi aggiungere EURO e € come **sinonimi**. Quando il documento viene addestrato utilizzando uno di questi **sinonimi**, **DocBits** riconoscerà automaticamente e selezionerà EUR come valore corrispondente dal tuo elenco. <mark style="color:red;">**Nota**</mark>: Ogni sinonimo deve essere confermato premendo **Invio** per aggiungerlo all'elenco.

4.  Dopo aver inserito tutte le proprietà desiderate, clicca sul pulsante **Risparmiare** per aggiungere la riga.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_11.png)

### Importare Valori da un File CSV

Per aggiungere più valori contemporaneamente tramite importazione CSV:

1.  Clicca sull'elenco che desideri aggiornare.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_3.png)
2.  Clicca su **Azioni**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_4.png)
3.  Clicca su **Caricare CSV**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_7.png)
4. Clicca su **File** per cercare e selezionare il file CSV che desideri caricare.
5. Scegli il **Delimitatore** appropriato utilizzato nel file CSV (`;` o `,`).
6.  Clicca su **Caricare** per importare i valori.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_8.png)

### Modificare Valori Esistenti

1. Trova la riga che desideri modificare.
2. Clicca sui tre punti nella colonna **Azioni**.
3.  Seleziona **Modifica** dal menu a discesa.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_10.png)
4. Apporta le modifiche necessarie.
5.  Clicca su **Risparmiare** per applicare le tue modifiche.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_11.png)

### Cancellare Valori

1. Trova la riga che desideri cancellare.
2. Clicca sui tre punti nella colonna **Azioni**.
3.  Seleziona **Cancellare** dal menu a discesa.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_12.png)

<mark style="color:red;">**Nota**</mark>: La riga verrà cancellata immediatamente. Le righe contrassegnate con il tag [**Predefinito**](list-of-values.md#elenchi-e-righe-definiti-dal-sistema) non possono essere cancellate.

## Aggiungere Traduzioni ai Tuoi Valori

Puoi aggiungere quante più traduzioni ci sono lingue supportate in **DocBits**.

Per aggiungere una traduzione:

1.  Clicca sull'icona del più (+).

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_14.png)
2.  Seleziona una lingua dal menu a discesa.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_15.png)
3.  Inserisci la traduzione desiderata nel campo **Etichetta**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_16.png)
4.  Per aggiungere un'altra traduzione, clicca di nuovo sull'icona del più (+).

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_17.png)
5.  Per rimuovere una traduzione, clicca sull'icona del cestino.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_18.png)
6.  Quando hai finito, clicca sul pulsante **Risparmiare** per salvare le tue traduzioni.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_19.png)

<mark style="color:red;">**Nota**</mark>: Se non è disponibile alcuna **Etichetta** per la lingua attiva, DocBits predefinirà la visualizzazione del **Valore**.

## Elenchi e Righe Definiti dal Sistema

Alcuni elenchi sono pre-creati dal sistema e sono contrassegnati con il tag **Standard**. Questi elenchi non possono essere cancellati, ma puoi aggiungere nuove righe a essi e rimuovere quelle appena aggiunte se necessario.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_9.png)

All'interno di questi elenchi standard, alcune righe sono contrassegnate con il tag **Predefinito**: queste sono voci definite dal sistema. Puoi aggiungere nuove **etichette** in diverse lingue, ma queste righe predefinite non possono essere cancellate.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_20.png)
