# Duplicate Detection

## Enabling Duplicate Detection

To enable duplicate document handling, follow these steps:

1.  Navigate to **Settings** → **Global Settings** → **Document Types**.

    <figure><img src="../../../../../.gitbook/assets/Calculate_PO_unit_price_1.png" alt=""><figcaption></figcaption></figure>
2.  Select the desired **Document Type** and click on **More Settings**.

    <figure><img src="../../../../../.gitbook/assets/Calculate_PO_unit_price_2.png" alt=""><figcaption></figcaption></figure>
3.  Go to the **Duplicate Detection** section.

    <figure><img src="../../../../../.gitbook/assets/DuplicateDocument_3 (1).png" alt=""><figcaption></figcaption></figure>

You have two options for detecting duplicate documents:

1. **Duplicate Document Detection**: \
   This feature checks for duplicate documents uploaded to DocBits based on the selected criteria. If any document matches the selected criteria across other documents, it will be flagged as a duplicate.
2.  **Duplicate Invoice Detection** (Only available for the **Invoice** document type):\
    This feature requires syncing Supplier Invoices from Infor to DocBits. It compares the invoice numbers in the DocBits dashboard with those in Infor. If the same invoice number appears more than once, it will be flagged as a duplicate.

    <mark style="color:red;">**Note**</mark>: Using the **Duplicate Invoice Detection** feature will result in an additional credit charge.

Once the setting is activated, you can select the specific criteria for duplicate detection.

<figure><img src="../../../../../.gitbook/assets/DuplicateDocument_4.png" alt=""><figcaption></figcaption></figure>

## Viewing Duplicate Documents on the Dashboard

After enabling Duplicate Detection, the dashboard will display an icon for any documents identified as duplicates based on the selected criteria. Clicking this icon will open the duplicate records in a split-screen view for easy comparison.

<figure><img src="../../../../../.gitbook/assets/DuplicateDomuent_6.png" alt="" width="329"><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/duplicate_invoice handling2.png" alt=""><figcaption></figcaption></figure>

When viewing a document, a warning bar will appear to indicate that the document is a duplicate

<figure><img src="../../../../../.gitbook/assets/DuplicateDocument_5.png" alt=""><figcaption></figcaption></figure>
