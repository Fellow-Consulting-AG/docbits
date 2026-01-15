# Konfigurowanie Właściwości Pola

## Szczegółowe instrukcje dotyczące ustawiania właściwości, takich jak Wymagane, Tylko do odczytu, Ukryte i OCR.

### Wymagane (Required):

<figure><img src="../../../../../.gitbook/assets/docbits_configure_classification_rule.png" alt="Docbits Configure Classification Rule"><figcaption></figcaption></figure>

Jeśli pole jest oznaczone jako Wymagane, oznacza to, że pole to musi zostać wypełnione przed zapisaniem lub przetworzeniem dokumentu.

**Aby ustawić tę właściwość:**

* Przejdź do ustawień pola w systemie DocBits.
* Włącz opcję Wymagane dla odpowiedniego pola.

**Wpływ:**

* To ustawienie zapewnia, że ważne informacje zostaną przechwycone i że żadne dokumenty nie zostaną przetworzone bez wymaganych danych.

### Tylko do odczytu (Read Only):

<figure><img src="../../../../../.gitbook/assets/docbits_model_prediction_test.png" alt="Docbits Model Prediction Test"><figcaption></figcaption></figure>

Jeśli pole jest oznaczone jako Tylko do odczytu, oznacza to, że użytkownicy mogą przeglądać zawartość tego pola, ale nie mogą wprowadzać w nim żadnych zmian.

**Aby ustawić tę właściwość:**

* Przejdź do Opcji Pola. Włącz opcję Tylko do odczytu dla wybranego pola.

**Wpływ:**

* To ustawienie może być przydatne do ochrony wrażliwych informacji lub zapewnienia, że ważne dane nie zostaną przypadkowo zmienione.

### Ukryte (Hidden):

<figure><img src="../../../../../.gitbook/assets/docbits_classification_extraction_settings.png" alt="Docbits Classification Extraction Settings"><figcaption></figcaption></figure>

Jeśli pole jest oznaczone jako „Ukryte”, oznacza to, że pole zostanie ukryte w interfejsie użytkownika i użytkownicy nie będą mogli go zobaczyć ani uzyskać do niego dostępu.

**Aby ustawić tę właściwość:**

* Przejdź do opcji pola.
* Włącz opcję „Ukryte” dla odpowiedniego pola.

**Wpływ:**

* To ustawienie jest często używane do ukrywania pól wewnętrznych lub technicznych, które są nieistotne dla użytkownika końcowego lub są potrzebne tylko do przetwarzania wewnętrznego.

### OCR (Optyczne Rozpoznawanie Znaków):

<figure><img src="../../../../../.gitbook/assets/image (114).png" alt=""><figcaption></figcaption></figure>

Jeśli pole jest skonfigurowane pod kątem OCR, oznacza to, że system spróbuje wyodrębnić tekst z dokumentu i wstawić go do tego pola. To ustawienie jest zwykle używane dla pól, które mają być wypełniane automatycznie.

**Aby to skonfigurować:**

* Włącz opcję OCR dla odpowiedniego pola.
* Jeśli to konieczne, skonfiguruj parametry OCR, takie jak język, czcionka itp.

**Wpływ:**

* Korzystanie z OCR umożliwia automatyczne przetwarzanie dokumentów poprzez wyodrębnianie informacji z tekstów i wprowadzanie ich do odpowiednich pól, co zmniejsza wysiłek ręczny i zwiększa wydajność.

### Wymuszona walidacja (Forced validation):

<figure><img src="../../../../../.gitbook/assets/docbits_sql_alter_table_syntax.png" alt="Docbits Sql Alter Table Syntax"><figcaption></figcaption></figure>

Skonfiguruj odpowiednio reguły walidacji, takie jak limity numeryczne, wyrażenia regularne lub relacje z innymi polami.

**Aby to skonfigurować:**

* Zapisz zmiany.

**Wpływ:**

* Wymuszona walidacja sprawdza wprowadzone dane pod kątem określonych kryteriów, aby upewnić się, że są one poprawne. Pomaga to wcześnie wykrywać błędy i poprawiać jakość danych.

### Wynik dopasowania (Match Score):

<figure><img src="../../../../../.gitbook/assets/docbits_add_new_column_steps.png" alt="Docbits Add New Column Steps"><figcaption></figcaption></figure>

Porównując dane wejściowe z danymi referencyjnymi, Match Score może pomóc potwierdzić dokładność i ważność danych. Jeśli Match Score przekroczy określony próg, dopasowanie uważa się za udane.

**Aby to skonfigurować:**

* Włącz opcję Match Score i ustaw pożądany próg.
* Zapisz zmiany.

**Wpływ:**

* Match Score służy do oceny dokładności dopasowań między danymi wejściowymi a wartościami referencyjnymi. Jeśli uzyskany wynik przekroczy ustawiony próg, dopasowanie uważa się za udane. Jest to szczególnie przydatne w przypadku pól wymagających walidacji danych lub dopasowywania danych, takich jak pola z nazwiskiem, adresem e-mail itp. np. podczas sprawdzania danych klientów.

<figure><img src="../../../../../.gitbook/assets/docbits_column_requirements_analysis.png" alt="Docbits Column Requirements Analysis" width="258"><figcaption></figcaption></figure>

Starannie konfigurując te właściwości pól, możesz zoptymalizować przepływy pracy przetwarzania dokumentów i zapewnić, że dane są poprawnie przechwytywane, chronione i wydajnie przetwarzane.
