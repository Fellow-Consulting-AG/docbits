# Polja

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 09.02.31.png" alt=""><figcaption></figcaption></figure>

#### Pregled

Postavka Polja pruža korisnički interfejs gde administratori mogu upravljati svojstvima i ponašanjem pojedinačnih podataka polja povezanih sa tipom dokumenta. Svako polje može biti prilagođeno radi optimizacije tačnosti i efikasnosti prikupljanja i validacije podataka.

#### Ključne funkcije i opcije

1. **Konfiguracija Polja**:
* **Imena Polja**: Navodi imena polja, obično odgovarajući podacima unutar dokumenta, poput "Broj Fakture" ili "Datum Narudžbenice".
* **Obavezno**: Administratori mogu označiti polja kao obavezna, obezbeđujući da podaci moraju biti uneti ili prikupljeni za ta polja kako bi se završila obrada dokumenta.
* **Samo za čitanje**: Polja mogu biti postavljena kao samo za čitanje kako bi se sprečila izmena nakon prikupljanja podataka ili tokom određenih faza obrade dokumenata.
* **Sakriveno**: Polja mogu biti sakrivena iz prikaza u korisničkom interfejsu, korisno za osetljive informacije ili za pojednostavljenje korisničkih radnih tokova.
2. **Napredne postavke**:
* **Prisilna Validacija**: Osigurava da podaci uneti u polje prođu određena pravila validacije pre nego što budu prihvaćeni.
* **OCR (Optičko prepoznavanje karaktera)**: Ovaj prekidač može biti uključen kako bi se omogućila OCR obrada za određeno polje, korisno za automatizovano izvlačenje podataka iz skeniranih ili digitalnih dokumenata.
* **Rezultat Podudaranja**: Administratori mogu definisati rezultat podudaranja, prag koji se koristi za određivanje nivoa poverenja prepoznavanja ili podudaranja podataka, utičući na to kako se vrše validacija podataka i provere kvaliteta.
3. **Dugmad za Akcije**:
* **Kreiraj Novo Polje**: Omogućava dodavanje novih polja tipu dokumenta.
* **Ikone za Uređivanje**: Svako polje ima ikonu za uređivanje koja omogućava administratorima dalje konfigurisanje postavki specifičnih za polje, poput tipa podataka, podrazumevanih vrednosti ili povezane poslovne logike.
* **Sačuvaj Postavke**: Potvrđuje promene napravljene u konfiguracijama polja.

{% @jira/embed url="https://fellowpro.atlassian.net/browse/DOCB-2494" %}
