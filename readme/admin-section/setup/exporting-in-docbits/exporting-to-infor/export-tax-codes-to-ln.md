# Export Tax Codes to LN

## **Overview:**

\
This guide will walk you through the setup process to ensure tax codes are correctly exported from DocBits to LN.



### **Step 1: Set Up List of Values**

1.  Go to **Settings** -> **Document Processing** -> **List of Values**.

    <figure><img src="../../../../.gitbook/assets/TaxCodes_1.png" alt=""><figcaption></figcaption></figure>
2.  Click **New**.



    <figure><img src="../../../../.gitbook/assets/TaxCodes_2.png" alt=""><figcaption></figcaption></figure>
3.  Create a list with the name `Tax_Country` and click **Save**.



    <figure><img src="../../../../.gitbook/assets/TaxCodes_3.png" alt="" width="375"><figcaption></figcaption></figure>
4.  Create the following three additional lists:

    * `Tax_Code_Full`
    * `Tax_Code_Reduced`
    * `Tax_Code_Free`

    <div align="left"><figure><img src="../../../../.gitbook/assets/TaxCodes_28.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../../../.gitbook/assets/TaxCodes_29.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../../../.gitbook/assets/TaxCodes_30.png" alt=""><figcaption></figcaption></figure></div>
5.  Click on one of the newly created lists to open it. Then, press the **Add Row** button to add a new row.



    <figure><img src="../../../../.gitbook/assets/TaxCode_4.png" alt=""><figcaption></figcaption></figure>
6.  Enter the desired respective values from **LN** and press **Save** to save the changes.

    * If you have multiple values, you can click **Add More Values** to add them.

    <div align="left"><figure><img src="../../../../.gitbook/assets/TaxCodes_5.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../../../.gitbook/assets/TaxCodes_27.png" alt=""><figcaption></figcaption></figure></div>

    * **NOTE:** You can find the Tax Codes in LN under: **Common** → **Taxation** → **Master Data** → **Tax Codes** → **Tax Codes by Country**

    <figure><img src="../../../../.gitbook/assets/TaxCodes_LN.png" alt=""><figcaption></figcaption></figure>

### **Step 2: Add Fields in DocBits**

1.  Navigate to **Settings** -> **Global Settings** -> **Document Types**.

    <figure><img src="../../../../.gitbook/assets/TaxCodes_6.png" alt=""><figcaption></figcaption></figure>
2.  Choose the Fields menu corresponding to the Document Type where you wish to add the fields.

    <figure><img src="../../../../.gitbook/assets/TaxCodes_7.png" alt=""><figcaption></figcaption></figure>
3.  Under **VAT & Amounts**, create six new fields as follows:

    <figure><img src="../../../../.gitbook/assets/TaxCodes_8.png" alt=""><figcaption></figcaption></figure>

| **Name**              | **Title**           | **Field Type** | **Value**          |
| --------------------- | ------------------- | -------------- | ------------------ |
| `tax_country`         | Tax Country         | Dropdown       | Tax\_Country       |
| `tax_country`         | Tax Country Reduced | Dropdown       | Tax\_Country       |
| `tax_country`         | Tax Country Free    | Dropdown       | Tax\_Country       |
| `tax_code_1_dropdown` | Tax Code            | Dropdown       | Tax\_Code\_Full    |
| `tax_code_2_dropdown` | Tax Code Reduced    | Dropdown       | Tax\_Code\_Reduced |
| `tax_code_3_dropdown` | Tax Code Free       | Dropdown       | Tax\_Code\_Free    |

<div align="left"><figure><img src="../../../../.gitbook/assets/TaxCodes_10.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../../../.gitbook/assets/TaxCodes_11.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../../../.gitbook/assets/TaxCodes_12.png" alt=""><figcaption></figcaption></figure></div>

<div align="left"><figure><img src="../../../../.gitbook/assets/TaxCodes_13.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../../../.gitbook/assets/TaxCodes_14.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../../../.gitbook/assets/TaxCodes_15.png" alt=""><figcaption></figcaption></figure></div>

4. After saving each field, click on **Save Settings** to apply the changes.

<figure><img src="../../../../.gitbook/assets/TaxCodes_20 (1).png" alt=""><figcaption></figcaption></figure>

### Step 3: Add a Script

To ensure the values are formatted correctly for processing by LN, you need to create a script.

1. Navigate to **Settings** → **Global Settings** → **Document Types**.
2. Select the Document Type where you want to add the script.
3. Open the **Scripts** menu for the selected Document Type.
4. Create a new script and follow these steps:
   * Provide a name for your script.
   * In the **Trigger On** dropdown menu, select **AFTER\_FORMATTING**.
   *   Paste the working script (example below) into the script editor:

       ```
       tax_code_1_dropdown = get_field_value(document_data, 'tax_code_1_dropdown', None)
       tax_code_2_dropdown = get_field_value(document_data, 'tax_code_2_dropdown', None)
       tax_code_3_dropdown = get_field_value(document_data, 'tax_code_3_dropdown', None)

       tax_country_1 = get_field_value(document_data, 'tax_country', None)
       tax_country_2 = get_field_value(document_data, 'tax_country', None)
       tax_country_3 = get_field_value(document_data, 'tax_country', None)

       if tax_code_1_dropdown and tax_country_1:
           set_field_value(document_data, "tax_code", tax_country_1 + "_" + tax_code_1_dropdown)
       if tax_code_2_dropdown and tax_country_2:
           set_field_value(document_data, "tax_code_2", tax_country_2 + "_" + tax_code_2_dropdown)
       if tax_code_3_dropdown and tax_country_3:
           set_field_value(document_data, "tax_code_3", tax_country_3 + "_" + tax_code_3_dropdown)
       ```
   * Click **Save** to finalize the script.

### **Step 4: Edit Layout**

1.  Go to **Settings** -> **Global Settings** -> **Document Types**.

    <figure><img src="../../../../.gitbook/assets/TaxCodes_6.png" alt=""><figcaption></figcaption></figure>
2.  Open the **Layout** menu for the Document Type you want to edit.

    <figure><img src="../../../../.gitbook/assets/TaxCodes_19.png" alt=""><figcaption></figcaption></figure>
3.  Select the appropriate **Document Origin** for which you want to apply the Tax Codes

    <figure><img src="../../../../.gitbook/assets/TaxCodes_26.png" alt=""><figcaption></figcaption></figure>
4.  Scroll down to the **Tax Details** section.

    <figure><img src="../../../../.gitbook/assets/TaxCodes_21.png" alt=""><figcaption></figcaption></figure>
5. Expand the **Form Elements** dropdown menu.
6.  In the **Tax Types** section, use the **Horizontal Separator Tool**. Drag and drop it between the sub-sections within the tax section to clearly separate them and reduce confusion.

    <figure><img src="../../../../.gitbook/assets/TaxCodes_22.png" alt=""><figcaption></figcaption></figure>
7. Expand the **Form** dropdown menu.
8.  Search for **Tax Country** and drag and drop the field into its respective area.

    <figure><img src="../../../../.gitbook/assets/TaxCodes_23.png" alt=""><figcaption></figcaption></figure>
9.  Search for **Tax Code** and drag and drop the field into its corresponding area.

    <figure><img src="../../../../.gitbook/assets/TaxCodes_24.png" alt=""><figcaption></figcaption></figure>
10. Save the template.

    <figure><img src="../../../../.gitbook/assets/TaxCodes_25.png" alt=""><figcaption></figcaption></figure>

### Step 5: Verify that Everything Worked

After uploading a new document into DocBits with the correct document settings selected, you should now be able to select the tax codes you added to the lists in Step 1.

<figure><img src="../../../../.gitbook/assets/TaxCodes_31.png" alt=""><figcaption></figcaption></figure>
