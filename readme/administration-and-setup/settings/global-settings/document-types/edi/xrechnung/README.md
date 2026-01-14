# XRechnung

## Panoramica

Nel pannello di amministrazione XRechnung, incontrerai i seguenti componenti chiave:

## 1. Trasformazione

### Scopo

Il processo di Trasformazione è essenziale per convertire i dati grezzi, solitamente in formato XML, in un formato strutturato che soddisfi requisiti specifici, come la generazione di una fattura. In XRechnung, questo viene ottenuto principalmente utilizzando XSLT (Extensible Stylesheet Language Transformations). XSLT è un linguaggio progettato per trasformare documenti XML in altri tipi di documenti, come un altro XML, HTML o testo semplice.

### Come funziona

• Modello XSLT: Il file XSLT definisce come i dati XML vengono elaborati e come dovrebbe apparire l'output finale. Applica regole e modelli per estrarre, manipolare e produrre i dati dal documento XML.

• Elementi e attributi: Il file XSLT contiene elementi e attributi specifici che controllano il processo di trasformazione. Ad esempio, \<xsl:value-of> viene utilizzato per estrarre il valore di un nodo specifico dal documento XML.

### Capacità dell'amministratore

• Modifica dell'XSLT:

• Modifica Modelli Esistenti: Un amministratore può modificare i modelli XSLT esistenti per cambiare il modo in cui i dati XML di input vengono trasformati. Ad esempio, se c'è la necessità di estrarre informazioni aggiuntive dal documento XML, un amministratore potrebbe aggiungere nuove regole nel file XSLT.

• Creazione di Nuove Versioni: Se sono necessarie modifiche, un amministratore può creare una nuova versione del modello XSLT. Ciò garantisce che le versioni precedenti rimangano intatte per riferimento storico o ripristino se necessario.

### Esempio:

Supponiamo che il modello XSLT estragga l'ID della fattura utilizzando:

```xml
<xsl:value-of select="//INVOICE/INVOICE_ID/text()" />
```

Se è necessario estrarre un nuovo campo, come un numero di riferimento cliente, un amministratore potrebbe aggiungere:

```xml
<xsl:value-of select="//INVOICE/CUSTOMER_REFERENCE_NUMBER/text()" />
```

## 2. Anteprima

### Scopo

La funzione Anteprima consente agli amministratori di visualizzare l'output generato dalla trasformazione XSLT prima di finalizzarlo. Questo passaggio è fondamentale per garantire che le regole di trasformazione funzionino correttamente e che l'output soddisfi gli standard richiesti.

### Come funziona

• Validazione in tempo reale: La funzione di anteprima fornisce un rendering in tempo reale di come appariranno i dati trasformati quando applicati a un documento reale (come una fattura). Ciò aiuta a rilevare tempestivamente errori o problemi di formattazione.

• Regolazioni: Se l'anteprima mostra discrepanze o errori, è possibile apportare regolazioni direttamente nel file di trasformazione (XSLT).

### Capacità dell'amministratore

• Personalizzazione dell'anteprima:

• Modifica Impostazioni Anteprima: Un amministratore può regolare quali parti della trasformazione vengono visualizzate in anteprima. Ad esempio, potrebbe concentrarsi su sezioni specifiche del documento o testare nuove regole aggiunte al modello XSLT.

• Salva e Itera: Dopo aver apportato le regolazioni, l'anteprima può essere aggiornata per vedere le modifiche. Questo processo iterativo consente la messa a punto fino al raggiungimento dell'output desiderato.

### Esempio:

Se un amministratore nota che il formato della data nell'anteprima è errato (ad esempio, mostra AAAA-MM-GG invece di GG-MM-AAAA), può modificare l'XSLT per formattare la data correttamente e vedere immediatamente il risultato nell'anteprima.

## 3. Percorsi di estrazione

### Scopo

I Percorsi di Estrazione definiscono i percorsi specifici all'interno di una struttura XML o JSON da cui i dati devono essere estratti. Questo processo è essenziale per isolare i pezzi chiave di informazioni all'interno del documento che verranno utilizzati nella trasformazione o per altre attività di elaborazione.

### Come funziona

• XPath e JSONPath: I percorsi di estrazione utilizzano linguaggi come XPath (per XML) o JSONPath (per JSON) per specificare la posizione dei dati all'interno del documento. Questi percorsi sono fondamentali per dire al sistema esattamente dove trovare e come estrarre le informazioni richieste.

### Capacità dell'amministratore

• Definizione e modifica dei percorsi:

• Modifica Percorsi Esistenti: Un amministratore può modificare i percorsi di estrazione se la struttura dei dati cambia o se è necessario estrarre dati aggiuntivi. Ciò potrebbe comportare la modifica delle espressioni XPath o JSONPath.

• Aggiunta di Nuovi Percorsi: Per nuovi campi o punti dati, un amministratore può definire nuovi percorsi di estrazione. Ciò comporterebbe la specifica del percorso corretto nel documento XML o JSON.

### Esempio:

In un documento di fattura XML, se il percorso dell'ID fattura è definito come:

```json
"invoice_id": "//INVOICE/INVOICE_ID/text()"
```

E deve essere aggiunto un nuovo campo, come un indirizzo di spedizione, un amministratore potrebbe aggiungere:

```json
"shipping_address": "//INVOICE/SHIPPING/ADDRESS/text()"
```
