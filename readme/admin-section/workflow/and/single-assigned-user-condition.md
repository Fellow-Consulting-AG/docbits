# Uslov sa jednim dodeljenim korisnikom

<figure><img src="../../../.gitbook/assets/userlmn_77e991cee96598023f9a3ac7ad230e50.png" alt=""><figcaption></figcaption></figure>

**Svrha**

Ova kartica radnog toka olakšava operacije zasnovane na dodeli zadatka ili dokumenta jednom određenom korisniku. Koristeći direktni uslovni logički pristup, upravlja radnim tokovima koji zahtevaju ciljano angažovanje korisnika, obezbeđujući preciznost u rukovanju zadacima zasnovanim na korisnicima.

**Komponente kartice**

1. **Operator**
* **Opis**: Specificira logiku koja će se primeniti na dodelu korisnika.
* **Opcije**:
* **JE**: Pokreće operaciju ako dodeljeni korisnik dokumenta ili zadatka odgovara određenom korisniku.
* **NIJE**: Pokreće operaciju ako dodeljeni korisnik ne odgovara određenom korisniku.
2. **Korisnik**
* **Opis**: Omogućava izbor jednog korisnika sa kojim će se uporediti dodeljeni korisnik.
* **Detalj**: Ovo uključuje jednostavno padajuće polje ili polje za automatsko završavanje gde se može odabrati jedan korisnik odjednom.

**Funkcionalnost**

* **Identifikacija dodele korisnika**: Identifikuje korisnika koji je trenutno dodeljen određenom zadatku ili dokumentu.
* **Procena uslova**:
* Za operator **JE**, kartica proverava da li je dodeljeni korisnik isti kao odabrani korisnik.
* Za operator **NIJE**, proverava da li je dodeljeni korisnik različit od odabranog korisnika.
* **Izvršenje radnje**:
* **Tačan uslov**: Ako dodela zadovoljava postavljeni uslov (JE ili NIJE), pokreće unapred definisane akcije, koje mogu uključivati nastavak odobrenja, pokretanje dodatnih zadataka, slanje obaveštenja ili druge povezane radne tokove.
* **Netačan uslov**: Ako uslov nije ispunjen, sistem može preusmeriti zadatak, zadržati ga radi pregleda ili pokrenuti alternativne unapred definisane akcije.

**Interakcije sa korisnicima**

* **Postavljanje i konfiguracija**: Korisnici postavljaju karticu biranjem operatora i odabirom korisnika iz polja za korisnika. Ovaj postupak postavljanja treba da bude jednostavan, obezbeđujući lako odabiranje korisnika i konfiguraciju.
* **Pratnja i izveštavanje**: Nudi alate za praćenje performansi kartice, kao što je praćenje koje zadatke pokreću određene dodele korisnika i ishode ovih pokretača.
* **Obrada grešaka i obaveštenja**: Pruža mehanizme za obaveštavanje korisnika ako su zadaci netačno dodeljeni ili ako dođe do operativnih grešaka zbog problema sa dodelom.

#### Zaključak

Kartica radnog toka "Uslov sa jednim dodeljenim korisnikom" je ključna za precizno upravljanje dokumentima i zadacima specifičnim za korisnika unutar ERP sistema. Ona pojednostavljuje radne tokove fokusiranjem na pojedinačne dodele korisnika, čime se obezbeđuje da se akcije izvršavaju samo kada je to prikladno, na osnovu uloge i odgovornosti korisnika. Jasno dokumentovanje ove kartice pomoći će korisnicima da razumeju njen primenjivi, omogućavajući im da je efikasno implementiraju i upravljaju njome u okviru svojih svakodnevnih operacija. Ova dokumentacija osigurava da svi potencijalni korisnici lako shvate svrhu kartice i integrišu je bez poteškoća u svoje radne tokove.
