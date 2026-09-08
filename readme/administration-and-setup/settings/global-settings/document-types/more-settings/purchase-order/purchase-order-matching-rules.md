# Pravila za usklađivanje porudžbenica

## Uvod: Porudžbenice i upravljanje PO pravilima

Usklađivanje porudžbenica (PO) je ključni proces za obezbeđivanje konzistentnosti između porudžbenica (PO) i odgovarajućih dolaznih faktura ili prijema robe. Robustan skup pravila je neophodan za postizanje visokog stepena automatskog usklađivanja, sprečavanje prevara i obezbeđivanje ispravnih uplata.

Ova stranica za konfiguraciju se koristi za definisanje i upravljanje pravilima koja određuju _kako_ se stavke porudžbenice usklađuju sa odgovarajućim dolaznim dokumentom (Faktura, Potvrda porudžbine).

{% hint style="info" %}
**Preduslov:** pravila za usklađivanje se koriste samo kada je **PO match server side** uključen za tip dokumenta (Podešavanja → Tipovi dokumenata → Više podešavanja → Porudžbenica). Kada je isključen, DocBits usklađuje sa svojim ugrađenim mehanizmom (količina, jedinicna cena, broj stavke, broj porudžbenice) i ignoriše skup pravila.
{% endhint %}

***

## Kako pristupiti

1.  Idite na **Podešavanja --> Globalna podešavanja --> Tipovi dokumenata**

    <figure><img src="../../../../../../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>


2.  Izaberite željeni tip dokumenta i kliknite na **Više podešavanja**.

    <figure><img src="../../../../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>


3.  Zatim idite u sekciju Porudžbenica i kliknite na dugme (PO match server side), a potom kliknite na Konfiguriši pravila za usklađivanje PO

    <figure><img src="../../../../../../.gitbook/assets/image (168).png" alt=""><figcaption></figcaption></figure>

***

<figure><img src="../../../../../../.gitbook/assets/Bildschirmfoto 2025-12-09 um 07.43.15.png" alt=""><figcaption></figcaption></figure>

## Globalna podešavanja (Osnovna pravila)

Ova podešavanja uspostavljaju okvir koji važi za sva pravila usklađivanja:

* **Podešavanje:** Uskladi količinu po
  * **Svrha:** Definiše koja se količina stavke porudžbenice upoređuje sa linijom dokumenta — na primer naručena količina ili **otvorena količina na fakturi** (naručeno minus već fakturisano), što je uobičajen izbor za fakture.
  * **Važeće vrednosti:** Količina ili druga dostupna polja količine u sistemu, u zavisnosti od strukture podataka (npr. alternativno normalizovano polje količine).
  * **Zavisnost:** Određuje osnovu za sva pravila usklađivanja koja uključuju količinu u svojim kriterijumima poređenja.
* **Podešavanje:** Standardna tolerancija (Podrazumevana tolerancija)
  * **Svrha:** Definiše koliko numerička vrednost na dokumentu može odstupati od vrednosti porudžbenice i još uvek se računati kao poklapanje. Kompenzuje razlike u zaokruživanju. Primjenjuje se na **svaki numerički stubac** sa uključenom opcijom "Dozvoli toleranciju" — količina kao i jedinicna cena.
  * **Važeća vrednost:** Decimalni broj. Da li se čita kao **apsolutna vrednost** (0.005 = odstupanje do 0.005 u upoređivanoj količini ili ceni) ili kao **procenat** (0.5 = 0.5 % upoređivane vrednosti) određuje se tipom tolerancije skupa pravila (`value` ili `percent`; novi skupovi pravila koriste `value`). Tolerancije po stavci (vidi [Podešavanja tolerancije](purchase-order-tolerance-settings-additional-purchase-order-tolerance.md)) nadjačavaju standardnu toleranciju za tu stavku.
  * **Zavisnost:** Primjenjuje se na pravila koja koriste numerička polja za usklađivanje i imaju uključenu opciju "Dozvoli toleranciju".

***

## Lista pravila

Lista pravila prikazuje sva dostupna pravila usklađivanja i upravlja njihovim redosledom izvršenja.

#### Struktura i izvršenje

* **Prioritet:** Ovo numeričko polje (npr. 1, 2, 3) određuje redosled izvršenja pravila. Pravila sa nižim brojem prioriteta se pokušavaju prvo. Ovo omogućava administratorima da strukturiraju hijerarhiju, obično počevši od najspecifičnijih i najstrožih pravila (npr. usklađivanje po broju linije i broju dela) i prelazeći na šira ili manje restriktivna pravila.
* **Naziv i opis:** Pruža jasnu identifikaciju i kontekst pravila, objašnjavajući primarne kriterijume koji se koriste (npr. "Standardno pravilo br. 1: Usklađivanje po broju linije, ID dela i količini").
* **Aktivno:** Jednostavan prekidač koji omogućava trenutno uključivanje ili isključivanje pravila bez potrebe za brisanjem njegove konfiguracije.

**Tok izvršenja:** Sistem vrši usklađivanje u kaskadnom nizu. Ako pravilo (npr. Prioritet 1) uspešno uskladi stavku, proces za tu stavku se zaustavlja. Ako nema poklapanja, sistem prelazi na sledeće pravilo u prioritetnom nizu (npr. Prioritet 2). Svako izvršenje se beleži na dokumentu; **istorija usklađivanja** na ekranu za usklađivanje porudžbenica prikazuje koje je pravilo pokušano, koje je uskladilo i koja su preskočena i zašto.

***

## Konfiguracija pravila (Detaljna podešavanja)

Ovaj detaljni deo konfiguracije definiše specifičnu logiku i kriterijume za pojedinačno pravilo.

#### Osnovni parametri

* **Tip pravila:** Specifikuje kardinalnost usklađivanja.

| Tip pravila          | Šta radi                                                                                                                                                                                             | Tipična upotreba                                                                |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| **Jedno usklađivanje** | Jedna linija porudžbenice sa jednom linijom dokumenta. Svaki konfigurisani stubac mora biti usklađen (u okviru tolerancije gde je dozvoljeno).                                                     | Standardni slučaj.                                                              |
| **Višestruko usklađivanje** | Više linija porudžbenice sa jednom linijom dokumenta, ili više linija dokumenta sa jednom linijom porudžbenice. Količine se **sabiraju**, jedinicna cena se poredi kao **prosek**, ostali stubci moraju biti usklađeni. | Podeljene isporuke, jedna linija fakture koja pokriva više linija porudžbine.   |
| **Usklađivanje po ukupnom iznosu** | Poredi jedan **iznos** — obično neto iznos linije dokumenta sa ukupnim iznosom porudžbenice — i usklađuje celu porudžbenicu odjednom.                                                        | Dobavljači koji fakturišu paušalno, servisne fakture, fakture sa jednom linijom.|

* **Automatsko usklađivanje:** Ako je omogućeno, sistem će pokušati da primeni ovo pravilo potpuno automatski. Potrebno je visoko poverenje u kriterijume za automatsku obradu.
* **Ručno usklađivanje:** Ako je omogućeno, ovo pravilo može biti prikazano ili primenjeno od strane korisnika tokom koraka ručne usklađenosti, nudeći im unapred definisan skup kriterijuma poređenja za rešavanje izuzetaka.
* **Rezervno pravilo:** Pravilo označeno kao rezervno se izvršava u kasnijoj fazi, samo za parove linija koji još nisu usklađeni nakon što su sva redovna pravila izvršena. Koristite ga za "labavije" pravilo koje treba da pokrije ono što su stroga pravila propustila.

#### Uslovi aktivacije

Pravilo može imati **uslove aktivacije** — izraze koji moraju biti tačni pre nego što se pravilo uopšte izvrši. Ako je uslov netačan, pravilo se **preskače za ovaj dokument** (istorija usklađivanja prikazuje ga kao "nije pokrenuto" sa razlogom). Izrazi koriste brojeve linija koje se usklađuju:

| Izraz                    | Značenje                                                            |
| ------------------------ | ------------------------------------------------------------------ |
| `[[count(po_lines)]]`    | broj linija porudžbenice dostupnih za usklađivanje                 |
| `[[count(table_lines)]]` | broj stavki na dokumentu koje su mapirane za usklađivanje          |

Uporedite ih sa `==`, `!=`, `>`, `>=`, `<`, `<=` i kombinujte više uslova sa `&` (i). Primeri:

* `([[count(po_lines)]] > 1) & ([[count(table_lines)]] > 1)` — samo za dokumente sa više linija sa obe strane (tipično za pravilo višestrukog usklađivanja).
* `([[count(po_lines)]] == 1) & ([[count(table_lines)]] == 1)` — samo za dokumente sa jednom linijom u odnosu na porudžbenicu sa jednom linijom.
* `([[count(po_lines)]] >= 1) & ([[count(table_lines)]] >= 1)` — kad god postoji nešto za usklađivanje.

{% hint style="warning" %}
Uslovi aktivacije su najčešći razlog zašto pravilo "ne radi ništa". Pravilo usklađivanja po ukupnom iznosu sa uslovom `[[count(table_lines)]] > 1` nikada se ne izvršava za fakturu sa jednom linijom — a [pravilo transformacije](../../transformation-rules.md) koje sabija fakturu u jednu ukupnu liniju proizvodi upravo takav dokument. Proverite brojeve u istoriji usklađivanja pre nego što menjate samo pravilo.
{% endhint %}

#### Poređenje kolona (Kriterijumi usklađivanja)

Ovo je osnovna definicija logike pravila, koja specificira koja polja moraju biti usklađena između dokumenata.

1. Definisanje kolona za poređenje:
   * **PO kolone:** Polje preuzeto iz podataka porudžbenice (npr. broj linije).
   * **Izvučene kolone tabele:** Odgovarajuće polje izvučeno ili parsirano iz dolaznog dokumenta (Faktura/Potvrda porudžbine) (npr. `POSITION`).
2. **Tip poređenja:** Definiše prirodu potrebnog poklapanja (npr. Tt za poređenje teksta/niza, zahtevajući tačno poklapanje karakter-po-karakter; # za numeričko poređenje).
3. **Dozvoli toleranciju:** Za numerička polja (količina, cena), aktiviranje ove opcije nalaže sistemu da primeni globalnu standardnu toleranciju definisanu ranije. Ako ovo _nije_ omogućeno za numeričko polje, vrednosti moraju biti tačno jednake.
4. **Ignoriši u ručnom usklađivanju:** Ako je čekirano, ovaj kriterijum se popušta tokom ručne intervencije. Korisno je za polja poput opisa ili internih referenci koje mogu malo varirati, omogućavajući korisniku da prevaziđe manje nebitne neusaglašenosti.

**Koje kolone se mogu porediti**

| Kolona                          | Strana dokumenta                         | Strana porudžbenice                     | Napomena                                                                                                                                                                                                                         |
| ------------------------------- | --------------------------------------- | -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Broj linije                     | `POSITION`                             | `line_number`                          | Tekst, tačno. Korisno samo ako dobavljač štampa brojeve linija porudžbenice na dokumentu.                                                                                                                                       |
| Identifikator stavke            | `ITEM_IDENTIFIER`                      | `item_identifier`                      | Tekst, tačno. Broj stavke ili broj stavke dobavljača, takođe preko [Mape brojeva stavki dobavljača](supplier-item-number-map-admin-documentation.md).                                                                           |
| Efektivna normalizovana količina | `QUANTITY_EFFECTIVE_NORMALIZED`        | `quantity_effective_normalized`        | Numeričko. Količina izabrana po **Match Quantity On**, konvertovana u istu jedinicu na obe strane (konverzija šifre jedinice, "po" količine).                                                                                   |
| Efektivna normalizovana jedinicna cena | `UNIT_PRICE_EFFECTIVE_NORMALIZED`      | `unit_price_effective_normalized`      | Numeričko. Jedinicna cena po jednoj jedinici nakon popusta i nakon **Unit Price Per** — i, ako je uključen [Izračunaj jedinicnu cenu PO](calculate-po-unit-price.md), cena izračunata iz iznosa i količine linije porudžbenice. |
| Neto iznos                     | `NET_AMOUNT`                           | `total_amount`                         | Numeričko. Koristi se kod pravila usklađivanja po ukupnom iznosu.                                                                                                                                                               |

**Primer: Strogo PO-pravilo usklađivanja (`DefaultRule#1`)**

Tipično strogo pravilo kombinuje obavezne provere identiteta sa proverama vrednosti:

* **Obavezni identitet:** Broj linije i identifikator stavke moraju se tačno poklapati (poređenje teksta, bez tolerancije).
* **Provere vrednosti:** Efektivna normalizovana količina i efektivna normalizovana jedinicna cena moraju se poklapati (numeričko poređenje, dozvoljena tolerancija). Samo ako su sva četiri kriterijuma ispunjena (sa tolerancijom za vrednosti) izvršava se automatsko usklađivanje.

***

## Podrazumevani skup pravila

Svaka organizacija počinje sa istim podrazumevanim skupom pravila. To je dobar referentni okvir kada pravite svoj skup:

| Pravilo                    | Tip / prioritet               | Poređene kolone                                                        | Uslov aktivacije                                      |
| -------------------------- | ----------------------------- | --------------------------------------------------------------------- | ----------------------------------------------------- |
| `DefaultRule#1`            | jedno usklađivanje, prioritet 1 | broj linije, identifikator stavke, količina (tol.), jedinicna cena (tol.) | uvek                                                  |
| `DefaultMultiMatchRules#1` | višestruko usklađivanje, prioritet 1, rezervno | identifikator stavke, količina (tol.), jedinicna cena (tol.)          | `count(po_lines) > 1` i `count(table_lines) > 1`      |
| `DefaultTotalMatchRules#1` | usklađivanje po ukupnom iznosu, prioritet 1 | neto iznos ↔ ukupno porudžbenice (bez tolerancije)                    | `count(po_lines) >= 1` i `count(table_lines) > 1`     |
| `DefaultRule#2`            | jedno usklađivanje, prioritet 2, rezervno | identifikator stavke, količina (tol.), jedinicna cena (tol.)          | uvek                                                  |
| `DefaultRule#3`            | jedno usklađivanje, prioritet 2, rezervno | količina (tol.), jedinicna cena (tol.)                                | `count(po_lines) == 1` i `count(table_lines) == 1`    |

Čitajući odozgo na dole: prvo strogo pravilo (broj linije i stavka moraju biti odštampani na dokumentu), zatim rezervna pravila bez broja linije, pa na kraju poslednja opcija za dokumente sa jednom linijom koja poredi samo količinu i cenu.

***

## Uticaj na proces usklađivanja PO

Definisani skup pravila direktno upravlja efikasnošću i integritetom procesa usklađivanja PO:

* **Prioriteti i rezervna pravila:** Definisani prioritet osigurava da sistem prvo pokušava najpouzdaniju metodu usklađivanja. Ako stroga pravila visokog prioriteta ne uspeju, sistem prelazi na šira pravila, nastojeći da minimizira broj izuzetaka koji se prosleđuju korisnicima.
* **Kontrola kvaliteta usklađivanja:** Stroža pravila (zahtevaju preciznije poklapanje i manju toleranciju) rezultiraju manjim brojem, ali veoma pouzdanih automatskih usklađivanja. Labavija pravila povećavaju stopu automatskog usklađivanja, ali povećavaju rizik od lažno pozitivnih rezultata.
* **Rukovanje izuzecima (ručno usklađivanje):** Omogućavanjem pravila za ručno usklađivanje, sistem pruža strukturirane opcije korisnicima. Ako transakcija ne prođe automatske kriterijume usklađivanja, postaje izuzetak. Korisnik tada može pokušati da reši izuzetak primenom unapred definisanog ručnog pravila, koje može imati opuštenije kriterijume (npr. ignorisanje manjeg neusaglašenosti teksta prema podešavanju "Ignoriši u ručnom usklađivanju").

## Šta još utiče na rezultat

* **Kada se usklađivanje pokreće:** tokom obrade dokumenta, kada korisnik klikne **Auto PO Match**, i **pri svakom čuvanju** u kojem se broj porudžbenice promenio ili nikada ranije nije tražen (na primer kada ga popune master podaci nakon obrade). Čuvanje nikada ne prepisuje već postojeće usklađivanje.
* **[Pravila transformacije](../../transformation-rules.md)** se izvršavaju pre usklađivanja i mogu menjati stavke linija — i sa njima brojeve linija koje uslovi aktivacije posmatraju. Pravilo tabele koje rekonstruiše linije zadržava postojeće usklađivanje dokle god linije ostaju iste; ako zameni usklađene linije, usklađivanje se briše i ime pravila se prikazuje kao razlog.
* **[Izračunaj jedinicnu cenu PO](calculate-po-unit-price.md)** menja koju jedinicnu cenu pravila poredi na strani porudžbenice.
* **[Podešavanja tolerancije](purchase-order-tolerance-settings-additional-purchase-order-tolerance.md)** i **[onemogućeni statusi](purchase-order-disable-statuses.md)** odlučuju koliko je poređenje strogo i koje linije porudžbenice se uopšte nude.

## Otklanjanje problema

| Simptom                                                         | Šta proveriti                                                                                                                                                                                     |
| ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| "Nema poklapanja" iako se svaka vrednost slaže                   | Otvorite istoriju usklađivanja: koje se pravilo izvršilo, na kom stubcu je neuspeh (odstupanje je prikazano po stubcu), da li je pravilo preskočeno uslovom aktivacije?                          |
| Jedinicna cena je usklađena za tačno poresku stopu               | Ukupna porudžbenica sadrži porez; uključite [Izračunaj jedinicnu cenu PO](calculate-po-unit-price.md) (prvo neto iznos) ili uporedite neto iznos linije.                                          |
| Pravilo usklađivanja po ukupnom iznosu se nikada ne izvršava     | Njegov uslov aktivacije zahteva više od jedne linije dokumenta. Postavite `[[count(table_lines)]] >= 1` ili ne sabijajte linije transformacionim pravilom.                                        |
| Skup pravila nema nikakav efekat                                 | **PO match server side** je isključen za tip dokumenta, ili je promenjeni skup pravila još uvek nacrt — aktivirajte verziju.                                                                     |

***

## Prilagođavanje pravila za usklađivanje PO

Da biste izmenili pravila za usklađivanje PO, podrazumevana verzija može biti klonirana klikom na **"Configure Versioning"** i korišćenjem opcije **"Clone as Draft"** iz dostupnih opcija kartice

<figure><img src="../../../../../../.gitbook/assets/image (197).png" alt=""><figcaption></figcaption></figure>