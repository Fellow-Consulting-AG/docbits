# Informacje o wersji

## Wydanie Spring Bloom – 23 kwietnia 2025

### Ulepszenia DocBits:

* **Opcja filtrowania dla dziennika importu e-maili:** Użytkownicy mają teraz możliwość filtrowania dzienników importu i sortowania tabeli, co zapewnia jaśniejszy i bardziej efektywny przegląd. To ulepszenie usprawnia proces identyfikacji i zarządzania wpisami e-mail, poprawiając rozwiązywanie problemów i ogólne zarządzanie dziennikami.
* **Wsparcie wielojęzyczne dla Listy Wartości:** Rozszerzyliśmy możliwości wielojęzyczne dla funkcji Listy Wartości. Administratorzy mogą teraz definiować etykiety w wielu językach, zapewniając, że odpowiednia etykieta jest automatycznie wyświetlana w zależności od ustawień językowych systemu użytkownika. To ulepszenie promuje większą dostępność i lokalizację, ułatwiając użytkownikom na całym świecie interakcję z platformą w ich rodzimym języku.
* **Ulepszenia szczegółów użytkownika w ustawieniach:** Interfejs ustawień teraz wyświetla kompleksowe informacje o użytkownikach. Administratorzy mogą łatwo przeglądać przynależności do grup, szczegóły podorganizacji i dodatkowe kluczowe dane, co umożliwia lepsze zarządzanie rolami użytkowników i jaśniejsze zrozumienie struktur zespołowych.
* **Informacje o automatycznym księgowaniu na ekranie zatwierdzania:** Ekran zatwierdzania teraz prezentuje szczegóły automatycznego księgowania obok informacji o fakturze. To ulepszenie zapewnia głębszy wgląd w dane transakcyjne, ułatwiając płynniejsze procesy przeglądowe i bardziej świadome podejmowanie decyzji dotyczących faktur.
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

​

## Wydanie Hot Fix Winter Frost 11 marca 2025

### Ulepszenia DocBits:

* **Ulepszona ekstrakcja danych:** Dodano opcję ekstrakcji **Zamówienia Zakupu** lub **Numeru Przedmiotu** z linii powyżej lub poniżej.
* **Rozszerzony dostęp do podorganizacji:** Użytkownicy niebędący administratorami mogą teraz również uzyskać dostęp do funkcji **Cross Sub-Organizations**.

### **Poprawki błędów:**

* Naprawiono problem, w którym użytkownicy **nie mogli być dodawani** do grupy.
* Naprawiono problem z **niepowodzeniami importu e-maili**.
