# Faktura zakupu - Eksportowanie ilości zatwierdzenia 2.

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-05-03 um 15.00.53.png" alt=""><figcaption></figcaption></figure>

Ten tytuł wskazuje, że reguła jest ustawiona w celu zarządzania drugą fazą zatwierdzenia faktur zakupu z naciskiem na szczegóły dotyczące ilości, zapewniając, że ilości na fakturze zgadzają się z tymi na oryginalnym zamówieniu zakupu.

#### Konfiguracja reguły:

1. **Kiedy…**
* **Typ dokumentu to Faktura**: Ta warunek zapewnia, że reguła jest aktywowana tylko dla dokumentów zidentyfikowanych jako faktury, co jest kluczowe dla dokładnego kierowania przepływem pracy.
2. **I…**
* **Status dokumentu to Oczekuje na drugie zatwierdzenie**: Określa to, że faktura oczekuje obecnie na drugie zatwierdzenie. Ten etap często zapewnia dodatkowy nadzór, aby zapewnić dokładność przed sfinalizowaniem transakcji.
* **Pole dokumentu Podtyp faktury to Równa się Fakturze zakupu**: Ten warunek dodatkowo określa, że reguła dotyczy tylko faktur sklasyfikowanych specjalnie jako "Faktury zakupu", odróżniając je od innych typów faktur.
* **Logika Ilość w potwierdzeniu zamówienia Równa się zamówieniu zakupu**: Ten warunek sprawdza, czy ilość podana w potwierdzeniu zamówienia zgadza się z ilością w zamówieniu zakupu. Zapewnia to, że przetwarzanie faktury przechodzi do przodu tylko wtedy, gdy ilości są zgodne, co jest kluczowe dla zarządzania zapasami i dokładności finansowej.

#### Działanie (Wtedy…):

* **Rozpocznij eksport**: Gdy faktura spełnia określone warunki (tj. ilości zgadzają się między potwierdzeniem zamówienia a zamówieniem zakupu), uruchamiane jest działanie "Rozpocznij eksport". Prawdopodobnie obejmuje to eksportowanie danych faktury do dalszego przetwarzania, być może do innego systemu finansowego lub w celach raportowania.

#### Cel tej reguły:

* **Zapewnienie dokładności i spójności**: Poprzez weryfikację, czy ilości zgadzają się między potwierdzeniem zamówienia a zamówieniem zakupu, system pomaga utrzymać dokładność zapasów i zapobiega rozbieżnościom, które mogłyby wpłynąć na raportowanie finansowe lub zarządzanie zapasami.
* **Usprawnienie przetwarzania finansowego**: Automatyzacja eksportu danych po potwierdzeniu ilości redukuje ręczne operacje i przyspiesza cykl przetwarzania finansowego.
* **Wzmocnienie zgodności i nadzoru**: Wymaganie drugiego zatwierdzenia w celu weryfikacji ilości dodaje dodatkową warstwę nadzoru, istotną dla zgodności z politykami finansowymi i kontrolami.

Ta reguła stanowi jasny przykład skutecznego wykorzystania automatyzacji przepływu pracy do zapewnienia precyzyjnego i efektywnego zarządzania dokumentami finansowymi w organizacji, zwłaszcza w kontekście procesów zakupowych, które obejmują duże ilości transakcji wymagających skrupulatnej walidacji.
