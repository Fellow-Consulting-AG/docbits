# Typy dokumentów

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 08.44.19.png" alt=""><figcaption></figcaption></figure>

#### Przegląd

Sekcja Typy Dokumentów wymienia wszystkie typy dokumentów rozpoznawanych i przetwarzanych przez Docbits. Administratorzy mogą zarządzać różnymi aspektami takimi jak układ, definicje pól, reguły ekstrakcji i inne dla każdego rodzaju dokumentu. Ta dostosowalność jest kluczowa dla zapewnienia dokładnej obsługi danych i zgodności z normami organizacyjnymi.

#### Główne funkcje i opcje

1. **Lista Typów Dokumentów**:
* Każdy wiersz reprezentuje typ dokumentu, takie jak Faktura, Nota Kredytowa, Nota Dostawy, itp.
* Typy dokumentów mogą być standardowe lub niestandardowe, co jest wskazane przez etykiety takie jak "Standardowy."
2. **Edytuj układ**: Ta opcja pozwala administratorom modyfikować ustawienia układu dokumentu, które obejmują określenie wyglądu dokumentu i miejsca, w którym znajdują się pola danych.
3. **Podtypy dokumentów**: Jeśli jakiekolwiek typy dokumentów mają podkategorie, ta opcja pozwala administratorom skonfigurować ustawienia specyficzne dla każdego podtypu.
4. **Kolumny tabeli**: Dostosuj, które kolumny danych powinny pojawić się, gdy typ dokumentu jest wyświetlany na listach lub raportach.
5. **Pola**: Zarządzaj polami danych powiązanymi z typem dokumentu, w tym dodawanie nowych pól lub modyfikowanie istniejących.
6. **Szkolenie modelu**: Skonfiguruj i trenuj model używany do rozpoznawania i ekstrakcji danych z dokumentów. Może to obejmować ustawianie parametrów modeli uczenia maszynowego, które poprawiają się z czasem dzięki większej ilości danych.
7. **Wyrażenia regularne (Regex)**: Skonfiguruj wyrażenia regularne, które są używane do ekstrakcji danych z dokumentów na podstawie wzorców. Jest to szczególnie przydatne do ekstrakcji danych strukturalnych.
8. **Skrypty**: Napisz lub zmodyfikuj skrypty, które uruchamiają niestandardowe reguły przetwarzania lub przepływy pracy dla dokumentów tego typu.
9. **EDI (Elektroniczna Wymiana Danych)**: Skonfiguruj ustawienia związane z wymianą dokumentów w standardowych formatach elektronicznych.

{% hint style="info" %}
Zobacz [Konfiguracja Typu Dokumentu](../../../setup/document-types/)
{% endhint %}

{% @jira/embed url="https://fellowpro.atlassian.net/browse/DOCB-2489" %}
