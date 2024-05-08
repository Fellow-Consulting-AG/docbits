# Skripta za Izračunavanje Ukupnih Troškova za DocBits

### Uvod

Ovaj dokument pruža detaljan vodič o skripti "Izračunavanje Ukupnih Troškova" unutar platforme DocBits. Skripta je dizajnirana da automatski izračunava ukupan iznos naplaćen na fakturi zbrajanjem različitih pojedinačnih troškova. Ova automatizacija poboljšava tačnost i efikasnost u procesu obrade dokumenata.

### Cilj

Cilj ove skripte je da optimizuje proces izračunavanja ukupnih troškova na fakturama. Automatskim sabiranjem određenih troškova, kao što su osnovni troškovi, porezi i dodatne naknade, skripta osigurava da ukupni troškovi prikazani na svakoj fakturi budu tačni i sveobuhvatni.

### Detalji Skripte

#### Implementacija Koda
```python
# Initialize variables to store the values of individual charges
total_charges = get_field_value(fields_dict, 'total_charges', None)
fracht = get_field_value(fields_dict, 'additional_amount_2', None)
verpackung = get_field_value(fields_dict, 'additional_amount', None)

# Calculate the total by converting each charge to a float and summing them up
total = 0
if fracht:
total += float(fracht)
if verpackung:
total += float(verpackung)

# Format the total to two decimal places and update the 'total_charges' field
formatted_total = "{0:.2f}".format(total)
if 'total_charges' not in fields_dict:
new_field = create_new_field('total_charges', formatted_total)
fields_dict['total_charges'] = new_field
document_json['fields'].append(new_field)
else:
set_field_value(fields_dict, 'total_charges', formatted_total)
```

