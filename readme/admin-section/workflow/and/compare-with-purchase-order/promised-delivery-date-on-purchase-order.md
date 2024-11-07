# Promised Delivery Date on Purchase Order

<figure><img src="../../../../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

## **Purpose**:

This DocBits card is designed to enable the precise comparison of promised delivery dates on purchase orders against the dates specified for line items in a table. It helps ensure that expected delivery timelines are met, providing an additional layer of assurance for inventory planning and customer satisfaction.

## **Functionality:**

* **Promised Delivery Date with Tolerance**: This card compares the promised delivery date on the purchase order with the delivery dates for line items in the table. A tolerance in days can be specified, allowing a margin of error in the delivery date comparison.
* **Operator**: Users can set specific conditions for comparing the promised delivery dates. Available operators include:
  * **Equals (=)**: Checks if the promised delivery date on the line item matches the purchase order’s delivery date.
  * **Not Equal (≠)**: Ensures the promised delivery date on the line item does not match the date on the purchase order.
  * **Greater Than (>)**: Validates that the promised delivery date on the line item is later than the purchase order’s date.
  * **Greater or Equals (≥)**: Validates that the promised delivery date on the line item equals to or is later than the purchase order’s date.
  * **Less Than (<)**: Confirms that the promised delivery date on the line item is earlier than the purchase order’s date.
  * **Less or Equals (≤):** Confirms that the promised delivery date on the line item equals to or is earlier than the purchase order’s date.
* **Tolerance (Value)**: Users can specify a number of days as tolerance to allow minor variations in the delivery date without triggering an alert. This helps account for minor delays or advances that are still within acceptable limits.

## **Usage**:

This card is particularly useful for supply chain managers and purchasing teams who need to monitor vendor performance and ensure adherence to agreed delivery timelines. By setting a tolerance, users can avoid flagging minor deviations that do not impact overall operations.

## **Example Scenario**:

* A purchase order specifies a promised delivery date of December 1st. The line item has a delivery date of December 3rd. With a tolerance value set to 2 days and using the “Equals” operator, the card considers this delivery date within the acceptable range, ensuring that small variances are tolerated.

By implementing the "Compare with Purchase Order: Promised Delivery Date" card, businesses can enhance their supply chain reliability by ensuring that delivery dates align with expectations, thereby reducing potential disruptions.
