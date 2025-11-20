# Informacje o wersji

## Release Winter 10 grudnia 2025

### Usprawnienia DocBits:

* **Ulepszona Personalizacja Reguł Dopasowania Zamówień:**\
  DocBits oferuje teraz szczegółową kontrolę nad regułami dopasowania zamówień zakupu. Możesz skonfigurować dokładnie, które kolumny powinny być dopasowane dla każdego typu dokumentu, zdefiniować tolerancje dla każdej kolumny i wybrać, czy każda reguła dotyczy dopasowania ręcznego, automatycznego czy obu. Te ulepszenia dają użytkownikom elastyczność w dostosowaniu procesu dopasowania do ich konkretnych potrzeb operacyjnych.
*   **Wsparcie dla Wielu Kont Finansowych Dostawców:**\
    DocBits obsługuje teraz wiele kont finansowych dla dostawców poprzez BOD RemitToPartyMaster z Infor. Dostępne jest nowe ustawienie konfiguracyjne do aktywacji tej funkcji.

    <figure><img src="../../.gitbook/assets/release_notes_12_2025_1.png" alt=""><figcaption></figcaption></figure>
*   **Dodanie Dostępu Użytkowników do Wyników Ekstrakcji OCR:**\
    Przycisk Widok OCR na ekranie Walidacji Pól jest teraz dostępny dla wszystkich użytkowników z dostępem do walidacji, a nie tylko dla administratorów, umożliwiając wszystkim użytkownikom przeglądanie wyników ekstrakcji OCR i wyszukiwanie określonych treści w dokumentach.

    <figure><img src="../../.gitbook/assets/release_notes_12_2025_2.png" alt=""><figcaption></figcaption></figure>
* **Dynamiczne Renderowanie Kolumn na Ekranach Zatwierdzania:**\
  Ulepszone widoki zatwierdzania, aby dynamicznie wyświetlać tylko kolumny skonfigurowane do porównania w preferencjach bazy danych każdej organizacji. Wcześniej kolumny takie jak Kod Jednostki i Obiecana Data Dostawy pojawiały się puste, gdy nie były skonfigurowane do porównania, powodując zamieszanie. Teraz widoki zatwierdzania pokazują tylko aktywnie porównywane pola. To zapewnia jaśniejsze, specyficzne dla organizacji ekrany zatwierdzania bez pustych lub nieistotnych kolumn.
* **Pole Typ Zamówienia Dodane do Wyszukiwania Danych Podstawowych**:\
  Lista nagłówków zamówień zakupu zawiera teraz kolumnę "Typ Zamówienia" (type\_code) w wyszukiwaniu danych podstawowych, zapewniając dodatkowe możliwości kategoryzacji.
* **Ulepszenia Panelu z Niestandardowymi Filtrami:**\
  Ulepszona funkcjonalność udostępniania panelu, umożliwiając użytkownikom, którym udostępniono panel, edycję filtrów panelu. Użytkownicy, którzy mają udostępnione panele, mogą teraz modyfikować filtry, aby uzyskać bardziej elastyczny i spersonalizowany widok.
* **Konfigurowalne Prefiksy dla Kolumn Ekranu Zatwierdzania:**\
  Dodano konfigurowalną opcję wyświetlania prefiksów przed kolumnami dokumentów na ekranach zatwierdzania. Prefiks można ustawić w konstruktorze układu, pozwalając użytkownikom wybrać, czy prefiksy się pojawiają i do jakich typów dokumentów się stosują.\


### Ogólne Usprawnienia

* Ulepszone rejestrowanie błędów dla źle wyszkolonych tabel w ekstrakcji tabel.
* Dodano limit udostępniania dla paneli do 10 użytkowników lub 5 grup, wraz z wyraźnym komunikatem o błędzie po osiągnięciu limitu.
* Ulepszona obsługa błędów dla niestandardowych paneli, gdy użytkownik próbuje utworzyć panel z nazwą, która już istnieje.

### Poprawki Błędów:

* Naprawiono problem, w którym e-maile wydawały się być wysyłane pomyślnie z sekcji Szczegóły Dostawcy, ale nie były dostarczane do odbiorców.
* Naprawiono problem, w którym pola rozwijane dodane do ekranów zatwierdzania/odrzucania nie były wyświetlane.
* Naprawiono problem, w którym wszystkie eksportowane dokumenty były oznaczone jako ostatnio zaktualizowane przez niewłaściwego użytkownika.
* Naprawiono problem, w którym importy FTP nie pobierały dokumentów.
* Naprawiono problem, w którym dokumenty pokazywały status "Workflow w toku", ale nie wykonywały się żadne workflow, a dziennik pozostawał pusty.
* Naprawiono problem, w którym niepowiązani użytkownicy byli przypisywani do dokumentów w momencie eksportu bez wykonywania jakiejkolwiek pracy nad nimi.
* Naprawiono problem, w którym użytkownicy z poprawnymi uprawnieniami nie mogli odrzucić przypisanych dokumentów i otrzymywali błędy.
* Naprawiono problem, w którym ikony przepływu dokumentów nie były wyświetlane dla niektórych organizacji.
* Naprawiono problem, w którym pojawiało się okienko pop-up podczas przesyłania dokumentów metodą przeciągnij i upuść na pulpit.
* Naprawiono problem, w którym flagi E-TEXT były wyświetlane jako włączone w interfejsie użytkownika, mimo że odpowiedź API pokazywała wszystkie wartości jako fałszywe.
* Naprawiono problem, w którym występował błąd podczas przesyłania dokumentów zawierających puste strony.
* Naprawiono problem, w którym hiperłącza zadań w powiadomieniach e-mail używały adresu URL zatwierdzania v2 zamiast v3.
* Naprawiono problem, w którym Wyszukiwanie Danych Podstawowych nie wyświetlało żadnych dostawców, gdy wybrana była podorganizacja "Cross", uniemożliwiając użytkownikom przeglądanie danych dostawców międzyorganizacyjnych.
* Naprawiono problem, w którym dokumenty przesłane w Cross nie były przypisywane do identyfikatora podorganizacji.
* Naprawiono problem, w którym importy przychodzących e-maili nie powiodły się dla nadawców z wielkimi literami w ich adresach e-mail z powodu porównania e-maili z rozróżnianiem wielkości liter.

## Release Autumn Summit 22 października 2025

### Usprawnienia DocBits:

*   #### Usprawnienia Projektowania Szablonów Email:

    Edytor szablonów email został przeprojektowany, aby zapewnić klarowną strukturę i płynniejsze doświadczenie. Wybieranie pól dokumentów jest teraz bardziej intuicyjne, a załączniki można teraz dołączać bezpośrednio do szablonów. Te usprawnienia sprawiają, że tworzenie profesjonalnych, spersonalizowanych wiadomości e-mail jest szybsze i łatwiejsze.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fdv4oDlfkRyD0W9yWGAA4%252Fimage.png%3Falt%3Dmedia%26token%3D14bf7ebd-d886-4758-8184-d7b94447518a\&width=768\&dpr=4\&quality=100\&sign=88405d9c\&sv=2)
*   #### Usprawnienia Panelu:

    Panel został rozszerzony, aby poprawić nawigację i dostosowanie. Dzięki nowym zakładkom użytkownicy mogą szybciej przełączać się między różnymi typami dokumentów, skracając czas spędzony na szukaniu odpowiedniego widoku.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FmpO7WSIrkL0I8Rje3HQt%252Fimage.png%3Falt%3Dmedia%26token%3D77d03fe7-e626-4645-b191-e332715a25fb\&width=768\&dpr=4\&quality=100\&sign=93fa9925\&sv=2)
*   #### Niestandardowe Filtry Paneli:

    Ponadto panele można teraz dostosowywać i filtrować zgodnie z indywidualnymi preferencjami. Te niestandardowe panele można również udostępniać współpracownikom, ułatwiając tworzenie spójnych widoków raportowania dla całego zespołu.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fn5rPvGnRltT3mTIDoJwV%252Fimage.png%3Falt%3Dmedia%26token%3D22d065e3-81eb-4f16-828c-7f9134c25b1b\&width=768\&dpr=4\&quality=100\&sign=eb11d3a3\&sv=2)
*   #### Logi Powiadomień Email:

    Dostępna jest nowa funkcja logowania dla wszystkich powiadomień email. Użytkownicy mogą teraz przejrzeć historię wysłanych powiadomień, co ułatwia weryfikację dostaw i rozwiązywanie problemów, jeśli wiadomości nie zostały odebrane.
*   #### Wsparcie dla Faktur Elektronicznych: e-SLOG 1.6 & 2.0:

    Wprowadzono obsługę dodatkowych formatów faktur elektronicznych. System może teraz przetwarzać i generować wersje e-SLOG 1.6 i 2.0, poszerzając zgodność z partnerami i wymaganiami regulacyjnymi.
*   #### Usprawnienia Wykrywania Duplikatów:

    Wykrywanie duplikatów zostało ulepszone dzięki dwóm potężnym opcjom konfiguracji. **Interwał Wykrywania Duplikatów** pozwala zdefiniować zakres czasowy w celu dokładniejszego sprawdzania duplikatów, podczas gdy ustawienie **Zabronić Eksportu Duplikatów** automatycznie uniemożliwia eksport dokumentów uznanych za duplikaty. Te usprawnienia zapewniają większą kontrolę i zapewniają wyższą dokładność danych.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FXHRKTmuSxTlDt9lDEkE7%252Fimage.png%3Falt%3Dmedia%26token%3D96b56af6-c644-4b0f-a488-8bc16a03c11f\&width=768\&dpr=4\&quality=100\&sign=9b723b7f\&sv=2)
*   #### Usprawnienia Drzew Decyzyjnych:

    Drzewa decyzyjne są teraz bardziej wszechstronne, umożliwiając zwracanie wartości pól dokumentów. Pozwala to na bardziej zaawansowaną logikę automatyzacji, umożliwiając przeprowadzanie decyzji na podstawie rzeczywistych danych dokumentów.
*   #### Nowe Karty Przepływu Roboczego:

    Dwie nowe karty przepływu roboczego poszerzają możliwości automatyzacji. Pierwsza pozwala sprawdzić, czy dokument należy do określonej podorganizacji, ułatwiając obsługę konfiguracji wielu jednostek. Druga wprowadza sprawdzenie tolerancji daty dostawy, porównując daty dostawy z bieżącą datą w dniach roboczych, aby pomóc lepiej zarządzać i egzekwować wymagania dotyczące dostawy.
*   #### Usprawnienia Eksportu CSV:

    Funkcja eksportu CSV została znacząco ulepszona. Zamiast eksportować tylko dokumenty wyświetlane na bieżącej stronie, system teraz eksportuje wszystkie dokumenty w zestawie danych. Każdy eksport tworzy wpis w dzienniku, a wynikowy plik CSV jest automatycznie wysyłany pocztą elektroniczną, zapewniając bardziej kompletny i niezawodny proces eksportu.
*   #### Ramy Czasowe Usuwania Zamówienia Zakupu:

    Nowa opcja konfiguracji pozwala administratorom zdefiniować ramy czasowe dla usuwania zamówienia zakupu. To usprawnienie dodaje elastyczność i kontrolę nad politykami retencji danych, zapewniając, że zamówienia zakupu są usuwane tylko w odpowiednim momencie.

### Poprawki Błędów

* Naprawiono problem, w którym stare dane były uwzględniane podczas eksportowania dokumentów.
* Poprawiono filtr dla Błędów Eksportu, który wcześniej pokazywał również inne statusy.
* Rozwiązano niezgodność walidacji tabeli, gdzie "Cena Jednostkowa" powodowała błędy, ale "Cena Jednostkowa Za" nie, mimo że wartości były poprawne.
* Naprawiono problem, w którym dodanie nowej kolumny do panelu nie powiodło się.
* Poprawiono problem, w którym zadania nie były widoczne w kolumnie zadań panelu.
* Naprawiono losowe zachowanie sortowania, dzięki czemu listy teraz podążają za spójnym porządkiem.
* Rozwiązano problem, w którym zmiana rozmiaru kolumny nie mogła zostać zatrzymana.
* Naprawiono błąd uniemożliwiający ręczne dopasowanie linii w ekranie Dopasowywania PO.
* Poprawiono problem, w którym opcja załącznika email została zresetowana po zapisaniu.
* Naprawiono problem, w którym początkowo wyświetlane były identyfikatory bazy danych w automatycznym rozliczaniu.
* Poprawiono zachowanie pola rozmytego, dzięki czemu wartości nie są już niewłaściwie nadpisywane.
* Naprawiono problem, w którym pola w automatycznym rozliczeniu zniknęły po usunięciu zawartości.
* Poprawiono błąd, w którym użytkownik nie mógł zmienić nazwy "Imię" i "Nazwisko" w oknie dialogowym ustawień.
* Rozwiązano problem, w którym dokumenty mogły utknąć w "przepływie roboczym w toku".
* Naprawiono problem z kolorem ikony menu, gdzie wybrane kolory organizacji nie były poprawnie stosowane.
* Poprawiono problem, w którym czasami kody QR nie były rozpoznawane.
* Naprawiono problem, w którym konta nie mogły być usunięte za pomocą klawisza backspace do wprowadzenia innego.
* Rozwiązano problem z mieszanym językiem po zalogowaniu się po wdrożeniu produkcji.

## Wydanie Spring Bloom – 23 kwietnia 2025

### Ulepszenia DocBits:

* **Opcja filtrowania dla dziennika importu e-maili:** Użytkownicy mają teraz możliwość filtrowania dzienników importu i sortowania tabeli, co zapewnia jaśniejszy i bardziej efektywny przegląd. To ulepszenie usprawnia proces identyfikacji i zarządzania wpisami e-mail, poprawiając rozwiązywanie problemów i ogólne zarządzanie dziennikami.
* **Wsparcie wielojęzyczne dla Listy Wartości:** Rozszerzyliśmy możliwości wielojęzyczne dla funkcji Listy Wartości. Administratorzy mogą teraz definiować etykiety w wielu językach, zapewniając, że odpowiednia etykieta jest automatycznie wyświetlana w zależności od ustawień językowych systemu użytkownika. To ulepszenie promuje większą dostępność i lokalizację, ułatwiając użytkownikom na całym świecie interakcję z platformą w ich rodzimym języku.
* **Ulepszenia szczegółów użytkownika w ustawieniach:** Interfejs ustawień teraz wyświetla kompleksowe informacje o użytkownikach. Administratorzy mogą łatwo przeglądać przynależności do grup, szczegóły podorganizacji i dodatkowe kluczowe dane, co umożliwia lepsze zarządzanie rolami użytkowników i jaśniejsze zrozumienie struktur zespołowych.
* **Informacje o automatycznym księgowaniu na ekranie zatwierdzania:** Ekran zatwierdzania teraz prezentuje szczegóły automatycznego księgowania obok informacji o fakturze. To ulepszenie zapewnia głębszy wgląd w dane transakcyjne, ułatwiając płynniejsze procesy przeglądowe i bardziej świadome podejmowanie decyzji dotyczących faktur.
* **Licznik zadań dla dokumentów w widoku pulpitu:** Dokumenty na pulpicie mogą teraz wskazywać otwarte zadania związane z nimi oraz wyświetlać łączną liczbę oczekujących zadań. Ta funkcja zapewnia użytkownikom szybki przegląd zaległych działań, poprawiając zarządzanie zadaniami i efektywność przepływu pracy.
* **Wybór modelu AI opartego na dostawcy:** Użytkownicy mogą teraz wybierać model AI używany do ekstrakcji danych na podstawie dostawcy. To ulepszenie pozwala na precyzyjną optymalizację, zapewniając lepszą dokładność ekstrakcji dla różnych dostawców i poprawiając ogólne wyniki przetwarzania danych.
* **Ulepszone dzienniki przepływu pracy dla kart drzewa decyzyjnego:** Dzienniki teraz wyświetlają wyniki drzewa decyzyjnego, co ułatwia śledzenie i zrozumienie, jak podejmowane były decyzje w ramach przepływów pracy.
*   **Wprowadzenie nowego ustawienia automatycznego testowania w celu poprawy funkcjonalności i stabilności systemu:**

    Z radością ogłaszamy wdrożenie nowego systemu automatycznego testowania, zaprojektowanego w celu poprawy ogólnej funkcjonalności i niezawodności naszej platformy. To nowe ustawienie będzie przeprowadzać regularne, dokładne kontrole naszego systemu, aby zidentyfikować wszelkie problemy, zanim wpłyną na Twoje doświadczenia. Automatyzując te testy, możemy zapewnić szybsze reakcje na potencjalne problemy i utrzymać najwyższe standardy jakości naszego systemu.

    ​

### Poprawki błędów

* Rozwiązano problem, w którym zadania nie pojawiały się na ekranie walidacji/zatwierdzania.
* Naprawiono pozycjonowanie przycisku Następny/Poprzedni, aby pozostał statyczny.
* Naprawiono problemy z przewijaniem w widokach skryptu i drzewa decyzyjnego, zapewniając, że przyciski akcji pozostają nieruchome podczas przewijania.
* Usunięto pole kraju pochodzenia z e-faktur.
* Naprawiono problem z licznikiem zadań wyświetlającym nieprawidłową liczbę zadań.
* Dodano brakujące tłumaczenia.
* Skorygowano pola niestandardowe, aby wyświetlały opisowe nazwy zamiast identyfikatorów.
* Zaktualizowano listę skrótów dla ekranu dopasowywania zamówień.
* Rozwiązano problem, w którym dokumenty były pobierane z nieprawidłową nazwą pliku.
* Naprawiono niespójności sortowania w tabeli linii faktury w ramach dopasowywania zamówień.
* Naprawiono problem wpływający na funkcjonalność tworzenia zadań.
* Naprawiono problem w dopasowywaniu zamówień, w którym sortowanie tabeli faktur resetowało się podczas dopasowywania linii.
* Rozwiązano problemy z automatycznym księgowaniem, zapewniając, że odniesienia do rezerwacji są poprawnie dzielone, gdy kwota jest dzielona.
* Zaktualizowano informacje o hoście ClickHouse.
* Rozwiązano problem, w którym zduplikowane dokumenty nie były rozpoznawane jako duplikaty.
* Naprawiono problemy z eksportem spowodowane zbyt długimi odniesieniami do rezerwacji.
* Rozwiązano problem, w którym pola wyboru tylko do odczytu nie były tylko do odczytu.
* Naprawiono problem, w którym użytkownicy mogli być dodawani do podorganizacji dwukrotnie.
* Naprawiono problem, w którym zmiana podorganizacji dla dokumentu powodowała zresetowanie przypisanego użytkownika lub grupy.

​

## Wydanie Hot Fix Winter Frost 10 kwietnia 2025

### Ulepszenia DocBits:

* **Ulepszona** **`set_column_date_value`** **Funkcja Skryptu:** Funkcja `set_column_date_value` teraz obsługuje opcję `skip_weekend`, co pozwala na automatyczne pomijanie weekendów przy stosowaniu wartości daty.
* **Poprawione wsparcie dla przesyłania plików:** Pliki PNG i JPEG mogą teraz być przesyłane bezpośrednio i są automatycznie konwertowane na format PDF w celu uproszczenia obsługi dokumentów.
* **Ulepszenia funkcjonalności Watchdog:**
  * Teraz obsługuje eksport do **Enaio** dla lepszej integracji systemowej.
  * Ulepszone możliwości analizy w celu wydobywania informacji z struktur XML `Sync.ContentDocument`, co umożliwia bardziej efektywne przetwarzanie danych.

### Poprawki błędów

* Naprawiono problem z funkcją skryptu.
* Rozwiązano problem, w którym zamówienia zakupu miały błędny status po ich aktualizacji.

## Wydanie Hot Fix Winter Frost 11 marca 2025

### Ulepszenia DocBits:

* **Ulepszona ekstrakcja danych:** Dodano opcję ekstrakcji **Zamówienia Zakupu** lub **Numeru Przedmiotu** z linii powyżej lub poniżej.
* **Rozszerzony dostęp do podorganizacji:** Użytkownicy niebędący administratorami mogą teraz również uzyskać dostęp do funkcji **Cross Sub-Organizations**.

### **Poprawki błędów:**

* Naprawiono problem, w którym użytkownicy nie mogli zostać dodani do grupy.
* Naprawiono problem z niepowodzeniami importu e-maili.
* Rozwiązano problem z treningiem w terenie na dokumentach z więcej niż jedną stroną.
* Naprawiono problem, w którym skrypty nie działały poprawnie.
* Rozwiązano problem, w którym dane dokumentu nie były wyświetlane poprawnie.
* Naprawiono problem z ustawieniem automatycznej aktualizacji zamówienia zakupu.
* Naprawiono problem, w którym tokeny subskrypcyjne były wyświetlane nieprawidłowo.
* Rozwiązano problem, w którym ekran zadań wyświetlał nieaktualną wersję dokumentu.
* Naprawiono problem, który powodował, że dokumenty nie zmieniały swojego statusu.
