# Funciones

## **Documentación Funcional**

Este módulo contiene funciones para manipular datos de documentos y realizar diversas operaciones relacionadas con los campos del documento.

## **Funciones**

### **set\_field\_value()**

Establece el valor de un campo en los datos del documento.

```python
po_number = get_field_value(fields_dict, 'purchase_order', None)
if not po_number:
    po_number = ''
    
if po_number:
    set_field_value(fields_dict, "invoice_sub_type", 'Purchase Invoice')
else:
    set_field_value(fields_dict, "invoice_sub_type", 'Cost Invoice')
```

#### Parámetros:

<table><thead><tr><th width="177">Nombre</th><th width="176">Tipo</th><th>Descripción</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Los datos del documento que contienen información del campo</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>El nombre del campo a establecer</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>any</code></td><td>El valor a establecer para el campo</td></tr><tr><td>remove_link (opcional)</td><td><code>bool</code></td><td>Eliminar la clave "coords" del campo.</td></tr></tbody></table>

### **set\_date\_value()**

Establece el valor de un campo de fecha en los datos del documento.

```python
invoice_date = get_field_value(document_data, 'invoice_date', None)
    
if not document_json.get("script_executed", False):
    if invoice_date:
        set_date_value(document_data, "accounting_date", invoice_date)
        document_json["script_executed"] = True
```

#### Parámetros:

<table><thead><tr><th width="229">Nombre</th><th width="196.0316162109375">Tipo</th><th>Descripción</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Los datos del documento que contienen información del campo</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>El nombre del campo a establecer</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>string</code></td><td>El valor de fecha a establecer en formato ISO (por ejemplo, "2020-12-31").</td></tr><tr><td>add_days (opcional)</td><td><code>int</code></td><td>Agregar días adicionales a la fecha dada<br>El valor predeterminado es 0</td></tr><tr><td>skip_weekend (opcional)</td><td><code>bool</code></td><td>Omitir la fecha si cae en fin de semana<br>El valor predeterminado es <code>False</code></td></tr><tr><td>remove link (opcional)</td><td><code>bool</code></td><td>Eliminar la clave "coords" del campo.</td></tr><tr><td>exclude_final_days<br>(opcional)</td><td>ya sea <code>string</code> o <code>int</code></td><td>Especifica los días a excluir (0-6 o domingo a sábado)</td></tr></tbody></table>

### **set\_amount\_value()**

Establece el valor de un campo de cantidad en los datos del documento.

```python
total_amount = get_field_value(document_data, "net_amount")
lines_total = 0.0
set_amount_value(document_data, "net_amount",str(lines_total))
```

#### Parámetros:

<table><thead><tr><th width="183.71087646484375">Nombre</th><th width="176">Tipo</th><th>Descripción</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Los datos del documento que contienen información del campo</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>El nombre del campo a establecer</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>string</code></td><td>El valor a establecer para el campo (pase un número como cadena, por ejemplo, "123456")</td></tr><tr><td>remove link (opcional)</td><td><code>bool</code></td><td>Eliminar la clave "coords" del campo.</td></tr></tbody></table>

### **get\_field\_value()**

Obtiene el valor de un campo de los datos del documento.

```python
total_amount = get_field_value(document_data, "net_amount")
lines_total = 0.0
set_amount_value(document_data, "net_amount", str(lines_total))
```

#### Parámetros:

<table><thead><tr><th width="191">Nombre</th><th width="176">Tipo</th><th>Descripción</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Los datos del documento que contienen información del campo</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>El nombre del campo a establecer</td></tr><tr><td>default_value (opcional)</td><td><code>any</code></td><td>Devuelve default_value si no se encuentra valor de campo<br>El valor predeterminado es <code>None</code></td></tr><tr><td>is_clean (opcional)</td><td><code>bool</code></td><td>Convierte el valor a mayúsculas y elimina espacios adicionales<br>El valor predeterminado es <code>False</code></td></tr></tbody></table>

#### Devuelve:

* Valor del campo especificado

### **create\_new\_field()**

Crea un nuevo campo con el nombre y valor especificados.

```python
currency = get_field_value(document_data, 'currency', None)

if not currency:
    if 'currency' not in fields_dict:
        new_field = create_new_field('currency','')
        fields_dict['currency'] = new_field
        document_json['fields'].append(new_field)
    set_field_value(document_data, "currency", "USD")
```

#### Parámetros:

<table><thead><tr><th width="140">Nombre</th><th width="133">Tipo</th><th>Descripción</th></tr></thead><tbody><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>str</code></td><td>Los datos del documento que contienen información del campo</td></tr><tr><td>value (opcional)</td><td><code>any</code></td><td>El valor inicial para el campo<br>El valor predeterminado es <code>""</code></td></tr></tbody></table>

#### Devuelve:

* Diccionario del nuevo campo creado

### **delete\_field()**

Elimina un campo de los datos del documento.

```python
field_amount = get_field_value(document_data, field_name)
    if not field_amount:
        delete_field(document_data, fields_dict, field_name)
    else:
        field_amount = float(field_amount)
        if field_amount == 0:
            delete_field(document_data, fields_dict, field_name)
```

#### Parámetros:

<table><thead><tr><th width="173">Nombre</th><th width="176">Tipo</th><th>Descripción</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Los datos del documento que contienen información del campo</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>El nombre del campo a eliminar</td></tr></tbody></table>

#### Devuelve:

* Document\_data como json y como dict después de que se eliminó el campo

### **set\_is\_required()**

Establece el atributo 'is\_required' de un campo en los datos del documento.

```python
net_amount = get_field_value(document_data, "net_amount", None)
if net_amount:
    set_is_required(document_data, "tax_country", True)
    set_is_required(document_data, "tax_code_without_country", True)
```

#### Parámetros:

<table><thead><tr><th width="173">Nombre</th><th width="176">Tipo</th><th>Descripción</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Los datos del documento que contienen información del campo</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>El nombre del campo a establecer</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>bool</code></td><td>El valor a establecer para el campo</td></tr></tbody></table>

### **set\_force\_validation()**

Establece el atributo 'force\_validation' de un campo en los datos del documento.

```python
if supplier_id in supplier_to_check:
    set_force_validation(document_data, 'purchase_order', True, reset_validation=reset_validation)
```

#### Parámetros:

<table><thead><tr><th width="173">Nombre</th><th width="176">Tipo</th><th>Descripción</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Los datos del documento que contienen información del campo</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>El nombre del campo a establecer</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>bool</code></td><td>El valor a establecer para el campo</td></tr><tr><td>reset_validation (opcional)</td><td><code>bool</code></td><td>Establece el atributo "is_validated" al valor especificado<br>El valor predeterminado es <code>False</code></td></tr></tbody></table>

### **set\_field\_as\_invalid()**

Marca un campo en la pantalla de validación como inválido y lo resalta.

```python
if not document_date:
    set_field_as_invalid(document_data, "document_date", "Es ist kein Datum vorhanden", "INVALID_VALUE")
```

#### Parámetros:

<table><thead><tr><th width="173">Nombre</th><th width="176">Tipo</th><th>Descripción</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Los datos del documento que contienen información del campo</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>El nombre del campo a marcar como inválido</td></tr><tr><td>message<mark style="color:red;">*</mark></td><td><code>string</code></td><td>El mensaje de validación para el campo</td></tr><tr><td>code (opcional)</td><td><code>string</code></td><td><p>Código de error para la validación</p><p>El valor predeterminado es <code>None</code></p></td></tr></tbody></table>

### **set\_field\_attribute()**

Establece un atributo personalizado de un campo en los datos del documento.

```python
if purchase_order:
    if po_supplier_id != invoice_supplier_id:
        set_field_as_invalid(document_data, "supplier_name", "Supplier is different from PO supplier")
    else:
        set_field_attribute(document_data, "supplier_name", "is_valid", True)
        set_field_attribute(document_data, "supplier_name", "validation_message","")
```

#### Parámetros:

<table><thead><tr><th width="173">Nombre</th><th width="176">Tipo</th><th>Descripción</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Los datos del documento que contienen información del campo</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>El nombre del campo a establecer</td></tr><tr><td>attribute_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>El nombre del atributo a establecer</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>any</code></td><td>El valor a establecer para el atributo</td></tr></tbody></table>

### **is\_supplier\_valid()**

Verifica si un proveedor es válido según los criterios proporcionados.

```python
bool = is_supplier_valid(user, {"name": "Supplier Inc."})
```

#### Parámetros:

<table><thead><tr><th width="203">Nombre</th><th width="216">Tipo</th><th>Descripción</th></tr></thead><tbody><tr><td>user<mark style="color:red;">*</mark></td><td><code>UserAuthentication</code></td><td>El usuario autenticado</td></tr><tr><td>filter_data_json<mark style="color:red;">*</mark></td><td><code>json</code></td><td>Criterios de filtrado para validar el proveedor</td></tr><tr><td>sub_org_id (opcional)</td><td><code>string</code></td><td>ID de suborganización opcional para filtrado<br>El valor predeterminado es <code>None</code></td></tr></tbody></table>

#### Devuelve:

* True, si el usuario es válido
* False si el usuario no es válido

### **get\_document\_content()**

Decodifica los datos del documento y los devuelve como una cadena.

```python
document_content = get_document_content(doc)
if document_content:
    document_content = document_content.lower()
```

#### Parámetros:

<table><thead><tr><th width="173">Nombre</th><th width="176">Tipo</th><th>Descripción</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Los datos del documento que contienen información del campo</td></tr></tbody></table>

#### Devuelve:

* Datos del documento como una cadena.

### **update\_document\_status\_with\_doc\_id()**

Actualiza el estado de un documento con un ID específico al estado dado.

```python
genehmigung_user_1 = get_field_value(document_data, 'genehmigung_user_1', None)

if genehmigung_user_1 != "LEER":
    update_document_status_with_doc_id(document_json['doc_id'], user, document_json['org_id'], "validated_pending_approval")
```

#### Parámetros:

<table><thead><tr><th width="228">Nombre</th><th width="216">Tipo</th><th>Descripción</th></tr></thead><tbody><tr><td>doc_id<mark style="color:red;">*</mark></td><td><code>string</code></td><td>El ID del documento a actualizar</td></tr><tr><td>user<mark style="color:red;">*</mark></td><td>ya sea <code>user ID</code> o <code>UserAuthentication</code> object</td><td>El usuario que realiza la actualización</td></tr><tr><td>org_id<mark style="color:red;">*</mark></td><td><code>string</code></td><td>El ID de la organización a la que pertenece el documento</td></tr><tr><td>status<mark style="color:red;">*</mark></td><td><code>string</code></td><td>El nuevo estado del documento</td></tr><tr><td>message (opcional)</td><td><code>string</code></td><td>Mensaje opcional asociado con la actualización de estado<br>El valor predeterminado es <code>None</code></td></tr><tr><td>doc_classification_class (opcional)</td><td><code>string</code></td><td>Clase de clasificación de documento opcional<br>El valor predeterminado es <code>None</code></td></tr></tbody></table>

### **get\_lov\_values()**

Obtiene los valores LOV de un org\_id y clave específicos.

```python
reverse_charge_to_check = get_lov_values(org_id, 'Kosten', return_type="list_of_values")
```

#### Parámetros:

<table><thead><tr><th width="173">Nombre</th><th width="176">Tipo</th><th>Descripción</th></tr></thead><tbody><tr><td>org_id<mark style="color:red;">*</mark></td><td><code>string</code></td><td>El ID de la organización a la que pertenece el documento</td></tr><tr><td>key<mark style="color:red;">*</mark></td><td><code>string</code></td><td>La clave de la Lista de Valores requerida</td></tr><tr><td>return_type (opcional)</td><td><code>string</code></td><td>El tipo en el que se deben devolver los datos<br>El valor predeterminado es <code>'list_of_objects'</code></td></tr><tr><td>sub_org_id (opcional)</td><td><code>string</code></td><td>ID de suborganización opcional para filtrado<br>El valor predeterminado es <code>None</code></td></tr><tr><td>language_code<br>(opcional)</td><td><code>string</code></td><td>Este parámetro establece el idioma en el que se devolverán los valores. Acepta códigos de idioma, como "en" para inglés o "fr" para francés.<br>El valor predeterminado es <code>""</code></td></tr></tbody></table>

#### Devuelve:

* Valores LOV como una lista de objetos o como una lista.

### **format\_decimal\_to\_locale()**

Formatea un valor decimal al formato en\_US.UTF-8.

```python
standard_value = "{0:.2f}".format(total)
formatted_value = format_decimal_to_locale(
    standard_value, document_json['amount_format_locale']
)
```

#### Parámetros:

<table><thead><tr><th width="208">Nombre</th><th width="187">Tipo</th><th>Descripción</th></tr></thead><tbody><tr><td>value<mark style="color:red;">*</mark></td><td><code>float, decimal.Decimal, str</code></td><td>El ID de la organización a la que pertenece el documento</td></tr><tr><td>to_locale (opcional)</td><td><code>string</code></td><td>El tipo en el que se deben devolver los datos<br>El valor predeterminado es <code>'en_US.UTF-8'</code></td></tr><tr><td>max_decimal_places (opcional)</td><td><code>int</code></td><td>ID de suborganización opcional para filtrado<br>El valor predeterminado es <code>4</code></td></tr><tr><td>min_decimal_places (opcional)</td><td><code>int</code></td><td>El mínimo de lugares decimales que se deben considerar<br>El valor predeterminado es <code>2</code></td></tr></tbody></table>

* value: El valor que debe ser formateado.
* to\_locale (opcional): El formato en el que se transforma el valor.
* max\_decimal\_places (opcional): El máximo de lugares decimales que se deben considerar.
* min\_decimal\_places (opcional): El mínimo de lugares decimales que se deben considerar.

#### Devuelve:

* El valor formateado.

### **compare\_values()**

Compara dos valores por igualdad, manejando varios tipos de datos.

```python
result = compare_values(10, "10")
```

#### Parámetros:

<table><thead><tr><th width="173">Nombre</th><th width="176">Tipo</th><th>Descripción</th></tr></thead><tbody><tr><td>value1<mark style="color:red;">*</mark></td><td><code>any</code></td><td>El primer valor a comparar</td></tr><tr><td>value2<mark style="color:red;">*</mark></td><td><code>any</code></td><td>El segundo valor a comparar</td></tr></tbody></table>

#### Devuelve:

* True si los valores son iguales y False si difieren

### **create\_document\_task()**

Crea una tarea, la asigna a un usuario o grupo, establece la prioridad y opcionalmente envía un correo electrónico.

```python
if not is_task_created:
            create_document_task(user, document_data, "Herkunftsland außerhalb der EU", "Die Gelangensbestätigung kommt von einem Land außerhalb der EU. Bitte das MRN-Dokument anhängen.", "high", 1007, None, False)
            document_data["document_json"]["country_check_task_created"] = True
```

#### Parámetros:

<table><thead><tr><th width="216">Nombre</th><th width="217">Tipo</th><th>Descripción</th></tr></thead><tbody><tr><td>user<mark style="color:red;">*</mark></td><td>ya sea <code>user ID</code> o <code>UserAuthentication</code> object</td><td>El usuario que realiza la actualización</td></tr><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Los datos del documento que contienen información del campo</td></tr><tr><td>title<mark style="color:red;">*</mark></td><td><code>string</code></td><td>El título de la tarea</td></tr><tr><td>description<mark style="color:red;">*</mark></td><td><code>string</code></td><td>La descripción de la tarea</td></tr><tr><td>priority<mark style="color:red;">*</mark></td><td><code>string</code></td><td>La prioridad de la tarea</td></tr><tr><td>assigned_to_user_id<mark style="color:red;">*</mark></td><td><code>int</code></td><td>El id del usuario al que se debe asignar la tarea</td></tr><tr><td>assigned_to_group_id<mark style="color:red;">*</mark></td><td><code>int</code></td><td>El id del grupo al que se debe asignar la tarea</td></tr><tr><td>send_email<mark style="color:red;">*</mark></td><td><code>bool</code></td><td>Determina si se debe enviar un correo electrónico o no</td></tr></tbody></table>

#### Devuelve:

* Dict que indica si el proceso fue exitoso o no

### **set\_document\_sub\_org\_id()**

Establece el sub\_org\_id de los datos del documento especificado.

```python
if sub_org_id != current_sub_org_id:
    document_data["document_json"]["sub_org_id4"] = sub_org_id
    set_document_sub_org_id(document_data, sub_org_id)
```

#### Parámetros:

<table><thead><tr><th width="173">Nombre</th><th width="176">Tipo</th><th>Descripción</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Los datos del documento que contienen información del campo</td></tr><tr><td>sub_org_id<mark style="color:red;">*</mark></td><td><code>string</code></td><td>ID de suborganización opcional para filtrado</td></tr></tbody></table>

### **get\_user\_by\_id()**

Obtiene el usuario con el ID de usuario correspondiente.

```python
requester_mail = str(get_user_by_id(str(requester)).email.lower())
```

#### Parámetros:

<table><thead><tr><th width="173">Nombre</th><th width="176">Tipo</th><th>Descripción</th></tr></thead><tbody><tr><td>user_id<mark style="color:red;">*</mark></td><td><code>string</code></td><td>El ID del usuario</td></tr></tbody></table>

#### Devuelve:

* El usuario con el ID de usuario correspondiente

### **get\_group\_by\_id()**

Obtiene el grupo con el ID de grupo correspondiente.

```python
group_name  = str(get_group_by_id(assigned_to_group_id))
```

#### Parámetros:

<table><thead><tr><th width="173">Nombre</th><th width="176">Tipo</th><th>Descripción</th></tr></thead><tbody><tr><td>group_id<mark style="color:red;">*</mark></td><td><code>string</code></td><td>El ID del grupo</td></tr></tbody></table>

#### Devuelve:

* El grupo con el ID de grupo correspondiente

### **get\_user\_by\_email()**

Obtiene el grupo con el ID de grupo correspondiente.

```python
user_name = str(get_user_by_email(email)
```

#### Parámetros:

<table><thead><tr><th width="173">Nombre</th><th width="176">Tipo</th><th>Descripción</th></tr></thead><tbody><tr><td>email<mark style="color:red;">*</mark></td><td><code>any</code></td><td>El correo electrónico del usuario</td></tr></tbody></table>

#### Devuelve:

* El usuario con el correo electrónico correspondiente

### **add\_table\_column()**

Agrega una columna a la tabla especificada.

```python
table = tables_dict.get("ORDER_CONFIRMATION_TABLE")

if table:
    add_table_column(table, "PROMISED_DELIVERY_DATE")
```

#### Parámetros:

<table><thead><tr><th width="173">Nombre</th><th width="176">Tipo</th><th>Descripción</th></tr></thead><tbody><tr><td>table<mark style="color:red;">*</mark></td><td><code>string</code></td><td>La tabla donde se debe agregar la columna</td></tr><tr><td>col_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>El nombre de la columna</td></tr><tr><td>default_value (opcional)</td><td><code>any</code></td><td><p>El valor inicial para el campo</p><p>El valor predeterminado es <code>None</code></p></td></tr></tbody></table>

### **get\_column\_value()**

Obtiene el valor de una columna especificada.

```python
for row in table['rows']:
        unit = get_column_value(row, "UNIT")
```

#### Parámetros:

<table><thead><tr><th width="173">Nombre</th><th width="176">Tipo</th><th>Descripción</th></tr></thead><tbody><tr><td>row<mark style="color:red;">*</mark></td><td><code>string</code></td><td>La fila donde se encuentra el valor</td></tr><tr><td>col_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>El nombre de la columna</td></tr><tr><td>default_value (opcional)</td><td><code>any</code></td><td>El valor inicial para el campo<br>El valor predeterminado es <code>None</code></td></tr><tr><td>is_clean (opcional)</td><td><code>bool</code></td><td>Convierte el valor a mayúsculas y elimina espacios adicionales<br>El valor predeterminado es <code>False</code></td></tr></tbody></table>

#### Devuelve

* Devuelve el valor de la columna especificada si existe; de lo contrario, devuelve `None`

### **set\_column\_value()**

Establece el valor de la columna especificada. Si la columna no existe, se creará.

```python
supplier_id = get_field_value(document_data, "supplier_id", "")

quote_table = tables_dict["QUOTE_TABLE"]

for row in quote_table.get('rows', []):
    set_column_value(row,"SUPPLIER_ID", supplier_id)
```

#### Parámetros:

<table><thead><tr><th width="173">Nombre</th><th width="176">Tipo</th><th>Descripción</th></tr></thead><tbody><tr><td>row<mark style="color:red;">*</mark></td><td><code>string</code></td><td>La fila donde se encuentra el valor</td></tr><tr><td>col_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>El nombre de la columna</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>any</code></td><td>El valor que se establecerá en la ubicación especificada</td></tr></tbody></table>

#### Devuelve:

* True si el cambio fue exitoso

### **set\_column\_date\_value()**

Establece el valor de fecha de una columna especificada.

```python
set_column_date_value(document_data, row, "DELIVERY_DATE", "2020-12-31", add_days=2)
```

#### Parámetros:

<table><thead><tr><th width="173">Nombre</th><th width="196.05859375">Tipo</th><th>Descripción</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Los datos del documento que contienen información del campo</td></tr><tr><td>row<mark style="color:red;">*</mark></td><td><code>string</code></td><td>La fila donde se encuentra el valor</td></tr><tr><td>col_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>El nombre de la columna</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>string</code></td><td>El valor de fecha a establecer en formato ISO (por ejemplo, "2020-12-31")</td></tr><tr><td>add_days (opcional)</td><td><code>int</code></td><td>Agregar días adicionales a la fecha dada<br>El valor predeterminado es <code>2</code></td></tr><tr><td>skip_weekend (opcional)</td><td><code>bool</code></td><td>Omitir la fecha si cae en fin de semana<br>El valor predeterminado es <code>False</code></td></tr><tr><td>exclude_final_days<br>(opcional)</td><td>ya sea <code>string</code> o <code>int</code></td><td>Especifica los días a excluir (0-6 o domingo a sábado)</td></tr></tbody></table>

### **set\_column\_amount\_value()**

* Convierte el valor a cadena y establece el valor para la columna
* Establece el contenido de la columna al valor
* Formatea el valor según la configuración regional

```python
quantity = float(quantity) / 1000
set_column_amount_value(document_data, row, "QUANTITY", str(quantity))
```

#### Parámetros:

<table><thead><tr><th width="173">Nombre</th><th width="176">Tipo</th><th>Descripción</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Los datos del documento que contienen información del campo</td></tr><tr><td>row<mark style="color:red;">*</mark></td><td><code>string</code></td><td>La fila donde se encuentra el valor</td></tr><tr><td>column_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>El nombre de la columna</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>string</code></td><td>El valor a establecer para el campo (pase un número como cadena, por ejemplo, "123456")</td></tr></tbody></table>

### **delete\_tables()**

Esta función elimina las tablas de los datos del documento.

```python
delete_tables(document_data)
```

#### Parámetros:

<table><thead><tr><th width="173">Nombre</th><th width="176">Tipo</th><th>Descripción</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Los datos del documento que contienen información del campo</td></tr></tbody></table>

### **restore\_tables()**

Esta función restaura las tablas en los datos del documento.

```python
restore_tables(document_data)
```

#### Parámetros:

<table><thead><tr><th width="173">Nombre</th><th width="176">Tipo</th><th>Descripción</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Los datos del documento que contienen información del campo</td></tr></tbody></table>

### **remove\_rows\_from\_table()**

Elimina filas de la tabla especificada.

```python
count = 1
start = 1
remove_rows_from_table(document_data,"INVOICE_TABLE",count,start) 
```

#### Parámetros:

<table><thead><tr><th width="173">Nombre</th><th width="176">Tipo</th><th>Descripción</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Los datos del documento que contienen información del campo</td></tr><tr><td>table_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>El nombre de la tabla</td></tr><tr><td>count<mark style="color:red;">*</mark></td><td><code>int</code></td><td>Cuántas líneas deben ser eliminadas</td></tr><tr><td>start<mark style="color:red;">*</mark></td><td><code>int</code></td><td>El punto de inicio</td></tr></tbody></table>

### **remove\_all\_rows\_except\_one\_from\_table()**

Elimina todas las filas excepto una de la tabla especificada.

```python
count = 1
start = 1
remove_rows_from_table(document_data,"INVOICE_TABLE",count,start) 
```

#### Parámetros:

<table><thead><tr><th width="173">Nombre</th><th width="176">Tipo</th><th>Descripción</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Los datos del documento que contienen información del campo</td></tr><tr><td>line_number<mark style="color:red;">*</mark></td><td><code>int</code></td><td>El número de la línea que no debe ser eliminada</td></tr></tbody></table>

## Atributos Soportados

### Atributos de Campo Principales

| Atributo            | Tipo   | Descripción                                                |
| ------------------- | ------ | ---------------------------------------------------------- |
| `value`             | any    | El valor bruto del campo                                   |
| `formatted_value`   | string | Valor formateado para visualización                        |
| `content`           | string | Contenido extraído original                                |
| `is_required`       | bool   | Si el campo es obligatorio                                 |
| `is_valid`          | bool   | Estado de validación                                       |
| `is_validated`      | bool   | Si el campo ha sido validado por el usuario                |
| `force_validation`  | bool   | Forzar al usuario a validar este campo                     |
| `highlight_field`   | bool   | Resaltar el campo en la interfaz de usuario                |
| `extraction_method` | string | Cómo se extrajo el valor (por ejemplo, `"SCRIPT"`)         |

### Atributos de Validación

| Atributo                | Tipo   | Descripción                                                              |
| ----------------------- | ------ | ------------------------------------------------------------------------ |
| `validation_message`    | string | Mensaje de error mostrado al usuario                                     |
| `validation_code`       | string | Código de error (por ejemplo, `"FORCED_VALIDATION"`, `"INVALID_VALUE"`)  |
| `invalidated_by_script` | bool   | Marca el campo como invalidado por un script                             |

### Atributos de Extracción/OCR

| Atributo            | Tipo   | Descripción                                              |
| ------------------- | ------ | -------------------------------------------------------- |
| `coords`            | object | Coordenadas del cuadro delimitador en el documento       |
| `confidence`        | float  | Puntuación de confianza de OCR/extracción                |
| `score`             | float  | Puntuación de coincidencia/validación                    |
| `score_description` | string | Descripción de la puntuación                             |
| `page`              | int    | Número de página donde se encontró el campo              |
| `rule`              | string | Regla de extracción que se aplicó                        |

## Funciones Integradas de Python

También puedes utilizar algunas de las funciones integradas de Python:

* abs(): Devuelve el valor absoluto de un número.
* len(): Devuelve la longitud (número de elementos) de un objeto, como una lista o cadena.
* isinstance(): Verifica si un objeto es una instancia de una clase o tipo particular.
* print(): Imprime la salida en la consola.
* round(): Redondea un número de punto flotante a un número especificado de lugares decimales.
* str\_to\_bool(): Convierte una cadena a un valor booleano (True o False).
* type(): Devuelve el tipo de un objeto.
* dict(): Crea un objeto diccionario.
* list(): Crea un objeto lista.
* str(): Convierte un valor a una cadena.
* float(): Convierte un valor a un número de punto flotante.
* int(): Convierte un valor a un entero.

Para más detalles, visita la documentación oficial de Python: [Funciones Integradas](https://docs.python.org/3.12/library/functions.html).

## Funciones de la Clase String

También puedes usar estas funciones específicamente para trabajar con cadenas:

* lower(): Convierte todos los caracteres en una cadena a minúsculas.
* upper(): Convierte todos los caracteres en una cadena a mayúsculas.
* split(): Divide una cadena en una lista basada en un delimitador (por ejemplo, espacio o coma).
* startswith(): Verifica si una cadena comienza con un prefijo especificado.
* endswith(): Verifica si una cadena termina con un sufijo especificado.
* strip(): Elimina cualquier espacio en blanco al principio o al final de una cadena.

## Funciones del Módulo Matemático de Python

Estas funciones son parte del módulo matemático y son útiles para operaciones matemáticas:

* floor(): Devuelve el entero más grande menor o igual a un número dado.
* ceil(): Devuelve el entero más pequeño mayor o igual a un número dado.

Para más información, consulta la documentación oficial de Python: [Funciones del Módulo Matemático](https://docs.python.org/3/library/math.html).

## Función de Expresión Regular

* re.search(): Busca un patrón dentro de una cadena y devuelve la primera coincidencia.

Consulta más detalles aquí: [Documentación de re.search](https://docs.python.org/3/library/re.html#re.search).

## Funciones Externas

Aquí hay algunas funciones útiles de bibliotecas externas:

* deepcopy(): Crea una copia de un objeto, incluidos los objetos anidados (del módulo copy).\
  [Documentación de Deepcopy](https://docs.python.org/3/library/copy.html#copy.deepcopy).
* levenshtein\_distance(): Calcula el número de ediciones (inserciones, eliminaciones, sustituciones) requeridas para cambiar una cadena en otra. Esta función está disponible en la [biblioteca Jellyfish](https://jamesturk.github.io/jellyfish/functions/).

## Funciones de Fecha y Hora

Puedes usar las siguientes funciones para trabajar con fechas y horas:

* strptime(): Convierte una cadena en un objeto datetime basado en un formato especificado.
* strftime(): Formatea un objeto datetime en una cadena basada en un formato especificado.

Para más información, consulta la documentación oficial:\
[Funciones de Fecha y Hora](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior).
