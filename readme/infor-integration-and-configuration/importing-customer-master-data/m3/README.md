# M3

## Importowanie szablonu połączenia API w Infor M3

Ten przewodnik wyjaśnia, jak zaimportować szablon połączenia API, aby szybko skonfigurować kluczowe ustawienia integracji z Infor M3. Użycie szablonu pozwala utworzyć wstępnie zdefiniowaną konfigurację połączenia, upraszczając proces i zapewniając spójność.

<mark style="color:red;">**Uwaga**</mark>: Szczegółowe konfiguracje określonych obszarów, takich jak Auto Accounting, integracja z dostawcami, zamówienia zakupu czy ekstrakcja tabel dla elementów kosztowych, znajdziesz w odpowiedniej dokumentacji:

* [Automatyczne księgowanie](auto-accounting.md)
* [Dostawcy i zamówienia zakupu](suppliers-and-purchase-orders.md)
* [Jak zaimportować wszystkich dostawców](how-to-import-all-suppliers.md)
* [Ekstrakcja tabel dla elementu kosztowego](table-extraction-for-costing-element.md)

### **Pobierz szablon**

Przed importem pobierz wymagany szablon połączenia, korzystając z poniższego pliku:

{% file src="../../../.gitbook/assets/DocBits-Dev-Import-Template.xml" %}

### Importowanie szablonu

#### Kroki importu szablonu połączenia

1. **Uzyskaj dostęp do Infor ION Desk:**
   *   Przejdź do **InforOS** → **ION Desk** → **Connect** → **Connection Points**.

       ![](https://lh7-us.googleusercontent.com/ySRjNzMXFzwSOYKx9hnlKLPHPuXpmfTvRADBfV6cpT8ajiEUbS4oXpd9InhXG09mHLakhqBTJMH4yQJNG5z9RXmbAjh8YbuGhxnXSeooIH_r3RAGOvJE6Ok67ST_272zFfhB_TTFYg3b-NwFq0CAv2o)
2. **Zaimportuj szablon:**
   *   Kliknij przycisk **Import**.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/m3_import_2.png)
   * Wybierz odpowiedni **Template File** z lokalnego systemu.
   *   Kliknij **OK**, aby rozpocząć proces importu.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/m3_import_3.png)
3. **Potwierdzenie:**
   *   Jeśli import zakończy się powodzeniem, zostanie wyświetlony komunikat potwierdzający.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/m3_import_4.png)
4. **Konfiguracja po imporcie:**
   * Po zaimportowaniu szablonu możesz dostosować konkretne ustawienia połączenia według potrzeb.
   * Pamiętaj o zaimportowaniu lub skonfigurowaniu swojego **Service Account** do uwierzytelniania i kontroli dostępu.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/m3_import_5.png)
