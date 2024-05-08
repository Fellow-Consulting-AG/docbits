# Gestionnaire de mise en page

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 08.46.24.png" alt=""><figcaption></figcaption></figure>

#### Aperçu

Le Gestionnaire de mise en page permet aux administrateurs de configurer et de modifier visuellement la mise en page des types de documents en définissant des propriétés pour divers champs de données et groupes au sein d'un document. Cette interface aide à garantir que les modèles d'extraction et les points de saisie manuelle de données s'alignent précisément sur la structure du document tel que numérisé ou téléchargé dans Docbits.

#### Composants clés

1. **Groupes et Champs**:
* **Groupes**: Unités organisationnelles au sein d'un type de document qui catégorisent des champs liés (par exemple, Détails de la facture, Détails de paiement). Ils peuvent être développés ou réduits et disposés pour refléter le regroupement logique dans le document réel.
* **Champs**: Points de données individuels au sein de chaque groupe (par exemple, Numéro de facture, Conditions de paiement). Chaque champ peut être personnalisé pour la capture, l'affichage et le traitement des données.
2. **Panneau de propriétés**:
* Ce panneau affiche les propriétés du champ ou du groupe sélectionné, permettant une configuration détaillée, telle que:
* **Étiquette**: L'étiquette visible pour le champ dans l'interface utilisateur.
* **Nom du champ**: L'identifiant technique utilisé dans le système.
* **Largeur de l'élément en pourcentage**: Détermine la largeur du champ par rapport à la mise en page du document.
* **Index de tabulation**: Contrôle l'ordre de tabulation pour la navigation.
* **Exécuter un script en cas de modification**: Indique si un script doit être exécuté lorsque la valeur du champ change.
* **Afficher l'étiquette à gauche**: Indique si l'étiquette est affichée à gauche du champ ou au-dessus de celui-ci.
* **Est un champ de texte long**: Spécifie si le champ doit être un champ de texte long, pouvant accueillir de plus grandes quantités de texte.
* **Sélectionner le type de modèle**: Option pour sélectionner quel type de modèle gérera l'extraction de ce champ.
* **Longueur du champ**: Longueur maximale des données à accepter dans ce champ.
* **Mots-clés interdits**: Mots-clés qui ne sont pas autorisés dans le champ.
3. **Aperçu du modèle**:
* Affiche un aperçu en temps réel de l'apparence du document en fonction de la configuration de mise en page actuelle. Cela aide à garantir que la mise en page correspond à la structure réelle du document et est essentiel pour tester et affiner la configuration de traitement du document.

{% @jira/embed url="https://fellowpro.atlassian.net/browse/DOCB-2490" %}
