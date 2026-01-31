# ZUGFeRD konfiguracija

{% embed url="https://youtu.be/AxrHNEmmXtg" %}
DocBits tutorijal za e-fakture: Obrada XRechnung / ZUGFeRD (Factur-X), validacija podataka i automatizacija radnih tokova
{% endembed %}

## **Podržane verzije ZUGFeRD-a**

DocBits podržava sve glavne verzije ZUGFeRD-a, uključujući:

* **1.0**
* **2.0**
* **2.1** (usklađen sa FACTUR-X 1.0.05)
* **2.2**
* **2.3** (usklađen sa FACTUR-X 1.07.2)
* **2.3.2**

#### Standardna aktivacija i modifikacija

ZUGFeRD standard je uvek aktivan po podrazumevanim postavkama, ali možete izvršiti izmene ako je potrebno.

### **Koraci za izmenu ZUGFeRD postavki:**

1. Idite na **Settings → Global Settings → Document Types → Invoice**.
2. Kliknite na **E-Doc**.

    <figure><img src="../../../../../.gitbook/assets/zugferd_1.png" alt=""><figcaption></figcaption></figure>
3. Pojaviće se lista svih dostupnih e-dokumenata.
4. Pronađite **ZUGFeRD** verziju koju želite da izmenite.

    <figure><img src="../../../../../.gitbook/assets/zugferd_2.png" alt=""><figcaption></figcaption></figure>

## **Konfiguracija transformacije i XML putanje:**

U **postavkama transformacije** možete definisati putanju za lociranje specifičnih informacija unutar XML datoteke i sačuvati ih u novoj strukturi, što olakšava pristup podacima.
<mark style="color:red;">**Napomena**</mark>: Ako koristite ovu funkcionalnost, morate koristiti novokreirane XML putanje, a ne originalne XML putanje, u **Preview** i **Extraction Path**.

### **Koraci za izmenu datoteke transformacije:**

1. Otvorite **Transformation**.
2. Kreirajte novi nacrt klikom na **ikonu olovke**.
3. Izaberite novokreirani nacrt.
4. Ili kreirajte novo polje ili izmenite postojeće.
5. Postavite željenu putanju za ekstrakciju podataka.
6. Kliknite na **Save**.

### Važne napomene:

* **Preview datoteka** se koristi samo za **FACTUR-X**, a ne za **ZUGFeRD**. ZUGFeRD će koristiti originalni **PDF**.

## Konfiguracija Preview PDF-a

**Preview PDF konfiguracija** se koristi za generisanje verzije dokumenta čitljive za korisnika. Možete je prilagoditi pomoću HTML-a kako bi odgovarala vašim potrebama.

### **Koraci za izmenu Preview datoteke:**

1. Otvorite **Preview**.
2. Kreirajte novi nacrt klikom na **ikonu olovke**.
3. Izaberite novokreirani nacrt.
4. Ili kreirajte novo polje ili izmenite postojeće.
5. Postavite željenu putanju za ekstrakciju podataka.
6. Kliknite na **Save**.

## Konfiguracija putanja ekstrakcije

**Konfiguracija putanja ekstrakcije** se koristi za izvlačenje podataka i popunjavanje polja na **ekranu za validaciju**, kao što su tabela faktura ili polja konfigurisana u rasporedu fakture.

### **Koraci za izmenu** **putanja ekstrakcije**:

1. Otvorite **Extraction Paths**.
2. Kreirajte novi nacrt klikom na **ikonu olovke**.
3. Izaberite novokreirani nacrt.
4. Kreirajte novo polje ili izmenite postojeće.
5. Leva strana predstavlja **DocBits ID polja**, koji se može naći u **Settings → Global Settings → Document Types → Invoice → Fields**.

    <figure><img src="../../../../../.gitbook/assets/zugferd_3.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/zugferd_4.png" alt=""><figcaption></figcaption></figure>
6. Desna strana predstavlja **putanju do polja** kreiranu u Transformaciji.
7. Kliknite na **Save**.

Prateći ove korake, možete osigurati tačnu ekstrakciju podataka i validaciju za ZUGFeRD fakture.
