# Faktura za kupovinu - Izvoz količine za drugo odobrenje

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-05-03 um 15.00.53.png" alt=""><figcaption></figcaption></figure>

Ovaj naslov ukazuje da je pravilo postavljeno kako bi se upravljala drugom fazom odobrenja za fakture za kupovinu sa naglaskom na detalje količine, osiguravajući da se količine na fakturi poklapaju sa onima na originalnoj narudžbenici.

#### Konfiguracija pravila:

1. **Kada…**
* **Tip dokumenta je Faktura**: Ova uslov osigurava da se pravilo aktivira samo za dokumenta identifikovana kao fakture, što je ključno za precizno usmeravanje radnog toka.
2. **I…**
* **Status dokumenta je Na čekanju za drugo odobrenje**: Ovo specificira da je faktura trenutno na čekanju za drugo odobrenje. Ova faza često pruža dodatni nadzor kako bi se osigurala tačnost pre nego što se transakcija finalizuje.
* **Polje dokumenta Tip fakture je Jednako Faktura za kupovinu**: Ovaj uslov dodatno specificira da se pravilo primenjuje samo na fakture kategorizovane specifično kao "Fakture za kupovinu", razlikujući ih od drugih vrsta faktura.
* **Logika Količina u potvrdi narudžbenice Jednako narudžbenici za kupovinu**: Ovaj uslov proverava da li se količina navedena u potvrdi narudžbenice poklapa sa količinom u narudžbenici za kupovinu. Osigurava da se obrada fakture nastavlja samo ako su količine konzistentne, što je ključno za upravljanje inventarom i finansijsku tačnost.

#### Akcija (Onda…):

* **Pokreni izvoz**: Kada faktura ispuni navedene uslove (tj. količine se poklapaju između potvrde narudžbenice i narudžbenice za kupovinu), pokreće se akcija "Pokreni izvoz". Ovo verovatno uključuje izvoz podataka fakture radi dalje obrade, možda u drugi finansijski sistem ili u svrhe izveštavanja.

#### Svrha ovog pravila:

* **Osigurati tačnost i doslednost**: Proverom da li se količine poklapaju između potvrde narudžbenice i narudžbenice za kupovinu, sistem pomaže u održavanju tačnosti inventara i sprečava neslaganja koja bi mogla uticati na finansijsko izveštavanje ili upravljanje zalihama.
* **Optimizacija finansijske obrade**: Automatizacija izvoza podataka nakon potvrde količina smanjuje ručno rukovanje i ubrzava ciklus finansijske obrade.
* **Poboljšanje usaglašenosti i nadzora**: Zahtevanje drugog odobrenja za proveru količine dodaje dodatni sloj nadzora, ključan za usaglašenost sa finansijskim politikama i kontrolama.

Ovo pravilo je jasan primer kako se automatizacija radnog toka može efikasno koristiti kako bi se osiguralo precizno i efikasno rukovanje finansijskim dokumentima unutar organizacije, posebno u kontekstu procesa kupovine koji uključuju velike količine transakcija koje zahtevaju temeljnu validaciju.
