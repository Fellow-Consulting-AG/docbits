# Model sztucznej inteligencji

## Przegląd

Ustawienie **Model sztucznej inteligencji** pozwala zdefiniować, który model AI jest używany domyślnie do **ekstrakcji pól** i **ekstrakcji tabeli** podczas przetwarzania dokumentów.\
W tej sekcji możesz przejrzeć koszt tokenów dla każdego modelu oraz sprawdzić, który model jest obecnie przypisany do każdego dostawcy.

## Jak uzyskać dostęp

1.  Przejdź do **Ustawienia** → **Przetwarzanie dokumentów** → **Klasyfikacja i ekstrakcja**

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_classification_and_extraction.png)
2.  Przewiń w dół do sekcji **Ekstrakcja tabeli**

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_1.png)

## Opcje Modelu sztucznej inteligencji

Możesz wybierać spośród następujących modeli AI. Najedź kursorem na ikonę informacji w interfejsie, aby zobaczyć koszt tokenów na dokument dla wybranego modelu AI:

* **Full** – 2 tokeny za dokument
* **Fast** – 1 token za dokument
* **Turbo** – 1 token za dokument

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_2.png)

## Tabela przypisania Modelu sztucznej inteligencji

Możesz również skonfigurować specyficzne dla dostawcy **modele AI** bezpośrednio na ekranie **Walidacja**, co pozwala dostosować dokładność ekstrakcji dla poszczególnych dostawców.\
\
Więcej informacji znajdziesz w odpowiedniej dokumentacji [tutaj](../../../../end-user-and-partner-section/end-user-section/validation-screen/selecting-a-supplier-specific-ai-model-for-field-and-table-extraction.md).

Tabela przypisania wyświetla ustawienia modelu AI dla każdego dostawcy i zawiera następujące szczegóły:

* **Supplier ID** – Unikalny identyfikator dostawcy
* **AI Model** – Model AI obecnie przypisany do dostawcy
* **E-Text**: Wskazuje, czy funkcja E-Text jest włączona
* **Action** – Zawiera opcję usunięcia wpisu

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_3.png)

### Usuń wpis – Zresetuj ustawienia specyficzne dla dostawcy

Aby zresetować ustawienie modelu AI dostawcy do domyślnych:

1.  Kliknij ikonę kosza w kolumnie **Action** obok wpisu dostawcy.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_4.png)
2.  Pojawi się okno potwierdzenia—potwierdź, że chcesz usunąć wpis.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_5.png)

Po usunięciu dostawca wróci do korzystania z domyślnego **modelu AI** do **ekstrakcji pól** i **ekstrakcji tabeli**.
