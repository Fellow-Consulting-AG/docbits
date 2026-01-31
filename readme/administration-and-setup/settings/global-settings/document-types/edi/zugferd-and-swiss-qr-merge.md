# ZUGFeRD + Swiss QR Code Veldtoewijzing

## Overzicht

Bij het verwerken van PDF-facturen die zowel ZUGFeRD XML-gegevens als een Swiss QR Code bevatten, haalt DocBits gegevens uit beide bronnen en voegt deze intelligent samen.

## Hoe het werkt

1. **ZUGFeRD XML-extractie** - DocBits haalt eerst velden uit de ingesloten ZUGFeRD XML
2. **Swiss QR Code-detectie** - De barcode-service detecteert en parseert Swiss QR Codes
3. **Smart Merge** - Lege velden worden gevuld met Swiss QR-gegevens (velden met waarden blijven behouden)
4. **Audit Trail** - Volledige QR-codegegevens worden opgeslagen in `qr_code_data` voor verificatie

## Veldtoewijzingstabel

### Swiss QR Code → DocBits Veldtoewijzing

| Swiss QR Veld | DocBits Veld | Beschrijving |
| :--- | :--- | :--- |
| IBAN | `supplier_iban` | IBAN van crediteur (bijv. CH9300762011...) |
| Amount | `total_amount` | Betalingsbedrag (bijv. 1234.56) |
| Currency | `currency` | Valutacode (CHF of EUR) |
| Reference | `payment_reference` / `esr_reference` | QR-referentie of ESR-nummer |
| Creditor.Name | `supplier_name` | Bedrijfsnaam leverancier |
| Creditor.AddressLine1 | `supplier_address` | Straatadres |
| Creditor.PostalCode | `supplier_plz` | Postcode |
| Creditor.City | `supplier_city` | Plaats |
| Creditor.Country | `supplier_country` | Landcode (CH) |
| Debtor.Name | `company_name` | Bedrijfsnaam ontvanger |
| Debtor.AddressLine1 | `company_street` | Straatadres ontvanger |
| Debtor.PostalCode | `company_plz` | Postcode ontvanger |
| Debtor.City | `company_city` | Plaats ontvanger |

## Voorbeeld: Verwerking van voorbeeldfactuur

### Invoerdocument

*   **PDF**: Factuur met ingesloten ZUGFeRD 1.0 XML + Swiss QR Code barcode

### Geëxtraheerde Swiss QR Code-gegevens

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

### Veldextractieresultaten

| Veld | Waarde | Bron | Methode |
| :--- | :--- | :--- | :--- |
| `supplier_iban` | CH9300762011623852957 | ZUGFeRD XML | ED |
| `total_amount` | 1234.56 | ZUGFeRD XML | ED |
| `currency` | CHF | ZUGFeRD XML | ED |
| `supplier_name` | Sample Company GmbH | ZUGFeRD XML | ED |
| `supplier_address` | Musterstrasse 123 | ZUGFeRD XML | ED |
| `payment_reference` | 210000000003139471430009017 | Swiss QR | SWISS_QR |
| `supplier_plz` | 8000 | Swiss QR | SWISS_QR |
| `supplier_city` | Zürich | Swiss QR | SWISS_QR |

## Extractiemethoden

| Methodecode | Beschrijving |
| :--- | :--- |
| **ED** | Elektronisch Document (ZUGFeRD/XRechnung/PEPPOL XML) |
| **SWISS_QR** | Swiss QR Code barcode-extractie |
| **OCR** | Optische Tekenherkenning |
| **ML** | Machine Learning extractie |

## Samenvoegingsprioriteit (Merge Priority)

1.  **ZUGFeRD XML** heeft de hoogste prioriteit (gestructureerde, betrouwbare gegevens)
2.  **Swiss QR Code** vult lege velden (gegarandeerd nauwkeurig voor betalingsgegevens)
3.  **OCR/ML** gebruikt voor velden die niet in elektronische bronnen staan

## Ondersteunde Swiss QR Code-versies

*   Swiss QR Bill-formaat (ISO 20022)
*   QR-IBAN-formaat (begint met 30, 31)
*   Standaard IBAN-formaat
*   Met/zonder gestructureerde referentie (QRR, SCOR)

## Versievereiste

Deze functie vereist **doc2-api versie 10.95.6** en **barcode-service versie 1.0.5** of hoger.

### Componentversies (Dev-omgeving)

| Component | Versie | Beschrijving |
| :--- | :--- | :--- |
| `doc2-api` | 10.95.6 | Core API met ZUGFeRD 1.0 extractie-ondersteuning |
| `barcode-service` | 1.0.5 | Swiss QR Code detectie en parsing |
| `auth-service` | 1.48.8 | Authenticatieservice |

### Migratie vereist

De ZUGFeRD 1.0-ondersteuning vereist dat de volgende Alembic-migratie wordt toegepast:

*   `g2h3i4j5k6l7_add_zugferd_1_0_attribute_values.py` - Voegt TRANSFORMATION, EXTRACTION_PATHS en PREVIEW waarden toe voor ZUGFeRD 1.0

Voer migraties uit met:

```bash
alembic upgrade head
```

### Verificatie

Controleer na de upgrade of ZUGFeRD 1.0-ondersteuning actief is:

```sql
SELECT attribute_name, LENGTH(value) as value_length
FROM electronic_document_extraction_attributes eda
JOIN electronic_document_extraction_attribute_values edav ON edav.attribute_id = eda.id
WHERE eda.electronic_document_type = 'ZUGFERD 1.0'
  AND eda.org_id = '00000000-0000-0000-0000-000000000000'
  AND eda.is_deleted = false;
```

Verwachte uitvoer:

| attribute_name | value_length |
| :--- | :--- |
| TRANSFORMATION | 21058 |
| EXTRACTION_PATHS | 2879 |
| PREVIEW | 2777 |
