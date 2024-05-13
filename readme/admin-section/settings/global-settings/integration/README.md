# Integracija

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 08.39.14.png" alt=""><figcaption></figcaption></figure>

## API ključ

* **Ključ**: Ovo je jedinstveni identifikator koji koriste spoljni programi za pristup API-ju Docbits-a. Ključan je za autentifikaciju zahteva upućenih Docbits-u iz drugog softvera.
* Radnje poput pregleda, regenerisanja ili kopiranja API ključa mogu se obaviti ovde, u zavisnosti od specifičnih potreba i sigurnosnih protokola.

## Podešavanja pružaoca usluge SSO (Single Sign-On)

* **Entitet ID**: Ovo je identifikator za Docbits kao pružaoca usluge u konfiguraciji SSO. Jedinstveno identifikuje Docbits unutar SSO okvira.
* **SLO (Single Logout) URL**: URL na koji se SSO sesije šalju radi istovremenog odjavljivanja sa svih aplikacija povezanih putem SSO.
* **SSO URL**: URL koji se koristi za pokretanje procesa jednokratne prijave.
* Radnje poput "Preuzmi sertifikat" i "Preuzmi metapodatke" dostupne su za dobijanje neophodnih sigurnosnih sertifikata i metapodataka koji se koriste pri postavljanju i održavanju integracije SSO.

{% hint style="info" %}
Pogledajte [Postavljanje SSO](../../../setup/sso-configuration/)
{% endhint %}

## Podešavanja pružaoca usluge identiteta

* **ID zakupca**: Ovo se može koristiti kada Docbits integriše sa cloud uslugama koje zahtevaju identifikator zakupca radi upravljanja podacima i pristupnim konfiguracijama specifičnim za kompaniju koja koristi Docbits.
* **Otpremi fajl**: Omogućava administratoru da otpremi konfiguracione fajlove ili druge neophodne fajlove koji olakšavaju integraciju sa pružaocem identiteta.
* **Konfiguriši**: Dugme za primenu ili ažuriranje podešavanja nakon izvršenih promena ili otpreme novih konfiguracija.

{% @jira/embed url="https://fellowpro.atlassian.net/browse/DOCB-2488" %}
