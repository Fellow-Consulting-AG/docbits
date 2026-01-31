# ZUGFeRD + Swiss QR Code mapiranje polja

## Pregled

Prilikom obrade PDF faktura koje sadrže i ZUGFeRD XML podatke i Swiss QR Code, DocBits izdvaja podatke iz oba izvora i inteligentno ih spaja.

## Kako to funkcioniše

1.  **Ekstrakcija ZUGFeRD XML-a** - DocBits prvo izdvaja polja iz ugrađenog ZUGFeRD XML-a
2.  **Detekcija Swiss QR Code-a** - Usluga barcode-service detektuje i parsira Swiss QR kodove
3.  **Pametno spajanje (Smart Merge)** - Prazna polja se popunjavaju podacima iz Swiss QR-a (polja sa vrednostima se zadržavaju)
4.  **Audit Trail** - Kompletni podaci QR koda se čuvaju u `qr_code_data` radi verifikacije

## Tabela mapiranja polja

### Swiss QR Code → DocBits mapiranje polja

| Swiss QR polje | DocBits polje | Opis |
| :--- | :--- | :--- |
| IBAN | `supplier_iban` | IBAN poverioca (npr. CH9300762011...) |
| Amount | `total_amount` | Iznos plaćanja (npr. 1234.56) |
| Currency | `currency` | Oznaka valute (CHF ili EUR) |
| Reference | `payment_reference` / `esr_reference` | QR referenca ili ESR broj |
| Creditor.Name | `supplier_name` | Naziv kompanije dobavljača |
| Creditor.AddressLine1 | `supplier_address` | Adresa (ulica) |
| Creditor.PostalCode | `supplier_plz` | Poštanski broj |
| Creditor.City | `supplier_city` | Grad |
| Creditor.Country | `supplier_country` | Oznaka zemlje (CH) |
| Debtor.Name | `company_name` | Naziv kompanije primaoca |
| Debtor.AddressLine1 | `company_street` | Adresa primaoca |
| Debtor.PostalCode | `company_plz` | Poštanski broj primaoca |
| Debtor.City | `company_city` | Grad primaoca |

## Primer: Obrada uzorka fakture

### Ulazni dokument

*   **PDF**: Faktura sa ugrađenim ZUGFeRD 1.0 XML-om + Swiss QR Code bar kodom

### Podaci ekstrahovani iz Swiss QR Code-a

```json
{
  "supplier_iban": "CH9300762011623852957",
  "amount_to_pay": 1234.56,
  "currency": "CHF",
  "esr_reference": "210000000003139471430009017",
  "supplier_name": "Sample Company GmbH",
  "supplier": {
    "name": "Sample Company GmbH",
    "address_line_1": "Musterstrasse",
    "address_line_2": "123",
    "postal_code": "8000",
    "city": "Zürich",
    "country": "CH"
  },
  "recipient": {
    "name": "Demo Customer AG",
    "address_line_1": "Beispielweg 45",
    "postal_code": "3000",
    "city": "Bern",
    "country": "CH"
  }
}
```

### Rezultati ekstrakcije polja

| Polje | Vrednost | Izvor | Metoda |
| :--- | :--- | :--- | :--- |
| `supplier_iban` | CH9300762011623852957 | ZUGFeRD XML | ED |
| `total_amount` | 1234.56 | ZUGFeRD XML | ED |
| `currency` | CHF | ZUGFeRD XML | ED |
| `supplier_name` | Sample Company GmbH | ZUGFeRD XML | ED |
| `supplier_address` | Musterstrasse 123 | ZUGFeRD XML | ED |
| `payment_reference` | 210000000003139471430009017 | Swiss QR | SWISS_QR |
| `supplier_plz` | 8000 | Swiss QR | SWISS_QR |
| `supplier_city` | Zürich | Swiss QR | SWISS_QR |

## Metode ekstrakcije

| Kod metode | Opis |
| :--- | :--- |
| **ED** | Elektronski dokument (ZUGFeRD/XRechnung/PEPPOL XML) |
| **SWISS_QR** | Ekstrakcija Swiss QR Code bar koda |
| **OCR** | Optičko prepoznavanje znakova |
| **ML** | Machine Learning ekstrakcija |

## Prioritet spajanja (Merge)

1.  **ZUGFeRD XML** ima najveći prioritet (strukturirani, pouzdani podaci)
2.  **Swiss QR Code** popunjava prazna polja (garantovano tačno za podatke o plaćanju)
3.  **OCR/ML** se koristi za polja koja nisu prisutna u elektronskim izvorima

## Podržane verzije Swiss QR Code-a

*   Swiss QR Bill format (ISO 20022)
*   QR-IBAN format (počinje sa 30, 31)
*   Standardni IBAN format
*   Sa/bez strukturirane reference (QRR, SCOR)

## Zahtevi verzije

Ova funkcija zahteva **doc2-api verziju 10.95.6** i **barcode-service verziju 1.0.5** ili noviju.

### Verzije komponenti (Dev okruženje)

| Komponenta | Verzija | Opis |
| :--- | :--- | :--- |
| `doc2-api` | 10.95.6 | Core API sa podrškom za ekstrakciju ZUGFeRD 1.0 |
| `barcode-service` | 1.0.5 | Detekcija i parsiranje Swiss QR Code-a |
| `auth-service` | 1.48.8 | Usluga autentifikacije |

### Potrebna migracija

Podrška za ZUGFeRD 1.0 zahteva primenu sledeće Alembic migracije:

*   `g2h3i4j5k6l7_add_zugferd_1_0_attribute_values.py` - Dodaje TRANSFORMATION, EXTRACTION_PATHS i PREVIEW vrednosti za ZUGFeRD 1.0

Pokrenite migracije pomoću:

```bash
alembic upgrade head
```

