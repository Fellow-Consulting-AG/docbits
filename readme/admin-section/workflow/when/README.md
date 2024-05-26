# Kada

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-05-04 um 16.25.45.png" alt=""><figcaption></figcaption></figure>

#### Razumevanje "Kada" u konfiguracijama toka rada

**Svrha "Kada"**

* Odeljak "Kada" u konfiguraciji toka rada definiše uslove okidača koji pokreću određenu radnju toka rada. Ovi uslovi se zasnivaju na određenim kriterijumima koji se odnose na atribute dokumenata ili aktivnosti korisnika unutar ERP sistema.

**Kako funkcioniše**

* Na vašem interfejsu, "Kada" izgleda kao početna tačka gde korisnici mogu odabrati različite kartice okidača. Svaka kartica specificira uslove pod kojima će se izvršiti naredne radnje (definisane u drugom delu konfiguracije toka rada, verovatno označenom kao "Radnja").

**Kartice uslova tipa dokumenta**

* Kartice prikazane na snimku ekrana su varijacije uslova "Tip dokumenta", koje se koriste za pokretanje tokova rada na osnovu tipa dokumenta koji se obrađuje. Evo razbijanja svake vrste kartice uslova:

* **Tip dokumenta (Operator) jedan od (Tip)**: Ova kartica pokreće radnju kada tip dokumenta odgovara jednom od navedenih tipova na listi. Operator može uključivati opcije poput "je" ili "nije", omogućavajući inkluzivne ili ekskluzivne uslove.
* **Tip dokumenta (Operator) (Tip)**: Ova jednostavnija varijanta pokreće se na osnovu jednog uslova tipa dokumenta. Obično će proveriti da li je tip dokumenta "je" ili "nije" određeni tip, bez opcije za odabir više tipova.

#### Postavljanje kartice okidača "Kada"

1. **Izbor tipa uslova**: Korisnici počinju tako što odaberu tip uslova koji je relevantan za tok rada koji žele da automatizuju. U ovom slučaju, fokus su tipovi dokumenata.
2. **Definisanje operatora**: Korisnici moraju odlučiti o logičkom operatoru - poput "je" ili "nije" - koji postavlja osnovu za poređenje stvarnih tipova dokumenata sa definisanim uslovima.
3. **Specifikacija tipova dokumenata**: Zavisno od kartice, korisnici mogu odabrati jedan ili više tipova dokumenata koji će pokrenuti tok rada kada se dokumenti tih tipova obrađuju.
4. **Finalizacija okidača**: Kada se uslov postavi, postaje osnova za pokretanje određenih radnji definisanih u toku rada. Ako dokument ispunjava postavljeni uslov, definisane radnje će automatski biti pokrenute.

#### Praktična primena

U praksi, ove kartice okidača su ključne za automatizaciju procesa poput odobrenja, obaveštenja ili bilo kog postupka koji zavisi od tipa dokumenta koji se obrađuje. Na primer, ako je tip dokumenta "Faktura", i ako odgovara uslovima postavljenim na kartici "Kada", tok rada može automatski proslediti dokument za obradu plaćanja.

Ovaj setup osigurava da tokovi rada ne samo da su efikasni, već su prilagođeni specifičnim operativnim potrebama organizacije, smanjujući ručni nadzor i ubrzavajući procese rukovanja dokumentima.

U suštini, deo "Kada" vaše konfiguracije toka rada se odnosi na postavljanje pozornice za automatske radnje zasnovane na specifičnim, unapred definisanim uslovima. To je moćan alat za osiguravanje da vaš ERP sistem dinamično reaguje na potrebe poslovanja, poboljšavajući produktivnost i tačnost u upravljanju dokumentima.
