# Lista uslova statusa dokumenta

<figure><img src="../../../.gitbook/assets/userlmn_e9d6da331deceed4f330358635d6b605.png" alt=""><figcaption></figcaption></figure>

**Svrha**

Ova kartica je dizajnirana da kontroliše radne akcije na osnovu trenutnog statusa dokumenta, koristeći uslovnu logiku da pokrene ili ograniči određene procese. Osigurava da dokumenti prolaze kroz radne tokove samo kada ispunjavaju unapred definisane kriterijume statusa.

**Komponente kartice**

1. **Operator**
* **Opis**: Određuje kako će se status dokumenta procenjivati u odnosu na određeni uslov.
* **Opcije**:
* **je**: Pokreće povezane akcije ako trenutni status dokumenta odgovara jednom od navedenih statusa.
* **nije**: Pokreće akcije ako status dokumenta ne odgovara nijednom od navedenih statusa.
2. **Status ( Lista )**&#x20;
* **Opis**: Navodi specifične statuse sa kojima će se uporediti trenutni status dokumenta.
* **Primeri**: "Greška", "Greška pri izvozu", "Spreman za validaciju", "Spreman za pregled", "Na čekanju odobrenja", "Na čekanju drugog odobrenja". Ovi predstavljaju različite faze ili uslove u kojima se dokument može nalaziti unutar procesa radnog toka.

**Funkcionalnost**

* **Identifikacija statusa**: Automatski identifikuje trenutni status dokumenta dok se kreće kroz radni tok sistema ERP.
* **Procena uslova**: Primenjuje izabrani operator (je ili nije) na status dokumenta u poređenju sa navedenim statusima:
* Ako je **je**, proverava da li status dokumenta odgovara bilo kom statusu na listi.
* Ako je **nije**, proverava da li status dokumenta ne postoji na listi.
* **Izvršenje akcija**: Zavisno od ishoda procene uslova:
* **Tačno**: Izvršava unapred definisane akcije ili radne tokove ako je uslov ispunjen.
* **Netačno**: Preskače ili pokreće alternativne radne tokove ako uslov nije ispunjen.
* **Integracija radnog toka**: Seamlessly se integriše sa drugim komponentama radnog toka, osiguravajući da se rukovanje dokumentima koordinira širom sistema.

**Interakcije sa korisnicima**

* **Postavljanje i konfiguracija**: Korisnici podešavaju karticu biranjem operatora i specificiranjem relevantnih statusa. Ovo podešavanje može uključivati jednostavne padajuće menije ili polja za potvrdu za biranje statusa i operatora.
* **Pracenje i upravljanje**: Korisnici mogu pratiti aktivnost kartice putem kontrolne table, koja pruža uvide u uslove statusa koji se prate i akcije koje se preduzimaju na osnovu tih uslova.
* **Upravljanje greškama i upozorenjima**: Podržava postavljanje upozorenja za neuspehe procesa ili neslaganja u očekivanim statusima dokumenata, omogućavajući brze odgovore na operativne probleme.

#### Zaključak

Radna kartica "Uslov statusa dokumenta" je od vitalnog značaja za osiguravanje da dokumenti budu obrađeni ispravno prema njihovom trenutnom statusu, unapređujući kontrolu i efikasnost unutar sistema ERP. Jasno dokumentovanje ove kartice u priručniku sistema pomoći će korisnicima da je efikasno implementiraju i upravljaju njome, iskorišćavajući njenu funkcionalnost za održavanje glatkih i usklađenih radnih tokova dokumenata. Ova kartica je posebno korisna za upravljanje životnim ciklusima dokumenata i osiguravanje da samo dokumenti koji ispunjavaju određene kriterijume napreduju ka narednim fazama poslovnih procesa.
