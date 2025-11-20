# Note della versione

## Release Autumn Summit 15 Ottobre 2025

### Miglioramenti di DocBits:

*   #### Miglioramenti al Design del Modello Email:

    L'editor del modello email è stato ridisegnato per fornire una struttura più chiara e un'esperienza più fluida. La selezione dei campi del documento è ora più intuitiva e gli allegati possono essere inclusi direttamente nei modelli. Questi miglioramenti rendono più veloce e semplice creare email professionali e personalizzate.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fdv4oDlfkRyD0W9yWGAA4%252Fimage.png%3Falt%3Dmedia%26token%3D14bf7ebd-d886-4758-8184-d7b94447518a\&width=768\&dpr=4\&quality=100\&sign=88405d9c\&sv=2)
*   #### Miglioramenti al Dashboard:

    Il dashboard è stato ampliato per migliorare la navigazione e la personalizzazione. Con nuove schede, gli utenti possono passare più rapidamente tra diversi tipi di documenti, riducendo il tempo trascorso nella ricerca della visualizzazione corretta.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FmpO7WSIrkL0I8Rje3HQt%252Fimage.png%3Falt%3Dmedia%26token%3D77d03fe7-e626-4645-b191-e332715a25fb\&width=768\&dpr=4\&quality=100\&sign=93fa9925\&sv=2)
*   #### Dashboard di Filtri Personalizzati:

    Inoltre, i dashboard possono ora essere personalizzati e filtrati in base alle preferenze individuali. Questi dashboard personalizzati possono anche essere condivisi con i colleghi, facilitando la creazione di visualizzazioni di report coerenti per l'intero team.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fn5rPvGnRltT3mTIDoJwV%252Fimage.png%3Falt%3Dmedia%26token%3D22d065e3-81eb-4f16-828c-7f9134c25b1b\&width=768\&dpr=4\&quality=100\&sign=eb11d3a3\&sv=2)
*   #### Registri di Notifiche Email:

    È disponibile una nuova funzionalità di registrazione per tutte le notifiche email. Gli utenti possono ora consultare un elenco delle notifiche inviate, facilitando la verifica delle consegne e la risoluzione dei problemi in caso di mancata ricezione delle email.
*   #### Supporto Fattura Elettronica: e-SLOG 1.6 & 2.0:

    È stato introdotto il supporto per formati di fattura elettronica aggiuntivi. Il sistema può ora elaborare e generare le versioni e-SLOG 1.6 e 2.0, ampliando la compatibilità con partner e requisiti normativi.
*   #### Miglioramenti alla Rilevazione dei Duplicati:

    Il rilevamento dei duplicati è stato potenziato con due potenti opzioni di configurazione. L'**Intervallo di Rilevamento dei Duplicati** consente di definire un intervallo di tempo per controllare i duplicati in modo più preciso, mentre l'impostazione **Vietare l'Esportazione dei Duplicati** impedisce automaticamente l'esportazione dei documenti rilevati come duplicati. Insieme, questi miglioramenti forniscono maggiore controllo e garantiscono una maggiore precisione dei dati.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FXHRKTmuSxTlDt9lDEkE7%252Fimage.png%3Falt%3Dmedia%26token%3D96b56af6-c644-4b0f-a488-8bc16a03c11f\&width=768\&dpr=4\&quality=100\&sign=9b723b7f\&sv=2)
*   #### Miglioramenti all'Albero delle Decisioni:

    Gli alberi decisionali sono ora più versatili, con la capacità di restituire i valori dei campi del documento. Ciò consente una logica di automazione più avanzata, consentendo ai flussi di lavoro di prendere decisioni basate sui dati effettivi del documento.
*   #### Nuove Carte di Flusso di Lavoro:

    Due nuove carte di flusso di lavoro ampliano le capacità di automazione. La prima consente di verificare se un documento appartiene a una specifica sotto-organizzazione, facilitando la gestione delle configurazioni multi-entità. La seconda introduce un controllo della tolleranza della data di consegna, che confronta le date di consegna con la data attuale in giorni lavorativi per aiutare a gestire ed applicare i requisiti di consegna in modo più efficace.
*   #### Miglioramenti all'Esportazione CSV:

    La funzionalità di esportazione CSV è stata significativamente migliorata. Invece di esportare solo i documenti visualizzati nella pagina corrente, il sistema esporta ora tutti i documenti in un set di dati. Ogni esportazione crea un registro e il CSV risultante viene inviato automaticamente via email, garantendo un processo di esportazione più completo e affidabile.
*   #### Intervallo di Eliminazione dell'Ordine di Acquisto:

    Una nuova opzione di configurazione consente agli amministratori di definire un intervallo di tempo per l'eliminazione dell'ordine di acquisto. Questo miglioramento aggiunge flessibilità e controllo sulle politiche di conservazione dei dati, garantendo che gli ordini di acquisto vengano rimossi solo quando appropriato.

### Correzioni di Bug

* Risolto un problema in cui i dati precedenti venivano inclusi durante l'esportazione dei documenti.
* Corretto il filtro per gli Errori di Esportazione, che in precedenza mostrava anche altri stati.
* Risolto un mismatch di validazione della tabella in cui "Prezzo Unitario" causava errori ma "Prezzo Unitario Per" no, nonostante i valori fossero corretti.
* Risolto un problema in cui l'aggiunta di una nuova colonna al dashboard falliva.
* Corretto un problema in cui i compiti non erano visibili nella colonna dei compiti del dashboard.
* Risolto il comportamento di ordinamento casuale in modo che le liste seguano ora un ordine coerente.
* Risolto un problema in cui non era possibile interrompere la modifica delle dimensioni delle colonne.
* Risolto un bug che impediva il matching manuale delle linee nella schermata di corrispondenza degli ordini di acquisto.
* Corretto un problema in cui l'opzione di allegato email veniva reimpostata dopo il salvataggio.
* Risolto un problema in cui l'auto contabilizzazione mostrava inizialmente gli ID del database all'apertura per la prima volta.
* Corretto il comportamento del campo fuzzy in modo che i valori non vengano più sovrascritti in modo errato.
* Risolto un problema in cui i campi nell'auto conto scomparivano dopo aver eliminato il contenuto.
* Corretto un bug in cui l'utente non poteva rinominare "Nome" e "Cognome" nella finestra di impostazioni.
* Risolto un problema in cui i documenti potevano rimanere bloccati in "flusso di lavoro in corso".
* Risolto un problema di colore dell'icona del menu in cui i colori dell'organizzazione selezionata non venivano applicati correttamente.
* Corretto un problema in cui i codici QR talvolta non venivano riconosciuti.
* Risolto un problema in cui gli account non potevano essere rimossi con il tasto backspace per inserirne uno diverso.
* Risolto un mix di lingue dopo il login seguente alla push in produzione.



## Release Spring Bloom – 23 aprile 2025

### Miglioramenti di DocBits:

* **Opzione di Filtro per il Registro di Importazione Email:** Gli utenti ora hanno la possibilità di filtrare i registri di importazione e ordinare la tabella per una panoramica più chiara ed efficiente. Questo miglioramento semplifica il processo di identificazione e gestione delle voci email, migliorando la risoluzione dei problemi e la gestione complessiva dei registri.
* **Supporto Multilingue per la Lista dei Valori:** Abbiamo ampliato le capacità multilingue alla funzionalità Lista dei Valori. Gli amministratori possono ora definire etichette in più lingue, assicurando che l'etichetta corretta venga visualizzata automaticamente in base alle impostazioni della lingua di sistema dell'utente. Questo miglioramento promuove una maggiore accessibilità e localizzazione, rendendo più facile per gli utenti di tutto il mondo interagire con la piattaforma nella loro lingua madre.
* **Miglioramenti ai Dettagli Utente nelle Impostazioni:** L'interfaccia delle impostazioni ora visualizza informazioni complete sugli utenti. Gli amministratori possono facilmente visualizzare le affiliazioni ai gruppi, i dettagli delle sotto-organizzazioni e ulteriori dati chiave, consentendo una migliore gestione dei ruoli degli utenti e una comprensione più chiara delle strutture del team.
* **Informazioni di Contabilità Automatica nella Schermata di Approvazione:** La schermata di approvazione ora presenta dettagli di contabilità automatica insieme alle informazioni sulle fatture. Questo miglioramento fornisce una visione più profonda dei dati delle transazioni, facilitando processi di revisione più fluidi e decisioni più informate riguardo alle fatture.
* **Contatore delle Attività per Documenti nella Vista Dashboard:** I documenti nella dashboard possono ora indicare le attività aperte ad essi associate e visualizzare il numero totale di attività in sospeso. Questa funzionalità fornisce agli utenti una panoramica rapida delle azioni in sospeso, migliorando la gestione delle attività e l'efficienza del flusso di lavoro.
* **Selezione del Modello AI Basato sul Fornitore:** Gli utenti possono ora selezionare il modello AI utilizzato per l'estrazione dei dati su base per-fornitore. Questo miglioramento consente un'ottimizzazione più precisa, garantendo una migliore accuratezza di estrazione per diversi fornitori e migliorando i risultati complessivi del processo di elaborazione dei dati.
* **Log di Flusso di Lavoro Migliorati per le Schede degli Alberi Decisionali:** I log ora visualizzano l'output dell'albero decisionale, rendendo più facile tracciare e comprendere come sono state prese le decisioni all'interno dei flussi di lavoro.
*   **Introduzione di un Nuovo Setup di Auto-Test per Migliorare la Funzionalità e la Stabilità del Sistema:**

    Siamo entusiasti di annunciare l'implementazione di un nuovo sistema di test automatizzati progettato per migliorare la funzionalità e l'affidabilità complessive della nostra piattaforma. Questo nuovo setup eseguirà controlli costanti e approfonditi sul nostro sistema per identificare eventuali problemi prima che impattino sulla tua esperienza. Automatizzando questi test, possiamo garantire risposte più rapide a potenziali problemi e mantenere i più alti standard di qualità per il nostro sistema.

    ​

### Correzioni di Bug

* Risolto un problema in cui i compiti non apparivano nella schermata di validazione/approvazione.
* Sistemata la posizione del pulsante Avanti/Indietro in modo che rimanga statico.
* Risolti problemi di scorrimento nelle visualizzazioni dello script e dell'albero decisionale, assicurando che i pulsanti di azione rimangano fissi durante lo scorrimento.
* Rimossa la campo del paese di origine dalle fatture elettroniche.
* Risolto un problema con il contatore dei compiti che visualizzava un numero inaccurato di compiti.
* Aggiunte traduzioni mancanti.
* Corretto i campi personalizzati per visualizzare nomi descrittivi invece di ID.
* Aggiornata la lista delle scorciatoie per la schermata di corrispondenza PO.
* Risolto un problema in cui i documenti venivano scaricati con un nome file errato.
* Sistemate le incoerenze di ordinamento nella tabella delle righe delle fatture all'interno della corrispondenza PO.
* Risolto un problema che influenzava la funzionalità di creazione dei compiti.
* Risolto un problema nella corrispondenza PO in cui l'ordinamento della tabella delle fatture si resetterebbe quando si abbina una riga.
* Risolti problemi di contabilità automatica assicurando che i riferimenti di prenotazione si dividano correttamente quando un importo è diviso.
* Aggiornate le informazioni sull'host ClickHouse.
* Risolto un problema in cui documenti duplicati non venivano riconosciuti come duplicati.
* Sistemati problemi di esportazione causati da riferimenti di prenotazione troppo lunghi.
* Risolto un problema in cui le caselle di controllo di sola lettura non erano di sola lettura.
* Risolto un problema in cui gli utenti potevano essere aggiunti a una sotto-organizzazione due volte.
* Risolto un problema in cui cambiare la sotto-organizzazione per un documento causava il ripristino dell'utente o del gruppo assegnato.

​

## Release Hot Fix Winter Frost 10 Aprile 2025

### Miglioramenti di DocBits:

* **Funzione Script `set_column_date_value` Migliorata:** La funzione `set_column_date_value` ora include il supporto per l'opzione `skip_weekend`, consentendo ai valori di data di saltare automaticamente i fine settimana quando applicati.
* **Supporto per il Caricamento di File Migliorato:** I file PNG e JPEG possono ora essere caricati direttamente e vengono automaticamente convertiti in formato PDF per una gestione dei documenti semplificata.
* **Aggiornamenti della Funzionalità Watchdog:**
  * Ora supporta l'esportazione in **Enaio** per una migliore integrazione del sistema.
  * Capacità di parsing migliorate per estrarre informazioni dalle strutture XML di `Sync.ContentDocument`, consentendo un'elaborazione dei dati più efficiente.

### Correzioni di Bug

* Risolto un problema su una funzione script.
* Risolto un problema in cui gli ordini di acquisto avevano uno stato errato dopo essere stati aggiornati.

## Release Hot Fix Winter Frost 11 marzo 2025

### Miglioramenti di DocBits:

* **Estrazione Dati Migliorata:** Aggiunta un'opzione per estrarre il **Purchase Order** o il **Item Number** da una riga sopra o sotto.
* **Accesso Espanso alle Sotto-Organizzazioni Incrociate:** Gli utenti non amministratori possono ora accedere anche alla funzionalità **Cross Sub-Organizations**.

### **Correzioni di Bug:**

* Risolto un problema in cui gli utenti non potevano essere aggiunti a un gruppo.
* Risolto un problema con i fallimenti di importazione email.
* Risolto un problema con la formazione sul campo su documenti con più di una pagina
* Risolto un problema in cui gli script non funzionavano correttamente.
* Risolto un problema in cui i dati del documento non venivano visualizzati correttamente
* Risolto un problema con l'impostazione dell'aggiornamento automatico dell'ordine di acquisto
* Risolto un problema in cui i token di abbonamento venivano visualizzati in modo errato
* Risolto un problema in cui la schermata delle attività visualizzava una versione obsoleta del documento
* Risolto un problema che causava il mancato cambiamento dello stato dei documenti
* Risolto un problema in cui i token di abbonamento venivano visualizzati in modo errato
* Risolto un problema in cui la schermata delle attività visualizzava una versione obsoleta del documento
* Risolto un problema che causava il mancato cambiamento dello stato dei documenti
