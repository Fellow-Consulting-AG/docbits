# Uslov dodeljenog korisnika

<figure><img src="../../../.gitbook/assets/userlmn_5e16e9b23626ec1211c753fec5333513.png" alt=""><figcaption></figcaption></figure>

**Svrha**

Ova kartica radnog toka upravlja izvršenjem operacija na osnovu toga da li je zadatak ili dokument dodeljen određenom korisniku ili grupi korisnika. Koristi uslovnu logiku da bi pokrenula ili sprečila određene akcije, čineći je idealnom za radne tokove koji zahtevaju rukovanje specifično za korisnike.

**Komponente kartice**

1. **Operator**
* **Opis**: Definiše logički uslov koji se primenjuje na dodelu korisnika.
* **Opcije**:
* **JE**: Pokreće operaciju ako dodeljeni korisnik dokumenta ili zadatka odgovara bilo kom korisniku na navedenom spisku.
* **NIJE**: Pokreće operaciju ako dodeljeni korisnik dokumenta ili zadatka ne odgovara nijednom korisniku na navedenom spisku.
2. **Spisak korisnika**
* **Opis**: Spisak ili izbor korisnika za poređenje sa dodeljenim korisnikom.
* **Detalji**: Ovaj spisak može uključivati jednog ili više korisnika, omogućavajući kartici da efikasno rukuje i jednim i više korisničkim uslovima. Izbor se može napraviti putem polja za potvrdu, višestrukog padajućeg menija ili sličnih UI elemenata.

**Funkcionalnost**

* **Identifikacija dodele korisnika**: Automatski identifikuje korisnika ili korisnike dodeljene određenom zadatku ili dokumentu unutar ERP sistema.
* **Evaluacija uslova**:
* Korišćenjem operatora **JE**, kartica proverava da li je dodeljeni korisnik među onima navedenim na Spisku korisnika.
* Korišćenjem operatora **NIJE**, kartica osigurava da dodeljeni korisnik nije među navedenima.
* **Izvršenje akcija**:
* **Tačan uslov**: Ako dodeljeni korisnik zadovoljava uslov (bilo JE ili NIJE), pokreću se relevantne akcije, poput obaveštenja, pokretanja zadataka, odobrenja ili drugih koraka radnog toka.
* **Netačan uslov**: Ako uslov nije ispunjen, dokument ili zadatak može proći kroz različito usmeravanje, ili se mogu specificirati alternativne akcije.

**Interakcije sa korisnicima**

* **Postavljanje i konfiguracija**: Korisnici konfigurišu karticu biranjem operatora i specificiranjem relevantnih korisnika sa Spiska korisnika. Postavljanje treba da bude korisnički prijateljsko i intuitivno kako bi se omogućilo biranje iz potencijalno velikih baza korisnika.
* **Pracenje i izveštavanje**: ERP sistem treba da pruži funkcionalnost za praćenje i izveštavanje o operacijama pokrenutim ovom karticom, nudeći uvide u tačnost dodele i efikasnost procesa.
* **Upravljanje greškama i obaveštenjima**: Korisnici treba da imaju opcije da primaju upozorenja ili obaveštenja ako postoje problemi sa dodelama, poput nedodeljenih zadataka ili grešaka u izboru korisnika.

#### Zaključak

Radna karta "Uslov dodeljenog korisnika" je ključan alat za upravljanje radnim tokovima dokumenata i zadataka koji zavise od dodela korisnika. Omogućavajući uslove zasnovane na tome da li je zadatak ili dokument dodeljen određenim korisnicima, osigurava da se radni tokovi pokreću samo odgovarajućim korisničkim interakcijama, unapređujući odgovornost i usklađenost zadataka unutar timova. Jasno dokumentovanje ove kartice pomoći će korisnicima da razumeju njen značaj i efikasno je integrišu u svoje radne tokove, osiguravajući glatke i efikasne operacije prilagođene korisničkim ulogama i odgovornostima.
