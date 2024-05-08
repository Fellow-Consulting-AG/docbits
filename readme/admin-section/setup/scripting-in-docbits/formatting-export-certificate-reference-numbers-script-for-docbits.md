# Formatiranje skripte za izvoz brojeva referenci sertifikata za Docbits

Ovaj dokument opisuje skriptu "Formatiranje brojeva referenci izvoza sertifikata", sa ciljem standardizacije brojeva referenci na izvoznim sertifikatima u Docbits-u. Pravilno formatiranje osigurava da brojevi referenci odgovaraju spoljnim sistemima ili regulatornim zahtevima.

### Svrha

Osnovni cilj skripte je formatiranje brojeva referenci na izvoznim sertifikatima, osiguravajući da zadovoljavaju unapred definisani zahtev za dužinu dodavanjem vodećih nula. Ova doslednost pomaže u održavanju standardizovanog formata za sve izvozne dokumente obrađene putem Docbits-a.

### Pregled skripte

Skripta identifikuje polje `reference_number` u izvoznom sertifikatu, proverava njegovu dužinu i, ako je potrebno, dodaje nule na početku broja kako bi se osiguralo da zadovoljava minimalni zahtev za dužinu.

#### Isječak koda
```python
ref_number = get_field_value(fields_dict, 'reference_number')
# Ensure the reference number meets a minimum length of 10 characters
if len(ref_number) < 10:
ref_number = ref_number.zfill(10)
set_field_value(fields_dict, 'reference_number', ref_number)
```

