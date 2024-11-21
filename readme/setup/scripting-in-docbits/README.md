# Scripting in DocBits

## Guida alla Scripting di Docbits

Benvenuto nella guida alla scripting di Docbits! Qui imparerai come utilizzare gli script per automatizzare e migliorare l'elaborazione dei documenti all'interno di Docbits. Gli script consentono la manipolazione personalizzata dei campi, la trasformazione dei dati e l'implementazione della logica su vari tipi di documenti.

### Per Iniziare

Gli script in Docbits sono scritti in Python. Interagiscono con i campi e i metadati dei documenti per eseguire una vasta gamma di operazioni, dalla semplice formattazione dei dati alla logica complessa.

**Funzioni Chiave**

* `get_field_value(fields_dict, field_name, default=None)`: Recupera il valore di un campo specificato.
* `set_field_value(fields_dict, field_name, value)`: Imposta il valore di un campo specificato.
* `create_new_field(field_name, value)`: Crea un nuovo campo con un nome e un valore specificati.
* `format_decimal_to_locale(value, locale)`: Formatizza un valore decimale secondo una località specificata.

### Esempi di Script

Di seguito sono riportati diversi esempi che dimostrano compiti comuni di scripting.

**Esempio 1: Mappatura della Valuta per le Fatture**

Standardizza i simboli o il testo della valuta ai codici di valuta ISO.

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
