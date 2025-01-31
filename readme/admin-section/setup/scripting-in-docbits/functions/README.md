# Funkcje

**Dokumentacja funkcjonalna**

Ten moduł zawiera funkcje do manipulacji danymi dokumentów oraz wykonywania różnych operacji związanych z polami dokumentów.

**Funkcje**

1. **set\_field\_value(document\_data, field\_name, value)**
   * Opis: Ustawia wartość pola w danych dokumentu.
   * Parametry:
     * document\_data (dict): Dane dokumentu zawierające informacje o polach.
     * field\_name (str): Nazwa pola do ustawienia.
     * value: Wartość do ustawienia dla pola.
   *   Przykład:

       ```
       set_field_value(document_data, "name", "John Doe")
       ```
2. **set\_date\_value(document\_data, field\_name, value, add\_days=0, skip\_weekend=False)**
   * Opis: Ustawia wartość pola daty w danych dokumentu.
   * Parametry:
     * document\_data (dict): Dane dokumentu zawierające informacje o polach.
     * field\_name (str): Nazwa pola daty do ustawienia.
     * value: Wartość daty do ustawienia w formacie ISO (np. "2020-12-31").
     * add\_days (int): Dodaje dodatkowe dni do podanej daty.
     * skip\_weekend (bool): Pomija datę, jeśli przypada na weekend.
   *   Przykład:

       ```
       set_date_value(document_data, "promised_delivery_date", "2020-12-31", add_days=2, skip_weekend=True)
       ```
3. **set\_amount\_value(document\_data, field\_name, value)**
   * Opis: Ustawia wartość pola kwoty w danych dokumentu.
   * Parametry:
     * document\_data (dict): Dane dokumentu zawierające informacje o polach.
     * field\_name (str): Nazwa pola do ustawienia.
     * value: Wartość do ustawienia dla pola.
   *   Przykład:

       ```
       set_amount_value(document_data, "number", "123456")
       ```
4. **get\_field\_value(document\_data, field\_name, default\_value=None, is\_clean=False)**
   * Opis: Pobiera wartość pola z danych dokumentu.
   * Parametry:
     * document\_data (dict): Dane dokumentu zawierające informacje o polach.
     * field\_name (str): Nazwa pola do ustawienia.
     * default\_value (opcjonalnie): Zwraca default\_value, jeśli nie znaleziono wartości pola.
     * is\_clean (opcjonalnie): Zmienia wartość na wielkie litery i czyści ją z pustych miejsc.
   * Zwraca:
     * Wartość pola.
   *   Przykład:

       ```
       value = get_field_value(document_data, "name")
       ```
5. **create\_new\_field(field\_name, value="")**
   * Opis: Tworzy nowe pole o określonej nazwie i wartości.
   * Parametry:
     * field\_name (str): Nazwa pola do utworzenia.
     * value: Wartość początkowa dla pola (domyślnie jest to pusty ciąg).
   * Zwraca:
     * Słownik nowo utworzonego pola.
   *   Przykład:

       ```
       dict = create_new_field("address", "")
       ```
6. **delete\_field(document\_data, field\_name)**
   * Opis: Usuwa pole z danych dokumentu.
   * Parametry:
     * document\_data (dict): Dane dokumentu zawierające informacje o polach.
     * field\_name (str): Nazwa pola do ustawienia.
   * Zwraca:
     * Document\_data jako json i jako dict po usunięciu pola.
   *   Przykład:

       ```
       //json, dict = (document_data, "name")
       ```
7. **set\_is\_required(document\_data, field\_name, value)**
   * Opis: Ustawia atrybut 'is\_required' pola w danych dokumentu.
   * Parametry:
     * document\_data (dict): Dane dokumentu zawierające informacje o polach.
     * field\_name (str): Nazwa pola do ustawienia.
     * value: Wartość do ustawienia dla pola.
   *   Przykład:

       ```
       set_is_required(document_data, "bank_id", True)
       ```
8. **set\_force\_validation(document\_data, field\_name, value)**
   * Opis: Ustawia atrybut 'force\_validation' pola w danych dokumentu.
   * Parametry:
     * document\_data (dict): Dane dokumentu zawierające informacje o polach.
     * field\_name (str): Nazwa pola do ustawienia.
     * value (bool): Wartość do ustawienia dla pola.
   *   Przykład:

       ```
       set_force_validation(document_data, 'supplier_name', True)
       ```
9. **set\_field\_as\_invalid(document\_data, field\_name, message, code=None)**
   * Opis: Oznacza pole jako nieważne w danych dokumentu.
   * Parametry:
     * document\_data (dict): Dane dokumentu zawierające informacje o polach.
     * field\_name (str): Nazwa pola do oznaczenia jako nieważne.
     * message (str): Komunikat walidacji dla pola.
     * code (opcjonalnie): Kod błędu dla walidacji (domyślnie None).
   *   Przykład:

       ```
       --set_field_as_invalid(document_data, "email", "Invalid email format", "EMAIL_FORMAT_INVALID")
       ```
10. **set\_field\_attribute(document\_data, field\_name, attribute\_name, value)**
    * Opis: Ustawia niestandardowy atrybut pola w danych dokumentu.
    * Parametry:
      * document\_data (str): Dane dokumentu zawierające informacje o polach.
      * field\_name (str): Nazwa pola do ustawienia.
      * attribute\_name (str): Nazwa atrybutu do ustawienia.
      * value (bool): Wartość do ustawienia dla atrybutu.
    *   Przykład:

        ```
        set_field_attribute(document_data, "address", "is_verified", True)
        ```
11. **is\_supplier\_valid(user: UserAuthentication, filter\_data\_json, sub\_org\_id=None)**
    * Opis: Sprawdza, czy dostawca jest ważny na podstawie podanych kryteriów.
    * Parametry:
      * user (UserAuthentication): Użytkownik uwierzytelniony.
      * filter\_data\_json: Kryteria filtrowania do walidacji dostawcy.
      * sub\_org\_id (opcjonalnie): Opcjonalny identyfikator podorganizacji do filtrowania.
    * Zwraca:
      * True, jeśli użytkownik jest ważny.
      * False, jeśli użytkownik nie jest ważny.
    *   Przykład:

        ```
        bool = is_supplier_valid(user, {"name": "Supplier Inc."})
        ```
12. **get\_document\_content(document\_data)**
    * Opis: Zwraca zawartość dokumentu na podstawie danych dokumentu.
    * Parametry:
      * document\_data (str): Dane dokumentu zawierające informacje o polach.
    * Zwraca:
      * Zawartość dokumentu danych dokumentu.
    *   Przykład:

        ```
        document_content = get_document_content(doc)
        ```
13. **update\_document\_status\_with\_doc\_id(doc\_id, user, org\_id, status, message=None, doc\_classification\_class=None)**
    * Opis: Aktualizuje status dokumentu o podanym identyfikatorze.
    * Parametry:
      * doc\_id (str): Identyfikator dokumentu do aktualizacji.
      * user: Użytkownik wykonujący aktualizację (identyfikator użytkownika lub obiekt UserAuthentication).
      * org\_id: Identyfikator organizacji, do której należy dokument.
      * status (str): Nowy status dokumentu.
      * message: Opcjonalna wiadomość związana z aktualizacją statusu.
      * doc\_classification\_class: Opcjonalna klasa klasyfikacji dokumentu.
    *   Przykład:

        ```
        update_document_status_with_doc_id("123456", user, "org_id", "approved", "Document approved")
        ```
14. **get\_lov\_values(org\_id, key, return\_type="list\_of\_objects", sub\_org\_id=None)**
    * Opis: Pobiera wartości LOV z określonego org\_id.
    * Parametry:
      * org\_id: Identyfikator organizacji, do której należy dokument.
      * return\_type (opcjonalnie): Typ, w jakim dane powinny być zwrócone.
      * sub\_org\_id (opcjonalnie): Opcjonalny identyfikator podorganizacji do filtrowania.
    * Zwraca:
      * Wartości LOV jako lista obiektów lub jako lista.
    *   Przykład:

        ```
        supplier_to_check = get_lov_values(org_id, 'BlacklistSupplier', return_type="list_of_values")
        ```
15. **format\_decimal\_to\_locale(value, to\_locale="en\_US.UTF-8", max\_decimal\_places=4, min\_decimal\_places=2)**
    * Opis: Formatuje wartość dziesiętną do formatu en\_US.UTF-8.
    * Parametry:
      * value: Wartość, która powinna być sformatowana.
      * to\_locale (opcjonalnie): Format, w jakim wartość ma być przekształcona.
      * max\_decimal\_places (opcjonalnie): Maksymalna liczba miejsc dziesiętnych, które powinny być brane pod uwagę.
      * min\_decimal\_places (opcjonalnie): Minimalna liczba miejsc dziesiętnych, które powinny być brane pod uwagę.
    * Zwraca:
      * Sformatowana wartość.
    *   Przykład:

        ```
        formatted_value = format_decimal_to_locale(value, document_json['amount_format_locale'])
        ```
16. **compare\_values(value1, value2)**
    * Opis: Porównuje dwie wartości pod kątem równości, obsługując różne typy danych.
    * Parametry:
      * value1: Pierwsza wartość do porównania.
      * value2: Druga wartość do porównania.
    * Zwraca:
      * True, jeśli wartości są równe, i False, jeśli się różnią.
    *   Przykład:

        ```
        result = compare_values(10, "10")
        ```
17. **create\_document\_task( user, document\_data, title, description, priority,**\
    **assigned\_to\_user\_id, assigned\_to\_group\_id, send\_email: bool)**
    * Opis: Tworzy zadanie dokumentu.
    * Parametry:
      * user: Użytkownik wykonujący aktualizację (identyfikator użytkownika lub obiekt UserAuthentication).
      * document\_data: Dane dokumentu zawierające informacje o polach.
      * title (str): Tytuł zadania.
      * description (str): Opis zadania.
      * priority: Priorytet zadania.
      * assigned\_to\_user\_id: Identyfikator użytkownika, do którego zadanie powinno być przypisane.
      * assigned\_to\_group\_id: Identyfikator grupy, do której zadanie powinno być przypisane.
      * send\_email (bool): Określa, czy e-mail powinien być wysłany, czy nie.
    * Zwraca:
      * Dict, który wskazuje, czy proces był udany, czy nie.
    *   Przykład:

        ```
        dict = create_document_task(user, document_data, "Country of origin outside the EU", "The confirmation comes from a country outside the EU. Please attach the MRN document.", "high", 1007, None, False)
        ```
18. **set\_document\_sub\_org\_id(document\_data, sub\_org\_id)**
    * Opis: Ustawia sub\_org\_id dla określonych danych dokumentu.
    * Parametry:
      * document\_data: Dane dokumentu zawierające informacje o polach.
      * sub\_org\_id (str): Opcjonalny identyfikator podorganizacji do filtrowania.
    *   Przykład:

        ```
        set_document_sub_org_id(document_data, sub_org_id)
        ```
19. **get\_user\_by\_id(user\_id)**
    * Opis: Pobiera użytkownika o odpowiadającym identyfikatorze użytkownika.
    * Parametry:
      * user\_id (str): Identyfikator użytkownika.
    * Zwraca:
      * Użytkownika o odpowiadającym identyfikatorze użytkownika.
    *   Przykład:

        ```
        user = get_user_by_id("123456")
        ```
20. **get\_group\_by\_id(group\_id)**
    * Opis: Pobiera grupę o odpowiadającym identyfikatorze grupy.
    * Parametry:
      * group\_id (str): Identyfikator grupy.
    * Zwraca:
      * Grupę o odpowiadającym identyfikatorze grupy.
    *   Przykład:

        ```
        group = get_group_by_id("123456")
        ```
21. **add\_table\_column(table, col\_name, default\_value=None)**
    * Opis: Dodaje kolumnę do odpowiedniej tabeli.
    * Parametry:
      * table: Tabela, do której kolumna powinna być dodana.
      * col\_name: Nazwa kolumny.
      * default\_value (opcjonalnie): Wartość początkowa dla pola (domyślnie jest to pusty ciąg).
    *   Przykład:

        ```
        add_table_column(table, "UNIT_PRICE_PER")
        ```
22. **get\_column\_value(row, column\_name, default\_value=None, is\_clean=False)**
    * Opis: Pobiera wartość z określonej kolumny.
    * Parametry:
      * row: Wiersz, w którym znajduje się wartość.
      * col\_name: Nazwa kolumny.
      * default\_value (opcjonalnie): Zwraca default\_value, jeśli nie znaleziono wartości pola.
      * is\_clean (opcjonalnie): Zmienia wartość na wielkie litery i czyści ją z pustych miejsc.
    *   Przykład:

        ```
        original_unit_price = get_column_value(row, "ORIGINAL_UNIT_PRICE")
        ```
23. **set\_column\_value(row, column\_name, value)**
    * Opis: Ustawia wartość w określonej kolumnie.
    * Parametry:
      * row: Wiersz, w którym znajduje się wartość.
      * col\_name: Nazwa kolumny.
      * value: Wartość, która zostanie ustawiona w określonym miejscu.
    * Zwraca:
      * True, jeśli zmiana była udana.
    *   Przykład:

        ```
        success = set_column_value(row,"SUPPLIER_ID", supplier_id)
        ```
24. **set\_column\_date\_value(document\_data, row, column\_name, value, add\_days=0)**
    * Opis: Ustawia wartość w określonej kolumnie.
    * Parametry:
      * document\_data: Dane dokumentu zawierające informacje o polach.
      * row: Wiersz, w którym znajduje się wartość.
      * col\_name: Nazwa kolumny.
      * value: Wartość daty do ustawienia w formacie ISO (np. "2020-12-31").
      * add\_days (int): Dodaje dodatkowe dni do podanej daty.
    *   Przykład:

        ```
        set_column_date_value(document_data, row, "DELIVERY_DATE", "2020-12-31", add_days=2)
        ```
25. **set\_column\_amount\_value(document\_data, row, column\_name, value)**
    * Opis: Wykonuje następujące działania:
      * Konwertuje wartość na ciąg i ustawia wartość dla kolumny.
      * Ustawia zawartość kolumny na wartość.
      * Formatuje wartość zgodnie z lokalizacją.
    * Parametry:
      * document\_data (dict): Dane dokumentu zawierające informacje o polach.
      * row: Wiersz linii tabeli.
      * column\_name: Nazwa kolumny.
      * value: Wartość do ustawienia.
    *   Przykład:

        ```
        set_column_amount_value(document_data, row, "UNIT_PRICE", str(unit_price))
        ```
26. **remove\_rows\_from\_table(document\_data, table\_name, count, start)**
    * Opis: Usuwa wiersze z określonej tabeli.
    * Parametry:
      * document\_data (dict): Dane dokumentu zawierające informacje o polach.
      * table\_name: Nazwa tabeli.
      * count: Ile linii powinno zostać usuniętych.
      * start: Punkt początkowy.
    *   Przykład:

        ```
        remove_rows_from_table(document_data,"INVOICE_TABLE",count,start)   
        ```
27. **remove\_all\_rows\_except\_one\_from\_table(document\_data, line\_number)**
    * Opis: Usuwa wszystkie wiersze z wyjątkiem jednego z określonej tabeli.
    * Parametry:
      * document\_data (dict): Dane dokumentu zawierające informacje o polach.
      * line\_number: Numer linii, która nie powinna zostać usunięta.
    *   Przykład:

        ```
        remove_all_rows_except_one_from_table(document_data, line_number) 
        ```

Możesz również wykorzystać niektóre z wbudowanych funkcji Pythona:

* abs(): Zwraca wartość bezwzględną liczby.
* len(): Zwraca długość (liczbę elementów) obiektu, takiego jak lista lub ciąg.
* isinstance(): Sprawdza, czy obiekt jest instancją określonej klasy lub typu.
* print(): Wyświetla wynik w konsoli.
* round(): Zaokrągla liczbę zmiennoprzecinkową do określonej liczby miejsc dziesiętnych.
* str\_to\_bool(): Konwertuje ciąg na wartość logiczną (True lub False).
* type(): Zwraca typ obiektu.
* dict(): Tworzy obiekt słownika.
* list(): Tworzy obiekt listy.
* str(): Konwertuje wartość na ciąg.
* float(): Konwertuje wartość na liczbę zmiennoprzecinkową.
* int(): Konwertuje wartość na liczbę całkowitą.

Aby uzyskać więcej informacji, odwiedź oficjalną dokumentację Pythona: [Funkcje wbudowane](https://docs.python.org/3.12/library/functions.html).

#### Funkcje klasy String

Możesz również używać tych funkcji specjalnie do pracy z ciągami:

* lower(): Konwertuje wszystkie znaki w ciągu na małe litery.
* upper(): Konwertuje wszystkie znaki w ciągu na wielkie litery.
* split(): Dzieli ciąg na listę na podstawie delimitera (np. spacji lub przecinka).
* startswith(): Sprawdza, czy ciąg zaczyna się od określonego prefiksu.
* endswith(): Sprawdza, czy ciąg kończy się na określony sufiks.
* strip(): Usuwa wszelkie wiodące lub końcowe białe znaki z ciągu.

#### Funkcje z modułu matematycznego Pythona

Te funkcje są częścią modułu matematycznego i są przydatne do operacji matematycznych:

* floor(): Zwraca największą liczbę całkowitą mniejszą lub równą danej liczbie.
* ceil(): Zwraca najmniejszą liczbę całkowitą większą lub równą danej liczbie.

Aby uzyskać więcej informacji, zapoznaj się z oficjalną dokumentacją Pythona: [Funkcje modułu matematycznego](https://docs.python.org/3/library/math.html).

#### Funkcja wyrażeń regularnych

* re.search(): Wyszukuje wzór w ciągu i zwraca pierwsze dopasowanie.

Zobacz więcej szczegółów tutaj: [Dokumentacja re.search](https://docs.python.org/3/library/re.html#re.search).

#### Funkcje zewnętrzne

Oto kilka przydatnych funkcji z zewnętrznych bibliotek:

* deepcopy(): Tworzy kopię obiektu, w tym zagnieżdżonych obiektów (z modułu copy).\
  [Dokumentacja deepcopy](https://docs.python.org/3/library/copy.html#copy.deepcopy).
* levenshtein\_distance(): Oblicza liczbę edycji (wstawień, usunięć, zamian) wymaganych do przekształcenia jednego ciągu w inny. Ta funkcja jest dostępna w [bibliotece Jellyfish](https://jamesturk.github.io/jellyfish/functions/).

#### Funkcje daty i czasu

Możesz używać następujących funkcji do pracy z datami i czasem:

* strptime(): Konwertuje ciąg na obiekt datetime na podstawie określonego formatu.
* strftime(): Formatuje obiekt datetime na ciąg na podstawie określonego formatu.

Aby uzyskać więcej informacji, sprawdź oficjalną dokumentację:\
[Funkcje daty i czasu](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior).
