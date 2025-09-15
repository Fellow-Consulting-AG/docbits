# Duplicate Detection

## Overview

In **DocBits**, you can filter for duplicate documents by specifying which fields must match and by defining a time interval during which duplicates should be detected.

This page provides a detailed guide on how to enable and use the **Duplicate Detection** feature effectively.

## Enabling Duplicate Detection

To enable duplicate document detection in **DocBits**, follow these steps:

1.  Navigate to **Settings** → **Global Settings** → **Document Types**.

    <figure><img src="../../../../../.gitbook/assets/Calculate_PO_unit_price_1.png" alt=""><figcaption></figcaption></figure>
2.  Select the desired **Document Type** and click on **More Settings**.

    <figure><img src="../../../../../.gitbook/assets/Calculate_PO_unit_price_2.png" alt=""><figcaption></figcaption></figure>
3.  Go to the **Duplicate Detection** section.

    <figure><img src="../../../../../.gitbook/assets/DuplicateDocument_3.png" alt=""><figcaption></figcaption></figure>

DocBits provides two options for identifying duplicate documents:

1. **Duplicate Document Detection**: \
   This feature checks for duplicate documents uploaded to **DocBits** based on the selected criteria. If any document matches the selected criteria across other documents, it will be flagged as a duplicate.
2.  **Duplicate Invoice Detection** (Only available for the **Invoice** document type):\
    This feature requires syncing Supplier Invoices from Infor to DocBits. It compares the invoice numbers in the DocBits dashboard with those in Infor. If the same invoice number appears more than once, it will be flagged as a duplicate.

    <mark style="color:red;">**Note**</mark>: Using the **Duplicate Invoice Detection** feature will result in an additional credit charge.

## Filter which documents should be detected as duplicate

Once **Duplicate Detection** is enabled, two dropdown menus will be available for configuration:

*   **Duplicate Detection Fields**\
    Select the fields that should be used to identify duplicates (e.g., Supplier ID, Date, Invoice Number, etc.). Documents matching these fields will be flagged as duplicates.

    <figure><img src="../../../../../.gitbook/assets/DuplicateDocument_4.png" alt=""><figcaption></figcaption></figure>
*   **Duplicate Detection Interval**

    Use this setting to define the time range within which duplicates are detected. Documents uploaded within the selected interval will be compared against each other based on the selected fields.

    **Available options:**

    * 1 Month
    * 3 Months (Recommended)
    * 6 Months
    * 1 Year

    <mark style="color:red;">**Note**</mark>: A 3-month interval is recommended to ensure optimal performance. Selecting a longer interval may lead to slower dashboard loading times.

    <figure><img src="../../../../../.gitbook/assets/DuplicateDocument_6.png" alt=""><figcaption></figcaption></figure>

## Viewing Duplicate Documents on the Dashboard

Once Duplicate Detection is enabled, any documents identified as duplicates will display the **Show Duplicates** icon on the dashboard.

*   Click the **Show Duplicates** icon to open duplicate records in a side-by-side split-screen view for easy comparison.

    <figure><img src="../../../../../.gitbook/assets/DuplicateDocument_7.png" alt=""><figcaption></figcaption></figure>
*   When viewing a flagged document, a warning bar will appear at the top, indicating that the document is a duplicate.

    <figure><img src="../../../../../.gitbook/assets/DuplicateDocument_5.png" alt=""><figcaption></figcaption></figure>
