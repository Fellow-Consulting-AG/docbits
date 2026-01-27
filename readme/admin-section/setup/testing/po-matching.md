# Provera podudaranja narudžbenica (PO Matching)

{% embed url="https://youtu.be/qR-lrSaj4Ug" %}
DocBits PO Matching Tutorial: Auto/Manual Line Matching, Tolerances & Mismatch Indicators
{% endembed %}

Kada je u pitanju testiranje konfiguracije podudaranja narudžbenica (PO Matching), moraćete da kreirate narudžbenicu u LN/M3 kako biste proverili da li je INFOR sinhronizovan sa DocBits-om. 

## Kreiranje narudžbenice u INFOR-u

* LN: [Dokumentacija za LN](https://docs.infor.com/ln/10.4/en-us/lnolh/docs/ln\_10.4\_procpoug\_\_en-us.pdf)
* M3: [Dokumentacija za M3](https://docs.infor.com/m3udi/16.x/en-us/m3beud/default.html?helpcontent=ois610.html)

Nakon što ste kreirali svoju narudžbenicu, idite na Postavke → Pretraga master podataka i potražite broj narudžbenice koju ste upravo kreirali, jer bi sada trebalo da se pojavi u master podacima o narudžbenicama u DocBits-u.

![](https://lh7-us.googleusercontent.com/JKGJdww6uF6U5mc1s1X\_uCcEMPYeqcikfrFOFjxpxpuaNjw-XmzNmIV2G2x6R-ZpwN2KlZACQe5Hs\_UB26klGU5XZyu6srVVLPVkS9AgEDZ1SO75YF-4ZTIt-aAuxoyyoW5sNPLsl0UxXwk193QNrFs)

Treba da vidite svoj jedinstveni broj narudžbenice ovde, što znači da su DocBits i INFOR ispravno sinhronizovani.

Sada otpremite svoj račun koji se podudara sa količinama i jediničnim cenama narudžbenice koju ste kreirali. Validirajte dokument i odaberite Podudaranje PO na ekranu za validaciju.

Stavke narudžbenice i računa trebalo bi automatski da se podudaraju, zatim jednostavno odaberite opciju za izvoz i proverite da li se dokument izvozi bez grešaka. Ukoliko naiđete na grešku prilikom izvoza, kreirajte tiket za tim podrške DocBits-a da vam pomogne. Ukoliko niste sigurni kako da kreirate tiket unutar DocBits-a, molimo pogledajte našu dokumentaciju za Pregled DocBits-a radi pomoći.
