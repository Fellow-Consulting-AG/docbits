# ZUGFeRD 2.1 (Factur-X 1.0) Alan Eşleştirme

## Genel Bakış

ZUGFeRD 2.1 (Factur-X 1.0), standardın ilk sürümüydü. Eski olmasına rağmen birçok belge hala bu formatı kullanmaktadır. DocBits, ZUGFeRD 2.1 (Factur-X 1.0) XML dosyalarından veri çıkarmak için tam destek sağlar.

## Üst Bilgi Alan Eşleştirme

### Fatura Tanımlama

| ZUGFeRD CII Yolu | DocBits Alanı | Infor BOD Alanı | Tür | Açıklama |
| :--- | :--- | :--- | :--- | :--- |
| `ExchangedDocument/ID` | `INVOICE_NUMBER` | `DocumentID` | STRING | Fatura numarası |
| `ExchangedDocument/TypeCode` | `INVOICE_TYPE_CODE` | `DocumentType` | STRING | Fatura türü kodu |
| `ExchangedDocument/IssueDateTime` | `INVOICE_DATE` | `DocumentDateTime` | DATE | Fatura düzenleme tarihi |

### Belge Referansları

| ZUGFeRD CII Yolu | DocBits Alanı | Infor BOD Alanı | Tür | Açıklama |
| :--- | :--- | :--- | :--- | :--- |
| `BuyerOrderReferencedDocument/ID` | `PURCHASE_ORDER` | `CustomerOrderID` | STRING | Satın alma siparişi numarası |
| `ContractReferencedDocument/ID` | `CONTRACT_NUMBER` | `ContractID` | STRING | Sözleşme referansı |
| `DespatchAdviceReferencedDocument/ID` | `DELIVERY_NOTE` | `ShipmentID` | STRING | Teslimat notu referansı |

### Tedarikçi (Satıcı) Bilgileri

| ZUGFeRD CII Yolu | DocBits Alanı | Infor BOD Alanı | Tür | Açıklama |
| :--- | :--- | :--- | :--- | :--- |
| `SellerTradeParty/ID` | `VENDOR_ID` | `SupplierPartyID` | STRING | Tedarikçi kimliği |
| `SellerTradeParty/Name` | `VENDOR_NAME` | `SupplierPartyName` | STRING | Tedarikçi adı |
| `SellerTradeParty/PostalTradeAddress/Line1` | `VENDOR_ADDRESS` | `SupplierAddress1` | STRING | Adres satırı 1 |
| `SellerTradeParty/PostalTradeAddress/PostcodeCode` | `VENDOR_POSTAL_CODE` | `SupplierPostalCode` | STRING | Posta kodu |
| `SellerTradeParty/PostalTradeAddress/CityName` | `VENDOR_CITY` | `SupplierCity` | STRING | Şehir |
| `SellerTradeParty/PostalTradeAddress/CountryID` | `VENDOR_COUNTRY` | `SupplierCountryCode` | STRING | Ülke kodu |

## Satır Öğesi Eşleştirme

| ZUGFeRD CII Yolu | DocBits Alanı | Infor BOD Alanı | Tür | Açıklama |
| :--- | :--- | :--- | :--- | :--- |
| `AssociatedDocumentLineDocument/LineID` | `POSITION` | `LineNumber` | STRING | Satır numarası |
| `SpecifiedTradeProduct/BuyerAssignedID` | `ITEM_NUMBER` | `BuyerItemID` | STRING | Alıcının ürün numarası |
| `SpecifiedTradeProduct/Name` | `DESCRIPTION` | `ItemDescription` | STRING | Ürün açıklaması |
| `BilledQuantity` | `QUANTITY` | `InvoicedQuantity` | NUMBER | Faturalanan miktar |
| `NetPriceProductTradePrice/ChargeAmount` | `UNIT_PRICE` | `UnitPrice` | AMOUNT | Net birim fiyat |
| `LineTotalAmount` | `TOTAL_AMOUNT` | `ExtendedAmount` | AMOUNT | Satır toplamı |
