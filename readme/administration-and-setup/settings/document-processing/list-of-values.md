# Lista wartości

## Przegląd

Funkcja **Lista wartości** umożliwia tworzenie i zarządzanie zdefiniowanymi zestawami wartości. Jest to szczególnie przydatne do konfigurowania rozwijanych menu w sekcji [**Pola**](../global-settings/document-types/fields/), które mogą być później używane w **Walidacji pól**.

Te listy mogą być dostosowane do różnych podorganizacji i wspierają wiele języków, co zapewnia elastyczność w **DocBits**.

## Jak uzyskać dostęp?

Możesz uzyskać dostęp do **Listy wartości**, przechodząc do **Ustawienia → Przetwarzanie dokumentów → Lista wartości**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_list_of_values.png)

## Jak dodać lub usunąć listę

### Utwórz nową listę wartości

1.  Kliknij **Nowy** w prawym górnym rogu ekranu.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_1.png)
2. Wprowadź **Nazwa** dla swojej listy.
3. _(Opcjonalnie)_ Wybierz **Podorganizację**, dla której lista powinna być aktywna.
4.  Kliknij **Ratować**, aby utworzyć listę.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_2.png)

### Jak usunąć listę

Aby usunąć listę, kliknij ikonę kosza obok odpowiedniej listy.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_13.png)

<mark style="color:red;">**Uwaga**</mark>: Lista zostanie usunięta natychmiast. Listy oznaczone tagiem [**Standard**](list-of-values.md#listy-i-wiersze-zdefiniowane-przez-system) nie mogą być usuwane.

## Jak dodać, edytować lub usunąć wartości z istniejącej listy

Możesz zarządzać wartościami w istniejącej **Liście wartości** za pomocą jednej z następujących metod:

* [**Ręczne dodawanie wartości**](list-of-values.md#reczne-dodawanie-wartosci) – Wprowadź wartości indywidualnie przez interfejs.
* [**Importowanie wartości z pliku CSV**](list-of-values.md#importowanie-wartosci-z-pliku-csv) – Prześlij plik CSV, aby dodać wiele wartości jednocześnie.

### Ręczne dodawanie wartości

1.  Kliknij na listę, którą chcesz zmodyfikować.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_3.png)
2.  Kliknij na **Akcje.**

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_4.png)
3.  Kliknij na **Dodaj wiersz.**

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_5.png)

Teraz możesz określić wiele właściwości dla każdego wpisu:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_6.png)

**Wartość**: To jest sposób, w jaki element będzie przechowywany wewnętrznie w **DocBits**. Pozostaje taki sam we wszystkich językach i służy również jako domyślny tekst wyświetlany podczas walidacji pola, jeśli nie określono etykiety dla wybranego języka.

**Etykieta**: To jest tekst wyświetlany na ekranie walidacji, w zależności od wybranego języka. Jeśli nie ma dostępnej etykiety dla aktywnego języka w DocBits, system domyślnie wyświetli **Wartość**.

**Język**: Określa język, w którym etykieta będzie wyświetlana.\
Bardziej szczegółowe wyjaśnienie można znaleźć [tutaj](list-of-values.md#dodaj-tlumaczenia-do-swoich-wartosci).

**Podorganizacje**: Określa, dla której **podorganizacji** wiersz powinien być aktywny. Jeśli pozostawisz puste, wiersz będzie dostępny dla wszystkich organizacji.

**Synonimy**: Tutaj możesz określić dodatkowe wartości, które pomogą w trenowaniu twojego dokumentu.\
Na przykład, jeśli **EUR** jest twoją główną **wartością**, możesz dodać EURO i € jako **synonimy**. Gdy dokument jest trenowany przy użyciu dowolnego z tych **synonimów**, **DocBits** automatycznie rozpozna i wybierze EUR jako odpowiadającą wartość z twojej listy.\
<mark style="color:red;">**Uwaga**</mark>: Każdy synonim musi być potwierdzony przez naciśnięcie **Enter**, aby dodać go do listy.

4.  Po wprowadzeniu wszystkich pożądanych właściwości kliknij przycisk **Ratować**, aby dodać wiersz.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_11.png)

### Importowanie wartości z pliku CSV

Aby dodać wiele wartości jednocześnie za pomocą importu CSV:

1.  Kliknij na listę, którą chcesz zaktualizować.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_3.png)
2.  Kliknij **Akcje**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_4.png)
3.  Kliknij na **Prześlij plik CSV**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_7.png)
4. Kliknij **Plik**, aby przeszukać i wybrać plik CSV, który chcesz przesłać.
5. Wybierz odpowiedni **Rozgranicznik** używany w pliku CSV (`;` lub `,`).
6.  Kliknij **Wgrywać**, aby zaimportować wartości.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_8.png)

### Edytowanie istniejących wartości

1. Zlokalizuj wiersz, który chcesz edytować.
2. Kliknij trzy kropki w kolumnie **Akcje**.
3.  Wybierz **Redagować** z rozwijanego menu.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_10.png)
4. Wprowadź wymagane zmiany.
5.  Kliknij **Ratować**, aby zastosować zmiany.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_11.png)

### Usuwanie wartości

1. Zlokalizuj wiersz, który chcesz usunąć.
2. Kliknij trzy kropki w kolumnie **Akcje**.
3.  Wybierz **Usuwać** z rozwijanego menu.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_12.png)

<mark style="color:red;">**Uwaga**</mark>: Wiersz zostanie usunięty natychmiast. Wiersze oznaczone tagiem [**Domyślny**](list-of-values.md#listy-i-wiersze-zdefiniowane-przez-system) nie mogą być usuwane.

## Dodaj tłumaczenia do swoich wartości

Możesz dodać tyle tłumaczeń, ile jest obsługiwanych języków w **DocBits**.

Aby dodać tłumaczenie:

1.  Kliknij ikonę plusa (+).

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_14.png)
2.  Wybierz język z rozwijanego menu.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_15.png)
3.  Wprowadź pożądane tłumaczenie w polu **Etykieta**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_16.png)
4.  Aby dodać kolejne tłumaczenie, kliknij ponownie ikonę plusa (+).

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_17.png)
5.  Aby usunąć tłumaczenie, kliknij ikonę kosza.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_18.png)
6.  Po zakończeniu kliknij przycisk **Ratować**, aby zapisać swoje tłumaczenia.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_19.png)

<mark style="color:red;">**Uwaga**</mark>: Jeśli nie ma dostępnej **Etykiety** dla aktywnego języka, DocBits domyślnie wyświetli **Wartość**.

## Listy i wiersze zdefiniowane przez system

Niektóre listy są wstępnie utworzone przez system i oznaczone tagiem **Standard**. Te listy nie mogą być usuwane, ale możesz dodać nowe wiersze do nich i usunąć te nowo dodane wiersze, jeśli zajdzie taka potrzeba.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_9.png)

W ramach tych standardowych list, niektóre wiersze są oznaczone tagiem **Domyślny**—są to wpisy zdefiniowane przez system. Możesz dodać nowe **etykiety** w różnych językach, ale te domyślne wiersze nie mogą być usuwane.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_20.png)
