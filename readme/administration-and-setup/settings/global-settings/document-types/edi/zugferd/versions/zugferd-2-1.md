# Mapeo de campos de ZUGFeRD 2.1 (Factur-X 1.0)

## Resumen

ZUGFeRD 2.1 (Factur-X 1.0) fue la versión inicial del estándar. Aunque es antigua, muchos documentos todavía utilizan este formato. DocBits ofrece compatibilidad total para extraer datos de archivos XML de ZUGFeRD 2.1 (Factur-X 1.0).

## Mapeo de campos de cabecera

### Identificación de la factura

| Ruta CII de ZUGFeRD | Campo de DocBits | Campo de Infor BOD | Tipo | Descripción |
| :--- | :--- | :--- | :--- | :--- |
| `ExchangedDocument/ID` | `INVOICE_NUMBER` | `DocumentID` | STRING | Número de factura |
| `ExchangedDocument/TypeCode` | `INVOICE_TYPE_CODE` | `DocumentType` | STRING | Código de tipo de factura |
| `ExchangedDocument/IssueDateTime` | `INVOICE_DATE` | `DocumentDateTime` | DATE | Fecha de emisión de la factura |

### Referencias de documentos

| Ruta CII de ZUGFeRD | Campo de DocBits | Campo de Infor BOD | Tipo | Descripción |
| :--- | :--- | :--- | :--- | :--- |
| `BuyerOrderReferencedDocument/ID` | `PURCHASE_ORDER` | `CustomerOrderID` | STRING | Número de pedido de compra |
| `ContractReferencedDocument/ID` | `CONTRACT_NUMBER` | `ContractID` | STRING | Referencia del contrato |
| `DespatchAdviceReferencedDocument/ID` | `DELIVERY_NOTE` | `ShipmentID` | STRING | Referencia de albarán de entrega |

### Información del proveedor (vendedor)

| Ruta CII de ZUGFeRD | Campo de DocBits | Campo de Infor BOD | Tipo | Descripción |
| :--- | :--- | :--- | :--- | :--- |
| `SellerTradeParty/ID` | `VENDOR_ID` | `SupplierPartyID` | STRING | ID del proveedor |
| `SellerTradeParty/Name` | `VENDOR_NAME` | `SupplierPartyName` | STRING | Nombre del proveedor |
| `SellerTradeParty/PostalTradeAddress/Line1` | `VENDOR_ADDRESS` | `SupplierAddress1` | STRING | Línea de dirección 1 |
| `SellerTradeParty/PostalTradeAddress/PostcodeCode` | `VENDOR_POSTAL_CODE` | `SupplierPostalCode` | STRING | Código postal |
| `SellerTradeParty/PostalTradeAddress/CityName` | `VENDOR_CITY` | `SupplierCity` | STRING | Ciudad |
| `SellerTradeParty/PostalTradeAddress/CountryID` | `VENDOR_COUNTRY` | `SupplierCountryCode` | STRING | Código de país |

## Mapeo de artículos de línea

| Ruta CII de ZUGFeRD | Campo de DocBits | Campo de Infor BOD | Tipo | Descripción |
| :--- | :--- | :--- | :--- | :--- |
| `AssociatedDocumentLineDocument/LineID` | `POSITION` | `LineNumber` | STRING | Número de línea |
| `SpecifiedTradeProduct/BuyerAssignedID` | `ITEM_NUMBER` | `BuyerItemID` | STRING | Número de artículo del comprador |
| `SpecifiedTradeProduct/Name` | `DESCRIPTION` | `ItemDescription` | STRING | Descripción del artículo |
| `BilledQuantity` | `QUANTITY` | `InvoicedQuantity` | NUMBER | Cantidad facturada |
| `NetPriceProductTradePrice/ChargeAmount` | `UNIT_PRICE` | `UnitPrice` | AMOUNT | Precio unitario neto |
| `LineTotalAmount` | `TOTAL_AMOUNT` | `ExtendedAmount` | AMOUNT | Total de la línea |
