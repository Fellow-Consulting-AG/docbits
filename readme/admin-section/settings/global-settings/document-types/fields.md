# Champs

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 09.02.31.png" alt=""><figcaption></figcaption></figure>

#### Aperçu

Le paramètre Champs fournit une interface utilisateur où les administrateurs peuvent gérer les propriétés et le comportement des champs de données individuels associés à un type de document. Chaque champ peut être ajusté pour optimiser la précision et l'efficacité de la capture et de la validation des données.

#### Fonctionnalités clés et Options

1. **Configuration des Champs**:
* **Noms des Champs**: Liste les noms des champs, correspondant généralement aux éléments de données dans le document, tels que "Numéro de Facture" ou "Date de Commande".
* **Requis**: Les administrateurs peuvent marquer les champs comme requis, s'assurant que des données doivent être saisies ou capturées pour que ces champs complètent le traitement du document.
* **Lecture Seule**: Les champs peuvent être définis en lecture seule pour empêcher toute modification après la capture des données ou pendant certaines étapes du traitement du document.
* **Caché**: Les champs peuvent être masqués dans l'interface utilisateur, utile pour les informations sensibles ou pour simplifier les flux de travail des utilisateurs.
2. **Paramètres Avancés**:
* **Forcer la Validation**: Garantit que les données saisies dans un champ respectent certaines règles de validation avant d'être acceptées.
* **OCR (Reconnaissance Optique de Caractères)**: Ce commutateur peut être activé pour permettre le traitement OCR pour un champ spécifique, utile pour l'extraction automatique de données à partir de documents numérisés ou numériques.
* **Score de Correspondance**: Les administrateurs peuvent définir un score de correspondance, un seuil utilisé pour déterminer le niveau de confiance de la reconnaissance ou de la correspondance des données, impactant la manière dont la validation des données et les contrôles de qualité sont effectués.
3. **Boutons d'Action**:
* **Créer un Nouveau Champ**: Permet d'ajouter de nouveaux champs au type de document.
* **Icônes d'Édition**: Chaque champ a une icône d'édition qui permet aux administrateurs de configurer davantage les paramètres spécifiques au champ, tels que le type de données, les valeurs par défaut ou la logique métier connectée.
* **Enregistrer les Paramètres**: Valide les modifications apportées aux configurations des champs.

{% @jira/embed url="https://fellowpro.atlassian.net/browse/DOCB-2494" %}
