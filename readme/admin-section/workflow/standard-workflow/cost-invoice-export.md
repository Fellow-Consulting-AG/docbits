# Izvoz troškova fakture

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-05-03 um 14.53.28.png" alt=""><figcaption></figcaption></figure>

Ovaj naslov ukazuje da je pravilo posebno konfigurisano za upravljanje troškovnim fakturama i uključuje akciju izvoza, možda za izveštavanje, dalju obradu ili integraciju sa drugim sistemima.

#### Konfiguracija pravila:

1. **Kada…**
* **Tip dokumenta je Faktura**: Ova uslova osigurava da se pravilo pokreće samo za dokumente kategorizovane kao fakture, održavajući specifičnost radnog toka za upravljanje fakturama.
2. **I…**
* **Polje fakture Tip fakture je Jednako Troškovna faktura**: Ovo specificira da se pravilo primenjuje samo na fakture koje su eksplicitno označene kao "Troškovne fakture" u određenom polju unutar dokumenta. To pomaže u razlikovanju od drugih vrsta faktura.
* **Status dokumenta je Na čekanju za drugo odobrenje**: Faktura mora biti u statusu "Na čekanju za drugo odobrenje". To ukazuje da je faktura već prošla kroz početno odobrenje i čeka drugo, možda konačno, pregledanje.

#### Akcija (Onda…):

* **Pokreni izvoz**: Kada faktura ispuni navedene uslove (bude troškovna faktura i na čekanju za drugo odobrenje), izvršava se akcija "Pokreni izvoz". To može uključivati slanje podataka fakture u drugi sistem radi finansijske analize, izveštavanja ili svrha usaglašenosti.

#### Svrha ovog pravila:

* **Efikasnost radnog toka**: Ovo pravilo pomaže automatizaciji obrade troškovnih faktura osiguravajući da prođu kroz neophodne faze odobrenja bez ručnog mešanja, povećavajući brzinu i tačnost finansijskih operacija.
* **Kontrola i usaglašenost**: Zahtevajući drugo odobrenje, sistem sprovodi kontrolni mehanizam koji osigurava da se troškovne fakture detaljno pregledaju, unapređujući finansijski nadzor.
* **Integracija i izveštavanje**: Akcija izvoza sugeriše da kada su fakture potpuno odobrene, mogu se integrisati u druge sisteme radi dalje obrade ili analize, što je ključno za finansijsko izveštavanje i revizije.

Ovakvo pravilo je od vitalnog značaja za organizacije koje se bave različitim vrstama faktura i trebaju osigurati da se svaka vrsta obrađuje prema specifičnim protokolima. Smanjuje rizik od grešaka i osigurava usaglašenost sa internim kontrolama i spoljnim propisima.
