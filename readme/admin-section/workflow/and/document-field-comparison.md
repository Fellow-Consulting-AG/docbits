# Poređenje polja dokumenata

<figure><img src="../../../.gitbook/assets/userlmn_7d5c06ce63181faee30b7bc6903e4d7b.png" alt=""><figcaption></figcaption></figure>

**Svrha**

Ova kartica radnog toka je dizajnirana da automatski uporedi vrednosti dva određena polja unutar dokumenta na osnovu definisanog operatora. Koristi se za sprovođenje integriteta podataka i osiguravanje da podaci dokumenta odgovaraju poslovnim pravilima ili uslovima.

**Komponente kartice**

1. **Imena polja**
* **Opis**: Specificira imena dva polja unutar dokumenta koja će biti upoređena.
* **Detalj**: Korisnici moraju uneti tačna imena polja kako se pojavljuju u sistemu. Ta polja mogu biti bilo kog tipa podataka koji podržava upoređivanje, kao što su numerička, datumska ili tekstualna polja.
2. **Operator**
* **Opis**: Operator upoređivanja koji se koristi za procenu odnosa između vrednosti dva polja.
* **Opcije**:
* **Jednako (==)**: Proverava da li je vrednost prvog polja jednaka vrednosti drugog polja.
* **Nije jednako (!=)**: Proverava da li je vrednost prvog polja različita od vrednosti drugog polja.
* **Veće od (>)**: Proverava da li je vrednost prvog polja veća od vrednosti drugog polja.
* **Veće od ili jednako (>=)**: Proverava da li je vrednost prvog polja veća od ili jednaka vrednosti drugog polja.
* **Manje od (<)**: Proverava da li je vrednost prvog polja manja od vrednosti drugog polja.
* **Manje od ili jednako (<=)**: Proverava da li je vrednost prvog polja manja od ili jednaka vrednosti drugog polja.

**Funkcionalnost**

* **Izbor polja**: Korisnici unose ili biraju imena dva polja za upoređivanje. Ovo se obično radi putem obrasca ili padajućeg menija unutar podešavanja kartice.
* **Izbor operatora**: Korisnici biraju operatora iz liste dostupnih opcija koji definiše kako će polja biti upoređena.
* **Izvršenje upoređivanja**:
* Sistem čita vrednosti iz navedenih polja i primenjuje izabrani operator kako bi procenio odnos između njih.
* Na osnovu rezultata upoređivanja (tačno ili netačno), mogu se pokrenuti naredne akcije. Na primer, ako upoređivanje ne uspe, sistem može označiti dokument za pregled, blokirati dalju obradu ili obavestiti odgovorne strane.

**Interakcije sa korisnicima**

* **Podešavanje i konfiguracija**: Korisnici konfigurišu upoređivanje unosom imena polja i izborom operatora. Ovo podešavanje treba da bude jednostavno i vođeno, možda sa pomoćnim tekstom ili primerima.
* **Pratnja i izveštavanje**: Sistem može pružiti povratne informacije o rezultatima upoređivanja, kao što su beleženje svih napravljenih upoređivanja, njihovi rezultati i bilo koje akcije preduzete kao odgovor na rezultate upoređivanja.
* **Upravljanje greškama i obaveštenjima**: Korisnici dobijaju upozorenja ako upoređivanje ne može biti izvršeno (na primer, ako jedno od polja nije pronađeno u dokumentu ili nije u uporedivom formatu).

#### Zaključak

Kartica radnog toka "Poređenje polja dokumenata" je od vitalnog značaja za održavanje tačnosti podataka i doslednosti preko dokumenata u ERP sistemu. Pomaže u automatizaciji provera koje bi inače bile ručne, sklonije greškama i vremenski zahtevne, unapređujući efikasnost i pouzdanost u obradi dokumenata. Jasno dokumentovanje ove kartice u priručniku vašeg ERP sistema pomoći će korisnicima da efikasno koriste ovu funkciju, osiguravajući da podaci preko dokumenata ostanu dosledni i u skladu sa poslovnim pravilima.
