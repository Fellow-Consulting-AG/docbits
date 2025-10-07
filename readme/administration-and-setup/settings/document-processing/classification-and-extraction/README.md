# Klasyfikacja i ekstrakcja

## Przegląd

W ustawieniach **Klasyfikacja i ekstrakcja** możesz:

* Włączyć **Podział dokumentów** na podstawie kodów QR
* Skonfigurować **Formatowanie kwoty**
* Skonfigurować **Ekstrakcja tabeli**
* Przełączyć przetwarzanie nieobsługiwanych plików **ZUGFeRD**
* Zdefiniować specjalne zasady klasyfikacji
* Monitorować niestandardowo trenowane **Modele AI** używane w procesie klasyfikacji

Ta strona zawiera szczegółowe wyjaśnienie wszystkich dostępnych ustawień.

## **Uzyskiwanie dostępu do Ustawienia Klasyfikacja i ekstrakcja**

Aby uzyskać dostęp do **Klasyfikacja i ekstrakcja**, przejdź do:\
**Ustawienia → Przetwarzanie dokumentów → Klasyfikacja i ekstrakcja**

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_classification_and_extraction.png)

## Podział dokumentów

W sekcji **Podział dokumentów** możesz skonfigurować, czy przesłany dokument powinien być podzielony na wiele dokumentów za każdym razem, gdy na jednej ze stron pojawi się **Kod kreskowy**.

Aby aktywować tę funkcję:

1. Przejdź do sekcji **Podział dokumentów**.
2.  Otwórz menu rozwijane.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_14.png)
3.  Wybierz **Podział według kodu kreskowego/kodu QR**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_15.png)

Następnie będziesz mieć możliwość:

* Wybrać jeden lub więcej typów kodów kreskowych do wykrycia.
*   Określić wzorzec regex, który kod kreskowy musi spełniać, aby uruchomić podział dokumentu.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_16.png)

## Formatowanie kwoty

W sekcji **Formatowanie kwoty** masz dwie opcje:

* **Zezwalaj na zaokrąglanie podczas porównywania kwot:**\
  Jeśli włączone, podczas porównywania kwot dozwolona jest tolerancja ±0,5.\
  Jeśli wyłączone, obowiązuje domyślna tolerancja ±0,05.
* **Wymagaj dokładnego dopasowania do porównania kwot:**\
  Jeśli włączone, kwoty muszą być zgodne dokładnie, z zerową tolerancją.\
  Jeśli wyłączone, dozwolona jest tolerancja ±0,05.

<mark style="color:red;">**Uwaga**</mark>: Tylko jedno z tych ustawień może być aktywne jednocześnie.

## Ekstrakcja tabeli

Możesz wyodrębniać tabele z dokumentów, włączając **Ekstrakcja tabeli** lub **Ekstrakcja tabeli AI**. Wytrenowana tabela — niezależnie od tego, czy oparta na AI, czy ręczna — zawsze będzie powiązana z określonym dostawcą.

**Ekstrakcja tabeli:** Aktywuje ręczną **Ekstrakcja tabeli**. Tabele muszą być trenowane ręcznie.\
Dowiedz się więcej o ręcznym treningu [tutaj](../../../setup/document-training/training-line-fields-table-training/defining-tables-and-columns.md).

**Ekstrakcja tabeli AI:** Używa AI do automatycznego wyodrębniania tabel. Jeśli wyniki nie są wystarczająco dokładne, zaleca się przełączenie na ręczną **Ekstrakcja tabeli** dla lepszej kontroli i trenowania.

**Ekstrakcja tabeli dla elementu kosztowego:** Po włączeniu DocBits może wyodrębniać elementy kosztowe z tabel na poziomie wiersza i odpowiednio je klasyfikować.\
Szczegółowe wyjaśnienie dostępne [tutaj](table-extraction-for-costing-element.md).

**Automatyczne wyodrębnianie kodu podatkowego:** Po włączeniu system automatycznie wypełnia pole **Kod podatkowy** na ekranie weryfikacji — pod warunkiem, że pole kodu podatkowego jest skonfigurowane.\
Więcej informacji o tym ustawieniu [tutaj](auto-extract-tax-code.md).

**Model sztucznej inteligencji:** Pozwala określić, który **model AI** jest używany do ekstrakcji tabeli.\
Zobaczysz także tabelę pokazującą:

* Którzy **Dostawcy** używają którego modelu AI
* Czy używają E-Text
* Opcje usunięcia wpisu lub resetu danych treningowych

To ustawienie jest szczegółowo wyjaśnione [tutaj](ai-model.md).

## Dokument elektroniczny

**Proces nieobsługiwany ZUGFeRD PDF:** Jeśli włączone, nieobsługiwane wersje **ZUGFeRD** będą przetwarzane jako standardowe pliki PDF, a osadzony XML zostanie zignorowany.

Listę obsługiwanych wersji **ZUGFeRD** można znaleźć [tutaj](../../global-settings/document-types/edi/zugferd-1.0-2.1-and-2.3.md).

## **Zasady klasyfikacji**

W sekcji **Zasady klasyfikacji** możesz zdefiniować konkretne wzorce regex i kryteria, które pomogą systemowi automatycznie klasyfikować dokumenty podczas przetwarzania.

Aby uzyskać dostęp do tej sekcji, kliknij kartę **Zasady klasyfikacji** u góry strony.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_1.png)

### **Dodać nową zasadę klasyfikacji**

Aby utworzyć nową regułę:

1.  Kliknij **Dodać** w prawym górnym rogu.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_2.png)
2. Wypełnij następujące pola:
   * **Wzór**: Wzorzec regex, którego system powinien szukać, aby uruchomić klasyfikację.
   * **Typ**: Gdzie należy szukać wzorca (np. **Kod kreskowy**).
   * **Podorganizacja** _(opcjonalnie)_: Określ, której podorganizacji dotyczy reguła.
   * **Typ dokumentu**: Zdefiniuj typ dokumentu do przypisania, gdy wzorzec zostanie dopasowany.
   *   **Typ dokumentu podrzędnego** _(opcjonalnie)_: Określ podtyp dla bardziej szczegółowej klasyfikacji.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_3.png)
3.  Kliknij **Ratować**, aby zapisać swoją regułę klasyfikacji.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_4.png)

### **Redagować zasadę klasyfikacji**

Aby edytować istniejącą regułę:

1.  Kliknij trzy kropki w kolumnie **Akcje**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_5.png)
2.  Wybierz **Redagować**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_6.png)
3. Wprowadź żądane zmiany.
4.  Kliknij **Ratować**, aby zastosować aktualizacje.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_4.png)

### **Usuwać zasadę klasyfikacji**

Aby usunąć regułę:

1.  Kliknij trzy kropki w kolumnie **Akcje**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_5.png)
2.  Wybierz **Usuwać**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_7.png)

## Modele AI

Sekcja **Modele AI** wyświetla wszystkie modele trenowane na zamówienie, które zostały specjalnie dostrojone do Twoich potrzeb.

### Uzyskiwanie dostępu do sekcji Modele AI

Aby otworzyć tę sekcję, kliknij kartę **Modele AI** znajdującą się u góry strony.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_8.png)

### Kategorie modeli

Modele są zorganizowane w kategorie. Poniżej nazwy każdej kategorii wyświetlana jest liczba zawartych w niej modeli.\
Kliknij kategorię, aby zobaczyć jej szczegóły.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_9.png)

U góry strony wybranej kategorii zobaczysz kluczowe informacje o każdym modelu:

* **Typ**: Typ modelu.
* **Tylko pierwsza strona**: Wskazuje, czy model przetwarza tylko pierwszą stronę dokumentu.
* **Wersja**: Numer wersji modelu.

### Tabela modeli

Wszystkie modele w danej kategorii są wymienione w tabeli, która zawiera następujące informacje:

* **Nazwa**: Nazwa modelu.
* **Następny model**: Model, który będzie dalej przetwarzał wynik bieżącego modelu.
* **Typ dokumentu**: Główny typ dokumentu przypisywany przez model podczas klasyfikacji.
* **Podtypy dokumentów**: Podtypy, do których dokument jest dalej klasyfikowany.
* **Priorytet**: Poziom priorytetu, który określa pozycję modelu w kolejce klasyfikacji.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_11.png)

### Redagowanie modelu

Aby edytować model:

1.  Kliknij ikonę długopisu w kolumnie **Akcje** obok modelu, który chcesz edytować.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_10.png)
2. Zaktualizuj dostępne pola:
   * **Następny model**: Wybierz model, który powinien przetwarzać wynik z bieżącego modelu.
   * **Typ dokumentu**: Wybierz typ dokumentu, jako który model powinien klasyfikować dane wejściowe.
3.  Kliknij **Ratować**, aby zastosować zmiany.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_12.png)
