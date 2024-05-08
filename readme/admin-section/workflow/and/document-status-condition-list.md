# Lista stanja dokumenta

<figure><img src="../../../.gitbook/assets/userlmn_e9d6da331deceed4f330358635d6b605.png" alt=""><figcaption></figcaption></figure>

**Svrha**

Ova kartica je dizajnirana da kontroliše radne akcije na osnovu trenutnog stanja dokumenta, koristeći uslovnu logiku da ili pokrene ili ograniči određene procese. Osigurava da dokumenti prolaze kroz tokove rada samo kada ispune unapred definisane kriterijume stanja.

**Komponente kartice**

1. **Operator**
* **Opis**: Određuje kako će se stanje dokumenta procenjivati u odnosu na određeni uslov.
* **Opcije**:
* **je**: Pokreće povezane akcije ako trenutno stanje dokumenta odgovara jednom od navedenih stanja.
* **nije**: Pokreće akcije ako stanje dokumenta ne odgovara nijednom od navedenih stanja.
2. **Status ( Lista )**&#x20;
* **Opis**: Navodi specifična stanja sa kojima će se uporediti trenutno stanje dokumenta.
* **Primeri**: "Greška", "Greška pri izvozu", "Spreman za validaciju", "Spreman za pregled", "Na čekanju odobrenja", "Na čekanju drugog odobrenja". Ova stanja predstavljaju različite faze ili uslove u kojima se dokument može nalaziti unutar procesa toka rada.

**Funkcionalnost**

* **Identifikacija stanja**: Automatski identifikuje trenutno stanje dokumenta dok se kreće kroz tok rada sistema za planiranje resursa preduzeća (ERP).
* **Procena uslova**: Primenjuje izabrani operator (je ili nije) na stanje dokumenta u poređenju sa navedenim stanjima:
* Ako je **je**, proverava da li stanje dokumenta odgovara bilo kom stanju na listi.
* Ako je **nije**, proverava da li se stanje dokumenta ne pojavljuje na listi.
* **Izvršenje akcija**: Zavisno od ishoda procene uslova:
* **Tačno**: Izvršava unapred definisane akcije ili tokove rada ako je uslov ispunjen.
* **Netačno**: Preskače ili pokreće alternativne tokove rada ako uslov nije ispunjen.
* **Integracija toka rada**: Seamlessly se integriše sa drugim komponentama toka rada, osiguravajući da se rukovanje dokumentima koordinira širom sistema.

**Interakcije sa korisnicima**

* **Postavljanje i konfiguracija**: Korisnici podešavaju karticu biranjem operatora i specificiranjem relevantnih stanja. Ovo podešavanje može uključivati jednostavne padajuće menije ili polja za potvrdu za biranje stanja i operatora.
* **Pratnja i upravljanje**: Korisnici mogu pratiti aktivnost kartice putem kontrolne table, koja pruža uvide u stanja koja se prate i akcije koje se preduzimaju na osnovu tih stanja.
* **Upravljanje greškama i upozorenjima**: Podržava postavljanje upozorenja za neuspehe procesa ili neslaganja sa očekivanim stanjima dokumenata, omogućavajući brze odgovore na operativne probleme.

#### Zaključak

Kartica toka rada "Uslov stanja dokumenta" je od vitalnog značaja za osiguravanje da se dokumenti pravilno obrađuju prema njihovom trenutnom stanju, unapređujući kontrolu i efikasnost unutar sistema za planiranje resursa preduzeća (ERP). Jasno dokumentovanje ove kartice u priručniku sistema pomoći će korisnicima da je efikasno implementiraju i upravljaju njome, iskorišćavajući njenu funkcionalnost za održavanje glatkih i usklađenih tokova dokumenata. Ova kartica je posebno korisna za upravljanje životnim ciklusima dokumenata i osiguravanje da samo dokumenti koji ispunjavaju određene kriterijume napreduju ka narednim fazama poslovnih procesa.
