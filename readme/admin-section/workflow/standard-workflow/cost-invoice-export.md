# Faktura kosztowa - Eksport

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-05-03 um 14.53.28.png" alt=""><figcaption></figcaption></figure>

Ten tytuł wskazuje, że reguła jest specjalnie skonfigurowana do zarządzania fakturami kosztowymi i obejmuje akcję eksportu, być może w celu raportowania, dalszej obróbki lub integracji z innymi systemami.

#### Konfiguracja reguły:

1. **Kiedy…**
* **Typ dokumentu to Faktura**: Ta warunek zapewnia, że reguła jest uruchamiana tylko dla dokumentów sklasyfikowanych jako faktury, zachowując specyficzność przepływu pracy dotyczącego zarządzania fakturami.
2. **I…**
* **Podtyp faktury to Faktura kosztowa**: To określa, że reguła dotyczy tylko tych faktur, które są wyraźnie oznaczone jako "Faktury kosztowe" w określonym polu w dokumencie. Pomaga to odróżnić je od innych typów faktur.
* **Status dokumentu to Oczekuje na drugie zatwierdzenie**: Faktura musi znajdować się w statusie "Oczekuje na drugie zatwierdzenie". Oznacza to, że faktura już przeszła pierwsze zatwierdzenie i oczekuje na drugie, być może ostateczne, sprawdzenie.

#### Akcja (Wtedy…):

* **Rozpocznij eksport**: Gdy faktura spełnia określone warunki (jest fakturą kosztową i oczekuje na drugie zatwierdzenie), wykonywana jest akcja "Rozpocznij eksport". Może to obejmować przesłanie danych faktury do innego systemu w celu analizy finansowej, raportowania lub celów związanych z zgodnością.

#### Cel tej reguły:

* **Efektywność przepływu pracy**: Ta reguła pomaga zautomatyzować obsługę faktur kosztowych, zapewniając ich przetwarzanie przez niezbędne etapy zatwierdzenia bez ingerencji manualnej, zwiększając szybkość i dokładność operacji finansowych.
* **Kontrola i zgodność**: Wymagając drugiego zatwierdzenia, system narzuca mechanizm kontroli, który zapewnia, że faktury kosztowe są dokładnie sprawdzane, zwiększając nadzór finansowy.
* **Integracja i raportowanie**: Akcja eksportu sugeruje, że po pełnym zatwierdzeniu faktury mogą być zintegrowane z innymi systemami do dalszej obróbki lub analizy, co jest kluczowe dla raportowania finansowego i audytów.

Ten rodzaj reguły jest istotny dla organizacji zajmujących się różnymi rodzajami faktur i potrzebujących zapewnić, że każdy rodzaj jest obsługiwany zgodnie z określonymi protokołami. Zmniejsza ryzyko błędów i zapewnia zgodność z wewnętrznymi kontrolami i zewnętrznymi przepisami.
