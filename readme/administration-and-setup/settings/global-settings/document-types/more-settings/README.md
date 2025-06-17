# Altre impostazioni

## Panoramica

Nella sezione "Altre impostazioni", puoi trovare varie opzioni relative ai singoli tipi di documenti. Una volta attivata un'impostazione, si applicherà solo a quel tipo di documento specifico. Questa pagina fornisce una breve panoramica di cosa fa ciascuna impostazione.

## Come accedere

1.  Naviga su **Impostazioni** -> **Impostazioni globali** -> **Tipi di documenti**.

    <figure><img src="../../../../../.gitbook/assets/Calculate_PO_unit_price_1_it.png" alt=""><figcaption></figcaption></figure>
2.  Seleziona il tipo di documento desiderato e fai clic su **Altre impostazioni**.

    <figure><img src="../../../../../.gitbook/assets/Calculate_PO_unit_price_2_it.png" alt=""><figcaption></figcaption></figure>

## Estrazione della tabella

* **Saltare la convalida della tabella**: Consente di bypassare il processo di convalida per i dati della tabella, il che può essere utile in scenari in cui la convalida dei dati deve essere flessibile.

## Rilevamento dei duplicati

* [**Rilevamento di documenti doppi**](duplicate-document-handling.md): Questo ti consente di rilevare e gestire documenti duplicati.

## In revisione

* **Progetta il modulo di revisione**: Configura il layout e i campi che appaiono nei moduli di revisione utilizzati durante il processo di revisione del documento.

## Rifiuto

* **Progettare il modulo di rifiuto**: Configura il layout e i campi visualizzati nel modulo di rifiuto utilizzato durante il processo di revisione del documento.

## Generazione PDF

* **Modello di design**: Specifica il modello utilizzato per generare versioni PDF dei documenti, che può essere cruciale per l'archiviazione o la comunicazione esterna.

## Esportazione in formato PDF

* **Formato del file di esportazione**: Ti consente di specificare il formato PDF da utilizzare quando si esportano documenti.

## Approvazione

* **Approvare prima dell'esportazione**: Garantisce che i documenti debbano essere approvati prima di poter essere esportati dal sistema. Inoltre, puoi progettare il modello utilizzato per lo schermo di approvazione.
* **Approvare prima dell'esportazione V2**: Abilita l'Approvazione V2, consentendo l'uso di campi dinamici invece di quelli statici. Puoi anche personalizzare il modello dello schermo di approvazione.
* **Seconda approvazione**: Aggiunge un ulteriore livello di approvazione per una convalida aggiuntiva, migliorando il controllo sul processo di elaborazione dei documenti. Puoi anche personalizzare il modello utilizzato per lo schermo di approvazione.
* [**Timbro di approvazione**](approval/approval-stamp.md): Aggiunge un timbro al documento quando viene approvato.
* **Storia dell'approvazione**: Abilita la visualizzazione della storia dell'approvazione sia nello schermo di approvazione che nella convalida dei campi.

## Ordine di acquisto

* [**Tabella PO nel generatore di layout**](purchase-order/po-table-in-layout-builder.md): Abilita l'inclusione di tabelle degli ordini di acquisto nel generatore di layout per layout di documenti personalizzati.
* [**Controllo automatico degli aggiornamenti dell'OP**](purchase-order/auto-check-for-po-updates.md): Quando abilitato, il sistema visualizza un indicatore visivo nello schermo di corrispondenza degli ordini di acquisto per mostrare quando un ordine di acquisto è stato aggiornato, invitando gli utenti a ricaricare per le ultime informazioni.
* **Aggiornamento automatico dei dati PO**: Attivando questo, i dati PO verranno aggiornati automaticamente quando sono disponibili nuovi dati.
* **Stato della linea PO consumata**: Attivando questo verrà disabilitata la tonalità colorata sulle righe dell'ordine di acquisto.
* [**Calcolo del prezzo unitario dell'OP**](purchase-order/calculate-po-unit-price.md): Questo ti consente di calcolare il prezzo unitario dell'OP utilizzando l'importo netto e la quantità, invece di estrarlo.
* **Ordine di acquisto**: Attiva o disattiva se il documento deve essere elaborato nello schermo di corrispondenza degli ordini di acquisto. Puoi anche specificare su quale termine di quantità deve basarsi il processo di corrispondenza.
* [**Esportazione di righe PO non corrispondenti**](purchase-order/export-not-matched-po-lines.md): Questa funzionalità controlla l'esportazione delle righe degli ordini di acquisto. Quando disabilitata, vengono esportate solo le righe abbinate. Quando abilitata, tutte le righe degli ordini di acquisto vengono esportate, anche se non sono abbinate a una riga di conferma d'ordine.
* [**Impostazione della tolleranza PO**](purchase-order/purchase-order-tolerance-settings-additional-purchase-order-tolerance.md): Questa funzionalità ti consente di impostare livelli di tolleranza per quantità e prezzo unitario, accogliendo piccole discrepanze senza segnalarle come non corrispondenti.
* [**Impostazione della tolleranza PO aggiuntiva**](purchase-order/purchase-order-tolerance-settings-additional-purchase-order-tolerance.md#impostazione-per-configurare-le-ulteriori-impostazioni-di-tolleranza-per-gli-ordini-di-acquisto): Questa funzionalità ti consente di impostare livelli di tolleranza aggiuntivi per spedizione, spese e tasse, accogliendo piccole discrepanze senza segnalarle come non corrispondenti.
* [**Esportazione alternativa**](purchase-order/alternate-export.md): Questo ti consente di impostare un'esportazione alternativa per stati specifici.
* [**Stati di disabilitazione dell'OP**](purchase-order/purchase-order-disable-statuses.md): Ti consente di disabilitare stati specifici affinché non vengano considerati nel processo di corrispondenza.
* **Ignorare le linee già abbinate**: Attivando questo verranno saltate le righe che sono già state abbinate durante un nuovo processo di corrispondenza.
* [**Numero di articolo del fornitore Mappa**](purchase-order/supplier-item-number-map-admin-documentation.md): Un'impostazione di utilità che mappa i numeri di articolo del fornitore ai numeri di articolo interni, garantendo precisione nella gestione dell'inventario e degli ordini di acquisto.
