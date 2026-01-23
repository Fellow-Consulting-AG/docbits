# Fonctions

## **Documentation Fonctionnelle**

Ce module contient des fonctions pour manipuler les données de document et effectuer diverses opérations liées aux champs de document.

## **Fonctions**

### **set\_field\_value()**

Définit la valeur d'un champ dans les données du document.

```python
po_number = get_field_value(fields_dict, 'purchase_order', None)
if not po_number:
    po_number = ''
    
if po_number:
    set_field_value(fields_dict, "invoice_sub_type", 'Purchase Invoice')
else:
    set_field_value(fields_dict, "invoice_sub_type", 'Cost Invoice')
```

#### Paramètres :

<table><thead><tr><th width="177">Nom</th><th width="176">Type</th><th>Description</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Les données du document contenant des informations sur les champs</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Le nom du champ à définir</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>any</code></td><td>La valeur à définir pour le champ</td></tr><tr><td>remove_link (optionnel)</td><td><code>bool</code></td><td>Supprime la clé "coords" du champ.</td></tr></tbody></table>

### **set\_date\_value()**

Définit la valeur d'un champ de date dans les données du document.

```python
invoice_date = get_field_value(document_data, 'invoice_date', None)
    
if not document_json.get("script_executed", False):
    if invoice_date:
        set_date_value(document_data, "accounting_date", invoice_date)
        document_json["script_executed"] = True
```

#### Paramètres :

<table><thead><tr><th width="229">Nom</th><th width="196.0316162109375">Type</th><th>Description</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Les données du document contenant des informations sur les champs</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Le nom du champ à définir</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>string</code></td><td>La valeur de date à définir au format ISO (par exemple, "2020-12-31").</td></tr><tr><td>add_days (optionnel)</td><td><code>int</code></td><td>Ajoute des jours supplémentaires à la date donnée<br>Par défaut, c'est 0</td></tr><tr><td>skip_weekend (optionnel)</td><td><code>bool</code></td><td>Ignore la date si elle tombe le week-end<br>Par défaut, c'est <code>False</code></td></tr><tr><td>remove link (optionnel)</td><td><code>bool</code></td><td>Supprime la clé "coords" du champ.</td></tr><tr><td>exclude_final_days<br>(optionnel)</td><td>soit <code>string</code> ou <code>int</code></td><td>Spécifie les jours à exclure (0-6 ou dimanche à samedi)</td></tr></tbody></table>

### **set\_amount\_value()**

Définit la valeur d'un champ de montant dans les données du document.

```python
total_amount = get_field_value(document_data, "net_amount")
lines_total = 0.0
set_amount_value(document_data, "net_amount",str(lines_total))
```

#### Paramètres :

<table><thead><tr><th width="183.71087646484375">Nom</th><th width="176">Type</th><th>Description</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Les données du document contenant des informations sur les champs</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Le nom du champ à définir</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>string</code></td><td>La valeur à définir pour le champ (passer un nombre sous forme de chaîne par exemple, "123456")</td></tr><tr><td>remove link (optionnel)</td><td><code>bool</code></td><td>Supprime la clé "coords" du champ.</td></tr></tbody></table>

### **get\_field\_value()**

Obtient la valeur d'un champ à partir des données du document.

```python
total_amount = get_field_value(document_data, "net_amount")
lines_total = 0.0
set_amount_value(document_data, "net_amount", str(lines_total))
```

#### Paramètres :

<table><thead><tr><th width="191">Nom</th><th width="176">Type</th><th>Description</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Les données du document contenant des informations sur les champs</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Le nom du champ à définir</td></tr><tr><td>default_value (optionnel)</td><td><code>any</code></td><td>Renvoie default_value si aucune valeur de champ n'est trouvée<br>Par défaut, c'est <code>None</code></td></tr><tr><td>is_clean (optionnel)</td><td><code>bool</code></td><td>Convertit la valeur en majuscules et supprime les espaces supplémentaires<br>Par défaut, c'est <code>False</code></td></tr></tbody></table>

#### Renvoie :

* Valeur du champ spécifié

### **create\_new\_field()**

Crée un nouveau champ avec le nom et la valeur spécifiés.

```python
currency = get_field_value(document_data, 'currency', None)

if not currency:
    if 'currency' not in fields_dict:
        new_field = create_new_field('currency','')
        fields_dict['currency'] = new_field
        document_json['fields'].append(new_field)
    set_field_value(document_data, "currency", "USD")
```

#### Paramètres :

<table><thead><tr><th width="140">Nom</th><th width="133">Type</th><th>Description</th></tr></thead><tbody><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>str</code></td><td>Les données du document contenant des informations sur les champs</td></tr><tr><td>value (optionnel)</td><td><code>any</code></td><td>La valeur initiale pour le champ<br>Par défaut, c'est <code>""</code></td></tr></tbody></table>

#### Renvoie :

* Dictionnaire du nouveau champ créé

### **delete\_field()**

Supprime un champ des données du document

```python
field_amount = get_field_value(document_data, field_name)
    if not field_amount:
        delete_field(document_data, fields_dict, field_name)
    else:
        field_amount = float(field_amount)
        if field_amount == 0:
            delete_field(document_data, fields_dict, field_name)
```

#### Paramètres :

<table><thead><tr><th width="173">Nom</th><th width="176">Type</th><th>Description</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Les données du document contenant des informations sur les champs</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Le nom du champ à supprimer</td></tr></tbody></table>

#### Renvoie :

* Document\_data en json et en dict après que le champ a été supprimé

### **set\_is\_required()**

Définit l'attribut 'is\_required' d'un champ dans les données du document.

```python
net_amount = get_field_value(document_data, "net_amount", None)
if net_amount:
    set_is_required(document_data, "tax_country", True)
    set_is_required(document_data, "tax_code_without_country", True)
```

#### Paramètres :

<table><thead><tr><th width="173">Nom</th><th width="176">Type</th><th>Description</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Les données du document contenant des informations sur les champs</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Le nom du champ à définir</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>bool</code></td><td>La valeur à définir pour le champ</td></tr></tbody></table>

### **set\_force\_validation()**

Définit l'attribut 'force\_validation' d'un champ dans les données du document.

```python
if supplier_id in supplier_to_check:
    set_force_validation(document_data, 'purchase_order', True, reset_validation=reset_validation)
```

#### Paramètres :

<table><thead><tr><th width="173">Nom</th><th width="176">Type</th><th>Description</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Les données du document contenant des informations sur les champs</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Le nom du champ à définir</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>bool</code></td><td>La valeur à définir pour le champ</td></tr><tr><td>reset_validation (optionnel)</td><td><code>bool</code></td><td>Définit l'attribut "is_validated" à la valeur spécifiée<br>Par défaut, c'est <code>False</code></td></tr></tbody></table>

### **set\_field\_as\_invalid()**

Marque un champ dans l'écran de validation comme invalide et le met en surbrillance.

```python
if not document_date:
    set_field_as_invalid(document_data, "document_date", "Es ist kein Datum vorhanden", "INVALID_VALUE")
```

#### Paramètres :

<table><thead><tr><th width="173">Nom</th><th width="176">Type</th><th>Description</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Les données du document contenant des informations sur les champs</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Le nom du champ à marquer comme invalide</td></tr><tr><td>message<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Le message de validation pour le champ</td></tr><tr><td>code (optionnel)</td><td><code>string</code></td><td><p>Code d'erreur pour la validation</p><p>Par défaut, c'est <code>None</code></p></td></tr></tbody></table>

### **set\_field\_attribute()**

Définit un attribut personnalisé d'un champ dans les données du document.

```python
if purchase_order:
    if po_supplier_id != invoice_supplier_id:
        set_field_as_invalid(document_data, "supplier_name", "Supplier is different from PO supplier")
    else:
        set_field_attribute(document_data, "supplier_name", "is_valid", True)
        set_field_attribute(document_data, "supplier_name", "validation_message","")
```

#### Paramètres :

<table><thead><tr><th width="173">Nom</th><th width="176">Type</th><th>Description</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Les données du document contenant des informations sur les champs</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Le nom du champ à définir</td></tr><tr><td>attribute_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Le nom de l'attribut à définir. La liste des attributs supportés se trouve <a href="functions.md#attributs-supportes">ici</a>.</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>any</code></td><td>La valeur à définir pour l'attribut</td></tr></tbody></table>

### **is\_supplier\_valid()**

Vérifie si un fournisseur est valide en fonction des critères fournis.

```python
bool = is_supplier_valid(user, {"name": "Supplier Inc."})
```

#### Paramètres :

<table><thead><tr><th width="203">Nom</th><th width="216">Type</th><th>Description</th></tr></thead><tbody><tr><td>user<mark style="color:red;">*</mark></td><td><code>UserAuthentication</code></td><td>L'utilisateur authentifié</td></tr><tr><td>filter_data_json<mark style="color:red;">*</mark></td><td><code>json</code></td><td>Critères de filtrage pour valider le fournisseur</td></tr><tr><td>sub_org_id (optionnel)</td><td><code>string</code></td><td>ID de sous-organisation optionnel pour le filtrage<br>Par défaut, c'est <code>None</code></td></tr></tbody></table>

#### Renvoie :

* True, si l'utilisateur est valide
* False si l'utilisateur n'est pas valide

### **get\_document\_content()**

Décode les données du document et les renvoie sous forme de chaîne.

```python
document_content = get_document_content(doc)
if document_content:
    document_content = document_content.lower()
```

#### Paramètres :

<table><thead><tr><th width="173">Nom</th><th width="176">Type</th><th>Description</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Les données du document contenant des informations sur les champs</td></tr></tbody></table>

#### Renvoie :

* Les données du document sous forme de chaîne.

### **update\_document\_status\_with\_doc\_id()**

Met à jour le statut d'un document avec un ID spécifique au statut donné.

```python
genehmigung_user_1 = get_field_value(document_data, 'genehmigung_user_1', None)

if genehmigung_user_1 != "LEER":
    update_document_status_with_doc_id(document_json['doc_id'], user, document_json['org_id'], "validated_pending_approval")
```

#### Paramètres :

<table><thead><tr><th width="228">Nom</th><th width="216">Type</th><th>Description</th></tr></thead><tbody><tr><td>doc_id<mark style="color:red;">*</mark></td><td><code>string</code></td><td>L'ID du document à mettre à jour</td></tr><tr><td>user<mark style="color:red;">*</mark></td><td>soit <code>user ID</code> ou <code>UserAuthentication</code> object</td><td>L'utilisateur effectuant la mise à jour</td></tr><tr><td>org_id<mark style="color:red;">*</mark></td><td><code>string</code></td><td>L'ID de l'organisation à laquelle appartient le document</td></tr><tr><td>status<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Le nouveau statut du document</td></tr><tr><td>message (optionnel)</td><td><code>string</code></td><td>Message optionnel associé à la mise à jour du statut<br>Par défaut, c'est <code>None</code></td></tr><tr><td>doc_classification_class (optionnel)</td><td><code>string</code></td><td>Classe de classification de document optionnelle<br>Par défaut, c'est <code>None</code></td></tr></tbody></table>

### **get\_lov\_values()**

Obtient les valeurs LOV d'un org\_id et d'une clé spécifiques.

```python
reverse_charge_to_check = get_lov_values(org_id, 'Kosten', return_type="list_of_values")
```

#### Paramètres :

<table><thead><tr><th width="173">Nom</th><th width="176">Type</th><th>Description</th></tr></thead><tbody><tr><td>org_id<mark style="color:red;">*</mark></td><td><code>string</code></td><td>L'ID de l'organisation à laquelle appartient le document</td></tr><tr><td>key<mark style="color:red;">*</mark></td><td><code>string</code></td><td>La clé de la Liste de Valeurs requise</td></tr><tr><td>return_type (optionnel)</td><td><code>string</code></td><td>Le type dans lequel les données doivent être renvoyées<br>Par défaut, c'est <code>'list_of_objects'</code></td></tr><tr><td>sub_org_id (optionnel)</td><td><code>string</code></td><td>ID de sous-organisation optionnel pour le filtrage<br>Par défaut, c'est <code>None</code></td></tr><tr><td>language_code<br>(optionnel)</td><td><code>string</code></td><td>Ce paramètre définit la langue dans laquelle les valeurs seront renvoyées. Il accepte des codes de langue, tels que "en" pour l'anglais ou "fr" pour le français.<br>Par défaut, c'est <code>""</code></td></tr></tbody></table>

#### Renvoie :

* Valeurs LOV sous forme de liste d'objets ou sous forme de liste.

### **format\_decimal\_to\_locale()**

Formate une valeur décimale au format en\_US.UTF-8.

```python
standard_value = "{0:.2f}".format(total)
formatted_value = format_decimal_to_locale(
    standard_value, document_json['amount_format_locale']
)
```

#### Paramètres :

<table><thead><tr><th width="208">Nom</th><th width="187">Type</th><th>Description</th></tr></thead><tbody><tr><td>value<mark style="color:red;">*</mark></td><td><code>float, decimal.Decimal, str</code></td><td>La valeur qui doit être formatée.</td></tr><tr><td>to_locale (optionnel)</td><td><code>string</code></td><td>Le format dans lequel la valeur est transformée.<br>Par défaut, c'est <code>'en_US.UTF-8'</code></td></tr><tr><td>max_decimal_places (optionnel)</td><td><code>int</code></td><td>ID de sous-organisation optionnel pour le filtrage<br>Par défaut, c'est <code>4</code></td></tr><tr><td>min_decimal_places (optionnel)</td><td><code>int</code></td><td>Le minimum de décimales qui doivent être considérées<br>Par défaut, c'est <code>2</code></td></tr></tbody></table>

* value: La valeur qui doit être formatée.
* to\_locale (optionnel): Le format dans lequel la valeur est transformée.
* max\_decimal\_places (optionnel): Le maximum de décimales qui doivent être considérées.
* min\_decimal\_places (optionnel): Le minimum de décimales qui doivent être considérées.

#### Renvoie :

* La valeur formatée.

### **compare\_values()**

Compare deux valeurs pour l'égalité, en gérant divers types de données.

```python
result = compare_values(10, "10")
```

#### Paramètres :

<table><thead><tr><th width="173">Nom</th><th width="176">Type</th><th>Description</th></tr></thead><tbody><tr><td>value1<mark style="color:red;">*</mark></td><td><code>any</code></td><td>La première valeur à comparer</td></tr><tr><td>value2<mark style="color:red;">*</mark></td><td><code>any</code></td><td>La deuxième valeur à comparer</td></tr></tbody></table>

#### Renvoie :

* True si les valeurs sont égales et False si elles diffèrent

### **create\_document\_task()**

Crée une tâche, l'assigne à un utilisateur ou un groupe, définit la priorité et envoie éventuellement un e-mail.

```python
if not is_task_created:
            create_document_task(user, document_data, "Herkunftsland außerhalb der EU", "Die Gelangensbestätigung kommt von einem Land außerhalb der EU. Bitte das MRN-Dokument anhängen.", "high", 1007, None, False)
            document_data["document_json"]["country_check_task_created"] = True
```

#### Paramètres :

<table><thead><tr><th width="216">Nom</th><th width="217">Type</th><th>Description</th></tr></thead><tbody><tr><td>user<mark style="color:red;">*</mark></td><td>soit <code>user ID</code> ou <code>UserAuthentication</code> object</td><td>L'utilisateur effectuant la mise à jour</td></tr><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Les données du document contenant des informations sur les champs</td></tr><tr><td>title<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Le titre de la tâche</td></tr><tr><td>description<mark style="color:red;">*</mark></td><td><code>string</code></td><td>La description de la tâche</td></tr><tr><td>priority<mark style="color:red;">*</mark></td><td><code>string</code></td><td>La priorité de la tâche</td></tr><tr><td>assigned_to_user_id<mark style="color:red;">*</mark></td><td><code>int</code></td><td>L'ID de l'utilisateur auquel la tâche doit être assignée</td></tr><tr><td>assigned_to_group_id<mark style="color:red;">*</mark></td><td><code>int</code></td><td>L'ID du groupe auquel la tâche doit être assignée</td></tr><tr><td>send_email<mark style="color:red;">*</mark></td><td><code>bool</code></td><td>Détermine si un e-mail doit être envoyé ou non</td></tr></tbody></table>

#### Renvoie :

* Dict qui indique si le processus a réussi ou non

### **set\_document\_sub\_org\_id()**

Définit le sub\_org\_id des données de document spécifiées.

```python
if sub_org_id != current_sub_org_id:
    document_data["document_json"]["sub_org_id4"] = sub_org_id
    set_document_sub_org_id(document_data, sub_org_id)
```

#### Paramètres :

<table><thead><tr><th width="173">Nom</th><th width="176">Type</th><th>Description</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Les données du document contenant des informations sur les champs</td></tr><tr><td>sub_org_id<mark style="color:red;">*</mark></td><td><code>string</code></td><td>ID de sous-organisation optionnel pour le filtrage</td></tr></tbody></table>

### **get\_user\_by\_id()**

Obtient l'utilisateur avec l'ID utilisateur correspondant.

```python
requester_mail = str(get_user_by_id(str(requester)).email.lower())
```

#### Paramètres :

<table><thead><tr><th width="173">Nom</th><th width="176">Type</th><th>Description</th></tr></thead><tbody><tr><td>user_id<mark style="color:red;">*</mark></td><td><code>string</code></td><td>L'ID de l'utilisateur</td></tr></tbody></table>

#### Renvoie :

* L'utilisateur avec l'ID utilisateur correspondant

### **get\_group\_by\_id()**

Obtient le groupe avec l'ID de groupe correspondant.

```python
group_name  = str(get_group_by_id(assigned_to_group_id))
```

#### Paramètres :

<table><thead><tr><th width="173">Nom</th><th width="176">Type</th><th>Description</th></tr></thead><tbody><tr><td>group_id<mark style="color:red;">*</mark></td><td><code>string</code></td><td>L'ID du groupe</td></tr></tbody></table>

#### Renvoie :

* Le groupe avec l'ID de groupe correspondant

### **get\_user\_by\_email()**

Obtient l'utilisateur avec l'e-mail correspondant.

```python
user_name = str(get_user_by_email(email))
```

#### Paramètres :

<table><thead><tr><th width="173">Nom</th><th width="176">Type</th><th>Description</th></tr></thead><tbody><tr><td>email<mark style="color:red;">*</mark></td><td><code>any</code></td><td>L'e-mail de l'utilisateur</td></tr></tbody></table>

#### Renvoie :

* L'utilisateur avec l'e-mail correspondant

### **add\_table\_column()**

Ajoute une colonne à la table spécifiée.

```python
table = tables_dict.get("ORDER_CONFIRMATION_TABLE")

if table:
    add_table_column(table, "PROMISED_DELIVERY_DATE")
```

#### Paramètres :

<table><thead><tr><th width="173">Nom</th><th width="176">Type</th><th>Description</th></tr></thead><tbody><tr><td>table<mark style="color:red;">*</mark></td><td><code>string</code></td><td>La table où la colonne doit être ajoutée</td></tr><tr><td>col_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Le nom de la colonne</td></tr><tr><td>default_value (optionnel)</td><td><code>any</code></td><td><p>La valeur initiale pour le champ</p><p>Par défaut, c'est <code>None</code></p></td></tr></tbody></table>

### **get\_column\_value()**

Obtient la valeur d'une colonne spécifiée.

```python
for row in table['rows']:
        unit = get_column_value(row, "UNIT")
```

#### Paramètres :

<table><thead><tr><th width="173">Nom</th><th width="176">Type</th><th>Description</th></tr></thead><tbody><tr><td>row<mark style="color:red;">*</mark></td><td><code>string</code></td><td>La ligne où la valeur est située</td></tr><tr><td>col_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Le nom de la colonne</td></tr><tr><td>default_value (optionnel)</td><td><code>any</code></td><td>La valeur initiale pour le champ<br>Par défaut, c'est <code>None</code></td></tr><tr><td>is_clean (optionnel)</td><td><code>bool</code></td><td>Convertit la valeur en majuscules et supprime les espaces supplémentaires<br>Par défaut, c'est <code>False</code></td></tr></tbody></table>

#### Renvoie

* Renvoie la valeur de la colonne spécifiée si elle existe ; sinon, elle renvoie `None`

### **set\_column\_value()**

Définit la valeur de la colonne spécifiée. Si la colonne n'existe pas, elle sera créée.

```python
supplier_id = get_field_value(document_data, "supplier_id", "")

quote_table = tables_dict["QUOTE_TABLE"]

for row in quote_table.get('rows', []):
    set_column_value(row,"SUPPLIER_ID", supplier_id)
```

#### Paramètres :

<table><thead><tr><th width="173">Nom</th><th width="176">Type</th><th>Description</th></tr></thead><tbody><tr><td>row<mark style="color:red;">*</mark></td><td><code>string</code></td><td>La ligne où la valeur est située</td></tr><tr><td>col_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Le nom de la colonne</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>any</code></td><td>La valeur qui sera définie à l'emplacement spécifié</td></tr></tbody></table>

#### Renvoie :

* True si le changement a réussi

### **set\_column\_date\_value()**

Définit la valeur de date d'une colonne spécifiée.

```python
set_column_date_value(document_data, row, "DELIVERY_DATE", "2020-12-31", add_days=2)
```

#### Paramètres :

<table><thead><tr><th width="173">Nom</th><th width="196.05859375">Type</th><th>Description</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Les données du document contenant des informations sur les champs</td></tr><tr><td>row<mark style="color:red;">*</mark></td><td><code>string</code></td><td>La ligne où la valeur est située</td></tr><tr><td>col_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Le nom de la colonne</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>string</code></td><td>La valeur de date à définir au format ISO (par exemple, "2020-12-31")</td></tr><tr><td>add_days (optionnel)</td><td><code>int</code></td><td>Ajoute des jours supplémentaires à la date donnée<br>Par défaut, c'est <code>2</code></td></tr><tr><td>skip_weekend (optionnel)</td><td><code>bool</code></td><td>Ignore la date si elle tombe le week-end<br>Par défaut, c'est <code>False</code></td></tr><tr><td>exclude_final_days<br>(optionnel)</td><td>soit <code>string</code> ou <code>int</code></td><td>Spécifie les jours à exclure (0-6 ou dimanche à samedi)</td></tr></tbody></table>

### **set\_column\_amount\_value()**

* Convertit la valeur en chaîne et définit la valeur pour la colonne
* Définit le contenu de la colonne à la valeur
* Formate la valeur selon la locale

```python
quantity = float(quantity) / 1000
set_column_amount_value(document_data, row, "QUANTITY", str(quantity))
```

#### Paramètres :

<table><thead><tr><th width="173">Nom</th><th width="176">Type</th><th>Description</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Les données du document contenant des informations sur les champs</td></tr><tr><td>row<mark style="color:red;">*</mark></td><td><code>string</code></td><td>La ligne où la valeur est située</td></tr><tr><td>column_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Le nom de la colonne</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>string</code></td><td>La valeur à définir pour le champ (passer un nombre sous forme de chaîne par exemple, "123456")</td></tr></tbody></table>

### **delete\_tables()**

Cette fonction supprime les tables des données du document.

```python
delete_tables(document_data)
```

#### Paramètres :

<table><thead><tr><th width="173">Nom</th><th width="176">Type</th><th>Description</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Les données du document contenant des informations sur les champs</td></tr></tbody></table>

### **restore\_tables()**

Cette fonction restaure les tables dans les données du document.

```python
restore_tables(document_data)
```

#### Paramètres :

<table><thead><tr><th width="173">Nom</th><th width="176">Type</th><th>Description</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Les données du document contenant des informations sur les champs</td></tr></tbody></table>

### **remove\_rows\_from\_table()**

Supprime des lignes de la table spécifiée.

```python
count = 1
start = 1
remove_rows_from_table(document_data,"INVOICE_TABLE",count,start) 
```

#### Paramètres :

<table><thead><tr><th width="173">Nom</th><th width="176">Type</th><th>Description</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Les données du document contenant des informations sur les champs</td></tr><tr><td>table_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>Le nom de la table</td></tr><tr><td>count<mark style="color:red;">*</mark></td><td><code>int</code></td><td>Combien de lignes doivent être supprimées</td></tr><tr><td>start<mark style="color:red;">*</mark></td><td><code>int</code></td><td>Le point de départ</td></tr></tbody></table>

### **remove\_all\_rows\_except\_one\_from\_table()**

Supprime toutes les lignes sauf une de la table spécifiée.

```python
count = 1
start = 1
remove_rows_from_table(document_data,"INVOICE_TABLE",count,start) 
```

#### Paramètres :

<table><thead><tr><th width="173">Nom</th><th width="176">Type</th><th>Description</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Les données du document contenant des informations sur les champs</td></tr><tr><td>line_number<mark style="color:red;">*</mark></td><td><code>int</code></td><td>Le numéro de la ligne qui ne doit pas être supprimée</td></tr></tbody></table>

## Attributs Supportés

### Attributs de Champ Principaux

| Attribut            | Type   | Description                                                 |
| ------------------- | ------ | ----------------------------------------------------------- |
| `value`             | any    | La valeur brute du champ                                    |
| `formatted_value`   | string | Valeur formatée pour l'affichage                            |
| `content`           | string | Contenu extrait original                                    |
| `is_required`       | bool   | Si le champ est obligatoire                                 |
| `is_valid`          | bool   | Statut de validation                                        |
| `is_validated`      | bool   | Si le champ a été validé par l'utilisateur                  |
| `force_validation`  | bool   | Forcer l'utilisateur à valider ce champ                     |
| `highlight_field`   | bool   | Mettre le champ en surbrillance dans l'interface utilisateur|
| `extraction_method` | string | Comment la valeur a été extraite (par exemple, `"SCRIPT"`)  |

### Attributs de Validation

| Attribut                | Type   | Description                                                              |
| ----------------------- | ------ | ------------------------------------------------------------------------ |
| `validation_message`    | string | Message d'erreur affiché à l'utilisateur                                 |
| `validation_code`       | string | Code d'erreur (par exemple, `"FORCED_VALIDATION"`, `"INVALID_VALUE"`)    |
| `invalidated_by_script` | bool   | Marque le champ comme invalidé par un script                             |

### Attributs d'Extraction/OCR

| Attribut            | Type   | Description                                              |
| ------------------- | ------ | -------------------------------------------------------- |
| `coords`            | object | Coordonnées du cadre de délimitation sur le document     |
| `confidence`        | float  | Score de confiance OCR/extraction                        |
| `score`             | float  | Score de correspondance/validation                       |
| `score_description` | string | Description du score                                     |
| `page`              | int    | Numéro de page où le champ a été trouvé                  |
| `rule`              | string | Règle d'extraction qui a été appliquée                   |

## Fonctions intégrées Python

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

## Fonctions de la classe String

Vous pouvez également utiliser ces fonctions spécifiquement pour travailler avec des chaînes :

* lower() : Convertit tous les caractères d'une chaîne en minuscules.
* upper() : Convertit tous les caractères d'une chaîne en majuscules.
* split() : Divise une chaîne en une liste en fonction d'un délimiteur (par exemple, un espace ou une virgule).
* startswith() : Vérifie si une chaîne commence par un préfixe spécifié.
* endswith() : Vérifie si une chaîne se termine par un suffixe spécifié.
* strip() : Supprime les espaces blancs au début ou à la fin d'une chaîne.

## Fonctions du module Math de Python

Ces fonctions font partie du module math et sont utiles pour les opérations mathématiques :

* floor() : Renvoie le plus grand entier inférieur ou égal à un nombre donné.
* ceil() : Renvoie le plus petit entier supérieur ou égal à un nombre donné.

Pour plus d'informations, consultez la documentation officielle de Python : [Fonctions du module Math](https://docs.python.org/3/library/math.html).

## Fonction d'expression régulière

* re.search() : Recherche un motif dans une chaîne et renvoie la première correspondance.

Voir plus de détails ici : [Documentation re.search](https://docs.python.org/3/library/re.html#re.search).

## Fonctions externes

Voici quelques fonctions utiles provenant de bibliothèques externes :

* deepcopy() : Crée une copie d'un objet, y compris des objets imbriqués (du module copy).\
  [Documentation Deepcopy](https://docs.python.org/3/library/copy.html#copy.deepcopy).
* levenshtein\_distance() : Calcule le nombre de modifications (insertion, suppression, substitution) nécessaires pour transformer une chaîne en une autre. Cette fonction est disponible dans la [bibliothèque Jellyfish](https://jamesturk.github.io/jellyfish/functions/).

## Fonctions de date et d'heure

Vous pouvez utiliser les fonctions suivantes pour travailler avec des dates et des heures :

* strptime() : Convertit une chaîne en un objet datetime en fonction d'un format spécifié.
* strftime() : Formate un objet datetime en une chaîne en fonction d'un format spécifié.

Pour plus d'informations, consultez la documentation officielle :\
[Fonctions de date et d'heure](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior).
