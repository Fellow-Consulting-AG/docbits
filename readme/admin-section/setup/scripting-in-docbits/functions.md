# Funktionen

## **Funktionale Dokumentation**

Dieses Modul enthält Funktionen zur Manipulation von Dokumentdaten und zur Durchführung verschiedener Operationen im Zusammenhang mit Dokumentfeldern.

## **Funktionen**

### **set\_field\_value()**

Setzt den Wert eines Feldes in den Dokumentdaten.

```python
po_number = get_field_value(fields_dict, 'purchase_order', None)
if not po_number:
    po_number = ''
    
if po_number:
    set_field_value(fields_dict, "invoice_sub_type", 'Purchase Invoice')
else:
    set_field_value(fields_dict, "invoice_sub_type", 'Cost Invoice')
```

#### Parameter:

<table><thead><tr><th width="177">Name</th><th width="176">Typ</th><th>Beschreibung</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Die Dokumentdaten, die Feldinformationen enthalten</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Der Name des zu setzenden Feldes</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>any</code></td><td>Der Wert, der für das Feld gesetzt werden soll</td></tr><tr><td>remove_link (optional)</td><td><code>bool</code></td><td>Entfernt den "coords"-Schlüssel aus dem Feld.</td></tr></tbody></table>

### **set\_date\_value()**

Setzt den Wert eines Datumsfeldes in den Dokumentdaten.

```python
invoice_date = get_field_value(document_data, 'invoice_date', None)
    
if not document_json.get("script_executed", False):
    if invoice_date:
        set_date_value(document_data, "accounting_date", invoice_date)
        document_json["script_executed"] = True
```

#### Parameter:

<table><thead><tr><th width="229">Name</th><th width="196.0316162109375">Typ</th><th>Beschreibung</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Die Dokumentdaten, die Feldinformationen enthalten</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Der Name des zu setzenden Feldes</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Der Datumswert, der im ISO-Format gesetzt werden soll (z.B. "2020-12-31").</td></tr><tr><td>add_days (optional)</td><td><code>int</code></td><td>Fügt zusätzliche Tage zum angegebenen Datum hinzu<br>Standard ist 0</td></tr><tr><td>skip_weekend (optional)</td><td><code>bool</code></td><td>Überspringt das Datum, wenn es auf das Wochenende fällt<br>Standard ist <code>False</code></td></tr><tr><td>remove link (optional)</td><td><code>bool</code></td><td>Entfernt den "coords"-Schlüssel aus dem Feld.</td></tr><tr><td>exclude_final_days<br>(optional)</td><td>entweder <code>string</code> oder <code>int</code></td><td>Gibt die auszuschließenden Tage an (0-6 oder Sonntag bis Samstag)</td></tr></tbody></table>

### **set\_amount\_value()**

Setzt den Wert eines Betragsfeldes in den Dokumentdaten.

```python
total_amount = get_field_value(document_data, "net_amount")
lines_total = 0.0
set_amount_value(document_data, "net_amount",str(lines_total))
```

#### Parameter:

<table><thead><tr><th width="183.71087646484375">Name</th><th width="176">Typ</th><th>Beschreibung</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Die Dokumentdaten, die Feldinformationen enthalten</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Der Name des zu setzenden Feldes</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Der Wert, der für das Feld gesetzt werden soll (geben Sie eine Zahl als String an, z.B. "123456")</td></tr><tr><td>remove link (optional)</td><td><code>bool</code></td><td>Entfernt den "coords"-Schlüssel aus dem Feld.</td></tr></tbody></table>

### **get\_field\_value()**

Erhält den Wert eines Feldes aus den Dokumentdaten.

```python
total_amount = get_field_value(document_data, "net_amount")
lines_total = 0.0
set_amount_value(document_data, "net_amount", str(lines_total))
```

#### Parameter:

<table><thead><tr><th width="191">Name</th><th width="176">Typ</th><th>Beschreibung</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Die Dokumentdaten, die Feldinformationen enthalten</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Der Name des zu setzenden Feldes</td></tr><tr><td>default_value (optional)</td><td><code>any</code></td><td>Gibt default_value zurück, wenn kein Feldwert gefunden wird<br>Standard ist <code>None</code></td></tr><tr><td>is_clean (optional)</td><td><code>bool</code></td><td>Konvertiert den Wert in Großbuchstaben und entfernt zusätzliche Leerzeichen<br>Standard ist <code>False</code></td></tr></tbody></table>

#### Gibt zurück:

* Wert des angegebenen Feldes

### **create\_new\_field()**

Erstellt ein neues Feld mit dem angegebenen Namen und Wert.

```python
currency = get_field_value(document_data, 'currency', None)

if not currency:
    if 'currency' not in fields_dict:
        new_field = create_new_field('currency','')
        fields_dict['currency'] = new_field
        document_json['fields'].append(new_field)
    set_field_value(document_data, "currency", "USD")
```

#### Parameter:

<table><thead><tr><th width="140">Name</th><th width="133">Typ</th><th>Beschreibung</th></tr></thead><tbody><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>str</code></td><td>Die Dokumentdaten, die Feldinformationen enthalten</td></tr><tr><td>value (optional)</td><td><code>any</code></td><td>Der Anfangswert für das Feld<br>Standard ist <code>""</code></td></tr></tbody></table>

#### Gibt zurück:

* Dictionary des neu erstellten Feldes

### **delete\_field()**

Löscht ein Feld aus den Dokumentdaten.

```python
field_amount = get_field_value(document_data, field_name)
    if not field_amount:
        delete_field(document_data, fields_dict, field_name)
    else:
        field_amount = float(field_amount)
        if field_amount == 0:
            delete_field(document_data, fields_dict, field_name)
```

#### Parameter:

<table><thead><tr><th width="173">Name</th><th width="176">Typ</th><th>Beschreibung</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Die Dokumentdaten, die Feldinformationen enthalten</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Der Name des zu löschenden Feldes</td></tr></tbody></table>

#### Gibt zurück:

* Document\_data als json und als dict, nachdem das Feld gelöscht wurde

### **set\_is\_required()**

Setzt das Attribut 'is\_required' eines Feldes in den Dokumentdaten.

```python
net_amount = get_field_value(document_data, "net_amount", None)
if net_amount:
    set_is_required(document_data, "tax_country", True)
    set_is_required(document_data, "tax_code_without_country", True)
```

#### Parameter:

<table><thead><tr><th width="173">Name</th><th width="176">Typ</th><th>Beschreibung</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Die Dokumentdaten, die Feldinformationen enthalten</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Der Name des zu setzenden Feldes</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>bool</code></td><td>Der Wert, der für das Feld gesetzt werden soll</td></tr></tbody></table>

### **set\_force\_validation()**

Setzt das Attribut 'force\_validation' eines Feldes in den Dokumentdaten.

```python
if supplier_id in supplier_to_check:
    set_force_validation(document_data, 'purchase_order', True, reset_validation=reset_validation)
```

#### Parameter:

<table><thead><tr><th width="173">Name</th><th width="176">Typ</th><th>Beschreibung</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Die Dokumentdaten, die Feldinformationen enthalten</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Der Name des zu setzenden Feldes</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>bool</code></td><td>Der Wert, der für das Feld gesetzt werden soll</td></tr><tr><td>reset_validation (optional)</td><td><code>bool</code></td><td>Setzt das Attribut "is_validated" auf den angegebenen Wert<br>Standard ist <code>False</code></td></tr></tbody></table>

### **set\_field\_as\_invalid()**

Markiert ein Feld im Validierungsbildschirm als ungültig und hebt es hervor.

```python
if not document_date:
    set_field_as_invalid(document_data, "document_date", "Es ist kein Datum vorhanden", "INVALID_VALUE")
```

#### Parameter:

<table><thead><tr><th width="173">Name</th><th width="176">Typ</th><th>Beschreibung</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Die Dokumentdaten, die Feldinformationen enthalten</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Der Name des Feldes, das als ungültig markiert werden soll</td></tr><tr><td>message<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Die Validierungsnachricht für das Feld</td></tr><tr><td>code (optional)</td><td><code>string</code></td><td><p>Fehlercode für die Validierung</p><p>Standard ist <code>None</code></p></td></tr></tbody></table>

### **set\_field\_attribute()**

Setzt ein benutzerdefiniertes Attribut eines Feldes in den Dokumentdaten.

```python
if purchase_order:
    if po_supplier_id != invoice_supplier_id:
        set_field_as_invalid(document_data, "supplier_name", "Supplier is different from PO supplier")
    else:
        set_field_attribute(document_data, "supplier_name", "is_valid", True)
        set_field_attribute(document_data, "supplier_name", "validation_message","")
```

#### Parameter:

<table><thead><tr><th width="173">Name</th><th width="176">Typ</th><th>Beschreibung</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Die Dokumentdaten, die Feldinformationen enthalten</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Der Name des zu setzenden Feldes</td></tr><tr><td>attribute_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Der Name des Attributs, das gesetzt werden soll</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>any</code></td><td>Der Wert, der für das Attribut gesetzt werden soll</td></tr></tbody></table>

### **is\_supplier\_valid()**

Überprüft, ob ein Lieferant basierend auf den angegebenen Kriterien gültig ist.

```python
bool = is_supplier_valid(user, {"name": "Supplier Inc."})
```

#### Parameter:

<table><thead><tr><th width="203">Name</th><th width="216">Typ</th><th>Beschreibung</th></tr></thead><tbody><tr><td>user<mark style="color:red;">*</mark></td><td><code>UserAuthentication</code></td><td>Der authentifizierte Benutzer</td></tr><tr><td>filter_data_json<mark style="color:red;">*</mark></td><td><code>json</code></td><td>Filterkriterien zur Validierung des Lieferanten</td></tr><tr><td>sub_org_id (optional)</td><td><code>string</code></td><td>Optionale Sub-Organisations-ID für die Filterung<br>Standard ist <code>None</code></td></tr></tbody></table>

#### Gibt zurück:

* True, wenn der Benutzer gültig ist
* False, wenn der Benutzer ungültig ist

### **get\_document\_content()**

Dekodiert Dokumentdaten und gibt sie als String zurück.

```python
document_content = get_document_content(doc)
if document_content:
    document_content = document_content.lower()
```

#### Parameter:

<table><thead><tr><th width="173">Name</th><th width="176">Typ</th><th>Beschreibung</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Die Dokumentdaten, die Feldinformationen enthalten</td></tr></tbody></table>

#### Gibt zurück:

* Dokumentdaten als String.

### **update\_document\_status\_with\_doc\_id()**

Aktualisiert den Status eines Dokuments mit einer bestimmten ID auf den angegebenen Status.

```python
genehmigung_user_1 = get_field_value(document_data, 'genehmigung_user_1', None)

if genehmigung_user_1 != "LEER":
    update_document_status_with_doc_id(document_json['doc_id'], user, document_json['org_id'], "validated_pending_approval")
```

#### Parameter:

<table><thead><tr><th width="228">Name</th><th width="216">Typ</th><th>Beschreibung</th></tr></thead><tbody><tr><td>doc_id<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Die ID des zu aktualisierenden Dokuments</td></tr><tr><td>user<mark style="color:red;">*</mark></td><td>entweder <code>user ID</code> oder <code>UserAuthentication</code> Objekt</td><td>Der Benutzer, der die Aktualisierung durchführt</td></tr><tr><td>org_id<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Die ID der Organisation, zu der das Dokument gehört</td></tr><tr><td>status<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Der neue Status des Dokuments</td></tr><tr><td>message (optional)</td><td><code>string</code></td><td>Optionale Nachricht, die mit der Statusaktualisierung verbunden ist<br>Standard ist <code>None</code></td></tr><tr><td>doc_classification_class (optional)</td><td><code>string</code></td><td>Optionale Dokumentklassifikationsklasse<br>Standard ist <code>None</code></td></tr></tbody></table>

### **get\_lov\_values()**

Erhält die LOV-Werte von einer bestimmten org\_id und einem Schlüssel.

```python
reverse_charge_to_check = get_lov_values(org_id, 'Kosten', return_type="list_of_values")
```

#### Parameter:

<table><thead><tr><th width="173">Name</th><th width="176">Typ</th><th>Beschreibung</th></tr></thead><tbody><tr><td>org_id<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Die ID der Organisation, zu der das Dokument gehört</td></tr><tr><td>key<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Der Schlüssel der benötigten Liste von Werten</td></tr><tr><td>return_type (optional)</td><td><code>string</code></td><td>Der Typ, in dem die Daten zurückgegeben werden sollen<br>Standard ist <code>'list_of_objects'</code></td></tr><tr><td>sub_org_id (optional)</td><td><code>string</code></td><td>Optionale Sub-Organisations-ID für die Filterung<br>Standard ist <code>None</code></td></tr><tr><td>language_code<br>(optional)</td><td><code>string</code></td><td>Dieser Parameter legt die Sprache fest, in der die Werte zurückgegeben werden. Er akzeptiert Sprachcodes, wie "en" für Englisch oder "fr" für Französisch.<br>Standard ist <code>""</code></td></tr></tbody></table>

#### Gibt zurück:

* LOV-Werte als Liste von Objekten oder als Liste.

### **format\_decimal\_to\_locale()**

Formatiert einen Dezimalwert im Format en\_US.UTF-8.

```python
standard_value = "{0:.2f}".format(total)
formatted_value = format_decimal_to_locale(
    standard_value, document_json['amount_format_locale']
)
```

#### Parameter:

<table><thead><tr><th width="208">Name</th><th width="187">Typ</th><th>Beschreibung</th></tr></thead><tbody><tr><td>value<mark style="color:red;">*</mark></td><td><code>float, decimal.Decimal, str</code></td><td>Der Wert, der formatiert werden soll.</td></tr><tr><td>to_locale (optional)</td><td><code>string</code></td><td>Das Format, in das der Wert umgewandelt werden soll.<br>Standard ist <code>'en_US.UTF-8'</code></td></tr><tr><td>max_decimal_places (optional)</td><td><code>int</code></td><td>Die maximale Anzahl von Dezimalstellen, die berücksichtigt werden sollen.<br>Standard ist <code>4</code></td></tr><tr><td>min_decimal_places (optional)</td><td><code>int</code></td><td>Die minimale Anzahl von Dezimalstellen, die berücksichtigt werden sollen.<br>Standard ist <code>2</code></td></tr></tbody></table>

* value: Der Wert, der formatiert werden soll.
* to\_locale (optional): Das Format, in das der Wert umgewandelt wird.
* max\_decimal\_places (optional): Die maximale Anzahl von Dezimalstellen, die berücksichtigt werden sollen.
* min\_decimal\_places (optional): Die minimale Anzahl von Dezimalstellen, die berücksichtigt werden sollen.

#### Gibt zurück:

* Den formatierten Wert.

### **compare\_values()**

Vergleicht zwei Werte auf Gleichheit und behandelt verschiedene Datentypen.

```python
result = compare_values(10, "10")
```

#### Parameter:

<table><thead><tr><th width="173">Name</th><th width="176">Typ</th><th>Beschreibung</th></tr></thead><tbody><tr><td>value1<mark style="color:red;">*</mark></td><td><code>any</code></td><td>Der erste Wert, der verglichen werden soll</td></tr><tr><td>value2<mark style="color:red;">*</mark></td><td><code>any</code></td><td>Der zweite Wert, der verglichen werden soll</td></tr></tbody></table>

#### Gibt zurück:

* True, wenn die Werte gleich sind, und False, wenn sie unterschiedlich sind.

### **create\_document\_task()**

Erstellt eine Aufgabe, weist sie einem Benutzer oder einer Gruppe zu, setzt die Priorität und sendet optional eine E-Mail.

```python
if not is_task_created:
            create_document_task(user, document_data, "Herkunftsland außerhalb der EU", "Die Gelangensbestätigung kommt von einem Land außerhalb der EU. Bitte das MRN-Dokument anhängen.", "high", 1007, None, False)
            document_data["document_json"]["country_check_task_created"] = True
```

#### Parameter:

<table><thead><tr><th width="216">Name</th><th width="217">Typ</th><th>Beschreibung</th></tr></thead><tbody><tr><td>user<mark style="color:red;">*</mark></td><td>entweder <code>user ID</code> oder <code>UserAuthentication</code> Objekt</td><td>Der Benutzer, der die Aktualisierung durchführt</td></tr><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Die Dokumentdaten, die Feldinformationen enthalten</td></tr><tr><td>title<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Der Titel der Aufgabe</td></tr><tr><td>description<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Die Beschreibung der Aufgabe</td></tr><tr><td>priority<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Die Priorität der Aufgabe</td></tr><tr><td>assigned_to_user_id<mark style="color:red;">*</mark></td><td><code>int</code></td><td>Die ID des Benutzers, dem die Aufgabe zugewiesen werden soll</td></tr><tr><td>assigned_to_group_id<mark style="color:red;">*</mark></td><td><code>int</code></td><td>Die ID der Gruppe, der die Aufgabe zugewiesen werden soll</td></tr><tr><td>send_email<mark style="color:red;">*</mark></td><td><code>bool</code></td><td>Bestimmt, ob eine E-Mail gesendet werden soll oder nicht</td></tr></tbody></table>

#### Gibt zurück:

* Dict, das angibt, ob der Prozess erfolgreich war oder nicht.

### **set\_document\_sub\_org\_id()**

Setzt die sub\_org\_id der angegebenen document\_data.

```python
if sub_org_id != current_sub_org_id:
    document_data["document_json"]["sub_org_id4"] = sub_org_id
    set_document_sub_org_id(document_data, sub_org_id)
```

#### Parameter:

<table><thead><tr><th width="173">Name</th><th width="176">Typ</th><th>Beschreibung</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Die Dokumentdaten, die Feldinformationen enthalten</td></tr><tr><td>sub_org_id<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Optionale Sub-Organisations-ID für die Filterung</td></tr></tbody></table>

### **get\_user\_by\_id()**

Erhält den Benutzer mit der entsprechenden Benutzer-ID.

```python
requester_mail = str(get_user_by_id(str(requester)).email.lower())
```

#### Parameter:

<table><thead><tr><th width="173">Name</th><th width="176">Typ</th><th>Beschreibung</th></tr></thead><tbody><tr><td>user_id<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Die ID des Benutzers</td></tr></tbody></table>

#### Gibt zurück:

* Den Benutzer mit der entsprechenden Benutzer-ID.

### **get\_group\_by\_id()**

Erhält die Gruppe mit der entsprechenden Gruppen-ID.

```python
group_name  = str(get_group_by_id(assigned_to_group_id))
```

#### Parameter:

<table><thead><tr><th width="173">Name</th><th width="176">Typ</th><th>Beschreibung</th></tr></thead><tbody><tr><td>group_id<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Die ID der Gruppe</td></tr></tbody></table>

#### Gibt zurück:

* Die Gruppe mit der entsprechenden Gruppen-ID.

### **get\_user\_by\_email()**

Erhält den Benutzer mit der entsprechenden E-Mail.

```python
user_name = str(get_user_by_email(email))
```

#### Parameter:

<table><thead><tr><th width="173">Name</th><th width="176">Typ</th><th>Beschreibung</th></tr></thead><tbody><tr><td>email<mark style="color:red;">*</mark></td><td><code>any</code></td><td>Die E-Mail des Benutzers</td></tr></tbody></table>

#### Gibt zurück:

* Den Benutzer mit der entsprechenden E-Mail.

### **add\_table\_column()**

Fügt eine Spalte zur angegebenen Tabelle hinzu.

```python
table = tables_dict.get("ORDER_CONFIRMATION_TABLE")

if table:
    add_table_column(table, "PROMISED_DELIVERY_DATE")
```

#### Parameter:

<table><thead><tr><th width="173">Name</th><th width="176">Typ</th><th>Beschreibung</th></tr></thead><tbody><tr><td>table<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Die Tabelle, in der die Spalte hinzugefügt werden soll</td></tr><tr><td>col_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Der Name der Spalte</td></tr><tr><td>default_value (optional)</td><td><code>any</code></td><td><p>Der Anfangswert für das Feld</p><p>Standard ist <code>None</code></p></td></tr></tbody></table>

### **get\_column\_value()**

Erhält den Wert einer bestimmten Spalte.

```python
for row in table['rows']:
        unit = get_column_value(row, "UNIT")
```

#### Parameter:

<table><thead><tr><th width="173">Name</th><th width="176">Typ</th><th>Beschreibung</th></tr></thead><tbody><tr><td>row<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Die Zeile, in der sich der Wert befindet</td></tr><tr><td>col_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Der Name der Spalte</td></tr><tr><td>default_value (optional)</td><td><code>any</code></td><td>Der Anfangswert für das Feld<br>Standard ist <code>None</code></td></tr><tr><td>is_clean (optional)</td><td><code>bool</code></td><td>Konvertiert den Wert in Großbuchstaben und entfernt zusätzliche Leerzeichen<br>Standard ist <code>False</code></td></tr></tbody></table>

#### Gibt zurück:

* Gibt den Wert der angegebenen Spalte zurück, wenn er existiert; andernfalls wird `None` zurückgegeben.

### **set\_column\_value()**

Setzt den Wert der angegebenen Spalte. Wenn die Spalte nicht existiert, wird sie erstellt.

```python
supplier_id = get_field_value(document_data, "supplier_id", "")

quote_table = tables_dict["QUOTE_TABLE"]

for row in quote_table.get('rows', []):
    set_column_value(row,"SUPPLIER_ID", supplier_id)
```

#### Parameter:

<table><thead><tr><th width="173">Name</th><th width="176">Typ</th><th>Beschreibung</th></tr></thead><tbody><tr><td>row<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Die Zeile, in der sich der Wert befindet</td></tr><tr><td>col_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Der Name der Spalte</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>any</code></td><td>Der Wert, der an der angegebenen Stelle gesetzt werden soll</td></tr></tbody></table>

#### Gibt zurück:

* True, wenn die Änderung erfolgreich war.

### **set\_column\_date\_value()**

Setzt den Datumswert einer bestimmten Spalte.

```python
set_column_date_value(document_data, row, "DELIVERY_DATE", "2020-12-31", add_days=2)
```

#### Parameter:

<table><thead><tr><th width="173">Name</th><th width="196.05859375">Typ</th><th>Beschreibung</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Die Dokumentdaten, die Feldinformationen enthalten</td></tr><tr><td>row<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Die Zeile, in der sich der Wert befindet</td></tr><tr><td>col_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Der Name der Spalte</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Der Datumswert, der im ISO-Format gesetzt werden soll (z.B. "2020-12-31")</td></tr><tr><td>add_days (optional)</td><td><code>int</code></td><td>Fügt zusätzliche Tage zum angegebenen Datum hinzu<br>Standard ist <code>2</code></td></tr><tr><td>skip_weekend (optional)</td><td><code>bool</code></td><td>Überspringt das Datum, wenn es auf das Wochenende fällt<br>Standard ist <code>False</code></td></tr><tr><td>exclude_final_days<br>(optional)</td><td>entweder <code>string</code> oder <code>int</code></td><td>Gibt die auszuschließenden Tage an (0-6 oder Sonntag bis Samstag)</td></tr></tbody></table>

### **set\_column\_amount\_value()**

* Konvertiert den Wert in einen String und setzt den Wert für die Spalte
* Setzt den Spalteninhalt auf den Wert
* Formatiert den Wert gemäß der Locale

```python
quantity = float(quantity) / 1000
set_column_amount_value(document_data, row, "QUANTITY", str(quantity))
```

#### Parameter:

<table><thead><tr><th width="173">Name</th><th width="176">Typ</th><th>Beschreibung</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Die Dokumentdaten, die Feldinformationen enthalten</td></tr><tr><td>row<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Die Zeile, in der sich der Wert befindet</td></tr><tr><td>column_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Der Name der Spalte</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Der Wert, der für das Feld gesetzt werden soll (geben Sie eine Zahl als String an, z.B. "123456")</td></tr></tbody></table>

### **delete\_tables()**

Diese Funktion löscht die Tabellen aus den Dokumentdaten.

```python
delete_tables(document_data)
```

#### Parameter:

<table><thead><tr><th width="173">Name</th><th width="176">Typ</th><th>Beschreibung</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Die Dokumentdaten, die Feldinformationen enthalten</td></tr></tbody></table>

### **restore\_tables()**

Diese Funktion stellt die Tabellen in den Dokumentdaten wieder her.

```python
restore_tables(document_data)
```

#### Parameter:

<table><thead><tr><th width="173">Name</th><th width="176">Typ</th><th>Beschreibung</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Die Dokumentdaten, die Feldinformationen enthalten</td></tr></tbody></table>

### **remove\_rows\_from\_table()**

Entfernt Zeilen aus der angegebenen Tabelle.

```python
count = 1
start = 1
remove_rows_from_table(document_data,"INVOICE_TABLE",count,start) 
```

#### Parameter:

<table><thead><tr><th width="173">Name</th><th width="176">Typ</th><th>Beschreibung</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Die Dokumentdaten, die Feldinformationen enthalten</td></tr><tr><td>table_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Der Name der Tabelle</td></tr><tr><td>count<mark style="color:red;">*</mark></td><td><code>int</code></td><td>Wie viele Zeilen gelöscht werden sollen</td></tr><tr><td>start<mark style="color:red;">*</mark></td><td><code>int</code></td><td>Der Ausgangspunkt</td></tr></tbody></table>

### **remove\_all\_rows\_except\_one\_from\_table()**

Entfernt alle Zeilen außer einer aus der angegebenen Tabelle.

```python
count = 1
start = 1
remove_rows_from_table(document_data,"INVOICE_TABLE",count,start) 
```

#### Parameter:

<table><thead><tr><th width="173">Name</th><th width="176">Typ</th><th>Beschreibung</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Die Dokumentdaten, die Feldinformationen enthalten</td></tr><tr><td>line_number<mark style="color:red;">*</mark></td><td><code>int</code></td><td>Die Nummer der Zeile, die nicht entfernt werden soll</td></tr></tbody></table>

## Python Eingebaute Funktionen

Sie können auch einige der eingebauten Python-Funktionen nutzen:

* abs(): Gibt den absoluten Wert einer Zahl zurück.
* len(): Gibt die Länge (Anzahl der Elemente) eines Objekts, wie einer Liste oder einem String, zurück.
* isinstance(): Überprüft, ob ein Objekt eine Instanz einer bestimmten Klasse oder eines bestimmten Typs ist.
* print(): Gibt Ausgaben auf der Konsole aus.
* round(): Rundet eine Fließkommazahl auf eine bestimmte Anzahl von Dezimalstellen.
* str\_to\_bool(): Konvertiert einen String in einen booleschen Wert (True oder False).
* type(): Gibt den Typ eines Objekts zurück.
* dict(): Erstellt ein Dictionary-Objekt.
* list(): Erstellt ein Listenobjekt.
* str(): Konvertiert einen Wert in einen String.
* float(): Konvertiert einen Wert in eine Fließkommazahl.
* int(): Konvertiert einen Wert in eine Ganzzahl.

Für weitere Details besuchen Sie die offizielle Python-Dokumentation: [Built-in Functions](https://docs.python.org/3.12/library/functions.html).

## String-Klassenfunktionen

Sie können auch diese Funktionen speziell für die Arbeit mit Strings verwenden:

* lower(): Konvertiert alle Zeichen in einem String in Kleinbuchstaben.
* upper(): Konvertiert alle Zeichen in einem String in Großbuchstaben.
* split(): Teilt einen String basierend auf einem Trennzeichen (z.B. Leerzeichen oder Komma) in eine Liste auf.
* startswith(): Überprüft, ob ein String mit einem bestimmten Präfix beginnt.
* endswith(): Überprüft, ob ein String mit einem bestimmten Suffix endet.
* strip(): Entfernt führende oder nachfolgende Leerzeichen aus einem String.

## Funktionen aus dem Python-Math-Modul

Diese Funktionen sind Teil des Math-Moduls und sind nützlich für mathematische Operationen:

* floor(): Gibt die größte Ganzzahl zurück, die kleiner oder gleich einer gegebenen Zahl ist.
* ceil(): Gibt die kleinste Ganzzahl zurück, die größer oder gleich einer gegebenen Zahl ist.

Für weitere Informationen siehe die offizielle Python-Dokumentation: [Math Module Functions](https://docs.python.org/3/library/math.html).

## Reguläre Ausdrucksfunktion

* re.search(): Durchsucht einen String nach einem Muster und gibt das erste Match zurück.

Siehe weitere Details hier: [re.search Dokumentation](https://docs.python.org/3/library/re.html#re.search).

## Externe Funktionen

Hier sind einige nützliche Funktionen aus externen Bibliotheken:

* deepcopy(): Erstellt eine Kopie eines Objekts, einschließlich verschachtelter Objekte (aus dem copy-Modul).\
  [Deepcopy Dokumentation](https://docs.python.org/3/library/copy.html#copy.deepcopy).
* levenshtein\_distance(): Berechnet die Anzahl der Änderungen (Einfügungen, Löschungen, Ersetzungen), die erforderlich sind, um einen String in einen anderen zu ändern. Diese Funktion ist in der [Jellyfish-Bibliothek](https://jamesturk.github.io/jellyfish/functions/) verfügbar.

## Datum- und Zeitfunktionen

Sie können die folgenden Funktionen für die Arbeit mit Daten und Zeiten verwenden:

* strptime(): Konvertiert einen String in ein datetime-Objekt basierend auf einem bestimmten Format.
* strftime(): Formatiert ein datetime-Objekt in einen String basierend auf einem bestimmten Format.

Für weitere Informationen siehe die offizielle Dokumentation:\
[Datum- und Zeitfunktionen](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior).
