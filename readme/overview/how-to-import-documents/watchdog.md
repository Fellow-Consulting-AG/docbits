# Watchdog

**Wersja:**

Wersja 2.0.9 jest już dostępna. Proszę zaktualizować do nowej wersji: [https://github.com/Fellow-Consulting-AG/docbits/blob/main/WatchDog.exe](https://github.com/Fellow-Consulting-AG/docbits/blob/main/WatchDog.exe)

**Instalacja i ustawienia**

Po pobraniu pliku WatchDog.exe, wyszukaj Wiersz polecenia → Uruchom jako administrator na swoim urządzeniu z systemem Windows.

![](https://lh7-us.googleusercontent.com/a2kmyk7eD7HqZfPiLWmvSGFnpzg9oHejHe5TpE6gFwErFyJYYBB5BZjqopwr-cEqmlMvaW8-PgARZUGI9KMKHSkz-lU_C_w6aHrVA4Wqhwo8WBSqnBfVvCpSckqLu4PwUriGs1MxbKHBBkuQ2pPaVRM)

Po otwarciu, wywołaj plik, wpisując ścieżkę, gdzie plik WatchDog.exe jest przechowywany na Twoim urządzeniu, jak poniżej

![](https://lh7-us.googleusercontent.com/W_jDgPVTtpEW96jR0w_ibnZGY2CVwF2nAN0nEjMW3liw10bgPGlADiVR_lWyEAlfGYRD--gSQMdEqboRlMW5TAEP6Ao3GOW-hP3tQimA58K9Uh-WNZf7i06YYNqk5_EgKERYkjMzPx1Xd56qH2Pw8wA)

Wpisz install po ścieżce pliku i naciśnij ENTER na klawiaturze

![](https://lh7-us.googleusercontent.com/vZQxNIh_wY2SFTznxNTboFOSePmEMqXQMWbhsSoO45B_mIh_6C-yjfJ4SPleBIIV4p943XBN1E-3HJBgFXRRABVfDX9Ey-dnb9c5KYaNleOmE5x1ocK32zLQ4luc71rmcbv7V_dQ8pEtH_WoWZkN0fg)

Powinieneś otrzymać następujący komunikat o błędzie, ponieważ aplikacja uruchomi się w trybie UI, a konfiguracja nie jest jeszcze obecna.

![](https://lh7-us.googleusercontent.com/HmudHszeaiAj3xIlb1Oz1IXPh3Kz1JovUvPjkr9UI7EwSGbGWRK7xVhUNwc9LGlt3t1RRVR0l7DFLfG_Ob2b8Yxd4DffLb27Hv3z22tzf9LqDVTn577CFV-4Bzs2P_vTsGDJvtNzf8XW0wPiaWLDj2o)

Aplikacja automatycznie otworzy się po instalacji. Na górze, przejdź do Einstellungen (Ustawienia) i tutaj zobaczysz 2 oddzielne sekcje.

**Ustawienia folderów (Ordner Einstellungen)**

![](https://lh7-us.googleusercontent.com/8uSWIY8EJKPrKj9Zk5buY_ByE9fu2oE7mJ-shG1VB2n7QWyVLAfDfUFdj-Jv3hBq2ncf2Ls1Wh3Lm7Kf-TFqet7yFso2S6srnZev-yzVdKjUxtCMTt2IUtWvUwUU0LMGktA8ioBfIkkZGqG4f53yYHM)

Tutaj skonfigurujesz ścieżki plików, gdzie dokumenty będą odczytywane i przetwarzane. Ścieżka odczytu będzie dla dokumentów, które chcesz, aby WatchDog wyodrębnił i przetworzył, natomiast ścieżka przetwarzania będzie używana do wskazania, które dokumenty z folderu odczytu zostały wyodrębnione i przetworzone.

**Ustawienia ogólne (Allgemeine Einstellungen)**

![](https://lh7-us.googleusercontent.com/mTUxSXPBZi_TTtVEQbGQXyXNonkIuganpTjqaamkB7C7zZ7Qaodvf9Sl8nXjnp6ZpYNf8XOwvuk-MYYEyGkFcKB-SqC9lklBXehC-3jMI7G12tXqfa6ROWywPBFE4fy-p-DcuLo3QdZXy-1rjSzlu9s)

Tutaj skonfigurujesz swoją aplikację DocBits z WatchDog. Będziesz musiał wprowadzić swoje środowisko DocBits, klucz API i typ dokumentu (jak wskazano powyżej). Aby dodać więcej niż jeden typ dokumentu, oddziel nazwy typów dokumentów przecinkiem (INVOICE,DELIVERY-NOTE,PURCHASE-ORDER, itp.)

Jeśli wprowadzona zostanie nieprawidłowa konfiguracja dla któregokolwiek z pól, otrzymasz komunikat o błędzie jak poniżej.

![](https://lh7-us.googleusercontent.com/BIOMuVCPUojfwPVr-cJukzvoBdWdtxzj5XCXocWlZwbaXwkTpb4u5Gk84vKu-_Z5UxvZ2cq0asHs4aFRLklBrUOKA19d2R4nqsxyZjd3iJlh3y97f07OfzEyv6jl7JpnorANzdPIgyZfqwmCEYZOlek)

Po zakończeniu, wróć do obszaru Wiersza polecenia i ponownie uruchom plik WatchDog.exe, a tym razem zostanie on poprawnie zainstalowany dzięki obecnym konfiguracjom

![](https://lh7-us.googleusercontent.com/GqtwbyvQjjNb1u9DY_Eww2woOdK1nYMm0oRMFxEGWSP9oSYN51eu1kkWiDzenz1rHGLvYG-ocwosOK2bTM6ruXTI5co05kjV2HPGI-8TgEIBTVCPpTrvs37SKMk9eBWY0KEj9vCCyPeqXYgCVD0DDXw)

Aby uruchomić aplikację w trybie UI, uruchom następujące polecenie

![](https://lh7-us.googleusercontent.com/LELZuaiuL8ukiKPE-pbezsOZAICffXxAomx6gSe0vOvYaIdkr8Sr7X2znc_Lb3G76bh11X6kGPizWzoA05L-nBwUcJV8NNLUgQuGOf0TyICmhyL4syhnZFGu82JP0a3dORlQXz9MnTA_f-8b6oy8v6g)

Jeśli chcesz tylko uruchomić aplikację, zamiast tego uruchom to polecenie.

![](https://lh7-us.googleusercontent.com/yHiO-x4CPGIjC9hRx6o-Wr5lAYiwjGi0vNBp3faB91OYIqm8TTZcz3SVDgjSmq_7TN11aVCsNHoHV5sR0FHsA5DJqxJ74z3lAmXoaDkkMutl7yXj4fCoabX-9SwfsWJwOaooiVZhCvOKFXvJOCBicEA)

**Automatyczne uruchamianie**

Aby skonfigurować aplikację WatchDog w sposób, który pozwala na jej automatyczne uruchamianie po włączeniu systemu.

Po prostu otwórz „Usługi” w ustawieniach swojego urządzenia z systemem Windows.

![](https://lh7-us.googleusercontent.com/IEqq96LGZ9lBz2E0ApDrTz5huYutY7G1DecXLwhkdIF0pS235RN9HIqcehuJvXv5tyLdOnobhM_VNeMFA7tnMhwvWCnFRU5G14cHWN1swA4ZYF1rjvKzZtFMaCK2MDsPebvIz3MejDwjiYEiQ-_BQyg)

Wyszukaj WatchDog w lokalnych usługach i otwórz usługę (kliknij dwukrotnie na wpis)

![](https://lh7-us.googleusercontent.com/qOtVCqR-zytJw2zifnjHmW_s5Hl6ijJt72d3PRI_euZU0H3wA-QD69mSFOnyDEnCVJXblEeA_Zbh5iQsyPa8gPJ85TY8wz-Ir0aMd2SWoKizKw1G4yi9jOmtxZG7-9EZbOvborv45OASD6zSa6lLbAk)

W powyższym menu będziesz mieć następujące opcje automatycznego uruchamiania:

* Wybierz Automatyczny, usługa uruchomi się przy starcie
* Automatyczny (opóźniony start), usługa uruchomi się 2 minuty po starcie
