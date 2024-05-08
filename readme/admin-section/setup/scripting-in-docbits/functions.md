# Fonctions

**Documentation fonctionnelle**

Ce module contient des fonctions pour manipuler les données de document et effectuer diverses opérations liées aux champs de document.

## **Fonctions**

1. ### **set\_field\_value(document\_data, field\_name, value)**
* Description : Définit la valeur d'un champ dans les données du document.
* Paramètres :
* `document_data` (dict) : Les données du document contenant les informations sur les champs.
* `field_name` (str) : Le nom du champ à définir.
* `value` : La valeur à définir pour le champ.
*   Exemple :

`set_field_value(document_data, "name", "John Doe")`
2. ### **set\_date\_value(document\_data, field\_name, value)**
* Description : Définit la valeur d'un champ de date dans les données du document.
* Paramètres :
* `document_data` (dict) : Les données du document contenant les informations sur les champs.
* `field_name` (str) : Le nom du champ de date à définir.
* `value` : La valeur de la date à définir au format ISO (par exemple, "2020-12-31").
*   Exemple :

`set_date_value(document_data, "date_of_birth", "1990-05-15")`
3. ### **set\_amount\_value(document\_data, field\_name, value)**
* Description : Définit la valeur d'un champ de montant dans les données du document.
* Paramètres et exemple d'utilisation similaires à `set_field_value`.
4. ### **set\_is\_required(document\_data, field\_name, value)**
* Description : Définit l'attribut 'is\_required' d'un champ dans les données du document.
* Paramètres et exemple d'utilisation similaires à `set_field_value`.
5. ### **set\_force\_validation(document\_data, field\_name, value)**
* Description : Définit l'attribut 'force\_validation' d'un champ dans les données du document.
* Paramètres et exemple d'utilisation similaires à `set_field_value`.
6. ### **set\_field\_attribute(document\_data, field\_name, attribute\_name, value)**
* Description : Définit un attribut personnalisé d'un champ dans les données du document.
* Paramètres :
* `attribute_name` (str) : Le nom de l'attribut à définir.
* `value` : La valeur à définir pour l'attribut.
*   Exemple :

`set_field_attribute(document_data, "address", "is_verified", True)`
7. ### **get\_field\_value(document\_data, field\_name, default\_value=None, is\_clean=False)**
* Description : Obtient la valeur d'un champ à partir des données du document.
* Paramètres et exemple d'utilisation similaires à `set_field_value`.
8. ### **create\_new\_field(field\_name, value="")**
* Description : Crée un nouveau champ avec le nom et la valeur spécifiés.
* Paramètres :
* `field_name` (str) : Le nom du champ à créer.
* `value` : La valeur initiale pour le champ (par défaut, une chaîne vide).
*   Exemple :

`create_new_field("address", "123 Main St")`
9. ### **delete\_field(document\_data, field\_name)**
* Description : Supprime un champ des données du document.
* Paramètres et exemple d'utilisation similaires à `set_field_value`.
10. ### **update\_document\_status\_with\_doc\_id(doc\_id, user, org\_id, status, message=None, doc\_classification\_class=None)**
* Description : Met à jour le statut d'un document avec l'ID spécifié.
* Paramètres :
* `doc_id` (str) : L'ID du document à mettre à jour.
* `user` : L'utilisateur effectuant la mise à jour (soit l'ID de l'utilisateur, soit l'objet UserAuthentication).
* `org_id` : L'ID de l'organisation à laquelle le document appartient.
* `status` (str) : Le nouveau statut du document.
* `message` : Message facultatif associé à la mise à jour du statut.
* `doc_classification_class` : Classe de classification du document facultative.
*   Exemple :

`update_document_status_with_doc_id("123456", user, org_id, "approved", "Document approved")`
11. ### **is\_supplier\_valid(user: UserAuthentication, filter\_data\_json, sub\_org\_id=None)**
* Description : Vérifie si un fournisseur est valide en fonction des critères fournis.
* Paramètres :
* `user` (UserAuthentication) : L'utilisateur authentifié.
* `filter_data_json` : Critères de filtrage pour valider le fournisseur.
* `sub_org_id` : ID de sous-organisation facultatif pour le filtrage.
*   Exemple :

`is_supplier_valid(user, {"name": "Supplier Inc."})`
12. ### **set\_field\_as\_invalid(document\_data, field\_name, message, code=None)**
* Description : Marque un champ comme invalide dans les données du document.
* Paramètres :
* `document_data` (dict) : Les données du document contenant les informations sur les champs.
* `field_name` (str) : Le nom du champ à marquer comme invalide.
* `message` (str) : Le message de validation pour le champ.
* `code` (optionnel) : Code d'erreur pour la validation (par défaut, None).
*   Exemple :

`set_field_as_invalid(document_data, "email", "Format d'email invalide", "EMAIL_FORMAT_INVALID")`
13. ### **compare\_values(value1, value2)**
* Description : Compare deux valeurs pour l'égalité, en gérant divers types de données.
* Paramètres :
* `value1` : La première valeur à comparer.
* `value2` : La deuxième valeur à comparer.
*   Exemple :

`compare_values(10, "10")`
