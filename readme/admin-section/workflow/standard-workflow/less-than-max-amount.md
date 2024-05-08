# Manje od maksimalnog iznosa

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-05-03 um 14.48.55.png" alt=""><figcaption></figcaption></figure>

Ovaj naslov sugeriše da je pravilo ili uslov koji se postavlja dizajniran da obradi fakture čiji je ukupan iznos manji ili jednak određenom maksimalnom iznosu.

#### Konfiguracija pravila:

1. **Kada…**
* **Tip dokumenta je Faktura**: Ovaj uslov proverava da li je dokument koji se obrađuje faktura. To je ključno kako bi se osiguralo da se pravilo primenjuje samo na fakture, a ne na druge vrste dokumenata.
2. **I…**
* **Status dokumenta je Na čekanju odobrenja**: Ovo navodi da faktura mora biti u statusu "Na čekanju odobrenja". Ova provera statusa osigurava da se pravilo primenjuje samo na fakture koje čekaju odobrenje.
* **Uporedi dva polja: Ukupan iznos Manje ili Jednako Maksimalnom iznosu odobravača**: Ovaj uslov upoređuje ukupan iznos fakture sa maksimalnim ovlašćenim iznosom odobravača. Ako je ukupan iznos fakture manji ili jednak ovom maksimalnom iznosu, pravilo nastavlja na sledeći korak. Verovatno uključuje nivo tolerancije koji dozvoljava manje odstupanja unutar određenih granica.

#### Akcija (Onda…):

* **Dodeli korisnika iz polja Ime odobravača, koristi korisnika Korisnik kao rezervu**: Ako su ispunjeni navedeni uslovi, faktura se automatski dodeljuje odobravaču čije je ime navedeno u polju. Ako je ovo polje prazno ili nedostupno, podrazumevani korisnik (verovatno administrator ili drugi određeni član osoblja) se dodeljuje kao rezerva za obradu odobrenja.

#### Elementi interfejsa:

* **Dodaj karticu**: Ovaj dugme verovatno omogućava korisnicima da dodaju više uslova ili akcija pravilu, poboljšavajući fleksibilnost i specifičnost radnog toka.
* **Sačuvaj**: Čuva konfigurisano pravilo u sistemu.

#### Svrha ovog pravila:

Ova postavka je dizajnirana da pojednostavi proces odobravanja faktura automatskim usmeravanjem faktura odgovarajućem odobravaču na osnovu iznosa i osigurava da se samo one unutar određenog praga obrađuju na ovaj automatizovan način. Pomaže u upravljanju finansijskim kontrolama i ubrzava radni tok smanjenjem ručnih provera za svaku fakturu.
