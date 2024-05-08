# Функције

**Функционална документација**

Овај модул садржи функције за манипулисање подацима докумената и извршавање различитих операција повезаних са пољима докумената.

## **Функције**

1. ### **set\_field\_value(document\_data, field\_name, value)**
* Опис: Поставља вредност поља у подацима докумената.
* Параметри:
* `document_data` (dict): Подаци докумената који садрже информације о пољу.
* `field_name` (str): Име поља које се поставља.
* `value`: Вредност која се поставља за поље.
*   Пример:

`set_field_value(document_data, "name", "John Doe")`
2. ### **set\_date\_value(document\_data, field\_name, value)**
* Опис: Поставља вредност датумског поља у подацима докумената.
* Параметри и пример коришћења су слични као код `set_field_value`.
3. ### **set\_amount\_value(document\_data, field\_name, value)**
* Опис: Поставља вредност поља износа у подацима докумената.
* Параметри и пример коришћења су слични као код `set_field_value`.
4. ### **set\_is\_required(document\_data, field\_name, value)**
* Опис: Поставља атрибут 'is\_required' поља у подацима докумената.
* Параметри и пример коришћења су слични као код `set_field_value`.
5. ### **set\_force\_validation(document\_data, field\_name, value)**
* Опис: Поставља атрибут 'force\_validation' поља у подацима докумената.
* Параметри и пример коришћења су слични као код `set_field_value`.
6. ### **set\_field\_attribute(document\_data, field\_name, attribute\_name, value)**
* Опис: Поставља прилагођени атрибут поља у подацима докумената.
* Параметри:
* `attribute_name` (str): Име атрибута који се поставља.
* `value`: Вредност која се поставља за атрибут.
*   Пример:

`set_field_attribute(document_data, "address", "is_verified", True)`
7. ### **get\_field\_value(document\_data, field\_name, default\_value=None, is\_clean=False)**
* Опис: Добија вредност поља из података докумената.
* Параметри и пример коришћења су слични као код `set_field_value`.
8. ### **create\_new\_field(field\_name, value="")**
* Опис: Креира ново поље са наведеним именом и вредношћу.
* Параметри:
* `field_name` (str): Име поља које се креира.
* `value`: Почетна вредност за поље (подразумевано је празан стринг).
*   Пример:

`create_new_field("address", "123 Main St")`
9. ### **delete\_field(document\_data, field\_name)**
* Опис: Брише поље из података докумената.
* Параметри и пример коришћења су слични као код `set_field_value`.
10. ### **update\_document\_status\_with\_doc\_id(doc\_id, user, org\_id, status, message=None, doc\_classification\_class=None)**
* Опис: Ажурира статус документа са наведеним идентификатором.
* Параметри:
* `doc_id` (str): ИД документа који се ажурира.
* `user`: Корисник који врши ажурирање (било идентификатор корисника или објекат UserAuthentication).
* `org_id`: ИД организације којој документ припада.
* `status` (str): Нови статус документа.
* `message`: Опционална порука повезана са ажурирањем статуса.
* `doc_classification_class`: Опционална класа класификације документа.
*   Пример:

`update_document_status_with_doc_id("123456", user, org_id, "approved", "Document approved")`
11. ### **is\_supplier\_valid(user: UserAuthentication, filter\_data\_json, sub\_org\_id=None)**
* Опис: Проверава да ли је добављач валидан на основу наведених критеријума.
* Параметри:
* `user` (UserAuthentication): Аутентификовани корисник.
* `filter_data_json`: Критеријуми филтрирања за проверу добављача.
* `sub_org_id`: Опционални ИД подорганизације за филтрирање.
*   Пример:

`is_supplier_valid(user, {"name": "Supplier Inc."})`
12. ### **set\_field\_as\_invalid(document\_data, field\_name, message, code=None)**
* Опис: Означава поље као невалидно у подацима докумената.
* Параметри:
* `document_data` (dict): Подаци докумената који садрже информације о пољу.
* `field_name` (str): Име поља које се означава као невалидно.
* `message` (str): Порука о валидацији за поље.
* `code` (опционо): Код грешке за валидацију (подразумевано је None).
*   Пример:

`set_field_as_invalid(document_data, "email", "Invalid email format", "EMAIL_FORMAT_INVALID")`
13. ### **compare\_values(value1, value2)**
* Опис: Пореди две вредности за једнакост, обрађујући различите типове података.
* Параметри:
* `value1`: Прва вредност за поређење.
* `value2`: Друга вредност за поређење.
*   Пример:

`compare_values(10, "10")`
