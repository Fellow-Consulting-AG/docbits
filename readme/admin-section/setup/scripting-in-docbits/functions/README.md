# Functions

## **Functional Documentation**

This module contains functions for manipulating document data and performing various operations related to document fields.

## **Functions**

### **set\_field\_value(document\_data, field\_name, value)**

Sets the value of a field in the document data.

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

<table><thead><tr><th width="173">Name</th><th width="176">Type</th><th>Description</th></tr></thead><tbody><tr><td>document_data</td><td><code>dictionary</code></td><td>The document data containing field information</td></tr><tr><td>field_name</td><td><code>string</code></td><td>The name of the field to set</td></tr><tr><td>value</td><td><code>any</code></td><td>The value to set for the field</td></tr></tbody></table>

### **set\_date\_value(document\_data, field\_name, value, add\_days=0, skip\_weekend=False)**

Sets the value of a date field in the document data.

```python
invoice_date = get_field_value(document_data, 'invoice_date', None)
    
if not document_json.get("script_executed", False):
    if invoice_date:
        set_date_value(document_data, "accounting_date", invoice_date)
        document_json["script_executed"] = True
```

#### Parameters:

<table><thead><tr><th width="229">Name</th><th width="138">Type</th><th>Description</th></tr></thead><tbody><tr><td>document_data</td><td><code>dictionary</code></td><td>The document data containing field information</td></tr><tr><td>field_name</td><td><code>string</code></td><td>The name of the field to set</td></tr><tr><td>value</td><td><code>string</code></td><td>The date value to set in ISO format (e.g., "2020-12-31").</td></tr><tr><td>add_days (optional)</td><td><code>int</code></td><td>Add additional days to the given date</td></tr><tr><td>skip_weekend (optional)</td><td><code>bool</code></td><td>Skips the date if it falls on the weekend</td></tr></tbody></table>

### **set\_amount\_value(document\_data, field\_name, value)**

Sets the value of an amount field in the document data.

```python
total_amount = get_field_value(document_data, "net_amount")
lines_total = 0.0
set_amount_value(document_data, "net_amount",str(lines_total))
```

#### Parameters:

<table><thead><tr><th width="173">Name</th><th width="176">Type</th><th>Description</th></tr></thead><tbody><tr><td>document_data</td><td><code>dictionary</code></td><td>The document data containing field information</td></tr><tr><td>field_name</td><td><code>string</code></td><td>The name of the field to set</td></tr><tr><td>value</td><td><code>string</code></td><td>The value to set for the field (pass a number as string e.g., "123456"</td></tr></tbody></table>

### **get\_field\_value(document\_data, field\_name, default\_value=None, is\_clean=False)**

Gets the value of a field from the document data.

```python
total_amount = get_field_value(document_data, "net_amount")
lines_total = 0.0
set_amount_value(document_data, "net_amount", str(lines_total))
```

<table><thead><tr><th width="191">Name</th><th width="176">Type</th><th>Description</th></tr></thead><tbody><tr><td>document_data</td><td><code>dictionary</code></td><td>The document data containing field information</td></tr><tr><td>field_name</td><td><code>string</code></td><td>The name of the field to set</td></tr><tr><td>default_value (optional)</td><td><code>any</code></td><td>Returns default_value if no field value is found</td></tr><tr><td>is_clean (optional)</td><td><code>bool</code></td><td>Converts the value to uppercase and removes any extra spaces</td></tr></tbody></table>

Returns:

* Value of the specified field

### **create\_new\_field(field\_name, value="")**

Creates a new field with the specified name and value.

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

<table><thead><tr><th width="140">Name</th><th width="133">Type</th><th>Description</th></tr></thead><tbody><tr><td>field_name</td><td><code>str</code></td><td>The document data containing field information</td></tr><tr><td>value</td><td><code>any</code></td><td>The initial value for the field (default is an empty string).</td></tr></tbody></table>

#### Returns:

* Dictionary of the new created field

### **delete\_field(document\_data, field\_name)**

Deletes a field from the document data

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

<table><thead><tr><th width="173">Name</th><th width="176">Type</th><th>Description</th></tr></thead><tbody><tr><td>document_data</td><td><code>dictionary</code></td><td>The document data containing field information</td></tr><tr><td>field_name</td><td><code>string</code></td><td>The name of the field to delete</td></tr></tbody></table>

#### Returns:

* Document\_data as json and as dict after field got deleted

### **set\_is\_required(document\_data, field\_name, value)**

Sets the 'is\_required' attribute of a field in the document data.

```python
net_amount = get_field_value(document_data, "net_amount", None)
if net_amount:
    set_is_required(document_data, "tax_country", True)
    set_is_required(document_data, "tax_code_without_country", True)
```

#### Parameters:

<table><thead><tr><th width="173">Name</th><th width="176">Type</th><th>Description</th></tr></thead><tbody><tr><td>document_data</td><td><code>dictionary</code></td><td>The document data containing field information</td></tr><tr><td>field_name</td><td><code>string</code></td><td>The name of the field to set</td></tr><tr><td>value</td><td><code>bool</code></td><td>The value to set for the field</td></tr></tbody></table>

### **set\_force\_validation(document\_data, field\_name, value, reset\_validation=False)**

Sets the 'force\_validation' attribute of a field in the document data.

```python
if supplier_id in supplier_to_check:
    set_force_validation(document_data, 'purchase_order', True, reset_validation=reset_validation)
```

#### Parameters:

<table><thead><tr><th width="173">Name</th><th width="176">Type</th><th>Description</th></tr></thead><tbody><tr><td>document_data</td><td><code>dictionary</code></td><td>The document data containing field information</td></tr><tr><td>field_name</td><td><code>string</code></td><td>The name of the field to set</td></tr><tr><td>value</td><td><code>bool</code></td><td>The value to set for the field</td></tr><tr><td>reset_validation (optional)</td><td><code>bool</code></td><td>Sets the "is_validated" attribute to the specified value</td></tr></tbody></table>

### **set\_field\_as\_invalid(document\_data, field\_name, message, code=None)**

Marks a field as invalid in the document data.

```python
if not document_date:
    set_field_as_invalid(document_data, "document_date", "Es ist kein Datum vorhanden", "INVALID_VALUE")
```

#### Parameters:

<table><thead><tr><th width="173">Name</th><th width="176">Type</th><th>Description</th></tr></thead><tbody><tr><td>document_data</td><td><code>dictionary</code></td><td>The document data containing field information</td></tr><tr><td>field_name</td><td><code>string</code></td><td>The name of the field to mark as invalid</td></tr><tr><td>message</td><td><code>string</code></td><td>The validation message for the field</td></tr><tr><td>code (optional)</td><td><code>string</code></td><td>Error code for the validation (default is None)</td></tr></tbody></table>

### **set\_field\_attribute(document\_data, field\_name, attribute\_name, value)**

Sets a custom attribute of a field in the document data.

```python
if purchase_order:
    if po_supplier_id != invoice_supplier_id:
        set_field_as_invalid(document_data, "supplier_name", "Supplier is different from PO supplier")
    else:
        set_field_attribute(document_data, "supplier_name", "is_valid", True)
        set_field_attribute(document_data, "supplier_name", "validation_message","")
```

#### Parameters:

<table><thead><tr><th width="173">Name</th><th width="176">Type</th><th>Description</th></tr></thead><tbody><tr><td>document_data</td><td><code>dictionary</code></td><td>The document data containing field information</td></tr><tr><td>field_name</td><td><code>string</code></td><td>The name of the field to set</td></tr><tr><td>attribute_name</td><td><code>string</code></td><td>The name of the attribute to set</td></tr><tr><td>value</td><td><code>any</code></td><td>The value to set for the attribute</td></tr></tbody></table>

### **is\_supplier\_valid(user: UserAuthentication, filter\_data\_json, sub\_org\_id=None)**

Checks if a supplier is valid based on the provided criteria.

```python
bool = is_supplier_valid(user, {"name": "Supplier Inc."})
```

#### Parameters:

<table><thead><tr><th width="203">Name</th><th width="216">Type</th><th>Description</th></tr></thead><tbody><tr><td>user </td><td><code>UserAuthentication</code></td><td>The authenticated user</td></tr><tr><td>filter_data_json</td><td><code>json</code></td><td>Filter criteria for validating the supplier</td></tr><tr><td>sub_org_id (optional)</td><td><code>string</code></td><td>Optional sub-organization ID for filtering</td></tr><tr><td>value</td><td><code>any</code></td><td>The value to set for the attribute</td></tr></tbody></table>

Returns:

* True, if the user is valid
* False if the user isn’t valid

### **get\_document\_content(document\_data)**

Returns the document content based on the document data.

```python
document_content = get_document_content(doc)
if document_content:
    document_content = document_content.lower()
```

#### Parameters:

<table><thead><tr><th width="173">Name</th><th width="176">Type</th><th>Description</th></tr></thead><tbody><tr><td>document_data</td><td><code>dictionary</code></td><td>The document data containing field information</td></tr></tbody></table>

#### Returns:

* Document content of document data.

### **update\_document\_status\_with\_doc\_id(doc\_id, user, org\_id, status, message=None, doc\_classification\_class=None)**

Updates the status of a document with the specified ID.

```python
genehmigung_user_1   = get_field_value(document_data, 'genehmigung_user_1', None)

if genehmigung_user_1!="LEER":
    update_document_status_with_doc_id(document_json['doc_id'], user, document_json['org_id'], "validated_pending_approval")
```

#### Parameters:

<table><thead><tr><th width="228">Name</th><th width="216">Type</th><th>Description</th></tr></thead><tbody><tr><td>doc_id</td><td><code>string</code></td><td>The ID of the document to update</td></tr><tr><td>user</td><td>either <code>user ID</code> or <code>UserAuthentication</code> object</td><td>The user performing the update</td></tr><tr><td>org_id</td><td><code>string</code></td><td>The ID of the organization to which the document belongs</td></tr><tr><td>status</td><td><code>string</code></td><td>The new status of the document</td></tr><tr><td>message (optional)</td><td><code>string</code></td><td>Optional message associated with the status update</td></tr><tr><td>doc_classification_class (optional)</td><td><code>string</code></td><td>Optional document classification class</td></tr></tbody></table>

### **get\_lov\_values(org\_id, key, return\_type="list\_of\_objects", sub\_org\_id=None)**

Gets the LOV values from a specific org\_id.

```python
reverse_charge_to_check = get_lov_values(org_id, 'Kosten', return_type="list_of_values")
```

#### Parameters:

<table><thead><tr><th width="173">Name</th><th width="176">Type</th><th>Description</th></tr></thead><tbody><tr><td>org_id</td><td><code>string</code></td><td>The ID of the organization to which the document belongs</td></tr><tr><td>return_type (optional)</td><td><code>string</code></td><td>The type in which the data should be returned</td></tr><tr><td>sub_org_id (optional)</td><td><code>string</code></td><td>Optional sub-organization ID for filtering</td></tr></tbody></table>

#### Returns:

* LOV-Values as a list of objects or as a list.

### **format\_decimal\_to\_locale(value, to\_locale="en\_US.UTF-8", max\_decimal\_places=4, min\_decimal\_places=2)**

Formats a decimal value to en\_US.UTF-8 format.

```python
standard_value = "{0:.2f}".format(total)
formatted_value = format_decimal_to_locale(
    standard_value, document_json['amount_format_locale']
)
```

#### Parameters:

<table><thead><tr><th width="208">Name</th><th width="187">Type</th><th>Description</th></tr></thead><tbody><tr><td>value</td><td><code>float, decimal.Decimal, str</code> </td><td>The ID of the organization to which the document belongs</td></tr><tr><td>to_locale (optional)</td><td><code>string</code></td><td>The type in which the data should be returned</td></tr><tr><td>max_decimal_places (optional)</td><td><code>int</code></td><td>Optional sub-organization ID for filtering</td></tr><tr><td>min_decimal_places (optional)</td><td><code>int</code></td><td>The minimum of decimal places which should be considered</td></tr></tbody></table>

* value: The value which should be formatted.
* to\_locale (optional): The format in which the value gets transformed.
* max\_decimal\_places (optional): The maximum of decimal places which should be considered.
* min\_decimal\_places (optional): The minimum of decimal places which should be considered.

#### Returns:

* The formatted value.

### **compare\_values(value1, value2)**

Compares two values for equality, handling various data types.

```python
result = compare_values(10, "10")
```

#### Parameters:

<table><thead><tr><th width="173">Name</th><th width="176">Type</th><th>Description</th></tr></thead><tbody><tr><td>value1</td><td><code>any</code></td><td>The first value to compare</td></tr><tr><td>value2</td><td><code>any</code></td><td>The second value to compare</td></tr></tbody></table>

#### Returns:

* True if the values are equal and False if they differ

### **create\_document\_task( user, document\_data, title, description, priority,** **assigned\_to\_user\_id, assigned\_to\_group\_id, send\_email: bool)**

Creates a task, assigns it to a user or group, sets priority, and optionally sends an email.

```python
if not is_task_created:
            create_document_task(user, document_data, "Herkunftsland außerhalb der EU", "Die Gelangensbestätigung kommt von einem Land außerhalb der EU. Bitte das MRN-Dokument anhängen.", "high", 1007, None, False)
            document_data["document_json"]["country_check_task_created"] = True
```

#### Parameters:

<table><thead><tr><th width="211">Name</th><th width="217">Type</th><th>Description</th></tr></thead><tbody><tr><td>user</td><td>either <code>user ID</code> or <code>UserAuthentication</code> object</td><td>The user performing the update</td></tr><tr><td>document_data</td><td><code>dictionary</code></td><td>The document data containing field information</td></tr><tr><td>title</td><td><code>string</code></td><td>The title of the task</td></tr><tr><td>description</td><td><code>string</code></td><td>The description of the task</td></tr><tr><td>priority</td><td><code>string</code></td><td>The priority of the task</td></tr><tr><td>assigned_to_user_id</td><td><code>int</code></td><td>The id of the user to which the task should assigned to</td></tr><tr><td>assigned_to_group_id</td><td><code>int</code></td><td>The id of the group to which the task should assigned to</td></tr><tr><td>send_email</td><td><code>bool</code></td><td>Determine if an email should be send or not</td></tr></tbody></table>

#### Returns:

* Dict which is indicating if the process was successful or not

### **set\_document\_sub\_org\_id(document\_data, sub\_org\_id)**

Sets the sub\_org\_id of the specified document\_data.

```python
if sub_org_id != current_sub_org_id:
    document_data["document_json"]["sub_org_id4"] = sub_org_id
    set_document_sub_org_id(document_data, sub_org_id)
```

#### Parameters:

<table><thead><tr><th width="173">Name</th><th width="176">Type</th><th>Description</th></tr></thead><tbody><tr><td>document_data</td><td><code>dictionary</code></td><td>The document data containing field information</td></tr><tr><td>sub_org_id</td><td><code>string</code></td><td>Optional sub-organization ID for filtering</td></tr></tbody></table>

### **get\_user\_by\_id(user\_id)**

Gets the user with the corresponding user ID.

```python
requester_mail = str(get_user_by_id(str(requester)).email.lower())
```

#### Parameters:

<table><thead><tr><th width="173">Name</th><th width="176">Type</th><th>Description</th></tr></thead><tbody><tr><td>user_id</td><td><code>string</code></td><td>The ID of the user</td></tr></tbody></table>

#### Returns:

* The user with the corresponding user ID

### **get\_group\_by\_id(group\_id)**

Gets the group with the corresponding group ID.

```python
group_name  = str(get_group_by_id(assigned_to_group_id))
```

Parameters:

<table><thead><tr><th width="173">Name</th><th width="176">Type</th><th>Description</th></tr></thead><tbody><tr><td>group_id</td><td><code>string</code></td><td>The ID of the group</td></tr></tbody></table>

#### Returns:

* The group with the corresponding group ID

### **add\_table\_column(table, col\_name, default\_value=None)**

Adds a column to the corresponding table.

```python
table = tables_dict.get("ORDER_CONFIRMATION_TABLE")

if table:
    add_table_column(table, "PROMISED_DELIVERY_DATE")
```

Parameters:

<table><thead><tr><th width="173">Name</th><th width="176">Type</th><th>Description</th></tr></thead><tbody><tr><td>table</td><td><code>string</code></td><td>The table where the column should be added</td></tr><tr><td>col_name</td><td><code>string</code></td><td>The name of the column</td></tr><tr><td>default_value (optional)</td><td><code>any</code></td><td>The initial value for the field (default is an empty string)</td></tr></tbody></table>

### **get\_column\_value(row, column\_name, default\_value=None, is\_clean=False)**

Gets the value of a specified column.

```python
for row in table['rows']:
        unit = get_column_value(row, "UNIT")
```

#### Parameters:

<table><thead><tr><th width="173">Name</th><th width="176">Type</th><th>Description</th></tr></thead><tbody><tr><td>row</td><td><code>string</code></td><td>The row where the value is located</td></tr><tr><td>col_name</td><td><code>string</code></td><td>The name of the column</td></tr><tr><td>default_value (optional)</td><td><code>any</code></td><td>The initial value for the field (default is an empty string)</td></tr><tr><td>is_clean (optional)</td><td><code>bool</code></td><td>Converts the value to uppercase and removes any extra spaces</td></tr></tbody></table>

#### Returns

* The value of the specified column

### **set\_column\_value(row, column\_name, value)**

Sets the value of a specified column.

```python
supplier_id = get_field_value(document_data, "supplier_id", "")

quote_table = tables_dict["QUOTE_TABLE"]

for row in quote_table.get('rows', []):
    set_column_value(row,"SUPPLIER_ID", supplier_id)
```

#### Parameters:

<table><thead><tr><th width="173">Name</th><th width="176">Type</th><th>Description</th></tr></thead><tbody><tr><td>row</td><td><code>string</code></td><td>The row where the value is located</td></tr><tr><td>col_name</td><td><code>string</code></td><td>The name of the column</td></tr><tr><td>value</td><td><code>any</code></td><td>The value that will be set at the specified location</td></tr></tbody></table>

#### Returns:

* True if the change was successful

### **set\_column\_date\_value(document\_data, row, column\_name, value, add\_days=0)**

Sets the date value of a specified column.

```python
set_column_date_value(document_data, row, "DELIVERY_DATE", "2020-12-31", add_days=2)
```

#### Parameters:

<table><thead><tr><th width="173">Name</th><th width="176">Type</th><th>Description</th></tr></thead><tbody><tr><td>document_data</td><td><code>dictionary</code></td><td>The document data containing field information</td></tr><tr><td>row</td><td><code>string</code></td><td>The row where the value is located</td></tr><tr><td>col_name</td><td><code>string</code></td><td>The name of the column</td></tr><tr><td>value</td><td><code>string</code></td><td>The date value to set in ISO format (e.g., "2020-12-31")</td></tr><tr><td>add_days</td><td><code>int</code></td><td>Add additional days to the given date</td></tr></tbody></table>

### **set\_column\_amount\_value(document\_data, row, column\_name, value)**

* Convert value to string and set the value for the column
* Set column content to the value
* Format value according to the locale

```python
quantity = float(quantity) / 1000
set_column_amount_value(document_data, row, "QUANTITY", str(quantity))
```

#### Parameters:

<table><thead><tr><th width="173">Name</th><th width="176">Type</th><th>Description</th></tr></thead><tbody><tr><td>document_data</td><td><code>dictionary</code></td><td>The document data containing field information</td></tr><tr><td>row</td><td><code>string</code></td><td>The row where the value is located</td></tr><tr><td>column_name</td><td><code>string</code></td><td>The name of the column</td></tr><tr><td>value</td><td><code>string</code></td><td>The value to set for the field (pass a number as string e.g., "123456")</td></tr></tbody></table>

### **remove\_rows\_from\_table(document\_data, table\_name, count, start)**

Removes rows from the specified table.

```python
count = 1
start = 1
remove_rows_from_table(document_data,"INVOICE_TABLE",count,start) 
```

#### Parameters:

<table><thead><tr><th width="173">Name</th><th width="176">Type</th><th>Description</th></tr></thead><tbody><tr><td>document_data</td><td><code>dictionary</code></td><td>The document data containing field information</td></tr><tr><td>table_name</td><td><code>string</code></td><td>The name of the table</td></tr><tr><td>count</td><td><code>int</code></td><td>How many lines should be deleted</td></tr><tr><td>start</td><td><code>int</code></td><td>The starting point</td></tr></tbody></table>

### **remove\_all\_rows\_except\_one\_from\_table(document\_data, line\_number)**

Removes all rows except one from the specified table

```python
count = 1
start = 1
remove_rows_from_table(document_data,"INVOICE_TABLE",count,start) 
```

#### Parameters:

<table><thead><tr><th width="173">Name</th><th width="176">Type</th><th>Description</th></tr></thead><tbody><tr><td>document_data</td><td><code>dictionary</code></td><td>The document data containing field information</td></tr><tr><td>line_number</td><td><code>int</code></td><td>The number of the line which should not be removed</td></tr></tbody></table>



## Python Built-in Functions

You can also utilize some of the python in-build functions:

* abs(): Returns the absolute value of a number.
* len(): Returns the length (number of items) of an object, like a list or string.
* isinstance(): Checks if an object is an instance of a particular class or type.
* print(): Prints output to the console.
* round(): Rounds a floating-point number to a specified number of decimal places.
* str\_to\_bool(): Converts a string to a boolean value (True or False).
* type(): Returns the type of an object.
* dict(): Creates a dictionary object.
* list(): Creates a list object.
* str(): Converts a value to a string.
* float(): Converts a value to a floating-point number.
* int(): Converts a value to an integer.

For more details, visit the official Python documentation: [Built-in Functions](https://docs.python.org/3.12/library/functions.html).

## String Class Functions

You can also use these functions specifically for working with strings:

* lower(): Converts all characters in a string to lowercase.
* upper(): Converts all characters in a string to uppercase.
* split(): Splits a string into a list based on a delimiter (e.g., space or comma).
* startswith(): Checks if a string starts with a specified prefix.
* endswith(): Checks if a string ends with a specified suffix.
* strip(): Removes any leading or trailing whitespace from a string.

## Functions from the Python Math Module

These functions are part of the math module and are useful for mathematical operations:

* floor(): Returns the largest integer less than or equal to a given number.
* ceil(): Returns the smallest integer greater than or equal to a given number.

For more information, check out the official Python documentation: [Math Module Functions](https://docs.python.org/3/library/math.html).

## Regular Expression Function

* re.search(): Searches for a pattern within a string and returns the first match.

See more details here: [re.search Documentation](https://docs.python.org/3/library/re.html#re.search).

## External Functions

Here are some useful functions from external libraries:

* deepcopy(): Creates a copy of an object, including nested objects (from the copy module).\
  [Deepcopy Documentation](https://docs.python.org/3/library/copy.html#copy.deepcopy).
* levenshtein\_distance(): Calculates the number of edits (insertions, deletions, substitutions) required to change one string into another. This function is available in the [Jellyfish library](https://jamesturk.github.io/jellyfish/functions/).

## Date and Time Functions

You can use the following functions for working with dates and times:

* strptime(): Converts a string into a datetime object based on a specified format.
* strftime(): Formats a datetime object into a string based on a specified format.

For more information, check the official documentation:\
[Date and Time Functions](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior).
