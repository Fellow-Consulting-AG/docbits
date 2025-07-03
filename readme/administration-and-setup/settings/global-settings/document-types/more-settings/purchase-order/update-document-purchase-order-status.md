# Update Document Purchase Order Status

## Overview

When enabled, the **PO Status** column on the dashboard is automatically updated whenever the status of the purchase order changes.

## Where to Activate

1. Go to: **Settings** → **Global Settings** → **Document Type**&#x20;
2.  Select the desired document type and click on **More Settings**.\


    <figure><img src="../../../../../../.gitbook/assets/image (20).png" alt=""><figcaption></figcaption></figure>
3.  In the **Purchase Order** section, navigate to the **Update Document Purchase Order Status** option.\


    <figure><img src="../../../../../../.gitbook/assets/image (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## How It Works

When this setting is enabled, the **PO Status** column on the dashboard will automatically reflect the current status of the purchase order.\
For example, if the PO status is updated to _Received_ or _Invoiced_, the dashboard column will update accordingly to show this new status.

<div align="left"><figure><img src="../../../../../../.gitbook/assets/Status on Dashboard.jpg" alt="" width="307"><figcaption></figcaption></figure></div>

## Setting It Up

1. **Enable the Setting**\
   Navigate to the location mentioned above and toggle the setting on.
2. **Add the PO Status Column (if not visible)**\
   If the **PO Status** column is not already visible on the dashboard:
   *   Go to: **Advanced Settings** → **Set Table Columns for Organizations**\


       <figure><img src="../../../../../../.gitbook/assets/image (2) (1) (1).png" alt=""><figcaption></figcaption></figure>
   * Add the field from the document type by searching for **PO Status**
3. **Configure lookup configuration**
   *   Configure the Status field in the Purchase order header lookup like this:\


       <figure><img src="../../../../../../.gitbook/assets/image (462).png" alt=""><figcaption></figcaption></figure>
   * <mark style="color:red;">**Note:**</mark>**&#x20;Purchase order needs to be on Auto Trigger otherwise Status updates may not update properly**&#x20;
   * Don't know how to **Configure lookup configuration? Here is the** [**lookup configuration guide**](../../../../../setup/document-types/fuzzy-data-configuration-with-master-data.md)\

4. **Verify**\
   Receive or invoice a PO, then check the dashboard to confirm that the status is updated correctly.\
