# Functies

## **Functionele Documentatie**

Deze module bevat functies voor het manipuleren van documentgegevens en het uitvoeren van verschillende bewerkingen met betrekking tot documentvelden.

## **Functies**

### **set\_field\_value()**

Stelt de waarde van een veld in de documentgegevens in.

```python
po_number = get_field_value(fields_dict, 'purchase_order', None)
if not po_number:
    po_number = ''
    
if po_number:
    set_field_value(fields_dict, "invoice_sub_type", 'Purchase Invoice')
else:
    set_field_value(fields_dict, "invoice_sub_type", 'Cost Invoice')
```

#### Parameters:

<table><thead><tr><th width="177">Naam</th><th width="176">Type</th><th>Beschrijving</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>De documentgegevens met veldinformatie</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>De naam van het in te stellen veld</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>any</code></td><td>De waarde die voor het veld moet worden ingesteld</td></tr><tr><td>remove_link (optioneel)</td><td><code>bool</code></td><td>Verwijder de "coords" sleutel uit het veld.</td></tr></tbody></table>

### **set\_date\_value()**

Stelt de waarde van een datumveld in de documentgegevens in.

```python
invoice_date = get_field_value(document_data, 'invoice_date', None)
    
if not document_json.get("script_executed", False):
    if invoice_date:
        set_date_value(document_data, "accounting_date", invoice_date)
        document_json["script_executed"] = True
```

#### Parameters:

<table><thead><tr><th width="229">Naam</th><th width="196.0316162109375">Type</th><th>Beschrijving</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>De documentgegevens met veldinformatie</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>De naam van het in te stellen veld</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>string</code></td><td>De datumwaarde die in ISO-formaat moet worden ingesteld (bijv. "2020-12-31").</td></tr><tr><td>add_days (optioneel)</td><td><code>int</code></td><td>Voeg extra dagen toe aan de gegeven datum<br>Standaard is 0</td></tr><tr><td>skip_weekend (optioneel)</td><td><code>bool</code></td><td>Overslaat de datum als deze in het weekend valt<br>Standaard is <code>False</code></td></tr><tr><td>remove link (optioneel)</td><td><code>bool</code></td><td>Verwijder de "coords" sleutel uit het veld.</td></tr><tr><td>exclude_final_days<br>(optioneel)</td><td>of <code>string</code> of <code>int</code></td><td>Geeft de dagen op die moeten worden uitgesloten (0-6 of zondag tot zaterdag)</td></tr></tbody></table>

### **set\_amount\_value()**

Stelt de waarde van een bedragveld in de documentgegevens in.

```python
total_amount = get_field_value(document_data, "net_amount")
lines_total = 0.0
set_amount_value(document_data, "net_amount",str(lines_total))
```

#### Parameters:

<table><thead><tr><th width="183.71087646484375">Naam</th><th width="176">Type</th><th>Beschrijving</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>De documentgegevens met veldinformatie</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>De naam van het in te stellen veld</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>string</code></td><td>De waarde die voor het veld moet worden ingesteld (geef een nummer als string door, bijv. "123456")</td></tr><tr><td>remove link (optioneel)</td><td><code>bool</code></td><td>Verwijder de "coords" sleutel uit het veld.</td></tr></tbody></table>

### **get\_field\_value()**

Haalt de waarde van een veld uit de documentgegevens.

```python
total_amount = get_field_value(document_data, "net_amount")
lines_total = 0.0
set_amount_value(document_data, "net_amount", str(lines_total))
```

#### Parameters:

<table><thead><tr><th width="191">Naam</th><th width="176">Type</th><th>Beschrijving</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>De documentgegevens met veldinformatie</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>De naam van het in te stellen veld</td></tr><tr><td>default_value (optioneel)</td><td><code>any</code></td><td>Geeft default_value terug als er geen veldwaarde wordt gevonden<br>Standaard is <code>None</code></td></tr><tr><td>is_clean (optioneel)</td><td><code>bool</code></td><td>Converteert de waarde naar hoofdletters en verwijdert extra spaties<br>Standaard is <code>False</code></td></tr></tbody></table>

#### Retourneert:

* Waarde van het opgegeven veld

### **create\_new\_field()**

Maakt een nieuw veld met de opgegeven naam en waarde.

```python
currency = get_field_value(document_data, 'currency', None)

if not currency:
    if 'currency' not in fields_dict:
        new_field = create_new_field('currency','')
        fields_dict['currency'] = new_field
        document_json['fields'].append(new_field)
    set_field_value(document_data, "currency", "USD")
```

#### Parameters:

<table><thead><tr><th width="140">Naam</th><th width="133">Type</th><th>Beschrijving</th></tr></thead><tbody><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>str</code></td><td>De documentgegevens met veldinformatie</td></tr><tr><td>value (optioneel)</td><td><code>any</code></td><td>De initiële waarde voor het veld<br>Standaard is <code>""</code></td></tr></tbody></table>

#### Retourneert:

* Woordenboek van het nieuw aangemaakte veld

### **delete\_field()**

Verwijdert een veld uit de documentgegevens

```python
field_amount = get_field_value(document_data, field_name)
    if not field_amount:
        delete_field(document_data, fields_dict, field_name)
    else:
        field_amount = float(field_amount)
        if field_amount == 0:
            delete_field(document_data, fields_dict, field_name)
```

#### Parameters:

<table><thead><tr><th width="173">Naam</th><th width="176">Type</th><th>Beschrijving</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>De documentgegevens met veldinformatie</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>De naam van het te verwijderen veld</td></tr></tbody></table>

#### Retourneert:

* Document\_data als json en als dict nadat het veld is verwijderd

### **set\_is\_required()**

Stelt het 'is\_required' attribuut van een veld in de documentgegevens in.

```python
net_amount = get_field_value(document_data, "net_amount", None)
if net_amount:
    set_is_required(document_data, "tax_country", True)
    set_is_required(document_data, "tax_code_without_country", True)
```

#### Parameters:

<table><thead><tr><th width="173">Naam</th><th width="176">Type</th><th>Beschrijving</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>De documentgegevens met veldinformatie</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>De naam van het in te stellen veld</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>bool</code></td><td>De waarde die voor het veld moet worden ingesteld</td></tr></tbody></table>

### **set\_force\_validation()**

Stelt het 'force\_validation' attribuut van een veld in de documentgegevens in.

```python
if supplier_id in supplier_to_check:
    set_force_validation(document_data, 'purchase_order', True, reset_validation=reset_validation)
```

#### Parameters:

<table><thead><tr><th width="173">Naam</th><th width="176">Type</th><th>Beschrijving</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>De documentgegevens met veldinformatie</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>De naam van het in te stellen veld</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>bool</code></td><td>De waarde die voor het veld moet worden ingesteld</td></tr><tr><td>reset_validation (optioneel)</td><td><code>bool</code></td><td>Stelt het "is_validated" attribuut in op de opgegeven waarde<br>Standaard is <code>False</code></td></tr></tbody></table>

### **set\_field\_as\_invalid()**

Markeert een veld in het validatiescherm als ongeldig en markeert het.

```python
if not document_date:
    set_field_as_invalid(document_data, "document_date", "Es ist kein Datum vorhanden", "INVALID_VALUE")
```

#### Parameters:

<table><thead><tr><th width="173">Naam</th><th width="176">Type</th><th>Beschrijving</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>De documentgegevens met veldinformatie</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>De naam van het veld dat als ongeldig moet worden gemarkeerd</td></tr><tr><td>message<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Het validatiebericht voor het veld</td></tr><tr><td>code (optioneel)</td><td><code>string</code></td><td><p>Foutcode voor de validatie</p><p>Standaard is <code>None</code></p></td></tr></tbody></table>

### **set\_field\_attribute()**

Stelt een aangepast attribuut van een veld in de documentgegevens in.

```python
if purchase_order:
    if po_supplier_id != invoice_supplier_id:
        set_field_as_invalid(document_data, "supplier_name", "Supplier is different from PO supplier")
    else:
        set_field_attribute(document_data, "supplier_name", "is_valid", True)
        set_field_attribute(document_data, "supplier_name", "validation_message","")
```

#### Parameters:

<table><thead><tr><th width="173">Naam</th><th width="176">Type</th><th>Beschrijving</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>De documentgegevens met veldinformatie</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>De naam van het in te stellen veld</td></tr><tr><td>attribute_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>De naam van het in te stellen attribuut</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>any</code></td><td>De waarde die voor het attribuut moet worden ingesteld</td></tr></tbody></table>

### **is\_supplier\_valid()**

Controleert of een leverancier geldig is op basis van de opgegeven criteria.

```python
bool = is_supplier_valid(user, {"name": "Supplier Inc."})
```

#### Parameters:

<table><thead><tr><th width="203">Naam</th><th width="216">Type</th><th>Beschrijving</th></tr></thead><tbody><tr><td>user<mark style="color:red;">*</mark></td><td><code>UserAuthentication</code></td><td>De geauthenticeerde gebruiker</td></tr><tr><td>filter_data_json<mark style="color:red;">*</mark></td><td><code>json</code></td><td>Filtercriteria voor het valideren van de leverancier</td></tr><tr><td>sub_org_id (optioneel)</td><td><code>string</code></td><td>Optionele sub-organisatie-ID voor filtering<br>Standaard is <code>None</code></td></tr></tbody></table>

#### Retourneert:

* True, als de gebruiker geldig is
* False als de gebruiker niet geldig is

### **get\_document\_content()**

Decodeert documentgegevens en retourneert deze als een string.

```python
document_content = get_document_content(doc)
if document_content:
    document_content = document_content.lower()
```

#### Parameters:

<table><thead><tr><th width="173">Naam</th><th width="176">Type</th><th>Beschrijving</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>De documentgegevens met veldinformatie</td></tr></tbody></table>

#### Retourneert:

* Documentgegevens als een string.

### **update\_document\_status\_with\_doc\_id()**

Werk de status van een document met een specifieke ID bij naar de gegeven status.

```python
genehmigung_user_1 = get_field_value(document_data, 'genehmigung_user_1', None)

if genehmigung_user_1 != "LEER":
    update_document_status_with_doc_id(document_json['doc_id'], user, document_json['org_id'], "validated_pending_approval")
```

#### Parameters:

<table><thead><tr><th width="228">Naam</th><th width="216">Type</th><th>Beschrijving</th></tr></thead><tbody><tr><td>doc_id<mark style="color:red;">*</mark></td><td><code>string</code></td><td>De ID van het document dat moet worden bijgewerkt</td></tr><tr><td>user<mark style="color:red;">*</mark></td><td>of <code>user ID</code> of <code>UserAuthentication</code> object</td><td>De gebruiker die de update uitvoert</td></tr><tr><td>org_id<mark style="color:red;">*</mark></td><td><code>string</code></td><td>De ID van de organisatie waartoe het document behoort</td></tr><tr><td>status<mark style="color:red;">*</mark></td><td><code>string</code></td><td>De nieuwe status van het document</td></tr><tr><td>message (optioneel)</td><td><code>string</code></td><td>Optioneel bericht dat aan de statusupdate is gekoppeld<br>Standaard is <code>None</code></td></tr><tr><td>doc_classification_class (optioneel)</td><td><code>string</code></td><td>Optionele documentclassificatieklasse<br>Standaard is <code>None</code></td></tr></tbody></table>

### **get\_lov\_values()**

Haalt de LOV-waarden op van een specifieke org\_id en sleutel.

```python
reverse_charge_to_check = get_lov_values(org_id, 'Kosten', return_type="list_of_values")
```

#### Parameters:

<table><thead><tr><th width="173">Naam</th><th width="176">Type</th><th>Beschrijving</th></tr></thead><tbody><tr><td>org_id<mark style="color:red;">*</mark></td><td><code>string</code></td><td>De ID van de organisatie waartoe het document behoort</td></tr><tr><td>key<mark style="color:red;">*</mark></td><td><code>string</code></td><td>De sleutel van de vereiste Lijst Van Waarden</td></tr><tr><td>return_type (optioneel)</td><td><code>string</code></td><td>Het type waarin de gegevens moeten worden geretourneerd<br>Standaard is <code>'list_of_objects'</code></td></tr><tr><td>sub_org_id (optioneel)</td><td><code>string</code></td><td>Optionele sub-organisatie-ID voor filtering<br>Standaard is <code>None</code></td></tr><tr><td>language_code<br>(optioneel)</td><td><code>string</code></td><td>Deze parameter stelt de taal in waarin de waarden worden geretourneerd. Het accepteert taalcodes, zoals "en" voor Engels of "fr" voor Frans.<br>Standaard is <code>""</code></td></tr></tbody></table>

#### Retourneert:

* LOV-waarden als een lijst van objecten of als een lijst.

### **format\_decimal\_to\_locale()**

Formatteert een decimale waarde naar en\_US.UTF-8 formaat.

```python
standard_value = "{0:.2f}".format(total)
formatted_value = format_decimal_to_locale(
    standard_value, document_json['amount_format_locale']
)
```

#### Parameters:

<table><thead><tr><th width="208">Naam</th><th width="187">Type</th><th>Beschrijving</th></tr></thead><tbody><tr><td>value<mark style="color:red;">*</mark></td><td><code>float, decimal.Decimal, str</code></td><td>De waarde die moet worden geformatteerd.</td></tr><tr><td>to_locale (optioneel)</td><td><code>string</code></td><td>Het type waarin de gegevens moeten worden geretourneerd<br>Standaard is <code>'en_US.UTF-8'</code></td></tr><tr><td>max_decimal_places (optioneel)</td><td><code>int</code></td><td>Optionele sub-organisatie-ID voor filtering<br>Standaard is <code>4</code></td></tr><tr><td>min_decimal_places (optioneel)</td><td><code>int</code></td><td>Het minimum aantal decimalen dat moet worden overwogen<br>Standaard is <code>2</code></td></tr></tbody></table>

* value: De waarde die moet worden geformatteerd.
* to\_locale (optioneel): Het formaat waarin de waarde wordt omgevormd.
* max\_decimal\_places (optioneel): Het maximum aantal decimalen dat moet worden overwogen.
* min\_decimal\_places (optioneel): Het minimum aantal decimalen dat moet worden overwogen.

#### Retourneert:

* De geformatteerde waarde.

### **compare\_values()**

Vergelijkt twee waarden op gelijkheid, met verschillende datatypes.

```python
result = compare_values(10, "10")
```

#### Parameters:

<table><thead><tr><th width="173">Naam</th><th width="176">Type</th><th>Beschrijving</th></tr></thead><tbody><tr><td>value1<mark style="color:red;">*</mark></td><td><code>any</code></td><td>De eerste waarde om te vergelijken</td></tr><tr><td>value2<mark style="color:red;">*</mark></td><td><code>any</code></td><td>De tweede waarde om te vergelijken</td></tr></tbody></table>

#### Retourneert:

* True als de waarden gelijk zijn en False als ze verschillen

### **create\_document\_task()**

Maakt een taak, wijst deze toe aan een gebruiker of groep, stelt prioriteit in en verstuurt optioneel een e-mail.

```python
if not is_task_created:
            create_document_task(user, document_data, "Herkunftsland außerhalb der EU", "Die Gelangensbestätigung kommt von einem Land außerhalb der EU. Bitte das MRN-Dokument anhängen.", "high", 1007, None, False)
            document_data["document_json"]["country_check_task_created"] = True
```

#### Parameters:

<table><thead><tr><th width="216">Naam</th><th width="217">Type</th><th>Beschrijving</th></tr></thead><tbody><tr><td>user<mark style="color:red;">*</mark></td><td>of <code>user ID</code> of <code>UserAuthentication</code> object</td><td>De gebruiker die de update uitvoert</td></tr><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>De documentgegevens met veldinformatie</td></tr><tr><td>title<mark style="color:red;">*</mark></td><td><code>string</code></td><td>De titel van de taak</td></tr><tr><td>description<mark style="color:red;">*</mark></td><td><code>string</code></td><td>De beschrijving van de taak</td></tr><tr><td>priority<mark style="color:red;">*</mark></td><td><code>string</code></td><td>De prioriteit van de taak</td></tr><tr><td>assigned_to_user_id<mark style="color:red;">*</mark></td><td><code>int</code></td><td>De id van de gebruiker aan wie de taak moet worden toegewezen</td></tr><tr><td>assigned_to_group_id<mark style="color:red;">*</mark></td><td><code>int</code></td><td>De id van de groep aan wie de taak moet worden toegewezen</td></tr><tr><td>send_email<mark style="color:red;">*</mark></td><td><code>bool</code></td><td>Bepaal of er een e-mail moet worden verzonden of niet</td></tr></tbody></table>

#### Retourneert:

* Dict dat aangeeft of het proces succesvol was of niet

### **set\_document\_sub\_org\_id()**

Stelt de sub\_org\_id van de opgegeven document\_data in.

```python
if sub_org_id != current_sub_org_id:
    document_data["document_json"]["sub_org_id4"] = sub_org_id
    set_document_sub_org_id(document_data, sub_org_id)
```

#### Parameters:

<table><thead><tr><th width="173">Naam</th><th width="176">Type</th><th>Beschrijving</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>De documentgegevens met veldinformatie</td></tr><tr><td>sub_org_id<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Optionele sub-organisatie-ID voor filtering</td></tr></tbody></table>

### **get\_user\_by\_id()**

Haalt de gebruiker op met de bijbehorende gebruikers-ID.

```python
requester_mail = str(get_user_by_id(str(requester)).email.lower())
```

#### Parameters:

<table><thead><tr><th width="173">Naam</th><th width="176">Type</th><th>Beschrijving</th></tr></thead><tbody><tr><td>user_id<mark style="color:red;">*</mark></td><td><code>string</code></td><td>De ID van de gebruiker</td></tr></tbody></table>

#### Retourneert:

* De gebruiker met de bijbehorende gebruikers-ID

### **get\_group\_by\_id()**

Haalt de groep op met de bijbehorende groeps-ID.

```python
group_name  = str(get_group_by_id(assigned_to_group_id))
```

#### Parameters:

<table><thead><tr><th width="173">Naam</th><th width="176">Type</th><th>Beschrijving</th></tr></thead><tbody><tr><td>group_id<mark style="color:red;">*</mark></td><td><code>string</code></td><td>De ID van de groep</td></tr></tbody></table>

#### Retourneert:

* De groep met de bijbehorende groeps-ID

### **get\_user\_by\_email()**

Haalt de gebruiker op met de bijbehorende e-mail.

```python
user_name = str(get_user_by_email(email)
```

#### Parameters:

<table><thead><tr><th width="173">Naam</th><th width="176">Type</th><th>Beschrijving</th></tr></thead><tbody><tr><td>email<mark style="color:red;">*</mark></td><td><code>any</code></td><td>De e-mail van de gebruiker</td></tr></tbody></table>

#### Retourneert:

* De gebruiker met de bijbehorende e-mail

### **add\_table\_column()**

Voegt een kolom toe aan de opgegeven tabel.

```python
table = tables_dict.get("ORDER_CONFIRMATION_TABLE")

if table:
    add_table_column(table, "PROMISED_DELIVERY_DATE")
```

#### Parameters:

<table><thead><tr><th width="173">Naam</th><th width="176">Type</th><th>Beschrijving</th></tr></thead><tbody><tr><td>table<mark style="color:red;">*</mark></td><td><code>string</code></td><td>De tabel waar de kolom aan moet worden toegevoegd</td></tr><tr><td>col_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>De naam van de kolom</td></tr><tr><td>default_value (optioneel)</td><td><code>any</code></td><td><p>De initiële waarde voor het veld</p><p>Standaard is <code>None</code></p></td></tr></tbody></table>

### **get\_column\_value()**

Haalt de waarde op van een opgegeven kolom.

```python
for row in table['rows']:
        unit = get_column_value(row, "UNIT")
```

#### Parameters:

<table><thead><tr><th width="173">Naam</th><th width="176">Type</th><th>Beschrijving</th></tr></thead><tbody><tr><td>row<mark style="color:red;">*</mark></td><td><code>string</code></td><td>De rij waar de waarde zich bevindt</td></tr><tr><td>col_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>De naam van de kolom</td></tr><tr><td>default_value (optioneel)</td><td><code>any</code></td><td>De initiële waarde voor het veld<br>Standaard is <code>None</code></td></tr><tr><td>is_clean (optioneel)</td><td><code>bool</code></td><td>Converteert de waarde naar hoofdletters en verwijdert extra spaties<br>Standaard is <code>False</code></td></tr></tbody></table>

#### Retourneert

* Retourneert de waarde van de opgegeven kolom als deze bestaat; anders retourneert het `None`

### **set\_column\_value()**

Stelt de waarde van de opgegeven kolom in. Als de kolom niet bestaat, wordt deze aangemaakt.

```python
supplier_id = get_field_value(document_data, "supplier_id", "")

quote_table = tables_dict["QUOTE_TABLE"]

for row in quote_table.get('rows', []):
    set_column_value(row,"SUPPLIER_ID", supplier_id)
```

#### Parameters:

<table><thead><tr><th width="173">Naam</th><th width="176">Type</th><th>Beschrijving</th></tr></thead><tbody><tr><td>row<mark style="color:red;">*</mark></td><td><code>string</code></td><td>De rij waar de waarde zich bevindt</td></tr><tr><td>col_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>De naam van de kolom</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>any</code></td><td>De waarde die op de opgegeven locatie moet worden ingesteld</td></tr></tbody></table>

#### Retourneert:

* True als de wijziging succesvol was

### **set\_column\_date\_value()**

Stelt de datumwaarde van een opgegeven kolom in.

```python
set_column_date_value(document_data, row, "DELIVERY_DATE", "2020-12-31", add_days=2)
```

#### Parameters:

<table><thead><tr><th width="173">Naam</th><th width="196.05859375">Type</th><th>Beschrijving</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>De documentgegevens met veldinformatie</td></tr><tr><td>row<mark style="color:red;">*</mark></td><td><code>string</code></td><td>De rij waar de waarde zich bevindt</td></tr><tr><td>col_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>De naam van de kolom</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>string</code></td><td>De datumwaarde die in ISO-formaat moet worden ingesteld (bijv. "2020-12-31")</td></tr><tr><td>add_days (optioneel)</td><td><code>int</code></td><td>Voeg extra dagen toe aan de gegeven datum<br>Standaard is <code>2</code></td></tr><tr><td>skip_weekend (optioneel)</td><td><code>bool</code></td><td>Overslaat de datum als deze in het weekend valt<br>Standaard is <code>False</code></td></tr><tr><td>exclude_final_days<br>(optioneel)</td><td>of <code>string</code> of <code>int</code></td><td>Geeft de dagen op die moeten worden uitgesloten (0-6 of zondag tot zaterdag)</td></tr></tbody></table>

### **set\_column\_amount\_value()**

* Converteer waarde naar string en stel de waarde voor de kolom in
* Stel de kolominhoud in op de waarde
* Formatteer waarde volgens de locale

```python
quantity = float(quantity) / 1000
set_column_amount_value(document_data, row, "QUANTITY", str(quantity))
```

#### Parameters:

<table><thead><tr><th width="173">Naam</th><th width="176">Type</th><th>Beschrijving</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>De documentgegevens met veldinformatie</td></tr><tr><td>row<mark style="color:red;">*</mark></td><td><code>string</code></td><td>De rij waar de waarde zich bevindt</td></tr><tr><td>column_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>De naam van de kolom</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>string</code></td><td>De waarde die voor het veld moet worden ingesteld (geef een nummer als string door, bijv. "123456")</td></tr></tbody></table>

### **delete\_tables()**

Deze functie verwijdert de tabellen uit de documentgegevens.

```python
delete_tables(document_data)
```

#### Parameters:

<table><thead><tr><th width="173">Naam</th><th width="176">Type</th><th>Beschrijving</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>De documentgegevens met veldinformatie</td></tr></tbody></table>

### **restore\_tables()**

Deze functie herstelt de tabellen in de documentgegevens.

```python
restore_tables(document_data)
```

#### Parameters:

<table><thead><tr><th width="173">Naam</th><th width="176">Type</th><th>Beschrijving</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>De documentgegevens met veldinformatie</td></tr></tbody></table>

### **remove\_rows\_from\_table()**

Verwijdert rijen uit de opgegeven tabel.

```python
count = 1
start = 1
remove_rows_from_table(document_data,"INVOICE_TABLE",count,start) 
```

#### Parameters:

<table><thead><tr><th width="173">Naam</th><th width="176">Type</th><th>Beschrijving</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>De documentgegevens met veldinformatie</td></tr><tr><td>table_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>De naam van de tabel</td></tr><tr><td>count<mark style="color:red;">*</mark></td><td><code>int</code></td><td>Hoeveel lijnen moeten worden verwijderd</td></tr><tr><td>start<mark style="color:red;">*</mark></td><td><code>int</code></td><td>Het startpunt</td></tr></tbody></table>

### **remove\_all\_rows\_except\_one\_from\_table()**

Verwijdert alle rijen behalve één uit de opgegeven tabel

```python
count = 1
start = 1
remove_rows_from_table(document_data,"INVOICE_TABLE",count,start) 
```

#### Parameters:

<table><thead><tr><th width="173">Naam</th><th width="176">Type</th><th>Beschrijving</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>De documentgegevens met veldinformatie</td></tr><tr><td>line_number<mark style="color:red;">*</mark></td><td><code>int</code></td><td>Het nummer van de regel die niet moet worden verwijderd</td></tr></tbody></table>

## Python Ingebouwde Functies

Je kunt ook enkele van de ingebouwde Python-functies gebruiken:

* abs(): Retourneert de absolute waarde van een getal.
* len(): Retourneert de lengte (aantal items) van een object, zoals een lijst of string.
* isinstance(): Controleert of een object een instantie is van een bepaalde klasse of type.
* print(): Drukt output af naar de console.
* round(): Rondt een drijvend getal af naar een opgegeven aantal decimalen.
* str\_to\_bool(): Converteert een string naar een boolean waarde (True of False).
* type(): Retourneert het type van een object.
* dict(): Maakt een woordenboekobject aan.
* list(): Maakt een lijstobject aan.
* str(): Converteert een waarde naar een string.
* float(): Converteert een waarde naar een drijvend getal.
* int(): Converteert een waarde naar een geheel getal.

Voor meer details, bezoek de officiële Python-documentatie: [Ingebouwde Functies](https://docs.python.org/3.12/library/functions.html).

## String Klasse Functies

Je kunt ook deze functies specifiek voor het werken met strings gebruiken:

* lower(): Converteert alle karakters in een string naar kleine letters.
* upper(): Converteert alle karakters in een string naar hoofdletters.
* split(): Splitst een string in een lijst op basis van een scheidingsteken (bijv. spatie of komma).
* startswith(): Controleert of een string begint met een opgegeven voorvoegsel.
* endswith(): Controleert of een string eindigt met een opgegeven achtervoegsel.
* strip(): Verwijdert eventuele leidende of achterblijvende spaties uit een string.

## Functies uit de Python Wiskunde Module

Deze functies maken deel uit van de wiskundemodule en zijn nuttig voor wiskundige bewerkingen:

* floor(): Retourneert het grootste gehele getal dat kleiner is dan of gelijk is aan een gegeven getal.
* ceil(): Retourneert het kleinste gehele getal dat groter is dan of gelijk is aan een gegeven getal.

Voor meer informatie, bekijk de officiële Python-documentatie: [Wiskunde Module Functies](https://docs.python.org/3/library/math.html).

## Reguliere Expressie Functie

* re.search(): Zoekt naar een patroon binnen een string en retourneert de eerste match.

Zie meer details hier: [re.search Documentatie](https://docs.python.org/3/library/re.html#re.search).

## Externe Functies

Hier zijn enkele nuttige functies van externe bibliotheken:

* deepcopy(): Maakt een kopie van een object, inclusief geneste objecten (van de copy-module).\
  [Deepcopy Documentatie](https://docs.python.org/3/library/copy.html#copy.deepcopy).
* levenshtein\_distance(): Berekent het aantal bewerkingen (invoegingen, verwijderingen, vervangingen) dat nodig is om de ene string in de andere te veranderen. Deze functie is beschikbaar in de [Jellyfish bibliotheek](https://jamesturk.github.io/jellyfish/functions/).

## Datum en Tijd Functies

Je kunt de volgende functies gebruiken voor het werken met data en tijden:

* strptime(): Converteert een string naar een datetime-object op basis van een opgegeven formaat.
* strftime(): Formatteert een datetime-object naar een string op basis van een opgegeven formaat.

Voor meer informatie, bekijk de officiële documentatie:\
[Datum en Tijd Functies](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior).
