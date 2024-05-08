# Postman za DocBits

Ovaj vodič će vam pokazati kako da napravite HTTP zahteve ka vašoj DocBits organizaciji putem Postmana. Veoma je jednostavno za korišćenje i veoma korisno za administratore organizacije.

## Postavka

Prvo, preuzmite Postman na svoj sistem i prijavite se/registrujte.

Sada pratite ovaj vodič korak po korak da biste naučili kako HTTP zahtevi funkcionišu u Postmanu.

Autorizacija u Postmanu

Pre nego što možete kreirati svoje HTTP zahteve, morate uneti svoj API ključ iz DocBits-a da biste ih autorizovali.

* Kliknite na karticu \`Authorization\` i izaberite \`API Key\` kao tip autorizacije.

![](https://lh7-us.googleusercontent.com/L3GaBZJvReeINaKbkq3VYQ9UHTBoKUA3nJkfyLqk61q5xaOJnmMLhbrEbgUgLEyYRkewHuLIAVzoYCZ6quHq0pwx\_69FEYJjzYllivB8WzdAtTFSrzl8VeFthbMsEB9sGjcGlVN38DXEXUwuNEPL6hg)

* Popunite vrednosti. Unesite “X-API-key” u polje \`Key\` i vaš API ključ kao vrednost (pronađite ga u meniju Podešavanja DocBits-a pod Integracija) Izaberite Dodaj u \`Header\`.

&#x20;

* Trebalo bi da izgleda ovako:

![](https://lh7-us.googleusercontent.com/SmNfci4z8ECTeXzFPE9YQ8nCzCRHglc\_7RR1cN8a8F7KvYWjJcBnY5wpl7q0AV8bfNLkMk8F4F4aw8j4xMK50HJweBRBPo8EasTn-FG-fmlUJQ41aUX-dvTeWP\_xJQThi8A6EwJl3qIc-Dw1B5W9fVE)

### DocBits API

Dostupno na https://api.polydocs.io

* Kliknite na Authorize u gornjem desnom uglu

![](https://lh7-us.googleusercontent.com/kuztHpkmRWlOYSU27r97KH15SJHPF\_hn\_eX3C1DYLVYCwMHXfLjYSyFubUCvlQiBt5q3xY0XBPmkcP6AnKF2C0Mdtx3tg\_dU\_qxqAmI6axYIsXR36\_YBz6j455K3-c2SBu4YzmYIXq8VXQxzgL-0j90)

* Unesite svoj API ključ i potvrdite klikom na \`Authorize\`

![](https://lh7-us.googleusercontent.com/zLhgpdjMnxqNBdjgtDxFEKglICIZul7dgmfFFm2hSnsDQ-HsZHRKRikZ0lcanGYkkZj4waC85mEUFO951ydVnY\_\_m\_TrMrsK3vrDv9FKL-adgWL4lJqp3cSxPeClBm9IHG2cXinRsv12xTeh3psQfO4)

### Kreiranje novog Workspace-a u Postmanu

* Kliknite na Workspace i kreirajte novi workspace (možete ga nazvati kako god želite)

![](https://lh7-us.googleusercontent.com/3rZw7jhOgVpkZuer58fPEKqDspJjK3S1lp3XpQuvE4c9212a0ALB-p7oLRwPqEbj10MpoCWsb7V9fPqiAdVvigE00x9mN5-lHFXZVVxlkeroBJd2ratgkJVJDM4LJkUJsycyl6tnFKazcFPY-vWtH2Q)

* Morate izabrati vidljivost koja određuje ko može pristupiti ovom workspace-u.

![](https://lh7-us.googleusercontent.com/ZajvDtMvfM5J\_Go3n\_PgzD3RXTMQAlST8\_3WnsTQ4-iw7e0QdAa3wqFk7Y0gt78IJVjNTN-5E72c1127CpXJWb8WbfDolxENLqxg5VZLPEK7-hxsNwbAyMceSHfeVy6v-b9QT0kFwnMibWndEAJ2lXA)

* Nakon što napravite svoj izbor i kliknete na \`Create Workspace\` izaberite Collections sa leve strane aplikacije i kreirajte novu kolekciju za vaše HTTP zahteve klikom na \`+\`.

![](https://lh7-us.googleusercontent.com/mbC5t86vaB2G7FQp-40XN-SHc019LKitfUeXRzbcG4HpNai5FPapShx9swHX3mz0va8QFsUQiYn-bhjvER0XYOEDRJpI9x3wG4NgRZCd4beU1NyKJd86bSGubxVbRCtz8HkTDZd28Z7Ice3rmscFMMo)

U ovoj kolekciji možete dodati više HTTP zahteva. Da biste to uradili, kliknite na 3 tačke kolekcije i izaberite \`Add request\`.

![](https://lh7-us.googleusercontent.com/S5W75clJz7JqoIWPbKBjrJqpTAwjS51Pu4dTU160Q7i6oW-HPnb7aN8WRK2AyAb6-HEqTYMZTy9563P0sq53MAjGpVg1JivZX2ATHa6GeFbTX2UCjud7ot8Y\_ksBuUbUfyEfxIDziV8TN3zDfX9Se58)

## Primer metode "GET"

GET metoda je veoma korisna za dobijanje informacija o korisnicima, podorganizacijama, obrađenim dokumentima i mnogo više.

* Izaberite GET metodu u vašem HTTP zahtevu.
* Autorizujte se kao što je opisano iznad.
* Otvorite https://api.polydocs.io i dodajte putanju funkcije iza URL-a Polydocs-a. Na primer:

![](https://lh7-us.googleusercontent.com/pIdgyqP7g1UwZbY5yaz1KAnKe\_ESs\_kQyiWAXXM-ukRKakS\_\_OL\_LS9J-07hZnZDf8QqtoN\_lKyuhvOIIIF-4Wp0dkofZYQwXZ0hu2RM0YogRxJah-zf8W\_cDNFf8xsec1tYIsfe0SpBuvdCG4WHMU0)

* Sada zalepite ovaj link u polje pored GET metode u Postmanu.

Kliknite na \`Send\` i trebalo bi da dobijete sve informacije o svakom korisniku u vašoj organizaciji.

## Primer metode "POST"

POST metoda se obično koristi za kreiranje korisnika ili organizacija, na primer. Ova metoda ubacuje informacije u bazu podataka.

Kreirajte korisnika

* Izaberite POST metodu.
* Autorizujte se kao što je opisano iznad.
* Otvorite https://api.polydocs.io i dodajte putanju funkcije iza URL-a Polydocs-a. U ovom slučaju:

![](https://lh7-us.googleusercontent.com/Gwabl4pN0k0NanHsFOzJj9s2H7ExS-JcWr-Y4EW0FLUYHfnaOZoMWvldJ6yDI33p\_DThVx0Rd5bi59XdOK11l1knc5rd-E5HXMw6v5E3qvHvKVWHlp21S728SVye6KU2W5ZeXtCIOzxBAcMlA2UNFfQ)

* Sada zalepite ovaj link u polje pored POST metode u Postmanu.
* Izaberite karticu \`Body\` u vašem HTTP zahtevu i unesite ključeve i vrednosti za svaku akreditaciju koja ima crvenu zvezdicu pored svog imena.

Kada završite, trebalo bi da izgleda ovako:

![](https://lh7-us.googleusercontent.com/lSExzZSbTcSRvuLDw0HNYE62yI7xs0eUewKuOcABCGYfsRBRbGz1lJxopR4QdUEoniCnZ83FKpz-AHLORP5cXGPrPhgouzE6zO920jA7A3r-Y14wY\_Gc3C98R2fcxXsWRMcle9qT981YWhCnjlUukPE)

Ako želite da kreirate administratorski nalog, postavite vrednost \`is\_admin\` na true.

&#x20;Na kraju, kliknite na \`Send\` i možete videti sve akreditacije koje ste postavili u odgovoru ispod. To znači da je korisnik kreiran.
### Postavljanje Dokumenta

Takođe možete koristiti POST metodu za postavljanje dokumenta na DocBits.

* Izaberite POST Metodu.
* Autorizujte se kao što je opisano iznad.
* Otvorite https://api.polydocs.io i dodajte putanju funkcije iza Polydocs URL-a.&#x20;

U ovom slučaju:

![](https://lh7-us.googleusercontent.com/-EwhMeH\_WXYVmMKus1-IZKLZNyTcYktcf\_YUT\_m2nfStfKXuBxKBb1MZfUIQCN4ZxNKQkNhvO\_pgnt1EUhNB34qG5AOe4wM0OxGRMQsV9a8h0XUgabqq8mLQhza\_AE7gxBetmb9bJmaWBQqEXrWT0VI)

* Sada zalepite ovaj link u polje za tekst pored POST metode u Postman-u.
* Izaberite tab \`Body\` u vašem HTTP zahtevu i izaberite \`form-data\`

![](https://lh7-us.googleusercontent.com/TNrKlyorn\_5YrIu5r4vcfyYgAnfhsl-SRVqWg9RoN0X1pUjXtn6J0EI7aeQ-oc2ZtFeTj8POcMXy6CwXzI1jhv-ufb2u7d80SC-lbGXmnx\_jVDunAbRw1jqAsB4PPsEzcFIOPeH5PJZvytUW2kIDYZ4)

![](https://lh7-us.googleusercontent.com/scAJpTSCqYSKYNNGPIrEsL0zDJIa7Dhe9tpqv\_zDjdLyAydugzdGA1s93njbFOOVbVbQf7oDEtRc14Kt4p1TXX8A--WjvRgeXWsAxDNWdrCN2-QDeya6-FFEG4\_-dhYgrj4yrVYllJs8eZsUgKOPvzo)

Unesite file u polje \`KEY\` gde ćete pronaći skriveni padajući meni File. Izaberite \`File\` i pređite na polje \`VALUE\` gde možete izabrati svoj fajl klikom na \`Select Files\`.

Kada kliknete na \`Send\`, trebalo bi da vidite “success”: true u odgovoru.

Treba da izgleda ovako:

![](https://lh7-us.googleusercontent.com/hNtG\_uTWgxww7iOmHLhnDqdrTlHCI1rk31LozG4l2DLPqxzSn9HoKn8CQIjeBgJLV4bxrGCjWOMRykJ3qBdZLYwxrZJGq\_S3tjVwSZmGTiMgVoqM97TTQjmW8CegEL2FV309NBmV0Fv\_vciSdQRFiOI)

## Primer Metode "DELETE"

Metoda DELETE se koristi za brisanje, na primer, korisnika, organizacija i slično.

* Izaberite DELETE Metodu.
* Autorizujte se kao što je opisano iznad.
* Otvorite https://api.polydocs.io i dodajte putanju funkcije iza Polydocs URL-a.

&#x20;Na primer:

![](https://lh7-us.googleusercontent.com/-QqSVIELl1IkxYK\_gGDa7nIv\_B1IvO3OjT3Ge6bAXwPl6jVDETuzXwtYJdRSmqLEP2d6B0L6MuwZvgJpI968pzp1APmJmuQ\_qlqYgZZhesocYCJVMCHhIZAKmlvMybUkUGXYZtySrnEbRTwWTritvKo)

* Sada zalepite ovaj link u polje za tekst pored DELETE metode u Postman-u.
* Zamenite {user\_id} na kraju URL-a sa stvarnim ID-em korisnika kog želite da obrišete. (ID korisnika možete dobiti koristeći GET metodu).
* Ako ste uključili user\_id u URL, ne morate dodati ključ i vrednost tela za to.
* Kada kliknete na \`Send\`, trebalo bi da vidite “success”: true u odgovoru.

&#x20;Treba da izgleda ovako:

![](https://lh7-us.googleusercontent.com/X8WNtsC9v7jqDIiaVhauJUgZK0yTC1GVz9rBptdiCxyLUiEEfbpIoYHpK7NvlDMTkhgiPyBb22H9GOfDdvmL-dakouTjuRDPwX4YX0Jz5IIo6eHu-wnw1S4jJd5ylHyffUXWKwX6ovDnp\_2WEAtSha4)

## Primer Metode "PUT"

Metoda PUT se uglavnom koristi za ažuriranje podataka korisnika ili organizacije. Veoma je lako razumeti i koristiti.

* Izaberite PUT Metodu.
* Autorizujte se kao što je opisano iznad.
* Otvorite https://api.polydocs.io i dodajte putanju funkcije iza Polydocs URL-a.

&#x20;Na primer:

![](https://lh7-us.googleusercontent.com/tC3qtPbFb1GsK6dBmB5Jrv5HqFOYLxNR1XB0PEuA8ipkHnH2ZQ6xrrkImNgbGSMoA6aAGvLr6K3cI4u\_qM96BOvR7AnQzmX17HBMBneNpLBc6RIzspfTYgrCWSj0fSE9mSWLIex3hc\_R-m-PI6zT6Rs)

* Sada zalepite ovaj link u polje za tekst pored PUT metode u Postman-u.
* Zamenite {user\_id} na kraju URL-a sa stvarnim ID-em korisnika kog želite da obrišete. (ID korisnika možete dobiti koristeći GET metodu).

## Promena Email Adrese Korisnika

* U telo unesite “email” kao ključ i novu email adresu kao vrednost.
* Zatim samo pritisnite \`Send\` i trebalo bi da vidite “success” u odgovoru.
