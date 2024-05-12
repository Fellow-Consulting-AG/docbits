# Upravljač rasporedom

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 08.46.24.png" alt=""><figcaption></figcaption></figure>

#### Pregled

Upravljač rasporedom omogućava administratorima da vizuelno konfigurišu i modifikuju raspored tipova dokumenata postavljanjem svojstava za različita polja podataka i grupe unutar dokumenta. Ovo sučelje pomaže u osiguravanju da se modeli ekstrakcije i ručni unos podataka precizno podudaraju sa strukturom dokumenta skeniranog ili otpremljenog u DocBits.

#### Ključni komponenti

1. **Grupe i Polja**:
* **Grupe**: Organizacione jedinice unutar tipa dokumenta koje kategorizuju povezana polja (npr. Detalji fakture, Detalji plaćanja). Ove grupe se mogu proširiti ili skupiti i rasporediti tako da odražavaju logičko grupisanje u stvarnom dokumentu.
* **Polja**: Individualne tačke podataka unutar svake grupe (npr. Broj fakture, Uslovi plaćanja). Svako polje može biti prilagođeno za način na koji se podaci prikupljaju, prikazuju i obrađuju.
2. **Panel svojstava**:
* Ovaj panel prikazuje svojstva odabranog polja ili grupe, omogućavajući detaljnu konfiguraciju, kao što su:
* **Oznaka**: Vidljiva oznaka za polje u korisničkom interfejsu.
* **Naziv polja**: Tehnički identifikator korišćen unutar sistema.
* **Širina elementa u procentima**: Određuje širinu polja u odnosu na raspored dokumenta.
* **Tab indeks**: Kontroliše redosled tabiranja za navigaciju.
* **Pokreni skriptu pri promeni**: Da li izvršiti skriptu kada se vrednost polja promeni.
* **Prikaži oznaku levo**: Da li se oznaka prikazuje sa leve strane polja ili iznad njega.
* **Je tekstualno polje**: Specificira da li polje treba da bude tekstualno polje, prilagođavajući veće količine teksta.
* **Izaberi tip modela**: Opcija za izbor modela koji će obraditi ekstrakciju ovog polja.
* **Dužina polja**: Maksimalna dužina podataka koji će biti prihvaćeni u ovom polju.
* **Zabranjene ključne reči**: Ključne reči koje nisu dozvoljene unutar polja.
3. **Pregled šablona**:
* Prikazuje trenutni pregled kako će dokument izgledati na osnovu trenutne konfiguracije rasporeda. Ovo pomaže u osiguravanju da raspored odgovara stvarnoj strukturi dokumenta i od vitalnog je značaja za testiranje i usavršavanje postavke obrade dokumenata.

{% @jira/embed url="https://fellowpro.atlassian.net/browse/DOCB-2490" %}
