# ZUGFeRD 1.0 Feldzuordnung

## Überblick

ZUGFeRD 1.0 war die erste Version des Standards. Obwohl sie älter ist, verwenden viele Dokumente immer noch dieses Format. DocBits bietet volle Unterstützung für die Extraktion von Daten aus ZUGFeRD 1.0 XML-Dateien.

## Header Feldzuordnung

### Rechnungsidentifikation

| ZUGFeRD CII Pfad | DocBits Feld | Infor BOD Feld | Typ | Beschreibung |
| :--- | :--- | :--- | :--- | :--- |
| `ExchangedDocument/ID` | `INVOICE_NUMBER` | `DocumentID` | STRING | Rechnungsnummer |
| `ExchangedDocument/TypeCode` | `INVOICE_TYPE_CODE` | `DocumentType` | STRING | Rechnungstyp-Code |
| `ExchangedDocument/IssueDateTime` | `INVOICE_DATE` | `DocumentDateTime` | DATE | Ausstellungsdatum der Rechnung |

### Dokumentreferenzen

| ZUGFeRD CII Pfad | DocBits Feld | Infor BOD Feld | Typ | Beschreibung |
| :--- | :--- | :--- | :--- | :--- |
| `BuyerOrderReferencedDocument/ID` | `PURCHASE_ORDER` | `CustomerOrderID` | STRING | Bestellnummer |
| `ContractReferencedDocument/ID` | `CONTRACT_NUMBER` | `ContractID` | STRING | Vertragsreferenz |
| `DespatchAdviceReferencedDocument/ID` | `DELIVERY_NOTE` | `ShipmentID` | STRING | Lieferscheinreferenz |

### Lieferanten-Informationen (Verkäufer)

| ZUGFeRD CII Pfad | DocBits Feld | Infor BOD Feld | Typ | Beschreibung |
| :--- | :--- | :--- | :--- | :--- |
| `SellerTradeParty/ID` | `VENDOR_ID` | `SupplierPartyID` | STRING | Lieferanten-ID |
| `SellerTradeParty/Name` | `VENDOR_NAME` | `SupplierPartyName` | STRING | Name des Lieferanten |
| `SellerTradeParty/PostalTradeAddress/Line1` | `VENDOR_ADDRESS` | `SupplierAddress1` | STRING | Adresszeile 1 |
| `SellerTradeParty/PostalTradeAddress/PostcodeCode` | `VENDOR_POSTAL_CODE` | `SupplierPostalCode` | STRING | Postleitzahl |
| `SellerTradeParty/PostalTradeAddress/CityName` | `VENDOR_CITY` | `SupplierCity` | STRING | Stadt |
| `SellerTradeParty/PostalTradeAddress/CountryID` | `VENDOR_COUNTRY` | `SupplierCountryCode` | STRING | Ländercode |

## Positionsmapping

| ZUGFeRD CII Pfad | DocBits Feld | Infor BOD Feld | Typ | Beschreibung |
| :--- | :--- | :--- | :--- | :--- |
| `AssociatedDocumentLineDocument/LineID` | `POSITION` | `LineNumber` | STRING | Positionsnummer |
| `SpecifiedTradeProduct/BuyerAssignedID` | `ITEM_NUMBER` | `BuyerItemID` | STRING | Artikelnummer des Käufers |
| `SpecifiedTradeProduct/Name` | `DESCRIPTION` | `ItemDescription` | STRING | Artikelbeschreibung |
| `BilledQuantity` | `QUANTITY` | `InvoicedQuantity` | NUMBER | Berechnete Menge |
| `NetPriceProductTradePrice/ChargeAmount` | `UNIT_PRICE` | `UnitPrice` | AMOUNT | Netto-Einzelpreis |
| `LineTotalAmount` | `TOTAL_AMOUNT` | `ExtendedAmount` | AMOUNT | Gesamtbetrag der Position |
