# Modello AI

## Panoramica

L'impostazione **Modello AI** consente di definire quale modello AI viene utilizzato per impostazione predefinita per l'**estrazione sul campo** e l'**estrazione della tabella** durante l'elaborazione dei documenti.\
In questa sezione, puoi esaminare il costo in token per ciascun modello e vedere quale modello è attualmente assegnato a ciascun fornitore.

## Come Accedere

1.  Naviga su **Impostazioni** → **Elaborazione dei documenti** → **Classificazione ed estrazione**

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_classification_and_extraction.png)
2.  Scorri verso il basso fino alla sezione **Estrazione della tabella**

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_1.png)

## Opzioni del Modello AI

Puoi scegliere tra i seguenti modelli AI. Passa il mouse sull'icona informativa nell'interfaccia per visualizzare il costo in token per documento per il modello AI selezionato:

* **Full** – 2 token per documento
* **Fast** – 1 token per documento
* **Turbo** – 1 token per documento

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_2.png)

## Tabella di Assegnazione del Modello AI

Puoi anche configurare **modelli AI** specifici per fornitore direttamente nella schermata di **Convalida**, permettendoti di perfezionare l'accuratezza dell'estrazione per singoli fornitori.\
\
Per ulteriori informazioni, consulta la documentazione corrispondente [qui](../../../../end-user-and-partner-section/end-user-section/validation-screen/supplier-specific-ai-model-for-field-and-table-extraction.md).

La tabella di assegnazione visualizza le impostazioni del modello AI per ciascun fornitore e include i seguenti dettagli:

* **Supplier ID** – L'identificatore unico del fornitore
* **AI Model** – Il modello AI attualmente assegnato al fornitore
* **E-Text**: Indica se la funzione E-Text è abilitata
* **Action** – Contiene l'opzione per eliminare l'entrata

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_3.png)

### Elimina Entrata – Ripristina Impostazioni Specifiche del Fornitore

Per ripristinare l'impostazione del modello AI di un fornitore ai valori predefiniti:

1.  Clicca sull'icona del cestino nella colonna **Action** accanto all'entrata del fornitore.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_4.png)
2.  Apparirà una finestra di conferma—conferma di voler eliminare l'entrata.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_5.png)

Una volta eliminato, il fornitore tornerà a utilizzare il **modello AI** predefinito per l'**estrazione sul campo** e l'**estrazione della tabella**.
