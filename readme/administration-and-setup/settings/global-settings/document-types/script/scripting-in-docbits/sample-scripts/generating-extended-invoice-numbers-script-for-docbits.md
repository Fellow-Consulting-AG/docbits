# Script voor het Genereren van Uitgebreide Factuurnummers voor Docbits

### Overzicht

Deze handleiding richt zich op het automatiseren van de creatie van uitgebreide factuurnummers in Docbits, een cruciale functie voor het verbeteren van factuurbeheer en -tracking. Het "Generating Extended Invoice Numbers" script voegt verschillende documentidentificatoren samen, zoals factuur-ID en inkoopordernummer, om een uitgebreide en unieke identificator voor elke factuur te creëren.

### Doelstelling

Het primaire doel van dit script is het automatiseren van de generatie van uitgebreide factuurnummers, waardoor het traceren en beheren van facturen wordt vergemakkelijkt door meerdere identificatoren te combineren tot één uniek nummer.

### Script-implementatie

#### Codefragment

```python
# Retrieve the values of invoice ID and purchase order number from the document
invoice_id = get_field_value(fields_dict, 'invoice_id')
purchase_order = get_field_value(fields_dict, 'purchase_order')

# Concatenate the invoice ID and purchase order number with a hyphen if both exist
extended_number = '-'.join(filter(None, [invoice_id, purchase_order]))

# Check and update the 'invoice_extended_number' field with the concatenated value
if extended_number:
    if 'invoice_extended_number' not in fields_dict:
        new_field = create_new_field('invoice_extended_number', extended_number)
        fields_dict['invoice_extended_number'] = new_field
        document_json['fields'].append(new_field)
    else:
        set_field_value(fields_dict, 'invoice_extended_number', extended_number)
```


