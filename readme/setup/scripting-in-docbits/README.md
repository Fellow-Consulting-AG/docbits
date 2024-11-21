# Scripting dans DocBits

## Guide de script Docbits

Bienvenue dans le guide de script Docbits ! Ici, vous apprendrez à utiliser des scripts pour automatiser et améliorer le traitement de vos documents dans Docbits. Les scripts permettent la manipulation personnalisée des champs, la transformation des données et l'implémentation de la logique à travers divers types de documents.

### Pour Commencer

Les scripts dans Docbits sont écrits en Python. Ils interagissent avec les champs de documents et les métadonnées pour effectuer une large gamme d'opérations, allant du formatage simple des données à une logique complexe.

**Fonctions Clés**

* `get_field_value(fields_dict, field_name, default=None)`: Récupère la valeur d'un champ spécifié.
* `set_field_value(fields_dict, field_name, value)`: Définit la valeur d'un champ spécifié.
* `create_new_field(field_name, value)`: Crée un nouveau champ avec un nom et une valeur spécifiés.
* `format_decimal_to_locale(value, locale)`: Formate une valeur décimale selon une locale spécifiée.

### Exemples de Scripts

Ci-dessous, plusieurs exemples démontrant des tâches de script courantes.

**Exemple 1 : Mapping de Devise pour les Factures**

Standardiser les symboles ou textes de devise en codes de devise ISO.

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
