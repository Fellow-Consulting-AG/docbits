# Configurazione delle Proprietà del Campo

## Istruzioni dettagliate sull'impostazione di proprietà quali Obbligatorio, Sola lettura, Nascosto e OCR.

### Obbligatorio (Required):

<figure><img src="../../../../../.gitbook/assets/docbits_configure_classification_rule.png" alt="Docbits Configure Classification Rule"><figcaption></figcaption></figure>

Se un campo è contrassegnato come Obbligatorio, significa che questo campo deve essere compilato prima che il documento possa essere salvato o elaborato.

**Per impostare questa proprietà:**

* Navigare nelle impostazioni del campo nel sistema DocBits.
* Abilitare l'opzione Obbligatorio per il campo pertinente.

**Impatto:**

* Questa impostazione garantisce che le informazioni importanti vengano acquisite e che nessun documento possa essere elaborato senza i dati richiesti.

### Sola lettura (Read Only):

<figure><img src="../../../../../.gitbook/assets/docbits_model_prediction_test.png" alt="Docbits Model Prediction Test"><figcaption></figcaption></figure>

Se un campo è contrassegnato come Sola lettura, significa che gli utenti possono visualizzare il contenuto di questo campo, ma non possono apportarvi modifiche.

**Per impostare questa proprietà:**

* Andare alle Opzioni del campo. Abilitare l'opzione Sola lettura per il campo desiderato.

**Impatto:**

* Questa impostazione può essere utile per proteggere informazioni sensibili o per garantire che i dati importanti non vengano modificati accidentalmente.

### Nascosto (Hidden):

<figure><img src="../../../../../.gitbook/assets/docbits_classification_extraction_settings.png" alt="Docbits Classification Extraction Settings"><figcaption></figcaption></figure>

Se un campo è contrassegnato come "Nascosto", significa che il campo verrà nascosto nell'interfaccia utente e gli utenti non potranno vederlo né accedervi.

**Per impostare questa proprietà:**

* Andare alle opzioni del campo.
* Abilitare l'opzione "Nascosto" per il campo corrispondente.

**Impatto:**

* Questa impostazione viene spesso utilizzata per nascondere campi interni o tecnici che sono irrilevanti per l'utente finale o sono necessari solo per l'elaborazione interna.

### OCR (Riconoscimento ottico dei caratteri):

<figure><img src="../../../../../.gitbook/assets/image (114).png" alt=""><figcaption></figcaption></figure>

Se un campo è configurato per l'OCR, significa che il sistema tenterà di estrarre il testo dal documento e inserirlo in questo campo. Questa impostazione viene solitamente utilizzata per i campi che devono essere compilati automaticamente.

**Per configurarlo:**

* Abilitare l'opzione OCR per il campo corrispondente.
* Se necessario, configurare i parametri OCR come lingua, carattere, ecc.

**Impatto:**

* L'utilizzo dell'OCR consente di elaborare i documenti automaticamente estraendo informazioni dai testi e inserendole nei campi appropriati, riducendo lo sforzo manuale e aumentando l'efficienza.

### Convalida forzata (Forced validation):

<figure><img src="../../../../../.gitbook/assets/docbits_sql_alter_table_syntax.png" alt="Docbits Sql Alter Table Syntax"><figcaption></figcaption></figure>

Configurare di conseguenza le regole di convalida, come limiti numerici, espressioni regolari o relazioni con altri campi.

**Per configurarlo:**

* Salvare le modifiche.

**Impatto:**

* La convalida forzata controlla i dati inseriti rispetto ai criteri specificati per garantire che siano validi. Ciò aiuta a rilevare tempestivamente gli errori e a migliorare la qualità dei dati.

### Punteggio di corrispondenza (Match Score):

<figure><img src="../../../../../.gitbook/assets/docbits_add_new_column_steps.png" alt="Docbits Add New Column Steps"><figcaption></figcaption></figure>

Confrontando i dati di input con i dati di riferimento, il Match Score può aiutare a confermare l'accuratezza e la validità dei dati. Se il Match Score supera una certa soglia, la corrispondenza è considerata riuscita.

**Per configurarlo:**

* Abilitare l'opzione Match Score e impostare la soglia desiderata.
* Salvare le modifiche.

**Impatto:**

* Il Match Score viene utilizzato per valutare l'accuratezza delle corrispondenze tra i dati di input e i valori di riferimento. Se il punteggio ottenuto supera la soglia impostata, la corrispondenza è considerata riuscita. Ciò è particolarmente utile per i campi che richiedono la convalida dei dati o la corrispondenza dei dati, come i campi con un nome, un indirizzo e-mail, ecc. ad esempio, durante il controllo dei dati dei clienti.

<figure><img src="../../../../../.gitbook/assets/docbits_column_requirements_analysis.png" alt="Docbits Column Requirements Analysis" width="258"><figcaption></figcaption></figure>

Configurando attentamente queste proprietà del campo, è possibile ottimizzare i flussi di lavoro di elaborazione dei documenti e garantire che i dati vengano acquisiti correttamente, protetti ed elaborati in modo efficiente.
