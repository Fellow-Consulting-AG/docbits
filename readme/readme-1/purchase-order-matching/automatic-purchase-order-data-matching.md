# Automatsko uparivanje podataka o narudžbenici

Docbits je napredni sistem dizajniran za automatizaciju uparivanja podataka o narudžbenici (PO) sa dolaznim fakturama. Ovaj alat je posebno dizajniran za efikasno upravljanje i obradu podataka o fakturama unutar ERP sistema. Ova dokumentacija objašnjava osnove automatskog uparivanja putem Docbits-a i definiše specifična pravila potrebna za uspešno uparivanje.

## **Osnovni principi automatskog uparivanja u Docbits-u**

**Ekstrakcija podataka:** Docbits započinje proces ekstrakcijom relevantnih podataka iz digitalizovanih faktura. Tipično, ovi podaci uključuju brojeve stavki, količine i jedinične cene svake stavke fakture. Preciznost ove ekstrakcije je ključna, jer predstavlja osnovu za naredni proces uparivanja.

**Poređenje sa podacima o narudžbenici:** Ekstraktovani podaci se porede sa odgovarajućim informacijama u sačuvanim narudžbenicama. Docbits proverava da li se brojevi stavki, količine i cene podudaraju sa onima u narudžbenicama. Za uspešno uparivanje, podaci na fakturama moraju odgovarati podacima u narudžbenicama, uzimajući u obzir definisane granice tolerancije.

**Automatsko uparivanje:** Na osnovu rezultata poređenja, Docbits vrši uparivanje. Sistem proverava da li kriterijumi uparivanja padaju unutar postavljenih granica tolerancije. Ako se ovi kriterijumi ispune, uparivanje se smatra uspešnim.

**Izveštavanje:** Nakon završetka procesa uparivanja, Docbits generiše izveštaje koji prikazuju status uparivanja. Ovi izveštaji informišu o uspešno uparenim fakturama i identifikuju one sa neslaganjima.

## **Definicija pravila uparivanja**

**Broj stavke:** Broj stavke na fakturi mora tačno odgovarati broju stavke u narudžbenici. Nema tolerancije za odstupanja u brojevima stavki.

**Količine:** Količina isporučenih dobara na fakturi može varirati unutar unapred definisanog opsega tolerancije. Tipično, tolerancija od ±5% može biti prihvatljiva kako bi se uzeli u obzir manji različiti u količinama isporuke.

**Cene:** Odstupanja cena su prihvatljiva do određenog praga. Česta tolerancija može biti ±2% cene kako bi se prihvatile male razlike u cenama koje proizilaze iz razlika u zaokruživanju ili fluktuacija valuta.

## **Status uparivanja:**

* **Potpuno uparivanje:** Svi podaci (broj stavke, količina i cena) su unutar postavljenih granica tolerancije.
* **Delimično uparivanje:** Jedan ili više podataka odstupa van granica tolerancije, ali odstupanja su minimalna i zahtevaju ručni pregled.
* **Bez uparivanja:** Značajna odstupanja u jednom ili više podataka koji zahtevaju odmah ispravku ili dalje istraživanje.

Precizna definicija ovih pravila i postavljanje granica tolerancije su ključni za efikasnost automatskog uparivanja i smanjenje ručnih intervencija. Docbits omogućava fleksibilnu konfiguraciju ovih parametara kako bi zadovoljio potrebe različitih preduzeća i industrija.
