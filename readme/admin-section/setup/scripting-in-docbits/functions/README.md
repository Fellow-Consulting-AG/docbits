# Fonctions

## Fonctions

**Documentation Fonctionnelle**

Ce module contient des fonctions pour manipuler les données de document et effectuer diverses opérations liées aux champs de document.

**Fonctions**

1. **set\_field\_value(document\_data, field\_name, value)**
   * Description: Définit la valeur d'un champ dans les données du document.
   * Paramètres:
     * document\_data (dict): Les données du document contenant des informations sur les champs.
     * field\_name (str): Le nom du champ à définir.
     * value: La valeur à définir pour le champ.
   *   [Exemple:](example-scripts.md#set_field_value-document_data-field_name-value)

       ```
       set_field_value(document_data, "name", "John Doe")
       ```
2. **set\_date\_value(document\_data, field\_name, value, add\_days=0, skip\_weekend=False)**
   * Description: Définit la valeur d'un champ de date dans les données du document.
   * Paramètres:
     * document\_data (dict): Les données du document contenant des informations sur les champs.
     * field\_name (str): Le nom du champ de date à définir.
     * value: La valeur de date à définir au format ISO (par exemple, "2020-12-31").
     * add\_days (int): Ajoute des jours supplémentaires à la date donnée.
     * skip\_weekend (bool): Ignore la date si elle tombe le week-end.
   *   [Exemple:](example-scripts.md#set_date_value-document_data-field_name-value-add_days-0-skip_weekend-false)

       ```
       set_date_value(document_data, "promised_delivery_date", "2020-12-31", add_days=2, skip_weekend=True)
       ```
3. **set\_amount\_value(document\_data, field\_name, value)**
   * Description: Définit la valeur d'un champ de montant dans les données du document.
   * Paramètres:
     * document\_data (dict): Les données du document contenant des informations sur les champs.
     * field\_name (str): Le nom du champ à définir.
     * value: La valeur à définir pour le champ.
   *   [Exemple:](example-scripts.md#set_amount_value-document_data-field_name-value)

       ```
       set_amount_value(document_data, "number", "123456")
       ```
4. **get\_field\_value(document\_data, field\_name, default\_value=None, is\_clean=False)**
   * Description: Obtient la valeur d'un champ à partir des données du document.
   * Paramètres:
     * document\_data (dict): Les données du document contenant des informations sur les champs.
     * field\_name (str): Le nom du champ à définir.
     * default\_value (optionnel): Renvoie default\_value si aucune valeur de champ n'est trouvée.
     * is\_clean (optionnel): Met la valeur en majuscules et la nettoie des espaces vides.
   * Renvoie:
     * Valeur du champ.
   *   [Exemple:](example-scripts.md#get_field_value-document_data-field_name-default_value-none-is_clean-false)

       ```
       value = get_field_value(document_data, "name")
       ```
5. **create\_new\_field(field\_name, value="")**
   * Description: Crée un nouveau champ avec le nom et la valeur spécifiés.
   * Paramètres:
     * field\_name (str): Le nom du champ à créer.
     * value: La valeur initiale pour le champ (par défaut, une chaîne vide).
   * Renvoie:
     * Dictionnaire du nouveau champ créé.
   *   [Exemple:](example-scripts.md#create_new_field-field_name-value)

       ```
       dict = create_new_field("address", "")
       ```
6. **delete\_field(document\_data, field\_name)**
   * Description: Supprime un champ des données du document.
   * Paramètres:
     * document\_data (dict): Les données du document contenant des informations sur les champs.
     * field\_name (str): Le nom du champ à définir.
   * Renvoie:
     * Document\_data au format json et au format dict après la suppression du champ.
   *   [Exemple:](example-scripts.md#delete_field-document_data-field_name)

       ```
       json, dict = (document_data, "name")
       ```
7. **set\_is\_required(document\_data, field\_name, value)**
   * Description: Définit l'attribut 'is\_required' d'un champ dans les données du document.
   * Paramètres:
     * document\_data (dict): Les données du document contenant des informations sur les champs.
     * field\_name (str): Le nom du champ à définir.
     * value: La valeur à définir pour le champ.
   *   [Exemple:](example-scripts.md#set_is_required-document_data-field_name-value)

       ```
       set_is_required(document_data, "bank_id", True)
       ```
8. **set\_force\_validation(document\_data, field\_name, value)**
   * Description: Définit l'attribut 'force\_validation' d'un champ dans les données du document.
   * Paramètres:
     * document\_data (dict): Les données du document contenant des informations sur les champs.
     * field\_name (str): Le nom du champ à définir.
     * value (bool): La valeur à définir pour le champ.
   *   [Exemple:](example-scripts.md#set_force_validation-document_data-field_name-value)

       ```
       set_force_validation(document_data, 'supplier_name', True)
       ```
9. **set\_field\_as\_invalid(document\_data, field\_name, message, code=None)**
   * Description: Marque un champ comme invalide dans les données du document.
   * Paramètres:
     * document\_data (dict): Les données du document contenant des informations sur les champs.
     * field\_name (str): Le nom du champ à marquer comme invalide.
     * message (str): Le message de validation pour le champ.
     * code (optionnel): Code d'erreur pour la validation (par défaut, None).
   *   [Exemple:](example-scripts.md#set_field_as_invalid-document_data-field_name-message-code-none)

       ```
       set_field_as_invalid(document_data, "email", "Format d'email invalide", "EMAIL_FORMAT_INVALID")
       ```
10. **set\_field\_attribute(document\_data, field\_name, attribute\_name, value)**
    * Description: Définit un attribut personnalisé d'un champ dans les données du document.
    * Paramètres:
      * document\_data (str): Les données du document contenant des informations sur les champs.
      * field\_name (str): Le nom du champ à définir.
      * attribute\_name (str): Le nom de l'attribut à définir.
      * value (bool): La valeur à définir pour l'attribut.
    *   [Exemple:](example-scripts.md#set_field_attribute-document_data-field_name-attribute_name-value)

        ```
        set_field_attribute(document_data, "address", "is_verified", True)
        ```
11. **is\_supplier\_valid(use: UserAuthentication, filter\_data\_json, sub\_org\_id=None)**
    * Description: Vérifie si un fournisseur est valide en fonction des critères fournis.
    * Paramètres:
      * user (UserAuthentication): L'utilisateur authentifié.
      * filter\_data\_json: Critères de filtrage pour valider le fournisseur.
      * sub\_org\_id (optionnel): ID de sous-organisation optionnel pour le filtrage.
    * Renvoie:
      * True, si l'utilisateur est valide.
      * False si l'utilisateur n'est pas valide.
    *   [Exemple:](example-scripts.md#is_supplier_valid-user-userauthentication-filter_data_json-sub_org_id-none)

        ```
        bool = is_supplier_valid(user, {"name: "Supplier Inc."})
        ```
12. **get\_document\_content(document\_data)**
    * Description: Renvoie le contenu du document basé sur les données du document.
    * Paramètres:
      * document\_data (str): Les données du document contenant des informations sur les champs.
    * Renvoie:
      * Contenu du document des données du document.
    *   [Exemple:](example-scripts.md#get_document_content-document_data)

        ```
        document_content = get_document_content(doc)
        ```
13. **update\_document\_status\_with\_doc\_id(doc\_id, user, org\_id, status, message=None, doc\_classification\_class=None)**
    * Description: Met à jour le statut d'un document avec l'ID spécifié.
    * Paramètres:
      * doc\_id (str): L'ID du document à mettre à jour.
      * user: L'utilisateur effectuant la mise à jour (soit l'ID de l'utilisateur, soit l'objet UserAuthentication).
      * org\_id: L'ID de l'organisation à laquelle appartient le document.
      * status (str): Le nouveau statut du document.
      * message: Message optionnel associé à la mise à jour du statut.
      * doc\_classification\_class: Classe de classification de document optionnelle.
    *   [Exemple:](example-scripts.md#update_document_status_with_doc_id-doc_id-user-org_id-status-message-none-doc_classification_class-n)

        ```
        update_document_status_with_doc_id("123456", user, "org_id", "approved", "Document approuvé")
        ```
14. **get\_lov\_values(org\_id, key, return\_type="list\_of\_objects", sub\_org\_id=None)**
    * Description: Obtient les valeurs LOV à partir d'un org\_id spécifique.
    * Paramètres:
      * org\_id: L'ID de l'organisation à laquelle appartient le document.
      * return\_type (optionnel): Le type dans lequel les données doivent être renvoyées.
      * sub\_org\_id (optionnel): ID de sous-organisation optionnel pour le filtrage.
    * Renvoie:
      * Valeurs LOV sous forme de liste d'objets ou sous forme de liste.
    *   [Exemple:](example-scripts.md#get_lov_values-org_id-key-return_type-list_of_objects-sub_org_id-none)

        ```
        supplier_to_check = get_lov_values(org_id, 'BlacklistSupplier', return_type="list_of_values")
        ```
15. **format\_decimal\_to\_locale(value, to\_locale="en\_US.UTF-8", max\_decimal\_places=4, min\_decimal\_places=2)**
    * Description: Formate une valeur décimale au format en\_US.UTF-8.
    * Paramètres:
      * value: La valeur qui doit être formatée.
      * to\_locale (optionnel): Le format dans lequel la valeur doit être transformée.
      * max\_decimal\_places (optionnel): Le maximum de décimales à considérer.
      * min\_decimal\_places (optionnel): Le minimum de décimales à considérer.
    * Renvoie:
      * La valeur formatée.
    *   [Exemple:](example-scripts.md#format_decimal_to_locale-value-to_locale-en_us.utf-8-max_decimal_places-4-min_decimal_places-2)

        ```
        formatted_value = format_decimal_to_locale(value, document_json['amount_format_locale'])
        ```
16. **compare\_values(value1, value2)**
    * Description: Compare deux valeurs pour l'égalité, en gérant divers types de données.
    * Paramètres:
      * value1: La première valeur à comparer.
      * value2: La deuxième valeur à comparer.
    * Renvoie:
      * True si les valeurs sont égales et False si elles diffèrent.
    *   [Exemple:](example-scripts.md#compare_values-value1-value2)

        ```
        result = compare_values(10, "10")
        ```
17. **create\_document\_task( user, document\_data, title, description, priority,**\
    **assigned\_to\_user\_id, assigned\_to\_group\_id, send\_emai: bool)**
    * Description: Crée une tâche de document.
    * Paramètres:
      * user: L'utilisateur effectuant la mise à jour (soit l'ID de l'utilisateur, soit l'objet UserAuthentication).
      * document\_data: Les données du document contenant des informations sur les champs.
      * title (str): Le titre de la tâche.
      * description (str): La description de la tâche.
      * priority: La priorité de la tâche.
      * assigned\_to\_user\_id: L'ID de l'utilisateur auquel la tâche doit être assignée.
      * assigned\_to\_group\_id: L'ID du groupe auquel la tâche doit être assignée.
      * send\_email (bool): Détermine si un email doit être envoyé ou non.
    * Renvoie:
      * Dict indiquant si le processus a été réussi ou non.
    *   [Exemple:](example-scripts.md#create_document_task-user-document_data-title-description-priority-assigned_to_user_id-assigned_to_g)

        ```
        dict = create_document_task(user, document_data, "Pays d'origine en dehors de l'UE", "La confirmation vient d'un pays en dehors de l'UE. Veuillez joindre le document MRN.", "high", 1007, None, False)
        ```
18. **set\_document\_sub\_org\_id(document\_data, sub\_org\_id)**
    * Description: Définit le sub\_org\_id des données de document spécifiées.
    * Paramètres:
      * document\_data: Les données du document contenant des informations sur les champs.
      * sub\_org\_id (str): ID de sous-organisation optionnel pour le filtrage.
    *   [Exemple:](example-scripts.md#set_document_sub_org_id-document_data-sub_org_id)

        ```
        set_document_sub_org_id(document_data, sub_org_id)
        ```
19. **get\_user\_by\_id(user\_id)**
    * Description: Obtient l'utilisateur avec l'ID utilisateur correspondant.
    * Paramètres:
      * user\_id (str): L'ID de l'utilisateur.
    * Renvoie:
      * L'utilisateur avec l'ID utilisateur correspondant.
    *   [Exemple:](example-scripts.md#get_user_by_id-user_id)

        ```
        user = get_user_by_id("123456")
        ```
20. **get\_group\_by\_id(group\_id)**
    * Description: Obtient le groupe avec l'ID de groupe correspondant.
    * Paramètres:
      * group\_id (str): L'ID du groupe.
    * Renvoie:
      * Le groupe avec l'ID de groupe correspondant.
    *   [Exemple:](example-scripts.md#get_group_by_id-group_id)

        ```
        group = get_group_by_id("123456")
        ```
21. **add\_table\_column(table, col\_name, default\_value=None)**
    * Description: Ajoute une colonne à la table correspondante.
    * Paramètres:
      * table: La table où la colonne doit être ajoutée.
      * col\_name: Le nom de la colonne.
      * default\_value (optionnel): La valeur initiale pour le champ (par défaut, une chaîne vide).
    *   [Exemple:](example-scripts.md#add_table_column-table-col_name-default_value-none)

        ```
        add_table_column(table, "UNIT_PRICE_PER")
        ```
22. **get\_column\_value(row, column\_name, default\_value=None, is\_clean=False)**
    * Description: Obtient une valeur d'une colonne spécifiée.
    * Paramètres:
      * row: La ligne où la valeur est située.
      * col\_name: Le nom de la colonne.
      * default\_value (optionnel): Renvoie default\_value si aucune valeur de champ n'est trouvée.
      * is\_clean (optionnel): Met la valeur en majuscules et la nettoie des espaces vides.
    *   [Exemple:](example-scripts.md#get_column_value-row-column_name-default_value-none-is_clean-false)

        ```
        original_unit_price = get_column_value(row, "ORIGINAL_UNIT_PRICE")
        ```
23. **set\_column\_value(row, column\_name, value)**
    * Description: Définit une valeur d'une colonne spécifiée.
    * Paramètres:
      * row: La ligne où la valeur est située.
      * col\_name: Le nom de la colonne.
      * value: La valeur qui sera définie à l'emplacement spécifié.
    * Renvoie:
      * True si le changement a été réussi.
    *   [Exemple:](example-scripts.md#set_column_value-row-column_name-value)

        ```
        success = set_column_value(row,"SUPPLIER_ID", supplier_id)
        ```
24. **set\_column\_date\_value(document\_data, row, column\_name, value, add\_days=0)**
    * Description: Définit une valeur d'une colonne spécifiée.
    * Paramètres:
      * document\_data: Les données du document contenant des informations sur les champs.
      * row: La ligne où la valeur est située.
      * col\_name: Le nom de la colonne.
      * value: La valeur de date à définir au format ISO (par exemple, "2020-12-31").
      * add\_days (int): Ajoute des jours supplémentaires à la date donnée.
    *   [Exemple:](example-scripts.md#set_column_date_value-document_data-row-column_name-value-add_days-0)

        ```
        set_column_date_value(document_data, row, "DELIVERY_DATE", "2020-12-31", add_days=2)
        ```
25. **set\_column\_amount\_value(document\_data, row, column\_name, value)**
    * Description: Effectue les actions suivantes:
      * Convertit la valeur en chaîne et définit la valeur pour la colonne.
      * Définit le contenu de la colonne sur la valeur.
      * Formate la valeur selon la locale.
    * Paramètres:
      * document\_data (dict): Les données du document contenant des informations sur les champs.
      * row: Ligne de la table.
      * column\_name: Nom de la colonne.
      * value: Valeur à définir.
    *   [Exemple:](example-scripts.md#set_column_amount_value-document_data-row-column_name-value)

        ```
        set_column_amount_value(document_data, row, "UNIT_PRICE", str(unit_price))
        ```
26. **remove\_rows\_from\_table(document\_data, table\_name, count, start)**
    * Description: Supprime des lignes de la table spécifiée.
    * Paramètres:
      * document\_data (dict): Les données du document contenant des informations sur les champs.
      * table\_name: Le nom de la table.
      * count: Combien de lignes doivent être supprimées.
      * start: Le point de départ.
    *   [Exemple:](example-scripts.md#remove_rows_from_table-document_data-table_name-count-start)

        ```
        remove_rows_from_table(document_data,"INVOICE_TABLE",count,start)   
        ```
27. **remove\_all\_rows\_except\_one\_from\_table(document\_data, line\_number)**
    * Description: Supprime toutes les lignes sauf une de la table spécifiée.
    * Paramètres:
      * document\_data (dict): Les données du document contenant des informations sur les champs.
      * line\_number: Le numéro de la ligne qui ne doit pas être supprimée.
    *   [Exemple:](example-scripts.md#remove_all_rows_except_one_from_table-document_data-line_number)

        ```
        remove_all_rows_except_one_from_table(document_data, line_number) 
        ```

Vous pouvez également utiliser certaines des fonctions intégrées de Python:

* abs(): Renvoie la valeur absolue d'un nombre.
* len(): Renvoie la longueur (nombre d'éléments) d'un objet, comme une liste ou une chaîne.
* isinstance(): Vérifie si un objet est une instance d'une classe ou d'un type particulier.
* print(): Imprime la sortie sur la console.
* round(): Arrondit un nombre à virgule flottante à un nombre spécifié de décimales.
* str\_to\_bool(): Convertit une chaîne en une valeur booléenne (True ou False).
* type(): Renvoie le type d'un objet.
* dict(): Crée un objet dictionnaire.
* list(): Crée un objet liste.
* str(): Convertit une valeur en chaîne.
* float(): Convertit une valeur en nombre à virgule flottante.
* int(): Convertit une valeur en entier.

Pour plus de détails, consultez la documentation officielle de Python: [Fonctions intégrées](http://docs.python.org/3.12/library/functions.html).

#### Fonctions de la classe String

Vous pouvez également utiliser ces fonctions spécifiquement pour travailler avec des chaînes:

* lower(): Convertit tous les caractères d'une chaîne en minuscules.
* upper(): Convertit tous les caractères d'une chaîne en majuscules.
* split(): Divise une chaîne en une liste en fonction d'un délimiteur (par exemple, espace ou virgule).
* startswith(): Vérifie si une chaîne commence par un préfixe spécifié.
* endswith(): Vérifie si une chaîne se termine par un suffixe spécifié.
* strip(): Supprime les espaces vides au début ou à la fin d'une chaîne.

#### Fonctions du module Math de Python

Ces fonctions font partie du module math et sont utiles pour les opérations mathématiques:

* floor(): Renvoie le plus grand entier inférieur ou égal à un nombre donné.
* ceil(): Renvoie le plus petit entier supérieur ou égal à un nombre donné.

Pour plus d'informations, consultez la documentation officielle de Python: [Fonctions du module Math](http://docs.python.org/3/library/math.html).

#### Fonction d'expression régulière

* re.search(): Recherche un motif dans une chaîne et renvoie la première correspondance.

Voir plus de détails ici: [Documentation re.search](http://docs.python.org/3/library/re.html#re.search).

#### Fonctions externes

Voici quelques fonctions utiles provenant de bibliothèques externes:

* deepcopy(): Crée une copie d'un objet, y compris des objets imbriqués (du module copy).\
  [Documentation Deepcopy](http://docs.python.org/3/library/copy.html#copy.deepcopy).
* levenshtein\_distance(): Calcule le nombre d'éditions (insertions, suppressions, substitutions) nécessaires pour transformer une chaîne en une autre. Cette fonction est disponible dans la [bibliothèque Jellyfish](http://jamesturk.github.io/jellyfish/functions/).

#### Fonctions de date et d'heure

Vous pouvez utiliser les fonctions suivantes pour travailler avec des dates et des heures:

* strptime(): Convertit une chaîne en un objet datetime basé sur un format spécifié.
* strftime(): Formate un objet datetime en une chaîne basée sur un format spécifié.

Pour plus d'informations, consultez la documentation officielle:\
[Fonctions de date et d'heure](http://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior).

## Scripts d'exemple
