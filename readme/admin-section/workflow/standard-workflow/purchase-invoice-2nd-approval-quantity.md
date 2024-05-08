# Faktura za kupovinu - Druga odobrenje količine

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-05-03 um 14.56.54.png" alt=""><figcaption></figcaption></figure>

Ovaj naslov ukazuje da se pravilo odnosi posebno na rukovanje fakturama za kupovinu tokom faze sekundarnog odobrenja, sa fokusom na proveru tačnosti navedenih količina.

#### Konfiguracija pravila:

1. **Kada…**
* **Tip dokumenta je Faktura**: Ova uslova osigurava da se pravilo aktivira samo za dokumenta klasifikovana kao fakture. To je ključno za održavanje specifičnosti i relevantnosti u radnom toku.
2. **I…**
* **Status dokumenta je Na čekanju za drugo odobrenje**: Ovo precizira da je faktura trenutno na čekanju za drugo odobrenje. Ova faza je obično namenjena dodatnom nadzoru pre finalizacije fakture.
* **Polje dokumenta Tip fakture je Jednako Faktura za kupovinu**: Ovaj uslov dodatno precizira pravilo da se primenjuje isključivo na fakture identifikovane kao "Fakture za kupovinu". Ova kategorizacija pomaže u razlikovanju od drugih tipova faktura.
* **Logika Količina u potvrdi porudžbine nije Jednako porudžbina za kupovinu**: Ovaj ključni uslov proverava da li se količina navedena u potvrdi porudžbine poklapa sa količinom u originalnoj porudžbini za kupovinu. Akcija se pokreće ako postoji neslaganje, što ukazuje na potencijalnu grešku ili problem koji zahteva rešenje.

#### Akcija (Onda…):

* **Dodeli korisnika iz polja Ime kupca, koristi korisnika Korisnik kao rezervu**: Ako su uslovi pravila ispunjeni (tj. postoji neslaganje u količinama), faktura se automatski dodeljuje osobi navedenoj u polju 'Ime kupca' radi dalje provere. Ako je ovo polje prazno ili određena osoba nije dostupna, podrazumevani korisnik (verovatno administrator ili drugi određeni član osoblja) preuzima kontrolu kako bi se osigurala pravovremena provera i rešenje.

#### Svrha ovog pravila:

* **Tačnost i usklađenost**: Pravilo je od vitalnog značaja za osiguravanje tačnosti procesa fakturisanja i usklađenosti sa uslovima dogovorenim u porudžbini za kupovinu. Pomaže u sprečavanju finansijskih neslaganja i potencijalnih grešaka u inventaru.
* **Odobrenja bez zastoja**: Automatizacija procesa pregleda specifičnih neslaganja pomaže u ubrzanju odobrenja i osigurava da se eventualni problemi brzo reše od strane odgovarajućeg osoblja.
* **Poboljšan finansijski nadzor**: Zahtevanje sekundarnog odobrenja za provere količina jača finansijske kontrole i odgovornost unutar organizacije.

Ova postavka ilustruje kako se automatizacija radnog toka može koristiti za poboljšanje operativne efikasnosti i osiguranje finansijske integriteta, posebno u upravljanju složenim procesima kupovine unutar kompanije.
