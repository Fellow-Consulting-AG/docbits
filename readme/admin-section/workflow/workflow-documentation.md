# Dokumentacija o radnom toku

**Dokumentacija o radnom toku**

Da biste imali pregled, možete dodijeliti različite naslove radnim tokovima kako biste odmah znali o kojem zadatku se radi.

Kreirajte novi radni tok: Kliknite na + DODAJ RADNI TOK

![](<../../.gitbook/assets/0 (1).png>)

Možete koristiti ove radne tokove (Test 1,2,3) da automatski dodijelite različite dokumente odgovarajućem zaposlenom u kompaniji.

![](<../../.gitbook/assets/1 (1).png>)

Ako račun ili drugi dokument premašuje određeni ukupni iznos koji zahteva prethodni pregled i odobrenje, ti dokumenti mogu odmah biti dodijeljeni odgovarajućoj osobi.

<figure><img src="../../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

**Test 1:              Logička kartica**

Kada:             **Zaduženi je:**                    Amier Haider

I:                **Tip dokumenta je:**        Račun

Onda:              **Dodijeli dokument:**   Stefan Reppermund

![](<../../.gitbook/assets/3 (1).png>)

**Test 2:              Logička kartica**

Kada:              **Zaduženi je:**                    Amier Haider

I:                 **Tip dokumenta je:**        Dostavna lista

Onda:               **Dodijeli dokument:**   James Edwards

![](<../../.gitbook/assets/4 (1).png>)

**Test 3:             Logička kartica**

**Kada:**             **Zaduženi je:**                    Amier Haider

**I:**                **Tip dokumenta je:**        Potvrda o narudžbini

**Onda:**              **Dodijeli dokument:**   Anian Sollinger

![](<../../.gitbook/assets/5 (1).png>)

Takođe je moguće, ako dokument nije dodijeljen jednoj osobi, dodijeliti ga određenom zaposlenom od početka.

<figure><img src="../../.gitbook/assets/image (25).png" alt="" width="375"><figcaption></figcaption></figure>

Za lakši pregled onoga što treba da se desi sa dokumentom, možete postaviti status za dolazne dokumente u ovom radnom toku. Ovaj radni tok omogućava da odmah vidite da li postoji, na primer, odobrenje u toku.

**Test 4:             Logička kartica**

**Kada:**             **Tip dokumenta je:**         Dostavna lista

**I:**                **Zaduženi je:**                     Amier Haider

**Onda:**              **Promeni status u:**         Na čekanju odobrenja

<figure><img src="../../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

![](<../../.gitbook/assets/8 (1).png>)

**Test 5:                Logička kartica**

Kada:                **Tip dokumenta je:**           Račun

I:                   **Zaduženi je:**                       Stefan Reppermund

Onda:                 **Promeni status u:**           Na čekanju drugog odobrenja

<figure><img src="../../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

![](<../../.gitbook/assets/10 (1).png>)

Ako račun ili drugi dokument premašuje određeni ukupni iznos koji zahteva prethodni pregled i odobrenje, ti dokumenti mogu biti odmah dodijeljeni odgovarajućoj osobi.

![](<../../.gitbook/assets/11 (1).png>)

**Test 6:                    Logička kartica**

Kada:                   **Zaduženi je:**                   Amier Haider

I:                      Polje dokumenta        **ukupan_iznos**     je      **Veći od       500**

Onda:                    **Dodijeli dokument:**   Asad Usman Khan

<figure><img src="../../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

![](<../../.gitbook/assets/13 (1).png>)

Takođe je moguće uneti status u radni tok, tako da dodijeljena osoba odmah može videti koji je status ovog dokumenta i šta treba da se desi sa njim.

**Test 7:                 Logička kartica**

**Kada:** **Zaduženi je:**                     Amier Haider

**I:**                   Polje dokumenta           **ukupan_iznos**      je        **Veći od      500**

**Onda:**                 **Dodijeli dokument:**     Asad Usman Khan

&#x20;                            **Promeni status u:**          Na čekanju odobrenja

<figure><img src="../../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/15 (1).png" alt=""><figcaption></figcaption></figure>

Na primer, ako nedostaju određene ili važne informacije u dokumentu, ali su važne i moraju biti uključene za dalju obradu, možete postaviti radni tok tako da se ti dokumenti odmah proslede kupcu i zamenskom licu.

<figure><img src="../../.gitbook/assets/image (10).png" alt=""><figcaption></figcaption></figure>

**Test 9:**

Radni tok sa ovim logičkim karticama dizajniran je da automatski proveri da li količina, jedinična cena ili popust navedeni u potvrdi o narudžbini odgovaraju odgovarajućim ciframa u narudžbenici. Ova provera osigurava doslednost i tačnost između onoga što je naručeno i onoga što dobavljač potvrđuje da će isporučiti.

Možete dati ovim dokumentima određeni status ili ih dodijeliti određenom zaposlenom.

<div align="center">

<figure><img src="../../.gitbook/assets/image (12).png" alt=""><figcaption></figcaption></figure>

</div>

<figure><img src="../../.gitbook/assets/image (16).png" alt=""><figcaption></figcaption></figure>

**Logička kartica: Podudaranje količine ili jedinične cene ili popusta**

Ova logička kartica je dizajnirana da automatski proveri da li količina, jedinična cena ili popust navedeni u potvrdi o narudžbini odgovaraju odgovarajućim ciframa u narudžbenici. Ova provera osigurava doslednost i tačnost između onoga što je naručeno i onoga što dobavljač potvrđuje da će isporučiti.



**Uslov okidača**

Logika se aktivira kada se ispunjava bilo koji od sledećih uslova u potvrdi o narudžbini u odnosu na originalnu narudžbenicu:

* **Količina**: Količina naručenih stavki odgovara količini potvrđenoj od strane dobavljača.
* **Jedinična cena**: Cena po dogovorenom artiklu odgovara potvrdi dobavljača.
* **Popust**: Bilo koji primenjeni popusti su dosledni između narudžbenice i potvrde o narudžbini.



* **Definišite parametre poređenja**: Postavite specifična polja (količina, jedinična cena, popust) koje će logička kartica proveriti da li se podudaraju.
* **Automatizujte verifikaciju**: Konfigurišite sistem da automatski uporedi ove detalje po prijemu potvrde o narudžbini.
* **Prilagodite upozorenja**: Odlučite o radnom toku za rukovanje neslaganjima, uključujući prilagođavanje upozorenja za ručni pregled.

Ova logička kartica je od vitalnog značaja za osiguravanje da detalji potvrde o narudžbini odgovaraju originalnoj narudžbenici, čime se čuva integritet ciklusa nabavke.



**Test 10:**

Ako imate drugačiji proračun za dodatne troškove, ili ih imate samo na nekim stavkama, možete koristiti generičke kartice za proračun tabele, neke od njih takođe omogućavaju filtriranje za redovne izraze.

<figure><img src="../../.gitbook/assets/19 (1).png" alt=""><figcaption></figcaption></figure>

Prikazan je primer proračuna za MTZ sa filterom za brojeve stavki koji počinju sa 01, 06, 9, 001 ili 000.



Sa ručnim podešavanjem preporučuje se razdvajanje proračuna koji zavise od novih kolona u zaseban radni tok. Za nastavak proračuna možete koristiti karticu Pokreni radni tok.

**Pokreni radni tok**

<figure><img src="../../.gitbook/assets/20 (1).png" alt=""><figcaption></figcaption></figure>

Ovom karticom možete odrediti ime radnog toka koji će se pokrenuti nakon trenutnog radnog toka ako se ispune njegovi uslovi i nakon prethodnih zatim kartica trenutnog radnog toka. Iako daje prednost pokretljivim, aktivnim radnim tokovima, takođe vam omogućava da pokrenete deaktivirane radne tokove ako dokument ispunjava uslove radnih tokova.
### **Dodavanje izračunatih nadoknada u postojeću kolonu** <a href="#pekg4i18rshn" id="pekg4i18rshn"></a>

<figure><img src="https://lh7-us.googleusercontent.com/XYY1xsFpp7_-Bi0WOSbotiVzspDLdaufx_xgoopMHmxdZnSDhroLpb0AE_si5PhwMq1jHfndc9FwOte9MOoCoTP5_JUYawO5cr4uIctIDHmwVjz3KacQrLJd8iBQy5KY4N-dMaWEi3IeTcc5OBRNJk4" alt=""><figcaption></figcaption></figure>

Ako želite da dodate sve nadoknade kao negativan popust u kolonu popusta, možete koristiti karticu za izračunavanje. Mogu postojati unosi u ovoj koloni, možete je postaviti kao jednu od promenljivih na kartici, imati MTZ oduzet od nje i dodati rezultat nazad u ovu kolonu. U slučaju praznih polja (samo nadoknade za neke stavke), pretpostaviće se 0 za njihovo izračunavanje.

**Obavestite korisnika da autorizuje potvrdu porudžbine u DocBits-u**

Nakon izračunavanja nadoknada, možda ćete želeti da obavestite određenog korisnika da autorizuje potvrdu porudžbine. Za to možete koristiti karticu za obaveštenja

<figure><img src="../../.gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>

Zavisno od podešavanja, korisniku se dodeljuje nova zadatak u DocBits-u i opciono se šalje e-pošta kako bi ih obavestila o njihovom novom zadatku.
