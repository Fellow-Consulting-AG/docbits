# ZUGFeRD 2.1 (Factur-X 1.0) Feldzuordnung

## Überblick

ZUGFeRD 2.1 ist identisch mit dem französischen Standard Factur-X 1.0. Er ist vollständig EN 16931-konform und wird häufig für grenzüberschreitende Transaktionen zwischen Deutschland und Frankreich verwendet.

## Header Feldzuordnung

### Rechnungsidentifikation

| ZUGFeRD CII Pfad | DocBits Feld | Infor BOD Feld | Typ | Beschreibung |
| :--- | :--- | :--- | :--- | :--- |
| `ExchangedDocument/ID` | `INVOICE_NUMBER` | `DocumentID` | STRING | Rechnungsnummer |
| `ExchangedDocument/TypeCode` | `INVOICE_TYPE_CODE` | `DocumentType` | STRING | Rechnungstyp-Code |
| `ExchangedDocument/IssueDateTime` | `INVOICE_DATE` | `DocumentDateTime` | DATE | Ausstellungsdatum der Rechnung |

### Käufer-Informationen

| ZUGFeRD CII Pfad | DocBits Feld | Infor BOD Feld | Typ | Beschreibung |
| :--- | :--- | :--- | :--- | :--- |
| `BuyerTradeParty/ID` | `COMPANY_ID` | `CustomerPartyID` | STRING | Kunden-ID |
| `BuyerTradeParty/Name` | `COMPANY_NAME` | `CustomerPartyName` | STRING | Firmenname |
| `BuyerTradeParty/PostalTradeAddress/Line1` | `COMPANY_ADDRESS` | `CustomerAddress1` | STRING | Adresszeile 1 |
| `BuyerTradeParty/PostalTradeAddress/PostcodeCode` | `COMPANY_POSTAL_CODE` | `CustomerPostalCode` | STRING | Postleitzahl |
| `BuyerTradeParty/PostalTradeAddress/CityName` | `COMPANY_CITY` | `CustomerCity` | STRING | Stadt |
| `BuyerTradeParty/PostalTradeAddress/CountryID` | `COMPANY_COUNTRY` | `CustomerCountryCode` | STRING | Ländercode |

## Positionsmapping

| ZUGFeRD CII Pfad | DocBits Feld | Infor BOD Feld | Typ | Beschreibung |
| :--- | :--- | :--- | :--- | :--- |
| `AssociatedDocumentLineDocument/LineID` | `POSITION` | `LineNumber` | STRING | Positionsnummer |
| `SpecifiedTradeProduct/SellerAssignedID` | `SUPPLIER_ITEM_NUMBER` | `SellerItemID` | STRING | Artikelnummer des Verkäufers |
| `SpecifiedTradeProduct/Name` | `DESCRIPTION` | `ItemDescription` | STRING | Artikelbeschreibung |
| `BilledQuantity` | `QUANTITY` | `InvoicedQuantity` | NUMBER | Berechnete Menge |
| `BilledQuantity/@unitCode` | `UNIT` | `UnitCode` | STRING | Maßeinheit |
| `NetPriceProductTradePrice/ChargeAmount` | `UNIT_PRICE` | `UnitPrice` | AMOUNT | Netto-Einzelpreis |
| `LineTotalAmount` | `TOTAL_AMOUNT` | `ExtendedAmount` | AMOUNT | Gesamtbetrag der Position |
