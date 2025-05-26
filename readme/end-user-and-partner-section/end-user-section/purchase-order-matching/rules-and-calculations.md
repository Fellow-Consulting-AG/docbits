# Rules and Calculations

## Matched Columns&#x20;

The Purchase Order Matching process only matches specific columns. This section details which columns are matched for each document type.

| Invoice                                           | Order Conformation                                | Delivery Note                                     |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| Quantity                                          | Quantity                                          | Quantity                                          |
| Open Quantity                                     | Open Quantity                                     | Unit Price                                        |
| Unit Price                                        | Promised Delivery Note                            | Promised Delivery Note                            |
| Item Number<mark style="color:red;">**\***</mark> | Item Number<mark style="color:red;">**\***</mark> | Promised Data                                     |
|                                                   |                                                   | Item Number<mark style="color:red;">**\***</mark> |

| Customer Order                                    | E-Invoice                                         |
| ------------------------------------------------- | ------------------------------------------------- |
| Quantity                                          | Quantity                                          |
| Open Quantity                                     | Open Quantity                                     |
| Unit Price                                        | Unit Price                                        |
| Item Number<mark style="color:red;">**\***</mark> | Item Number<mark style="color:red;">**\***</mark> |

<mark style="color:red;">**Note:**</mark> The _Item Number_ column is only matched when the Purchase Order Matching is triggered using the [_Auto PO Match_](purchase-order-matching-tools.md#auto-po-match) button.

## Calculation

Below the table containing the information extracted from your document, you can find simple calculations to verify whether the total bookings match.

<figure><img src="../../../.gitbook/assets/image (441).png" alt="" width="423"><figcaption></figcaption></figure>

### Recorded bookings:

This is calculated based on the recorded Purchase Order number using the following formula\
**UNIT PRICE \* QUANTITY**

### Matched total:

This is calculated based on the amount extracted from the document using the following formula:\
**UNIT PRICE \* QUANTITY**

### **Charges:**

In this section, any applicable charges will be added if they are present.

### Unsettled amount:

The resulting difference is displayed here and is calculated as follows:\
**Recorded bookings - Matched total**&#x20;

