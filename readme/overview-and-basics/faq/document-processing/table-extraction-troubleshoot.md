# Rozwiązywanie problemów z ekstrakcją tabeli

## **Krok 1: Otwórz widok OCR dla złych wyników ekstrakcji**

Jeśli wyniki szkolenia ekstrakcji tabeli nie są dobre:

1. Otwórz **widok OCR**, klikając na ikonę lupy z napisem **OCR**.
2. Przejrzyj wyniki ekstrakcji i sprawdź, czy proces OCR może poprawić przechwytywanie danych.
3. Jeśli wyniki nadal są złe, spróbuj innego dokumentu, aby sprawdzić, czy problem jest związany z dokumentem.
4. Jeśli problem jest związany z dokumentem, użyj innego dokumentu do ekstrakcji.
   * Jeśli problem nadal występuje, przejdź do kolejnych kroków.

## **Krok 2: Sprawdź dostępność e-tekstu**

1. Sprawdź, czy dokument zawiera dostępny **e-tekst**.
   * Możesz to zweryfikować za pomocą narzędzia takiego jak **Adobe Acrobat**.
   * Jeśli dokument zawiera e-tekst, przejdź do **Kroku 3.**
   * Jeśli dokument nie zawiera e-tekstu, przejdź do **Kroku 4.**

## **Krok 3: Włącz ekstrakcję e-tekstu**

Jeśli dokument zawiera e-tekst, masz dwie opcje:

1. **Włącz ekstrakcję e-tekstu tylko dla tego dostawcy**:
   * Wróć do **Walidacji Pola Dokumentów**.
   * Kliknij kwadrat z trzema kropkami w lewym pasku narzędzi.
   * Tutaj aktywuj opcję **Użyj e-tekstu, jeśli jest dostępny**, aby włączyć ją tylko dla tego dostawcy.
2. **Włącz ekstrakcję e-tekstu dla wszystkich dostawców**:
   * Przejdź do **Ustawienia** > **Przetwarzanie Dokumentów** > **Ustawienia OCR**.
   * W tej sekcji znajdziesz opcję **Użyj e-tekstu, jeśli jest dostępny** i możesz włączyć ją dla wszystkich dostawców.
3. Po włączeniu ekstrakcji e-tekstu, ponów szkolenie ekstrakcji tabeli.
   * Jeśli wyniki się poprawią, problem zostanie rozwiązany.
   * Jeśli wyniki nadal są złe, przejdź do **Kroku 4**.

## **Krok 4: Brak dostępnego e-tekstu - Zmień wersję AI OCR**

Jeśli dokument nie zawiera dostępnego e-tekstu:

1. Przejdź do **Ustawienia** > **Przetwarzanie Dokumentów** > **Ustawienia OCR**.
2. Zmień **Wersję AI OCR** na inną wersję.
3. Wróć do **Szkolenia Ekstrakcji Tabeli** i spróbuj ponownie.
4. Jeśli wynik jest lepszy:
   * Sprawdź inne dokumenty od różnych dostawców, aby upewnić się, że wyniki ekstrakcji dla tych dostawców nie są dotknięte tą zmianą.
   * **Bądź ostrożny, ponieważ ta zmiana może wpłynąć na wyniki ekstrakcji innych dostawców.**
   * Ta zmiana może wpłynąć na innych dostawców, dlatego upewnij się, że dokładnie zweryfikujesz wyniki, aby nie miały negatywnego wpływu na ekstrakcje dokumentów innych dostawców.
5. Jeśli wynik nie poprawił się po zmianie wersji AI OCR, prosimy o **kontakt z nami** w celu uzyskania dalszej pomocy.
