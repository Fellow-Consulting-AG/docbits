# Script voor het Berekenen van Totale Kosten voor Docbits

### Introductie

Dit document biedt een gedetailleerde handleiding over het "Calculating Total Charges" script binnen het Docbits-platform. Het script is ontworpen om automatisch het totale bedrag op een factuur te berekenen door verschillende individuele kosten op te tellen. Deze automatisering verbetert de nauwkeurigheid en efficiëntie bij documentverwerking.

### Doelstelling

Het doel van dit script is om het berekeningsproces voor totale kosten op facturen te stroomlijnen. Door automatisch opgegeven kosten op te tellen, zoals basiskosten, belastingen en extra vergoedingen, zorgt het script ervoor dat de totale kosten die op elke factuur worden weergegeven nauwkeurig en volledig zijn.

### Scriptdetails

#### Code-implementatie

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


