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

### Transformation and XML Path Configuration

In the transformation settings, you can define the path where specific information is located within the XML file.

### **Steps to Modify Transformation Paths:**

1. Create a new draft by clicking the **pencil icon**.
2. Select the newly created draft.
3. Either create a new field or modify an existing one.
4. Set the desired path for the data extraction.
5. Click **Save**.

### **Steps to Configure Extraction Path:**

1. Create a new draft by clicking the **pencil icon**.
2. Select the new draft.
3. Create a new field or edit an existing one.
4.  The left side represents the **DocBits field ID**, which can be found in the  **Settings → Global Settings → Document Types → Invoice → Fields**.\


    <figure><img src="../../../../../.gitbook/assets/image (379).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/image (378).png" alt=""><figcaption></figcaption></figure>
5. The right side represents the **path to the field** created in the Transformation.
6. Click **Save**.

### Important Notes:

* The **preview file** is used only for **FACTUR-X** and not for **ZUGFeRD**. ZUGFeRD will use the **PDF**.
* The **extraction path file** is utilized to display extracted data in the **validation screen** (e.g., invoice date).

By following these steps, you can ensure accurate data extraction and validation for ZUGFeRD invoices.
