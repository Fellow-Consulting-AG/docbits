# Document Types

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto%202024-05-08%20um%2008.44.19.png" alt=""><figcaption></figcaption></figure>

#### Panoramica

La sezione Tipi di Documenti elenca tutti i tipi di documenti riconosciuti e elaborati da Docbits. Gli amministratori possono gestire vari aspetti come il layout, le definizioni dei campi, le regole di estrazione e altro ancora per ciascun tipo di documento. Questa personalizzazione è fondamentale per garantire un'accurata gestione dei dati e la conformità agli standard organizzativi.

#### Funzionalità Chiave e Opzioni

1. **Elenco Tipi di Documenti**:

* Ogni riga rappresenta un tipo di documento come Fattura, Nota di Credito, DDT, ecc.
* I tipi di documenti possono essere standard o personalizzati, come indicato dalle etichette come "Standard".

2. **Modifica layout**: Questa opzione consente agli amministratori di modificare le impostazioni del layout del documento, che includono la definizione di come appare il documento e dove sono posizionati i campi dati.
3. **Sottotipi di Documenti**: Se alcuni tipi di documenti hanno sottocategorie, questa opzione consente agli amministratori di configurare impostazioni specifiche per ciascun sottotipo.
4. **Colonne della tabella**: Personalizza quali colonne di dati dovrebbero apparire quando il tipo di documento è visualizzato in elenchi o report.
5. **Campi**: Gestisci i campi dati associati al tipo di documento, inclusa l'aggiunta di nuovi campi o la modifica di quelli esistenti.
6. **Addestramento del Modello**: Configura e addestra il modello utilizzato per riconoscere ed estrarre dati dai documenti. Ciò potrebbe comportare la configurazione dei parametri per i modelli di apprendimento automatico che migliorano nel tempo con più dati.
7. **Regex**: Imposta espressioni regolari utilizzate per estrarre dati dai documenti in base a modelli. Questo è particolarmente utile per l'estrazione di dati strutturati.
8. **Script**: Scrivi o modifica script che eseguono regole di elaborazione personalizzate o flussi di lavoro per documenti di questo tipo.
9. **EDI (Scambio Elettronico di Dati)**: Configura impostazioni relative allo scambio di documenti in formati elettronici standardizzati.

{% hint style="info" %}
Vedi [Configurazione Tipo di Documento](../../../../admin-section/setup/document-types/)
{% endhint %}

{% @jira/embed url="https://fellowpro.atlassian.net/browse/DOCB-2489" %}
