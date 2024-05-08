# Funktionen

**Funktionale Dokumentation**

Dieses Modul enthält Funktionen zum Manipulieren von Dokumentendaten und zum Durchführen verschiedener Operationen im Zusammenhang mit Dokumentenfeldern.

## **Funktionen**

1. ### **set\_field\_value(document\_data, field\_name, value)**
* Beschreibung: Legt den Wert eines Feldes in den Dokumentendaten fest.
* Parameter:
* `document_data` (dict): Die Dokumentendaten enthalten Informationen zum Feld.
* `field_name` (str): Der Name des zu setzenden Feldes.
* `value`: Der Wert, der für das Feld festgelegt werden soll.
*   Beispiel:

`set_field_value(document_data, "name", "John Doe")`
2. ### **set\_date\_value(document\_data, field\_name, value)**
* Beschreibung: Legt den Wert eines Datumsfeldes in den Dokumentendaten fest.
* Parameter:
* `document_data` (dict): Die Dokumentendaten enthalten Informationen zum Feld.
* `field_name` (str): Der Name des Datumsfeldes, das festgelegt werden soll.
* `value`: Der Datumswert, der im ISO-Format festgelegt werden soll (z. B. "2020-12-31").
*   Beispiel:

`set_date_value(document_data, "date_of_birth", "1990-05-15")`
3. ### **set\_amount\_value(document\_data, field\_name, value)**
* Beschreibung: Legt den Wert eines Betragsfeldes in den Dokumentendaten fest.
* Parameter und Beispiel ähnlich wie bei `set_field_value`.
4. ### **set\_is\_required(document\_data, field\_name, value)**
* Beschreibung: Legt das Attribut 'is\_required' eines Feldes in den Dokumentendaten fest.
* Parameter und Beispiel ähnlich wie bei `set_field_value`.
5. ### **set\_force\_validation(document\_data, field\_name, value)**
* Beschreibung: Legt das Attribut 'force\_validation' eines Feldes in den Dokumentendaten fest.
* Parameter und Beispiel ähnlich wie bei `set_field_value`.
6. ### **set\_field\_attribute(document\_data, field\_name, attribute\_name, value)**
* Beschreibung: Legt ein benutzerdefiniertes Attribut eines Feldes in den Dokumentendaten fest.
* Parameter:
* `attribute_name` (str): Der Name des zu setzenden Attributs.
* `value`: Der Wert, der für das Attribut festgelegt werden soll.
*   Beispiel:

`set_field_attribute(document_data, "address", "is_verified", True)`
7. ### **get\_field\_value(document\_data, field\_name, default\_value=None, is\_clean=False)**
* Beschreibung: Ruft den Wert eines Feldes aus den Dokumentendaten ab.
* Parameter und Beispiel ähnlich wie bei `set_field_value`.
8. ### **create\_new\_field(field\_name, value="")**
* Beschreibung: Erstellt ein neues Feld mit dem angegebenen Namen und Wert.
* Parameter:
* `field_name` (str): Der Name des zu erstellenden Feldes.
* `value`: Der Anfangswert für das Feld (Standardwert ist ein leerer String).
*   Beispiel:

`create_new_field("address", "123 Main St")`
9. ### **delete\_field(document\_data, field\_name)**
* Beschreibung: Löscht ein Feld aus den Dokumentendaten.
* Parameter und Beispiel ähnlich wie bei `set_field_value`.
10. ### **update\_document\_status\_with\_doc\_id(doc\_id, user, org\_id, status, message=None, doc\_classification\_class=None)**
* Beschreibung: Aktualisiert den Status eines Dokuments mit der angegebenen ID.
* Parameter:
* `doc_id` (str): Die ID des zu aktualisierenden Dokuments.
* `user`: Der Benutzer, der das Update durchführt (entweder Benutzer-ID oder UserAuthentication-Objekt).
* `org_id`: Die ID der Organisation, zu der das Dokument gehört.
* `status` (str): Der neue Status des Dokuments.
* `message`: Optionale Nachricht, die mit dem Statusupdate verknüpft ist.
* `doc_classification_class`: Optionale Dokumentklassifizierungsklasse.
*   Beispiel:

`update_document_status_with_doc_id("123456", user, org_id, "approved", "Dokument genehmigt")`
11. ### **is\_supplier\_valid(user: UserAuthentication, filter\_data\_json, sub\_org\_id=None)**
* Beschreibung: Überprüft, ob ein Lieferant basierend auf den bereitgestellten Kriterien gültig ist.
* Parameter:
* `user` (UserAuthentication): Der authentifizierte Benutzer.
* `filter_data_json`: Filterkriterien zur Validierung des Lieferanten.
* `sub_org_id`: Optionale Unterorganisations-ID zur Filterung.
*   Beispiel:

`is_supplier_valid(user, {"name": "Supplier Inc."})`
12. ### **set\_field\_as\_invalid(document\_data, field\_name, message, code=None)**
* Beschreibung: Markiert ein Feld in den Dokumentendaten als ungültig.
* Parameter:
* `document_data` (dict): Die Dokumentendaten enthalten Informationen zum Feld.
* `field_name` (str): Der Name des Feldes, das als ungültig markiert werden soll.
* `message` (str): Die Validierungsnachricht für das Feld.
* `code` (optional): Fehlercode für die Validierung (Standardwert ist None).
*   Beispiel:

`set_field_as_invalid(document_data, "email", "Ungültiges E-Mail-Format", "EMAIL_FORMAT_INVALID")`
13. ### **compare\_values(value1, value2)**
* Beschreibung: Vergleicht zwei Werte auf Gleichheit und behandelt verschiedene Datentypen.
* Parameter:
* `value1`: Der erste zu vergleichende Wert.
* `value2`: Der zweite zu vergleichende Wert.
*   Beispiel:

`compare_values(10, "10")`
