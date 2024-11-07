# Confirmed Delivery Date

<figure><img src="../../../../.gitbook/assets/image (8) (1).png" alt=""><figcaption></figcaption></figure>

## **Purpose:**

This DocBits card is designed to ensure that the confirmed delivery dates on invoices or shipping documents align with the accepted delivery dates as stipulated in the master data lookup table. It helps manage expectations and adherence to scheduled deliveries within the supply chain.

## **Functionality:**

* **Confirmed Delivery Date:** This component of the card captures the delivery date as confirmed on the invoice or shipping documentation.
* **Master Data Table Lookup:** The card references a master data lookup table specified by the user (identified by the \<Master Data Table> parameter). This table contains the accepted delivery dates for comparison.
* **Operator Value:** Users can specify how the confirmed delivery date should compare to the accepted delivery date from the master data table. Available operators include:
  * **Is**: Confirms that the confirmed delivery date **is** the same as the accepted delivery date in the master data.
  * **Is Not**: Ensures that the confirmed delivery date **is not** the same as the accepted delivery date.

## **Usage:**&#x20;

This card is invaluable for ERP Managers and financial accountants who need to monitor and ensure compliance with delivery schedules. It is particularly useful in sectors where timely delivery is critical, such as manufacturing, retail, and distribution.

## Example Scenario:

* An invoice lists a confirmed delivery date of June 10th. The master data table, however, shows an accepted delivery date of June 15th. Setting the operator to "Before," the card confirms that the goods are scheduled for early delivery, allowing logistics planning to adjust accordingly.

By implementing the "Compare with Purchase Order: Confirmed vs. Accepted Delivery Dates" card, organizations can proactively manage their supply chain, ensuring that deliveries are planned and executed in accordance with agreed-upon timelines, thus enhancing operational efficiency and customer satisfaction.
