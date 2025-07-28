# Szkolenie Pól Linii/Szkolenie Tabeli

## Szkolenie Tabeli: Kiedy i Jak Je Używać

DocBits domyślnie korzysta z ekstrakcji tabel opartej na sztucznej inteligencji, która działa w przypadku różnych dostawców. Jednakże, gdy potrzebujesz większej kontroli nad tym, jak elementy linii są ekstrahowane dla konkretnego dostawcy, możesz użyć **Szkolenia Tabeli** do ręcznego zdefiniowania struktury.

#### **Ważne: Szkolenie Specyficzne dla Dostawcy**

Szkolenie tabeli jest **specyficzne dla każdego dostawcy**. Jeśli przeszkolisz układ tabeli dla jednego dostawcy, zasady będą obowiązywać tylko w dokumentach tego dostawcy.\
Inni dostawcy będą nadal korzystać z ekstrakcji tabel opartej na sztucznej inteligencji, chyba że zostaną przeszkoleni oddzielnie.

#### Kiedy Należy Użyć Szkolenia Tabeli?

Użyj Szkolenia Tabeli **tylko wtedy, gdy układ dokumentu jest stabilny**, i chcesz zapewnić spójną, wysokiej jakości ekstrakcję. Najlepiej nadaje się dla dostawców, którzy:

* Używają **ustalonego formatu faktury** w czasie.
* Wymagają **precyzyjnego mapowania** elementów linii do konkretnych pól.
* Są **dostawcami o dużym wolumenie**, gdzie spójna automatyzacja jest cenna.

#### Kiedy Nie Używać Szkolenia Tabeli

Unikaj korzystania ze Szkolenia Tabeli jeśli:

* Dostawca **często zmienia układ swojej faktury** (np. co kilka miesięcy).
* Nie otrzymujesz regularnie dokumentów od tego dostawcy.
* Domyślna ekstrakcja oparta na sztucznej inteligencji działa **wystarczająco dobrze** bez ręcznego szkolenia.

W takich przypadkach wielokrotne przeszkolenie tabeli byłoby nieskuteczne i czasochłonne.

## Jak Je Używać:

**Tryb Szkolenia** służy do nauczenia DocBits, jak poprawnie ekstrahować elementy linii z układu dokumentu konkretnego dostawcy.

Gdy jesteś w Trybie Szkolenia, definiujesz:

* **Gdzie znajduje się tabela** na dokumencie.
* **Które obszary odpowiadają każdej kolumnie** (np. Ilość, Opis, Cena Jednostkowa).

Ten tryb tworzy **szablon ekstrakcji do ponownego użycia** dla tego dostawcy, dzięki czemu przyszłe dokumenty o tym samym układzie będą przetwarzane automatycznie — nie trzeba ponownie szkolić.

**Kluczowe Cechy:**

* **Zmapowane kolumny są tylko do odczytu** — nie można ręcznie zmieniać tekstu.
* **Nie można dodawać ani usuwać wierszy**.
* Skupiasz się na **mapowaniu pozycji**, a nie na poprawianiu wartości.
* Gdy zakończysz mapowanie tabeli i jej kolumn, kliknij **"Zapisz Zasady"**, aby DocBits nauczył się i zastosował to szkolenie do podobnych dokumentów od tego samego dostawcy.

**Tryb Korekty** pozwala ci **poprawić błędy ekstrakcji** w danych tabeli dla bieżącego dokumentu. Jest używany, gdy DocBits już próbował ekstrahować tabelę, ale wyniki wymagają niewielkich poprawek.

Użyj Trybu Korekty, gdy:

* Niektóre **wartości są brakujące lub źle wyrównane**.
* Wyekstrahowano **pusty lub zduplikowany wiersz**, który trzeba usunąć.

**Co Możesz Zrobić w Trybie Korekty:**

* **Ręcznie dostosować wartości** w zmapowanych kolumnach (np. naprawić przemieszczenia).
* **Usunąć wiersze**, które nie powinny być częścią tabeli.
* **Dodać wiersze**, które zostały pominięte podczas ekstrakcji.
