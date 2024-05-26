# Potvrđeni datum isporuke

<figure><img src="../../../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

Svrha: Ova DocBits kartica dizajnirana je kako bi se osiguralo da potvrđeni datumi isporuke na fakturama ili dokumentima o isporuci odgovaraju prihvaćenim datumima isporuke navedenim u tabeli pretrage master podataka. Pomaže u upravljanju očekivanjima i pridržavanju zakazanih isporuka unutar lanca snabdevanja.

## Funkcionalnost:

* Potvrđeni datum isporuke: Ova komponenta kartice beleži datum isporuke potvrđen na fakturi ili dokumentaciji o isporuci.
* Pretraga Tabele Master Podataka: Kartica referiše tabelu pretrage master podataka specificiranu od strane korisnika (identifikovanu parametrom \<Master Data Table>). Ova tabela sadrži prihvaćene datume isporuke za poređenje.
* Vrednost Operatora: Korisnici mogu specificirati kako bi potvrđeni datum isporuke trebao da se uporedi sa prihvaćenim datumom isporuke iz tabele master podataka. Dostupni operatori uključuju:
*
* Jednako (=): Osigurava da je potvrđeni datum isporuke isti kao prihvaćeni datum isporuke.
* Nije Jednako (≠): Ukazuje na neslaganje između potvrđenog i prihvaćenog datuma isporuke.
* Pre (<): Verifikuje da je potvrđeni datum isporuke raniji od prihvaćenog datuma isporuke.
* Posle (>): Proverava da li je potvrđeni datum isporuke kasniji od prihvaćenog datuma isporuke.

Korišćenje: Ova kartica je neprocenjiva za menadžere ERP-a i finansijske računovođe koji treba da prate i osiguraju usklađenost sa rasporedima isporuke. Posebno je korisna u sektorima gde je pravovremena isporuka ključna, kao što su proizvodnja, maloprodaja i distribucija.

## Primer scenarija:

* Faktura navodi potvrđeni datum isporuke 10. juna. Međutim, master data tabela pokazuje prihvaćeni datum isporuke 15. juna. Postavljanjem operatora na "Pre," kartica potvrđuje da su proizvodi planirani za ranu isporuku, omogućavajući planiranje logistike da se prilagodi.

Implementiranjem kartice "Uporedi sa Narudžbenicom: Potvrđeni vs. Prihvaćeni Datumi Isporuke," organizacije mogu proaktivno upravljati svojim lancem snabdevanja, osiguravajući da se isporuke planiraju i izvršavaju u skladu sa dogovorenim vremenima, čime se poboljšava operativna efikasnost i zadovoljstvo kupaca.

\
\
