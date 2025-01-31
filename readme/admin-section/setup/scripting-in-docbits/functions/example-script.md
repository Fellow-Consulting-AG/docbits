# Example Script

Here's a simple example of how you can use different functions in a small script.

```
iban_fuzzy = get_field_value(document_data, 'supplier_iban', None)
iban_extracted = get_field_value(document_data, 'iban_extracted', None)

if iban_extracted:
    iban_extracted = iban_extracted.replace(' ','')

if iban_fuzzy and iban_extracted and iban_fuzzy != iban_extracted:
    set_field_as_invalid(document_data, "supplier_iban", "Es gibt einen Unterschied bei der IBAN", "INVALID_VALUE")
elif iban_fuzzy and not iban_extracted: 
    set_field_as_invalid(document_data, "supplier_iban", "Es gibt einen Unterschied bei der IBAN", "INVALID_VALUE")
elif iban_extracted and not iban_fuzzy:
    set_field_as_invalid(document_data, "supplier_iban", "Es gibt einen Unterschied bei der IBAN", "INVALID_VALUE")
```
