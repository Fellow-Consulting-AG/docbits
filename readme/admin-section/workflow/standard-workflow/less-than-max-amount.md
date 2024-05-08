# Mniej niż maksymalna kwota

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-05-03 um 14.48.55.png" alt=""><figcaption></figcaption></figure>

Ten tytuł sugeruje, że reguła lub warunek jest zaprojektowany tak, aby obsługiwać faktury, których całkowita kwota jest mniejsza lub równa określonej maksymalnej kwocie.

#### Konfiguracja reguły:

1. **Kiedy…**
* **Typ dokumentu to Faktura**: Ten warunek sprawdza, czy przetwarzany dokument to faktura. Jest to kluczowe dla zapewnienia, że reguła dotyczy tylko faktur, a nie innych typów dokumentów.
2. **I…**
* **Status dokumentu to Oczekuje na zatwierdzenie**: Określa, że faktura musi znajdować się w statusie "Oczekuje na zatwierdzenie". Sprawdzenie tego statusu zapewnia, że reguła dotyczy tylko faktur oczekujących na zatwierdzenie.
* **Porównaj dwie pola: Całkowita kwota Mniejsza lub Równa Maksymalnej Kwocie Zatwierdzającego**: Ten warunek porównuje całkowitą kwotę faktury z maksymalną upoważnioną kwotą zatwierdzającą. Jeśli całkowita kwota faktury jest mniejsza lub równa tej maksymalnej kwocie, reguła przechodzi do następnego kroku. Prawdopodobnie obejmuje to poziom tolerancji, który pozwala na niewielkie odchylenia w określonych granicach.

#### Akcja (Wtedy…):

* **Przypisz użytkownika z pola Nazwa Zatwierdzającego, użyj użytkownika Użytkownik jako awaryjnego**: Jeśli spełnione są określone warunki, faktura jest automatycznie przypisywana do zatwierdzającego, którego nazwa jest określona w polu. Jeśli to pole jest puste lub niedostępne, domyślny użytkownik (prawdopodobnie administrator lub inny wyznaczony pracownik) jest przypisywany jako awaryjny do obsługi zatwierdzenia.

#### Elementy interfejsu:

* **Dodaj Kartę**: Ten przycisk prawdopodobnie pozwala użytkownikom dodać więcej warunków lub akcji do reguły, zwiększając elastyczność i specyficzność przepływu pracy.
* **Zapisz**: Zapisuje skonfigurowaną regułę w systemie.

#### Cel tej reguły:

To ustawienie ma na celu usprawnienie procesu zatwierdzania faktur poprzez automatyczne kierowanie faktur do odpowiedniego zatwierdzającego na podstawie kwoty oraz zapewnienie, że tylko te znajdujące się w określonym progu są obsługiwane w ten zautomatyzowany sposób. Pomaga w zarządzaniu kontrolami finansowymi i przyspiesza przepływ pracy poprzez ograniczenie ręcznych kontroli dla każdej faktury.
