# Script de Génération de Numéros de Facture Étendus pour Docbits

Ce document détaille le script "Generating Extended Invoice Numbers", qui automatise la création de numéros de facture étendus dans Docbits. Les numéros de facture étendus combinent plusieurs identifiants de documents, tels que l'ID de facture et le numéro de bon de commande, en un seul identifiant complet. Ce script améliore la traçabilité des documents et simplifie la tenue des registres.

### Objectif

L'objectif de ce script est de rationaliser le processus de génération de numéros de facture étendus en concaténant automatiquement l'ID de facture et le numéro de bon de commande, fournissant ainsi un identifiant unifié et unique pour chaque document de facture.

### Aperçu du Script

Le script vérifie la présence des champs ID de facture et numéro de bon de commande dans le document, concatène leurs valeurs si les deux sont présents (séparés par un tiret), et met à jour ou crée un nouveau champ pour stocker la valeur combinée.

#### Extrait de Code

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


