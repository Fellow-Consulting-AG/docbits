# Przykładowy skrypt

Oto prosty przykład, jak możesz używać różnych funkcji w małym skrypcie.

```
iban_fuzzy = get_field_value(document_data, 'supplier_iban', None)
iban_extracted = get_field_value(document_data, 'iban_extracted', None)
​
if iban_extracted:
    iban_extracted = iban_extracted.replace(' ','')
​
if iban_fuzzy and iban_extracted and iban_fuzzy != iban_extracted:
    set_field_as_invalid(document_data, "supplier_iban", "There is a difference in the IBAN", "INVALID_VALUE")
elif iban_fuzzy and not iban_extracted: 
    set_field_as_invalid(document_data, "supplier_iban", "There is a difference in the IBAN", "INVALID_VALUE")
elif iban_extracted and not iban_fuzzy:
    set_field_as_invalid(document_data, "supplier_iban", "There is a difference in the IBAN", "INVALID_VALUE")
```
