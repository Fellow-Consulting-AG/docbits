# Documentazione sul Workflow

**Documentazione sul Workflow**

Per mantenere una panoramica, è possibile dare ai workflow diversi titoli in modo da sapere immediatamente di quale compito si tratta.

Creare un nuovo Workflow: Fare clic su + AGGIUNGI WORKFLOW

![](<../../.gitbook/assets/0 (1).png>)

È possibile utilizzare questi workflow (Test 1,2,3) per assegnare automaticamente vari documenti al dipendente giusto nell'azienda.

![](<../../.gitbook/assets/1 (1).png>)

Se una fattura o un altro documento supera un certo importo totale che richiede una revisione e un'approvazione preventiva, questi documenti possono essere immediatamente assegnati alla persona corretta.

<figure><img src="../../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

**Test 1:              Scheda Logica**

Quando:             **Assegnatario è:**                    Amier Haider

E:                **Tipo di documento è:**        Fattura

Quindi:              **Assegna documento a:**   Stefan Reppermund

![](<../../.gitbook/assets/3 (1).png>)

**Test 2:              Scheda Logica**

Quando:              **Assegnatario è:**                    Amier Haider

E:                 **Tipo di documento è:**        Bollettino di Consegna

Quindi:               **Assegna documento a:**   James Edwards

![](<../../.gitbook/assets/4 (1).png>)

**Test 3:             Scheda Logica**

**Quando:**             **Assegnatario è:**                    Amier Haider

**E:**                **Tipo di documento è:**        Conferma d'Ordine

**Quindi:**              **Assegna documento a:**   Anian Sollinger

![](<../../.gitbook/assets/5 (1).png>)





È anche possibile, se il documento non è assegnato a una singola persona, assegnarlo a un dipendente specifico fin dall'inizio.

<figure><img src="../../.gitbook/assets/image (25).png" alt="" width="375"><figcaption></figcaption></figure>





Per una panoramica più semplice di cosa dovrebbe accadere a un documento, è possibile impostare lo stato per i documenti in arrivo in questo workflow. Questo workflow consente di vedere immediatamente se c'è, ad esempio, un'approvazione in sospeso.



**Test 4:             Scheda Logica**

**Quando:**             **Tipo di documento è:**         Bollettino di Consegna

**E:**                **Assegnatario è:**                     Amier Haider

**Quindi:**              **Cambia Stato in:**         Approvazione in Sospeso

<figure><img src="../../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

![](<../../.gitbook/assets/8 (1).png>)



**Test 5:                Scheda Logica**

Quando:                **Tipo di documento è:**           Fattura

E:                   **Assegnatario è:**                       Stefan Reppermund

Quindi:                 **Cambia Stato in:**           Seconda Approvazione in Sospeso

<figure><img src="../../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

![](<../../.gitbook/assets/10 (1).png>)





Se una fattura o un altro documento supera un certo importo totale che richiede una revisione e un'approvazione preventiva, questi documenti possono essere assegnati immediatamente alla persona giusta.

![](<../../.gitbook/assets/11 (1).png>)



**Test 6:                    Scheda Logica**

Quando:                   **Assegnatario è:**                   Amier Haider

E:                      CampoDoc        **total\_amount**     è      **Maggiore di       500**

Quindi:                    **Assegna documento a:**   Asad Usman Khan

<figure><img src="../../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

![](<../../.gitbook/assets/13 (1).png>)



È anche possibile inserire lo stato nel workflow, in modo che la persona assegnata possa vedere immediatamente in che stato si trova il documento e cosa dovrebbe accadere dopo.



**Test 7:                 Scheda Logica**

**Quando:** **Assegnatario è:**                     Amier Haider

**E:**                   CampoDoc           **total\_amount**      è        **Maggiore di      500**

**Quindi:**                 **Assegna documento a:**     Asad Usman Khan

&#x20;                            **Cambia Stato in:**          Approvazione in Sospeso

<figure><img src="../../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/15 (1).png" alt=""><figcaption></figcaption></figure>





Ad esempio, se mancano informazioni specifiche o importanti da un documento, ma sono importanti e devono essere incluse per ulteriori elaborazioni, è possibile configurare il workflow in modo che questi documenti vengano immediatamente inoltrati al compratore e a un sostituto.

<figure><img src="../../.gitbook/assets/image (10).png" alt=""><figcaption></figcaption></figure>



**Test 9:**

Il Workflow con queste schede logiche è progettato per verificare automaticamente che la quantità, il prezzo unitario o lo sconto dettagliati in una conferma d'ordine corrispondano alle cifre corrispondenti nell'ordine di acquisto. Questa verifica garantisce coerenza e precisione tra ciò che è stato ordinato e ciò che il fornitore conferma di consegnare.

È possibile assegnare a questi documenti uno stato specifico o assegnarli a un dipendente specifico.

<div align="center">

<figure><img src="../../.gitbook/assets/image (12).png" alt=""><figcaption></figcaption></figure>

</div>

<figure><img src="../../.gitbook/assets/image (16).png" alt=""><figcaption></figcaption></figure>

**Scheda Logica: Quantità o Prezzo Unitario o Sconto Corrispondente**

Questa scheda logica è progettata per verificare automaticamente che la quantità, il prezzo unitario o lo sconto dettagliati in una conferma d'ordine corrispondano alle cifre corrispondenti nell'ordine di acquisto. Questa verifica garantisce coerenza e precisione tra ciò che è stato ordinato e ciò che il fornitore conferma di consegnare.



**Condizione di Trigger**

La logica viene attivata quando una qualsiasi delle seguenti condizioni è soddisfatta in una conferma d'ordine rispetto all'ordine di acquisto originale:

* **Quantità**: La quantità di articoli ordinati corrisponde alla quantità confermata dal fornitore.
* **Prezzo Unitario**: Il prezzo per articolo concordato corrisponde alla conferma del fornitore.
* **Sconto**: Eventuali sconti applicati sono coerenti tra l'ordine di acquisto e la conferma d'ordine.



* **Definire Parametri di Confronto**: Configurare i campi specifici (quantità, prezzo unitario, sconto) che la scheda logica verificherà per una corrispondenza.
* **Automatizzare la Verifica**: Configurare il sistema per confrontare automaticamente questi dettagli al ricevimento di una conferma d'ordine.
* **Personalizzare gli Avvisi**: Decidere sul workflow per gestire le discrepanze, inclusa la personalizzazione degli avvisi per la revisione manuale.

Questa scheda logica è fondamentale per garantire che i dettagli di una conferma d'ordine siano in linea con l'ordine di acquisto originale, salvaguardando l'integrità del ciclo di approvvigionamento.



**Test 10:**

Se si dispone di un calcolo diverso per sovrapprezzi, o li si ha solo su alcuni articoli, è possibile utilizzare le schede di calcolo tabellare generiche, alcune delle quali consentono anche di filtrare per espressioni regolari.

<figure><img src="../../.gitbook/assets/19 (1).png" alt=""><figcaption></figcaption></figure>

Di seguito è riportato un esempio di calcolo per MTZ con un filtro per numeri di articolo che iniziano con 01, 06, 9, 001 o 000.



Con una configurazione manuale è consigliabile suddividere i calcoli che dipendono da nuove colonne in un workflow separato. Per continuare con il calcolo è possibile utilizzare la scheda Esegui Workflow.

**Esegui Workflow**

<figure><img src="../../.gitbook/assets/20 (1).png" alt=""><figcaption></figcaption></figure>

Con questa scheda è possibile specificare il nome di un workflow che deve essere eseguito dopo il workflow corrente se le sue condizioni sono soddisfatte e dopo le schede then precedenti del workflow corrente. Pur privilegiando i workflow eseguibili e attivi, consente anche di eseguire workflow disattivati se il documento soddisfa le condizioni del workflow.
### **Aggiunta di sovrapprezzi calcolati in una colonna esistente** <a href="#pekg4i18rshn" id="pekg4i18rshn"></a>

<figure><img src="https://lh7-us.googleusercontent.com/XYY1xsFpp7_-Bi0WOSbotiVzspDLdaufx_xgoopMHmxdZnSDhroLpb0AE_si5PhwMq1jHfndc9FwOte9MOoCoTP5_JUYawO5cr4uIctIDHmwVjz3KacQrLJd8iBQy5KY4N-dMaWEi3IeTcc5OBRNJk4" alt=""><figcaption></figcaption></figure>

Se si desidera aggiungere tutti i sovrapprezzi come uno sconto negativo nella colonna degli sconti, è possibile utilizzare la carta di calcolo. Potrebbero esserci voci in questa colonna, è possibile impostarla come una delle variabili sulla carta, fare sottrarre l'MTZ da essa e aggiungere il risultato di nuovo in questa colonna. Nel caso ci siano campi vuoti (sovrapprezzi solo per alcuni articoli) si assumerà un 0 per il calcolo.

**Avvisare l'utente di autorizzare la conferma dell'ordine in DocBits**

Dopo aver calcolato i sovrapprezzi, potresti voler notificare a un utente specifico di autorizzare la conferma dell'ordine. Per questo puoi utilizzare la carta di notifica

<figure><img src="../../.gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>

A seconda delle impostazioni, all'utente viene assegnato un nuovo compito in DocBits e facoltativamente una email per informarlo del suo nuovo compito.
