# Wiadomości e-mail przychodzące

## Aktywacja Wiadomości e-mail przychodzących dla Przetwarzania dokumentów

Aby rozpocząć korzystanie z wiadomości e-mail przychodzących do przetwarzania dokumentów, wykonaj następujące kroki:

1. **Przejdź do Ustawienia**: Rozpocznij od przejścia do menu **Ustawienia** aplikacji.
2. **Wybierz Przetwarzanie dokumentów**: W sekcji ustawień wybierz **Przetwarzanie dokumentów**, aby uzyskać dostęp do powiązanych opcji konfiguracyjnych.
3. **Otwórz Moduły**: W sekcji Przetwarzanie dokumentów kliknij na **Moduły**.
4. **Przewiń do Typ dokumentu**: Przewiń w dół, aż znajdziesz **Typ dokumentu**.
5. **Aktywuj Wiadomość e-mail przychodzącą**: Znajdź **Wiadomość e-mail przychodzącą** i aktywuj ją, przełączając przełącznik.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/inbound_emails_1.png)

## Konfigurowanie Wiadomości e-mail przychodzącej do Importu dokumentów

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/inbound_emails_2.png)

Po aktywacji wiadomości e-mail przychodzącej skonfiguruj ustawienia, aby kontrolować, jak dokumenty są importowane. Oto jak:

1. **Wróć do Przetwarzania dokumentów**: W ustawieniach przejdź do **Przetwarzanie dokumentów**.
2.  **Wybierz Import**: Wybierz **Import**, aby uzyskać dostęp do ustawień wiadomości e-mail przychodzącej.

    Zobaczysz następujące opcje:

    * **Pole e-mail**: To pole wyświetla unikalny, systemowo generowany adres e-mail oparty na identyfikatorze Twojej organizacji. Format to `org_id@environment.inbound.docbits.com`. Wyślij lub przekaż e-maile z dokumentami na ten adres, aby zautomatyzować import.
    * **Importuj dokumenty tylko z predefiniowanych adresów e-mail**: Przełącz tę opcję, aby ograniczyć importy do e-maili otrzymanych tylko z określonych, predefiniowanych adresów.
    * **Odpowiedz na ten e-mail, jeśli import nie może zostać wykonany**: Przełącz tę opcję, jeśli chcesz, aby system automatycznie odpowiadał, gdy próba importu się nie powiedzie.
3. **Zapisz Ustawienia**: Po skonfigurowaniu tych opcji kliknij **Ratować**, aby je zastosować.

## Predefiniowane adresy e-mail

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/inbound_emails_3.png)

Gdy opcja **Importuj dokumenty tylko z predefiniowanych adresów e-mail** jest włączona, możesz zarządzać, które adresy e-mail są uprawnione do wysyłania dokumentów na wiadomość e-mail przychodzącą.

1. **Wprowadź Autoryzowane e-maile**: W polu **Wprowadź e-mail tutaj** wpisz każdy adres e-mail, który chcesz autoryzować.
2. **Przypisz do Podorganizacji (Opcjonalnie)**:
   * Jeśli nie wybrano podorganizacji, dokument zostanie przypisany do głównej organizacji.
   * Jeśli wybrano podorganizację, dokument zostanie skierowany tylko do tej podorganizacji.
3. **Dodaj E-mail**: Kliknij **Dodać**, aby zapisać każdy e-mail na liście autoryzowanych adresów.
4. **Usuń E-mail**: Aby usunąć autoryzowany e-mail, kliknij **Usuwać** obok wpisu e-mail.

Dzięki tej konfiguracji dokumenty z nieautoryzowanych adresów e-mail będą ignorowane, co zapewni, że tylko określone źródła mogą wysyłać dokumenty do importu.

## **Odpowiedz na ten e-mail, jeśli import nie może zostać wykonany**

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/inbound_emails_4.png)

Jeśli włączysz **Odpowiedz na ten e-mail, jeśli import nie może zostać wykonany**, pojawi się dodatkowe pole, w którym możesz wpisać adres e-mail. Ten adres e-mail otrzyma powiadomienie, jeśli jakakolwiek próba importu dokumentu się nie powiedzie, co pozwoli Ci być na bieżąco z problemami w procesie importu.

1. **Włącz Powiadomienie o Niepowodzeniu**: Włącz **Odpowiedz na ten e-mail, jeśli import nie może zostać wykonany**.
2. **Wprowadź E-mail Powiadomienia**: W nowym polu wpisz adres e-mail, na który chcesz otrzymywać powiadomienia o niepowodzeniach.

Po włączeniu tej funkcji wszelkie nieudane próby importu spowodują automatyczną odpowiedź na wskazany e-mail, co pomoże Ci szybko rozwiązać problemy z importem.

**Po skonfigurowaniu wszystkich ustawień nie zapomnij kliknąć Ratować, aby zastosować zmiany.**
