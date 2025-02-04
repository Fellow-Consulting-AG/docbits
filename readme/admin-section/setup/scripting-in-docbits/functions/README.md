# Funzioni

**Documentazione Funzionale**

Questo modulo contiene funzioni per manipolare i dati dei documenti e per eseguire varie operazioni relative ai campi del documento.

#### **Funzioni**

1. **set\_field\_value(document\_data, field\_name, value)**
   * Descrizione: Imposta il valore di un campo nei dati del documento.
   * Parametri:
     * document\_data (dict): I dati del documento contenenti informazioni sui campi.
     * field\_name (str): Il nome del campo da impostare.
     * value: Il valore da impostare per il campo.
   *   [Esempio:](example-scripts.md#set_field_value-document_data-field_name-value)

       ```
       set_field_value(document_data, "name", "John Doe")
       ```
2. **set\_date\_value(document\_data, field\_name, value, add\_days=0, skip\_weekend=False)**
   * Descrizione: Imposta il valore di un campo data nei dati del documento.
   * Parametri:
     * document\_data (dict): I dati del documento contenenti informazioni sui campi.
     * field\_name (str): Il nome del campo data da impostare.
     * value: Il valore della data da impostare in formato ISO (ad es., "2020-12-31").
     * add\_days (int): Aggiungi giorni aggiuntivi alla data fornita.
     * skip\_weekend (bool): Salta la data se cade nel fine settimana.
   *   [Esempio:](example-scripts.md#set_date_value-document_data-field_name-value-add_days-0-skip_weekend-false)

       ```
       set_date_value(document_data, "promised_delivery_date", "2020-12-31", add_days=2, skip_weekend=True)
       ```
3. **set\_amount\_value(document\_data, field\_name, value)**
   * Descrizione: Imposta il valore di un campo importo nei dati del documento.
   * Parametri:
     * document\_data (dict): I dati del documento contenenti informazioni sui campi.
     * field\_name (str): Il nome del campo da impostare.
     * value: Il valore da impostare per il campo.
   *   [Esempio:](example-scripts.md#set_amount_value-document_data-field_name-value)

       ```
       set_amount_value(document_data, "number", "123456")
       ```
4. **get\_field\_value(document\_data, field\_name, default\_value=None, is\_clean=False)**
   * Descrizione: Ottiene il valore di un campo dai dati del documento.
   * Parametri:
     * document\_data (dict): I dati del documento contenenti informazioni sui campi.
     * field\_name (str): Il nome del campo da impostare.
     * default\_value (opzionale): Restituisce default\_value se non viene trovato alcun valore del campo.
     * is\_clean (opzionale): Trasforma il valore in maiuscolo e lo pulisce dagli spazi vuoti.
   * Restituisce:
     * Valore del campo.
   *   [Esempio:](example-scripts.md#get_field_value-document_data-field_name-default_value-none-is_clean-false)

       ```
       value = get_field_value(document_data, "name")
       ```
5. **create\_new\_field(field\_name, value="")**
   * Descrizione: Crea un nuovo campo con il nome e il valore specificati.
   * Parametri:
     * field\_name (str): Il nome del campo da creare.
     * value: Il valore iniziale per il campo (il valore predefinito è una stringa vuota).
   * Restituisce:
     * Dizionario del nuovo campo creato.
   *   [Esempio:](example-scripts.md#create_new_field-field_name-value)

       ```
       dict = create_new_field("address", "")
       ```
6. **delete\_field(document\_data, field\_name)**
   * Descrizione: Elimina un campo dai dati del documento.
   * Parametri:
     * document\_data (dict): I dati del documento contenenti informazioni sui campi.
     * field\_name (str): Il nome del campo da impostare.
   * Restituisce:
     * Document\_data come json e come dict dopo che il campo è stato eliminato.
   *   [Esempio:](example-scripts.md#delete_field-document_data-field_name)

       ```
       json, dict = (document_data, "name")
       ```
7. **set\_is\_required(document\_data, field\_name, value)**
   * Descrizione: Imposta l'attributo 'is\_required' di un campo nei dati del documento.
   * Parametri:
     * document\_data (dict): I dati del documento contenenti informazioni sui campi.
     * field\_name (str): Il nome del campo da impostare.
     * value: Il valore da impostare per il campo.
   *   [Esempio:](example-scripts.md#set_is_required-document_data-field_name-value)

       ```
       set_is_required(document_data, "bank_id", True)
       ```
8. **set\_force\_validation(document\_data, field\_name, value)**
   * Descrizione: Imposta l'attributo 'force\_validation' di un campo nei dati del documento.
   * Parametri:
     * document\_data (dict): I dati del documento contenenti informazioni sui campi.
     * field\_name (str): Il nome del campo da impostare.
     * value (bool): Il valore da impostare per il campo.
   *   [Esempio:](example-scripts.md#set_force_validation-document_data-field_name-value)

       ```
       set_force_validation(document_data, 'supplier_name', True)
       ```
9. **set\_field\_as\_invalid(document\_data, field\_name, message, code=None)**
   * Descrizione: Contrassegna un campo come non valido nei dati del documento.
   * Parametri:
     * document\_data (dict): I dati del documento contenenti informazioni sui campi.
     * field\_name (str): Il nome del campo da contrassegnare come non valido.
     * message (str): Il messaggio di validazione per il campo.
     * code (opzionale): Codice di errore per la validazione (il valore predefinito è None).
   *   [Esempio:](example-scripts.md#set_field_as_invalid-document_data-field_name-message-code-none)

       ```
       set_field_as_invalid(document_data, "email", "Formato email non valido", "EMAIL_FORMAT_INVALID")
       ```
10. **set\_field\_attribute(document\_data, field\_name, attribute\_name, value)**
    * Descrizione: Imposta un attributo personalizzato di un campo nei dati del documento.
    * Parametri:
      * document\_data (str): I dati del documento contenenti informazioni sui campi.
      * field\_name (str): Il nome del campo da impostare.
      * attribute\_name (str): Il nome dell'attributo da impostare.
      * value (bool): Il valore da impostare per l'attributo.
    *   [Esempio:](example-scripts.md#set_field_attribute-document_data-field_name-attribute_name-value)

        ```
        set_field_attribute(document_data, "address", "is_verified", True)
        ```
11. **is\_supplier\_valid(user: UserAuthentication, filter\_data\_json, sub\_org\_id=None)**
    * Descrizione: Controlla se un fornitore è valido in base ai criteri forniti.
    * Parametri:
      * user (UserAuthentication): L'utente autenticato.
      * filter\_data\_json: Criteri di filtro per la validazione del fornitore.
      * sub\_org\_id (opzionale): ID della sotto-organizzazione opzionale per il filtraggio.
    * Restituisce:
      * True, se l'utente è valido.
      * False se l'utente non è valido.
    *   [Esempio:](example-scripts.md#is_supplier_valid-user-userauthentication-filter_data_json-sub_org_id-none)

        ```
        bool = is_supplier_valid(user, {"name": "Supplier Inc."})
        ```
12. **get\_document\_content(document\_data)**
    * Descrizione: Restituisce il contenuto del documento in base ai dati del documento.
    * Parametri:
      * document\_data (str): I dati del documento contenenti informazioni sui campi.
    * Restituisce:
      * Contenuto del documento dei dati del documento.
    *   [Esempio:](example-scripts.md#get_document_content-document_data)

        ```
        document_content = get_document_content(doc)
        ```
13. **update\_document\_status\_with\_doc\_id(doc\_id, user, org\_id, status, message=None, doc\_classification\_class=None)**
    * Descrizione: Aggiorna lo stato di un documento con l'ID specificato.
    * Parametri:
      * doc\_id (str): L'ID del documento da aggiornare.
      * user: L'utente che esegue l'aggiornamento (ID utente o oggetto UserAuthentication).
      * org\_id: L'ID dell'organizzazione a cui appartiene il documento.
      * status (str): Il nuovo stato del documento.
      * message: Messaggio opzionale associato all'aggiornamento dello stato.
      * doc\_classification\_class: Classe di classificazione del documento opzionale.
    *   [Esempio:](example-scripts.md#update_document_status_with_doc_id-doc_id-user-org_id-status-message-none-doc_classification_class-n)

        ```
        update_document_status_with_doc_id("123456", user, "org_id", "approved", "Documento approvato")
        ```
14. **get\_lov\_values(org\_id, key, return\_type="list\_of\_objects", sub\_org\_id=None)**
    * Descrizione: Ottiene i valori LOV da un org\_id specifico.
    * Parametri:
      * org\_id: L'ID dell'organizzazione a cui appartiene il documento.
      * return\_type (opzionale): Il tipo in cui i dati devono essere restituiti.
      * sub\_org\_id (opzionale): ID della sotto-organizzazione opzionale per il filtraggio.
    * Restituisce:
      * Valori LOV come lista di oggetti o come lista.
    *   [Esempio:](example-scripts.md#get_lov_values-org_id-key-return_type-list_of_objects-sub_org_id-none)

        ```
        supplier_to_check = get_lov_values(org_id, 'BlacklistSupplier', return_type="list_of_values")
        ```
15. **format\_decimal\_to\_locale(value, to\_locale="en\_US.UTF-8", max\_decimal\_places=4, min\_decimal\_places=2)**
    * Descrizione: Formatta un valore decimale nel formato en\_US.UTF-8.
    * Parametri:
      * value: Il valore che deve essere formattato.
      * to\_locale (opzionale): Il formato in cui il valore viene trasformato.
      * max\_decimal\_places (opzionale): Il numero massimo di decimali da considerare.
      * min\_decimal\_places (opzionale): Il numero minimo di decimali da considerare.
    * Restituisce:
      * Il valore formattato.
    *   [Esempio:](example-scripts.md#format_decimal_to_locale-value-to_locale-en_us.utf-8-max_decimal_places-4-min_decimal_places-2)

        ```
        formatted_value = format_decimal_to_locale(value, document_json['amount_format_locale'])
        ```
16. **compare\_values(value1, value2)**
    * Descrizione: Confronta due valori per uguaglianza, gestendo vari tipi di dati.
    * Parametri:
      * value1: Il primo valore da confrontare.
      * value2: Il secondo valore da confrontare.
    * Restituisce:
      * True se i valori sono uguali e False se differiscono.
    *   [Esempio:](example-scripts.md#compare_values-value1-value2)

        ```
        result = compare_values(10, "10")
        ```
17. **create\_document\_task( user, document\_data, title, description, priority,**\
    **assigned\_to\_user\_id, assigned\_to\_group\_id, send\_email: bool)**
    * Descrizione: Crea un'attività per il documento.
    * Parametri:
      * user: L'utente che esegue l'aggiornamento (ID utente o oggetto UserAuthentication).
      * document\_data: I dati del documento contenenti informazioni sui campi.
      * title (str): Il titolo dell'attività.
      * description (str): La descrizione dell'attività.
      * priority: La priorità dell'attività.
      * assigned\_to\_user\_id: L'ID dell'utente a cui l'attività deve essere assegnata.
      * assigned\_to\_group\_id: L'ID del gruppo a cui l'attività deve essere assegnata.
      * send\_email (bool): Determina se deve essere inviato un'email o meno.
    * Restituisce:
      * Dict che indica se il processo è stato completato con successo o meno.
    *   [Esempio:](example-scripts.md#create_document_task-user-document_data-title-description-priority-assigned_to_user_id-assigned_to_g)

        ```
        dict = create_document_task(user, document_data, "Paese di origine al di fuori dell'UE", "La conferma proviene da un paese al di fuori dell'UE. Si prega di allegare il documento MRN.", "high", 1007, None, False)
        ```
18. **set\_document\_sub\_org\_id(document\_data, sub\_org\_id)**
    * Descrizione: Imposta il sub\_org\_id dei dati del documento specificato.
    * Parametri:
      * document\_data: I dati del documento contenenti informazioni sui campi.
      * sub\_org\_id (str): ID della sotto-organizzazione opzionale per il filtraggio.
    *   [Esempio:](example-scripts.md#set_document_sub_org_id-document_data-sub_org_id)

        ```
        set_document_sub_org_id(document_data, sub_org_id)
        ```
19. **get\_user\_by\_id(user\_id)**
    * Descrizione: Ottiene l'utente con l'ID utente corrispondente.
    * Parametri:
      * user\_id (str): L'ID dell'utente.
    * Restituisce:
      * L'utente con l'ID utente corrispondente.
    *   [Esempio:](example-scripts.md#get_user_by_id-user_id)

        ```
        user = get_user_by_id("123456")
        ```
20. **get\_group\_by\_id(group\_id)**
    * Descrizione: Ottiene il gruppo con l'ID gruppo corrispondente.
    * Parametri:
      * group\_id (str): L'ID del gruppo.
    * Restituisce:
      * Il gruppo con l'ID gruppo corrispondente.
    *   [Esempio:](example-scripts.md#get_group_by_id-group_id)

        ```
        group = get_group_by_id("123456")
        ```
21. **add\_table\_column(table, col\_name, default\_value=None)**
    * Descrizione: Aggiunge una colonna alla tabella corrispondente.
    * Parametri:
      * table: La tabella a cui deve essere aggiunta la colonna.
      * col\_name: Il nome della colonna.
      * default\_value (opzionale): Il valore iniziale per il campo (il valore predefinito è una stringa vuota).
    *   [Esempio:](example-scripts.md#add_table_column-table-col_name-default_value-none)

        ```
        add_table_column(table, "UNIT_PRICE_PER")
        ```
22. **get\_column\_value(row, column\_name, default\_value=None, is\_clean=False)**
    * Descrizione: Ottiene un valore da una colonna specificata.
    * Parametri:
      * row: La riga in cui si trova il valore.
      * col\_name: Il nome della colonna.
      * default\_value (opzionale): Restituisce default\_value se non viene trovato alcun valore del campo.
      * is\_clean (opzionale): Trasforma il valore in maiuscolo e lo pulisce dagli spazi vuoti.
    *   [Esempio:](example-scripts.md#get_column_value-row-column_name-default_value-none-is_clean-false)

        ```
        original_unit_price = get_column_value(row, "ORIGINAL_UNIT_PRICE")
        ```
23. **set\_column\_value(row, column\_name, value)**
    * Descrizione: Imposta un valore da una colonna specificata.
    * Parametri:
      * row: La riga in cui si trova il valore.
      * col\_name: Il nome della colonna.
      * value: Il valore che sarà impostato nella posizione specificata.
    * Restituisce:
      * True se la modifica è stata effettuata con successo.
    *   [Esempio:](example-scripts.md#set_column_value-row-column_name-value)

        ```
        success = set_column_value(row,"SUPPLIER_ID", supplier_id)
        ```
24. **set\_column\_date\_value(document\_data, row, column\_name, value, add\_days=0)**
    * Descrizione: Imposta un valore da una colonna specificata.
    * Parametri:
      * document\_data: I dati del documento contenenti informazioni sui campi.
      * row: La riga in cui si trova il valore.
      * col\_name: Il nome della colonna.
      * value: Il valore della data da impostare in formato ISO (ad es., "2020-12-31").
      * add\_days (int): Aggiungi giorni aggiuntivi alla data fornita.
    *   [Esempio:](example-scripts.md#set_column_date_value-document_data-row-column_name-value-add_days-0)

        ```
        set_column_date_value(document_data, row, "DELIVERY_DATE", "2020-12-31", add_days=2)
        ```
25. **set\_column\_amount\_value(document\_data, row, column\_name, value)**
    * Descrizione: Esegue le seguenti azioni:
      * Converte il valore in stringa e imposta il valore per la colonna.
      * Imposta il contenuto della colonna sul valore.
      * Formattta il valore secondo la locale.
    * Parametri:
      * document\_data (dict): I dati del documento contenenti informazioni sui campi.
      * row: Riga della linea della tabella.
      * column\_name: Nome della colonna.
      * value: Valore da impostare.
    *   [Esempio:](example-scripts.md#set_column_amount_value-document_data-row-column_name-value)

        ```
        set_column_amount_value(document_data, row, "UNIT_PRICE", str(unit_price))
        ```
26. **remove\_rows\_from\_table(document\_data, table\_name, count, start)**
    * Descrizione: Rimuove righe dalla tabella specificata.
    * Parametri:
      * document\_data (dict): I dati del documento contenenti informazioni sui campi.
      * table\_name: Il nome della tabella.
      * count: Quante righe devono essere eliminate.
      * start: Il punto di partenza.
    *   [Esempio:](example-scripts.md#remove_rows_from_table-document_data-table_name-count-start)

        ```
        remove_rows_from_table(document_data,"INVOICE_TABLE",count,start)   
        ```
27. **remove\_all\_rows\_except\_one\_from\_table(document\_data, line\_number)**
    * Descrizione: Rimuove tutte le righe tranne una dalla tabella specificata.
    * Parametri:
      * document\_data (dict): I dati del documento contenenti informazioni sui campi.
      * line\_number: Il numero della riga che non deve essere rimossa.
    *   [Esempio:](example-scripts.md#remove_all_rows_except_one_from_table-document_data-line_number)

        ```
        remove_all_rows_except_one_from_table(document_data, line_number) 
        ```

#### Funzioni Incorporate di Python

Puoi anche utilizzare alcune delle funzioni incorporate di Python:

* abs(): Restituisce il valore assoluto di un numero.
* len(): Restituisce la lunghezza (numero di elementi) di un oggetto, come una lista o una stringa.
* isinstance(): Controlla se un oggetto è un'istanza di una particolare classe o tipo.
* print(): Stampa l'output sulla console.
* round(): Arrotonda un numero in virgola mobile a un numero specificato di decimali.
* str\_to\_bool(): Converte una stringa in un valore booleano (True o False).
* type(): Restituisce il tipo di un oggetto.
* dict(): Crea un oggetto dizionario.
* list(): Crea un oggetto lista.
* str(): Converte un valore in una stringa.
* float(): Converte un valore in un numero in virgola mobile.
* int(): Converte un valore in un intero.

Per ulteriori dettagli, visita la documentazione ufficiale di Python: [Funzioni Incorporate](https://docs.python.org/3.12/library/functions.html).

#### Funzioni della Classe String

Puoi anche utilizzare queste funzioni specificamente per lavorare con le stringhe:

* lower(): Converte tutti i caratteri in una stringa in minuscolo.
* upper(): Converte tutti i caratteri in una stringa in maiuscolo.
* split(): Divide una stringa in una lista in base a un delimitatore (ad es., spazio o virgola).
* startswith(): Controlla se una stringa inizia con un prefisso specificato.
* endswith(): Controlla se una stringa termina con un suffisso specificato.
* strip(): Rimuove eventuali spazi bianchi iniziali o finali da una stringa.

#### Funzioni dal Modulo Math di Python

Queste funzioni fanno parte del modulo math e sono utili per operazioni matematiche:

* floor(): Restituisce il più grande intero minore o uguale a un dato numero.
* ceil(): Restituisce il più piccolo intero maggiore o uguale a un dato numero.

Per ulteriori informazioni, consulta la documentazione ufficiale di Python: [Funzioni del Modulo Math](https://docs.python.org/3/library/math.html).

#### Funzione di Espressione Regolare

* re.search(): Cerca un modello all'interno di una stringa e restituisce la prima corrispondenza.

Vedi ulteriori dettagli qui: [Documentazione re.search](https://docs.python.org/3/library/re.html#re.search).

#### Funzioni Esterne

Ecco alcune funzioni utili da librerie esterne:

* deepcopy(): Crea una copia di un oggetto, inclusi oggetti annidati (dal modulo copy).\
  [Documentazione Deepcopy](https://docs.python.org/3/library/copy.html#copy.deepcopy).
* levenshtein\_distance(): Calcola il numero di modifiche (inserimenti, eliminazioni, sostituzioni) necessarie per cambiare una stringa in un'altra. Questa funzione è disponibile nella [libreria Jellyfish](https://jamesturk.github.io/jellyfish/functions/).

#### Funzioni di Data e Ora

Puoi utilizzare le seguenti funzioni per lavorare con date e ore:

* strptime(): Converte una stringa in un oggetto datetime in base a un formato specificato.
* strftime(): Formattta un oggetto datetime in una stringa in base a un formato specificato.

Per ulteriori informazioni, consulta la documentazione ufficiale:\
[Funzioni di Data e Ora](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior).
