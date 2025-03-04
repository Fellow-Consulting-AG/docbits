# Note della versione

## Release Spring Bloom – 23 aprile 2025

### Miglioramenti di DocBits:

* **Opzione di Filtro per il Registro di Importazione Email:** Gli utenti ora hanno la possibilità di filtrare i registri di importazione e ordinare la tabella per una panoramica più chiara ed efficiente. Questo miglioramento semplifica il processo di identificazione e gestione delle voci email, migliorando la risoluzione dei problemi e la gestione complessiva dei registri.
* **Supporto Multilingue per la Lista dei Valori:** Abbiamo ampliato le capacità multilingue alla funzionalità Lista dei Valori. Gli amministratori possono ora definire etichette in più lingue, assicurando che l'etichetta corretta venga visualizzata automaticamente in base alle impostazioni della lingua di sistema dell'utente. Questo miglioramento promuove una maggiore accessibilità e localizzazione, rendendo più facile per gli utenti di tutto il mondo interagire con la piattaforma nella loro lingua madre.
* **Miglioramenti ai Dettagli Utente nelle Impostazioni:** L'interfaccia delle impostazioni ora visualizza informazioni complete sugli utenti. Gli amministratori possono facilmente visualizzare le affiliazioni ai gruppi, i dettagli delle sotto-organizzazioni e ulteriori dati chiave, consentendo una migliore gestione dei ruoli degli utenti e una comprensione più chiara delle strutture del team.
* **Informazioni di Contabilità Automatica nella Schermata di Approvazione:** La schermata di approvazione ora presenta dettagli di contabilità automatica insieme alle informazioni sulle fatture. Questo miglioramento fornisce una visione più profonda dei dati delle transazioni, facilitando processi di revisione più fluidi e decisioni più informate riguardo alle fatture.
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

​

## Release Hot Fix Winter Frost 11 marzo 2025

### Miglioramenti di DocBits:

* **Estrazione Dati Migliorata:** Aggiunta un'opzione per estrarre il **Purchase Order** o il **Item Number** da una riga sopra o sotto.
* **Accesso Espanso alle Sotto-Organizzazioni Incrociate:** Gli utenti non amministratori possono ora accedere anche alla funzionalità **Cross Sub-Organizations**.

### **Correzioni di Bug:**

* Risolto un problema in cui gli utenti **non potevano essere aggiunti** a un gruppo.
* Risolto un problema con **i fallimenti di importazione email**.
