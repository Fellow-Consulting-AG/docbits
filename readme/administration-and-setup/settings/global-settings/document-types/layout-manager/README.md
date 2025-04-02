# Layout Manager

<figure><img src="../../../../../.gitbook/assets/Bildschirmfoto%202024-05-08%20um%2008.46.24.png" alt=""><figcaption></figcaption></figure>

#### Przegląd

Menedżer układu umożliwia administratorom wizualną konfigurację i modyfikację układu typów dokumentów poprzez ustawianie właściwości dla różnych pól danych i grup w dokumencie. Ten interfejs pomaga zapewnić, że modele ekstrakcji i punkty ręcznego wprowadzania danych są dokładnie zgodne z strukturą dokumentu zeskanowanego lub przesłanego do DocBits.

#### Główne składniki

1. **Grupy i pola**:

* **Grupy**: Jednostki organizacyjne w obrębie typu dokumentu, które kategoryzują powiązane pola (np. Szczegóły faktury, Szczegóły płatności). Mogą być rozszerzane lub zwijane oraz ustawiane tak, aby odzwierciedlać logiczne grupowanie w rzeczywistym dokumencie.
* **Pola**: Indywidualne punkty danych w każdej grupie (np. Numer faktury, Warunki płatności). Każde pole może być dostosowane pod kątem sposobu przechwytywania, wyświetlania i przetwarzania danych.

2. **Panel właściwości**:

* Ten panel wyświetla właściwości wybranego pola lub grupy, umożliwiając szczegółową konfigurację, taką jak:
* **Etykieta**: Widoczna etykieta pola w interfejsie użytkownika.
* **Nazwa pola**: Techniczny identyfikator używany w systemie.
* **Szerokość elementu w procentach**: Określa szerokość pola w stosunku do układu dokumentu.
* **Indeks zakładki**: Kontroluje kolejność przemieszczania się za pomocą klawiszy TAB.
* **Uruchom skrypt po zmianie**: Czy ma zostać wykonany skrypt po zmianie wartości pola.
* **Wyświetl etykietę po lewej**: Czy etykieta ma być wyświetlana po lewej stronie pola czy nad nim.
* **Jest polem tekstowym**: Określa, czy pole powinno być polem tekstowym, dostosowującym się do większych ilości tekstu.
* **Wybierz typ modelu**: Opcja wyboru, który typ modelu będzie obsługiwał ekstrakcję tego pola.
* **Długość pola**: Maksymalna długość danych do zaakceptowania w tym polu.
* **Zabronione słowa kluczowe**: Słowa kluczowe niedozwolone w polu.

3. **Podgląd szablonu**:

* Pokazuje podgląd w czasie rzeczywistym, jak będzie wyglądał dokument na podstawie bieżącej konfiguracji układu. Pomaga to w zapewnieniu, że układ odpowiada rzeczywistej strukturze dokumentu i jest kluczowy do testowania i udoskonalania konfiguracji przetwarzania dokumentów.

{% @jira/embed url="https://fellowpro.atlassian.net/browse/DOCB-2490" %}
