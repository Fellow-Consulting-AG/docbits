# Duplicate Invoice Handling In DocBits

## Setting to Enable Duplicate Invoice Handling

Go to _Settings → Document Types → Invoice → More Settings_ as shown in the screenshot below

<figure><img src="../../.gitbook/assets/duplicate_invoice handling.png" alt=""><figcaption></figcaption></figure>

The user has two options for detecting duplicate invoices:

1. **Duplicate Document Detection** \
   This feature checks for duplicate documents uploaded to DocBits based on the selected criteria. If the selected criteria match across documents, the system will flag the document as a duplicate.
2.  **Duplicate Invoice Detection**\
    This feature requires Supplier Invoices to be synced from Infor to DocBits. It compares the invoice numbers in the DocBits invoice dashboard with those in Infor. If the same invoice number is uploaded more than once, it will be flagged as a duplicate.

    <mark style="color:red;">**NOTE**</mark><mark style="color:red;">:</mark> Using the **Duplicate Invoice Detection** feature will result in an additional credit charge.

Once the setting is turned on the user can select the criteria for duplicate detection

## Duplicate Invoices on Dashboard

Once Duplicate Detection is enabled in the settings, the dashboard will display an icon for any invoices identified as duplicates based on the specified criteria. Clicking this icon will open the duplicate records in a split-screen view for easy comparison

<figure><img src="../../.gitbook/assets/duplicate_invoice handling2 (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/duplicate_invoice handling2.png" alt=""><figcaption></figcaption></figure>

When the user opens the document a warning bar is shown for the duplicate invoices as shown in the screenshot

<figure><img src="../../.gitbook/assets/duplicate_invoice handling3.png" alt=""><figcaption></figcaption></figure>

\
