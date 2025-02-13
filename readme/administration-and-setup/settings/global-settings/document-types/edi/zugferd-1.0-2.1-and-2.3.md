# ZUGFeRD 1.0, 2.1 and 2.3

## **Supported Versions of ZUGFeRD**

Currently supported versions of ZUGFeRD are:

* **1.0**
* **2.1** (compliant with FACTUR-X 1.0.05)
* **2.3** (compliant with FACTUR-X 1.07.2)

#### Standard Activation and Modification

The ZUGFeRD standard is always active by default, but you can make modifications to it if needed.

### **Steps to Modify ZUGFeRD Settings:**

1. Navigate to **Settings → Global Settings → Document Types → Invoice**.
2.  Click on **E-Doc**.\


    <figure><img src="../../../../../.gitbook/assets/image (375).png" alt=""><figcaption></figcaption></figure>
3. A list of all available e-docs will appear.
4.  Locate the **ZUGFeRD** version you want to modify.\


    <figure><img src="../../../../../.gitbook/assets/image (376).png" alt=""><figcaption></figcaption></figure>

## **Transformation and XML Path Configuration:**

In the **transformation settings**, you can define the path to locate specific information within the XML file and save it in a new structure, making it easier to access the data.\
**Note:** If you use this functionality, you must use the newly created XML paths, not the original XML paths, in the **Preview** and **Extraction Path**.

### **Steps to Modify Transformation File:**

1. Open the **Transformation**.
2. Create a new draft by clicking the **pencil icon**.
3. Select the newly created draft.
4. Either create a new field or modify an existing one.
5. Set the desired path for data extraction.
6. Click **Save**.

### Important Notes:

* The **preview file** is used only for **FACTUR-X** and not for **ZUGFeRD**. ZUGFeRD will use the original **PDF**.

## Preview PDF Configuration

The **Preview PDF Configuration** is used to generate a user-readable version of the document. You can customize it with HTML to match your needs.

### **Steps to Modify Preview File:**

1. Open the **Preview**.
2. Create a new draft by clicking the **pencil icon**.
3. Select the newly created draft.
4. Either create a new field or modify an existing one.
5. Set the desired path for data extraction.
6. Click **Save**.

## Extraction Paths Configuration

The **Extraction Paths Configuration** is used to extract data and populate fields in the **validation screen**, such as the invoice table or fields configured in the invoice layout.

### **Steps to Modify** **Extraction Paths**:

1. Open the **Extraction Paths**.
2. Create a new draft by clicking the **pencil icon**.
3. Select the newly created draft.
4. Create a new field or modify an existing one.
5.  The left side represents the **DocBits field ID**, which can be found in the  **Settings → Global Settings → Document Types → Invoice → Fields**.\


    <figure><img src="../../../../../.gitbook/assets/image (379).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/image (378).png" alt=""><figcaption></figcaption></figure>
6. The right side represents the **path to the field** created in the Transformation.
7. Click **Save**.

By following these steps, you can ensure accurate data extraction and validation for ZUGFeRD invoices.
