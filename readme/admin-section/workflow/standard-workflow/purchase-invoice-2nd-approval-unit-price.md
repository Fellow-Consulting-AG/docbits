# Faktura za kupovinu - Drugo odobrenje jedinične cene

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-05-03 um 14.55.09.png" alt=""><figcaption></figcaption></figure>

Ovaj naslov ukazuje da je pravilo postavljeno da upravlja drugom fazom odobrenja fakture za kupovinu, sa posebnim fokusom na validaciju jedinične cene.

#### Konfiguracija pravila:

1. **Kada…**
* **Tip dokumenta je Faktura**: Ova uslov osigurava da se pravilo pokreće samo za dokumenta koji su identifikovani kao fakture, filtrirajući druge tipove dokumenata i održavajući relevantnost radnog toka.
2. **I…**
* **Status dokumenta je Na čekanju drugog odobrenja**: Ovo precizira da je faktura u fazi gde čeka drugo odobrenje. Ovo je obično korak dizajniran da osigura dodatni nadzor pre konačne obrade.
* **Polje dokumenta Tip fakture je Jednako Faktura za kupovinu**: Ovo dodatno sužava primenu ovog pravila samo na fakture koje su klasifikovane kao "Fakture za kupovinu", razlikujući ih od drugih podtipova faktura.
* **Logika Jedinična cena u potvrdi porudžbine nije Jednako porudžbini za kupovinu**: Ova logička provera je ključna jer upoređuje jediničnu cenu navedenu u potvrdi porudžbine sa jediničnom cenom u originalnoj porudžbini za kupovinu. Akcija se pokreće ako se ove vrednosti ne podudaraju, što može ukazivati na neslaganje koje zahteva rešenje.

#### Akcija (Onda…):

* **Dodeli korisnika iz polja Ime kupca, koristi korisnika Korisnik kao zamenu**: Ako su ispunjeni navedeni uslovi (tj. postoji neslaganje u jediničnim cenama), faktura se automatski dodeljuje kupcu (ime navedeno u polju 'Ime kupca') radi dalje provere. Ako je polje 'Ime kupca' prazno ili nije navedeno, podrazumevani korisnik (verovatno administrator ili drugi određeni član osoblja) se dodeljuje kao zamena za obradu odobrenja.

#### Svrha ovog pravila:

* **Osigurati tačnost i usklađenost**: Ovo pravilo je ključno za osiguravanje tačnosti procesa fakturisanja i usklađenosti sa dogovorenim uslovima. Pokretanjem pregleda kada postoji neslaganje u jediničnim cenama, sistem pomaže u sprečavanju finansijskih grešaka ili potencijalne prevare.
* **Optimizacija odobrenja**: Automatizacija dodele za pregled na osnovu određenih neslaganja pomaže u optimizaciji procesa odobrenja i osigurava da se problemi brzo reše od strane odgovarajućeg osoblja.
* **Finansijski nadzor**: Zahtevanje drugog odobrenja, posebno na osnovu podudaranja cena, jača finansijske kontrole i odgovornost unutar organizacije.
