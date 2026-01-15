# Jak Utworzyć Dostęp do Bazy Danych dla Konkretnego Użytkownika Organizacji

### **1. Zaloguj się do Docbits** <a href="#id-1.-login-to-the-docbits" id="id-1.-login-to-the-docbits"></a>

1. Przejdź do strony logowania swojej aplikacji.
2. Wprowadź swoje dane uwierzytelniające (nazwę użytkownika i hasło), aby się zalogować.

### **2. Uzyskaj Dostęp do Ustawień** <a href="#id-2.-access-the-settings" id="id-2.-access-the-settings"></a>

1. Po zalogowaniu znajdź ikonę **Ustawienia** (koło zębate ⚙️) na lewym pasku bocznym.
2. Kliknij **Ustawienia**, aby otworzyć panel konfiguracji systemu.

### **3. Otwórz Moduł Przetwarzania Dokumentów** <a href="#id-3.-open-the-document-processing-module" id="id-3.-open-the-document-processing-module"></a>

1. W **Ustawieniach** znajdź sekcję **Przetwarzanie Dokumentów**.
2. W sekcji **Przetwarzanie Dokumentów** znajdź i kliknij opcję **Moduł**.
   * Otworzy to odpowiednią stronę konfiguracji modułu, na której możesz przejść do tworzenia użytkownika dla bazy danych.

<figure><img src="../../../../.gitbook/assets/docbits_db_access_creation.png" alt="Docbits Db Access Creation"><figcaption></figcaption></figure>

### 4. Kroki, aby Włączyć i Uzyskać Dostęp do Użytkownika Dokumentów AI i Bazy Danych: <a href="#id-4.-steps-to-enable-and-access-the-ai-document-and-database-user" id="id-4.-steps-to-enable-and-access-the-ai-document-and-database-user"></a>

1. **Przełącz Funkcje**:
   * Użyj przełączników po prawej stronie, aby włączyć lub wyłączyć określone funkcje:
     * **Magazyn Dokumentów AI**: Włącz to, aby umożliwić dostęp do funkcji związanych z AI.
     * **Dostęp do BD**: Włącz to, aby przyznać użytkownikowi dostęp do bazy danych.

<figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

2. **Dane Uwierzytelniające Bazy Danych**:
   * Pulpit nawigacyjny udostępnia następujące szczegóły połączenia z bazą danych:
     * **Nazwa użytkownika**: Wyświetlana jest unikalna nazwa użytkownika.
     * **Hasło**: Upewnij się, że hasło jest bezpiecznie przechowywane lub skopiowane.
     * **Baza danych**: To nazwa Bazy Danych.
     * **Host**: Nazwa Hosta.
     * **Port**: To Port.
     * **Tryb SSL:** Połączenie wymaga `sslmode=require` dla bezpiecznej komunikacji.
3. **Kopiowanie Danych Uwierzytelniających**:
   * Użyj ikon kopiowania obok każdego pola, aby szybko skopiować dane uwierzytelniające do użycia w kliencie bazy danych lub aplikacji.
4. **Połączenie przez DBeaver:**
   *   Połącz przez Host

       * wybierz PostgreSQL

       <figure><img src="../../../../.gitbook/assets/image (2) (1) (1) (2) (1) (1).png" alt=""><figcaption></figcaption></figure>

       * Wypełnij wymagane informacje

       <figure><img src="../../../../.gitbook/assets/image (4) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

       * przejdź do zakładki SSL i zaznacz Użyj SSL. Przejdź w dół do trybu SSL i wybierz require

       <figure><img src="../../../../.gitbook/assets/image (3) (1) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>
   *   Połącz przez URL

       * Wypełnij wymagane informacje:
         - zamień Host na podane informacje o hoście
         - zamień Port na podane informacje o porcie
         - zamień Baza danych na podane informacje o bazie danych
         - dla Nazwa użytkownika wybierz podane informacje o nazwie użytkownika
         - dla Hasło wybierz podane informacje o haśle

       <figure><img src="../../../../.gitbook/assets/image (5) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>
5. **Przetestuj Połączenie**:
   * Kliknij przycisk **"Testuj Połączenie"**, aby upewnić się, że dane uwierzytelniające i szczegóły połączenia są poprawne.
   * Jeśli test się powiedzie, przejdź do połączenia.
6. **Eksploruj Bazę Danych**:
   * Po połączeniu przejdź do sekcji **schemat** lub **tabele** w swoim kliencie bazy danych.
   * Sprawdź dostępne tabele.
