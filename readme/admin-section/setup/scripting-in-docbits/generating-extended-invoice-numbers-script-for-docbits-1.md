# Generisanje skripte za proširene brojeve računa za Docbits

Ovaj dokument detaljno opisuje skriptu "Generisanje proširenih brojeva računa", koja automatizuje kreiranje proširenih brojeva računa u Docbits-u. Prošireni brojevi računa kombinuju više identifikatora dokumenata, poput ID računa i broja narudžbenice, u jedan sveobuhvatan identifikator. Ova skripta poboljšava praćenje dokumenata i pojednostavljuje vođenje evidencije.

### Svrha

Svrha ove skripte je da olakša proces generisanja proširenih brojeva računa automatskim spajanjem ID-a računa i broja narudžbenice, pružajući tako ujedinjeni i jedinstveni identifikator za svaki dokument računa.

### Pregled skripte

Skripta proverava prisustvo polja ID-a računa i broja narudžbenice unutar dokumenta, spaja njihove vrednosti ako su oba prisutna (razdvojena crticom), i ažurira ili kreira novo polje za čuvanje kombinovane vrednosti.

#### Isječak koda
```python
invoice_id = get_field_value(fields_dict, 'invoice_id')
purchase_order = get_field_value(fields_dict, 'purchase_order')

# Combining invoice ID and purchase order number with a hyphen separator
extended_number = '-'.join(filter(None, [invoice_id, purchase_order]))

# Check if there is an extended number to set
if extended_number:
# Updating the 'invoice_extended_number' field with the combined value
if not 'invoice_extended_number' in fields_dict:
new_field = create_new_field('invoice_extended_number', extended_number)
fields_dict['invoice_extended_number'] = new_field
document_json['fields'].append(new_field)
else:
set_field_value(fields_dict, 'invoice_extended_number', extended_number)
```

