# Funkcje

**Dokumentacja Funkcjonalna**

Ten moduł zawiera funkcje do manipulowania danymi dokumentu i wykonywania różnych operacji związanych z polami dokumentu.

## **Funkcje**

1. ### **set\_field\_value(document\_data, field\_name, value)**
* Opis: Ustawia wartość pola w danych dokumentu.
* Parametry:
* `document_data` (dict): Dane dokumentu zawierające informacje o polu.
* `field_name` (str): Nazwa pola do ustawienia.
* `value`: Wartość do ustawienia dla pola.
*   Przykład:

`set_field_value(document_data, "name", "John Doe")`
2. ### **set\_date\_value(document\_data, field\_name, value)**
* Opis: Ustawia wartość pola daty w danych dokumentu.
* Parametry i przykładowe użycie podobne do `set_field_value`.
3. ### **set\_amount\_value(document\_data, field\_name, value)**
* Opis: Ustawia wartość pola kwoty w danych dokumentu.
* Parametry i przykładowe użycie podobne do `set_field_value`.
4. ### **set\_is\_required(document\_data, field\_name, value)**
* Opis: Ustawia atrybut 'is\_required' pola w danych dokumentu.
* Parametry i przykładowe użycie podobne do `set_field_value`.
5. ### **set\_force\_validation(document\_data, field\_name, value)**
* Opis: Ustawia atrybut 'force\_validation' pola w danych dokumentu.
* Parametry i przykładowe użycie podobne do `set_field_value`.
6. ### **set\_field\_attribute(document\_data, field\_name, attribute\_name, value)**
* Opis: Ustawia niestandardowy atrybut pola w danych dokumentu.
* Parametry:
* `attribute_name` (str): Nazwa atrybutu do ustawienia.
* `value`: Wartość do ustawienia dla atrybutu.
*   Przykład:

`set_field_attribute(document_data, "address", "is_verified", True)`
7. ### **get\_field\_value(document\_data, field\_name, default\_value=None, is\_clean=False)**
* Opis: Pobiera wartość pola z danych dokumentu.
* Parametry i przykładowe użycie podobne do `set_field_value`.
8. ### **create\_new\_field(field\_name, value="")**
* Opis: Tworzy nowe pole o określonej nazwie i wartości.
* Parametry:
* `field_name` (str): Nazwa pola do utworzenia.
* `value`: Wartość początkowa dla pola (domyślnie pusty ciąg znaków).
*   Przykład:

`create_new_field("address", "123 Main St")`
9. ### **delete\_field(document\_data, field\_name)**
* Opis: Usuwa pole z danych dokumentu.
* Parametry i przykładowe użycie podobne do `set_field_value`.
10. ### **update\_document\_status\_with\_doc\_id(doc\_id, user, org\_id, status, message=None, doc\_classification\_class=None)**
* Opis: Aktualizuje status dokumentu o określonym ID.
* Parametry:
* `doc_id` (str): ID dokumentu do zaktualizowania.
* `user`: Użytkownik wykonujący aktualizację (ID użytkownika lub obiekt UserAuthentication).
* `org_id`: ID organizacji, do której należy dokument.
* `status` (str): Nowy status dokumentu.
* `message`: Opcjonalna wiadomość związana z aktualizacją statusu.
* `doc_classification_class`: Opcjonalna klasa klasyfikacji dokumentu.
*   Przykład:

`update_document_status_with_doc_id("123456", user, org_id, "approved", "Document approved")`
11. ### **is\_supplier\_valid(user: UserAuthentication, filter\_data\_json, sub\_org\_id=None)**
* Opis: Sprawdza, czy dostawca jest ważny na podstawie podanych kryteriów.
* Parametry:
* `user` (UserAuthentication): Zautoryzowany użytkownik.
* `filter_data_json`: Kryteria filtrowania w celu zweryfikowania dostawcy.
* `sub_org_id`: Opcjonalne ID podorganizacji do filtrowania.
*   Przykład:

`is_supplier_valid(user, {"name": "Supplier Inc."})`
12. ### **set\_field\_as\_invalid(document\_data, field\_name, message, code=None)**
* Opis: Oznacza pole jako nieprawidłowe w danych dokumentu.
* Parametry:
* `document_data` (dict): Dane dokumentu zawierające informacje o polu.
* `field_name` (str): Nazwa pola do oznaczenia jako nieprawidłowe.
* `message` (str): Komunikat walidacyjny dla pola.
* `code` (opcjonalne): Kod błędu walidacji (domyślnie brak).
*   Przykład:

`set_field_as_invalid(document_data, "email", "Invalid email format", "EMAIL_FORMAT_INVALID")`
13. ### **compare\_values(value1, value2)**
* Opis: Porównuje dwie wartości pod kątem równości, obsługując różne typy danych.
* Parametry:
* `value1`: Pierwsza wartość do porównania.
* `value2`: Druga wartość do porównania.
*   Przykład:

`compare_values(10, "10")`
