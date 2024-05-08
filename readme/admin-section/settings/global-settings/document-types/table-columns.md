# Tabelarni Stubovi

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 08.57.49.png" alt=""><figcaption></figcaption></figure>

#### Pregled

Interfejs Tabelarnih Stubova u DocBits-u koristi se za specificiranje stubova koji se pojavljuju u tabelama podataka za svaki tip dokumenta. Svaki stub može biti konfigurisan da drži specifične tipove podataka, kao što su stringovi ili numeričke vrednosti, i može biti ključan za sortiranje, filtriranje i funkcije izveštavanja unutar DocBits-a.

#### Ključne Funkcije i Opcije

1. **Konfiguracija Stubova**:
* **Ime Stubova**: Identifikator za stub u bazi podataka.
* **Naslov**: Čitljiv naslov za stub koji će se pojaviti u interfejsu.
* **Tip Stubova**: Definiše tip podataka stuba (npr. STRING, IZNOS), što određuje kakav tip podataka može biti smešten u stubu.
* **Ime Tabele**: Označava kojoj tabeli stub pripada, povezujući ga sa određenim tipom dokumenta poput INVOICE\_TABLE.
2. **Radnje**:
* **Izmeni**: Modifikuj postavke postojećeg stuba.
* **Obriši**: Ukloni stub iz tabele, što je korisno ako podaci više nisu potrebni ili ako se struktura podataka tipa dokumenta promeni.
3. **Dodavanje Novih Stubova i Tabela**:
* **Dodaj Novi Stub Tabele**: Otvara dijalog gde možete definisati novi stub, uključujući njegovo ime, da li je obavezan, njegov tip podataka i tabelu kojoj pripada.
* **Kreiraj Novu Tabelu**: Omogućava kreiranje nove tabele, definišući jedinstveno ime koje će se koristiti za čuvanje podataka povezanih sa određenim setom tipova dokumenata.

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 08.58.01.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 08.58.11.png" alt=""><figcaption></figcaption></figure>

Ova sekcija je od vitalnog značaja za održavanje strukturalne celovitosti i upotrebljivosti podataka unutar sistema DocBits, osiguravajući da podaci izdvojeni iz dokumenata budu smešteni na organizovan i pristupačan način.

{% @jira/embed url="https://fellowpro.atlassian.net/browse/DOCB-2493" %}
