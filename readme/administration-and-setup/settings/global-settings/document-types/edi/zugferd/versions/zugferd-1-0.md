# Mapeamento de campos ZUGFeRD 1.0

## Visão geral

O ZUGFeRD 1.0 foi a versão inicial do padrão. Embora seja antiga, muitos documentos ainda usam esse formato. O DocBits oferece suporte total para a extração de dados de arquivos XML do ZUGFeRD 1.0.

## Mapeamento de campos de cabeçalho

### Identificação da fatura

| Caminho ZUGFeRD CII | Campo DocBits | Campo Infor BOD | Tipo | Descrição |
| :--- | :--- | :--- | :--- | :--- |
| `ExchangedDocument/ID` | `INVOICE_NUMBER` | `DocumentID` | STRING | Número da fatura |
| `ExchangedDocument/TypeCode` | `INVOICE_TYPE_CODE` | `DocumentType` | STRING | Código do tipo de fatura |
| `ExchangedDocument/IssueDateTime` | `INVOICE_DATE` | `DocumentDateTime` | DATE | Data de emissão da fatura |

### Referências de documentos

| Caminho ZUGFeRD CII | Campo DocBits | Campo Infor BOD | Tipo | Descrição |
| :--- | :--- | :--- | :--- | :--- |
| `BuyerOrderReferencedDocument/ID` | `PURCHASE_ORDER` | `CustomerOrderID` | STRING | Número do pedido de compra |
| `ContractReferencedDocument/ID` | `CONTRACT_NUMBER` | `ContractID` | STRING | Referência do contrato |
| `DespatchAdviceReferencedDocument/ID` | `DELIVERY_NOTE` | `ShipmentID` | STRING | Referência da nota de entrega |

### Informações do fornecedor (vendedor)

| Caminho ZUGFeRD CII | Campo DocBits | Campo Infor BOD | Tipo | Descrição |
| :--- | :--- | :--- | :--- | :--- |
| `SellerTradeParty/ID` | `VENDOR_ID` | `SupplierPartyID` | STRING | ID do fornecedor |
| `SellerTradeParty/Name` | `VENDOR_NAME` | `SupplierPartyName` | STRING | Nome do fornecedor |
| `SellerTradeParty/PostalTradeAddress/Line1` | `VENDOR_ADDRESS` | `SupplierAddress1` | STRING | Linha de endereço 1 |
| `SellerTradeParty/PostalTradeAddress/PostcodeCode` | `VENDOR_POSTAL_CODE` | `SupplierPostalCode` | STRING | Código postal |
| `SellerTradeParty/PostalTradeAddress/CityName` | `VENDOR_CITY` | `SupplierCity` | STRING | Cidade |
| `SellerTradeParty/PostalTradeAddress/CountryID` | `VENDOR_COUNTRY` | `SupplierCountryCode` | STRING | Código do país |

## Mapeamento de itens de linha

| Caminho ZUGFeRD CII | Campo DocBits | Campo Infor BOD | Tipo | Descrição |
| :--- | :--- | :--- | :--- | :--- |
| `AssociatedDocumentLineDocument/LineID` | `POSITION` | `LineNumber` | STRING | Número da linha |
| `SpecifiedTradeProduct/BuyerAssignedID` | `ITEM_NUMBER` | `BuyerItemID` | STRING | Número do item do comprador |
| `SpecifiedTradeProduct/Name` | `DESCRIPTION` | `ItemDescription` | STRING | Descrição do item |
| `BilledQuantity` | `QUANTITY` | `InvoicedQuantity` | NUMBER | Quantidade faturada |
| `NetPriceProductTradePrice/ChargeAmount` | `UNIT_PRICE` | `UnitPrice` | AMOUNT | Preço unitário líquido |
| `LineTotalAmount` | `TOTAL_AMOUNT` | `ExtendedAmount` | AMOUNT | Total da linha |
