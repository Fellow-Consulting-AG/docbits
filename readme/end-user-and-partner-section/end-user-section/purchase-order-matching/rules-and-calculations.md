# Rules and Calculations

On this page, you can find which columns are matched, the rules they follow, and how the resulting calculation is performed.

## Matched Columns&#x20;

The Purchase Order Matching process matches only specific columns. The list below outlines which columns are matched, if available. If no [tolerance](rules-and-calculations.md#accept-tolerances) is set, the columns will only match if they are an exact (100%) match.

* [Quantity](rules-and-calculations.md#quantity) (Quantity | Received Quantity | Received Delivery Quantity)
* Unit Price
* Purchase Order Number
* Item Number
* Supplier Item ID
* Promised Delivery Date

## Quantity

You have three options for matching the quantity.&#x20;

* Quantity&#x20;
* Received Quantity
* Received Delivery Quantity&#x20;

You can set this option in **Settings → General Settings → Document Types → More Settings → Purchase Order Section → Purchase Order**

## Accept Tolerances

You can specify that a particular tolerance is acceptable during the matching process. By default, only exact (100%) matches are considered valid. For more information, see the [detailed documentation](../../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order-tolerance-settings-additional-purchase-order-tolerance.md).

## Disable statuses

You can exclude specific lines with certain statuses from being matched. For more information, refer to the [detailed documentation](../../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order-disable-statuses.md).

## Calculation

Below the table containing the information extracted from your document, you can find simple calculations to verify whether the total bookings match.

<figure><img src="../../../.gitbook/assets/image (441).png" alt="" width="423"><figcaption></figcaption></figure>

### Recorded bookings:

This is calculated based on the recorded Purchase Order number using the following formula\
**UNIT PRICE \* QUANTITY (based on the purchase order)**

### Matched total:

This is calculated based on the amount extracted from the document using the following formula:\
**UNIT PRICE \* QUANTITY (based on the document)**

### **Charges:**

In this section, any applicable charges will be added if they are present.

### Unsettled amount:

The resulting difference is displayed here and is calculated as follows:\
**Recorded bookings - Matched total - Charges**

