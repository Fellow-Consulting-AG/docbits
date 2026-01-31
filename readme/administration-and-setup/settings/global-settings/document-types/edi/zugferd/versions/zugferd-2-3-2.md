# ZUGFeRD 2.3.2 Field Mapping

## Overview

ZUGFeRD 2.3.2 is a maintenance release of the 2.3 standard, ensuring compatibility with the latest CII updates.

## Header Field Mapping

### Invoice Identification

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `ExchangedDocument/ID` | `INVOICE_NUMBER` | `DocumentID` | STRING | Invoice number |
| `ExchangedDocument/IssueDateTime` | `INVOICE_DATE` | `DocumentDateTime` | DATE | Invoice issue date |

### Tax Breakdown

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `ApplicableTradeTax[1]/RateApplicablePercent` | `TAX_RATE` | `TaxPercent` | NUMBER | Tax rate 1 |
| `ApplicableTradeTax[1]/BasisAmount` | `NET_AMOUNT` | `TaxableAmount` | AMOUNT | Net amount for tax 1 |
| `ApplicableTradeTax[1]/CalculatedAmount` | `TAX_AMOUNT` | `TaxAmount` | AMOUNT | Tax amount 1 |

## Line Item Mapping

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `AssociatedDocumentLineDocument/LineID` | `POSITION` | `LineNumber` | STRING | Line number |
| `SpecifiedTradeProduct/Name` | `DESCRIPTION` | `ItemDescription` | STRING | Item description |
| `BilledQuantity` | `QUANTITY` | `InvoicedQuantity` | NUMBER | Billed quantity |
| `NetPriceProductTradePrice/ChargeAmount` | `UNIT_PRICE` | `UnitPrice` | AMOUNT | Net unit price |
| `LineTotalAmount` | `TOTAL_AMOUNT` | `ExtendedAmount` | AMOUNT | Line total |
