# Račun troškova - Izvoz

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-05-03 um 14.53.28.png" alt=""><figcaption></figcaption></figure>

Ovaj naslov ukazuje da je pravilo posebno konfigurisano za upravljanje računima troškova i uključuje akciju izvoza, možda za izveštavanje, dalju obradu ili integraciju sa drugim sistemima.

#### Konfiguracija pravila:

1. **Kada…**
* **Tip dokumenta je Račun**: Ova uslova osigurava da se pravilo pokreće samo za dokumente kategorizovane kao računi, održavajući specifičnost radnog toka za upravljanje računima.
2. **I…**
* **Polje računa podtipa je Jednako Račun troškova**: Ovo specificira da se pravilo primenjuje samo na one račune koji su eksplicitno označeni kao "Računi troškova" u određenom polju unutar dokumenta. To pomaže u razlikovanju od drugih vrsta računa.
* **Status dokumenta je Na čekanju za drugo odobrenje**: Račun mora biti u statusu "Na čekanju za drugo odobrenje". To ukazuje da je račun već prošao kroz početno odobrenje i čeka drugo, možda konačno, pregledanje.

#### Akcija (Onda…):

* **Pokreni izvoz**: Kada račun ispuni navedene uslove (bude račun troškova i na čekanju za drugo odobrenje), izvršava se akcija "Pokreni izvoz". To može uključivati slanje podataka o računu u drugi sistem radi finansijske analize, izveštavanja ili svrhe usaglašenosti.

#### Svrha ovog pravila:

* **Efikasnost radnog toka**: Ovo pravilo pomaže automatizaciji obrade računa troškova osiguravajući da prođu kroz neophodne faze odobrenja bez ručnog mešanja, povećavajući brzinu i tačnost finansijskih operacija.
* **Kontrola i usaglašenost**: Zahtevajući drugo odobrenje, sistem sprovodi kontrolni mehanizam koji osigurava da se računi troškova detaljno pregledaju, poboljšavajući finansijski nadzor.
* **Integracija i izveštavanje**: Akcija izvoza sugeriše da kada su računi potpuno odobreni, mogu se integrisati u druge sisteme radi dalje obrade ili analize, što je ključno za finansijsko izveštavanje i revizije.

Ovakvo pravilo je od vitalnog značaja za organizacije koje se bave različitim vrstama računa i trebaju osigurati da se svaka vrsta obrađuje prema specifičnim protokolima. Smanjuje rizik od grešaka i osigurava usaglašenost sa internim kontrolama i spoljnim propisima.
