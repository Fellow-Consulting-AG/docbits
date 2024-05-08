# Konfiguracija M3

## Preduslovi

Kreirali ste:

* ION API Endpoint
* ION API Datoteku
* BOD Mapiranje Datoteku
* IDM Mapiranje Datoteku

## Uvoz Mapirajućih Datoteka

Pre nego što postavite protok podataka, morate uvesti mapirajuće datoteke u InforOS.

U ION Desk-u → Poveži i otvori Mapiranja

![](https://lh7-us.googleusercontent.com/EV8z6b_W9tjTgML0j3qJAYHCTYLd4N5yLrArdIECftYpMOCRTRJ_a7eADEzljFM4XHxMUJ6Nx9Z6EN3Hmzote5F0HrM5zd4p1BS0NYicUWDnkhQFX-_3MGbblEYi6x2a1K25SclYYttgW3cWQbOjvfQ)

Kliknite na ikonu za uvoz

![](https://lh7-us.googleusercontent.com/agBHtjNitneogoZsSG1791QAARbvesv9eSriAkw0HL9Fy372Ty6SmQG1sKJjOYZCuE0SnGT3agHAFRJYjgGNxJrN1CMJj9L-fSPhNmXxN78iDKqrrdgEVYFHxsNwy9XLiUFpBCQ1wnWlwyeFH08DsWI)

Odatle treba da odaberete različite mapirajuće datoteke koje će vam biti potrebne, uključujući: SyncCaptDoc\_SyncSuppInv, SyncSupplierInvoice\_LoadSupplierInvoice i LoadSupplierInvoice\_ProcessSupplierInvoice.

Kada uvezete sve mapirajuće datoteke, obavezno odobrite svaku od njih klikom na ikonu kvačice unutar svakog njihovog kvadrata na kontrolnoj tabli Mapiranja.

## DocBits u M3

Sledeći korak je postavljanje Protoka Podataka u ION Desk-u, idite na aplikaciju ION Desk i odaberite Protok Podataka → + DODAJ → Protok Dokumenata kao što je prikazano ispod

![](https://lh7-us.googleusercontent.com/Kkro7w2LPfnwf-JPMmPI2DzrSRNEi_F9aWW02KDtBvAZz_R7j9DZ71Nqw3ETPSQqDuxBzJ1TU8Uuzz5jU9rOO_tvDBf9abVF-FDSxln_pjr-HMRdYBnGMwgcM6hg-pC2B7FgdBkXibivMB4PptvZ6fk)

Zatim ćete videti ovu stranicu, ovo je mesto gde ćete izgraditi tok informacija od DocBits-a do M3

![](https://lh7-us.googleusercontent.com/K0B1lC_KLO5RZqGqAltp6JnZZ1sfZG4wg-i_nxZCnLjML33yvViRUHOInK3iHYbzbV4I0uqDY8JpsZMxssD8bbJy24A1zKr9PfQEyqVxewx_L87RCIwzn5MDRjMqgx4X42vkKthbyz--5DDe1H0rvHQ)

Protok podataka M3 će izgledati slično kao što je prikazano ispod (postoje 3 aplikacije i API-ja DocBits zbog korišćenja za 3 odvojena okruženja).

![](https://lh7-us.googleusercontent.com/6Oy_UBzYNml-7_sayDEKhqYF92yDzlUNzmGLQSWZOfDT-avvfg3oNUnv_DtXNSP0XF43D-zgIizIuTrCXl6ockLU2uQLYFJna72fzL5BP-T89xjF4oWz2eAz9w0hsoVieyTpgSw_Prvj--89Kc4Kqoo)

Svi delovi lanca se prevlače i otpuštaju iz gornjeg dela

U lancu, DocBits i M3 su obe Aplikacije dok između njih postoje mapiranja koja pretvaraju podatke u oblik koji može biti razumljiv sledećem delu voza i "mapiraju" informacije tako da idu tamo gde su potrebne ili namenjene.

![](https://lh7-us.googleusercontent.com/1kjgKNmIQ-NbM_JukcPsj7qmyiMB9b693ixg6Dh1kOlZ6NKgBXViYwn0MNUBHt0WKKWf_1gpRvxgqjIaqpqcy-SyXoYjhJLt3m_bv7wbVADzqHRsx8TYXWyIQO82X-Ixfl5b7iI7nxTRkw06sX3xsBM)

### Aplikacija DocBits

Dajte joj odgovarajuće ime kao što je "DocBits", zatim odaberite znak plus i potražite tačku povezivanja koju ste prethodno kreirali, poput DocBits\_Export ili slično i kliknite na nju.

Da biste kreirali ovu tačku povezivanja, idite na ION Desk → Poveži → Tačke Povezivanja

![](https://lh7-us.googleusercontent.com/8qsMIUKMrgmcYqqJPL2zF4GVeHuvSHvn8Z7dfonRuvKFPcXmN4hx2PIrXko4lvW7ayD7s2VRFOMvWkQSxfAH5tTuhg0XhzYmSzlsgnowWRw8GmQC2y5BjcS9X2MjDzLSutgoHg2VN59kCYRunMSxkIY)

Kliknite na "+ Dodaj"

![](https://lh7-us.googleusercontent.com/-3-3TzgEQppYmX64-clxjp1JBjNz9fsA2FDPqirgNF0wL8DsDJACzUBuSw5wBL2k9JanqvMzAG352CWafOdtjhMfZalJnBFVSjaWA1AszhCjKtCsTvLUUqq1WwMfF-PqL-u7LRo4TPbj4fP2_j48240)

Odaberite "IMS putem API Gateway-a" i popunite sledeće informacije

![](https://lh7-us.googleusercontent.com/wImUEi9mXiQjW5O6mp7_IrKk4CTaHFs903DJ6TXqUEcjGq45TnUWdusFTGH1jzpBPP_TC7rokyjrkYWmh3emSKBQs05qYbO80TO87De0C5OveVURykQMCLFRRYakEMoFHpoeXzxH5QIbKJdjxujeY98)

ION API Client ID se nalazi u ION API Datoteci koju ste kreirali u "Kako kreirati ION API Datoteku", ovo se može pronaći preko vrednosti "ci".

Prebacite se na karticu dokumenta i dodajte Sync.CaptureDocument BOD na tačku povezivanja DocBits kao što je prikazano ispod.

![](https://lh7-us.googleusercontent.com/ga1q0Uwdi2GNwuiz22NvDtCzGL0krSkBPLsEVxE-mtoMV7CtEU8TPO0PhF40oB9NB9iv7DCJi9niLnsKjpqarWJsgGRdc1W0pFl9rTDm7i2_BSLj3JOrzR7iclPdqOdpztgCxWZG2Teg1gWljaMUq2E)

Zatim sačuvajte tačku povezivanja pritiskom na ikonu diska u gornjem levom uglu.

Vratite se na sekciju Protoka Podataka u ION Desk-u kako biste pristupili svom protoku podataka. Vaša aplikacija DocBits trebalo bi da izgleda slično kao što je prikazano ispod.

![](https://lh7-us.googleusercontent.com/fBzKL6RU0XvGpn1cKFZIyAp2amKonBWc8ilbAq5u_r867xywWWAD7EjP-g-wjlwUsrG4Wz0lS6Ujdnu8P3vc8Q3FbtbRR4qSBmbSLoICfX-aHITMDdHp07bESefC9TuUUUQiHGb1j00HNtB_7A3iDFs)
### Mapiranje 1

Prvi čvor mapiranja treba da izgleda ovako

![](https://lh7-us.googleusercontent.com/F9AcE4V-s9vs-0kRz8BcCtdHUUQoaooyK3GqOj8pAQWuvIguoUO-tJx7WBEW6\_GmzwNsJp8VUYezGCiLPXvPhEynac3FPh\_NJOvqs1SXtMIUsF5\_HjWmcvY3VC-eZsjG0ZE8HmsKsFhocadr96drSbY)

### Mapiranje 2

Drugi čvor mapiranja treba da izgleda ovako

![](https://lh7-us.googleusercontent.com/8M\_V2BtkOGyqV-828ct5c2QvSs5n5\_RtLjlH717kspZwlgtfjbz6tpOJCCXDelruBenMjxsJPqncQ5hUw2bQkM3ya7\_WrVyEBz3UnaU-C9oVOWB8nNtXA20RBYgO3EBMon2TfgpefY0lSPBzF9NoTeU)

### Mapiranje 3

Treći čvor mapiranja treba da izgleda ovako

![](https://lh7-us.googleusercontent.com/x9QUHTgQrNaeKnTeMIUflkWjcBr2c3LgsYe2BZBjv01hXiEkvsLtU0GzYt5KppcE12ZqxWeBJ1kbLOC6qA3yKHhujCZt3sFpDNE5yERkHHMJJEjFl0jJE90nQ-iXeMLbR-Bk6G0NIL8AqG3U48Seiuc)

### M3 Aplikacija

Već bi trebalo da postoji tačka povezivanja nazvana M3 ili slično kreirana u INFOR-u, pa kao i za DocBits aplikaciju, izaberete je klikom na znak "+" i trebalo bi da izgleda ovako

![](https://lh7-us.googleusercontent.com/JTXIN5QxidvFJyjegxSw8kA7yVfHfuypxi5yX21CsSlGtOVgykc52U2r0077-cKqNhc0B4zSSZotlipFesmLo371kho3wUSRPzmwEir-stbxyZV1PwCDXkq6qJMm4PNXt\_wGarDMixGIU0tu-eAqV5Y)

### DocBits API

Prvo ćete morati da kreirate ovaj API kao tačku povezivanja na sledeći način:

ION Desk → Poveži se → Tačke povezivanja

![](https://lh7-us.googleusercontent.com/VOXW6LixmcKjHW0CTOO5L8fK6r-4k3jqk0AnoR6DEVoGgJMbx65hS3yKSgMWItypdz4Ha82T-bKCN0aMv34gif-b0Aw7zpDFPBK9G-K6x9\_csrM9xyKcpmWam15tKqO1\_rwKtMsJ2CSoWqdpLxCD5tA)

Kliknite na "+ Dodaj" i izaberite API

![](https://lh7-us.googleusercontent.com/c1RAUNoA3YBhvf6FLJ\_L3ouyZwHK-3bBRU83eL3oAQXjG6SjWEO9O-gDKPItPm8AI\_YhadaCZU-GxY-qUXNuQMiRiKUhBYUtJ8kOFVg\_YYpzJDSoJ68NYSaEtHBSyyfnq0VbHUdWY1e8lBQ0j\_G5xvI)

Informacije koje popunite treba da izgledaju ovako

![](https://lh7-us.googleusercontent.com/h2KU6pKeKl9wX8oyul0KmbL\_kg-iPQJpBqbf29l64ED2e-Z4tNj8-m4hBN\_4SSiNPf2TrE92TD4H0-0AZ0eWxMFmDV22IdPlU9NO4XlQF9k0Swg0X3Sm1HMsSPvWi7Q1HUr8uy8j3aDRheFxZqZ2Gbc)

Prebacite se na karticu dokumenta i dodajte sledeću konfiguraciju

![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_api\_docs1-1024x279.png)

**Acknowledge.SupplierInvoice**

Konfiguracija za ovaj BOD je sledeća

![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_ack\_11.png)

Proverite da ste izabrali opciju "Pošalji na API" u gornjem meniju.

![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_ack\_2-1024x338.png)

Na kraju se uverite da ste takođe promenili telo zahteva da izgleda ovako.

![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_ack\_3-1024x260.png)

Ponovite ovaj proces za ostale BOD-ove, svaka konfiguracija je prikazana ispod.

**Sync.PurchaseOrder**

Konfiguracija za ovaj BOD je sledeća

![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_po\_1.png)![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_po\_2-1024x359.png)![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_po\_3-1024x297.png)

**Sync.RemitToPartyMaster**

Konfiguracija za ovaj BOD je sledeća

![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_remit\_1-1.png)![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_remit\_2-1024x351.png)![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_remit\_3-1024x299.png)

**Sync.SupplierPartyMaster**

Konfiguracija za ovaj BOD je sledeća

![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_sup\_1.png)![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_sup\_2.png)![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_sup\_3-1024x295.png)

### BOD-ovi

![](https://lh7-us.googleusercontent.com/zaDSnm844wXqyefN58Y1DvuJOnMaoOrYQ\_12Z5ZSng8-TPy38Th2ZPdAD6hyIYCOvBKGPDSvGpTmtBPq4K5IwyGtsKyMvk-CKOuY-hzD-RL7UrsG39qLN7m3\_IDcDS66KeIQF5e70OWlHO1cbVvQUXM)

Navedene konfiguracije treba da izgledaju ovako:
#### Prvo

![](https://lh7-us.googleusercontent.com/5gLpbQEYYW90dVLkSc5V60LeToMe2wcOcHHtwTdIdT0o0Gktu8T_7i7zfNikjgETM3QmzAsJAknlEGeB0W0YFLLi56g2PKPwyr2zPcHaKdu8XJWHgaC1u4--_CHNYfd1wQ__3kZpv1_PwyZty3JEyak)

#### Drugo

![](https://lh7-us.googleusercontent.com/xbWTcP8hYA72Ijt7_IV6l-9jKeSalbRPvTn7aNVcnWYMQcD2RDjM-EzKpBKjSIKF_-r8BaxmmCo9uz6-E-vC9flKb4toU3SH24EPLgbXc-VcfJeDdJKglf5P6WV6XYZg0cZVWAoyvS8qgtuR6ZqJYlI)

#### Treće

![](https://lh7-us.googleusercontent.com/F8wVWXuHkLLW2kuu_7Dxe9LhyYdm04tl__Sp6FjeTyk_JFUzhCIUhVlKS_cq3I3FP_h2ksV4zEJHFC_KXK6sSZ5iz5yhTFZcPnH1HS_RvZb2Nr-UXYQ1H316UMoj6eRv6wMn3wHX842B5WVfPHVnJ74)

#### Četvrto

![](https://lh7-us.googleusercontent.com/myhi9y2sCvS5ZFkIJa5ysLbu7p0X6CYqbiuJ3sQ5-O-2QWlfAseunjwhXK0kakmAofplm0zmh_H1Np7bA559w0-jdurQUsZwYF9CyKYSKSeGnQaIit0HQ5iN-3Xv8CIC-5nk6mMj3JTDS97SlzbsOFE)

#### Peto

![](https://lh7-us.googleusercontent.com/c-5iaUhhx0swH-mQfXE5Mdwe4J0skGt7mst4kJdOpjL3Uat329TZmKM5Af-lGQWmcmBht-ib_aUj4dVG7GaUAHHULjly3jxsR8MJNnLDcu5eZB268Vy-dXPxHmkVB8dMZTRhU5SUB59AREurJlW-K6o)

Poslednja ikona treba da bude prazna jer ne nosi nikakav dokument ili informaciju.

Kada dodate sve potrebne čvorove u tok podataka, pritisnite ovu dugmad za aktiviranje toka podataka (nakon što sačuvate tok podataka pritiskom na ikonu hardvera).

![](https://lh7-us.googleusercontent.com/WIecHktG7e5dbVScLbR8hUcZUdCEWXBW4xWDEuq0IqTMmguA_Ih_oRymvpk6CzowWFG5TTSCPIH-68ICnPSOPxeZksc-n4bmpvuH8dvHuHFU1DlppGRno3PKjCSJiK12p9bNlo_9cN2t9Ps3nbqF3xE)
