# Kreiranje IDM Mapping fajla

Kada ga dobijete, otvorite fajl u svom odgovarajućem uređivaču fajlova po izboru. Za ovaj korak, koristiće se VSCode.

## Uredi Mapping fajl

Proverite da li je kod tipa dokumenta isti kao u DocBits-u (na primer, kod BOD Mapping fajla treba da se poklapa sa imenom tipa dokumenta u URL-u postavki polja) i takođe proverite ime tipa dokumenta kako treba da bude u Document Manager-u (IDM) u Infor-u.

![](https://lh7-us.googleusercontent.com/WHO0vg2W36yVFBq0ay0wBMFVzMfT6pNvHklt0o8N4tqUpM03jXJm2fykuYjyZh0z4wFTO4Eaeh39-D03re3a9utegrdVdsjHBfucmALA3B7YBWd92-9bcYr543G4MWftv0RosvTgFP3J6NNmLZAz5Dc)

**Napomena**: Navodi se da je ime tipa dokumenta u IDM-u M3\_SupplierInvoice, to je zbog toga što je ovo primer sa M3 instance. Ovo može da se promeni u zavisnosti od toga da li koristite LN ili M3, kao i vaše specifične konfiguracije IDM-a.

Proverite ID kompanije, proverite Entity ID (SF\_MDS\_EntityType) ova vrednost treba da bude ista kao što je bila u BOD Mapping fajlu.

Proverite da li je IndexFieldFromDocBits=IDMAttributeID (proverite da li se DocBits na levoj strani u postavkama polja poklapa sa IDM-om na desnoj strani u Tip dokumenta → Atributi).

### Document Manager u Infor-u

Idite na Document Manager i izaberite ime trenutnog tipa dokumenta koji pokušavate da izvezete, na primer, Faktura dobavljača.

![](https://lh7-us.googleusercontent.com/EV3uw3R1L6\_RRANB7FRLwtUFMbv\_KGtL4x6kAk6lEYhwI90UeG2uWqFD2Azpxv-SRFl9zfvdratOZbXxp2D1-SryLo3Boj2x9Xc4PQXJ6vUhX5c9pvhv4XHuCk-qMK51DZ885vRUJ5dwES7k84uhoyk)

Kliknite na gornju ikonu, a zatim kliknite na Administracija → Tip dokumenta i zatim pronađite tip dokumenta koji vam je potreban na listi.

![](https://lh7-us.googleusercontent.com/ldsuINS9SCUQm3E57s8j\_95gzBGwHQFavcf6d3myg6tuVxRoQHtq8R-6we5OEJ63swDxwPc9w7hbySWqWdfaMsGdQpn99m6EchPY5f5DzXEj-8mjocwPNtdJVNP34CuPvw0JIImDgFX1Q05M8-ogZo8)

Kao što je prikazano ispod, videćete ime tipa dokumenta onako kako je prikazano u INFOR-u.

![](https://lh7-us.googleusercontent.com/KSreWGS7TqdMP64BqtufM24xk0RDnNDHUZapnPsSuRj\_umPJ3icll89KI2RYpbtet2F6ccL8QfYbl27-2j1nQPwQ0z-Nq873c4Tv72ee9AJhKMxynIUxmJKKsQQCupW\_dpRfw\_5BXm0WvAnw4HOALmw)

Proverite da li je ovo kako je ime prikazano u IDM Mapping fajlu.

## Učitaj fajl u DocBits

Kada je fajl spreman, učitajte ga u vašu konfiguraciju izvoza u DocBits-u. Ovo je dostupno na Podešavanja → Izvoz.

![](https://lh7-us.googleusercontent.com/rUHhvImiWamK6JxnWSPL4JEioAJq3AmvdsubJDo-DoDV9F\_i5mZ42YDnjqZUYKYSJu1Cetc\_4fLwlvvmoZXYIzmBf3hoyW6RjfP9HQ8FkNDhW1IbLHvNTCHWFRaeCECdZ97u79-Eu37TvzqnqGPEayM)
