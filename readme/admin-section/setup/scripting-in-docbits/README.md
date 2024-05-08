# Skriptovanje u DocBits-u

## Vodič za skriptovanje u DocBits-u

Dobrodošli u vodič za skriptovanje u DocBits-u! Ovde ćete naučiti kako da koristite skripte za automatizaciju i unapređenje obrade dokumenata unutar DocBits-a. Skripte omogućavaju manipulaciju prilagođenih polja, transformaciju podataka i implementaciju logike na različitim tipovima dokumenata.

### Početak rada

Skripte u DocBits-u se pišu u Pythonu. One interaguju sa poljima dokumenata i metapodacima kako bi obavile širok spektar operacija, od jednostavnog oblikovanja podataka do kompleksne logike.

#### Ključne funkcije

* `get_field_value(fields_dict, field_name, default=None)`: Dobavlja vrednost određenog polja.
* `set_field_value(fields_dict, field_name, value)`: Postavlja vrednost određenog polja.
* `create_new_field(field_name, value)`: Kreira novo polje sa određenim imenom i vrednošću.
* `format_decimal_to_locale(value, locale)`: Oblikuje decimalnu vrednost prema određenom lokalitetu.

### Primeri skripti

U nastavku su prikazani neki primeri koji ilustruju uobičajene zadatke skriptovanja.

#### Primer 1: Mapiranje valuta za fakture

Standardizujte simbole ili tekst valute u ISO kodove valuta.
```python
currency_map = {
"€": "EUR",
"EURO": "EUR",
"$": "USD",
"£": "GBP"
}
currency_value = get_field_value(fields_dict, "currency", None)
if currency_value:
currency_value = currency_value.upper()
if currency_value in currency_map:
currency_value = currency_map[currency_value]
set_field_value(fields_dict, "currency", currency_value)
```

