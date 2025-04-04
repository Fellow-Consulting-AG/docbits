# Creating an IDM Mapping File

## Required Fields for IDM Mapping File

When creating an IDM mapping file, the following fields are required:

* **Document Type Definition**
  * Ensure the document type code in DocBits matches the name used in the URL of the field settings, similar to the BOD Mapping File.
  * Verify that the document type name in IDM aligns with your system configuration. For example, in M3, it may be **M3\_SupplierInvoice**, while in LN, it will be different based on your setup.
    * A Guide on how to navigate in IDM can be found at Document Manager in IDM on this page.

```properties
#Define Name of document
#Example: <DocBitsDocumentType>=<IDMDocumentType>
#INVOICE=LN_SupplierInvoice
INVOICE=M3_SupplierInvoice
```

*   **Static Values**

    * First, define all static values in a single line using the **Static\_Values** key:

    ```properties
    Static_Values=FileNameSeparator,ACLString
    ```

    * Then, assign values to each static variable using the **SV\_** prefix:

    ```properties
    SV_FileNameSeparator=_ 
    SV_ACLString=Public
    ```

```properties
#Define mappings for the static values
#Example: Static_Values=<StaticVariableName>
Static_Values=FileNameSeparator,ACLString
#Example: SF_<StaticVariableName> = StaticValue
SV_FileNameSeparator=_
SV_ACLString=Public
```

* **ACL Field Definition**

```properties
#Define ACL Field value
#Example: ACL_Fields= Concatenation of other defined fields that together should be a valid ACL in IDM
ACL_Fields=SV_ACLString
```

* **Searchable Name in IDM**&#x20;
  * The **Searchable PDF Name** will be the document name in IDM.

```properties
#Define Resource Mapping
#Example: Searchable_PDF_Name= Concatenation of other defined fields
Searchable_PDF_Name=IF_INVOICE_ID 
```

### Field Mapping

```properties
#Example: Index_Fields=<IndexFieldIdFromIDM>:<type>
Index_Fields=delivery_note_id:STRING,delivery_date:STRING,CORRELATION_ID:STRING,ACCOUNTING_ENTITY:STRING,GROUP_ACCOUNTING_ENTITY:STRING,supplier_name:STRING,supplier_id:STRING,purchase_order:STRING
#Example: IF_<IndexFieldIdFromEphesoft> = <IDMAttributeId>
IF_delivery_note_id=Delivery_Note_Id
IF_delivery_date=Document_Date
IF_supplier_name=SupplierName
IF_supplier_id=Supplier_Id
IF_purchase_order=Purchase_Order
```

*   Start by listing all the index fields used, specifying the field ID and type.

    ```properties
    Index_Fields=delivery_note_id:STRING,delivery_date:STRING,CORRELATION_ID:STRING,ACCOUNTING_ENTITY:STRING,GROUP_ACCOUNTING_ENTITY:STRING,supplier_name:STRING,supplier_id:STRING,purchase_order:STRING
    ```
*   Each mapped field follows the format:

    ```properties
    IF_<DocBitsFieldID> = <IDMAttributeId>
    ```

    * Confirm that **IndexFieldFromDocBits = IDMAttributeID**, ensuring that the field mapping in DocBits aligns with the attributes in IDM (Document Type → Attributes).\
      A Guide on how to navigate in IDM can be found at Document Manager in IDM on this page.

<figure><img src="../../.gitbook/assets/image (428).png" alt=""><figcaption></figcaption></figure>

## XML and EDI  file export&#x20;

To export the original XML/EDI file along with the generated PDF, you need to modify the IDM Mapping file, in the export configuration. First, update the **Static\_Values** section by adding the file prefix and extension. After that, define the actual mapping to ensure the correct export configuration.

If an export for invoices to IDM is already set up, the generated PDF should already be included in the export. If you don’t need the XML file, you can skip the next part. However, if you do need the XML file, follow the steps below.

### Updating the Static Values:

Find the **Static\_Values** field and add the following:a

```properties
,EDI_FILE_PREFIX,XML_FILE_PREFIX,PDF_FILE_PREFIX,PDF_FILE_EXTENSION,EDI_FILE_EXTENSION,XML_FILE_EXTENSION
```

Then, add the following entries below **SV\_ACLString**:

```properties
SV_EDI_FILE_PREFIX=EDI_810_
SV_XML_FILE_PREFIX=XML_810_
SV_PDF_FILE_PREFIX=INV_EDI_
SV_PDF_FILE_EXTENSION=.pdf
SV_EDI_FILE_EXTENSION=.xml
SV_XML_FILE_EXTENSION=.xml
```

<figure><img src="../../.gitbook/assets/image (371).png" alt=""><figcaption></figcaption></figure>

### XML Mapping

Add the following mapping at the bottom of the file:

<pre class="language-properties"><code class="lang-properties"><strong>EMBEDDED_FILES_EXPORT = TRANSFORMED, XML
</strong>EFE_TRANSFORMED_SOURCE_NAME = Transformed.xml
EFE_TRANSFORMED_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_TRANSFORMED_EXPORT_FILENAME = SV_XML_FILE_PREFIX+IF_INVOICE_ID+SV_XML_FILE_EXTENSION

EFE_XML_SOURCE_NAME = XML_DOCUMENT.xml
EFE_XML_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_XML_EXPORT_FILENAME = SV_XML_FILE_PREFIX+IF_INVOICE_ID+SV_XML_FILE_EXTENSION
</code></pre>

Note: Ensure that **export\_doc\_type** is set to the IDM invoice type. In this example, it is set for **M3**.

<figure><img src="../../.gitbook/assets/image (373).png" alt=""><figcaption></figcaption></figure>

### EDI Mapping

Add the following mapping at the bottom of the file:

```properties
EMBEDDED_FILES_EXPORT = TRANSFORMED, EDI
EFE_TRANSFORMED_SOURCE_NAME = Transformed.xml
EFE_TRANSFORMED_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_TRANSFORMED_EXPORT_FILENAME = SV_XML_FILE_PREFIX+IF_INVOICE_NUMBER+SV_XML_FILE_EXTENSION

EFE_EDI_SOURCE_NAME = EDI.edi
EFE_EDI_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_EDI_EXPORT_FILENAME = SV_EDI_FILE_PREFIX+IF_INVOICE_NUMBER+SV_EDI_FILE_EXTENSION
```

Note: Ensure that **export\_doc\_type** is set to the IDM invoice type. In this example, it is set for **M3**.

<figure><img src="../../.gitbook/assets/image (374).png" alt=""><figcaption></figcaption></figure>

### Document Manager in Infor

Go to Document Manager and select the name of the current document type you are trying to export, for example, Supplier Invoice.

![](https://lh7-us.googleusercontent.com/EV3uw3R1L6_RRANB7FRLwtUFMbv_KGtL4x6kAk6lEYhwI90UeG2uWqFD2Azpxv-SRFl9zfvdratOZbXxp2D1-SryLo3Boj2x9Xc4PQXJ6vUhX5c9pvhv4XHuCk-qMK51DZ885vRUJ5dwES7k84uhoyk)

Click the above icon and then click Administration → Document Type and then find the document type you need in the list

![](https://lh7-us.googleusercontent.com/ldsuINS9SCUQm3E57s8j_95gzBGwHQFavcf6d3myg6tuVxRoQHtq8R-6we5OEJ63swDxwPc9w7hbySWqWdfaMsGdQpn99m6EchPY5f5DzXEj-8mjocwPNtdJVNP34CuPvw0JIImDgFX1Q05M8-ogZo8)

As shown below, you will then see the doc type name as it is in INFOR

![](https://lh7-us.googleusercontent.com/KSreWGS7TqdMP64BqtufM24xk0RDnNDHUZapnPsSuRj_umPJ3icll89KI2RYpbtet2F6ccL8QfYbl27-2j1nQPwQ0z-Nq873c4Tv72ee9AJhKMxynIUxmJKKsQQCupW_dpRfw_5BXm0WvAnw4HOALmw)

Make sure this is how the name is shown in the IDM Mapping File

## Upload File to DocBits

Once the file is prepared, upload it to your export configuration in DocBits. This is available at Settings → Export.

![](https://lh7-us.googleusercontent.com/rUHhvImiWamK6JxnWSPL4JEioAJq3AmvdsubJDo-DoDV9F_i5mZ42YDnjqZUYKYSJu1Cetc_4fLwlvvmoZXYIzmBf3hoyW6RjfP9HQ8FkNDhW1IbLHvNTCHWFRaeCECdZ97u79-Eu37TvzqnqGPEayM)
