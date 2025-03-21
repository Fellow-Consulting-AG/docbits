# Calculate PO unit price

## **Overview**

You can choose to calculate the unit price manually by dividing the net amount by the quantity, instead of automatically extracting it from the document. This is particularly useful when the unit price in the purchase order (in Infor) differs from the price extracted from the document. Such discrepancies may arise if a discount is applied to the unit price in the Infor purchase order, while the document only applies the discount to the net amount.

## **Activation Steps**

1.  Navigate to **Settings** -> **Global Settings** -> **Document Types**.

    <figure><img src="../../../../../.gitbook/assets/Calculate_PO_unit_price_1.png" alt=""><figcaption></figcaption></figure>
2.  Select the desired document type and click on **More Settings**.

    <figure><img src="../../../../../.gitbook/assets/Calculate_PO_unit_price_2.png" alt=""><figcaption></figcaption></figure>
3.  In the **Purchase Order** section, enable the option **Calculate PO Unit Price**.

    <figure><img src="../../../../../.gitbook/assets/Calculate_PO_unit_price_3.png" alt=""><figcaption></figcaption></figure>

## Example:

<figure><img src="../../../../../.gitbook/assets/Calculate_PO_unit_price_4.png" alt="" width="563"><figcaption></figcaption></figure>

In this case, the unit price (without the discount) is extracted from the document, while the purchase order in Infor stores the unit price with the discount applied. This results in a mismatch in the unit price.

Once the setting is activated, the unit price will be recalculated as follows:\
**Unit Price = Net Amount ÷ Quantity**\
This ensures that the unit price is consistent and matches the intended value.
