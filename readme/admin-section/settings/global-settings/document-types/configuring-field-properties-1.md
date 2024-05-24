# Configuring Field Properties

## Detailed instructions on setting properties such as Required, Read Only, Hidden, and OCR.

### Required:

<figure><img src="../../../../.gitbook/assets/image (111).png" alt=""><figcaption></figcaption></figure>

If a field is marked as Required, it means that this field must be filled in before the document can be saved or processed.&#x20;

**To set this property:**

* Navigate to the field's settings in your DocBits system.
* Enable the Required option for the relevant field.

**Impact:**

* This setting ensures that important information is captured and that no documents can be processed without the required data.



### Read Only:

<figure><img src="../../../../.gitbook/assets/image (112).png" alt=""><figcaption></figcaption></figure>

If a field is marked as Read Only, it means that users can view the contents of this field, but cannot make any changes to it.&#x20;

**To set this property:**

* Go to the Field Options. Enable the Read Only option for the desired field.

**Impact:**

* This setting can be useful to protect sensitive information or to ensure that important data is not accidentally changed.



### Hidden:

<figure><img src="../../../../.gitbook/assets/image (113).png" alt=""><figcaption></figcaption></figure>

If a field is marked as "Hidden", it means that the field will be hidden in the user interface and users will not be able to see or access it.&#x20;

**To set this property:**

* Go to the field options.
* Enable the "Hidden" option for the corresponding field.

**Impact:**

* This setting is often used to hide internal or technical fields that are irrelevant to the end user or are only needed for internal processing.



### OCR (Optical Character Recognition):

<figure><img src="../../../../.gitbook/assets/image (114).png" alt=""><figcaption></figcaption></figure>

If a field is configured for OCR, it means that the system will try to extract the text from the document and insert it into this field. This setting is usually used for fields that are intended to be auto-filled.&#x20;

**To set this up:**

* Enable the OCR option for the corresponding field.&#x20;
* If necessary, configure the OCR parameters such as language, font, etc.

**Impact:**

* Using OCR allows documents to be processed automatically by extracting information from texts and entering it into the appropriate fields, reducing manual effort and increasing efficiency.



### Forced validation:

<figure><img src="../../../../.gitbook/assets/image (115).png" alt=""><figcaption></figcaption></figure>

Configure the validation rules accordingly, such as numeric limits, regular expressions, or relationships with other fields.

**To set this up:**

* Save the changes.

**Impact:**&#x20;

* Forced validation checks the entered data against the specified criteria to ensure it is valid. This helps to detect errors early and improve data quality.



### Match Score:

<figure><img src="../../../../.gitbook/assets/image (116).png" alt=""><figcaption></figcaption></figure>

&#x20;By comparing input data with reference data, the Match Score can help confirm the accuracy and validity of the data. If the Match Score exceeds a certain threshold, the match is considered successful.

**To set this up:**

* Enable the Match Score option and set the desired threshold.
* Save the changes.

**Impact:**

* The Match Score is used to evaluate the accuracy of matches between input data and reference values. If the score obtained exceeds the set threshold, the match is considered successful. This is especially useful for fields that require data validation or data matching, such as fields with a name, email address, or e-mail address. B. when checking customer data.

<figure><img src="../../../../.gitbook/assets/image (117).png" alt="" width="258"><figcaption></figcaption></figure>

By carefully configuring these field properties, you can optimize document processing workflows and ensure that your data is correctly captured, protected, and processed efficiently.

