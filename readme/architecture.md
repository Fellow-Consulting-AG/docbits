# Architettura

<figure><img src=".gitbook/assets/DocBits_D_Doc2-Infor-1.png" alt=""><figcaption></figcaption></figure>

Doc**Bits** si integra perfettamente con Infor LN/M3 tramite ION API, ION Desk e Infor Standard BODs. La nostra integrazione API ci consente di esportare dati in Infor e di eseguire la convalida dei dati principali in Doc**Bits**.

## Esportazione dei Dati in Infor

Utilizziamo l'API ION per inviare il PDF con attributi a IDM e il BOD Sync.CaptureDocument a ION Desk. In ION Desk, trasformiamo il [Sync.CaptureDocument](admin-section/setup/exporting-in-docbits/) nei BOD desiderati in base al tipo di documento in fase di elaborazione. Questi BOD Infor trasformati vengono quindi importati automaticamente in LN o M3.

{% hint style="info" %}
Esporta in [Infor](admin-section/setup/exporting-in-docbits/exporting-to-infor/)&#x20;
{% endhint %}

## Convalida dei Dati Principali in DocBits

Per identificare il fornitore o confrontare/abbinare le righe dell'ordine di acquisto, attiviamo un trigger in LN/M3 che invia i BOD Sync.RemitToPartyMaster, Sync.SupplierPartyMaster e Sync.PurchaseOrder a Doc**Bits**. Configuriamo questo processo in ION Desk definendo il flusso di dati verso un punto di connessione specifico per Doc**Bits**.

\
