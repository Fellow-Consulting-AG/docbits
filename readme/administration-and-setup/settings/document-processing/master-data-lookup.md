# Wyszukiwanie danych głównych

## Przegląd

" Wyszukiwanie danych głównych" w Twoich ustawieniach przetwarzania dokumentów umożliwia kompleksowe i zintegrowane podejście do zarządzania danymi dokumentów i ich walidacji poprzez synchronizację z systemem Infor ERP. Oto, jak pomaga usprawnić weryfikację i wzbogacanie przetwarzania dokumentów w środowisku ERP:

1. **Scentralizowane zarządzanie danymi**: Ta funkcja pełni rolę centralnego repozytorium, w którym mogą być przechowywane i zarządzane dane z różnych źródeł, takich jak dostawcy, adresy klientów, kody podatkowe i inne. Zapewnia pojedynczy punkt odniesienia dla wszystkich danych głównych, gwarantując spójność i dokładność w całej organizacji.
2. **Weryfikacja względem danych ERP**: Synchronizując dane główne, takie jak informacje o dostawcach, z Infor do DocBits, możesz automatycznie weryfikować dane wyodrębnione z dokumentów względem danych z ERP. Zapewnia to zgodność przetwarzanych informacji (np. nazwy dostawców, adresy, kody podatkowe) z danymi przechowywanymi w systemie ERP, minimalizując błędy i rozbieżności.
3. **Ułatwia automatyzację**: Solidny system wyszukiwania danych głównych pomaga automatyzować przetwarzanie napływających dokumentów. Na przykład zamówienia zakupu lub faktury mogą być automatycznie sprawdzane pod kątem poprawności danych dostawcy, zatwierdzane, jeśli się zgadzają, lub oznaczane do weryfikacji w przypadku wykrycia rozbieżności.
4. **Zwiększa integralność danych**: Regularne aktualizacje z systemu ERP do Wyszukiwania danych głównych zapewniają, że dane używane do przetwarzania dokumentów są aktualne. Zmniejsza to ryzyko przetwarzania dokumentów na podstawie nieaktualnych informacji, zwiększając integralność transakcji biznesowych.
5. **Większa efektywność w przetwarzaniu dokumentów**: Dzięki bezpośredniemu i stałemu powiązaniu z danymi głównymi przetwarzanie dokumentów staje się bardziej wydajne. Dokumenty mogą być automatycznie klasyfikowane i kierowane na podstawie określonych w danych głównych kryteriów, takich jak warunki współpracy z dostawcą czy przepisy podatkowe mające zastosowanie do różnych typów transakcji.

{% hint style="info" %}
Zobacz tutaj, jak [zaimportować dane główne](../../../infor-integration-and-configuration/importing-customer-master-data/)
{% endhint %}

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/master_data_lookup_1.png)

## **Dostęp do Wyszukiwania danych głównych**

Aby przejść do sekcji **Wyszukiwanie danych głównych**, przejdź do:\
**Ustawienia → Przetwarzanie dokumentów → Wyszukiwanie danych głównych**

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_mater_data_lookup.png)

## **Ustawienia**

Dostęp do ustawień dla **Wyszukiwanie danych głównych** uzyskasz, klikając ikonę **Ustawienia** w lewym dolnym rogu ekranu **Wyszukiwanie danych głównych**. Dostępne są następujące opcje konfiguracji:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/master_data_lookup_2.png)

### **BOD dostawcy**

* **Zezwól na synchronizację wielu kont dostawców**:
  * **Włączone**:\
    Jeden dostawca może mieć wiele elementów `<FinancialParty>` w BOD (Business Object Document), często z powodu wielu powiązanych IBAN-ów lub rachunków finansowych. Gdy ta opcja jest włączona, wszystkie wpisy `<FinancialParty>` dla dostawcy zostaną wyodrębnione i zapisane w tabeli dostawców, co pozwala przechowywać wiele atrybutów finansowych.
  * **Wyłączone**:\
    Tylko ostatni element `<FinancialParty>` znaleziony dla danego dostawcy w BOD zostanie wyodrębniony. Wszelkie wcześniejsze atrybuty finansowe (np. dodatkowe IBAN-y) zostaną pominięte, a do tabeli dostawców zostaną zapisane wyłącznie dane z ostatniego wystąpienia.

### **Usunięcie zamówienia zakupu**

*   **Usuń zamówienie zakupu po**: Określ, kiedy zamknięte zamówienia zakupu powinny zostać usunięte. Po upływie wybranego okresu rekordy zostaną usunięte automatycznie.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/master_data_lookup_3.png)
