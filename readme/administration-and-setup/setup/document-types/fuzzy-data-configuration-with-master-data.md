# Fuzzy Data Configuration with Master Data

### **Overview**

Each document type has its own default configurations and must be set up separately. While this example explains the setup for **Invoices**, the same process applies to all document types.

### To configure Fuzzy Data, navigate to:

Settings → Global Settings → Document Types → Invoice → Fields → Master Data Settings → Lookup Master Data

<div align="center"><figure><img src="../../../.gitbook/assets/fuzzy_data_config_1.png" alt="" width="454"><figcaption></figcaption></figure></div>

### **Default Lookups**

There are **four default lookup groups** for invoices:

1. **Company Data**
2. **Purchase Order Header**
3. **Supplier**
4. **Tax Code**

<figure><img src="../../../.gitbook/assets/fuzzy_data_config_2.png" alt="" width="563"><figcaption></figcaption></figure>

Each group contains specific fields. Click on a group to **expand** it and view the fields. Default lookup groups are labeled with a **"Default" tag**.

### **Lookup Configuration Status**

* **Active configurations** are marked with an **"Activated" tag**.
* **Deactivated configurations** are marked with a **"Deactivated" tag**.

### **Prerequisite: Importing Master Data**

For Fuzzy Data to function correctly, the relevant **master data** must be imported. Without this, the system has no reference data to use. Here is how to import master data:

{% content-ref url="../../../infor-integration-and-configuration/importing-customer-master-data/" %}
[importing-customer-master-data](../../../infor-integration-and-configuration/importing-customer-master-data/)
{% endcontent-ref %}

### **Managing Lookup Groups**

Each lookup group is **activated by default** but can be modified by clicking the three dots:

* **Deactivate** → Deactivates a group. _(Only available for activated groups)_
* **Activate** → Deactivates a group. _(Only available for deactivated groups)_
* **Duplicate** → Creates a copy that can be modified without affecting the original.
* **View** → Displays information such as the **document type** it belongs to and the **lookup table** it uses. _(Only available for default groups)_
* **Edit** → Available for **non-default** groups. Allows modifying group details.
* **Delete** → Removes the group entirely. _(Only for non-default groups)_

### **Creating a New Lookup Configuration**

There are **two ways** to create a lookup configuration:

1.  **Duplicate an existing lookup**



    <figure><img src="../../../.gitbook/assets/fuzzy_data_config_3.png" alt=""><figcaption></figcaption></figure>

    * This copies all information and fields from an existing group.
    * You only need to provide a **new name**.
2.  **Create a lookup from scratch**\


    <figure><img src="../../../.gitbook/assets/fuzzy_data_config_4.png" alt=""><figcaption></figcaption></figure>

    * Click **"Create Lookup Configuration"**.
    * Fill in the required details:
      * **Configuration Name**
      * **Lookup Table** (Master Data Table to be used)
      * **Conflict Handler** (Choose one: Best Score, Return None, Return First)
      * **Context Type** → Defines where the lookup is applied:
        * **Header** → Used for document-level fields such as Invoice Number, Date, etc.
        * **Line** → Used for line item fields within the invoice table. If **Line** is selected, the user must also specify **which invoice table** should be used.
      * **Match All** → When enabled, only results that match **all** filter conditions will be returned.

### **Managing Fields Within a Lookup Group**

Each group contains fields that can be **added, removed, edited, or viewed**, depending on whether they are default fields or custom fields.

#### **Default Fields**

*   Marked with a **"Default" tag**.\


    <div align="left"><figure><img src="../../../.gitbook/assets/fuzzy_data_config_5.png" alt="" width="251"><figcaption></figcaption></figure></div>
* **Can only be viewed**, not edited or deleted.

#### **Non-Default Fields**

* **Can be edited or deleted** by clicking the three dots and selecting **Edit** or **Remove**.

#### **Adding a New Field**

<mark style="color:red;">**Note:**</mark> You can create fields inside a default Lookup configurations.

To add a new field within a group:

1.  Click **"Create"** inside the relevant group.\


    <figure><img src="../../../.gitbook/assets/fuzzy_data_config_6.png" alt=""><figcaption></figcaption></figure>
2. Provide the following details:
   * **Lookup Field** → Column name from the master data lookup table.
   * **Validation Field** → Corresponding DocBits field.
   * **Parent Field** →&#x20;
   * **Search Operator** → Choose one:
     * Smart
     * Contains
     * Exact
     * Starts with
     * Ends with
   * **Checkboxes:**
     * **Auto Trigger** → When enabled, the field will automatically trigger the lookup process during extraction. That means as soon as the related DocBits field is populated, the system will  populate the remaining fields **automatically**.
     * **Searchable** → Enables the field as a **Fuzzy Data** field, allowing searches in the master data lookup (blue icon in validation screen).

### **Final Step: Adding Fields to the Layout**

After configuring Fuzzy Data fields, **make sure to add them to the layout using the Layout Builder**. If fields are not added to the layout, they will not be available for use.

{% content-ref url="../../settings/global-settings/document-types/layout-manager/" %}
[layout-manager](../../settings/global-settings/document-types/layout-manager/)
{% endcontent-ref %}

