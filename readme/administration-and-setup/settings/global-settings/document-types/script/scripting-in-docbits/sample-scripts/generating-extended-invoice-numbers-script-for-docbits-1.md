# Script per la Generazione di Numeri di Fattura Estesi per Docbits

Questo documento descrive in dettaglio lo script "Generating Extended Invoice Numbers", che automatizza la creazione di numeri di fattura estesi in Docbits. I numeri di fattura estesi combinano più identificatori di documenti, come l'ID fattura e il numero dell'ordine di acquisto, in un unico identificatore completo. Questo script migliora la tracciabilità dei documenti e semplifica la tenuta dei registri.

### Scopo

Lo scopo di questo script è ottimizzare il processo di generazione di numeri di fattura estesi concatenando automaticamente l'ID fattura e il numero dell'ordine di acquisto, fornendo così un identificatore unificato e univoco per ogni documento di fattura.

### Panoramica dello Script

Lo script verifica la presenza dei campi ID fattura e numero dell'ordine di acquisto all'interno del documento, concatena i loro valori se entrambi sono presenti (separati da un trattino) e aggiorna o crea un nuovo campo per memorizzare il valore combinato.

#### Frammento di Codice

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


