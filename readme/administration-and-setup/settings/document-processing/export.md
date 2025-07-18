# Eksport

## Przegląd

Strona Eksportu wyświetla wszystkie skonfigurowane ustawienia eksportu, w tym informacje o tym, czy są aktywne czy nieaktywne. Użytkownicy mogą tutaj:

* Przeglądać i zarządzać istniejącymi konfiguracjami eksportu
* Tworzyć nowe połączenia eksportowe (np. do **Infor**, **Infor & IDM**, **Webhook**, lub **SFTP**)
* Edytować lub usuwać istniejące konfiguracje eksportu

## Gdzie to znaleźć

Możesz znaleźć to pod: **Ustawienia** → **Przetwarzanie Dokumentów** → **Eksport**

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fn6ldlcI2sVUEgDdWb9U4%252Fimage.png%3Falt%3Dmedia%26token%3D8368818d-c899-4bee-ad21-a631d6be5c20\&width=768\&dpr=4\&quality=100\&sign=fbfcbd0c\&sv=2)

## **Korzystanie z Strony Eksportu**

Po otwarciu strony Eksportu, zobaczysz listę wszystkich istniejących konfiguracji eksportu.

Każdy wiersz na liście pokazuje:

* **Wskaźnik Statusu**
  * **Zielony** oznacza, że eksport jest aktywny
  * **Czerwony** oznacza, że eksport jest dezaktywowany
* **Nazwa** – nazwa konfiguracji eksportu
* **Typ Dokumentu** – typ dokumentu, dla którego skonfigurowano eksport
* **Pod-Organizacja** – jeśli eksport jest ograniczony do konkretnej pod-organizacji
* **Metoda Eksportu** – gdzie dokument zostanie wysłany (np. Infor, IDM, SFTP)
* **Działania** – przyciski do **edycji, usunięcia** lub **aktywacji/dezaktywacji** konfiguracji

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FyN87I5gzXxwGoAqC6zMF%252Fimage.png%3Falt%3Dmedia%26token%3D7df9d573-7e57-4ace-99c6-15a83691b926\&width=768\&dpr=4\&quality=100\&sign=6221cb80\&sv=2)

#### **Ważne Zasady Konfiguracji Eksportu**

Dla każdego **typu dokumentu** **w ramach danej organizacji lub pod-organizacji**, obowiązują następujące zasady:

* Możesz mieć **tylko jeden aktywny eksport Infor**
* Możesz mieć **tylko jeden aktywny eksport spoza Infor** (np. Webhook, SFTP)

Jednakże, jest możliwe mieć:

* **Jeden aktywny eksport Infor** _i_ **jeden aktywny eksport spoza Infor** jednocześnie dla tego samego typu dokumentu
* **Różne konfiguracje eksportu dla różnych pod-organizacji** — na przykład, jeden eksport Infor dla Pod-Org A i inny eksport Infor dla Pod-Org B

## **Tworzenie Nowego Eksportu**

Aby utworzyć nowy eksport:

1. Kliknij przycisk **“Nowy”**. \
   ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FTsHrIAUpe7EqenIzNAaJ%252Fimage.png%3Falt%3Dmedia%26token%3Dd2dbc996-b129-443c-a8df-9927a6f43a36\&width=300\&dpr=4\&quality=100\&sign=8769c331\&sv=2)
2. Wybierz **Typ Eksportu**, który chcesz skonfigurować (np. Infor, IDM, SFTP).
3. Wypełnij wymagane pola na podstawie typu eksportu.
4. Zapisz konfigurację.

## Opcje eksportu

#### Webhook

<details>

<summary>Webhook</summary>

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FCwXUqFdCbRI5lRW49ymw%252Fimage.png%3Falt%3Dmedia%26token%3D798c0f40-6c4a-4650-9320-af2c17634fe9\&width=768\&dpr=4\&quality=100\&sign=15836833\&sv=2)

#### **Opisy pól**

* **Tytuł** Nazwa konfiguracji eksportu. Będzie widoczna na liście eksportu.
* **Podorganizacja** _(opcjonalne)_ Lista rozwijana z dostępnymi podorganizacjami.
  * Jeśli pozostanie puste: dotyczy głównej organizacji.
  * Jeśli wybrane: eksport będzie dotyczył tylko wybranej podorganizacji.
* **Typ dokumentu** Lista rozwijana z dostępnymi typami dokumentów. Określa, do jakiego typu dokumentu ma być zastosowana ta konfiguracja eksportu.
* **URL eksportu** Docelowy URL, pod który ma zostać wyeksportowany dokument.

</details>

#### SFTP

<details>

<summary>SFTP</summary>

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FzwUCWTdFETTvuTGl8qAn%252Fimage.png%3Falt%3Dmedia%26token%3D3f94b210-0128-4710-ae69-150a1363ce49\&width=768\&dpr=4\&quality=100\&sign=4ecd353\&sv=2)

#### **Opisy pól**

* **Tytuł** Nazwa konfiguracji eksportu. Będzie widoczna na liście eksportów.
* **Podorganizacja** _(opcjonalne)_ Lista rozwijana z dostępnymi podorganizacjami.
  * Jeśli pozostanie puste: dotyczy głównej organizacji.
  * Jeśli wybrane: eksport będzie stosowany tylko do wybranej podorganizacji.
* **Typ dokumentu** Lista rozwijana z dostępnymi typami dokumentów. Określa, do jakiego typu dokumentu ma być stosowana ta konfiguracja eksportu.
* **Nazwa użytkownika** Nazwa użytkownika używana do uwierzytelnienia na serwerze SFTP.
* **Hasło** Odpowiadające hasło dla konta SFTP. Upewnij się, że konto ma uprawnienia do zapisu w określonym folderze.
* **Adres URL serwera** Nazwa hosta lub adres IP docelowego serwera SFTP.
* **Port** Port używany do połączenia z serwerem SFTP.
* **Folder** Ścieżka na serwerze SFTP, do której dokumenty powinny być przesyłane (np. `/incoming/invoices/`). Musi istnieć i być zapisywalny.
*   **Plik XSLT (Opcjonalnie)**

    Plik **XSLT** umożliwia transformację domyślnego formatu eksportu DocBits.

    * **Kiedy używać:** Tylko jeśli system docelowy wymaga innej struktury lub określonego formatowania, które różni się od domyślnego formatu DocBits.
    * **Pozostaw puste** jeśli domyślny format eksportu spełnia wymagania.

</details>

#### Eksport danych do SFTP w Infor

<details>

<summary>Eksport danych do SFTP w Infor</summary>

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FU0W4Qdy7ZlNoCn3E9wX5%252Fimage.png%3Falt%3Dmedia%26token%3D33673a12-55c4-479b-8ca8-b7c95e7a6a89\&width=768\&dpr=4\&quality=100\&sign=4af07f48\&sv=2)

#### **Opisy pól**

* **Tytuł** Nazwa konfiguracji eksportu. Będzie widoczna na liście eksportów.
* **Pod-Organizacja** _(opcjonalne)_ Lista rozwijana z dostępnymi pod-organizacjami.
  * Jeśli pozostanie puste: dotyczy głównej organizacji.
  * Jeśli wybrane: eksport będzie dotyczył tylko wybranej pod-organizacji.
* **Typ Dokumentu** Lista rozwijana z dostępnymi typami dokumentów. Określa, do jakiego typu dokumentu ma być zastosowana ta konfiguracja eksportu.
* **Plik mapowania IDM** Wybierz plik mapowania z menedżera plików. [Potrzebujesz pomocy przy tworzeniu? Zobacz Przewodnik po Mapowaniu IDM](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file)
* **Plik mapowania BOD** Wybierz plik mapowania z menedżera plików. [Potrzebujesz pomocy przy tworzeniu? Zobacz Przewodnik po Mapowaniu BOD](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file)
* **Folder** Ścieżka na serwerze SFTP, gdzie dokumenty powinny być przesłane (np. `/incoming/invoices/`). Musi istnieć i być zapisywalny.

</details>

#### **SMB**

<details>

<summary>SMB</summary>

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F6e4B9BWQWgHvcHhduXKb%252Fimage.png%3Falt%3Dmedia%26token%3D09e9534e-9268-4221-bd7b-89b621c80670\&width=768\&dpr=4\&quality=100\&sign=b03835a\&sv=2)

#### **Opisy pól**

* **Tytuł** Nazwa konfiguracji eksportu. Będzie widoczna na liście eksportu.
* **Pod-Organizacja** _(opcjonalne)_ Lista rozwijana z dostępnymi pod-organizacjami.
  * Jeśli pozostanie puste: dotyczy głównej organizacji.
  * Jeśli wybrane: eksport będzie dotyczył tylko wybranej pod-organizacji.
* **Typ Dokumentu** Lista rozwijana z dostępnymi typami dokumentów. Określa, do jakiego typu dokumentu ma być zastosowana ta konfiguracja eksportu.
* **Nazwa użytkownika** Nazwa użytkownika używana do połączenia z udziałem SMB.
* **Hasło** Odpowiadające hasło do uwierzytelniania SMB.
* **Adres URL serwera** Adres serwera SMB.
* **Port** Numer portu używany do dostępu do udziału SMB.
* **Folder** Ścieżka folderu w udziale SMB, gdzie dokumenty powinny być zapisywane (np. `/incoming/invoices/`). Musi istnieć i być zapisywalny.
*   **Plik mapowania JPL (opcjonalny)**

    Plik **JPL** służy do zdefiniowania transformacji danych eksportowanych przed zapisaniem ich do udziału SMB.

    * **Kiedy używać:** Tylko gdy dane dokumentu eksportowanego muszą być dostosowane do zewnętrznego formatowania lub oczekiwań systemowych.
    * **Pozostaw puste**, jeśli nie jest konieczna żadna transformacja.

</details>

#### **Infor IDM**

<details>

<summary>Infor IDM</summary>

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FQ1AtdmTRZr1sGkH6oLwP%252Fimage.png%3Falt%3Dmedia%26token%3D720a4184-3f91-4b70-b3da-b846f3cce030\&width=768\&dpr=4\&quality=100\&sign=dc678c2c\&sv=2)

#### **Opisy Pola**

* **Tytuł** Nazwa konfiguracji eksportu. Będzie widoczna na liście eksportu.
* **Pod-Organizacja** _(opcjonalne)_ Lista rozwijana z dostępnymi pod-organizacjami.
  * Jeśli pozostanie puste: dotyczy głównej organizacji.
  * Jeśli wybrane: eksport będzie dotyczył tylko wybranej pod-organizacji.
* **Typ Dokumentu** Lista rozwijana z dostępnymi typami dokumentów. Określa, do jakiego rodzaju dokumentu ma być zastosowana ta konfiguracja eksportu.
* **Plik Mapowania ION** Wybierz plik mapowania z menedżera plików.
* **Plik Mapowania IDM** Wybierz plik mapowania z menedżera plików. [Potrzebujesz pomocy przy tworzeniu? Zobacz Przewodnik po Mapowaniu IDM](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file)
* **Przełącznik Chmura / On-Prem** Przełącznik wskazujący typ wdrożenia Infor:
  * **Chmura**: Wybierz to, jeśli klient korzysta z Infor CloudSuite.
  * **On-Prem**: Wybierz to, jeśli Infor jest hostowany lokalnie.

</details>

#### **Infor ION**

<details>

<summary>Infor ION</summary>

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FcYDXwDYH4RSc5vcY4fmr%252Fimage.png%3Falt%3Dmedia%26token%3Da9cfac80-9795-4e8f-a664-e268c9b4856c\&width=768\&dpr=4\&quality=100\&sign=5a4b0bd0\&sv=2)

#### **Opisy pól**

* **Tytuł** Nazwa konfiguracji eksportu. Będzie widoczna na liście eksportu.
* **Pod-Organizacja** _(opcjonalne)_ Lista rozwijana z dostępnymi podorganizacjami.
  * Jeśli pozostanie puste: dotyczy głównej organizacji.
  * Jeśli wybrane: eksport będzie dotyczył tylko wybranej podorganizacji.
* **Typ Dokumentu** Lista rozwijana z dostępnymi typami dokumentów. Określa, do jakiego typu dokumentu ma być zastosowana ta konfiguracja eksportu.
* **Plik Mapowania ION** Wybierz plik mapowania z menedżera plików.
* **Plik Mapowania BOD** Wybierz plik mapowania z menedżera plików. [Potrzebujesz pomocy przy tworzeniu? Zobacz Przewodnik po Mapowaniu BOD](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file)
* **Przełącznik Chmura / Lokalnie** Przełącznik wskazujący typ wdrożenia Infor:
  * **Chmura**: Wybierz to, jeśli jesteś klientem Infor CloudSuite.
  * **Lokalnie**: Wybierz to, jeśli Infor jest hostowany samodzielnie.

</details>

#### Infor IDM + ION BOD

<details>

<summary>Infor IDM + ION BOD</summary>

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FY13EX2xxOKLZzliAAHB0%252Fimage.png%3Falt%3Dmedia%26token%3D94335922-6342-405f-8c6d-29fdf2f31a2e\&width=768\&dpr=4\&quality=100\&sign=c0322806\&sv=2)

#### **Opisy pól**

* **Tytuł** Nazwa konfiguracji eksportu. Będzie widoczna na liście eksportów.
* **Pod-Organizacja** _(opcjonalne)_ Lista rozwijana z dostępnymi pod-organizacjami.
  * Jeśli pozostanie puste: dotyczy głównej organizacji.
  * Jeśli wybrane: eksport będzie dotyczył tylko wybranej pod-organizacji.
* **Typ Dokumentu** Lista rozwijana z dostępnymi typami dokumentów. Określa, do jakiego typu dokumentu ma być zastosowana ta konfiguracja eksportu.
* **Plik Mapowania ION** Wybierz plik mapowania z menedżera plików.
* **Plik Mapowania IDM** Wybierz plik mapowania z menedżera plików. [Potrzebujesz pomocy przy tworzeniu? Zobacz Przewodnik po Mapowaniu IDM](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file)
* **Plik Mapowania BOD** Wybierz plik mapowania z menedżera plików. [Potrzebujesz pomocy przy tworzeniu? Zobacz Przewodnik po Mapowaniu BOD](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file)
* **Przełącznik Chmura / Lokalnie** Przełącznik wskazujący typ wdrożenia Infor:
  * **Chmura**: Wybierz to, jeśli klient korzysta z Infor CloudSuite.
  * **Lokalnie**: Wybierz to, jeśli Infor jest hostowany lokalnie.

</details>

### Dla klientów Infor CloudSuite

#### Infor IDM + LN

<details>

<summary>Infor IDM + LN</summary>

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F4SfGDqhA4KDrPfJ5vcsT%252Fimage.png%3Falt%3Dmedia%26token%3D4833c0dc-af8b-48a1-a977-6cc8ded20277\&width=768\&dpr=4\&quality=100\&sign=6301596\&sv=2)

#### **Opisy pól**

* **Tytuł** Nazwa konfiguracji eksportu. Będzie widoczna na liście eksportu.
* **Pod-Organizacja** _(opcjonalne)_ Lista rozwijana z dostępnymi pod-organizacjami.
  * Jeśli pozostanie puste: dotyczy głównej organizacji.
  * Jeśli wybrane: eksport będzie dotyczył tylko wybranej pod-organizacji.
* **Typ Dokumentu** Lista rozwijana z dostępnymi typami dokumentów. Określa, do jakiego rodzaju dokumentu ma być zastosowana ta konfiguracja eksportu.
* **Plik Mapowania ION** Wybierz plik mapowania z menedżera plików.
* **Plik Mapowania IDM** Wybierz plik mapowania z menedżera plików. [Potrzebujesz pomocy przy tworzeniu? Zobacz Przewodnik po Mapowaniu IDM](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file)
* **Plik Mapowania LN** Wybierz plik mapowania z menedżera plików. [Potrzebujesz pomocy przy tworzeniu? Zobacz Przykład Mapowania LN](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/ln/example-export-ln)

</details>

#### Infor IDM + M3

<details>

<summary>Infor IDM + M3</summary>

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FAN4T0aQEoogbUA8PUgy9%252Fimage.png%3Falt%3Dmedia%26token%3Da2b91153-858f-4711-abcc-4ed7ad60d49a\&width=768\&dpr=4\&quality=100\&sign=bb6bda83\&sv=2)

#### **Opisy pól**

* **Tytuł** Nazwa konfiguracji eksportu. Będzie widoczna na liście eksportu.
* **Pod-Organizacja** _(opcjonalne)_ Lista rozwijana z dostępnymi pod-organizacjami.
  * Jeśli pozostanie puste: dotyczy głównej organizacji.
  * Jeśli wybrane: eksport będzie dotyczył tylko wybranej pod-organizacji.
* **Typ Dokumentu** Lista rozwijana z wszystkimi dostępnymi typami dokumentów. Określa, do jakiego typu dokumentu ma być zastosowana ta konfiguracja eksportu.
* **Plik Mapowania ION** Wybierz plik mapowania z menedżera plików.
* **Plik Mapowania IDM** Wybierz plik mapowania z menedżera plików. [Potrzebujesz pomocy przy tworzeniu? Zobacz Przewodnik po Mapowaniu IDM](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file)
* **Plik Mapowania M3** Wybierz plik mapowania z menedżera plików. [Potrzebujesz pomocy przy tworzeniu? Zobacz Przykład Mapowania M3](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/m3/example-export-m3)

</details>

#### Infor IDM + M3 (toml)

<details>

<summary>Infor IDM + M3 (toml)</summary>

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FCdoduCkkbnomw3ahZgul%252Fimage.png%3Falt%3Dmedia%26token%3D4e5c7d08-5eaf-4c3e-9918-5cce58d8e3b3\&width=768\&dpr=4\&quality=100\&sign=e984c4e0\&sv=2)

#### **Opisy pól**

* **Tytuł** Nazwa konfiguracji eksportu. Będzie widoczna na liście eksportu.
* **Pod-Organizacja** _(opcjonalne)_ Lista rozwijana z dostępnymi pod-organizacjami.
  * Jeśli pozostanie puste: dotyczy głównej organizacji.
  * Jeśli wybrane: eksport będzie dotyczył tylko wybranej pod-organizacji.
* **Typ Dokumentu** Lista rozwijana z dostępnymi typami dokumentów. Określa, do jakiego rodzaju dokumentu ma być zastosowana ta konfiguracja eksportu.
* **Plik Mapowania ION** Wybierz plik mapowania z menedżera plików.
* **Plik Mapowania IDM** Wybierz plik mapowania z menedżera plików. [Potrzebna pomoc przy tworzeniu? Zobacz Przewodnik po Mapowaniu IDM](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file)
* **Plik Mapowania M3 toml** Wybierz plik mapowania z menedżera plików lub skorzystaj z opcji wyboru Toml, aby użyć toml utworzonego za pomocą menedżera reguł. [Potrzebna pomoc przy tworzeniu? Zobacz Przewodnik po Menadżerze Reguł](https://docs.docbits.com/administration-and-setup/settings/document-processing/rule-manager)

</details>
