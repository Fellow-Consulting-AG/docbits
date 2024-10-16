# Drzewa Decyzyjne

#### Przegląd

Drzewa Decyzyjne to potężna funkcja, która umożliwia automatyczne kierowanie i podejmowanie decyzji na podstawie zdefiniowanych reguł. Ta funkcja jest szczególnie przydatna w złożonych środowiskach, gdzie różne warunki muszą być oceniane, aby określić właściwy tok działania, takie jak ustalanie cen, określanie ilości lub kierowanie dokumentami.

**Kluczowe Komponenty**

* **Lista Drzew Decyzyjnych**: To główny interfejs, w którym wyświetlane są wszystkie istniejące drzewa decyzyjne. Każde drzewo decyzyjne może być powiązane z określonym typem dokumentu, takim jak `FAKTURA` lub `OFERTA`.
* **Edytor Drzew Decyzyjnych**: Ten interfejs umożliwia tworzenie i edytowanie drzew decyzyjnych, gdzie można definiować reguły, operatory i działania, które mają być podjęte, gdy spełnione są określone warunki.

#### Interfejs Drzewa Decyzyjnego

**Lista Drzew Decyzyjnych**

Lista Drzew Decyzyjnych wyświetla wszystkie dostępne drzewa decyzyjne. Każdy wpis pokazuje:

* **Nazwa**: Nazwa drzewa decyzyjnego.
* **Typ Dokumentu**: Typ dokumentu powiązanego z drzewem decyzyjnym (np. `FAKTURA`, `OFERTA`).

**Edytor Drzew Decyzyjnych**

Edytor Drzew Decyzyjnych pozwala na konfigurowanie reguł, które określają, jak podejmowane są decyzje.

**Komponenty Edytora Drzew Decyzyjnych**

* **Reguły**: Każda reguła składa się z warunków i działań.
* **Wybierz Źródło**: To rozwijane menu pozwala określić pole źródłowe do oceny.
* **Wybierz Operator**: Definiuje operator logiczny (np. `<=`, `>=`, `=`, `!=`), który ma być zastosowany do pola źródłowego.
* **Wynik**: Definiuje wynik lub działanie, które powinno być podjęte, gdy warunki są spełnione.
* **Dodaj Nowy Wiersz**: Pozwala dodać dodatkowe reguły do drzewa decyzyjnego.

**Przykład Konfiguracji Drzewa Decyzyjnego**

1. **Reguła 1**:
   * **Źródło**: Ilość
   * **Operator**: `<=`
   * **Wartość**: `250000`
   * **Wynik**: Przypisz do `CATMGR_CMM`
2. **Reguła 2**:
   * **Źródło**: Cena
   * **Operator**: `>`
   * **Wartość**: `500000`
   * **Wynik**: Przypisz do `PROCUREMENT_DIRECTOR`

Każda reguła jest oceniana sekwencyjnie, a odpowiednie działanie jest wykonywane, jeśli warunki są spełnione.

#### Polityka Drzewa Decyzyjnego

Polityka Drzewa Decyzyjnego definiuje, jak wiele reguł w obrębie drzewa decyzyjnego jest przetwarzanych. Możesz wybierać spośród kilku polityk:

* **Unikalna**: Zapewnia, że tylko jedna reguła może pasować. Jeśli więcej niż jedna reguła pasuje, drzewo decyzyjne zgłosi błąd.
* **Pierwsza**: Zastosowana zostaje pierwsza pasująca reguła, a dalsze reguły nie są oceniane.
* **Priorytet**: Reguły są oceniane na podstawie ich kolejności priorytetowej. Zastosowana zostaje reguła o najwyższym priorytecie.
* **Zbieraj (suma)**: Zbiera wszystkie pasujące reguły i sumuje wyniki.
* **Zbieraj (min/max/liczba)**: Zbiera wszystkie pasujące reguły i wybiera minimum, maksimum lub liczy wystąpienia.
* **Kolejność Reguł**: Zastosowuje reguły w kolejności, w jakiej pojawiają się w drzewie decyzyjnym.
* **Jakakolwiek**: Może być zastosowana dowolna pasująca reguła, co pozwala na wiele wyników.

**Przykład Polityki Drzewa Decyzyjnego w Działaniu**

W drzewie decyzyjnym "Cena Grupy Bezpośredniej":

* **Wybrana Polityka**: `Pierwsza`
* Oznacza to, że jak tylko warunek reguły zostanie spełniony, zastosowane zostaje przypisane działanie, a dalsze reguły nie są oceniane.

#### Eksport i Zapis

* **Zapisz**: Zapisuje bieżącą konfigurację drzewa decyzyjnego.
* **Eksportuj**: Umożliwia eksportowanie konfiguracji drzewa decyzyjnego, która może być następnie importowana do innego środowiska lub używana do celów kopii zapasowej.
