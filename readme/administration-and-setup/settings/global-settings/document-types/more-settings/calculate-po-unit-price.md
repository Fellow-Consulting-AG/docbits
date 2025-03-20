# Calculate PO unit price

## **Overview**

The unit price is typically extracted directly from the document. However, discrepancies can occur between the extracted unit price and the one stored in Infor due to discounts. In these cases, you can manually calculate the unit price using the quantity and net amount to prevent errors during the PO matching process. The following steps outline how to activate this setting.

## **Activation Steps**

1.  Navigate to **Settings** -> **Global Settings** -> **Document Types**.

    <figure><img src="../../../../../.gitbook/assets/Calculate_PO_unit_price_1.png" alt=""><figcaption></figcaption></figure>
2.  Select the desired document type and click on **More Settings**.

    <figure><img src="../../../../../.gitbook/assets/Calculate_PO_unit_price_2.png" alt=""><figcaption></figcaption></figure>
3.  In the **Purchase Order** section, activate the option **Calculate PO Unit Price**.

    <figure><img src="../../../../../.gitbook/assets/Calculate_PO_unit_price_3.png" alt=""><figcaption></figcaption></figure>

## Example:

<figure><img src="../../../../../.gitbook/assets/Calculate_PO_unit_price_4.png" alt="" width="563"><figcaption></figcaption></figure>

In this example, the unit price extracted from the document does not include the discount, while the unit price stored in Infor does. As a result, there will be a mismatch between the extracted unit price and the one in the system.

Once the setting is activated, the unit price will be automatically recalculated as follows:

**NET AMOUNT / QUANTITY**

This ensures that the unit price aligns correctly, avoiding any discrepancies during the PO matching process.
