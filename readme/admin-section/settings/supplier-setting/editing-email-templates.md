### Przegląd

Funkcja Szablonów E-mail pozwala administratorom na tworzenie i dostosowywanie komunikacji e-mail, która jest automatycznie wysyłana do dostawców. Jednym z kluczowych elementów używanych w tych szablonach jest `{{magic_link}}`, który zapewnia dynamiczny link dostosowany do każdego odbiorcy.

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-08-25 um 12.33.35.png" alt="Portal Dostawcy - Szablon E-mail"><figcaption></figcaption></figure>

#### Czym jest `{{magic_link}}`?

`{{magic_link}}` to placeholder, który jest dynamicznie zastępowany unikalnym URL-em, gdy e-mail jest wysyłany. Ten URL zazwyczaj kieruje odbiorcę do wykonania akcji, takiej jak rejestracja, zatwierdzenie lub uzyskanie dostępu do konkretnej części portalu dostawcy.

### Edytowanie Szablonów E-mail

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-08-25 um 12.35.53.png" alt=""><figcaption></figcaption></figure>

#### Uzyskiwanie dostępu do Edytora Szablonów E-mail

1. **Przejdź do Szablonów E-mail**:
   * Przejdź do sekcji **Szablony E-mail** z głównego menu.
2. **Wybierz Szablon do Edycji**:
   * Wybierz szablon e-mail, który chcesz edytować, klikając na nazwę szablonu (np. "E-mail zaproszenie dla dostawcy").
3. **Edytuj Szablon**:
   * Edytor pozwala na modyfikację zarówno kodu HTML, jak i wizualnego wyglądu e-maila.
   * Możesz przełączać się między edytowaniem wizualnym a edytowaniem kodu, korzystając z dostępnych zakładek.

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-08-25 um 12.36.41.png" alt=""><figcaption></figcaption></figure>

#### Definiowanie `{{magic_link}}` jako Linku

Aby zdefiniować `{{magic_link}}` jako klikalny link w e-mailu, musisz upewnić się, że jest on poprawnie sformatowany w kodzie HTML szablonu. Wykonaj następujące kroki:

1. **Zlokalizuj Sekcję Linku w Kodzie HTML**:
   * W edytorze kodu znajdź sekcję, w której chcesz, aby magiczny link się pojawił. Zazwyczaj znajduje się to w tagu `<a>` (kotwica).
2. **Wstaw Placeholder `{{magic_link}}`**:

    * Zastąp atrybut `href` tagu kotwicy `{{magic_link}}`.
    * Upewnij się, że link jest odpowiednio stylizowany dla szablonu e-mail. Oto przykład:

    ```html
    <a href="{{magic_link}}" target="_blank" style="
        background-color: #B7184B;
        border-radius: 25px;
        font-family: 'Montserrat', Arial, sans-serif;
        font-size: 14px;
        font-weight: bold;
        padding: 12px 25px;
        color: #FFFFFF;
        text-decoration: none;
        display: inline-block;
        cursor: pointer;">
        Ukończ Rejestrację
    </a>
    ```

### 3. Dostosuj Tekst Linku:

• Zmień tekst pomiędzy otwierającymi \<a> a zamykającymi \</a> tagami, aby odzwierciedlał akcję, którą chcesz, aby użytkownik wykonał. Na przykład „Ukończ Rejestrację” lub „Uzyskaj Dostęp do Swojego Konta”.

4\. Zapisz i Przetestuj Szablon:

• Po wprowadzeniu zmian kliknij przycisk Zapisz.

• Możesz użyć przycisku Wyślij Test, aby wysłać testowy e-mail i upewnić się, że link działa zgodnie z oczekiwaniami.

## Najlepsze Praktyki Używania \{{magic\_link\}}

• Umiejscowienie Linku: Umieść \{{magic\_link\}} w widocznym miejscu w e-mailu, aby zapewnić łatwy dostęp dla odbiorców.

• Jasne Wezwanie do Działania: Tekst w linku powinien być jasnym wezwaniem do działania, takim jak „Ukończ Rejestrację” lub „Potwierdź Swój E-mail”.

• Stylizacja: Upewnij się, że link jest stylizowany w sposób spójny z resztą szablonu e-mail i wyróżnia się wizualnie.

• Testowanie: Zawsze wysyłaj testowy e-mail po edytowaniu szablonu, aby zweryfikować, że \{{magic\_link\}} działa poprawnie i stylizacja jest odpowiednia.

## Podsumowanie

Poprzez odpowiednie zdefiniowanie \{{magic\_link\}} w swoich szablonach e-mail, możesz zapewnić, że odbiorcy otrzymają spersonalizowany i wykonalny e-mail, który prowadzi ich do odpowiedniego zadania w Twoim portalu dostawcy. To poprawia doświadczenie użytkownika i zapewnia płynne procesy onboardingu i komunikacji.

\

Ta dokumentacja zawiera instrukcje krok po kroku dla administratorów, jak zdefiniować i używać \{{magic\_link\}} w szablonach e-mail, zapewniając, że e-maile są zarówno funkcjonalne, jak i estetyczne.