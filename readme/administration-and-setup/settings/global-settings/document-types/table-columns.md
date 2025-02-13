# Colonnes de Tableau

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 08.57.49.png" alt=""><figcaption></figcaption></figure>

#### Aperçu

L'interface des Colonnes de Tableau dans Docbits est utilisée pour spécifier les colonnes qui apparaissent dans les tableaux de données pour chaque type de document. Chaque colonne peut être configurée pour contenir des types spécifiques de données, telles que des chaînes de caractères ou des valeurs numériques, et peut être essentielle pour les fonctions de tri, de filtrage et de reporting au sein de Docbits.

#### Fonctionnalités Clés et Options

1. **Configuration de la Colonne**:
* **Nom de la Colonne**: L'identifiant de la colonne dans la base de données.
* **Titre**: Le titre lisible par l'homme de la colonne qui apparaîtra dans l'interface.
* **Type de Colonne**: Définit le type de données de la colonne (par exemple, STRING, MONTANT), ce qui détermine le type de données pouvant être stockées dans la colonne.
* **Nom de la Table**: Indique à quelle table appartient la colonne, la reliant à un type de document spécifique comme INVOICE\_TABLE.
2. **Actions**:
* **Modifier**: Modifier les paramètres d'une colonne existante.
* **Supprimer**: Supprimer la colonne du tableau, ce qui est utile si les données ne sont plus nécessaires ou si la structure de données du type de document change.
3. **Ajout de Nouvelles Colonnes et Tables**:
* **Ajouter une Nouvelle Colonne de Table**: Ouvre une boîte de dialogue où vous pouvez définir une nouvelle colonne, y compris son nom, si elle est requise, son type de données et la table à laquelle elle appartient.
* **Créer une Nouvelle Table**: Permet la création d'une nouvelle table, en définissant un nom unique qui sera utilisé pour stocker des données liées à un ensemble spécifique de types de documents.

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 08.58.01.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 08.58.11.png" alt=""><figcaption></figcaption></figure>

Cette section est essentielle pour maintenir l'intégrité structurelle et la facilité d'utilisation des données dans le système Docbits, en veillant à ce que les données extraites des documents soient stockées de manière bien organisée et accessible.

{% @jira/embed url="https://fellowpro.atlassian.net/browse/DOCB-2493" %}
