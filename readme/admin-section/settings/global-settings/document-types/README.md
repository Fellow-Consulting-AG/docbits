# Tipovi dokumenata

{% embed url="https://youtu.be/pFz_6tvNlU4" %}
DocBits Admin Guide: Adding, Editing & Configuring Document Types (Full Walkthrough)
{% endembed %}

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 08.44.19.png" alt=""><figcaption></figcaption></figure>

#### Pregled

Odeljak Tipovi dokumenata navodi sve vrste dokumenata koje prepoznaje i obrađuje Docbits. Administratori mogu upravljati različitim aspektima kao što su izgled, definicije polja, pravila ekstrakcije i još mnogo toga za svaku vrstu dokumenta. Ova prilagođavanja su ključna za osiguravanje tačnog rukovanja podacima i usaglašenosti sa organizacionim standardima.

#### Ključne funkcije i opcije

1. **Lista tipova dokumenata**:
* Svaki red predstavlja tip dokumenta kao što su Faktura, Kreditna nota, Dostavna lista, itd.
* Tipovi dokumenata mogu biti standardni ili prilagođeni, kako je naznačeno oznakama poput "Standardni."
2. **Uređivanje izgleda**: Ova opcija omogućava administratorima da modifikuju postavke izgleda dokumenta, uključujući definisanje kako dokument izgleda i gde se nalaze polja sa podacima.
3. **Podtipovi dokumenata**: Ako neki tipovi dokumenata imaju podkategorije, ova opcija omogućava administratorima da konfigurišu postavke specifične za svaki podtip.
4. **Kolone tabele**: Prilagodite koje kolone podataka treba da se pojave kada se tip dokumenta pregleda u listama ili izveštajima.
5. **Polja**: Upravljajte poljima podataka povezanim sa tipom dokumenta, uključujući dodavanje novih polja ili modifikaciju postojećih.
6. **Obuka modela**: Konfigurišite i obučite model koji se koristi za prepoznavanje i ekstrakciju podataka iz dokumenata. Ovo može uključivati postavljanje parametara za modele mašinskog učenja koji se poboljšavaju vremenom sa više podataka.
7. **Regex**: Postavite redovne izraze koji se koriste za ekstrakciju podataka iz dokumenata na osnovu obrazaca. Ovo je posebno korisno za ekstrakciju strukturisanih podataka.
8. **Skripte**: Pišite ili modifikujte skripte koje pokreću prilagođena pravila obrade ili tokove rada za dokumente ovog tipa.
9. **EDI (Elektronska razmena podataka)**: Konfigurišite postavke koje se odnose na razmenu dokumenata u standardizovanim elektronskim formatima.

{% hint style="info" %}
Pogledajte [Postavljanje tipa dokumenata](../../../setup/document-types/)
{% endhint %}

{% @jira/embed url="https://fellowpro.atlassian.net/browse/DOCB-2489" %}
