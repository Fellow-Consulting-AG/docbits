# Ustawienia OCR

## Przegląd

W ustawieniach **OCR (Optical Character Recognition)** możesz skonfigurować, jak OCR jest stosowane podczas przetwarzania dokumentów. Obejmuje to określenie minimalnej wymaganej jakości, wybór, czy używać tekstu osadzonego (e-text), wybór wersji OCR i inne. Ta strona zawiera szczegółowe wyjaśnienie wszystkich dostępnych ustawień.

## Jak uzyskać dostęp do ustawień OCR

Aby uzyskać dostęp do ustawień OCR:

*   Przejdź do: **Ustawienia** → **Przetwarzanie dokumentów** → **Ustawienia OCR**

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_ocr.png)

## Jakość OCR

W tej sekcji możesz ustawić minimalną jakość dokumentu wymaganą do przetwarzania OCR, dostosowując suwak jakości. Przesuń suwak w lewo lub w prawo, aby odpowiednio zmniejszyć lub zwiększyć próg jakości.

Jeśli dokument nie spełnia zdefiniowanego poziomu jakości, DocBits oferuje trzy opcje jego obsługi:

* **Biegnij mimo wszystko**\
  Dokument zostanie przetworzony niezależnie od jego jakości.
* **Uruchom ponownie po potwierdzeniu**\
  **DocBits** zatrzyma się i poprosi o potwierdzenie, czy kontynuować przetwarzanie.
* **Wyrzuć błąd**\
  Przetwarzanie dokumentu całkowicie się zatrzyma, a na ekranie pojawi się komunikat o błędzie, wskazujący, że dokument nie spełnia wymaganego progu jakości.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ocr_settings_1.png)

## Ogólne ustawienia OCR

* **Użyj E-Textu, jeśli jest dostępny**\
  Po włączeniu **DocBits** użyje osadzonego tekstu elektronicznego (np. z PDF-ów) zamiast przeprowadzać OCR. To poprawia zarówno szybkość, jak i dokładność, ponieważ tekst jest wyodrębniany bezpośrednio bez potrzeby przetwarzania OCR.
* **Użyj DESKEW, jeśli jest dostępny**\
  Ta opcja automatycznie koryguje wyrównanie zeskanowanych dokumentów. Proste obrazki pomagają poprawić dokładność OCR.
*   **Wersja AI OCR**\
    Pozwala na wybór konkretnej wersji silnika OCR opartego na AI.\
    Może to być przydatne, jeśli:

    * Nie osiągasz pożądanych wyników z aktualnie wybraną wersją.
    * Rozwiązujesz problemy związane z wydajnością lub dokładnością OCR.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ocr_settings_2.png)

## Ustawienia OCR dla tabel

* **Jeśli są dostępne, użyj danych AI w tabelach**\
  Po włączeniu DocBits użyje danych OCR dla tabel zamiast osadzonego tekstu elektronicznego (E-Text) — nawet jeśli ustawienie **Użyj E-Textu, jeśli jest dostępny** jest włączone.

## Ustawienia OCR dla pól nagłówka

* **Użyj ekstrakcji reguł**\
  DocBits zastosuje Twoje zdefiniowane reguły ekstrakcji do identyfikacji pól nagłówka.
* **Użyj ekstrakcji AI**\
  DocBits użyje AI do automatycznego wykrywania i wyodrębniania pól nagłówka.

**Kolejność wykonania:**\
Jeśli obie opcje są włączone, **DocBits** przeprowadzi ekstrakcję w następującej kolejności:\
**Ekstrakcja reguł → Ekstrakcja AI**\
\
<mark style="color:red;">**Uwaga**</mark>: Aby uzyskać najlepsze wyniki i spójną zachowanie, włącz obie opcje. Pozwoli to **DocBits** na wykorzystanie zarówno metod opartych na regułach, jak i metod opartych na AI w połączeniu podczas ekstrakcji nagłówków.
