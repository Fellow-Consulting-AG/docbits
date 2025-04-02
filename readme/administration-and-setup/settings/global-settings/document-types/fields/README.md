# Fields

<figure><img src="../../../../../.gitbook/assets/Bildschirmfoto%202024-05-08%20um%2009.02.31.png" alt=""><figcaption></figcaption></figure>

#### Panoramica

L'impostazione dei Campi fornisce un'interfaccia utente in cui gli amministratori possono gestire le proprietà e il comportamento dei singoli campi dati associati a un tipo di documento. Ogni campo può essere regolato per ottimizzare l'accuratezza e l'efficienza della cattura e della validazione dei dati.

#### Funzionalità Chiave e Opzioni

1. **Configurazione dei Campi**:

* **Nomi dei Campi**: Elenca i nomi dei campi, corrispondenti tipicamente agli elementi di dati all'interno del documento, come "Numero Fattura" o "Data Ordine di Acquisto".
* **Obbligatorio**: Gli amministratori possono contrassegnare i campi come obbligatori, garantendo che i dati debbano essere inseriti o catturati per completare l'elaborazione del documento.
* **Sola Lettura**: I campi possono essere impostati come sola lettura per impedire la modifica dopo la cattura dei dati o durante determinate fasi dell'elaborazione del documento.
* **Nascosto**: I campi possono essere nascosti dalla vista nell'interfaccia utente, utile per informazioni sensibili o per semplificare i flussi di lavoro dell'utente.

2. **Impostazioni Avanzate**:

* **Forza la Validazione**: Garantisce che i dati inseriti in un campo superino determinate regole di validazione prima di essere accettati.
* **OCR (Riconoscimento Ottico dei Caratteri)**: Questo interruttore può essere attivato per abilitare l'elaborazione OCR per un campo specifico, utile per l'estrazione automatica dei dati da documenti scansionati o digitali.
* **Punteggio di Corrispondenza**: Gli amministratori possono definire un punteggio di corrispondenza, una soglia utilizzata per determinare il livello di fiducia del riconoscimento o della corrispondenza dei dati, influenzando il modo in cui vengono eseguite la convalida dei dati e i controlli di qualità.

3. **Pulsanti di Azione**:

* **Crea Nuovo Campo**: Consente di aggiungere nuovi campi al tipo di documento.
* **Icone di Modifica**: Ogni campo ha un'icona di modifica che consente agli amministratori di configurare ulteriormente le impostazioni specifiche del campo, come il tipo di dati, i valori predefiniti o la logica aziendale collegata.
* **Salva Impostazioni**: Conferma le modifiche apportate alle configurazioni dei campi.

{% @jira/embed url="https://fellowpro.atlassian.net/browse/DOCB-2494" %}
