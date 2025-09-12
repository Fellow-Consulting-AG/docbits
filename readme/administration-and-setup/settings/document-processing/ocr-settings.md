# Impostazioni OCR

## Panoramica

Nelle impostazioni **OCR (Riconoscimento Ottico dei Caratteri)**, puoi configurare come viene applicato l'OCR durante l'elaborazione dei documenti. Questo include la specifica della qualità minima richiesta, la scelta se utilizzare il testo incorporato (e-text), la selezione della versione OCR e altro ancora. Questa pagina fornisce una spiegazione dettagliata di tutte le impostazioni disponibili.

## Come Accedere alle Impostazioni OCR

Per accedere alle impostazioni OCR:

*   Naviga a: **Impostazioni** → **Elaborazione dei documenti** → **Impostazioni OCR**

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_ocr.png)

## Qualità OCR

In questa sezione, puoi impostare la qualità minima del documento richiesta per l'elaborazione OCR regolando il cursore di qualità. Sposta il cursore a sinistra o a destra per diminuire o aumentare la soglia di qualità, rispettivamente.

Se un documento non soddisfa il livello di qualità definito, DocBits fornisce tre opzioni per gestirlo:

* **Correte Comunque**\
  Il documento verrà elaborato indipendentemente dalla sua qualità.
* **Eseguire Nuovamente Dopo la Conferma**\
  **DocBits** si fermerà e ti chiederà di confermare se procedere con l'elaborazione.
* **Lanciare l'Errore**\
  L'elaborazione del documento si fermerà completamente e verrà visualizzato un messaggio di errore, indicando che il documento non ha soddisfatto la soglia di qualità richiesta.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ocr_settings_1.png)

## Impostazioni Generali OCR

* **Utilizzare il Testo Elettronico, se Disponibile**\
  Quando abilitato, **DocBits** utilizzerà il testo elettronico incorporato (ad es., da PDF) invece di eseguire l'OCR. Questo migliora sia la velocità che l'accuratezza, poiché il testo viene estratto direttamente senza richiedere l'elaborazione OCR.
* **Utilizzare DESKEW se Disponibile**\
  Questa opzione corregge automaticamente l'allineamento dei documenti scansionati. Raddrizzare le immagini distorte aiuta a migliorare l'accuratezza dell'OCR.
*   **Versione AI OCR**\
    Ti consente di selezionare una versione specifica del motore OCR basato su AI.\
    Questo può essere utile se:

    * Non stai ottenendo i risultati desiderati con la versione attualmente selezionata.
    * Stai risolvendo problemi relativi alle prestazioni o all'accuratezza dell'OCR.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ocr_settings_2.png)

## Impostazioni OCR per le Tabelle

* **Utilizzare i Dati AI per le Tabelle, se Disponibili**\
  Quando abilitato, DocBits utilizzerà i dati OCR per le tabelle invece del testo elettronico incorporato (E-Text) — anche se l'impostazione **Utilizzare il Testo Elettronico, se Disponibile** è attivata.

## Impostazioni OCR per i Campi di Intestazione

* **Estrazione delle Regole di Utilizzo**\
  DocBits applicherà le tue regole di estrazione predefinite per identificare i campi di intestazione.
* **Utilizzare l'Estrzione AI**\
  DocBits utilizzerà l'AI per rilevare ed estrarre automaticamente i campi di intestazione.

**Ordine di Esecuzione:**\
Se entrambe le opzioni sono abilitate, **DocBits** eseguirà l'estrazione nel seguente ordine:\
**Estrazione delle Regole → Estrazione AI**\
\
<mark style="color:red;">**Nota**</mark>: Per i migliori risultati e un comportamento coerente, abilita entrambe le opzioni. Questo consente a **DocBits** di utilizzare sia metodi basati su regole che metodi basati su AI in combinazione durante l'estrazione dell'intestazione.
