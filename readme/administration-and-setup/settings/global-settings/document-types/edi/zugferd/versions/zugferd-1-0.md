# ZUGFeRD 1.0 mapiranje polja

## Pregled

ZUGFeRD 1.0 je bio početna verzija standarda. Iako je stariji, mnogi dokumenti i dalje koriste ovaj format. DocBits pruža punu podršku za izvlačenje podataka iz ZUGFeRD 1.0 XML datoteka.

## Mapiranje polja zaglavlja

### Identifikacija fakture

| ZUGFeRD CII putanja | DocBits polje | Infor BOD polje | Tip | Opis |
| :--- | :--- | :--- | :--- | :--- |
| `ExchangedDocument/ID` | `INVOICE_NUMBER` | `DocumentID` | STRING | Broj fakture |
| `ExchangedDocument/TypeCode` | `INVOICE_TYPE_CODE` | `DocumentType` | STRING | Kod tipa fakture |
| `ExchangedDocument/IssueDateTime` | `INVOICE_DATE` | `DocumentDateTime` | DATE | Datum izdavanja fakture |

### Reference dokumenata

| ZUGFeRD CII putanja | DocBits polje | Infor BOD polje | Tip | Opis |
| :--- | :--- | :--- | :--- | :--- |
| `BuyerOrderReferencedDocument/ID` | `PURCHASE_ORDER` | `CustomerOrderID` | STRING | Broj narudžbenice |
| `ContractReferencedDocument/ID` | `CONTRACT_NUMBER` | `ContractID` | STRING | Referenca ugovora |
| `DespatchAdviceReferencedDocument/ID` | `DELIVERY_NOTE` | `ShipmentID` | STRING | Referenca otpremnice |

### Informacije o dobavljaču (prodavcu)

| ZUGFeRD CII putanja | DocBits polje | Infor BOD polje | Tip | Opis |
| :--- | :--- | :--- | :--- | :--- |
| `SellerTradeParty/ID` | `VENDOR_ID` | `SupplierPartyID` | STRING | ID dobavljača |
| `SellerTradeParty/Name` | `VENDOR_NAME` | `SupplierPartyName` | STRING | Naziv dobavljača |
| `SellerTradeParty/PostalTradeAddress/Line1` | `VENDOR_ADDRESS` | `SupplierAddress1` | STRING | Adresa red 1 |
| `SellerTradeParty/PostalTradeAddress/PostcodeCode` | `VENDOR_POSTAL_CODE` | `SupplierPostalCode` | STRING | Poštanski broj |
| `SellerTradeParty/PostalTradeAddress/CityName` | `VENDOR_CITY` | `SupplierCity` | STRING | Grad |
| `SellerTradeParty/PostalTradeAddress/CountryID` | `VENDOR_COUNTRY` | `SupplierCountryCode` | STRING | Kod zemlje |

## Mapiranje stavki

| ZUGFeRD CII putanja | DocBits polje | Infor BOD polje | Tip | Opis |
| :--- | :--- | :--- | :--- | :--- |
| `AssociatedDocumentLineDocument/LineID` | `POSITION` | `LineNumber` | STRING | Broj pozicije |
| `SpecifiedTradeProduct/BuyerAssignedID` | `ITEM_NUMBER` | `BuyerItemID` | STRING | Broj artikla kupca |
| `SpecifiedTradeProduct/Name` | `DESCRIPTION` | `ItemDescription` | STRING | Opis artikla |
| `BilledQuantity` | `QUANTITY` | `InvoicedQuantity` | NUMBER | Fakturisana količina |
| `NetPriceProductTradePrice/ChargeAmount` | `UNIT_PRICE` | `UnitPrice` | AMOUNT | Neto jedinična cena |
| `LineTotalAmount` | `TOTAL_AMOUNT` | `ExtendedAmount` | AMOUNT | Ukupno za stavku |
