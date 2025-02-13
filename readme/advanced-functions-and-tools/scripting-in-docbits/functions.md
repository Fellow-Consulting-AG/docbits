# Funkcje

## **Dokumentacja funkcjonalna**

Ten moduł zawiera funkcje do manipulacji danymi dokumentów oraz wykonywania różnych operacji związanych z polami dokumentów.

## **Funkcje**

### **set\_field\_value()**

Ustawia wartość pola w danych dokumentu.

```python
po_number = get_field_value(fields_dict, 'purchase_order', None)
if not po_number:
    po_number = ''
    
if po_number:
    set_field_value(fields_dict, "invoice_sub_type", 'Purchase Invoice')
else:
    set_field_value(fields_dict, "invoice_sub_type", 'Cost Invoice')
```

#### Parametry:

<table><thead><tr><th width="177">Nazwa</th><th width="176">Typ</th><th>Opis</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Dane dokumentu zawierające informacje o polach</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Nazwa pola do ustawienia</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>any</code></td><td>Wartość do ustawienia dla pola</td></tr></tbody></table>

### **set\_date\_value()**

Ustawia wartość pola daty w danych dokumentu.

```python
invoice_date = get_field_value(document_data, 'invoice_date', None)
    
if not document_json.get("script_executed", False):
    if invoice_date:
        set_date_value(document_data, "accounting_date", invoice_date)
        document_json["script_executed"] = True
```

#### Parametry:

<table><thead><tr><th width="229">Nazwa</th><th width="138">Typ</th><th>Opis</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Dane dokumentu zawierające informacje o polach</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Nazwa pola do ustawienia</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Wartość daty do ustawienia w formacie ISO (np. "2020-12-31").</td></tr><tr><td>add_days (opcjonalnie)</td><td><code>int</code></td><td>Dodaje dodatkowe dni do podanej daty<br>Domyślnie 0</td></tr><tr><td>skip_weekend (opcjonalnie)</td><td><code>bool</code></td><td>Pomija datę, jeśli przypada na weekend<br>Domyślnie <code>False</code></td></tr></tbody></table>

### **set\_amount\_value()**

Ustawia wartość pola kwoty w danych dokumentu.

```python
total_amount = get_field_value(document_data, "net_amount")
lines_total = 0.0
set_amount_value(document_data, "net_amount",str(lines_total))
```

#### Parametry:

<table><thead><tr><th width="173">Nazwa</th><th width="176">Typ</th><th>Opis</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Dane dokumentu zawierające informacje o polach</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Nazwa pola do ustawienia</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Wartość do ustawienia dla pola (przekaż liczbę jako string np. "123456"</td></tr></tbody></table>

### **get\_field\_value()**

Pobiera wartość pola z danych dokumentu.

```python
total_amount = get_field_value(document_data, "net_amount")
lines_total = 0.0
set_amount_value(document_data, "net_amount", str(lines_total))
```

#### Parametry:

<table><thead><tr><th width="191">Nazwa</th><th width="176">Typ</th><th>Opis</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Dane dokumentu zawierające informacje o polach</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Nazwa pola do ustawienia</td></tr><tr><td>default_value (opcjonalnie)</td><td><code>any</code></td><td>Zwraca default_value, jeśli nie znaleziono wartości pola<br>Domyślnie <code>None</code></td></tr><tr><td>is_clean (opcjonalnie)</td><td><code>bool</code></td><td>Konwertuje wartość na wielkie litery i usuwa dodatkowe spacje<br>Domyślnie <code>False</code></td></tr></tbody></table>

#### Zwraca:

* Wartość określonego pola

### **create\_new\_field()**

Tworzy nowe pole o określonej nazwie i wartości.

```python
currency = get_field_value(document_data, 'currency', None)

if not currency:
    if 'currency' not in fields_dict:
        new_field = create_new_field('currency','')
        fields_dict['currency'] = new_field
        document_json['fields'].append(new_field)
    set_field_value(document_data, "currency", "USD")
```

#### Parametry:

<table><thead><tr><th width="140">Nazwa</th><th width="133">Typ</th><th>Opis</th></tr></thead><tbody><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>str</code></td><td>Dane dokumentu zawierające informacje o polach</td></tr><tr><td>value (opcjonalnie)</td><td><code>any</code></td><td>Początkowa wartość dla pola<br>Domyślnie <code>""</code></td></tr></tbody></table>

#### Zwraca:

* Słownik nowo utworzonego pola

### **delete\_field()**

Usuwa pole z danych dokumentu.

```python
field_amount = get_field_value(document_data, field_name)
    if not field_amount:
        delete_field(document_data, fields_dict, field_name)
    else:
        field_amount = float(field_amount)
        if field_amount == 0:
            delete_field(document_data, fields_dict, field_name)
```

#### Parametry:

<table><thead><tr><th width="173">Nazwa</th><th width="176">Typ</th><th>Opis</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Dane dokumentu zawierające informacje o polach</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Nazwa pola do usunięcia</td></tr></tbody></table>

#### Zwraca:

* Document\_data jako json i jako dict po usunięciu pola

### **set\_is\_required()**

Ustawia atrybut 'is\_required' pola w danych dokumentu.

```python
net_amount = get_field_value(document_data, "net_amount", None)
if net_amount:
    set_is_required(document_data, "tax_country", True)
    set_is_required(document_data, "tax_code_without_country", True)
```

#### Parametry:

<table><thead><tr><th width="173">Nazwa</th><th width="176">Typ</th><th>Opis</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Dane dokumentu zawierające informacje o polach</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Nazwa pola do ustawienia</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>bool</code></td><td>Wartość do ustawienia dla pola</td></tr></tbody></table>

### **set\_force\_validation()**

Ustawia atrybut 'force\_validation' pola w danych dokumentu.

```python
if supplier_id in supplier_to_check:
    set_force_validation(document_data, 'purchase_order', True, reset_validation=reset_validation)
```

#### Parametry:

<table><thead><tr><th width="173">Nazwa</th><th width="176">Typ</th><th>Opis</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Dane dokumentu zawierające informacje o polach</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Nazwa pola do ustawienia</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>bool</code></td><td>Wartość do ustawienia dla pola</td></tr><tr><td>reset_validation (opcjonalnie)</td><td><code>bool</code></td><td>Ustawia atrybut "is_validated" na określoną wartość<br>Domyślnie <code>False</code></td></tr></tbody></table>

### **set\_field\_as\_invalid()**

Oznacza pole na ekranie walidacji jako nieważne i podświetla je.

```python
if not document_date:
    set_field_as_invalid(document_data, "document_date", "Es ist kein Datum vorhanden", "INVALID_VALUE")
```

#### Parametry:

<table><thead><tr><th width="173">Nazwa</th><th width="176">Typ</th><th>Opis</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Dane dokumentu zawierające informacje o polach</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Nazwa pola do oznaczenia jako nieważne</td></tr><tr><td>message<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Wiadomość walidacyjna dla pola</td></tr><tr><td>code (opcjonalnie)</td><td><code>string</code></td><td><p>Kod błędu dla walidacji</p><p>Domyślnie <code>None</code></p></td></tr></tbody></table>

### **set\_field\_attribute()**

Ustawia niestandardowy atrybut pola w danych dokumentu.

```python
if purchase_order:
    if po_supplier_id != invoice_supplier_id:
        set_field_as_invalid(document_data, "supplier_name", "Supplier is different from PO supplier")
    else:
        set_field_attribute(document_data, "supplier_name", "is_valid", True)
        set_field_attribute(document_data, "supplier_name", "validation_message","")
```

#### Parametry:

<table><thead><tr><th width="173">Nazwa</th><th width="176">Typ</th><th>Opis</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Dane dokumentu zawierające informacje o polach</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Nazwa pola do ustawienia</td></tr><tr><td>attribute_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Nazwa atrybutu do ustawienia</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>any</code></td><td>Wartość do ustawienia dla atrybutu</td></tr></tbody></table>

### **is\_supplier\_valid()**

Sprawdza, czy dostawca jest ważny na podstawie podanych kryteriów.

```python
bool = is_supplier_valid(user, {"name": "Supplier Inc."})
```

#### Parametry:

<table><thead><tr><th width="203">Nazwa</th><th width="216">Typ</th><th>Opis</th></tr></thead><tbody><tr><td>user<mark style="color:red;">*</mark></td><td><code>UserAuthentication</code></td><td>Użytkownik uwierzytelniony</td></tr><tr><td>filter_data_json<mark style="color:red;">*</mark></td><td><code>json</code></td><td>Kryteria filtrowania do walidacji dostawcy</td></tr><tr><td>sub_org_id (opcjonalnie)</td><td><code>string</code></td><td>Opcjonalny identyfikator podorganizacji do filtrowania<br>Domyślnie <code>None</code></td></tr></tbody></table>

#### Zwraca:

* True, jeśli użytkownik jest ważny
* False, jeśli użytkownik nie jest ważny

### **get\_document\_content()**

Dekoduje dane dokumentu i zwraca je jako string.

```python
document_content = get_document_content(doc)
if document_content:
    document_content = document_content.lower()
```

#### Parametry:

<table><thead><tr><th width="173">Nazwa</th><th width="176">Typ</th><th>Opis</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Dane dokumentu zawierające informacje o polach</td></tr></tbody></table>

#### Zwraca:

* Dane dokumentu jako string.

### **update\_document\_status\_with\_doc\_id()**

Aktualizuje status dokumentu o określonym ID na dany status.

```python
genehmigung_user_1 = get_field_value(document_data, 'genehmigung_user_1', None)

if genehmigung_user_1 != "LEER":
    update_document_status_with_doc_id(document_json['doc_id'], user, document_json['org_id'], "validated_pending_approval")
```

#### Parametry:

<table><thead><tr><th width="228">Nazwa</th><th width="216">Typ</th><th>Opis</th></tr></thead><tbody><tr><td>doc_id<mark style="color:red;">*</mark></td><td><code>string</code></td><td>ID dokumentu do aktualizacji</td></tr><tr><td>user<mark style="color:red;">*</mark></td><td>albo <code>user ID</code> albo <code>UserAuthentication</code> obiekt</td><td>Użytkownik wykonujący aktualizację</td></tr><tr><td>org_id<mark style="color:red;">*</mark></td><td><code>string</code></td><td>ID organizacji, do której należy dokument</td></tr><tr><td>status<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Nowy status dokumentu</td></tr><tr><td>message (opcjonalnie)</td><td><code>string</code></td><td>Opcjonalna wiadomość związana z aktualizacją statusu<br>Domyślnie <code>None</code></td></tr><tr><td>doc_classification_class (opcjonalnie)</td><td><code>string</code></td><td>Opcjonalna klasa klasyfikacji dokumentu<br>Domyślnie <code>None</code></td></tr></tbody></table>

### **get\_lov\_values()**

Pobiera wartości LOV z określonego org\_id i klucza.

```python
reverse_charge_to_check = get_lov_values(org_id, 'Kosten', return_type="list_of_values")
```

#### Parametry:

<table><thead><tr><th width="173">Nazwa</th><th width="176">Typ</th><th>Opis</th></tr></thead><tbody><tr><td>org_id<mark style="color:red;">*</mark></td><td><code>string</code></td><td>ID organizacji, do której należy dokument</td></tr><tr><td>key<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Klucz wymaganej Listy Wartości</td></tr><tr><td>return_type (opcjonalnie)</td><td><code>string</code></td><td>Typ, w jakim dane powinny być zwrócone<br>Domyślnie <code>'list_of_objects'</code></td></tr><tr><td>sub_org_id (opcjonalnie)</td><td><code>string</code></td><td>Opcjonalny identyfikator podorganizacji do filtrowania<br>Domyślnie <code>None</code></td></tr></tbody></table>

#### Zwraca:

* Wartości LOV jako lista obiektów lub jako lista.

### **format\_decimal\_to\_locale()**

Formatuje wartość dziesiętną do formatu en\_US.UTF-8.

```python
standard_value = "{0:.2f}".format(total)
formatted_value = format_decimal_to_locale(
    standard_value, document_json['amount_format_locale']
)
```

#### Parametry:

<table><thead><tr><th width="208">Nazwa</th><th width="187">Typ</th><th>Opis</th></tr></thead><tbody><tr><td>value<mark style="color:red;">*</mark></td><td><code>float, decimal.Decimal, str</code></td><td>Wartość, która powinna być sformatowana.</td></tr><tr><td>to_locale (opcjonalnie)</td><td><code>string</code></td><td>Typ, w jakim dane powinny być zwrócone<br>Domyślnie <code>'en_US.UTF-8'</code></td></tr><tr><td>max_decimal_places (opcjonalnie)</td><td><code>int</code></td><td>Opcjonalny identyfikator podorganizacji do filtrowania<br>Domyślnie <code>4</code></td></tr><tr><td>min_decimal_places (opcjonalnie)</td><td><code>int</code></td><td>Minimalna liczba miejsc dziesiętnych, które powinny być brane pod uwagę<br>Domyślnie <code>2</code></td></tr></tbody></table>

* value: Wartość, która powinna być sformatowana.
* to\_locale (opcjonalnie): Format, w jakim wartość jest przekształcana.
* max\_decimal\_places (opcjonalnie): Maksymalna liczba miejsc dziesiętnych, które powinny być brane pod uwagę.
* min\_decimal\_places (opcjonalnie): Minimalna liczba miejsc dziesiętnych, które powinny być brane pod uwagę.

#### Zwraca:

* Sformatowana wartość.

### **compare\_values()**

Porównuje dwie wartości pod kątem równości, obsługując różne typy danych.

```python
result = compare_values(10, "10")
```

#### Parametry:

<table><thead><tr><th width="173">Nazwa</th><th width="176">Typ</th><th>Opis</th></tr></thead><tbody><tr><td>value1<mark style="color:red;">*</mark></td><td><code>any</code></td><td>Pierwsza wartość do porównania</td></tr><tr><td>value2<mark style="color:red;">*</mark></td><td><code>any</code></td><td>Druga wartość do porównania</td></tr></tbody></table>

#### Zwraca:

* True, jeśli wartości są równe, i False, jeśli się różnią

### **create\_document\_task()**

Tworzy zadanie, przypisuje je do użytkownika lub grupy, ustawia priorytet i opcjonalnie wysyła e-mail.

```python
if not is_task_created:
            create_document_task(user, document_data, "Herkunftsland außerhalb der EU", "Die Gelangensbestätigung kommt von einem Land außerhalb der EU. Bitte das MRN-Dokument anhängen.", "high", 1007, None, False)
            document_data["document_json"]["country_check_task_created"] = True
```

#### Parametry:

<table><thead><tr><th width="216">Nazwa</th><th width="217">Typ</th><th>Opis</th></tr></thead><tbody><tr><td>user<mark style="color:red;">*</mark></td><td>albo <code>user ID</code> albo <code>UserAuthentication</code> obiekt</td><td>Użytkownik wykonujący aktualizację</td></tr><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Dane dokumentu zawierające informacje o polach</td></tr><tr><td>title<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Tytuł zadania</td></tr><tr><td>description<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Opis zadania</td></tr><tr><td>priority<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Priorytet zadania</td></tr><tr><td>assigned_to_user_id<mark style="color:red;">*</mark></td><td><code>int</code></td><td>ID użytkownika, do którego zadanie powinno być przypisane</td></tr><tr><td>assigned_to_group_id<mark style="color:red;">*</mark></td><td><code>int</code></td><td>ID grupy, do której zadanie powinno być przypisane</td></tr><tr><td>send_email<mark style="color:red;">*</mark></td><td><code>bool</code></td><td>Określa, czy e-mail powinien być wysłany, czy nie</td></tr></tbody></table>

#### Zwraca:

* Dict, który wskazuje, czy proces był udany, czy nie

### **set\_document\_sub\_org\_id()**

Ustawia sub\_org\_id w określonych document\_data.

```python
if sub_org_id != current_sub_org_id:
    document_data["document_json"]["sub_org_id4"] = sub_org_id
    set_document_sub_org_id(document_data, sub_org_id)
```

#### Parametry:

<table><thead><tr><th width="173">Nazwa</th><th width="176">Typ</th><th>Opis</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Dane dokumentu zawierające informacje o polach</td></tr><tr><td>sub_org_id<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Opcjonalny identyfikator podorganizacji do filtrowania</td></tr></tbody></table>

### **get\_user\_by\_id()**

Pobiera użytkownika o odpowiadającym identyfikatorze użytkownika.

```python
requester_mail = str(get_user_by_id(str(requester)).email.lower())
```

#### Parametry:

<table><thead><tr><th width="173">Nazwa</th><th width="176">Typ</th><th>Opis</th></tr></thead><tbody><tr><td>user_id<mark style="color:red;">*</mark></td><td><code>string</code></td><td>ID użytkownika</td></tr></tbody></table>

#### Zwraca:

* Użytkownika o odpowiadającym identyfikatorze użytkownika

### **get\_group\_by\_id()**

Pobiera grupę o odpowiadającym identyfikatorze grupy.

```python
group_name  = str(get_group_by_id(assigned_to_group_id))
```

Parametry:

<table><thead><tr><th width="173">Nazwa</th><th width="176">Typ</th><th>Opis</th></tr></thead><tbody><tr><td>group_id<mark style="color:red;">*</mark></td><td><code>string</code></td><td>ID grupy</td></tr></tbody></table>

#### Zwraca:

* Grupę o odpowiadającym identyfikatorze grupy

### **add\_table\_column()**

Dodaje kolumnę do określonej tabeli.

```python
table = tables_dict.get("ORDER_CONFIRMATION_TABLE")

if table:
    add_table_column(table, "PROMISED_DELIVERY_DATE")
```

Parametry:

<table><thead><tr><th width="173">Nazwa</th><th width="176">Typ</th><th>Opis</th></tr></thead><tbody><tr><td>table<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Tabela, do której powinna być dodana kolumna</td></tr><tr><td>col_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Nazwa kolumny</td></tr><tr><td>default_value (opcjonalnie)</td><td><code>any</code></td><td><p>Początkowa wartość dla pola</p><p>Domyślnie <code>None</code></p></td></tr></tbody></table>

### **get\_column\_value()**

Pobiera wartość określonej kolumny.

```python
for row in table['rows']:
        unit = get_column_value(row, "UNIT")
```

#### Parametry:

<table><thead><tr><th width="173">Nazwa</th><th width="176">Typ</th><th>Opis</th></tr></thead><tbody><tr><td>row<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Wiersz, w którym znajduje się wartość</td></tr><tr><td>col_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Nazwa kolumny</td></tr><tr><td>default_value (opcjonalnie)</td><td><code>any</code></td><td>Początkowa wartość dla pola<br>Domyślnie <code>None</code></td></tr><tr><td>is_clean (opcjonalnie)</td><td><code>bool</code></td><td>Konwertuje wartość na wielkie litery i usuwa dodatkowe spacje<br>Domyślnie <code>False</code></td></tr></tbody></table>

#### Zwraca

* Wartość określonej kolumny

### **set\_column\_value()**

Ustawia wartość określonej kolumny.

```python
supplier_id = get_field_value(document_data, "supplier_id", "")

quote_table = tables_dict["QUOTE_TABLE"]

for row in quote_table.get('rows', []):
    set_column_value(row,"SUPPLIER_ID", supplier_id)
```

#### Parametry:

<table><thead><tr><th width="173">Nazwa</th><th width="176">Typ</th><th>Opis</th></tr></thead><tbody><tr><td>row<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Wiersz, w którym znajduje się wartość</td></tr><tr><td>col_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Nazwa kolumny</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>any</code></td><td>Wartość, która zostanie ustawiona w określonym miejscu</td></tr></tbody></table>

#### Zwraca:

* True, jeśli zmiana była udana

### **set\_column\_date\_value()**

Ustawia wartość daty określonej kolumny.

```python
set_column_date_value(document_data, row, "DELIVERY_DATE", "2020-12-31", add_days=2)
```

#### Parametry:

<table><thead><tr><th width="173">Nazwa</th><th width="176">Typ</th><th>Opis</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Dane dokumentu zawierające informacje o polach</td></tr><tr><td>row<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Wiersz, w którym znajduje się wartość</td></tr><tr><td>col_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Nazwa kolumny</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Wartość daty do ustawienia w formacie ISO (np. "2020-12-31")</td></tr><tr><td>add_days (opcjonalnie)</td><td><code>int</code></td><td>Dodaje dodatkowe dni do podanej daty<br>Domyślnie <code>2</code></td></tr></tbody></table>

### **set\_column\_amount\_value()**

* Konwertuje wartość na string i ustawia wartość dla kolumny
* Ustawia zawartość kolumny na wartość
* Formatuje wartość zgodnie z lokalizacją

```python
quantity = float(quantity) / 1000
set_column_amount_value(document_data, row, "QUANTITY", str(quantity))
```

#### Parametry:

<table><thead><tr><th width="173">Nazwa</th><th width="176">Typ</th><th>Opis</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Dane dokumentu zawierające informacje o polach</td></tr><tr><td>row<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Wiersz, w którym znajduje się wartość</td></tr><tr><td>column_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Nazwa kolumny</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Wartość do ustawienia dla pola (przekaż liczbę jako string np. "123456")</td></tr></tbody></table>

### **remove\_rows\_from\_table()**

Usuwa wiersze z określonej tabeli.

```python
count = 1
start = 1
remove_rows_from_table(document_data,"INVOICE_TABLE",count,start) 
```

#### Parametry:

<table><thead><tr><th width="173">Nazwa</th><th width="176">Typ</th><th>Opis</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Dane dokumentu zawierające informacje o polach</td></tr><tr><td>table_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Nazwa tabeli</td></tr><tr><td>count<mark style="color:red;">*</mark></td><td><code>int</code></td><td>Ile wierszy powinno zostać usuniętych</td></tr><tr><td>start<mark style="color:red;">*</mark></td><td><code>int</code></td><td>Punkt początkowy</td></tr></tbody></table>

### **remove\_all\_rows\_except\_one\_from\_table()**

Usuwa wszystkie wiersze z wyjątkiem jednego z określonej tabeli.

```python
count = 1
start = 1
remove_rows_from_table(document_data,"INVOICE_TABLE",count,start) 
```

#### Parametry:

<table><thead><tr><th width="173">Nazwa</th><th width="176">Typ</th><th>Opis</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Dane dokumentu zawierające informacje o polach</td></tr><tr><td>line_number<mark style="color:red;">*</mark></td><td><code>int</code></td><td>Numer linii, która nie powinna zostać usunięta</td></tr></tbody></table>

## Wbudowane funkcje Pythona

Możesz również wykorzystać niektóre wbudowane funkcje Pythona:

* abs(): Zwraca wartość bezwzględną liczby.
* len(): Zwraca długość (liczbę elementów) obiektu, takiego jak lista lub string.
* isinstance(): Sprawdza, czy obiekt jest instancją określonej klasy lub typu.
* print(): Wypisuje wynik na konsoli.
* round(): Zaokrągla liczbę zmiennoprzecinkową do określonej liczby miejsc dziesiętnych.
* str\_to\_bool(): Konwertuje string na wartość boolean (True lub False).
* type(): Zwraca typ obiektu.
* dict(): Tworzy obiekt słownika.
* list(): Tworzy obiekt listy.
* str(): Konwertuje wartość na string.
* float(): Konwertuje wartość na liczbę zmiennoprzecinkową.
* int(): Konwertuje wartość na liczbę całkowitą.

Aby uzyskać więcej informacji, odwiedź oficjalną dokumentację Pythona: [Wbudowane funkcje](https://docs.python.org/3.12/library/functions.html).

## Funkcje klasy String

Możesz również używać tych funkcji specjalnie do pracy z stringami:

* lower(): Konwertuje wszystkie znaki w stringu na małe litery.
* upper(): Konwertuje wszystkie znaki w stringu na wielkie litery.
* split(): Dzieli string na listę na podstawie separatora (np. spacja lub przecinek).
* startswith(): Sprawdza, czy string zaczyna się od określonego prefiksu.
* endswith(): Sprawdza, czy string kończy się określonym sufiksem.
* strip(): Usuwa wszelkie wiodące lub końcowe białe znaki ze stringa.

## Funkcje z modułu matematycznego Pythona

Te funkcje są częścią modułu matematycznego i są przydatne do operacji matematycznych:

* floor(): Zwraca największą liczbę całkowitą mniejszą lub równą danej liczbie.
* ceil(): Zwraca najmniejszą liczbę całkowitą większą lub równą danej liczbie.

Aby uzyskać więcej informacji, sprawdź oficjalną dokumentację Pythona: [Funkcje modułu matematycznego](https://docs.python.org/3/library/math.html).

## Funkcja wyrażeń regularnych

* re.search(): Wyszukuje wzór w stringu i zwraca pierwsze dopasowanie.

Zobacz więcej szczegółów tutaj: [Dokumentacja re.search](https://docs.python.org/3/library/re.html#re.search).

## Funkcje zewnętrzne

Oto kilka przydatnych funkcji z zewnętrznych bibliotek:

* deepcopy(): Tworzy kopię obiektu, w tym zagnieżdżonych obiektów (z modułu copy).\
  [Dokumentacja Deepcopy](https://docs.python.org/3/library/copy.html#copy.deepcopy).
* levenshtein\_distance(): Oblicza liczbę edycji (wstawień, usunięć, substytucji) wymaganych do przekształcenia jednego stringa w inny. Ta funkcja jest dostępna w [bibliotece Jellyfish](https://jamesturk.github.io/jellyfish/functions/).

## Funkcje daty i czasu

Możesz używać następujących funkcji do pracy z datami i czasami:

* strptime(): Konwertuje string na obiekt datetime na podstawie określonego formatu.
* strftime(): Formatuje obiekt datetime na string na podstawie określonego formatu.

Aby uzyskać więcej informacji, sprawdź oficjalną dokumentację:\
[Funkcje daty i czasu](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior).
