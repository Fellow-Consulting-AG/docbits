# Faktura zakupu - Eksport jednostkowej ceny zatwierdzenia 2

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-05-03 um 14.59.02.png" alt=""><figcaption></figcaption></figure>

Ten tytuł wskazuje, że reguła jest ustawiona w celu zarządzania drugą fazą zatwierdzenia faktur zakupu, skupiając się na cenie jednostkowej, zapewniając zgodność z ustalonymi warunkami.

#### Konfiguracja reguły:

1. **Kiedy…**
* **Typ dokumentu to Faktura**: Ta warunek zapewnia, że reguła jest aktywowana tylko dla dokumentów zidentyfikowanych jako faktury, co jest kluczowe dla dokładnego kierowania przepływem pracy.
2. **I…**
* **Status dokumentu to Oczekuje na drugie zatwierdzenie**: To określa, że faktura oczekuje na drugie zatwierdzenie. Ten etap często zapewnia dodatkowy nadzór, aby zapewnić dokładność przed sfinalizowaniem transakcji.
* **Podtyp faktury to Równa się Faktura zakupu**: Ten warunek dodatkowo określa, że reguła dotyczy tylko faktur sklasyfikowanych specjalnie jako "Faktury zakupu", odróżniając je od innych typów faktur.
* **Logika Cena jednostkowa w potwierdzeniu zamówienia Równa zamówieniu zakupu**: Ten warunek sprawdza, czy cena jednostkowa podana w potwierdzeniu zamówienia odpowiada cenie jednostkowej w zamówieniu zakupu. Zapewnia to, że przetwarzanie faktury przechodzi do przodu tylko wtedy, gdy istnieje spójność cenowa, co jest kluczowe dla budżetowania i raportowania finansowego.

#### Działanie (Wtedy…):

* **Rozpocznij eksport**: Gdy faktura spełnia określone warunki (tj. ceny jednostkowe są zgodne między potwierdzeniem zamówienia a zamówieniem zakupu), uruchamiane jest działanie "Rozpocznij eksport". Prawdopodobnie obejmuje to eksport danych faktury do dalszego przetwarzania, być może do innego systemu finansowego lub w celach raportowania.

#### Cel tej reguły:

* **Zapewnienie dokładności i spójności**: Poprzez weryfikację zgodności cen jednostkowych między potwierdzeniem zamówienia a zamówieniem zakupu, system pomaga utrzymać dokładność finansową i zapobiega nadpłacaniu lub niedopłacaniu.
* **Usprawnienie przetwarzania finansowego**: Automatyzacja eksportu danych po potwierdzeniu cen redukuje ręczne operacje i przyspiesza cykl przetwarzania finansowego.
* **Wzmocnienie zgodności i nadzoru**: Wymaganie drugiego zatwierdzenia w celu weryfikacji ceny dodaje dodatkową warstwę nadzoru, co jest istotne dla zgodności z politykami i kontrolami finansowymi.

Ta reguła jest przykładem skutecznego wykorzystania automatyzacji przepływu pracy do zapewnienia precyzyjnego i efektywnego zarządzania dokumentami finansowymi w organizacji, zwłaszcza w kontekście dużych wolumenów transakcji, które wymagają skrupulatnej walidacji.
