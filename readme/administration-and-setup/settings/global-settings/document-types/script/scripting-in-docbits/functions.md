# Funzioni

## **Documentazione Funzionale**

Questo modulo contiene funzioni per manipolare i dati dei documenti e per eseguire varie operazioni relative ai campi del documento.

## **Funzioni**

### **set\_field\_value()**

Imposta il valore di un campo nei dati del documento.

```python
po_number = get_field_value(fields_dict, 'purchase_order', None)
if not po_number:
    po_number = ''
    
if po_number:
    set_field_value(fields_dict, "invoice_sub_type", 'Purchase Invoice')
else:
    set_field_value(fields_dict, "invoice_sub_type", 'Cost Invoice')
```

#### Parametri:

<table><thead><tr><th width="177">Nome</th><th width="176">Tipo</th><th>Descrizione</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>I dati del documento contenenti informazioni sui campi</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Il nome del campo da impostare</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>any</code></td><td>Il valore da impostare per il campo</td></tr><tr><td>remove_link (opzionale)</td><td><code>bool</code></td><td>Rimuove la chiave "coords" dal campo.</td></tr></tbody></table>

### **set\_date\_value()**

Imposta il valore di un campo data nei dati del documento.

```python
invoice_date = get_field_value(document_data, 'invoice_date', None)
    
if not document_json.get("script_executed", False):
    if invoice_date:
        set_date_value(document_data, "accounting_date", invoice_date)
        document_json["script_executed"] = True
```

#### Parametri:

<table><thead><tr><th width="229">Nome</th><th width="196.0316162109375">Tipo</th><th>Descrizione</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>I dati del documento contenenti informazioni sui campi</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Il nome del campo da impostare</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Il valore della data da impostare in formato ISO (ad es., "2020-12-31").</td></tr><tr><td>add_days (opzionale)</td><td><code>int</code></td><td>Aggiunge giorni aggiuntivi alla data fornita<br>Il valore predefinito è 0</td></tr><tr><td>skip_weekend (opzionale)</td><td><code>bool</code></td><td>Salta la data se cade nel fine settimana<br>Il valore predefinito è <code>False</code></td></tr><tr><td>remove link (opzionale)</td><td><code>bool</code></td><td>Rimuove la chiave "coords" dal campo.</td></tr><tr><td>exclude_final_days<br>(opzionale)</td><td>either <code>string</code> or <code>int</code></td><td>Specifica i giorni da escludere (0-6 o Domenica a Sabato)</td></tr></tbody></table>

### **set\_amount\_value()**

Imposta il valore di un campo importo nei dati del documento.

```python
total_amount = get_field_value(document_data, "net_amount")
lines_total = 0.0
set_amount_value(document_data, "net_amount",str(lines_total))
```

#### Parametri:

<table><thead><tr><th width="183.71087646484375">Nome</th><th width="176">Tipo</th><th>Descrizione</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>I dati del documento contenenti informazioni sui campi</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Il nome del campo da impostare</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Il valore da impostare per il campo (passa un numero come stringa ad es., "123456")</td></tr><tr><td>remove link (opzionale)</td><td><code>bool</code></td><td>Rimuove la chiave "coords" dal campo.</td></tr></tbody></table>

### **get\_field\_value()**

Ottiene il valore di un campo dai dati del documento.

```python
total_amount = get_field_value(document_data, "net_amount")
lines_total = 0.0
set_amount_value(document_data, "net_amount", str(lines_total))
```

#### Parametri:

<table><thead><tr><th width="191">Nome</th><th width="176">Tipo</th><th>Descrizione</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>I dati del documento contenenti informazioni sui campi</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Il nome del campo da impostare</td></tr><tr><td>default_value (opzionale)</td><td><code>any</code></td><td>Restituisce default_value se non viene trovato alcun valore del campo<br>Il valore predefinito è <code>None</code></td></tr><tr><td>is_clean (opzionale)</td><td><code>bool</code></td><td>Converte il valore in maiuscolo e rimuove eventuali spazi extra<br>Il valore predefinito è <code>False</code></td></tr></tbody></table>

#### Restituisce:

* Valore del campo specificato

### **create\_new\_field()**

Crea un nuovo campo con il nome e il valore specificati.

```python
currency = get_field_value(document_data, 'currency', None)

if not currency:
    if 'currency' not in fields_dict:
        new_field = create_new_field('currency','')
        fields_dict['currency'] = new_field
        document_json['fields'].append(new_field)
    set_field_value(document_data, "currency", "USD")
```

#### Parametri:

<table><thead><tr><th width="140">Nome</th><th width="133">Tipo</th><th>Descrizione</th></tr></thead><tbody><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>str</code></td><td>I dati del documento contenenti informazioni sui campi</td></tr><tr><td>value (opzionale)</td><td><code>any</code></td><td>Il valore iniziale per il campo<br>Il valore predefinito è <code>""</code></td></tr></tbody></table>

#### Restituisce:

* Dizionario del nuovo campo creato

### **delete\_field()**

Elimina un campo dai dati del documento

```python
field_amount = get_field_value(document_data, field_name)
    if not field_amount:
        delete_field(document_data, fields_dict, field_name)
    else:
        field_amount = float(field_amount)
        if field_amount == 0:
            delete_field(document_data, fields_dict, field_name)
```

#### Parametri:

<table><thead><tr><th width="173">Nome</th><th width="176">Tipo</th><th>Descrizione</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>I dati del documento contenenti informazioni sui campi</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Il nome del campo da eliminare</td></tr></tbody></table>

#### Restituisce:

* Document\_data come json e come dict dopo che il campo è stato eliminato

### **set\_is\_required()**

Imposta l'attributo 'is\_required' di un campo nei dati del documento.

```python
net_amount = get_field_value(document_data, "net_amount", None)
if net_amount:
    set_is_required(document_data, "tax_country", True)
    set_is_required(document_data, "tax_code_without_country", True)
```

#### Parametri:

<table><thead><tr><th width="173">Nome</th><th width="176">Tipo</th><th>Descrizione</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>I dati del documento contenenti informazioni sui campi</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Il nome del campo da impostare</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>bool</code></td><td>Il valore da impostare per il campo</td></tr></tbody></table>

### **set\_force\_validation()**

Imposta l'attributo 'force\_validation' di un campo nei dati del documento.

```python
if supplier_id in supplier_to_check:
    set_force_validation(document_data, 'purchase_order', True, reset_validation=reset_validation)
```

#### Parametri:

<table><thead><tr><th width="173">Nome</th><th width="176">Tipo</th><th>Descrizione</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>I dati del documento contenenti informazioni sui campi</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Il nome del campo da impostare</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>bool</code></td><td>Il valore da impostare per il campo</td></tr><tr><td>reset_validation (opzionale)</td><td><code>bool</code></td><td>Imposta l'attributo "is_validated" al valore specificato<br>Il valore predefinito è <code>False</code></td></tr></tbody></table>

### **set\_field\_as\_invalid()**

Contrassegna un campo nella schermata di validazione come non valido e lo evidenzia.

```python
if not document_date:
    set_field_as_invalid(document_data, "document_date", "Es ist kein Datum vorhanden", "INVALID_VALUE")
```

#### Parametri:

<table><thead><tr><th width="173">Nome</th><th width="176">Tipo</th><th>Descrizione</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>I dati del documento contenenti informazioni sui campi</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Il nome del campo da contrassegnare come non valido</td></tr><tr><td>message<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Il messaggio di validazione per il campo</td></tr><tr><td>code (opzionale)</td><td><code>string</code></td><td><p>Codice di errore per la validazione</p><p>Il valore predefinito è <code>None</code></p></td></tr></tbody></table>

### **set\_field\_attribute()**

Imposta un attributo personalizzato di un campo nei dati del documento.

```python
if purchase_order:
    if po_supplier_id != invoice_supplier_id:
        set_field_as_invalid(document_data, "supplier_name", "Supplier is different from PO supplier")
    else:
        set_field_attribute(document_data, "supplier_name", "is_valid", True)
        set_field_attribute(document_data, "supplier_name", "validation_message","")
```

#### Parametri:

<table><thead><tr><th width="173">Nome</th><th width="176">Tipo</th><th>Descrizione</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>I dati del documento contenenti informazioni sui campi</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Il nome del campo da impostare</td></tr><tr><td>attribute_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Il nome dell'attributo da impostare. L'elenco degli attributi supportati è disponibile <a href="functions.md#attributi-supportati">qui</a>.</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>any</code></td><td>Il valore da impostare per l'attributo</td></tr></tbody></table>

### **is\_supplier\_valid()**

Controlla se un fornitore è valido in base ai criteri forniti.

```python
bool = is_supplier_valid(user, {"name": "Supplier Inc."})
```

#### Parametri:

<table><thead><tr><th width="203">Nome</th><th width="216">Tipo</th><th>Descrizione</th></tr></thead><tbody><tr><td>user<mark style="color:red;">*</mark></td><td><code>UserAuthentication</code></td><td>L'utente autenticato</td></tr><tr><td>filter_data_json<mark style="color:red;">*</mark></td><td><code>json</code></td><td>Criteri di filtro per la validazione del fornitore</td></tr><tr><td>sub_org_id (opzionale)</td><td><code>string</code></td><td>ID della sotto-organizzazione opzionale per il filtro<br>Il valore predefinito è <code>None</code></td></tr></tbody></table>

#### Restituisce:

* True, se l'utente è valido
* False se l'utente non è valido

### **get\_document\_content()**

Decodifica i dati del documento e li restituisce come stringa.

```python
document_content = get_document_content(doc)
if document_content:
    document_content = document_content.lower()
```

#### Parametri:

<table><thead><tr><th width="173">Nome</th><th width="176">Tipo</th><th>Descrizione</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>I dati del documento contenenti informazioni sui campi</td></tr></tbody></table>

#### Restituisce:

* I dati del documento come stringa.

### **update\_document\_status\_with\_doc\_id()**

Aggiorna lo stato di un documento con un ID specifico allo stato dato.

```python
genehmigung_user_1 = get_field_value(document_data, 'genehmigung_user_1', None)

if genehmigung_user_1 != "LEER":
    update_document_status_with_doc_id(document_json['doc_id'], user, document_json['org_id'], "validated_pending_approval")
```

#### Parametri:

<table><thead><tr><th width="228">Nome</th><th width="216">Tipo</th><th>Descrizione</th></tr></thead><tbody><tr><td>doc_id<mark style="color:red;">*</mark></td><td><code>string</code></td><td>L'ID del documento da aggiornare</td></tr><tr><td>user<mark style="color:red;">*</mark></td><td>either <code>user ID</code> or <code>UserAuthentication</code> object</td><td>L'utente che esegue l'aggiornamento</td></tr><tr><td>org_id<mark style="color:red;">*</mark></td><td><code>string</code></td><td>L'ID dell'organizzazione a cui appartiene il documento</td></tr><tr><td>status<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Il nuovo stato del documento</td></tr><tr><td>message (opzionale)</td><td><code>string</code></td><td>Messaggio opzionale associato all'aggiornamento dello stato<br>Il valore predefinito è <code>None</code></td></tr><tr><td>doc_classification_class (opzionale)</td><td><code>string</code></td><td>Classe di classificazione del documento opzionale<br>Il valore predefinito è <code>None</code></td></tr></tbody></table>

### **get\_lov\_values()**

Ottiene i valori LOV da un org\_id e una chiave specifici.

```python
reverse_charge_to_check = get_lov_values(org_id, 'Kosten', return_type="list_of_values")
```

#### Parametri:

<table><thead><tr><th width="173">Nome</th><th width="176">Tipo</th><th>Descrizione</th></tr></thead><tbody><tr><td>org_id<mark style="color:red;">*</mark></td><td><code>string</code></td><td>L'ID dell'organizzazione a cui appartiene il documento</td></tr><tr><td>key<mark style="color:red;">*</mark></td><td><code>string</code></td><td>La chiave della Lista Di Valori richiesta</td></tr><tr><td>return_type (opzionale)</td><td><code>string</code></td><td>Il tipo in cui i dati devono essere restituiti<br>Il valore predefinito è <code>'list_of_objects'</code></td></tr><tr><td>sub_org_id (opzionale)</td><td><code>string</code></td><td>ID della sotto-organizzazione opzionale per il filtro<br>Il valore predefinito è <code>None</code></td></tr><tr><td>language_code<br>(opzionale)</td><td><code>string</code></td><td>Questo parametro imposta la lingua in cui verranno restituiti i valori. Accetta codici di lingua, come "en" per l'inglese o "fr" per il francese.<br>Il valore predefinito è <code>""</code></td></tr></tbody></table>

#### Restituisce:

* Valori LOV come lista di oggetti o come lista.

### **format\_decimal\_to\_locale()**

Formatta un valore decimale nel formato en\_US.UTF-8.

```python
standard_value = "{0:.2f}".format(total)
formatted_value = format_decimal_to_locale(
    standard_value, document_json['amount_format_locale']
)
```

#### Parametri:

<table><thead><tr><th width="208">Nome</th><th width="187">Tipo</th><th>Descrizione</th></tr></thead><tbody><tr><td>value<mark style="color:red;">*</mark></td><td><code>float, decimal.Decimal, str</code></td><td>Il valore che deve essere formattato.</td></tr><tr><td>to_locale (opzionale)</td><td><code>string</code></td><td>Il formato in cui il valore viene trasformato.<br>Il valore predefinito è <code>'en_US.UTF-8'</code></td></tr><tr><td>max_decimal_places (opzionale)</td><td><code>int</code></td><td>ID della sotto-organizzazione opzionale per il filtro<br>Il valore predefinito è <code>4</code></td></tr><tr><td>min_decimal_places (opzionale)</td><td><code>int</code></td><td>Il minimo di cifre decimali che devono essere considerate<br>Il valore predefinito è <code>2</code></td></tr></tbody></table>

* value: Il valore che deve essere formattato.
* to\_locale (opzionale): Il formato in cui il valore viene trasformato.
* max\_decimal\_places (opzionale): Il massimo di cifre decimali che devono essere considerate.
* min\_decimal\_places (opzionale): Il minimo di cifre decimali che devono essere considerate.

#### Restituisce:

* Il valore formattato.

### **compare\_values()**

Confronta due valori per uguaglianza, gestendo vari tipi di dati.

```python
result = compare_values(10, "10")
```

#### Parametri:

<table><thead><tr><th width="173">Nome</th><th width="176">Tipo</th><th>Descrizione</th></tr></thead><tbody><tr><td>value1<mark style="color:red;">*</mark></td><td><code>any</code></td><td>Il primo valore da confrontare</td></tr><tr><td>value2<mark style="color:red;">*</mark></td><td><code>any</code></td><td>Il secondo valore da confrontare</td></tr></tbody></table>

#### Restituisce:

* True se i valori sono uguali e False se differiscono

### **create\_document\_task()**

Crea un'attività, la assegna a un utente o a un gruppo, imposta la priorità e, facoltativamente, invia un'email.

```python
if not is_task_created:
            create_document_task(user, document_data, "Herkunftsland außerhalb der EU", "Die Gelangensbestätigung kommt von einem Land außerhalb der EU. Bitte das MRN-Dokument anhängen.", "high", 1007, None, False)
            document_data["document_json"]["country_check_task_created"] = True
```

#### Parametri:

<table><thead><tr><th width="216">Nome</th><th width="217">Tipo</th><th>Descrizione</th></tr></thead><tbody><tr><td>user<mark style="color:red;">*</mark></td><td>either <code>user ID</code> or <code>UserAuthentication</code> object</td><td>L'utente che esegue l'aggiornamento</td></tr><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>I dati del documento contenenti informazioni sui campi</td></tr><tr><td>title<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Il titolo dell'attività</td></tr><tr><td>description<mark style="color:red;">*</mark></td><td><code>string</code></td><td>La descrizione dell'attività</td></tr><tr><td>priority<mark style="color:red;">*</mark></td><td><code>string</code></td><td>La priorità dell'attività</td></tr><tr><td>assigned_to_user_id<mark style="color:red;">*</mark></td><td><code>int</code></td><td>L'id dell'utente a cui l'attività deve essere assegnata</td></tr><tr><td>assigned_to_group_id<mark style="color:red;">*</mark></td><td><code>int</code></td><td>L'id del gruppo a cui l'attività deve essere assegnata</td></tr><tr><td>send_email<mark style="color:red;">*</mark></td><td><code>bool</code></td><td>Determina se un'email deve essere inviata o meno</td></tr></tbody></table>

#### Restituisce:

* Dict che indica se il processo è stato completato con successo o meno

### **set\_document\_sub\_org\_id()**

Imposta il sub\_org\_id dei dati del documento specificato.

```python
if sub_org_id != current_sub_org_id:
    document_data["document_json"]["sub_org_id4"] = sub_org_id
    set_document_sub_org_id(document_data, sub_org_id)
```

#### Parametri:

<table><thead><tr><th width="173">Nome</th><th width="176">Tipo</th><th>Descrizione</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>I dati del documento contenenti informazioni sui campi</td></tr><tr><td>sub_org_id<mark style="color:red;">*</mark></td><td><code>string</code></td><td>ID della sotto-organizzazione opzionale per il filtro</td></tr></tbody></table>

### **get\_user\_by\_id()**

Ottiene l'utente con l'ID utente corrispondente.

```python
requester_mail = str(get_user_by_id(str(requester)).email.lower())
```

#### Parametri:

<table><thead><tr><th width="173">Nome</th><th width="176">Tipo</th><th>Descrizione</th></tr></thead><tbody><tr><td>user_id<mark style="color:red;">*</mark></td><td><code>string</code></td><td>L'ID dell'utente</td></tr></tbody></table>

#### Restituisce:

* L'utente con l'ID utente corrispondente

### **get\_group\_by\_id()**

Ottiene il gruppo con l'ID gruppo corrispondente.

```python
group_name  = str(get_group_by_id(assigned_to_group_id))
```

#### Parametri:

<table><thead><tr><th width="173">Nome</th><th width="176">Tipo</th><th>Descrizione</th></tr></thead><tbody><tr><td>group_id<mark style="color:red;">*</mark></td><td><code>string</code></td><td>L'ID del gruppo</td></tr></tbody></table>

#### Restituisce:

* Il gruppo con l'ID gruppo corrispondente

### **get\_user\_by\_email()**

Ottiene il gruppo con l'ID gruppo corrispondente.

```python
user_name = str(get_user_by_email(email)
```

#### Parametri:

<table><thead><tr><th width="173">Nome</th><th width="176">Tipo</th><th>Descrizione</th></tr></thead><tbody><tr><td>email<mark style="color:red;">*</mark></td><td><code>any</code></td><td>L'email dell'utente</td></tr></tbody></table>

#### Restituisce:

* L'utente con l'email corrispondente

### **add\_table\_column()**

Aggiunge una colonna alla tabella specificata.

```python
table = tables_dict.get("ORDER_CONFIRMATION_TABLE")

if table:
    add_table_column(table, "PROMISED_DELIVERY_DATE")
```

#### Parametri:

<table><thead><tr><th width="173">Nome</th><th width="176">Tipo</th><th>Descrizione</th></tr></thead><tbody><tr><td>table<mark style="color:red;">*</mark></td><td><code>string</code></td><td>La tabella in cui deve essere aggiunta la colonna</td></tr><tr><td>col_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Il nome della colonna</td></tr><tr><td>default_value (opzionale)</td><td><code>any</code></td><td><p>Il valore iniziale per il campo</p><p>Il valore predefinito è <code>None</code></p></td></tr></tbody></table>

### **get\_column\_value()**

Ottiene il valore di una colonna specificata.

```python
for row in table['rows']:
        unit = get_column_value(row, "UNIT")
```

#### Parametri:

<table><thead><tr><th width="173">Nome</th><th width="176">Tipo</th><th>Descrizione</th></tr></thead><tbody><tr><td>row<mark style="color:red;">*</mark></td><td><code>string</code></td><td>La riga in cui si trova il valore</td></tr><tr><td>col_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Il nome della colonna</td></tr><tr><td>default_value (opzionale)</td><td><code>any</code></td><td>Il valore iniziale per il campo<br>Il valore predefinito è <code>None</code></td></tr><tr><td>is_clean (opzionale)</td><td><code>bool</code></td><td>Converte il valore in maiuscolo e rimuove eventuali spazi extra<br>Il valore predefinito è <code>False</code></td></tr></tbody></table>

#### Restituisce

* Restituisce il valore della colonna specificata se esiste; altrimenti, restituisce `None`

### **set\_column\_value()**

Imposta il valore della colonna specificata. Se la colonna non esiste, verrà creata.

```python
supplier_id = get_field_value(document_data, "supplier_id", "")

quote_table = tables_dict["QUOTE_TABLE"]

for row in quote_table.get('rows', []):
    set_column_value(row,"SUPPLIER_ID", supplier_id)
```

#### Parametri:

<table><thead><tr><th width="173">Nome</th><th width="176">Tipo</th><th>Descrizione</th></tr></thead><tbody><tr><td>row<mark style="color:red;">*</mark></td><td><code>string</code></td><td>La riga in cui si trova il valore</td></tr><tr><td>col_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Il nome della colonna</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>any</code></td><td>Il valore che verrà impostato nella posizione specificata</td></tr></tbody></table>

#### Restituisce:

* True se la modifica è stata eseguita con successo

### **set\_column\_date\_value()**

Imposta il valore della data di una colonna specificata.

```python
set_column_date_value(document_data, row, "DELIVERY_DATE", "2020-12-31", add_days=2)
```

#### Parametri:

<table><thead><tr><th width="173">Nome</th><th width="196.05859375">Tipo</th><th>Descrizione</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>I dati del documento contenenti informazioni sui campi</td></tr><tr><td>row<mark style="color:red;">*</mark></td><td><code>string</code></td><td>La riga in cui si trova il valore</td></tr><tr><td>col_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Il nome della colonna</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Il valore della data da impostare in formato ISO (ad es., "2020-12-31")</td></tr><tr><td>add_days (opzionale)</td><td><code>int</code></td><td>Aggiunge giorni aggiuntivi alla data fornita<br>Il valore predefinito è <code>2</code></td></tr><tr><td>skip_weekend (opzionale)</td><td><code>bool</code></td><td>Salta la data se cade nel fine settimana<br>Il valore predefinito è <code>False</code></td></tr><tr><td>exclude_final_days<br>(opzionale)</td><td>either <code>string</code> or <code>int</code></td><td>Specifica i giorni da escludere (0-6 o Domenica a Sabato)</td></tr></tbody></table>

### **set\_column\_amount\_value()**

* Converte il valore in stringa e imposta il valore per la colonna
* Imposta il contenuto della colonna al valore
* Format value according to the locale

```python
quantity = float(quantity) / 1000
set_column_amount_value(document_data, row, "QUANTITY", str(quantity))
```

#### Parametri:

<table><thead><tr><th width="173">Nome</th><th width="176">Tipo</th><th>Descrizione</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>I dati del documento contenenti informazioni sui campi</td></tr><tr><td>row<mark style="color:red;">*</mark></td><td><code>string</code></td><td>La riga in cui si trova il valore</td></tr><tr><td>column_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Il nome della colonna</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Il valore da impostare per il campo (passa un numero come stringa ad es., "123456")</td></tr></tbody></table>

### **delete\_tables()**

Questa funzione elimina le tabelle dai dati del documento.

```python
delete_tables(document_data)
```

#### Parametri:

<table><thead><tr><th width="173">Nome</th><th width="176">Tipo</th><th>Descrizione</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>I dati del documento contenenti informazioni sui campi</td></tr></tbody></table>

### **restore\_tables()**

Questa funzione ripristina le tabelle nei dati del documento.

```python
restore_tables(document_data)
```

#### Parametri:

<table><thead><tr><th width="173">Nome</th><th width="176">Tipo</th><th>Descrizione</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>I dati del documento contenenti informazioni sui campi</td></tr></tbody></table>

### **remove\_rows\_from\_table()**

Rimuove righe dalla tabella specificata.

```python
count = 1
start = 1
remove_rows_from_table(document_data,"INVOICE_TABLE",count,start) 
```

#### Parametri:

<table><thead><tr><th width="173">Nome</th><th width="176">Tipo</th><th>Descrizione</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>I dati del documento contenenti informazioni sui campi</td></tr><tr><td>table_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Il nome della tabella</td></tr><tr><td>count<mark style="color:red;">*</mark></td><td><code>int</code></td><td>Quante righe devono essere eliminate</td></tr><tr><td>start<mark style="color:red;">*</mark></td><td><code>int</code></td><td>Il punto di partenza</td></tr></tbody></table>

### **remove\_all\_rows\_except\_one\_from\_table()**

Rimuove tutte le righe tranne una dalla tabella specificata

```python
count = 1
start = 1
remove_rows_from_table(document_data,"INVOICE_TABLE",count,start) 
```

#### Parametri:

<table><thead><tr><th width="173">Nome</th><th width="176">Tipo</th><th>Descrizione</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>I dati del documento contenenti informazioni sui campi</td></tr><tr><td>line_number<mark style="color:red;">*</mark></td><td><code>int</code></td><td>Il numero della riga che non deve essere rimossa</td></tr></tbody></table>

## Attributi Supportati

### Attributi Campo Principali

| Attributo           | Tipo   | Descrizione                                                |
| ------------------- | ------ | ---------------------------------------------------------- |
| `value`             | any    | Il valore grezzo del campo                                 |
| `formatted_value`   | string | Valore formattato per la visualizzazione                   |
| `content`           | string | Contenuto estratto originale                               |
| `is_required`       | bool   | Se il campo è obbligatorio                                 |
| `is_valid`          | bool   | Stato di validazione                                       |
| `is_validated`      | bool   | Se il campo è stato validato dall'utente                   |
| `force_validation`  | bool   | Forza l'utente a validare questo campo                     |
| `highlight_field`   | bool   | Evidenzia il campo nell'interfaccia utente                 |
| `extraction_method` | string | Come è stato estratto il valore (ad es., `"SCRIPT"`)       |

### Attributi di Validazione

| Attributo               | Tipo   | Descrizione                                                              |
| ----------------------- | ------ | ------------------------------------------------------------------------ |
| `validation_message`    | string | Messaggio di errore mostrato all'utente                                  |
| `validation_code`       | string | Codice di errore (ad es., `"FORCED_VALIDATION"`, `"INVALID_VALUE"`)      |
| `invalidated_by_script` | bool   | Contrassegna il campo come invalidato da uno script                      |

### Attributi di Estrazione/OCR

| Attributo           | Tipo   | Descrizione                                              |
| ------------------- | ------ | -------------------------------------------------------- |
| `coords`            | object | Coordinate del riquadro di delimitazione sul documento   |
| `confidence`        | float  | Punteggio di confidenza OCR/estrazione                   |
| `score`             | float  | Punteggio di corrispondenza/validazione                  |
| `score_description` | string | Descrizione del punteggio                                |
| `page`              | int    | Numero di pagina dove è stato trovato il campo           |
| `rule`              | string | Regola di estrazione che è stata applicata               |

## Funzioni Incorporate di Python

Puoi anche utilizzare alcune delle funzioni incorporate di Python:

* abs(): Restituisce il valore assoluto di un numero.
* len(): Restituisce la lunghezza (numero di elementi) di un oggetto, come una lista o una stringa.
* isinstance(): Controlla se un oggetto è un'istanza di una particolare classe o tipo.
* print(): Stampa l'output sulla console.
* round(): Arrotonda un numero in virgola mobile a un numero specificato di cifre decimali.
* str\_to\_bool(): Converte una stringa in un valore booleano (True o False).
* type(): Restituisce il tipo di un oggetto.
* dict(): Crea un oggetto dizionario.
* list(): Crea un oggetto lista.
* str(): Converte un valore in una stringa.
* float(): Converte un valore in un numero in virgola mobile.
* int(): Converte un valore in un intero.

Per ulteriori dettagli, visita la documentazione ufficiale di Python: [Funzioni Incorporate](https://docs.python.org/3.12/library/functions.html).

## Funzioni della Classe String

Puoi anche utilizzare queste funzioni specificamente per lavorare con le stringhe:

* lower(): Converte tutti i caratteri in una stringa in minuscolo.
* upper(): Converte tutti i caratteri in una stringa in maiuscolo.
* split(): Divide una stringa in una lista in base a un delimitatore (ad es., spazio o virgola).
* startswith(): Controlla se una stringa inizia con un prefisso specificato.
* endswith(): Controlla se una stringa termina con un suffisso specificato.
* strip(): Rimuove eventuali spazi bianchi all'inizio o alla fine di una stringa.

## Funzioni del Modulo Matematico di Python

Queste funzioni fanno parte del modulo matematico e sono utili per operazioni matematiche:

* floor(): Restituisce l'intero più grande minore o uguale a un numero dato.
* ceil(): Restituisce l'intero più piccolo maggiore o uguale a un numero dato.

Per ulteriori informazioni, consulta la documentazione ufficiale di Python: [Funzioni del Modulo Matematico](https://docs.python.org/3/library/math.html).

## Funzione di Espressione Regolare

* re.search(): Cerca un modello all'interno di una stringa e restituisce la prima corrispondenza.

Vedi ulteriori dettagli qui: [Documentazione re.search](https://docs.python.org/3/library/re.html#re.search).

## Funzioni Esterne

Ecco alcune funzioni utili da librerie esterne:

* deepcopy(): Crea una copia di un oggetto, inclusi oggetti annidati (dal modulo copy).\
  [Documentazione Deepcopy](https://docs.python.org/3/library/copy.html#copy.deepcopy).
* levenshtein\_distance(): Calcola il numero di modifiche (inserimenti, eliminazioni, sostituzioni) necessarie per cambiare una stringa in un'altra. Questa funzione è disponibile nella [libreria Jellyfish](https://jamesturk.github.io/jellyfish/functions/).

## Funzioni di Data e Ora

Puoi utilizzare le seguenti funzioni per lavorare con date e orari:

* strptime(): Converte una stringa in un oggetto datetime in base a un formato specificato.
* strftime(): Formattta un oggetto datetime in una stringa in base a un formato specificato.

Per ulteriori informazioni, consulta la documentazione ufficiale:\
[Funzioni di Data e Ora](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior).
