# Gestione delle Fatture Duplicati in DocBits

## Impostazione per Abilitare la Gestione delle Fatture Duplicati

Vai a _Impostazioni → Tipi di Documento → Fattura → Altre Impostazioni_ come mostrato nello screenshot qui sotto

<figure><img src="../../.gitbook/assets/duplicate_invoice handling.png" alt=""><figcaption></figcaption></figure>

L'utente ha due opzioni per rilevare le fatture duplicate:

1. **Rilevamento Documenti Duplicati**\
   Questa funzione controlla la presenza di documenti duplicati caricati su DocBits in base ai criteri selezionati. Se i criteri selezionati corrispondono tra i documenti, il sistema contrassegnerà il documento come duplicato.
2.  **Rilevamento Fatture Duplicati**\
    Questa funzione richiede che le Fatture Fornitori siano sincronizzate da Infor a DocBits. Confronta i numeri delle fatture nel dashboard fatture di DocBits con quelli in Infor. Se lo stesso numero di fattura viene caricato più di una volta, verrà contrassegnato come duplicato.

    <mark style="color:red;">**NOTA**</mark><mark style="color:red;">:</mark> L'uso della funzionalità **Rilevamento Fatture Duplicati** comporterà un addebito di credito aggiuntivo.

Una volta attivata l'impostazione, l'utente può selezionare i criteri per il rilevamento dei duplicati

## Fatture Duplicati nel Dashboard

Una volta abilitato il Rilevamento Duplicati nelle impostazioni, il dashboard mostrerà un'icona per tutte le fatture identificate come duplicati in base ai criteri specificati. Cliccando su questa icona si apriranno i record duplicati in una vista a schermo diviso per un facile confronto

<figure><img src="../../.gitbook/assets/duplicate_invoice handling2.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/duplicate_invoice handling2b.png" alt=""><figcaption></figcaption></figure>

Quando l'utente apre il documento, viene mostrata una barra di avviso per le fatture duplicate come mostrato nello screenshot

<figure><img src="../../.gitbook/assets/duplicate_invoice handling3.png" alt=""><figcaption></figcaption></figure>
