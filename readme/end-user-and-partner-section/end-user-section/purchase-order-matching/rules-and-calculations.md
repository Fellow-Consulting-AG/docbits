# Rules and Calculations

## Matched Columns&#x20;

The Purchase Order Matching process only matches specific columns. This section details which columns are matched for each document type.

| Invoice                                           | Order Conformation                                | Delivery Note                                     |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| Quantity                                          | Quantity                                          | Quantity                                          |
| Unit Price                                        | Promised Delivery Note                            | Promised Delivery Note                            |
| Item Number<mark style="color:red;">**\***</mark> | Item Number<mark style="color:red;">**\***</mark> | Item Number<mark style="color:red;">**\***</mark> |

| Customer Order                                    | E-Invoice                                         |
| ------------------------------------------------- | ------------------------------------------------- |
| Quantity                                          | Quantity                                          |
| Unit Price                                        | Unit Price                                        |
| Item Number<mark style="color:red;">**\***</mark> | Item Number<mark style="color:red;">**\***</mark> |

<mark style="color:red;">**\*Note:**</mark> The _Item Number_ column is only matched when the Purchase Order Matching is triggered using the [_Auto PO Match_](purchase-order-matching-tools.md#auto-po-match) button.

## Quantity

You have three options for matching the quantity.&#x20;

* Quantity&#x20;
* Received Quantity
* Received Delivery Quantity&#x20;

You can set this option in **Settings → General Settings → Document Types → More Settings → Purchase Order Section → Purchase Order**

## Accept Tolerances

You can specify that a particular tolerance is acceptable during the matching process. By default, only exact (100%) matches are considered valid. For more information, see the [detailed documentation](../../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order-tolerance-settings-additional-purchase-order-tolerance.md).

## Disable statuses

You can prevent specific statuses from being matched. For more information, see the [detailed documentation](../../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order-disable-statuses.md).

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

