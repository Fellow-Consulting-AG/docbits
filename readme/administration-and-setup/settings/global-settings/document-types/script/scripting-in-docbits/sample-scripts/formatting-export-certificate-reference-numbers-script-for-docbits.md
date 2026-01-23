# Script de Formatage des Numéros de Référence de Certificats d'Exportation pour Docbits

Ce document décrit le script "Formatting Export Certificate Reference Numbers", destiné à standardiser les numéros de référence sur les certificats d'exportation dans Docbits. Un formatage approprié garantit que les numéros de référence sont conformes aux exigences des systèmes externes ou aux réglementations.

### Objectif

L'objectif principal du script est de formater les numéros de référence sur les certificats d'exportation, en s'assurant qu'ils respectent une exigence de longueur prédéfinie en les complétant avec des zéros en tête. Cette cohérence aide à maintenir un format standardisé pour tous les documents d'exportation traités via Docbits.

### Aperçu du Script

Le script identifie le champ `reference_number` dans un certificat d'exportation, vérifie sa longueur et, si nécessaire, complète le numéro avec des zéros en tête pour s'assurer qu'il respecte l'exigence de longueur minimale.

#### Extrait de Code

```python
ref_number = get_field_value(fields_dict, 'reference_number')
# Ensure the reference number meets a minimum length of 10 characters
if len(ref_number) < 10:
    ref_number = ref_number.zfill(10)
    set_field_value(fields_dict, 'reference_number', ref_number)
```


