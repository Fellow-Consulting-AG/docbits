# Pravila transformacije

## Pregled

Pravila transformacije automatski čiste ili prepravljaju izvučene podatke — polje u zaglavlju, kolonu u tabeli, cele redove tabele ili atribut dokumenta — svaki put kada se dokument obrađuje i svaki put kada se čuva. Ona zamenjuju male skripte koje su mnoge organizacije pisale za "uvek skini praznine sa ovog polja", "podrazumevano postavi ovu kolonu na 1", "mapiraj kodove jedinica ovog dobavljača" ili "svedi stavke ovog dobavljača u jedan ukupni red".

Pravilo se definiše po **tipu dokumenta** i izvršava se na svakom dokumentu tog tipa. Pravila se izvršavaju **pre** validacije, skripti i usklađivanja porudžbina, tako da sve dalje već vidi transformisane vrednosti.

## Kako pristupiti

1. Idite na **Settings → Global Settings → Document Types**.
2. Otvorite tip dokumenta i izaberite **Transformation Rules**. Lista prikazuje svako pravilo tog tipa sa njegovim opsegom, ciljem, prioritetom i da li je aktivno.
3. Kliknite na **New rule** da otvorite kreator pravila, ili otvorite postojeće pravilo da ga izmenite.

## Anatomija pravila

| Deo               | Šta je to                                                                                                                                                                                                                      |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Ime / ključ**   | Prikazno ime koje se vidi na listama, u porukama i istoriji usklađivanja, i tehnički ključ koji ostaje stabilan kada preimenujete pravilo.                                                                                      |
| **Opseg**         | Gde pravilo upisuje: **polje zaglavlja**, **kolonu tabele**, **tabelu** (cele redove) ili **atribut dokumenta**. Pogledajte dole.                                                                                              |
| **Cilj**          | Polje, kolona (sa svojom tabelom) ili tabela u koju pravilo upisuje.                                                                                                                                                           |
| **Izvor**         | Opcionalno. Odakle pravilo čita ulaz umesto samog cilja: `header.<field>` za polje zaglavlja, `doc.<attribute>` za atribut dokumenta, `row.<column>` za drugu kolonu istog reda (samo za opseg kolone).                         |
| **Kada**          | **Uvek**, ili **samo kada** je uslov tačan (vidi Uslove).                                                                                                                                                                    |
| **Akcije**        | Lista transformacija, primenjenih redom; izlaz jedne akcije je ulaz za sledeću.                                                                                                                                               |
| **Prioritet**     | Pravila istog opsega se izvršavaju po rastućem prioritetu (zatim po ključu). Koristite ga kada jedno pravilo mora da vidi rezultat drugog.                                                                                   |
| **Izvrši jednom** | Pravilo se primenjuje na dokument **najviše jednom**. Potrebno za akcije koje bi menjale vrednost ponovo pri svakom čuvanju (substring, regex_replace, regex_extract) i za pravila tabele koja ne bi smela ponovo da prave redove. |
| **Zabeleži izvršenje** | Upisuje jedan log red po primeni — korisno dok podešavate novo pravilo.                                                                                                                                                      |

### Opsezi

| Opseg                 | Upisuje u                                               | Tipično pravilo                                                                                  |
| --------------------- | ------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| **Polje zaglavlja**   | jedno izvučeno polje zaglavlja (broj fakture, valuta, …) | skini praznine i pretvori broj fakture u velika slova; mapiraj "EUR€" u "EUR"                    |
| **Kolona tabele**     | jednu kolonu u svakom redu tabele                        | podrazumevano `UNIT_PRICE_PER` na 1; ukloni prefiks "Art.-Nr." iz broja artikla                  |
| **Tabela**            | redove tabele                                           | očisti redove i dodaj jedan ukupni red za dobavljača koji je usklađen po ukupnom iznosu          |
| **Atribut dokumenta** | atribut samog dokumenta (trenutno podorganizacija)      | usmeri dokumente dobavljača ka podorganizaciji                                                  |

Pravila se izvršavaju po opsegu u ovom redosledu: zaglavlje → dokument → tabela → kolona. Pravilo kolone zato već vidi redove koje je dodalo pravilo tabele.

### Uslovi ("samo kada")

Uslov poredi vrednost dokumenta sa konstantom. Vrednost dolazi iz polja zaglavlja (`header.<field>`), atributa dokumenta (`doc.<attribute>`) ili, za pravila kolone, iz kolone trenutnog reda (`row.<column>`).

| Operator                          | Značenje                                  |
| -------------------------------- | ----------------------------------------- |
| is / is not                      | tačno poređenje                           |
| is one of / is not one of        | vrednost u listi                         |
| contains, starts with, ends with | poređenje teksta                         |
| is empty / is not empty          | nije potrebna vrednost                   |
| greater than, less than, at least, at most | numeričko poređenje             |
| matches                         | regularni izraz                          |

Uslovi se mogu grupisati sa **all of** (i) i **any of** (ili) i negirati sa **not**. Primer: _samo kada je `header.supplier_id` `20723`_ — pravilo se izvršava samo za jednog dobavljača.

### Akcije

Akcije za polja zaglavlja i kolone tabele (one formiraju pipeline; vrednost ulazi na vrhu i izlazi na dnu):

| Akcija             | Efekat                                                                                                              |
| ------------------ | ------------------------------------------------------------------------------------------------------------------- |
| `trim`             | ukloni praznine (ili zadate karaktere) sa leve, desne ili obe strane                                              |
| `case`             | velika slova, mala slova, naslovna slova ili kapitalizacija                                                        |
| `pad`              | dopuni do dužine sa karakterom, sa leve ili desne strane                                                            |
| `truncate`         | skraćivanje na maksimalnu dužinu                                                                                   |
| `affix`            | dodaj prefiks ili sufiks, ili ukloni jedan                                                                          |
| `sanitize`         | zadrži samo određenu klasu karaktera (alfa-numeričke, alfa, numeričke, alfa-numeričke + razmak) ili ukloni skup karaktera |
| `substring`        | uzmi deo vrednosti po početku i dužini ili kraju                                                                    |
| `regex_replace`    | zameni ono što regularni izraz poklapa                                                                              |
| `regex_extract`    | zadrži ono što regularni izraz hvata                                                                                 |
| `value_map`        | mapiraj vrednosti na druge vrednosti (opciono bez obzira na velika/mala slova, sa podrazumevanom vrednošću)          |
| `date_format`      | promeni format datuma (ulaz mora biti ISO datum koji DocBits čuva u `value`)                                        |
| `number_format`    | promeni format broja                                                                                                |
| `default`          | postavi vrednost samo kada je polje prazno                                                                           |
| `set_value`        | postavi fiksnu vrednost, bez obzira šta je polje sadržavalo                                                        |
| `clear`            | isprazni polje                                                                                                      |

Akcije za opseg **tabele** (rade na redovima, ne na vrednostima, i ne mogu se mešati sa gore navedenim akcijama):

| Akcija       | Efekat                                                                                                                             |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| `clear_rows` | izbriši svaki red tabele                                                                                                           |
| `add_row`    | dodaj jedan red na kraj ili početak; svaka kolona dobija ili fiksnu vrednost ili vrednost pročitanu iz zaglavlja (`header.<field>`) ili dokumenta (`doc.<attribute>`) |

{% hint style="info" %}
`substring`, `regex_replace` i `regex_extract` menjaju vrednost ponovo kada se izvršavaju na već transformisanoj vrednosti. Kombinujte ih sa **Izvrši jednom**, ili napišite regularni izraz tako da drugi prolaz nema šta da menja.
{% endhint %}

## Kada se pravila izvršavaju

* Tokom obrade, nakon ekstrakcije i pre validacije, skripti i usklađivanja porudžbina.
* Na **svakom čuvanju** dokumenta u kome su izvučeni podaci promenjeni. Pravila bez **Izvrši jednom** se ponovo primenjuju pri svakom čuvanju; pošto je svaka akcija osim tri gore navedene idempotentna, vrednost koja je već u ciljnom obliku ostaje nepromenjena.

## Pravila transformacije i usklađivanje porudžbina

Pravila tabele i kolone menjaju ono što PO matcher vidi:

* Pravilo tabele koje **ponovo gradi** redove (na primer, očisti sve redove i dodaj jedan ukupni red) zadržava postojeće usklađivanje porudžbine sve dok proizvodi **iste redove ponovo** — vrednosti se porede po značenju, tako da su `1.0` i `1.00` isti red. Redovi zadržavaju svoj identitet i usklađivanje preživljava svako čuvanje.
* Ako pravilo **zamenjuje ili uklanja redove koji su bili usklađeni**, usklađivanje se ne može sačuvati. Dokument tada beleži koje pravilo ga je uklonilo, ekran za usklađivanje porudžbina prikazuje razlog ("_Usklađivanje PO nije moglo biti sačuvano: pravilo transformacije "…" je ponovo izgradilo tabelu_") i administratori dobijaju link ka pravilu. **Istorija usklađivanja** dokumenta prikazuje korak _Transformation rules_ pre prve faze usklađivanja sa pravilima koja su se izvršila.
* Broj redova nakon pravila je ono što [uslovi aktivacije](more-settings/purchase-order/purchase-order-matching-rules.md#activation-conditions) pravila usklađivanja broje. Pravilo koje svede fakturu na **jedan** red ima smisla samo zajedno sa pravilom za usklađivanje po ukupnom iznosu koje je aktivno za dokumente sa jednim redom (`[[count(table_lines)]] >= 1`).

## Primeri

**Očisti broj fakture** — polje zaglavlja `invoice_id`, uvek: `trim` → `case` upper.

**Podrazumevano postavi osnovu cene** — kolona tabele `UNIT_PRICE_PER` u tabeli stavki, uvek: `default` `1`.

**Mapiraj kodove jedinica dobavljača** — kolona tabele `UNIT` u tabeli stavki, samo kada je `header.supplier_id` `10040`: `value_map` `{ "STK": "PCE", "KG": "KGM" }`.

**Jedan ukupni red za dobavljača koji je usklađen po ukupnom iznosu** — opseg tabele na tabeli stavki, samo kada je `header.supplier_id` `20723`: `clear_rows`, zatim `add_row` sa `POSITION` = `001`, `UNIT_PRICE` = `1.0`, `QUANTITY` = `header.total_net_amount`, `NET_AMOUNT` = `header.total_net_amount`. Uparite ga sa pravilom za usklađivanje po ukupnom iznosu čiji uslov aktivacije prihvata dokument sa jednim redom.

**Usmeri dobavljača ka podorganizaciji** — atribut dokumenta `sub_org_id`, samo kada je `header.supplier_id` jedan od `[…]`: `set_value` `<id podorganizacije>`.

## Otklanjanje problema

| Simptom                                                   | Šta proveriti                                                                                                                                                                             |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Pravilo nije ništa promenilo                              | Da li je aktivno? Da li se tip dokumenta poklapa? Da li je uslov tačan za ovaj dokument (uporedite tačnu vrednost, uključujući razmake)? Da li je pravilo sa **Izvrši jednom** već primenjeno? |
| Vrednost se menja ponovo pri svakom čuvanju              | Pipeline sadrži `substring`, `regex_replace` ili `regex_extract`. Uključite **Izvrši jednom** ili učinite izraz idempotentnim.                                                               |
| Usklađivanje porudžbine se gubi nakon čuvanja            | Pravilo tabele je zamenilo usklađene redove. Razlog u dokumentu navodi pravilo; podesite pravilo da reprodukuje iste redove, ili ga postavite na **Izvrši jednom**.                          |
| Pravilo za usklađivanje se nikada ne izvršava nakon transformacije | Pravilo je promenilo broj redova; prilagodite uslov aktivacije pravila za usklađivanje.                                                                                                   |