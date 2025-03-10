# Informacje o wersji

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
