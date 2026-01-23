# Skript zur Berechnung der Gesamtkosten für Docbits

### Einführung

Dieses Dokument bietet eine detaillierte Anleitung zum Skript "Calculating Total Charges" innerhalb der Docbits-Plattform. Das Skript ist darauf ausgelegt, automatisch den Gesamtbetrag einer Rechnung zu berechnen, indem verschiedene Einzelgebühren summiert werden. Diese Automatisierung erhöht die Genauigkeit und Effizienz bei der Dokumentenverarbeitung.

### Ziel

Das Ziel dieses Skripts ist es, den Berechnungsprozess für Gesamtkosten auf Rechnungen zu optimieren. Durch das automatische Addieren bestimmter Gebühren wie Basisgebühren, Steuern und zusätzliche Gebühren stellt das Skript sicher, dass die auf jeder Rechnung ausgewiesenen Gesamtkosten korrekt und vollständig sind.

### Skriptdetails

#### Code-Implementierung

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


