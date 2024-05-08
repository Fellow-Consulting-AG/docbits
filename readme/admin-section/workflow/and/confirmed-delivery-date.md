# Potvrđeni datum isporuke

<figure><img src="../../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

Svrha: Ova kartica DocBits-a dizajnirana je da osigura da potvrđeni datumi isporuke na fakturama ili dokumentima o isporuci odgovaraju prihvaćenim datumima isporuke navedenim u tabeli pretrage master podataka. Pomaže u upravljanju očekivanjima i pridržavanju planiranih isporuka unutar lanca snabdevanja.

Funkcionalnost:

* Potvrđeni datum isporuke: Ova komponenta kartice beleži datum isporuke potvrđen na fakturi ili dokumentaciji o isporuci.
* Pretraga tabele master podataka: Kartica se odnosi na tabelu pretrage master podataka koju određuje korisnik (identifikovanu parametrom \<Master Data Table>). Ova tabela sadrži prihvaćene datume isporuke za poređenje.
* Vrednost operatora: Korisnici mogu odrediti kako potvrđeni datum isporuke treba da se uporedi sa prihvaćenim datumom isporuke iz tabele master podataka. Dostupni operatori uključuju:
*
* Jednako (=): Osigurava da je potvrđeni datum isporuke isti kao prihvaćeni datum isporuke.
* Nije jednako (≠): Ukazuje na neslaganje između potvrđenog i prihvaćenog datuma isporuke.
* Pre (<): Verifikuje da je potvrđeni datum isporuke raniji od prihvaćenog datuma isporuke.
* Posle (>): Proverava da li je potvrđeni datum isporuke kasniji od prihvaćenog datuma isporuke.

Upotreba: Ova kartica je neprocenjiva za menadžere ERP-a i finansijske računovođe koji treba da prate i osiguraju usaglašenost sa rasporedima isporuke. Posebno je korisna u sektorima gde je pravovremena isporuka ključna, kao što su proizvodnja, maloprodaja i distribucija.

Primer scenarija:

* Faktura navodi potvrđeni datum isporuke 10. juna. Međutim, tabela master podataka pokazuje prihvaćeni datum isporuke 15. juna. Postavljanjem operatora na "Pre," kartica potvrđuje da su robe planirane za ranu isporuku, omogućavajući planiranje logistike da se prilagodi.

Implementiranjem kartice "Uporedi sa narudžbenicom: Potvrđeni vs. Prihvaćeni datumi isporuke", organizacije mogu proaktivno upravljati svojim lancem snabdevanja, osiguravajući da se isporuke planiraju i izvršavaju u skladu sa dogovorenim rokovima, čime se poboljšava operativna efikasnost i zadovoljstvo kupaca.

\
\
