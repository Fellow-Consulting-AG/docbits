# Pola

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 09.02.31.png" alt=""><figcaption></figcaption></figure>

#### Przegląd

Ustawienie Pola zapewnia interfejs użytkownika, w którym administratorzy mogą zarządzać właściwościami i zachowaniem poszczególnych pól danych powiązanych z typem dokumentu. Każde pole można dostosować, aby zoptymalizować dokładność i wydajność przechwytywania danych oraz walidacji.

#### Główne funkcje i opcje

1. **Konfiguracja pól**:
* **Nazwy pól**: Wyświetla nazwy pól, zazwyczaj odpowiadające elementom danych w dokumencie, takie jak "Numer faktury" lub "Data zamówienia".
* **Wymagane**: Administratorzy mogą oznaczyć pola jako wymagane, zapewniając, że dane muszą zostać wprowadzone lub przechwycone, aby ukończyć przetwarzanie dokumentu.
* **Tylko do odczytu**: Pola można ustawić jako tylko do odczytu, aby zapobiec modyfikacji po przechwyceniu danych lub podczas określonych etapów przetwarzania dokumentu.
* **Ukryte**: Pola można ukryć w interfejsie użytkownika, co jest przydatne dla poufnych informacji lub w celu uproszczenia procesów użytkownika.
2. **Zaawansowane ustawienia**:
* **Wymuszenie walidacji**: Zapewnia, że dane wprowadzone do pola przechodzą określone reguły walidacji przed zaakceptowaniem.
* **OCR (Optyczne rozpoznawanie znaków)**: Ten przełącznik można włączyć, aby umożliwić przetwarzanie OCR dla określonego pola, co jest przydatne do automatycznego wyodrębniania danych zeskanowanych lub cyfrowych dokumentów.
* **Wynik dopasowania**: Administratorzy mogą zdefiniować wynik dopasowania, czyli próg używany do określenia poziomu pewności rozpoznawania lub dopasowania danych, wpływający na sposób wykonywania walidacji danych i kontroli jakości.
3. **Przyciski akcji**:
* **Utwórz nowe pole**: Umożliwia dodanie nowych pól do typu dokumentu.
* **Ikony edycji**: Każde pole ma ikonę edycji, która umożliwia administratorom dalszą konfigurację ustawień specyficznych dla pola, takich jak typ danych, wartości domyślne lub powiązana logika biznesowa.
* **Zapisz ustawienia**: Zatwierdza dokonane zmiany w konfiguracjach pola.

{% @jira/embed url="https://fellowpro.atlassian.net/browse/DOCB-2494" %}
