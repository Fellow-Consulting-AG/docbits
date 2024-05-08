# Faktura zakupu - Druga zatwierdzenie ilości

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-05-03 um 14.56.54.png" alt=""><figcaption></figcaption></figure>

Ten tytuł wskazuje, że reguła dotyczy specjalnie obsługi faktur zakupu podczas drugiej fazy zatwierdzenia, ze szczególnym uwzględnieniem weryfikacji poprawności podanych ilości.

#### Konfiguracja reguły:

1. **Kiedy…**
* **Typ dokumentu to Faktura**: Ta warunek zapewnia, że reguła jest aktywowana tylko dla dokumentów sklasyfikowanych jako faktury. Jest to istotne dla zachowania specyficzności i istotności w przepływie pracy.
2. **I…**
* **Status dokumentu to Oczekuje na drugie zatwierdzenie**: To określa, że faktura jest obecnie oczekująca na drugie zatwierdzenie. Ten etap ma na celu dodatkowy nadzór przed finalizacją faktury.
* **Pole dokumentu Podtyp faktury to Równa się Faktura zakupu**: Ten warunek dalszo precyzuje regułę, aby dotyczyła wyłącznie faktur zidentyfikowanych jako "Faktury zakupu". Ta kategoryzacja pomaga odróżnić je od innych typów faktur.
* **Logika Ilość w potwierdzeniu zamówienia Nie równa się zamówieniu zakupu**: Ten istotny warunek sprawdza, czy ilość podana w potwierdzeniu zamówienia zgadza się z ilością w oryginalnym zamówieniu zakupu. Akcja jest wywoływana w przypadku rozbieżności, wskazując potencjalny błąd lub problem, który wymaga rozwiązania.

#### Akcja (Wtedy…):

* **Przypisz użytkownika z pola Nazwa kupującego, użyj użytkownika Użytkownik jako awaryjnego**: Jeśli warunki reguły są spełnione (czyli istnieje rozbieżność w ilościach), faktura jest automatycznie przypisywana do osoby wymienionej w polu 'Nazwa kupującego' do dalszej weryfikacji. Jeśli to pole jest puste lub wskazana osoba jest niedostępna, domyślny użytkownik (prawdopodobnie administrator lub inny wyznaczony pracownik) przejmuje kontrolę, aby zapewnić terminową weryfikację i rozwiązanie.

#### Cel tej reguły:

* **Dokładność i zgodność**: Reguła jest kluczowa dla zapewnienia, że proces fakturowania jest dokładny i zgodny z warunkami uzgodnionymi w zamówieniu zakupu. Pomaga zapobiegać rozbieżnościom finansowym i potencjalnym błędom w inwentaryzacji.
* **Zautomatyzowane zatwierdzenia**: Automatyzacja procesu weryfikacji określonych rozbieżności pomaga usprawnić zatwierdzenia i zapewnia, że wszelkie problemy są szybko rozwiązywane przez odpowiedni personel.
* **Wzmocniony nadzór finansowy**: Wymaganie drugiego zatwierdzenia dla weryfikacji ilości wzmacnia kontrole finansowe i odpowiedzialność w organizacji.

To ustawienie ilustruje, jak automatyzacja przepływu pracy może być wykorzystana do poprawy efektywności operacyjnej i zapewnienia integralności finansowej, zwłaszcza przy zarządzaniu złożonymi procesami zakupowymi w firmie.
