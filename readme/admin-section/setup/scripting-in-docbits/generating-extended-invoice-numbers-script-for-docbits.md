# Generisanje skripte za proširene brojeve fakture za Docbits

### Pregled

Ovaj vodič se fokusira na automatizaciju kreiranja proširenih brojeva faktura u Docbits-u, ključnoj funkciji za poboljšanje upravljanja fakturama i praćenja. Skripta "Generisanje proširenih brojeva faktura" spaja različite identifikatore dokumenata, poput ID fakture i broja narudžbenice, kako bi kreirala sveobuhvatan i jedinstven identifikator za svaku fakturu.

### Cilj

Osnovni cilj ove skripte je automatizacija generisanja proširenih brojeva faktura, olakšavajući praćenje i upravljanje fakturama kombinovanjem više identifikatora u jedan, jedinstveni broj.

### Implementacija skripte

#### Isječak koda
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

