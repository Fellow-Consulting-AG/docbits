# Architecture

Cloud customer:

<figure><img src="../../.gitbook/assets/image (264).png" alt=""><figcaption></figcaption></figure>

On premise:

<figure><img src="../../.gitbook/assets/image (263).png" alt=""><figcaption></figcaption></figure>

Doc**Bits** seamlessly integrates with Infor LN/M3 through ION API, ION Desk, and Infor Standard BODs. Our API integration allows us to export data to Infor and perform master data validation in Doc**Bits**.

## Exporting Data to Infor

We use the ION API to send the PDF with attributes to IDM and the BOD Sync.CaptureDocument to ION Desk. In ION Desk, we transform the [Sync.CaptureDocument](../../infor-integration-and-configuration/exporting-in-docbits/) to the desired target BODs based on the document type being processed. These transformed Infor BODs are then automatically imported to LN or M3.

{% hint style="info" %}
Export to [Infor](../../infor-integration-and-configuration/exporting-to-infor/)
{% endhint %}

## Master Data Validation in DocBits

To identify the supplier or compare/match purchase order lines, we activate a trigger in LN/M3 that sends the Sync.RemitToPartyMaster, Sync.SupplierPartyMaster, and Sync.PurchaseOrder BODs to Doc**Bits**. We configure this process in ION Desk by defining the dataflow to a specific connection point to Doc**Bits**.

<figure><img src="../../.gitbook/assets/docbits_architecture (1).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
[Master Data Validation](../../infor-integration-and-configuration/importing-customer-master-data/)
{% endhint %}
