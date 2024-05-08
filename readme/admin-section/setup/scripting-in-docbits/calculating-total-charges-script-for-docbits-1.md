# Skripta za izračunavanje ukupnih troškova za DocBits

##

Skripta "Izračunavanje ukupnih troškova" automatizuje proces sabiranja različitih troškova i dodatnih iznosa unutar faktura. Ovaj vodič će vas provesti kroz postavljanje skripte, logiku i primenu kako biste osigurali tačna izračunavanja ukupnih troškova na vašim dokumentima.

### Svrha

Ova skripta ima za cilj da pruži dinamičan način za izračunavanje ukupnih troškova na fakturi sabiranjem različitih vrsta troškova, kao što su osnovni troškovi, prevoz (Fracht) i pakovanje (Verpackung). Zatim ažurira polje ukupnih troškova fakture sa izračunatim zbirom, osiguravajući tačne informacije o naplati.

### Pregled Skripte

Skripta dobavlja vrednosti iz određenih polja, pretvara ih u decimalne brojeve, sabira ih, a zatim ažurira polje `total_charges` rezultatom. Ako polje `total_charges` ne postoji, skripta će kreirati ovo polje i postaviti vrednost prema potrebi.

#### Isječak koda
```python
total_charges = get_field_value(fields_dict, 'total_charges', None)
fracht = get_field_value(fields_dict, 'additional_amount_2', None)
verpackung = get_field_value(fields_dict, 'additional_amount', None)

# Initialize total to 0
total = 0

# Add fracht to total if it exists
if fracht:
fracht = float(fracht)
total += fracht

# Add verpackung to total if it exists
if verpackung:
verpackung = float(verpackung)
total += verpackung

# Formatting the total to two decimal places
formatted_total = "{0:.2f}".format(total)

# Checking if the total_charges field exists and updating or creating accordingly
if 'total_charges' not in fields_dict:
new_field = create_new_field('total_charges', formatted_total)
fields_dict['total_charges'] = new_field
document_json['fields'].append(new_field)
else:
set_field_value(fields_dict, 'total_charges', formatted_total)
```

