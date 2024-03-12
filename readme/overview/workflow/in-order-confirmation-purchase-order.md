# In Order Confirmation Purchase Order

### Logic: In Order Confirmation Purchase Order

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-03-12 um 19.50.53.png" alt=""><figcaption></figcaption></figure>

#### Logic Card: Quantity or Unit Price or Discount Match

This logic card is designed to automatically verify that the quantity, unit price, or discount detailed in an order confirmation matches the corresponding figures in the purchase order. This verification ensures consistency and accuracy between what was ordered and what the supplier confirms to deliver.

#### Trigger Condition

The logic is activated when any of the following conditions are met in an order confirmation relative to the original purchase order:

* **Quantity**: The quantity of items ordered matches the quantity confirmed by the supplier.
* **Unit Price**: The price per item agreed upon matches the supplier's confirmation.
* **Discount**: Any discounts applied are consistent between the purchase order and the order confirmation.

#### Outcomes

* **Equals**: If the order confirmation's quantity, unit price, or discount exactly matches the purchase order, the system considers the confirmation as valid and proceeds with the next steps in the procurement process.
* **Not Equal**: If there's a discrepancy in the quantity, unit price, or discount, the system flags the order confirmation for manual review. This ensures any mismatches are resolved before moving forward.

#### Benefits

* **Accuracy and Consistency**: Maintains accuracy in the procurement process, ensuring that payments and deliveries are made based on correct figures.
* **Efficiency**: Automates the verification process, reducing the need for manual checks and speeding up order processing.
* **Cost Control**: Helps prevent overpayments or incorrect deliveries by catching discrepancies early in the process.

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-03-12 um 19.59.01.png" alt=""><figcaption></figcaption></figure>

1. **Define Comparison Parameters**: Set up the specific fields (quantity, unit price, discount) that the logic card will check for a match.
2. **Automate Verification**: Configure the system to automatically compare these details upon receipt of an order confirmation.
3. **Customize Alerts**: Decide on the workflow for handling discrepancies, including customization of alerts for manual review.

This logic card is vital for ensuring that the details of an order confirmation align with the original purchase order, safeguarding the integrity of the procurement cycle. \`\`
