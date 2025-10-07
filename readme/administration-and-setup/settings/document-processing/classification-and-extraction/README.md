# Classificazione ed estrazione

## Panoramica

Nelle Impostazioni di **Classificazione ed estrazione**, puoi:

* Abilitare la **Divisione del documento** basata su codici QR
* Configurare la **Formattazione degli importi**
* Configurare l'**Estrazione della tabella**
* Attivare/disattivare l'elaborazione di **ZUGFeRD** non supportati
* Definire Regole di classificazione speciali
* Monitorare i **Modelli AI** addestrati su misura utilizzati nel processo di classificazione

Questa pagina fornisce una spiegazione dettagliata di tutte le Impostazioni disponibili.

## **Accesso alle Impostazioni di Classificazione ed estrazione**

Per accedere alle Impostazioni di **Classificazione ed estrazione**, vai a:\
**Impostazioni → Elaborazione dei documenti → Classificazione ed estrazione**

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_classification_and_extraction.png)

## Divisione del documento

Nella sezione **Divisione del documento**, puoi configurare se un documento caricato debba essere suddiviso in più documenti ogni volta che un **Codice a barre** appare in una delle sue pagine.

Per attivare questa funzione:

1. Vai alla sezione **Divisione del documento**.
2.  Apri il menu a discesa.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_14.png)
3.  Seleziona **Dividere per codice a barre/QR-Code**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_15.png)

Avrai quindi la possibilità di:

* Selezionare uno o più tipi di Codice a barre da rilevare.
*   Specificare un modello regex che il Codice a barre deve corrispondere per attivare la Divisione del documento.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_16.png)

## Formattazione degli importi

Nella sezione **Formattazione degli importi**, hai due opzioni:

* **Consenti l'arrotondamento durante il confronto degli importi:**\
  Se abilitata, è consentita una tolleranza di ±0.5 durante il confronto degli importi.\
  Se disabilitata, si applica una tolleranza predefinita di ±0.05.
* **Richiedi corrispondenza esatta per il confronto degli importi:**\
  Se abilitata, gli importi devono corrispondere esattamente con tolleranza zero.\
  Se disabilitata, è consentita una tolleranza di ±0.05.

<mark style="color:red;">**Nota**</mark>: Solo una di queste Impostazioni può essere attiva alla volta.

## Estrazione della tabella

Puoi estrarre tabelle dai documenti abilitando **Estrazione della tabella** oppure **Estrazione della tabella AI**. Una tabella addestrata — sia basata su AI che manuale — sarà sempre collegata a un Fornitore specifico.

**Estrazione della tabella:** Attiva l'**Estrazione della tabella** manuale. Le tabelle devono essere addestrate manualmente.\
Scopri di più sull'addestramento manuale [qui](../../../setup/document-training/training-line-fields-table-training/defining-tables-and-columns.md).

**Estrazione della tabella AI:** Utilizza l'AI per estrarre automaticamente le tabelle. Se i risultati non sono sufficientemente accurati, si consiglia di passare a **Estrazione della tabella** per un controllo e un addestramento migliori.

**Estrazione della tabella per l'elemento di costo:** Quando abilitata, DocBits può estrarre elementi di costo dalle tabelle a livello di riga e classificarli di conseguenza.\
Spiegazione dettagliata disponibile [qui](table-extraction-for-costing-element.md).

**Estrazione automatica del codice fiscale:** Quando abilitata, il sistema compila automaticamente il campo **Codice fiscale** nella schermata di convalida — a condizione che sia configurato un campo per il codice fiscale.\
Ulteriori informazioni su questa Impostazione [qui](auto-extract-tax-code.md).

**Modello AI:** Consente di specificare quale **Modello AI** viene utilizzato per l'estrazione della tabella.\
Vedrai anche una tabella che mostra:

* Quali Fornitori stanno utilizzando quale Modello AI
* Se utilizzano E-Text
* Opzioni per Cancellare una voce o reimpostare i dati di addestramento

Questa Impostazione è spiegata in dettaglio [qui](ai-model.md).

## Documento elettronico

**Elaborazione di ZUGFeRD PDF non supportati:** Se abilitata, le versioni **ZUGFeRD** non supportate verranno elaborate come PDF standard e l'XML incorporato verrà ignorato.

L'elenco delle versioni **ZUGFeRD** supportate è disponibile [qui](../../global-settings/document-types/edi/zugferd-1.0-2.1-and-2.3.md).

## **Regole di classificazione**

Nella sezione **Regole di classificazione**, puoi definire Modelli **regex** e criteri specifici per aiutare il sistema a classificare automaticamente i documenti durante l'elaborazione.

Per accedere a questa sezione, fai clic sulla scheda **Regole di classificazione** nella parte superiore della pagina.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_1.png)

### **Aggiungi una nuova Regola di classificazione**

Per creare una nuova regola:

1.  Fai clic su **Aggiungi** nell'angolo in alto a destra.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_2.png)
2. Compila i seguenti campi:
   * **Modello**: Il modello regex che il sistema deve cercare per attivare la classificazione.
   * **Tipo**: Dove cercare il modello (ad es., **Codice a barre**).
   * **Organizzazione secondaria** _(opzionale)_: Specifica a quale organizzazione secondaria si applica la regola.
   * **Tipo di documento**: Definisci il tipo di documento da assegnare quando il modello viene riscontrato.
   *   **Tipo di documento secondario** _(opzionale)_: Specifica un sottotipo per una classificazione più dettagliata.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_3.png)
3.  Fai clic su **Risparmiare** per salvare la tua regola di classificazione.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_4.png)

### **Modifica una Regola di classificazione**

Per modificare una regola esistente:

1.  Fai clic sui tre puntini nella colonna **Azioni**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_5.png)
2.  Seleziona **Modifica**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_6.png)
3. Apporta le modifiche desiderate.
4.  Fai clic su **Risparmiare** per applicare gli aggiornamenti.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_4.png)

### **Cancellare una Regola di classificazione**

Per cancellare una regola:

1.  Fai clic sui tre puntini nella colonna **Azioni**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_5.png)
2.  Seleziona **Cancellare**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_7.png)

## Modelli AI

La sezione **Modelli AI** mostra tutti i modelli addestrati su misura che sono stati specificamente perfezionati per le tue esigenze.

### Accesso alla sezione Modelli AI

Per aprire questa sezione, fai clic sulla scheda **Modelli AI** situata nella parte superiore della pagina.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_8.png)

### Categorie di modelli

I modelli sono organizzati in categorie. Sotto il nome di ciascuna categoria è mostrato il numero di modelli che contiene.\
Fai clic su una categoria per visualizzarne i dettagli.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_9.png)

Nella parte superiore della pagina della categoria selezionata, vedrai informazioni chiave su ciascun modello:

* **Tipo**: Il tipo di modello.
* **Solo la prima pagina**: Indica se il modello elabora solo la prima pagina di un documento.
* **Versione**: Il numero di versione del modello.

### Tabella dei modelli

Tutti i modelli all'interno di una categoria sono elencati in una tabella, che include le seguenti informazioni:

* **Nome**: Il nome del modello.
* **Modello successivo**: Il modello che elaborerà ulteriormente l'output del modello corrente.
* **Tipo di documento**: Il tipo di documento principale assegnato dal modello durante la classificazione.
* **Sottotipi di documento**: I sottotipi in cui il documento viene ulteriormente classificato.
* **Priorità**: Il livello di priorità che determina la posizione del modello nella coda di classificazione.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_11.png)

### Modifica di un modello

Per modificare un modello:

1.  Fai clic sull'icona della penna nella colonna **Azioni** accanto al modello che desideri modificare.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_10.png)
2. Aggiorna i campi disponibili:
   * **Modello successivo**: Seleziona il modello che dovrebbe elaborare l'output del modello corrente.
   * **Tipo di documento**: Scegli il tipo di documento con cui il modello dovrebbe classificare l'input.
3.  Fai clic su **Risparmiare** per applicare le modifiche.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_12.png)
