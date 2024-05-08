# Polja

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 09.02.31.png" alt=""><figcaption></figcaption></figure>

#### Pregled

Postavka Polja pruža korisnički interfejs gde administratori mogu upravljati svojstvima i ponašanjem pojedinačnih podataka polja povezanih sa tipom dokumenta. Svako polje može biti prilagođeno radi optimizacije tačnosti i efikasnosti prikupljanja i validacije podataka.

#### Ključne funkcije i opcije

1. **Konfiguracija polja**:
* **Imena polja**: Navodi imena polja, obično odgovarajući elementima podataka unutar dokumenta, poput "Broj fakture" ili "Datum porudžbine".
* **Obavezno**: Administratori mogu označiti polja kao obavezna, obezbeđujući da podaci moraju biti uneti ili prikupljeni za ta polja kako bi se završila obrada dokumenta.
* **Samo za čitanje**: Polja mogu biti postavljena kao samo za čitanje kako bi se sprečila izmena nakon prikupljanja podataka ili tokom određenih faza obrade dokumenata.
* **Sakriveno**: Polja mogu biti sakrivena iz prikaza u korisničkom interfejsu, korisno za osetljive informacije ili za pojednostavljanje korisničkih radnih tokova.
2. **Napredne postavke**:
* **Prisilna validacija**: Osigurava da podaci uneti u polje prođu određena pravila validacije pre nego što budu prihvaćeni.
* **OCR (Optičko prepoznavanje karaktera)**: Ovaj prekidač može biti uključen kako bi se omogućila OCR obrada za određeno polje, korisno za automatizovano izvlačenje podataka sa skeniranih ili digitalnih dokumenata.
* **Rezultat podudaranja**: Administratori mogu definisati rezultat podudaranja, prag koji se koristi za određivanje nivoa poverenja prepoznavanja ili podudaranja podataka, što utiče na to kako se vrše validacija podataka i provere kvaliteta.
3. **Dugmad za akcije**:
* **Kreiraj novo polje**: Omogućava dodavanje novih polja tipu dokumenta.
* **Ikone za uređivanje**: Svako polje ima ikonu za uređivanje koja omogućava administratorima dalje konfigurisanje specifičnih postavki polja, poput tipa podataka, podrazumevanih vrednosti ili povezane poslovne logike.
* **Sačuvaj postavke**: Potvrđuje promene napravljene u konfiguracijama polja.

{% @jira/embed url="https://fellowpro.atlassian.net/browse/DOCB-2494" %}
