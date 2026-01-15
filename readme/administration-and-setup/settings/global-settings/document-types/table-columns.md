# Kolumny tabeli

<figure><img src="../../../../.gitbook/assets/docbits_table_columns_overview.png" alt="Docbits Table Columns Overview"><figcaption></figcaption></figure>

#### Przegląd

Interfejs Kolumn Tabel w Docbits służy do określenia kolumn, które pojawiają się w tabelach danych dla każdego typu dokumentu. Każda kolumna może być skonfigurowana do przechowywania określonych typów danych, takich jak ciągi znaków lub wartości liczbowe, i może być istotna dla funkcji sortowania, filtrowania i raportowania w Docbits.

#### Główne funkcje i opcje

1. **Konfiguracja kolumn**:
* **Nazwa kolumny**: Identyfikator kolumny w bazie danych.
* **Tytuł**: Czytelny dla człowieka tytuł kolumny, który pojawi się w interfejsie.
* **Typ kolumny**: Określa typ danych kolumny (np. CIĄG ZNAKÓW, KWOTA), co determinuje, jakiego rodzaju dane mogą być przechowywane w kolumnie.
* **Nazwa tabeli**: Wskazuje, do której tabeli należy kolumna, łącząc ją z określonym typem dokumentu, takim jak TABELA_FAKTUR.
2. **Działania**:
* **Edytuj**: Modyfikuj ustawienia istniejącej kolumny.
* **Usuń**: Usuń kolumnę z tabeli, co jest przydatne, jeśli dane nie są już wymagane lub jeśli struktura danych typu dokumentu ulega zmianie.
3. **Dodawanie nowych kolumn i tabel**:
* **Dodaj nową kolumnę tabeli**: Otwiera okno dialogowe, w którym można zdefiniować nową kolumnę, w tym jej nazwę, czy jest wymagana, jej typ danych i tabelę, do której należy.
* **Utwórz nową tabelę**: Pozwala na utworzenie nowej tabeli, definiując unikalną nazwę, która będzie używana do przechowywania danych związanych z określonym zestawem typów dokumentów.

<figure><img src="../../../../.gitbook/assets/docbits_create_new_table.png" alt="Docbits Create New Table"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/docbits_table_columns_integrity.png" alt="Docbits Table Columns Integrity"><figcaption></figcaption></figure>

Ta sekcja jest kluczowa dla utrzymania integralności strukturalnej i użyteczności danych w systemie Docbits, zapewniając, że dane wyodrębnione z dokumentów są przechowywane w dobrze zorganizowany i dostępny sposób.

{% @jira/embed url="https://fellowpro.atlassian.net/browse/DOCB-2493" %}
