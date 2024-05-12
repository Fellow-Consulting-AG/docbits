# Document Types

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 08.44.19.png" alt=""><figcaption></figcaption></figure>

#### Overview

The Document Types section lists all document types recognized and processed by Docbits. Administrators can manage various aspects such as layout, field definitions, extraction rules, and more for each type of document. This customization is key to ensuring accurate data handling and compliance with organizational standards.

#### Key Features and Options

1. **Document Type List**:
   * Each row represents a document type such as Invoice, Credit Note, Delivery Note, etc.
   * Document types can be standard or custom, as indicated by labels like "Standard."
2. **Edit layout**: This option allows administrators to modify the document layout settings, which include defining how the document appears and where data fields are located.
3. **Document Sub Types**: If any document types have subcategories, this option lets admins configure settings specific to each subtype.
4. **Table columns**: Customize which data columns should appear when the document type is viewed in lists or reports.
5. **Fields**: Manage the data fields associated with the document type, including adding new fields or modifying existing ones.
6. **Model Training**: Configure and train the model used for recognizing and extracting data from the documents. This may involve setting parameters for machine learning models that improve over time with more data.
7. **Regex**: Set up regular expressions that are used to extract data from documents based on patterns. This is particularly useful for structured data extraction.
8. **Scripts**: Write or modify scripts that run custom processing rules or workflows for documents of this type.
9. **EDI (Electronic Data Interchange)**: Configure settings related to the exchange of documents in standardized electronic formats.

{% hint style="info" %}
See [Setup Document Type ](../../../setup/document-types/)
{% endhint %}

{% @jira/embed url="https://fellowpro.atlassian.net/browse/DOCB-2489" %}

