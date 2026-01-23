# Script per il Calcolo delle Spese Totali per Docbits

### Introduzione

Questo documento fornisce una guida dettagliata sullo script "Calculating Total Charges" all'interno della piattaforma Docbits. Lo script è progettato per calcolare automaticamente l'importo totale addebitato su una fattura sommando vari addebiti individuali. Questa automazione migliora la precisione e l'efficienza nell'elaborazione dei documenti.

### Obiettivo

L'obiettivo di questo script è ottimizzare il processo di calcolo delle spese totali sulle fatture. Sommando automaticamente gli addebiti specificati, come spese base, tasse e commissioni aggiuntive, lo script garantisce che le spese totali riflesse su ogni fattura siano accurate e complete.

### Dettagli dello Script

#### Implementazione del Codice

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


