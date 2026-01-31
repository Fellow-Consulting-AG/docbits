# ZUGFeRD 2.2 Feldzuordnung

## Überblick

ZUGFeRD 2.2 setzt die Ausrichtung auf EN 16931 fort und übernimmt weitere Aktualisierungen aus dem CII-Standard.

## Header Feldzuordnung

### Rechnungsidentifikation

| ZUGFeRD CII Pfad | DocBits Feld | Infor BOD Feld | Typ | Beschreibung |
| :--- | :--- | :--- | :--- | :--- |
| `ExchangedDocument/ID` | `INVOICE_NUMBER` | `DocumentID` | STRING | Rechnungsnummer |
| `ExchangedDocument/IssueDateTime` | `INVOICE_DATE` | `DocumentDateTime` | DATE | Ausstellungsdatum der Rechnung |

### Währung & Beträge

| ZUGFeRD CII Pfad | DocBits Feld | Infor BOD Feld | Typ | Beschreibung |
| :--- | :--- | :--- | :--- | :--- |
| `InvoiceCurrencyCode` | `CURRENCY` | `CurrencyCode` | STRING | Rechnungswährung |
| `TaxBasisTotalAmount` | `TOTAL_NET_AMOUNT` | `TaxBasisTotalAmount` | AMOUNT | Gesamt-Nettobetrag |
| `TaxTotalAmount` | `TOTAL_TAX_AMOUNT` | `TaxTotalAmount` | AMOUNT | Gesamt-Steuerbetrag |
| `GrandTotalAmount` | `TOTAL_AMOUNT` | `GrandTotalAmount` | AMOUNT | Bruttobetrag |

## Positionsmapping

| ZUGFeRD CII Pfad | DocBits Feld | Infor BOD Feld | Typ | Beschreibung |
| :--- | :--- | :--- | :--- | :--- |
| `AssociatedDocumentLineDocument/LineID` | `POSITION` | `LineNumber` | STRING | Positionsnummer |
| `SpecifiedTradeProduct/Name` | `DESCRIPTION` | `ItemDescription` | STRING | Artikelbeschreibung |
| `BilledQuantity` | `QUANTITY` | `InvoicedQuantity` | NUMBER | Berechnete Menge |
| `NetPriceProductTradePrice/ChargeAmount` | `UNIT_PRICE` | `UnitPrice` | AMOUNT | Netto-Einzelpreis |
| `LineTotalAmount` | `TOTAL_AMOUNT` | `ExtendedAmount` | AMOUNT | Gesamtbetrag der Position |
