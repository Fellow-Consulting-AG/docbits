# Purchase Order Matching Screen

## Overview

In the **Purchase Order Matching** screen, you can compare the line items extracted from your document with those stored in the **Infor system**, using the purchase order number as the reference.

You can:

* **Immediately identify** any differences between extracted and stored data
* **Set tolerances** to allow acceptable deviations
* **Ignore specific statuses** from Infor, if necessary
* **Approve and export** the document after a successful match
* **Reject** the document if the data does not meet the required validation criteria

This page will guide you through the purchase order matching process and explain all related functionality available in this section.

## Tools in the Purchase Order Matching Screen

At the top of the Purchase Order Matching screen, you’ll find several tools—such as **Save**, **Auto-Match**, **Export**, and others—that assist with the matching process.\
A detailed description of each tool and its functionality can be found [here](purchase-order-matching-tools.md).

<figure><img src="../../../.gitbook/assets/po_match_tools_0.png" alt=""><figcaption></figcaption></figure>

## Filter and Add Purchase Order Numbers

You can search for specific purchase order numbers by entering the number into the search field.\
For more refined filtering, click the icon on the right side of the search bar to select specific criteria for your search.

<figure><img src="../../../.gitbook/assets/po_match_3.png" alt=""><figcaption></figcaption></figure>

The following filter options are available to help you refine your search for purchase orders:

* **Keyword** – Filter by purchase order numbers.
* **Supplier** – Filter by supplier name or ID.
* **After Date** – Show purchase orders created after a specific date.
* **Before Date** – Show purchase orders created before a specific date.
* **Minimum Order Amount** – Filter by minimum order value.
* **Maximum Order Amount** – Filter by maximum order value.
* **Sort By** – Select the attribute to sort the results (e.g., date, amount).
* **Sort Direction** – Choose the sort order: ascending or descending.
* **Number of Records to Display** – Define how many results should be shown per page.
* **More** – Additional filtering options include:
  * **Delivery Number**
  * **Packing Slip Number**
  * **Item ID**

After configuring your filters, click **"Apply"** to apply them or **"Clear"** to reset all filter settings.

The matching purchase orders will be displayed based on the applied filters.\
You can either:

* **Adjust the filters** and search again, or
* **Double-click** on a purchase order entry to add it to the Purchase Order Matching screen.

<figure><img src="../../../.gitbook/assets/po_match_5 (2).png" alt=""><figcaption></figcaption></figure>

## Select Purchase Order Numbers and Rearrange Columns

You can switch between individual purchase orders to view their respective line items by clicking on the purchase order number at the top of the table.

You can also rearrange the columns within each purchase order view by simply dragging and dropping them into your preferred order.

<figure><img src="../../../.gitbook/assets/po_match_7.png" alt=""><figcaption></figcaption></figure>

To permanently hide specific columns, use the [**Set PO Table Columns for Organizations**](./#set-po-table-columns-for-organizations) feature.

## Set PO Table Columns for Organizations

You have the option to hide or show specific columns in the purchase order table by clicking the column settings icon (shown below).\
This setting is available in both the **Purchase Order Matching** screen and the **Advanced Purchase Order Search** menu.

<figure><img src="../../../.gitbook/assets/po_tools_new_10.png" alt=""><figcaption></figcaption></figure>

Additional details can be found [here](purchase-order-matching-tools.md).

## Re-Sync purchase order number with Infor

To resynchronize the data in **DocBits** with the data from **Infor**, click the **refresh button** next to the purchase order number above the table.

<figure><img src="../../../.gitbook/assets/po_match_8 (1).png" alt=""><figcaption></figcaption></figure>

If your matching process is based on the **Received Delivery Open Quantity** attribute, you also have the option to perform a **manual synchronization**, as described in detail [here](purchase-order-matching-tools.md#sync-data).

<figure><img src="../../../.gitbook/assets/po_tools_new_7.png" alt=""><figcaption></figcaption></figure>

## How to match?

To match a purchase order line item with a line item extracted from the document, you have three options:

1. **Drag and Drop**\
   Drag the desired purchase order line item and drop it onto the corresponding line item in the extracted table.
2. **Right-Click and Connect**
   * Right-click the purchase order line item you want to match and select **"Select for match"**.
   * Then, right-click the corresponding line item in the extracted table and select **"Connect"**.
3.  **Auto Match**

    Click the **Auto Match** button to let the system automatically attempt to match all line items based on the extracted and purchase order data.

    <figure><img src="../../../.gitbook/assets/po_tools_new_5.png" alt=""><figcaption></figcaption></figure>

You can also select **multiple purchase order lines** and match them to a **single line** in the extracted table.

## Which columns are being matched?

The Purchase Order Matching process matches only specific columns. The list below outlines which columns are matched, if available. If no [tolerance](./#accept-tolerances) is set, the columns will only match if they are an exact (100%) match.

* [Quantity](./#quantity) (Quantity | Received Quantity | Received Delivery Open Quantity)
* Unit Price
* Purchase Order Number
* Item Number/Supplier Item ID
* Promised Delivery Date

### Quantity

You have three options for matching the quantity.&#x20;

* Quantity&#x20;
* Received Quantity
* Received Delivery Open Quantity&#x20;

You can set this option in **Settings → Global Settings → Document Types → More Settings → Purchase Order Section → Purchase Order**

## Accept Tolerances

You can specify acceptable tolerance levels during the matching process.\
By default, only exact (100%) matches are considered valid.

If tolerances are configured in the system settings, you can adjust them for the allowed attributes directly in the **Extracted Table** under the **Actions** column.

<figure><img src="../../../.gitbook/assets/po_match_11.png" alt=""><figcaption></figcaption></figure>

For more information on configuring and using tolerances, see the [detailed documentation](../../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-tolerance-settings-additional-purchase-order-tolerance.md).

## Disable statuses

You can exclude specific lines with certain statuses from being matched. For more information, refer to the [detailed documentation](../../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-disable-statuses.md).

## Verify matched lines

Several indicators are available to help you verify whether a line item has been successfully matched or not.

### Purchase Order Table

<figure><img src="../../../.gitbook/assets/po_match_14.png" alt=""><figcaption></figcaption></figure>

* This icon indicates that the purchase order line item has been successfully matched.

<figure><img src="../../../.gitbook/assets/guide_po_2.png" alt=""><figcaption></figcaption></figure>

* This icon indicates that the purchase order line item contains a mismatch.

<figure><img src="../../../.gitbook/assets/guide_po_5.png" alt=""><figcaption></figcaption></figure>

### Extracted Table from the Document

*   This icon indicates that the line item has been successfully matched. You can hover over the icon to highlight the corresponding purchase order line.

    <figure><img src="../../../.gitbook/assets/po_match_15.png" alt=""><figcaption></figcaption></figure>
*   This icon indicates that the line item contains a mismatch. You can hover over the icon to highlight the corresponding purchase order line and view the columns where mismatches occur.

    <figure><img src="../../../.gitbook/assets/po_match_2 (1).png" alt=""><figcaption></figcaption></figure>

## Multi Matches

If a single line item is matched to multiple lines, you can view detailed information by clicking the plus (+) icon next to the respective line item.

This expands the view to show all matched entries, helping you verify and manage multiple matches effectively.

<figure><img src="../../../.gitbook/assets/po_match_19.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/po_match_18.png" alt=""><figcaption></figcaption></figure>



## Remove PO Connections

To remove a connection between a purchase order line item and an extracted line item, simply click the **X** icon next to the matched pair.\
Once removed, the connection is canceled, and the line item becomes available for matching again.

<figure><img src="../../../.gitbook/assets/po_match_new_2 (1).png" alt=""><figcaption></figcaption></figure>

## Calculation

Below the table containing the information extracted from your document, you can find simple calculations to verify whether the total bookings match.

<figure><img src="../../../.gitbook/assets/image (441).png" alt="" width="423"><figcaption></figcaption></figure>

### Recorded bookings:

This is calculated based on the recorded Purchase Order number using the following formula:

```
Recorded bookings = UNIT PRICE * QUANTITY (based on the purchase order)
```

### Matched total:

This is calculated based on the amount extracted from the document using the following formula:

```
 Matched total = UNIT PRICE * QUANTITY (based on the document)
```

### **Charges:**

In this section, any applicable charges will be added if they are present.

### Unsettled amount:

The resulting difference is displayed here and is calculated as follows:

```
Unsettled amount = Recorded bookings - Matched total - Charges
```

## Viewing the Document for Validation

On the right side of the **Purchase Order Matching** screen, you can view the document to assist with validation.

<figure><img src="../../../.gitbook/assets/po_new_1.png" alt=""><figcaption></figcaption></figure>

**Document Viewer Toolbar Features:**

* Scroll through the document pages to review content.
* Click the file name to open the full validation screen.
* Enter a page number and press Enter to jump directly to that page.
* Use the plus (+) and minus (–) buttons to zoom in or out of the document.
*   Click the button on the far right to open the document in a separate window, which is especially useful when working with multiple screens.

    <figure><img src="../../../.gitbook/assets/po_match_10.png" alt=""><figcaption></figcaption></figure>

## Saving Changes:

To save your changes, click the **Save** button in the toolbar.\
If you leave the page without saving, all progress made during the matching process will be lost.

<figure><img src="../../../.gitbook/assets/po_tools_new_6.png" alt=""><figcaption></figcaption></figure>

## Exporting the Document

After matching all line items and validating their correctness, you can export the document by clicking the **Export** button in the toolbar.

* Clicking the small arrow next to the **Export** button reveals all available export options.
* Clicking **Export** directly will trigger the default export option (the first one in the list).

<figure><img src="../../../.gitbook/assets/po_tools_new_8.png" alt=""><figcaption></figcaption></figure>
