# Primer radnog toka: Uslovni okidač izvoza

<figure><img src="../../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

Ovaj radni tok opisuje uslove pod kojima treba pokrenuti proces izvoza. Osigurava da se samo dokumenti koji ispunjavaju sve navedene kriterijume obrađuju za izvoz, poboljšavajući integritet podataka i usklađenost sa poslovnim pravilima.

### Kada:

* Dokument unutar sistema se procenjuje za ispunjenost uslova za izvoz.

### Logika:

1. **Provera tipa dokumenta**
* Dokument mora biti određenog tipa (npr. "Faktura" ili "Račun"). Navedite tip dokumenta koji se kvalifikuje za proces izvoza.
2. **Provera statusa**
* Trenutni status dokumenta mora zadovoljiti unapred definisane kriterijume (npr. "Odobreno" ili "Spremno za izvoz"), što ukazuje da je spreman za dalju obradu.
3. **Kontekstualni uslovi**
* Vrše se dodatne provere kako bi se osiguralo da se detalji dokumenta usklađuju sa specifičnim zahtevima. Ove provere mogu uključivati proveru informacija unutar potvrda o porudžbini ili narudžbenica. Navedite posebne uslove koji treba da budu ispunjeni. Na primer:
* Svi predmeti navedeni u potvrdi o porudžbini se poklapaju sa onima u narudžbenici.
* Ukupan iznos u potvrdi o porudžbini se poklapa sa ukupnim iznosom u narudžbenici.
* Datumi isporuke navedeni u potvrdi o porudžbini se poklapaju sa onima u narudžbenici.

### Zatim:

#### Akcija:

* **Pokreni izvoz**
* Ako su ispunjeni svi navedeni uslovi, sistem automatski pokreće proces izvoza za dokument.
* Ovo može uključivati generisanje izvozne datoteke, slanje podataka u spoljni sistem ili pokretanje radnog toka u drugoj aplikaciji.

#### Primer implementacije:
```yaml
rules:
- description: "Conditional Export Trigger"
conditions:
- type: "DocumentType"
criteria: "<SpecifyDocumentType>"
- type: "Status"
criteria: "<SpecifyStatus>"
- type: "DetailMatch"
criteria:
- "ItemMatch"
- "AmountMatch"
- "DateMatch"
actions:
- operation: "StartExport"
```

