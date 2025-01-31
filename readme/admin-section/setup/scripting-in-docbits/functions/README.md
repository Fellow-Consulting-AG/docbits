# Funktionen

**Funktionale Dokumentation**

Dieses Modul enthält Funktionen zur Manipulation von Dokumentdaten und zur Durchführung verschiedener Operationen im Zusammenhang mit Dokumentfeldern.

**Funktionen**

1. **set\_field\_value(document\_data, field\_name, value)**
   * Beschreibung: Setzt den Wert eines Feldes in den Dokumentdaten.
   * Parameter:
     * document\_data (dict): Die Dokumentdaten, die Feldinformationen enthalten.
     * field\_name (str): Der Name des Feldes, das gesetzt werden soll.
     * value: Der Wert, der für das Feld gesetzt werden soll.
   *   Beispiel:

       ```
       set_field_value(document_data, "name", "John Doe")
       ```
2. **set\_date\_value(document\_data, field\_name, value, add\_days=0, skip\_weekend=False)**
   * Beschreibung: Setzt den Wert eines Datumsfeldes in den Dokumentdaten.
   * Parameter:
     * document\_data (dict): Die Dokumentdaten, die Feldinformationen enthalten.
     * field\_name (str): Der Name des Datumsfeldes, das gesetzt werden soll.
     * value: Der Datumswert, der im ISO-Format gesetzt werden soll (z. B. "2020-12-31").
     * add\_days (int): Fügt zusätzliche Tage zum angegebenen Datum hinzu.
     * skip\_weekend (bool): Überspringt das Datum, wenn es auf das Wochenende fällt.
   *   Beispiel:

       ```
       set_date_value(document_data, "promised_delivery_date", "2020-12-31", add_days=2, skip_weekend=True)
       ```
3. **set\_amount\_value(document\_data, field\_name, value)**
   * Beschreibung: Setzt den Wert eines Betragsfeldes in den Dokumentdaten.
   * Parameter:
     * document\_data (dict): Die Dokumentdaten, die Feldinformationen enthalten.
     * field\_name (str): Der Name des Feldes, das gesetzt werden soll.
     * value: Der Wert, der für das Feld gesetzt werden soll.
   *   Beispiel:

       ```
       set_amount_value(document_data, "number", "123456")
       ```
4. **get\_field\_value(document\_data, field\_name, default\_value=None, is\_clean=False)**
   * Beschreibung: Holt den Wert eines Feldes aus den Dokumentdaten.
   * Parameter:
     * document\_data (dict): Die Dokumentdaten, die Feldinformationen enthalten.
     * field\_name (str): Der Name des Feldes, das gesetzt werden soll.
     * default\_value (optional): Gibt default\_value zurück, wenn kein Feldwert gefunden wird.
     * is\_clean (optional): Wandelt den Wert in Großbuchstaben um und bereinigt ihn von Leerzeichen.
   * Gibt zurück:
     * Wert des Feldes.
   *   Beispiel:

       ```
       value = get_field_value(document_data, "name")
       ```
5. **create\_new\_field(field\_name, value="")**
   * Beschreibung: Erstellt ein neues Feld mit dem angegebenen Namen und Wert.
   * Parameter:
     * field\_name (str): Der Name des zu erstellenden Feldes.
     * value: Der Anfangswert für das Feld (Standard ist ein leerer String).
   * Gibt zurück:
     * Wörterbuch des neu erstellten Feldes.
   *   Beispiel:

       ```
       dict = create_new_field("address", "")
       ```
6. **delete\_field(document\_data, field\_name)**
   * Beschreibung: Löscht ein Feld aus den Dokumentdaten.
   * Parameter:
     * document\_data (dict): Die Dokumentdaten, die Feldinformationen enthalten.
     * field\_name (str): Der Name des Feldes, das gesetzt werden soll.
   * Gibt zurück:
     * Document\_data als JSON und als dict, nachdem das Feld gelöscht wurde.
   *   Beispiel:

       ```
       //json, dict = (document_data, "name")
       ```
7. **set\_is\_required(document\_data, field\_name, value)**
   * Beschreibung: Setzt das Attribut 'is\_required' eines Feldes in den Dokumentdaten.
   * Parameter:
     * document\_data (dict): Die Dokumentdaten, die Feldinformationen enthalten.
     * field\_name (str): Der Name des Feldes, das gesetzt werden soll.
     * value: Der Wert, der für das Feld gesetzt werden soll.
   *   Beispiel:

       ```
       set_is_required(document_data, "bank_id", True)
       ```
8. **set\_force\_validation(document\_data, field\_name, value)**
   * Beschreibung: Setzt das Attribut 'force\_validation' eines Feldes in den Dokumentdaten.
   * Parameter:
     * document\_data (dict): Die Dokumentdaten, die Feldinformationen enthalten.
     * field\_name (str): Der Name des Feldes, das gesetzt werden soll.
     * value (bool): Der Wert, der für das Feld gesetzt werden soll.
   *   Beispiel:

       ```
       set_force_validation(document_data, 'supplier_name', True)
       ```
9. **set\_field\_as\_invalid(document\_data, field\_name, message, code=None)**
   * Beschreibung: Markiert ein Feld als ungültig in den Dokumentdaten.
   * Parameter:
     * document\_data (dict): Die Dokumentdaten, die Feldinformationen enthalten.
     * field\_name (str): Der Name des Feldes, das als ungültig markiert werden soll.
     * message (str): Die Validierungsnachricht für das Feld.
     * code (optional): Fehlercode für die Validierung (Standard ist None).
   *   Beispiel:

       ```
       --set_field_as_invalid(document_data, "email", "Ungültiges E-Mail-Format", "EMAIL_FORMAT_INVALID")
       ```
10. **set\_field\_attribute(document\_data, field\_name, attribute\_name, value)**
    * Beschreibung: Setzt ein benutzerdefiniertes Attribut eines Feldes in den Dokumentdaten.
    * Parameter:
      * document\_data (str): Die Dokumentdaten, die Feldinformationen enthalten.
      * field\_name (str): Der Name des Feldes, das gesetzt werden soll.
      * attribute\_name (str): Der Name des Attributs, das gesetzt werden soll.
      * value (bool): Der Wert, der für das Attribut gesetzt werden soll.
    *   Beispiel:

        ```
        set_field_attribute(document_data, "address", "is_verified", True)
        ```
11. **is\_supplier\_valid(user: UserAuthentication, filter\_data\_json, sub\_org\_id=None)**
    * Beschreibung: Überprüft, ob ein Lieferant basierend auf den angegebenen Kriterien gültig ist.
    * Parameter:
      * user (UserAuthentication): Der authentifizierte Benutzer.
      * filter\_data\_json: Filterkriterien zur Validierung des Lieferanten.
      * sub\_org\_id (optional): Optionale Sub-Organisations-ID für die Filterung.
    * Gibt zurück:
      * True, wenn der Benutzer gültig ist.
      * False, wenn der Benutzer ungültig ist.
    *   Beispiel:

        ```
        bool = is_supplier_valid(user, {"name": "Supplier Inc."})
        ```
12. **get\_document\_content(document\_data)**
    * Beschreibung: Gibt den Dokumentinhalt basierend auf den Dokumentdaten zurück.
    * Parameter:
      * document\_data (str): Die Dokumentdaten, die Feldinformationen enthalten.
    * Gibt zurück:
      * Dokumentinhalt der Dokumentdaten.
    *   Beispiel:

        ```
        document_content = get_document_content(doc)
        ```
13. **update\_document\_status\_with\_doc\_id(doc\_id, user, org\_id, status, message=None, doc\_classification\_class=None)**
    * Beschreibung: Aktualisiert den Status eines Dokuments mit der angegebenen ID.
    * Parameter:
      * doc\_id (str): Die ID des zu aktualisierenden Dokuments.
      * user: Der Benutzer, der die Aktualisierung durchführt (entweder Benutzer-ID oder UserAuthentication-Objekt).
      * org\_id: Die ID der Organisation, zu der das Dokument gehört.
      * status (str): Der neue Status des Dokuments.
      * message: Optionale Nachricht, die mit der Statusaktualisierung verbunden ist.
      * doc\_classification\_class: Optionale Dokumentklassifikationsklasse.
    *   Beispiel:

        ```
        update_document_status_with_doc_id("123456", user, "org_id", "approved", "Dokument genehmigt")
        ```
14. **get\_lov\_values(org\_id, key, return\_type="list\_of\_objects", sub\_org\_id=None)**
    * Beschreibung: Holt die LOV-Werte von einer bestimmten org\_id.
    * Parameter:
      * org\_id: Die ID der Organisation, zu der das Dokument gehört.
      * return\_type (optional): Der Typ, in dem die Daten zurückgegeben werden sollen.
      * sub\_org\_id (optional): Optionale Sub-Organisations-ID für die Filterung.
    * Gibt zurück:
      * LOV-Werte als Liste von Objekten oder als Liste.
    *   Beispiel:

        ```
        supplier_to_check = get_lov_values(org_id, 'BlacklistSupplier', return_type="list_of_values")
        ```
15. **format\_decimal\_to\_locale(value, to\_locale="en\_US.UTF-8", max\_decimal\_places=4, min\_decimal\_places=2)**
    * Beschreibung: Formatiert einen Dezimalwert im en\_US.UTF-8-Format.
    * Parameter:
      * value: Der Wert, der formatiert werden soll.
      * to\_locale (optional): Das Format, in das der Wert umgewandelt werden soll.
      * max\_decimal\_places (optional): Die maximale Anzahl von Dezimalstellen, die berücksichtigt werden sollen.
      * min\_decimal\_places (optional): Die minimale Anzahl von Dezimalstellen, die berücksichtigt werden sollen.
    * Gibt zurück:
      * Den formatierten Wert.
    *   Beispiel:

        ```
        formatted_value = format_decimal_to_locale(value, document_json['amount_format_locale'])
        ```
16. **compare\_values(value1, value2)**
    * Beschreibung: Vergleicht zwei Werte auf Gleichheit und behandelt verschiedene Datentypen.
    * Parameter:
      * value1: Der erste Wert zum Vergleichen.
      * value2: Der zweite Wert zum Vergleichen.
    * Gibt zurück:
      * True, wenn die Werte gleich sind, und False, wenn sie unterschiedlich sind.
    *   Beispiel:

        ```
        result = compare_values(10, "10")
        ```
17. **create\_document\_task( user, document\_data, title, description, priority,**\
    **assigned\_to\_user\_id, assigned\_to\_group\_id, send\_email: bool)**
    * Beschreibung: Erstellt eine Dokumentaufgabe.
    * Parameter:
      * user: Der Benutzer, der die Aktualisierung durchführt (entweder Benutzer-ID oder UserAuthentication-Objekt).
      * document\_data: Die Dokumentdaten, die Feldinformationen enthalten.
      * title (str): Der Titel der Aufgabe.
      * description (str): Die Beschreibung der Aufgabe.
      * priority: Die Priorität der Aufgabe.
      * assigned\_to\_user\_id: Die ID des Benutzers, dem die Aufgabe zugewiesen werden soll.
      * assigned\_to\_group\_id: Die ID der Gruppe, der die Aufgabe zugewiesen werden soll.
      * send\_email (bool): Bestimmt, ob eine E-Mail gesendet werden soll oder nicht.
    * Gibt zurück:
      * Dict, das angibt, ob der Prozess erfolgreich war oder nicht.
    *   Beispiel:

        ```
        dict = create_document_task(user, document_data, "Herkunftsland außerhalb der EU", "Die Bestätigung kommt aus einem Land außerhalb der EU. Bitte fügen Sie das MRN-Dokument bei.", "hoch", 1007, None, False)
        ```
18. **set\_document\_sub\_org\_id(document\_data, sub\_org\_id)**
    * Beschreibung: Setzt die sub\_org\_id der angegebenen document\_data.
    * Parameter:
      * document\_data: Die Dokumentdaten, die Feldinformationen enthalten.
      * sub\_org\_id (str): Optionale Sub-Organisations-ID für die Filterung.
    *   Beispiel:

        ```
        set_document_sub_org_id(document_data, sub_org_id)
        ```
19. **get\_user\_by\_id(user\_id)**
    * Beschreibung: Holt den Benutzer mit der entsprechenden Benutzer-ID.
    * Parameter:
      * user\_id (str): Die ID des Benutzers.
    * Gibt zurück:
      * Der Benutzer mit der entsprechenden Benutzer-ID.
    *   Beispiel:

        ```
        user = get_user_by_id("123456")
        ```
20. **get\_group\_by\_id(group\_id)**
    * Beschreibung: Holt die Gruppe mit der entsprechenden Gruppen-ID.
    * Parameter:
      * group\_id (str): Die ID der Gruppe.
    * Gibt zurück:
      * Die Gruppe mit der entsprechenden Gruppen-ID.
    *   Beispiel:

        ```
        group = get_group_by_id("123456")
        ```
21. **add\_table\_column(table, col\_name, default\_value=None)**
    * Beschreibung: Fügt eine Spalte zur entsprechenden Tabelle hinzu.
    * Parameter:
      * table: Die Tabelle, in der die Spalte hinzugefügt werden soll.
      * col\_name: Der Name der Spalte.
      * default\_value (optional): Der Anfangswert für das Feld (Standard ist ein leerer String).
    *   Beispiel:

        ```
        add_table_column(table, "UNIT_PRICE_PER")
        ```
22. **get\_column\_value(row, column\_name, default\_value=None, is\_clean=False)**
    * Beschreibung: Holt einen Wert aus einer bestimmten Spalte.
    * Parameter:
      * row: Die Zeile, in der sich der Wert befindet.
      * col\_name: Der Name der Spalte.
      * default\_value (optional): Gibt default\_value zurück, wenn kein Feldwert gefunden wird.
      * is\_clean (optional): Wandelt den Wert in Großbuchstaben um und bereinigt ihn von Leerzeichen.
    *   Beispiel:

        ```
        original_unit_price = get_column_value(row, "ORIGINAL_UNIT_PRICE")
        ```
23. **set\_column\_value(row, column\_name, value)**
    * Beschreibung: Setzt einen Wert aus einer bestimmten Spalte.
    * Parameter:
      * row: Die Zeile, in der sich der Wert befindet.
      * col\_name: Der Name der Spalte.
      * value: Der Wert, der an der angegebenen Stelle gesetzt werden soll.
    * Gibt zurück:
      * True, wenn die Änderung erfolgreich war.
    *   Beispiel:

        ```
        success = set_column_value(row,"SUPPLIER_ID", supplier_id)
        ```
24. **set\_column\_date\_value(document\_data, row, column\_name, value, add\_days=0)**
    * Beschreibung: Setzt einen Wert aus einer bestimmten Spalte.
    * Parameter:
      * document\_data: Die Dokumentdaten, die Feldinformationen enthalten.
      * row: Die Zeile, in der sich der Wert befindet.
      * col\_name: Der Name der Spalte.
      * value: Der Datumswert, der im ISO-Format gesetzt werden soll (z. B. "2020-12-31").
      * add\_days (int): Fügt zusätzliche Tage zum angegebenen Datum hinzu.
    *   Beispiel:

        ```
        set_column_date_value(document_data, row, "DELIVERY_DATE", "2020-12-31", add_days=2)
        ```
25. **set\_column\_amount\_value(document\_data, row, column\_name, value)**
    * Beschreibung: Führt folgende Aktionen aus:
      * Konvertiert den Wert in einen String und setzt den Wert für die Spalte.
      * Setzt den Inhalt der Spalte auf den Wert.
      * Formatiert den Wert gemäß der Locale.
    * Parameter:
      * document\_data (dict): Die Dokumentdaten, die Feldinformationen enthalten.
      * row: Zeile der Tabellenzeile.
      * column\_name: Name der Spalte.
      * value: Wert, der gesetzt werden soll.
    *   Beispiel:

        ```
        set_column_amount_value(document_data, row, "UNIT_PRICE", str(unit_price))
        ```
26. **remove\_rows\_from\_table(document\_data, table\_name, count, start)**
    * Beschreibung: Entfernt Zeilen aus der angegebenen Tabelle.
    * Parameter:
      * document\_data (dict): Die Dokumentdaten, die Feldinformationen enthalten.
      * table\_name: Der Name der Tabelle.
      * count: Wie viele Zeilen gelöscht werden sollen.
      * start: Der Ausgangspunkt.
    *   Beispiel:

        ```
        remove_rows_from_table(document_data,"INVOICE_TABLE",count,start)   
        ```
27. **remove\_all\_rows\_except\_one\_from\_table(document\_data, line\_number)**
    * Beschreibung: Entfernt alle Zeilen außer einer aus der angegebenen Tabelle.
    * Parameter:
      * document\_data (dict): Die Dokumentdaten, die Feldinformationen enthalten.
      * line\_number: Die Nummer der Zeile, die nicht entfernt werden soll.
    *   Beispiel:

        ```
        remove_all_rows_except_one_from_table(document_data, line_number) 
        ```

Sie können auch einige der integrierten Python-Funktionen nutzen:

* abs(): Gibt den Absolutwert einer Zahl zurück.
* len(): Gibt die Länge (Anzahl der Elemente) eines Objekts, wie einer Liste oder einem String, zurück.
* isinstance(): Überprüft, ob ein Objekt eine Instanz einer bestimmten Klasse oder eines bestimmten Typs ist.
* print(): Gibt Ausgaben auf der Konsole aus.
* round(): Rundet eine Fließkommazahl auf eine bestimmte Anzahl von Dezimalstellen.
* str\_to\_bool(): Konvertiert einen String in einen booleschen Wert (True oder False).
* type(): Gibt den Typ eines Objekts zurück.
* dict(): Erstellt ein Wörterbuch-Objekt.
* list(): Erstellt ein Listen-Objekt.
* str(): Konvertiert einen Wert in einen String.
* float(): Konvertiert einen Wert in eine Fließkommazahl.
* int(): Konvertiert einen Wert in eine Ganzzahl.

Für weitere Details besuchen Sie die offizielle Python-Dokumentation: [Integrierte Funktionen](https://docs.python.org/3.12/library/functions.html).

#### String-Klassenfunktionen

Sie können auch diese Funktionen speziell für die Arbeit mit Strings verwenden:

* lower(): Wandelt alle Zeichen in einem String in Kleinbuchstaben um.
* upper(): Wandelt alle Zeichen in einem String in Großbuchstaben um.
* split(): Teilt einen String in eine Liste basierend auf einem Trennzeichen (z. B. Leerzeichen oder Komma).
* startswith(): Überprüft, ob ein String mit einem bestimmten Präfix beginnt.
* endswith(): Überprüft, ob ein String mit einem bestimmten Suffix endet.
* strip(): Entfernt führende oder nachfolgende Leerzeichen aus einem String.

#### Funktionen aus dem Python-Math-Modul

Diese Funktionen sind Teil des Math-Moduls und nützlich für mathematische Operationen:

* floor(): Gibt die größte Ganzzahl zurück, die kleiner oder gleich einer gegebenen Zahl ist.
* ceil(): Gibt die kleinste Ganzzahl zurück, die größer oder gleich einer gegebenen Zahl ist.

Für weitere Informationen, schauen Sie sich die offizielle Python-Dokumentation an: [Math-Modul-Funktionen](https://docs.python.org/3/library/math.html).

#### Reguläre Ausdrucksfunktion

* re.search(): Durchsucht einen String nach einem Muster und gibt das erste Ergebnis zurück.

Siehe weitere Details hier: [re.search-Dokumentation](https://docs.python.org/3/library/re.html#re.search).

#### Externe Funktionen

Hier sind einige nützliche Funktionen aus externen Bibliotheken:

* deepcopy(): Erstellt eine Kopie eines Objekts, einschließlich verschachtelter Objekte (aus dem copy-Modul).\
  [Deepcopy-Dokumentation](https://docs.python.org/3/library/copy.html#copy.deepcopy).
* levenshtein\_distance(): Berechnet die Anzahl der Änderungen (Einfügungen, Löschungen, Ersetzungen), die erforderlich sind, um einen String in einen anderen zu ändern. Diese Funktion ist in der [Jellyfish-Bibliothek](https://jamesturk.github.io/jellyfish/functions/) verfügbar.

#### Datum- und Zeitfunktionen

Sie können die folgenden Funktionen für die Arbeit mit Daten und Zeiten verwenden:

* strptime(): Konvertiert einen String in ein datetime-Objekt basierend auf einem bestimmten Format.
* strftime(): Formatiert ein datetime-Objekt in einen String basierend auf einem bestimmten Format.

Für weitere Informationen, überprüfen Sie die offizielle Dokumentation:\
[Datum- und Zeitfunktionen](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior).
