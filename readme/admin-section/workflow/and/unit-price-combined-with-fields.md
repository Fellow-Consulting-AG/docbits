# Cena jedinice kombinovana sa poljima

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-05-02 um 14.24.55.png" alt=""><figcaption></figcaption></figure>

Svrha: Ova DocBits kartica olakšava detaljno poređenje cena jedinica na fakturama sa onima navedenim u odgovarajućim narudžbenicama. Poboljšava tačnost finansijskog izveštavanja osiguravajući poštovanje dogovorenih cena.

Funkcionalnost:

* Cena jedinice kombinovana sa poljima: Ova kartica izračunava ukupan iznos za određenu stavku kombinovanjem cene jedinice sa dodatno navedenim poljima sa fakture. Zatim se ukupan iznos upoređuje sa zabeleženom cenom jedinice u narudžbenici za tu stavku.
* Vrednost operatora: Korisnici mogu postaviti specifične uslove za poređenje kombinovane cene jedinice sa fakture sa cenom jedinice u narudžbenici. Dostupni operatori uključuju:
*
* Jednako (=): Proverava da li se kombinovana cena fakture poklapa sa cenom u narudžbenici.
* Nije jednako (≠): Osigurava da se kombinovana cena fakture ne poklapa sa cenom u narudžbenici.
* Veće od (>): Proverava da li kombinovana cena fakture premašuje cenu u narudžbenici.
* Manje od (<): Potvrđuje da je kombinovana cena fakture ispod cene u narudžbenici.

Upotreba: Ova kartica je posebno korisna za menadžere ERP sistema i finansijske računovođe zadužene za održavanje strogih kontrola nad procesima nabavke i plaćanja. Osigurava da cene na fakturama odgovaraju onima dogovorenim u narudžbenicama, čime se umanjuju finansijske razlike.

Primer scenarija:

* Faktura prikazuje cenu jedinice od 50 dolara za proizvod. "Naziv polja" uključuje dodatnu manipulativnu naknadu od 5 dolara po jedinici. Kada se kombinuju, ukupan iznos po jedinici iznosi 55 dolara. Korišćenjem operatora "Jednako" sa postavljenom vrednošću od 55 dolara, kartica proverava da li se cena fakture poklapa sa narudžbenicom, osiguravajući usklađenost dogovora.

Implementiranjem kartice "Uporedi sa narudžbenicom: Cena jedinice kombinovana", preduzeća mogu automatizovati proveru tačnosti cena u odnosu na narudžbenice, optimizovati finansijske operacije i zaštititi se od prekomernog naplaćivanja.
