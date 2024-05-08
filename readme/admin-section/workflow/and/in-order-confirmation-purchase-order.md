# Potvrda Narudžbenice Kupovine

### Uporedite sa Narudžbenicom:&#x20;

**Potvrda Narudžbenice Kupovine**

<figure><img src="https://lh7-us.googleusercontent.com/glQHETatKah-1YugeLqBb7Jim6lNJxuarRv-KEMv4NPzFfcjSm6mVhTMdI30nxdJ0SHXZ55Oup6KH7K-J6IxjUOiG0wxUX8toAaCopgBJwPyr94CPjoKuauNTmoHGGhg6f3gwHD39W7gpvijg4LQVJ4" alt="" width="563"><figcaption></figcaption></figure>

#### Logička Kartica: Podudarnost Količine, Cene po Jedinici ili Popusta

Ova logička kartica je dizajnirana da automatski proveri da li se količina, cena po jedinici ili popust detaljni u potvrdi narudžbenice podudaraju sa odgovarajućim ciframa u narudžbenici. Ova verifikacija osigurava doslednost i tačnost između onoga što je naručeno i onoga što dobavljač potvrđuje da će isporučiti.

#### Uslov Okidača

Logika se aktivira kada se ispune bilo koji od sledećih uslova u potvrdi narudžbenice u odnosu na originalnu narudžbenicu:

* **Količina**: Količina naručenih artikala se podudara sa količinom potvrđenom od strane dobavljača.
* **Cena po Jedinici**: Cena po artiklu dogovorena se podudara sa potvrdom dobavljača.
* **Popust**: Svi primenjeni popusti su dosledni između narudžbenice i potvrde narudžbenice.

#### Ishodi

* **Jednako**: Ako se količina, cena po jedinici ili popust u potvrdi narudžbenice tačno podudaraju sa narudžbenicom, sistem smatra potvrdu validnom i nastavlja sa sledećim koracima u procesu nabavke.
* **Nije Jednako**: Ako postoji neslaganje u količini, ceni po jedinici ili popustu, sistem označava potvrdu narudžbenice za ručni pregled. Ovo osigurava da se sva neslaganja reše pre nastavka.

#### Beneficije

* **Tačnost i Doslednost**: Održava tačnost u procesu nabavke, osiguravajući da se plaćanja i isporuke vrše na osnovu tačnih cifara.
* **Efikasnost**: Automatizuje proces verifikacije, smanjujući potrebu za ručnim proverama i ubrzavajući obradu narudžbi.
* **Kontrola Troškova**: Pomaže u sprečavanju preplaćivanja ili neispravnih isporuka hvatanjem neslaganja na početku procesa.

<figure><img src="https://lh7-us.googleusercontent.com/DRTMJxJ9XLeC5zWSU8QuZwPLkqHzmCUm9RwiUZIkcc8pVxMZsxLv56dX9spzqr7KeDkTigbeBX2DvAZRe-6MdqOgAnrO-QPnCbi4e6hP4--P_O0A0DSoQJxjGeefOS1p6GuXHs1YXv-A73DXYaE8qlI" alt="" width="563"><figcaption></figcaption></figure>

1. **Definišite Parametre Uporedjivanja**: Postavite specifična polja (količina, cena po jedinici, popust) koje će logička kartica proveriti da li se podudaraju.
2. **Automatizujte Verifikaciju**: Konfigurišite sistem da automatski uporedi ove detalje po prijemu potvrde narudžbenice.
3. **Prilagodite Upozorenja**: Odlučite o toku rada za rukovanje neslaganjima, uključujući prilagođavanje upozorenja za ručni pregled.

Ova logička kartica je od vitalnog značaja za osiguravanje da se detalji potvrde narudžbenice podudaraju sa originalnom narudžbenicom, čuvajući integritet ciklusa nabavke. \`\`
