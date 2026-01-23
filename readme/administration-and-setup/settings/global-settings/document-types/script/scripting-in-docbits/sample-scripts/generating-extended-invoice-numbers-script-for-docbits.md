# Skrypt Generowania Rozszerzonych Numerów Faktur dla DocBits

### Przegląd

Ten przewodnik koncentruje się na automatyzacji tworzenia rozszerzonych numerów faktur w DocBits, co jest kluczową funkcją usprawniającą zarządzanie i śledzenie faktur. Skrypt „Generating Extended Invoice Numbers" łączy różne identyfikatory dokumentów, takie jak ID faktury i numer zamówienia zakupu, tworząc kompleksowy i unikalny identyfikator dla każdej faktury.

### Cel

Głównym celem tego skryptu jest automatyzacja generowania rozszerzonych numerów faktur, ułatwiając śledzenie i zarządzanie fakturami poprzez połączenie wielu identyfikatorów w jeden unikalny numer.

### Implementacja Skryptu

#### Fragment Kodu

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
