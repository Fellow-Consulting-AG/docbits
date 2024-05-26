# Faktura za kupovinu - Izvoz jedinične cene za drugo odobrenje

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-05-03 um 14.59.02.png" alt=""><figcaption></figcaption></figure>

Ovaj naslov ukazuje da je pravilo postavljeno kako bi se upravljala drugom fazom odobrenja faktura za kupovinu sa fokusom na jediničnu cenu, osiguravajući da se podudara sa dogovorenim uslovima.

#### Konfiguracija pravila:

1. **Kada…**
* **Tip dokumenta je Faktura**: Ova uslova osigurava da se pravilo aktivira samo za dokumenta identifikovana kao fakture, što je ključno za precizno usmeravanje radnog toka.
2. **I…**
* **Status dokumenta je Na čekanju za drugo odobrenje**: Ovo precizira da faktura čeka drugo odobrenje. Ova faza često pruža dodatni nadzor kako bi se osigurala tačnost pre finalizacije transakcije.
* **Polje dokumenta Tip fakture je Jednako Faktura za kupovinu**: Ovaj uslov dodatno precizira da pravilo važi samo za fakture kategorizovane specifično kao "Fakture za kupovinu", razlikujući ih od drugih vrsta faktura.
* **Logika jedinične cene u potvrdi porudžbine Jednaka je porudžbini za kupovinu**: Ovaj uslov proverava da li se jedinična cena navedena u potvrdi porudžbine podudara sa jediničnom cenom u porudžbini za kupovinu. Osigurava da se obrada fakture nastavlja samo ako postoji doslednost u cenama, što je ključno za budžetiranje i finansijsko izveštavanje.

#### Akcija (Onda…):

* **Pokreni izvoz**: Kada faktura ispuni navedene uslove (tj. jedinične cene se podudaraju između potvrde porudžbine i porudžbine za kupovinu), pokreće se akcija "Pokreni izvoz". Ovo verovatno uključuje izvoz podataka fakture radi dalje obrade, možda u drugi finansijski sistem ili u svrhe izveštavanja.

#### Svrha ovog pravila:

* **Osigurati tačnost i doslednost**: Proverom da li se jedinične cene podudaraju između potvrde porudžbine i porudžbine za kupovinu, sistem pomaže u održavanju finansijske tačnosti i sprečava preterano naplaćivanje ili podcenjivanje.
* **Optimizacija finansijske obrade**: Automatizacija izvoza podataka nakon potvrde cena smanjuje ručno rukovanje i ubrzava finansijski ciklus obrade.
* **Poboljšanje usaglašenosti i nadzora**: Zahtevanje drugog odobrenja za proveru cena dodaje dodatni sloj nadzora, što je ključno za usaglašenost sa finansijskim politikama i kontrolama.

Ovo pravilo je primer kako se automatizacija radnog toka može efikasno koristiti kako bi se osiguralo precizno i efikasno rukovanje finansijskim dokumentima unutar organizacije, posebno u kontekstu velikih obima transakcija koje zahtevaju temeljnu validaciju.
