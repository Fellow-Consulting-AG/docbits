# Kreiranje BOD datoteke mapiranja

Preuzmite BOD datoteku mapiranja i otvorite je u svom odgovarajućem uređivaču datoteka po izboru kako biste je uredili. Za ovaj korak, koristi se VSCode.

## Uređivanje datoteke mapiranja

Promenite kompaniju na tačnu (SFV\_AccountingEntityID) i izmenite ID lokacije ako je potrebno.

![](https://lh7-us.googleusercontent.com/eJQI1CKlxEkS\_Pwp0VH2hgS220b-q8NSFG5iJKpLOL457qTN3CbUB8IHTw1lRinbB\_kP00UUNgepWNsbh3\_Ko-SExObePjqmxP7ee\_lQnADTtDmxEtRM\_S7AONMbcpjwtnHTakYd1Q06GVm2G0o-UDA)

Proverite kod dokumenta odlaskom na podešavanja polja tipa dokumenta koji pokušavate da izvezete (pronađeno u URL-u podešavanja polja tipa dokumenta u DocBits-u kao što je prikazano ispod

![](https://lh7-us.googleusercontent.com/AhU3i27qFS7BMCgpNQnmLWAjcIWHXHOlxMKqd2Yob5RQKa8qysQQsSsacr6zao4cnAh3DISPgYu1GnjubIJpgtAdiBR\_0vy3WJZXPY-HeEfVQkWnlRI9UEJWMPQ7DbWYLQhz339BOlbd4KgxU9B\_CPE)

Na kraju, izmenite SFV\_LogicalID koji se može pronaći u INFOR ION DESK → Connect → Connection points i izaberite DocBits\_Export ili sličan connection point i unutar te stranice pronaći ćete Logical ID koji vam je potreban.

![](https://lh7-us.googleusercontent.com/f50i7pzRuZULJ6shehba0lWIWFBTsPZyip-LQxAYJpYDXK66SlzdGOpdEG-wqLQfqXMgMMhm5SAvj57UOCvF6xf2OMCXtFiEEKr9yiQr4xtv8vbV-NGcLuJwuQ9zHMBBKfTktAp1nSfBJhdPeAu3RWc)

![](https://lh7-us.googleusercontent.com/qyEt4iYRIjOZCCrVbImeK6EdZGun2YrAy8li8u3tulcD8bwzl\_sl1TiEXKqbik-4MxnbV\_MCwltvuA2WAgzzvDpTVd7W52he9QD9IK0qijoz3ZihUYcWJlqlD5kbcsRTj3SfP1CDqcyhoFfBeiE1Xfo)

## Kreiranje Logical ID (Connection Point)

Ako ovaj Connection Point još uvek ne postoji, morate ga kreirati.

Prvo, idite na ION Desk → Connect → Connection Points i kliknite na dugme “+ Dodaj”

![](https://lh7-us.googleusercontent.com/fQPmV8KgffyWhM0i0cQlyh7fyQe37p8uR6C\_pVD5SboEx2emIJX2212GXqk\_KT71DfYMKSjkfYFFTARqgLLxoOPNQFXHxUOo9vMXH2pmDN469VgbQkV-JjRtCevZJsbvS8vbfUtasN83xN25tX6\_S5U)

Zatim izaberite opciju “IMS putem API Gateway-a”

![](https://lh7-us.googleusercontent.com/uPLiiLHp6Z3jPCzYBOzHVuI8sGY5XQuUfv66fZYH0HndSBL7yvzFHh3lJjEMxteJfXsVMhUe3U\_38xZHDRFSn0jeiMZUQBJJLzZ2oaIQAixY7wUPd6D0PJwg7wvC8XBeZxPmjNoiUvP3ImoG\_aOhFmY)

![](https://lh7-us.googleusercontent.com/VhyMDEuglPfxeX-3cATu6ZFB\_Mz2Y7C-yJ99EvBvrhD8IoVzGd4ksjrWAE0mIPub2PX5\_Zua10ZHQeWI82QbJ8ZgJKN-tVpVrYGvMdfQOj3Uco5efsPT6JYkDyPu\_lkeR9aTGhh5-q2bzZztXuTUixM)

Bićete preusmereni na ekran prikazan iznad gde sada morate popuniti neophodne informacije, ime bi trebalo da bude nešto poput “DocBits\_export” ili slično.

Za “ION API Client ID” unesite isti Client ID koji ste prethodno dobili za ION datoteku mapiranja.

Zatim izaberite karticu Dokument Connection Point kreacije menija i dodajte sledeće dokumente pritiskom na znak “+”, ovo će postati korisno kasnije.

![](https://lh7-us.googleusercontent.com/GtHlTliePV-JIDLP9YNGlXELKuWIU2VSlUt4mvWO4q\_XM54MSL9zTmtxPMdeOl24VFtNC0pQ-nbXyHb9PaeMkKvgzpCOo5kLdL3A8Bw54ILniwIdTyfxFhPuzRUGKs2hRi5ioKvfkdsPMgq4x6EHOtM)

Kada sačuvate ovaj Connection Point, dobićete Logical ID prikazan ispod

![](https://lh7-us.googleusercontent.com/P7cihsQT2Qcq\_XGL08dTV2jHMUK7YCMQyXsJudkVDXDh73GZ-hS61IoAKSHptPyX4C5e\_xPKP0yZGzpQOwCFw6BppPlzZuFWZ\_VGIrOUmJH2egxaCEXMoVBHBM6lkZeb3gPYWYdMYpuNqFFPC-4Qol0)

Zatim umetnite ovaj Logical ID u odgovarajući deo BOD datoteke mapiranja i sačuvajte datoteku.

## Učitajte datoteku u DocBits

Prevucite i otpustite datoteku u vašu konfiguraciju izvoza u DocBits-u. Ovo je dostupno na Podešavanja → Izvoz.

![](https://lh7-us.googleusercontent.com/AqCo7QgC-kaAxbaIJD8MYeKGLBXbwGVJPGx9\_2yfUp3R2MYxJPowVAjnO80uxQ9qMDxNoXy1eY3WH-mEpaeWwatwi91edm\_0lS9Hg93FSAjQGtDAR5y7Ptce-ARfetSiXIBJKiGwujSggVXXHUhG77U)
