# ZUGFeRD 2.3.2 Feldzuordnung

## Überblick

ZUGFeRD 2.3.2 ist ein Wartungs-Release des 2.3-Standards, das die Kompatibilität mit den neuesten CII-Aktualisierungen sicherstellt.

## Header Feldzuordnung

### Rechnungsidentifikation

| ZUGFeRD CII Pfad | DocBits Feld | Infor BOD Feld | Typ | Beschreibung |
| :--- | :--- | :--- | :--- | :--- |
| `ExchangedDocument/ID` | `INVOICE_NUMBER` | `DocumentID` | STRING | Rechnungsnummer |
| `ExchangedDocument/IssueDateTime` | `INVOICE_DATE` | `DocumentDateTime` | DATE | Ausstellungsdatum der Rechnung |

### Steueraufschlüsselung

| ZUGFeRD CII Pfad | DocBits Feld | Infor BOD Feld | Typ | Beschreibung |
| :--- | :--- | :--- | :--- | :--- |
| `ApplicableTradeTax[1]/RateApplicablePercent` | `TAX_RATE` | `TaxPercent` | NUMBER | Steuersatz 1 |
| `ApplicableTradeTax[1]/BasisAmount` | `NET_AMOUNT` | `TaxableAmount` | AMOUNT | Nettobetrag für Steuer 1 |
| `ApplicableTradeTax[1]/CalculatedAmount` | `TAX_AMOUNT` | `TaxAmount` | AMOUNT | Steuerbetrag 1 |

## Positionsmapping

| ZUGFeRD CII Pfad | DocBits Feld | Infor BOD Feld | Typ | Beschreibung |
| :--- | :--- | :--- | :--- | :--- |
| `AssociatedDocumentLineDocument/LineID` | `POSITION` | `LineNumber` | STRING | Positionsnummer |
| `SpecifiedTradeProduct/Name` | `DESCRIPTION` | `ItemDescription` | STRING | Artikelbeschreibung |
| `BilledQuantity` | `QUANTITY` | `InvoicedQuantity` | NUMBER | Berechnete Menge |
| `NetPriceProductTradePrice/ChargeAmount` | `UNIT_PRICE` | `UnitPrice` | AMOUNT | Netto-Einzelpreis |
| `LineTotalAmount` | `TOTAL_AMOUNT` | `ExtendedAmount` | AMOUNT | Gesamtbetrag der Position |
