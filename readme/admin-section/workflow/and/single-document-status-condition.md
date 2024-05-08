# Uslov stanja jednog dokumenta

<figure><img src="../../../.gitbook/assets/userlmn_928e514bc0e2aa775894e4ec5f992bd9.png" alt=""><figcaption></figcaption></figure>

**Svrha**

Ova kartica radnog toka prilagođena je za upravljanje operacijama nad dokumentima na osnovu jednog, određenog statusa dokumenta. Pojednostavljujući uslov na jedan status, kartica je usmerena na vrlo specifične okidače radnog toka, što je čini idealnom za ciljane aktivnosti obrade dokumenata unutar ERP sistema.

**Komponente kartice**

1. **Operator**
* **Opis**: Određuje metod za procenu statusa dokumenta u odnosu na izabrani uslov.
* **Opcije**:
* **je**: Okida operaciju ako trenutni status dokumenta odgovara izabranom statusu.
* **nije**: Okida operaciju ako trenutni status dokumenta ne odgovara izabranom statusu.
2. **Status**
* **Opis**: Omogućava izbor jednog statusa dokumenta za postavljanje uslova.
* **Primeri statusa**: "Greška", "Greška pri izvozu", "Spreman za validaciju", "Spreman za pregled", "Na čekanju odobrenja", "Na čekanju drugog odobrenja".
* **Detalji**: Korisnici biraju jedan status iz padajućeg menija ili seta radio dugmadi. Taj status zatim služi kao kriterijum za rad kartice.

**Funkcionalnost**

* **Identifikacija statusa dokumenta**: Identifikuje trenutni status dokumenta dok prolazi kroz ERP sistem.
* **Procena uslova**:
* Na osnovu izabranog operatora (`je` ili `nije`), kartica proverava da li se trenutni status dokumenta poklapa sa izabranim kriterijumom statusa.
* **Izvršenje akcije**:
* **Tačan uslov**: Ako status odgovara (ili ne odgovara, u zavisnosti od operatora), pokreće se odgovarajuća akcija. To može biti rutiranje za dalju obradu, generisanje obaveštenja ili drugi unapred definisani radni tokovi.
* **Netačan uslov**: Ako uslov nije ispunjen, nijedna akcija se ne preduzima, ili se pokreće alternativni put.
* **Integracija sa drugim radnim tokovima**: Iako je dizajniran za evaluaciju jednog statusa, ova kartica se može efikasno integrisati u šire sekvence radnih tokova kako bi se osiguralo precizno rukovanje dokumentima.

**Interakcije sa korisnicima**

* **Postavljanje i konfiguracija**: Korisnici postavljaju karticu biranjem operatora, a zatim izborom jednog statusa iz dostupnih opcija. Ovaj proces izbora je jednostavan i dizajniran da spreči zabunu.
* **Monitoring i izveštavanje**: Omogućava praćenje putem izveštaja generisanih od strane sistema ili tabli koje prate obradu dokumenata na osnovu njihovog statusa, pomažući u nadgledanju efikasnosti implementiranih radnih tokova.
* **Upravljanje greškama i obaveštenjima**: Konfigurabilno je da obavesti korisnike o bilo kakvim anomalijama u obradi ili da označi dokumenta koja ne ispunjavaju postavljene uslove, osiguravajući brzu pažnju i rešavanje.

#### Zaključak

Radna karta "Uslov stanja jednog dokumenta" pojednostavljuje upravljanje dokumentima fokusirajući se na pojedinačne uslove statusa. Ova specifikacija pomaže u slučajevima kada je precizna kontrola nad tokovima dokumenata neophodna, posebno u okruženjima sa strogim kriterijumima obrade. Jasno dokumentovanje ove verzije kartice će osigurati da korisnici potpuno razumeju njen primenjivi i mogu je efikasno integrisati u svoje svakodnevne operacije, unapređujući kako usklađenost tako i efikasnost u obradi dokumenata.
