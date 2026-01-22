# ZUGFeRD 1.0, 2.1 i 2.3

{% embed url="https://youtu.be/AxrHNEmmXtg" %}
DocBits E-Invoice Tutorial: Process XRechnung / ZUGFeRD (Factur-X), Validate Data & Automate Workflows
{% endembed %}

## **Obsługiwane wersje ZUGFeRD**

Aktualnie obsługiwane wersje ZUGFeRD to:

* **1.0**
* **2.1** (zgodna z FACTUR-X 1.0.05)
* **2.3** (zgodna z FACTUR-X 1.07.2)

#### Aktywacja i modyfikacja standardu

Standard ZUGFeRD jest domyślnie zawsze aktywny, ale w razie potrzeby możesz go modyfikować.

### **Kroki modyfikacji Ustawienia ZUGFeRD:**

1. Przejdź do **Ustawienia → Ustawienia globalne → Typy dokumentów → Faktura**.
2.  Kliknij **E-dokument**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/zugferd_1.png)
3. Pojawi się lista wszystkich dostępnych e-dokumentów.
4.  Zlokalizuj wersję **ZUGFeRD**, którą chcesz zmodyfikować.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/zugferd_2.png)

## **Extraction Transformation i konfiguracja ścieżek XML:**

W ustawieniach **Extraction Transformation** możesz zdefiniować ścieżkę do zlokalizowania określonych informacji w pliku XML i zapisać je w nowej strukturze, co ułatwia dostęp do danych.\
[<mark style="color:red;">**Uwaga**</mark>](#user-content-fn-1)[^1]: Jeśli korzystasz z tej funkcjonalności, musisz używać nowo utworzonych ścieżek XML, a nie oryginalnych ścieżek XML, w **Preview** i **Extraction Path**.

### **Kroki modyfikacji pliku Extraction Transformation:**

1. Otwórz **Extraction Transformation**.
2. Utwórz nowy szkic, klikając **ikonę ołówka**.
3. Wybierz nowo utworzony szkic.
4. Utwórz nowe pole lub zmodyfikuj istniejące.
5. Ustaw żądaną ścieżkę do ekstrakcji danych.
6. Kliknij **Ratować**.

### Ważne uwagi:

* **Plik Preview** jest używany tylko dla **FACTUR-X**, a nie dla **ZUGFeRD**. ZUGFeRD użyje oryginalnego **PDF**.

## Konfiguracja Preview PDF

**Konfiguracja Preview PDF** służy do generowania czytelnej dla użytkownika wersji dokumentu. Możesz dostosować ją za pomocą HTML do swoich potrzeb.

### **Kroki modyfikacji pliku Preview:**

1. Otwórz **Preview**.
2. Utwórz nowy szkic, klikając **ikonę ołówka**.
3. Wybierz nowo utworzony szkic.
4. Utwórz nowe pole lub zmodyfikuj istniejące.
5. Ustaw żądaną ścieżkę do ekstrakcji danych.
6. Kliknij **Ratować**.

## Konfiguracja Extraction Paths

**Konfiguracja Extraction Paths** służy do wyodrębniania danych i wypełniania pól na **ekranie walidacji**, takich jak tabela faktury lub pola skonfigurowane w układzie faktury.

### **Kroki modyfikacji** **Extraction Paths**:

1. Otwórz **Extraction Paths**.
2. Utwórz nowy szkic, klikając **ikonę ołówka**.
3. Wybierz nowo utworzony szkic.
4. Utwórz nowe pole lub zmodyfikuj istniejące.
5.  Lewa strona reprezentuje **DocBits field ID**, które można znaleźć w **Ustawienia → Ustawienia globalne → Typy dokumentów → Faktura → Pola**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/zugferd_3.png)

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/zugferd_4.png)
6. Prawa strona reprezentuje **ścieżkę do pola** utworzonego w Extraction Transformation.
7. Kliknij **Ratować**.

Postępując zgodnie z tymi krokami, możesz zapewnić dokładne wyodrębnianie danych i ich walidację dla faktur ZUGFeRD.

[^1]: 
