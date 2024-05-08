# Konfiguracija SSO

## Preduslovi

| Potrebne informacije           | Opis                                                                                                                                       |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Detalji za prijavljivanje u oblaku         | Kredencijali su obavezni za pristup Infor Cloud okruženju. Korisnik treba imati uloge "Infor-SystemAdministrator" i "UserAdmin".  |
| Detalji za konfiguraciju administratora (DocBits) | Trebalo bi da ste primili e-poštu od kompanije FellowPro AG sa detaljima za prijavljivanje na stranicu za podešavanje DocBits SSO. Potrebni su vam korisničko ime i lozinka. |
| Sertifikat                    | Možete preuzeti sertifikat u DocBits-u pod SSO postavkama pružaoca usluge                                                                   |

## Pristupite oblaku i proverite svoj pristup

URL počinje sa https://mingle-portal.eu1.inforcloudsuite.com/\<TENANT\_NAME> praćeno vašim ličnim proširenjem

![](https://lh7-us.googleusercontent.com/bLBEM2KCtSiztzy3htdtA8hpnR9J616ecGXPVYZIn-r\_m1tHkLeC8SJZJobl8Hu-Xju4WR7BanVq6NClf9hvbp5qXpjLVHaO9thfmE6-2ITJrlIZzv6OyG93KVhmOsdt6xiEoNrfJO8PwUFRDBblMT4)

Izaberite opciju Cloud Identities i koristite svoje podatke za prijavljivanje

![](https://lh7-us.googleusercontent.com/aF9VyjY-cuTx5NZ9GdnyOQjZmegW9Hp5r7-8AY8SJb1Lj-\_saFTwju49KKqltxXt3ZevQ1Yr47MRQA0UdXkXeb2TnactKpxC5YV3eqkyZiYJVx-cVkolYfwuJElPEgiYMrRQSeSb5fALoUQehxQUh\_0)

Nakon prijave imaćete pristup Infor oblaku. U ovom slučaju ulazimo na ovu stranicu, ali u meniju sa hamburgerom pronaći ćete pristup svim aplikacijama.

![](https://lh7-us.googleusercontent.com/rUfjNI7DIYDw\_sm-KWcGaU\_xGWRZesRkyoYB\_00gOe6OUVAeFXL4UvlKWdtuz771fElXi4fC9NWahRQVLGAxAL6alR5K8edHcOdpdxu-PPfGO7O9exx61NyL4KTqNrt2AofIcnkbWyjf2EGeytPKTdA)

![](https://lh7-us.googleusercontent.com/low1Mq1NxL-Fzo72m-Wy8RPaooMuuQHBdA7rMFVcl7Ps\_G284L2Ze-BjEGy2bM7gcbeWBNeMm6yU8taNCUXgSzb9OcRWRFhQACzsg90XxmxhIfXanKz\_y8tqB4qv8I3W6HIj7SB84NzqK0IJ6UAcYbs)

## Otvorite Upravljanje korisnicima za dodavanje novog pružaoca usluga

Na desnoj strani trake menija, pronaći ćete korisnički meni i tamo možete pristupiti upravljanju korisnicima

![](https://lh7-us.googleusercontent.com/4SvG9pBCyZxBc-kUzwGarIdJkL4S-3bbFnxdfEQoAczOY7abTN72-MYDZ7TtIMqpvAkgsrpM\_Fz2sud5M84r8PrAXkEZHJuhIAAHCCpxqKwkmmfFVnCxiU-iLLBeAlEANp05j\_3kznyOGYqOgs1e1fo)

Zatim treba da izaberete u meniju sa leve strane opciju Security Administration i Service Provider.

![](https://lh7-us.googleusercontent.com/F2dwiMbEqSF8XkZz5JvuOOOjs6MoxIqUAyj3gU6QasaGEUPuPiR\_ANQuJ6wrZjnl1LWNRh2aBBvLvXNp85yfpTjnJP6cLbNoEfcjTbbDyrGfEciYu39jXwcBral6Q70IKkIvzANbJN1WjIonpDzPZQ0)

Videćete ovaj prozor sa pružaocima usluga.

![](https://lh7-us.googleusercontent.com/BBANp\_qDLF8qBKXErAc65893Ya954hqNzg2U8xK-oZCXiSqr\_pboGzuLLW7cCeDjjpCzJn1Zkzc5B4IAI-NOCA\_E5EVW47AWixVGRDUkJ4NGuqAAXYM2UDmIWgi2DggfPkE2CaX0Da7CPGBNrDbe9Yo)

Sada kliknite na znak "+" i dodajte naš DocBits kao pružaoca usluga.&#x20;

![](https://lh7-us.googleusercontent.com/Ksq7zDLEy0AZ3CfobBG8ua2QXsec10nJ3UAed-LXsziZs4VVzxdydmWzP4lBgIOkfQmiCSQo4Q-773wRbsGLyvk2UG4Mj34HeyiSyRAAET7Ojr8mJFZENfAszSViM-QPpcC3AIEFOQuKWYfN0-jOsHY)

## Pristupite SSO POSTAVKAMA PRUŽAOCA USLUGE u DocBits-u

* Prijavite se na URL https://app.docbits.com/ sa podacima za prijavljivanje koje ste dobili od nas.
* Idite na SETTINGS (na vrhu trake) i izaberite INTEGRATION, pod SSO Service Provider Settings pronaći ćete sve informacije potrebne za sledeće korake.
* Preuzmite sertifikat

![](https://lh7-us.googleusercontent.com/R9VSArrCuGWySeSTYBCLHXybVdvbx37TiviLKFvgNZVfaGXITpxoNkIY4JUMuaROZ1f9BYmqfhhq5YYdRbIz5aJaLGAt7oOxZ5m47MAzgUacP-STjdEHzcy1zjgq22YUh4UrqiTrzC969upxt1qDFxs)

Popunite pružaoca usluga uz pomoć SSO Service Provider Settings u DocBits-u&#x20;

![](https://lh7-us.googleusercontent.com/ATCza1efYWKWr7MfDZfa3WbK1r88L9U91fKs319lTh\_QZxyJEp5WLjjCuOqwqnA6Li-h3\_KmRzaxVujbhqTn4Xq6eHAaeAt3K5Whg4KuLPlgTHAuCU02YXaOqhPNBAWSERRwCCmuXQDknoTPosNlDgA)

| Polje                      | Vrednost                                                                                      |
| -------------------------- | ------------------------------------------------------------------------------------------ |
| Tip aplikacije           | DEFAULT\_SAML                                                                              |
| Prikazano ime               | DocBits                                                                                    |
| Identitet entiteta                  | Pogledajte Identitet entiteta pod SSO SERVICE SETTINGS                                                   |
| SSO krajnja tačka               | Kopirajte SSO URL iz SSO SERVICE SETTINGS i zalepite ga u polje SSO krajnja tačka.         |
| Sertifikat za potpisivanje        | Učitajte odgovarajući .cer fajl koji ste preuzeli u koraku 3c) iz SSO SERVICE SETTINGS |
| Format i mapiranje ID-a imena | adresa e-pošte                                                                              |

![](https://lh7-us.googleusercontent.com/YfEUu3X34cjKrPKTLybMvRn-6rKS5aSWGoJLria08yYFZYyidnnVQKRJgzVgudPVPk8k9xWwUpzQyGi2peHFxY8UsQvXV-2twH9G-8IiFSRfoCk5eQUnoplNrttNYNYKUDjs7ckFw0BVYpzGz26Htxs)

* Kada popunite sve, ne zaboravite da sačuvate klikom na ikonu diska iznad Tipa aplikacije
* Ponovo unesite pružaoca usluga DocBits.
* Kliknite na pregled informacija o pružaocu identiteta ispod.

![](https://lh7-us.googleusercontent.com/ajA6zmOcJCNOHJM\_2fUMaObnOGzTLmjUHhOm5QfR7inIfhavc0YywcyUHalVY22ay5rG\_JtcTbUVUX7ZIn7GOPecylljFLdhrQg-JzOZ3Vcav8FM0ZdjT82otfdNYMFyPT3W3ZZuXpKJ1gUcvyx70jU)
![](https://lh7-us.googleusercontent.com/7VPP4izI8E5idcQOA3zRhCOCB5L9uZuylVcMhToiHUI3qk_fCE4n30D-ccYO3OAvAjIrrhJ-AApNMJ7tQO3DmtP3TS5n5r15YUgf_FzBCdL77a_wcAIE0zS2VjKLPB2iPaxOokPHk9G5NW86MV6sZUI)

## Izvezi SAML METADATA.

Datoteka izgleda ovako: ServiceProviderSAMLMetadata_10_20_2021.xml

Uvezi SAML METADATA u podešavanjima SSO.

Idite na PODEŠAVANJA PONUĐAČA IDENTITETA, koji se nalazi pod INTEGRACIJAMA u PODEŠAVANJIMA. Unesite svoj ID zakupca (npr. FELLOWPRO_DEV) i ispod te linije videćete dugme za otpremanje datoteke i dugme UVOZ, gde treba da otpremite prethodno izveštenu datoteku SAML METADATA.

* Kliknite na UVOZ, a zatim izaberite METADATA datoteku koju ste već preuzeli iz PODEŠAVANJA PONUĐAČA USLUGA SSO
* Kliknite na KONFIGURIŠI

![](https://lh7-us.googleusercontent.com/7-v_YNgl_29WrK2lE62nEfIRQ3R5KVmOL_PeR8_ZxS8LNxHSVpHuKcNwDAmaSGTNepi0Izg64T3l3FY6XUSMZCVB-kyV3cbf0DtI-9GnspkrSibmRW3Dx2ESxZeyrkseRYRKdnmUn-GR4fmh8gUx_Rg)

## Dodaj novu aplikaciju u INFOR Ming.le

Idite na Administrativna podešavanja

![](https://lh7-us.googleusercontent.com/D5shQ6CN5YAbGM_0Gr6Hf7-nOlAkTXMyOSr1DntZv8NMSg-mxT5ckp2uIxpHkt4WRQGwCcpIBip9D4Q7_Z590oRQOlg36lu9Y_gq0VxHojNu8ma_3tvtYzrBlZVJJdrXPoib9cvizawCBxGaQlvZ4x8)

Kliknite na DODAJ APLIKACIJU u gornjem desnom uglu

![](https://lh7-us.googleusercontent.com/l1JjP7c7Y9Echd_xx9gEoG7zD-U9wLv-0DNpHtdycXco--1urpcmObRhW4mYngaS8U0OcSv3vA_wSvg3diSMmsC50BcSTbcMD47hsS7q3QwssdS7cY8rpNQHF7v_20_tBpZRuUhTLZ5bY6QnD53T0Lw)

Popunite sva polja kao na sledećoj slici, ali sa vašim sopstvenim SSO URL-om, ne zaboravite da izaberete ikonu i kliknite na SAČUVAJ.

![](https://lh7-us.googleusercontent.com/_ToZv0_KzrnCJtTprJU7FJirxGC9Vn7c632BaLbIQH8aSJCAeOaw6XxpJ3nzUKs4yI4MtEX5QxuLwf_ywjiAP_cEdVEV8fIueOGh10A46pBIEnK5cDu4PS-q2La8tbqOWQb3nkKPyfgfEYxRDlWf7bI)

**Poslednji korak**

* Odjavite se iz DocBits-a.
* Vratite se na meni sa hamburgerom u Inforu i izaberite ikonu koju ste upravo kreirali.
* Bićete preusmereni na kontrolnu tablu DocBits-a.
