# Iznad maksimalnog iznosa

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-05-03 um 14.51.42.png" alt=""><figcaption></figcaption></figure>

Ovaj naslov ukazuje da je pravilo dizajnirano da upravlja slučajevima kada je ukupan iznos fakture veći od maksimalnog iznosa koji je ovlašćeni odobravatelj ovlašćen da obradi.

#### Konfiguracija pravila:

1. **Kada…**
* **Tip dokumenta je Faktura**: Ova uslova osigurava da se pravilo primenjuje samo na fakture, što je ključno za usmeravanje radnog toka na pravilan način.
2. **I…**
* **Status dokumenta je Na čekanju odobrenja**: Faktura mora biti u statusu "Na čekanju odobrenja". Ovaj status je ključan kako bi se osiguralo da se pravilo primenjuje na fakture koje se još uvek obrađuju i nisu još završene.
* **Uporedi dva polja: Ukupan iznos veći od maksimalnog iznosa odobravatelja**: Ovaj uslov proverava da li ukupan iznos fakture prelazi maksimalni iznos koji je odobravatelj ovlašćen da obradi. Ova provera može uključivati i postavljanje tolerancije, što omogućava manje varijacije na osnovu unapred definisanih kriterijuma.

#### Akcija (Onda…):

* **Dodeli korisnika iz polja Sledeći nivo odobravaoca, koristi korisnika kao rezervu**: Ako faktura premaši određeni maksimalni iznos, automatski se dodeljuje odobravaocu višeg nivoa, što je naznačeno poljem 'Sledeći nivo odobravaoca'. Ako ovo polje nije popunjeno ili određeni korisnik nije dostupan, podrazumevani korisnik (verovatno administrator ili drugi određeni član osoblja) se koristi kao rezerva kako bi se osiguralo da se faktura pregleda bez odlaganja.

#### Elementi interfejsa:

* **Dodaj karticu**: Ova opcija omogućava dodavanje dodatnih uslova ili akcija pravilu, pružajući fleksibilnost za rešavanje složenih scenarija.
* **Sačuvaj**: Ovaj dugme čuva konfiguraciju pravila u sistemu.

#### Svrha ovog pravila:

Svrha ovog pravila je da se osigura da se fakture koje premašuju određene finansijske pragove pregledaju od strane odobravatelja sa odgovarajućim nivoima ovlašćenja. Ovo pomaže u održavanju finansijske kontrole i nadzora, osiguravajući da troškovi budu pregledani od strane osoblja sa potrebnim limitima odobrenja, čime se organizacija štiti od neovlašćenih ili neadekvatnih troškova.

Ovo pravilo, kao i prethodno, pomaže u automatizaciji radnog toka, smanjujući ručni rad i poboljšavajući usklađenost sa finansijskim politikama organizacije. To je primer kako se automatizacija radnog toka može efikasno koristiti za upravljanje složenim finansijskim procesima unutar kompanije.
