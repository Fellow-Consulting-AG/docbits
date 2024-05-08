# Powyżej maksymalnej kwoty

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-05-03 um 14.51.42.png" alt=""><figcaption></figcaption></figure>

Ten tytuł wskazuje, że reguła ta ma na celu zarządzanie przypadkami, w których całkowita kwota faktury przekracza maksymalną kwotę, którą zatwierdzający jest upoważniony obsłużyć.

#### Konfiguracja reguły:

1. **Kiedy…**
* **Typ dokumentu to Faktura**: Warunek ten zapewnia, że reguła dotyczy tylko faktur, co jest istotne dla poprawnego kierowania przepływem pracy.
2. **I…**
* **Status dokumentu to Oczekuje na zatwierdzenie**: Faktura musi znajdować się w statusie "Oczekuje na zatwierdzenie". Ten status jest kluczowy, aby zapewnić, że reguła jest stosowana do faktur, które są wciąż przetwarzane i nie zostały jeszcze sfinalizowane.
* **Porównaj dwie pola: Całkowita kwota większa niż maksymalna kwota zatwierdzającego**: Ten warunek sprawdza, czy całkowita kwota faktury przekracza maksymalną kwotę, którą zatwierdzający ma prawo obsłużyć. To porównanie może również obejmować ustawienie tolerancji, pozwalającą na niewielkie różnice na podstawie wstępnie zdefiniowanych kryteriów.

#### Działanie (Wtedy…):

* **Przypisz użytkownika z pola Następny Zatwierdzający, użyj użytkownika Użytkownik jako awaryjnego**: Jeśli faktura przekracza określoną maksymalną kwotę, automatycznie jest przypisywana do zatwierdzającego na wyższym poziomie, wskazanego przez pole 'Następny Zatwierdzający'. Jeśli to pole nie jest wypełnione lub określony użytkownik jest niedostępny, domyślnie używany jest inny użytkownik (prawdopodobnie administrator lub inny wyznaczony pracownik) jako awaryjny, aby zapewnić, że faktura zostanie zrewidowana bez opóźnień.

#### Elementy interfejsu:

* **Dodaj kartę**: Ta opcja pozwala dodać dodatkowe warunki lub działania do reguły, zapewniając elastyczność w rozwiązywaniu skomplikowanych scenariuszy.
* **Zapisz**: Ten przycisk zapisuje konfigurację reguły w systemie.

#### Cel tej reguły:

Celem tej reguły jest zapewnienie, że faktury przekraczające określone progi finansowe są przeglądane przez zatwierdzających posiadających odpowiednie poziomy uprawnień. Pomaga to w utrzymaniu kontroli finansowej i nadzoru, zapewniając, że wydatki są przeglądane przez personel posiadający wymagane limity zatwierdzeń, co z kolei chroni organizację przed nieautoryzowanymi lub nieodpowiednimi wydatkami.

Ta reguła, podobnie jak poprzednia, pomaga zautomatyzować przepływ pracy, zmniejszając nakład pracy manualnej i zwiększając zgodność z politykami finansowymi organizacji. Jest to przykład skutecznego wykorzystania automatyzacji przepływu pracy do zarządzania złożonymi procesami finansowymi w firmie.
