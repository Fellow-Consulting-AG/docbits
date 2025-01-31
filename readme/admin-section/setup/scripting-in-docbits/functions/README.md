# Fonctions

**Documentation Fonctionnelle**

Ce module contient des fonctions pour manipuler les données de document et effectuer diverses opérations liées aux champs de document.

**Fonctions**

1. **set\_field\_value(document\_data, field\_name, value)**
   * Description : Définit la valeur d'un champ dans les données du document.
   * Paramètres :
     * document\_data (dict) : Les données du document contenant des informations sur les champs.
     * field\_name (str) : Le nom du champ à définir.
     * value : La valeur à définir pour le champ.
   *   Exemple :

       ```
       set_field_value(document_data, "name", "John Doe")
       ```
2. **set\_date\_value(document\_data, field\_name, value, add\_days=0, skip\_weekend=False)**
   * Description : Définit la valeur d'un champ de date dans les données du document.
   * Paramètres :
     * document\_data (dict) : Les données du document contenant des informations sur les champs.
     * field\_name (str) : Le nom du champ de date à définir.
     * value : La valeur de date à définir au format ISO (par exemple, "2020-12-31").
     * add\_days (int) : Ajoute des jours supplémentaires à la date donnée.
     * skip\_weekend (bool) : Ignore la date si elle tombe le week-end.
   *   Exemple :

       ```
       set_date_value(document_data, "promised_delivery_date", "2020-12-31", add_days=2, skip_weekend=True)
       ```
3. **set\_amount\_value(document\_data, field\_name, value)**
   * Description : Définit la valeur d'un champ de montant dans les données du document.
   * Paramètres :
     * document\_data (dict) : Les données du document contenant des informations sur les champs.
     * field\_name (str) : Le nom du champ à définir.
     * value : La valeur à définir pour le champ.
   *   Exemple :

       ```
       set_amount_value(document_data, "number", "123456")
       ```
4. **get\_field\_value(document\_data, field\_name, default\_value=None, is\_clean=False)**
   * Description : Obtient la valeur d'un champ à partir des données du document.
   * Paramètres :
     * document\_data (dict) : Les données du document contenant des informations sur les champs.
     * field\_name (str) : Le nom du champ à définir.
     * default\_value (optionnel) : Renvoie default\_value si aucune valeur de champ n'est trouvée.
     * is\_clean (optionnel) : Met la valeur en majuscules et la nettoie des espaces vides.
   * Renvoie :
     * Valeur du champ.
   *   Exemple :

       ```
       value = get_field_value(document_data, "name")
       ```
5. **create\_new\_field(field\_name, value="")**
   * Description : Crée un nouveau champ avec le nom et la valeur spécifiés.
   * Paramètres :
     * field\_name (str) : Le nom du champ à créer.
     * value : La valeur initiale pour le champ (par défaut, une chaîne vide).
   * Renvoie :
     * Dictionnaire du nouveau champ créé.
   *   Exemple :

       ```
       dict = create_new_field("address", "")
       ```
6. **delete\_field(document\_data, field\_name)**
   * Description : Supprime un champ des données du document.
   * Paramètres :
     * document\_data (dict) : Les données du document contenant des informations sur les champs.
     * field\_name (str) : Le nom du champ à définir.
   * Renvoie :
     * Document\_data au format json et au format dict après la suppression du champ.
   *   Exemple :

       ```
       //json, dict = (document_data, "name")
       ```
7. **set\_is\_required(document\_data, field\_name, value)**
   * Description : Définit l'attribut 'is\_required' d'un champ dans les données du document.
   * Paramètres :
     * document\_data (dict) : Les données du document contenant des informations sur les champs.
     * field\_name (str) : Le nom du champ à définir.
     * value : La valeur à définir pour le champ.
   *   Exemple :

       ```
       set_is_required(document_data, "bank_id", True)
       ```
8. **set\_force\_validation(document\_data, field\_name, value)**
   * Description : Définit l'attribut 'force\_validation' d'un champ dans les données du document.
   * Paramètres :
     * document\_data (dict) : Les données du document contenant des informations sur les champs.
     * field\_name (str) : Le nom du champ à définir.
     * value (bool) : La valeur à définir pour le champ.
   *   Exemple :

       ```
       set_force_validation(document_data, 'supplier_name', True)
       ```
9. **set\_field\_as\_invalid(document\_data, field\_name, message, code=None)**
   * Description : Marque un champ comme invalide dans les données du document.
   * Paramètres :
     * document\_data (dict) : Les données du document contenant des informations sur les champs.
     * field\_name (str) : Le nom du champ à marquer comme invalide.
     * message (str) : Le message de validation pour le champ.
     * code (optionnel) : Code d'erreur pour la validation (par défaut, None).
   *   Exemple :

       ```
       --set_field_as_invalid(document_data, "email", "Format d'email invalide", "EMAIL_FORMAT_INVALID")
       ```
10. **set\_field\_attribute(document\_data, field\_name, attribute\_name, value)**
    * Description : Définit un attribut personnalisé d'un champ dans les données du document.
    * Paramètres :
      * document\_data (str) : Les données du document contenant des informations sur les champs.
      * field\_name (str) : Le nom du champ à définir.
      * attribute\_name (str) : Le nom de l'attribut à définir.
      * value (bool) : La valeur à définir pour l'attribut.
    *   Exemple :

        ```
        set_field_attribute(document_data, "address", "is_verified", True)
        ```
11. **is\_supplier\_valid(user: UserAuthentication, filter\_data\_json, sub\_org\_id=None)**
    * Description : Vérifie si un fournisseur est valide en fonction des critères fournis.
    * Paramètres :
      * user (UserAuthentication) : L'utilisateur authentifié.
      * filter\_data\_json : Critères de filtrage pour valider le fournisseur.
      * sub\_org\_id (optionnel) : ID d'organisation secondaire optionnel pour le filtrage.
    * Renvoie :
      * True, si l'utilisateur est valide.
      * False si l'utilisateur n'est pas valide.
    *   Exemple :

        ```
        bool = is_supplier_valid(user, {"name": "Supplier Inc."})
        ```
12. **get\_document\_content(document\_data)**
    * Description : Renvoie le contenu du document basé sur les données du document.
    * Paramètres :
      * document\_data (str) : Les données du document contenant des informations sur les champs.
    * Renvoie :
      * Contenu du document des données du document.
    *   Exemple :

        ```
        document_content = get_document_content(doc)
        ```
13. **update\_document\_status\_with\_doc\_id(doc\_id, user, org\_id, status, message=None, doc\_classification\_class=None)**
    * Description : Met à jour le statut d'un document avec l'ID spécifié.
    * Paramètres :
      * doc\_id (str) : L'ID du document à mettre à jour.
      * user : L'utilisateur effectuant la mise à jour (soit l'ID de l'utilisateur, soit l'objet UserAuthentication).
      * org\_id : L'ID de l'organisation à laquelle appartient le document.
      * status (str) : Le nouveau statut du document.
      * message : Message optionnel associé à la mise à jour du statut.
      * doc\_classification\_class : Classe de classification de document optionnelle.
    *   Exemple :

        ```
        update_document_status_with_doc_id("123456", user, "org_id", "approved", "Document approuvé")
        ```
14. **get\_lov\_values(org\_id, key, return\_type="list\_of\_objects", sub\_org\_id=None)**
    * Description : Obtient les valeurs LOV à partir d'un org\_id spécifique.
    * Paramètres :
      * org\_id : L'ID de l'organisation à laquelle appartient le document.
      * return\_type (optionnel) : Le type dans lequel les données doivent être renvoyées.
      * sub\_org\_id (optionnel) : ID d'organisation secondaire optionnel pour le filtrage.
    * Renvoie :
      * Valeurs LOV sous forme de liste d'objets ou sous forme de liste.
    *   Exemple :

        ```
        supplier_to_check = get_lov_values(org_id, 'BlacklistSupplier', return_type="list_of_values")
        ```
15. **format\_decimal\_to\_locale(value, to\_locale="en\_US.UTF-8", max\_decimal\_places=4, min\_decimal\_places=2)**
    * Description : Formate une valeur décimale au format en\_US.UTF-8.
    * Paramètres :
      * value : La valeur qui doit être formatée.
      * to\_locale (optionnel) : Le format dans lequel la valeur doit être transformée.
      * max\_decimal\_places (optionnel) : Le maximum de décimales à considérer.
      * min\_decimal\_places (optionnel) : Le minimum de décimales à considérer.
    * Renvoie :
      * La valeur formatée.
    *   Exemple :

        ```
        formatted_value = format_decimal_to_locale(value, document_json['amount_format_locale'])
        ```
16. **compare\_values(value1, value2)**
    * Description : Compare deux valeurs pour l'égalité, en gérant divers types de données.
    * Paramètres :
      * value1 : La première valeur à comparer.
      * value2 : La deuxième valeur à comparer.
    * Renvoie :
      * True si les valeurs sont égales et False si elles diffèrent.
    *   Exemple :

        ```
        result = compare_values(10, "10")
        ```
17. **create\_document\_task( user, document\_data, title, description, priority,**\
    **assigned\_to\_user\_id, assigned\_to\_group\_id, send\_email: bool)**
    * Description : Crée une tâche de document.
    * Paramètres :
      * user : L'utilisateur effectuant la mise à jour (soit l'ID de l'utilisateur, soit l'objet UserAuthentication).
      * document\_data : Les données du document contenant des informations sur les champs.
      * title (str) : Le titre de la tâche.
      * description (str) : La description de la tâche.
      * priority : La priorité de la tâche.
      * assigned\_to\_user\_id : L'ID de l'utilisateur auquel la tâche doit être assignée.
      * assigned\_to\_group\_id : L'ID du groupe auquel la tâche doit être assignée.
      * send\_email (bool) : Détermine si un email doit être envoyé ou non.
    * Renvoie :
      * Dict indiquant si le processus a réussi ou non.
    *   Exemple :

        ```
        dict = create_document_task(user, document_data, "Pays d'origine en dehors de l'UE", "La confirmation vient d'un pays en dehors de l'UE. Veuillez joindre le document MRN.", "élevé", 1007, None, False)
        ```
18. **set\_document\_sub\_org\_id(document\_data, sub\_org\_id)**
    * Description : Définit le sub\_org\_id des données de document spécifiées.
    * Paramètres :
      * document\_data : Les données du document contenant des informations sur les champs.
      * sub\_org\_id (str) : ID d'organisation secondaire optionnel pour le filtrage.
    *   Exemple :

        ```
        set_document_sub_org_id(document_data, sub_org_id)
        ```
19. **get\_user\_by\_id(user\_id)**
    * Description : Obtient l'utilisateur avec l'ID d'utilisateur correspondant.
    * Paramètres :
      * user\_id (str) : L'ID de l'utilisateur.
    * Renvoie :
      * L'utilisateur avec l'ID d'utilisateur correspondant.
    *   Exemple :

        ```
        user = get_user_by_id("123456")
        ```
20. **get\_group\_by\_id(group\_id)**
    * Description : Obtient le groupe avec l'ID de groupe correspondant.
    * Paramètres :
      * group\_id (str) : L'ID du groupe.
    * Renvoie :
      * Le groupe avec l'ID de groupe correspondant.
    *   Exemple :

        ```
        group = get_group_by_id("123456")
        ```
21. **add\_table\_column(table, col\_name, default\_value=None)**
    * Description : Ajoute une colonne à la table correspondante.
    * Paramètres :
      * table : La table où la colonne doit être ajoutée.
      * col\_name : Le nom de la colonne.
      * default\_value (optionnel) : La valeur initiale pour le champ (par défaut, une chaîne vide).
    *   Exemple :

        ```
        add_table_column(table, "UNIT_PRICE_PER")
        ```
22. **get\_column\_value(row, column\_name, default\_value=None, is\_clean=False)**
    * Description : Obtient une valeur d'une colonne spécifiée.
    * Paramètres :
      * row : La ligne où la valeur est située.
      * col\_name : Le nom de la colonne.
      * default\_value (optionnel) : Renvoie default\_value si aucune valeur de champ n'est trouvée.
      * is\_clean (optionnel) : Met la valeur en majuscules et la nettoie des espaces vides.
    *   Exemple :

        ```
        original_unit_price = get_column_value(row, "ORIGINAL_UNIT_PRICE")
        ```
23. **set\_column\_value(row, column\_name, value)**
    * Description : Définit une valeur d'une colonne spécifiée.
    * Paramètres :
      * row : La ligne où la valeur est située.
      * col\_name : Le nom de la colonne.
      * value : La valeur qui sera définie à l'emplacement spécifié.
    * Renvoie :
      * True si le changement a réussi.
    *   Exemple :

        ```
        success = set_column_value(row,"SUPPLIER_ID", supplier_id)
        ```
24. **set\_column\_date\_value(document\_data, row, column\_name, value, add\_days=0)**
    * Description : Définit une valeur d'une colonne spécifiée.
    * Paramètres :
      * document\_data : Les données du document contenant des informations sur les champs.
      * row : La ligne où la valeur est située.
      * col\_name : Le nom de la colonne.
      * value : La valeur de date à définir au format ISO (par exemple, "2020-12-31").
      * add\_days (int) : Ajoute des jours supplémentaires à la date donnée.
    *   Exemple :

        ```
        set_column_date_value(document_data, row, "DELIVERY_DATE", "2020-12-31", add_days=2)
        ```
25. **set\_column\_amount\_value(document\_data, row, column\_name, value)**
    * Description : Effectue les actions suivantes :
      * Convertit la valeur en chaîne et définit la valeur pour la colonne.
      * Définit le contenu de la colonne à la valeur.
      * Formate la valeur selon la locale.
    * Paramètres :
      * document\_data (dict) : Les données du document contenant des informations sur les champs.
      * row : Ligne de la ligne de la table.
      * column\_name : Nom de la colonne.
      * value : Valeur à définir.
    *   Exemple :

        ```
        set_column_amount_value(document_data, row, "UNIT_PRICE", str(unit_price))
        ```
26. **remove\_rows\_from\_table(document\_data, table\_name, count, start)**
    * Description : Supprime des lignes de la table spécifiée.
    * Paramètres :
      * document\_data (dict) : Les données du document contenant des informations sur les champs.
      * table\_name : Le nom de la table.
      * count : Combien de lignes doivent être supprimées.
      * start : Le point de départ.
    *   Exemple :

        ```
        remove_rows_from_table(document_data,"INVOICE_TABLE",count,start)   
        ```
27. **remove\_all\_rows\_except\_one\_from\_table(document\_data, line\_number)**
    * Description : Supprime toutes les lignes sauf une de la table spécifiée.
    * Paramètres :
      * document\_data (dict) : Les données du document contenant des informations sur les champs.
      * line\_number : Le numéro de la ligne qui ne doit pas être supprimée.
    *   Exemple :

        ```
        remove_all_rows_except_one_from_table(document_data, line_number) 
        ```

Vous pouvez également utiliser certaines des fonctions intégrées de Python :

* abs() : Renvoie la valeur absolue d'un nombre.
* len() : Renvoie la longueur (nombre d'éléments) d'un objet, comme une liste ou une chaîne.
* isinstance() : Vérifie si un objet est une instance d'une classe ou d'un type particulier.
* print() : Affiche la sortie dans la console.
* round() : Arrondit un nombre à virgule flottante à un nombre spécifié de décimales.
* str\_to\_bool() : Convertit une chaîne en une valeur booléenne (True ou False).
* type() : Renvoie le type d'un objet.
* dict() : Crée un objet dictionnaire.
* list() : Crée un objet liste.
* str() : Convertit une valeur en chaîne.
* float() : Convertit une valeur en nombre à virgule flottante.
* int() : Convertit une valeur en entier.

Pour plus de détails, visitez la documentation officielle de Python : [Fonctions intégrées](https://docs.python.org/3.12/library/functions.html).

#### Fonctions de la classe String

Vous pouvez également utiliser ces fonctions spécifiquement pour travailler avec des chaînes :

* lower() : Convertit tous les caractères d'une chaîne en minuscules.
* upper() : Convertit tous les caractères d'une chaîne en majuscules.
* split() : Divise une chaîne en une liste en fonction d'un délimiteur (par exemple, espace ou virgule).
* startswith() : Vérifie si une chaîne commence par un préfixe spécifié.
* endswith() : Vérifie si une chaîne se termine par un suffixe spécifié.
* strip() : Supprime les espaces vides au début ou à la fin d'une chaîne.

#### Fonctions du module Math de Python

Ces fonctions font partie du module math et sont utiles pour les opérations mathématiques :

* floor() : Renvoie le plus grand entier inférieur ou égal à un nombre donné.
* ceil() : Renvoie le plus petit entier supérieur ou égal à un nombre donné.

Pour plus d'informations, consultez la documentation officielle de Python : [Fonctions du module Math](https://docs.python.org/3/library/math.html).

#### Fonction d'expression régulière

* re.search() : Recherche un motif dans une chaîne et renvoie la première correspondance.

Voir plus de détails ici : [Documentation re.search](https://docs.python.org/3/library/re.html#re.search).

#### Fonctions externes

Voici quelques fonctions utiles provenant de bibliothèques externes :

* deepcopy() : Crée une copie d'un objet, y compris des objets imbriqués (du module copy).\
  [Documentation Deepcopy](https://docs.python.org/3/library/copy.html#copy.deepcopy).
* levenshtein\_distance() : Calcule le nombre de modifications (insertions, suppressions, substitutions) nécessaires pour transformer une chaîne en une autre. Cette fonction est disponible dans la [bibliothèque Jellyfish](https://jamesturk.github.io/jellyfish/functions/).

#### Fonctions de date et d'heure

Vous pouvez utiliser les fonctions suivantes pour travailler avec des dates et des heures :

* strptime() : Convertit une chaîne en un objet datetime basé sur un format spécifié.
* strftime() : Formate un objet datetime en une chaîne basée sur un format spécifié.

Pour plus d'informations, consultez la documentation officielle :\
[Fonctions de date et d'heure](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior).
