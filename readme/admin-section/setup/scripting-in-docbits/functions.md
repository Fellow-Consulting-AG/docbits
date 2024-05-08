# Funzioni

**Documentazione Funzionale**

Questo modulo contiene funzioni per manipolare i dati del documento e eseguire varie operazioni relative ai campi del documento.

## **Funzioni**

1. ### **set\_field\_value(document\_data, field\_name, value)**
* Descrizione: Imposta il valore di un campo nei dati del documento.
* Parametri:
* `document_data` (dict): I dati del documento contenenti le informazioni del campo.
* `field_name` (str): Il nome del campo da impostare.
* `value`: Il valore da impostare per il campo.
*   Esempio:

`set_field_value(document_data, "nome", "John Doe")`
2. ### **set\_date\_value(document\_data, field\_name, value)**
* Descrizione: Imposta il valore di un campo data nei dati del documento.
* Parametri:
* `document_data` (dict): I dati del documento contenenti le informazioni del campo.
* `field_name` (str): Il nome del campo data da impostare.
* `value`: Il valore data da impostare nel formato ISO (ad esempio, "2020-12-31").
*   Esempio:

`set_date_value(document_data, "data_di_nascita", "1990-05-15")`
3. ### **set\_amount\_value(document\_data, field\_name, value)**
* Descrizione: Imposta il valore di un campo importo nei dati del documento.
* Parametri e utilizzo dell'esempio simili a `set_field_value`.
4. ### **set\_is\_required(document\_data, field\_name, value)**
* Descrizione: Imposta l'attributo 'is\_required' di un campo nei dati del documento.
* Parametri e utilizzo dell'esempio simili a `set_field_value`.
5. ### **set\_force\_validation(document\_data, field\_name, value)**
* Descrizione: Imposta l'attributo 'force\_validation' di un campo nei dati del documento.
* Parametri e utilizzo dell'esempio simili a `set_field_value`.
6. ### **set\_field\_attribute(document\_data, field\_name, attribute\_name, value)**
* Descrizione: Imposta un attributo personalizzato di un campo nei dati del documento.
* Parametri:
* `attribute_name` (str): Il nome dell'attributo da impostare.
* `value`: Il valore da impostare per l'attributo.
*   Esempio:

`set_field_attribute(document_data, "indirizzo", "è_verificato", True)`
7. ### **get\_field\_value(document\_data, field\_name, default\_value=None, is\_clean=False)**
* Descrizione: Ottiene il valore di un campo dai dati del documento.
* Parametri e utilizzo dell'esempio simili a `set_field_value`.
8. ### **create\_new\_field(field\_name, value="")**
* Descrizione: Crea un nuovo campo con il nome e il valore specificati.
* Parametri:
* `field_name` (str): Il nome del campo da creare.
* `value`: Il valore iniziale per il campo (per impostazione predefinita è una stringa vuota).
*   Esempio:

`create_new_field("indirizzo", "123 Main St")`
9. ### **delete\_field(document\_data, field\_name)**
* Descrizione: Elimina un campo dai dati del documento.
* Parametri e utilizzo dell'esempio simili a `set_field_value`.
10. ### **update\_document\_status\_with\_doc\_id(doc\_id, user, org\_id, status, message=None, doc\_classification\_class=None)**
* Descrizione: Aggiorna lo stato di un documento con l'ID specificato.
* Parametri:
* `doc_id` (str): L'ID del documento da aggiornare.
* `user`: L'utente che esegue l'aggiornamento (ID utente o oggetto UserAuthentication).
* `org_id`: L'ID dell'organizzazione a cui appartiene il documento.
* `status` (str): Il nuovo stato del documento.
* `message`: Messaggio opzionale associato all'aggiornamento dello stato.
* `doc_classification_class`: Classe di classificazione del documento opzionale.
*   Esempio:

`update_document_status_with_doc_id("123456", user, org_id, "approvato", "Documento approvato")`
11. ### **is\_supplier\_valid(user: UserAuthentication, filter\_data\_json, sub\_org\_id=None)**
* Descrizione: Verifica se un fornitore è valido in base ai criteri forniti.
* Parametri:
* `user` (UserAuthentication): L'utente autenticato.
* `filter_data_json`: Criteri di filtro per la convalida del fornitore.
* `sub_org_id`: ID sottorganizzazione opzionale per il filtraggio.
*   Esempio:

`is_supplier_valid(user, {"nome": "Fornitore Spa"})`
12. ### **set\_field\_as\_invalid(document\_data, field\_name, message, code=None)**
* Descrizione: Contrassegna un campo come non valido nei dati del documento.
* Parametri:
* `document_data` (dict): I dati del documento contenenti le informazioni del campo.
* `field_name` (str): Il nome del campo da contrassegnare come non valido.
* `message` (str): Il messaggio di convalida per il campo.
* `code` (opzionale): Codice di errore per la convalida (per impostazione predefinita è None).
*   Esempio:

`set_field_as_invalid(document_data, "email", "Formato email non valido", "EMAIL_FORMAT_INVALID")`
13. ### **compare\_values(value1, value2)**
* Descrizione: Confronta due valori per l'uguaglianza, gestendo vari tipi di dati.
* Parametri:
* `value1`: Il primo valore da confrontare.
* `value2`: Il secondo valore da confrontare.
*   Esempio:

`compare_values(10, "10")`
