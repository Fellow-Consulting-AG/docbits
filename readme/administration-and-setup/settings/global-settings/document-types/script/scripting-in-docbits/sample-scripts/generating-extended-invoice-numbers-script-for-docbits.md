# Script per la Generazione di Numeri di Fattura Estesi per Docbits

### Panoramica

Questa guida si concentra sull'automazione della creazione di numeri di fattura estesi in Docbits, una funzionalità cruciale per migliorare la gestione e il tracciamento delle fatture. Lo script "Generating Extended Invoice Numbers" concatena vari identificatori di documenti, come l'ID fattura e il numero dell'ordine di acquisto, per creare un identificatore completo e univoco per ogni fattura.

### Obiettivo

L'obiettivo principale di questo script è automatizzare la generazione di numeri di fattura estesi, facilitando il tracciamento e la gestione delle fatture combinando più identificatori in un unico numero univoco.

### Implementazione dello Script

#### Frammento di Codice

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


