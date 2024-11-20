# Compare Order Confirmation with Purchase order

<figure><img src="../../../../.gitbook/assets/image (8) (1).png" alt=""><figcaption></figcaption></figure>

## **Purpose**:

This DocBits card allows for a detailed comparison of specific order data—such as quantity, discount, or unit price—between an order confirmation and a purchase order. This ensures consistency and accuracy across key data points, which is critical for maintaining reliable order records.

## **Functionality**:

* **Order Data Comparison**: This card compares specified fields (such as quantity, discount, or unit price) between the order confirmation and the purchase order.
* **Any/All Selection**: Users can specify whether the comparison should verify **any** (at least one field matches) or **all** (all selected fields match) order data fields.
* **Order Data Fields**: The fields available for comparison include:
  * **Quantity**: Verifies the quantity ordered against the confirmed order.
  * **Discount**: Checks that any discounts applied in the confirmation align with those in the purchase order.
  * **Unit Price**: Ensures that the unit price in the confirmation is consistent with the purchase order.
* **Operator**: Users can set conditions for how the selected data fields should be compared. Available operators include:
  * **Equals (=)**: Confirms that the value in the order confirmation matches the purchase order.
  * **Not Equal (≠)**: Ensures the value in the order confirmation does not match the purchase order.
  * **Greater Than (>)**: Checks if the value in the order confirmation exceeds the purchase order’s value.
  * **Greater or Equals (≥)**: Checks if the value in the order confirmation equals to or exceeds the purchase order’s value.
  * **Less Than (<)**: Confirms that the value in the order confirmation is below the purchase order’s value.
  * **Less or Equals (≤)**: Confirms that the value in the order confirmation is below or equals to the purchase order’s value.

## **Usage**:

This card is particularly useful for procurement teams and order management specialists who need to verify that order confirmations adhere to agreed terms in the purchase order. By comparing critical fields, they can detect discrepancies early in the process, reducing the risk of fulfillment errors.

## **Example Scenario**:

* An order confirmation lists a quantity of 100 units, a unit price of $25, and a 10% discount. The purchase order reflects the same values. Using the "All" option and the "Equals" operator, the card confirms that all specified data in the order confirmation aligns with the purchase order, ensuring consistency.

By using the "Compare with Purchase Order: Order Data" card, businesses can automate the verification of essential order details, improving accuracy in order fulfillment and financial reconciliation.
