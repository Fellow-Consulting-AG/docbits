# Gestore Layout

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 08.46.24.png" alt=""><figcaption></figcaption></figure>

#### Panoramica

Il Gestore Layout consente agli amministratori di configurare e modificare visivamente il layout dei tipi di documento impostando proprietà per vari campi dati e gruppi all'interno di un documento. Questa interfaccia aiuta a garantire che i modelli di estrazione e i punti di inserimento dati manuali siano allineati precisamente con la struttura del documento acquisito o caricato in Docbits.

#### Componenti Chiave

1. **Gruppi e Campi**:
* **Gruppi**: Unità organizzative all'interno di un tipo di documento che categorizzano campi correlati (ad esempio, Dettagli Fattura, Dettagli Pagamento). Questi possono essere espansi o compressi e disposti per rispecchiare il raggruppamento logico nel documento effettivo.
* **Campi**: Punti dati individuali all'interno di ciascun gruppo (ad esempio, Numero Fattura, Termini di Pagamento). Ogni campo può essere personalizzato per come i dati vengono acquisiti, visualizzati e elaborati.
2. **Pannello Proprietà**:
* Questo pannello mostra le proprietà del campo o gruppo selezionato, consentendo una configurazione dettagliata, come:
* **Etichetta**: L'etichetta visibile per il campo nell'interfaccia utente.
* **Nome Campo**: L'identificatore tecnico utilizzato all'interno del sistema.
* **Larghezza Elemento in Percentuale**: Determina la larghezza del campo rispetto al layout del documento.
* **Indice Tabulazione**: Controlla l'ordine di tabulazione per la navigazione.
* **Esegui Script su Modifica**: Se eseguire uno script quando il valore del campo cambia.
* **Mostra Etichetta a Sinistra**: Se l'etichetta viene visualizzata a sinistra del campo o sopra di esso.
* **È Textarea**: Specifica se il campo dovrebbe essere un'area di testo, adattandosi a quantità maggiori di testo.
* **Seleziona Tipo Modello**: Opzione per selezionare quale tipo di modello gestirà l'estrazione di questo campo.
* **Lunghezza Campo**: Lunghezza massima dei dati accettati in questo campo.
* **Parole Chiave Vietate**: Parole chiave non consentite all'interno del campo.
3. **Anteprima Modello**:
* Mostra un'anteprima in tempo reale di come apparirà il documento in base alla configurazione del layout attuale. Questo aiuta a garantire che il layout corrisponda alla struttura effettiva del documento ed è vitale per il testing e il perfezionamento dell'impostazione di elaborazione del documento.

{% @jira/embed url="https://fellowpro.atlassian.net/browse/DOCB-2490" %}
