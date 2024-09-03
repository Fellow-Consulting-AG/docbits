# Release

## Release Sunset 12th August 2024

### New Features:



## Duplicate Invoice handling

This feature allows users to identify if documents are duplicated across their system. This feature works by analyzing document fields that can be configured by the user. By selecting specific fields, users can customize the detection criteria to suit their needs, ensuring that only relevant duplicates are flagged. This helps to maintain data integrity and reduces the clutter of redundant documents, streamlining document management processes.

{% embed url="https://youtu.be/WW36TTIUCs4" %}

## Decision Tree

The decision tree is a tool used to automate decision-making in a workflow by mapping out choices and their outcomes. By integrating decision trees, you can ensure consistent decisions based on specific criteria, streamline processes, and reduce errors. This approach enhances efficiency by automating complex decision points within the workflow.

{% embed url="https://youtu.be/E7cx8BDGTI0" %}



## Choosing AI Models

DocBits now allows users to switch between different AI models to better suit their needs. You can choose the AI model that best fits your specific use case, whether it's for document analysis, data extraction, or text classification. This flexibility enables you to optimize performance and achieve more accurate results, tailoring the AI's capabilities to your organization's unique requirements.

{% embed url="https://youtu.be/YvgEVagPepY" %}

## Choosing OCR Version

DocBits now offers the ability to change the OCR (Optical Character Recognition) version used within the platform. Users can select different OCR versions based on their specific needs, ensuring better accuracy and compatibility with various document types. This feature allows for more precise text extraction from images and scanned documents, improving overall data quality and workflow efficiency.

{% embed url="https://youtu.be/zkW8zj0H5Ko" %}

## Rule Manager

[rule-manager](admin-section/settings/document-processing/rule-manager/ "mention") provides the flexibility to create and edit conflict resolution rules tialored for DocBits invoicing system. These rules are designed to automatically handle discrepancies between invoice details and purchase order (PO) data, ensuring accurate financial reconciliation. The system applies these rules to process invoice lines, charges, and taxes, and generates appropriate adjustments or notes when necessary.

<figure><img src=".gitbook/assets/RuleManager.png" alt=""><figcaption><p>Rule Manager</p></figcaption></figure>

### Syncing Data Using Stream

BOD syncing from Infor utilizes AWS Stream for real-time data processing, enhancing efficiency and significantly reducing data syncing time.

### XRechnung

DocBits now processes XRechnung (electronic invoices) seamlessly by first creating a user-friendly PDF, streamlining and simplifying the invoice processing workflow.

<figure><img src=".gitbook/assets/XRECHNUNG.png" alt=""><figcaption></figcaption></figure>

### Bug Fixes:

1. PO Match Button Visibility\
   Issue: PO Match button is available when there is no table or the table is deleted.\
   Status: On field validation, PO Match will be hidden if there is no table or the table is deleted
2. Table Drag & Drop Sorting\
   Issue: Table Drag & drop for sorting on all Lists/Dashboards\
   Resolution: User can now drag and drop to sort the table
3. Validation Screen Toolbar\
   Issue: Validation screen: toolbar right side not scrollable\
   Resolution: Fixed
4. Horizontal Scroll\
   Issue: Horizontal Scroll on Approval Screen\
   Resolution: Fixed
5. Approval Screen Decision Clearing\
   Issue: Ability to clear the approve/reject decision on approval screen\
   Resolution: Fixed
6. Task Display on Approval Screen\
   Issue: Task shown on the Approval Screen\
   Resolution: Toolbar is available which shows the tasks count of open/in progress
7. PO Match Table Size\
   Issue: PO Match table gets smaller after matching a line\
   Resolution: Fixed
8. Task Assignment based on Item Procurement Group\
   Issue: Translation for procurement group assignment\
   Resolution: Fixed
9. Supplier Name and Id in Task Creation\
   Issue: Adding Supplier Name and Id in Task creation\
   Resolution: Supplier Name and Id will be picked from the document
10. Document Subtype Copy\
    Issue: Click on Copy Document Subtype from sub document type setting was not working\
    Resolution: Fixed
11. New Label Field\
    Issue: New Label field in list of values to add label along with value and synonym\
    Resolution: Fixed
12. Country Origin Card in Workflow\
    Issue: New Card in workflow that checks country origin of a supplier and create a task or continue porcessing docuemtn accordingly\
    Resolution: Fixed
13. Dark Mode Fix on settings searchbar\
    Issue: This issue was previously identified\
    Resolution: Fixed
14. Extracted Table Column Visibility Indicator\
    Issue: Indicator if Columns are hidden in extracted table on Field validation\
    Resolution: Fixed
15. Dashboard Assignment for Admins\
    Issue: Make Assign to on the dashboard only for admins\
    Resolution: Fixed
16. Document Split Visibility\
    Issue: Show Document split only when more pages\
    Resolution: Fixed
17. Invoice Dashboard Columns\
    Issue: Additional columns on invoice dashboard\
    Resolution: Fixed
18. Field Validation Script Deactivation\
    Issue: Field Validation- Deactivate script was not working correctly\
    Resolution: Fixed
19. Approval Layout Button Customization\
    Issue: Cannot change the button type and style on approval layout builder\
    Resolution: Fixed
20. Data Sync Table\
    Issue: Data Sync Table in settings\
    Resolution: Fixed
21. Dashboard Analytics Total Display\
    Issue: Dashboard Analytics- display wrong total number\
    Resolution: Fixed

## Release Firework Juli 8th, 2024

### New Features

**Line Charges Export to M3**

• Export line charges to M3 with appropriate costing elements as per your business needs.

**PO & Invoice Discrepancy Handling**

• Smart handling of discrepancies in quantity, prices, charges, and tax.

### Key Bug Resolutions

#### 1. PO Search Functionality

• Issue: PO search was not working.&#x20;

• Status: This issue has been identified and will not be addressed in this release.

#### 2. PO Matching Connection

• Issue: PO matching connection was not removing as expected.

• Resolution: Fixed to ensure seamless PO matching operations.

#### 3. Exported Document Alerts

• Issue: Exported documents had alerts for costing elements even when the system was not set up for it.

• Resolution: Corrected to prevent unnecessary alerts, ensuring accurate document exports.

#### 4. Advance Shipment EDI View

• Issue: Advance shipment EDI view showed IDs in the title.

• Resolution: Titles now display correctly, improving data readability.

#### 5. Calculation Errors in Split by Total Issue

• Issue: Calculation errors occurred when lines were split further.

• Resolution: Fixed to ensure accurate calculations in all scenarios.

#### 6. PO Screen Table Display

• Issue: No table was showing on the PO screen.

• Resolution: Display issue resolved to ensure tables appear correctly.

#### 7. Auto Export on Order Confirmation

• Issue: Auto export was not working.

• Resolution: Functionality restored to ensure automatic exports operate smoothly.

#### 8. Mismatch Issue on PO

• Issue: Mismatch issue on PO showed despite everything being identical on the Delivery Note.

• Resolution: Resolved to ensure accurate mismatch detection.

#### 9. Report Download Issues

• Issue: Reports were not downloading.

• Resolution: Fixed to enable seamless report downloads.

#### 10. Incorrect Total and Net Amounts

• Issue: Total and Net amounts were showing incorrect values.

• Resolution: Values corrected to ensure financial accuracy.

#### 11. Invoice Date Format on Dashboard

• Issue: Invoice Date column had wrong format values.

• Resolution: Dates now display in the correct format, enhancing usability.

#### 12. Workflow Delays at “Ready for Validation”

• Issue: Workflow delays occurred at “Ready for Validation” until feedback from Doc2flow.

• Resolution: Workflow timing improved for faster validation processes.

## Next Release Firework Juli 8th, 2024

### Problem:

The existing system lacks automated rules for accurately matching and processing invoice charges against purchase orders (POs). This manual process can lead to discrepancies, as illustrated in the screenshots, where invoice charges and POs need reconciliation for correct invoicing.

<div>

<figure><img src=".gitbook/assets/Bildschirmfoto 2024-06-07 um 17.11.37.png" alt=""><figcaption></figcaption></figure>

 

<figure><img src=".gitbook/assets/Bildschirmfoto 2024-06-07 um 17.11.46.png" alt=""><figcaption><p>Rule Manager DocBits</p></figcaption></figure>

</div>

### Solution:

With the new Rule Manager in DocBits, launching in July, you can automate this process:

#### 1. Create Rules:

Define criteria (e.g., Quantity > PO Quantity) for invoice line items.

#### 2. Set Actions:

Map fields and actions to export data seamlessly to Infor.

#### 3. Test Rules:

Validate rules with sample data to ensure accuracy.

## Junebug Release Notes - June 10th, 2024

This update brings exciting new features and bug fixes to Junebug:

**New Features:**

* **Automated Charge Extraction:** Junebug now automatically extracts and maps charges within your Docbit documents. This eliminates manual data entry and streamlines your workflow.
* **Portal Export to Infor IDM:** The new Portal allows you to effortlessly export supplier documents directly to Infor IDM. This simplifies shipment processing and reduces manual intervention.
* **Origin Identification (AI):** Junebug introduces a powerful AI feature that automatically learns the origin of documents. This saves you time and effort in document classification.
*

    <div>

    <figure><img src=".gitbook/assets/POShipmentTable.png" alt=""><figcaption></figcaption></figure>

     

    <figure><img src=".gitbook/assets/ApprovalScreen2.png" alt=""><figcaption></figcaption></figure>

     

    <figure><img src=".gitbook/assets/ApprovalScreen1.png" alt=""><figcaption></figcaption></figure>

    </div>

**Bug Fixes:**

* **QR Code Fix:** An issue that previously caused problems with QR code processing has been resolved.
* **Non-EDI Document Handling:** Junebug now handles non-EDI documents more effectively.

<figure><img src=".gitbook/assets/EDI810-Invoice.png" alt=""><figcaption></figcaption></figure>

Hotfix - 5 Juni [**Priority System**](readme-1/our-document-priority-system.md)

## Next Release - Junebug Release 10th June 2024

Sandbox Freeze - 3th June 2024

<figure><img src=".gitbook/assets/Bildschirmfoto 2024-05-08 um 20.37.35.png" alt=""><figcaption></figcaption></figure>

In the upcoming release, a significant enhancement to the classification and extraction capabilities will be introduced, specifically aimed at table lines within documents. This new feature allows users to define whether a line in a table represents a charge. This functionality is particularly useful in detailed financial documents, such as invoices, where distinguishing between different types of transactions—such as charges, taxes, or fees—is crucial for accurate processing and record-keeping.

**Key Points for Release Notes:**

* **Enhanced Table Line Classification**: Users can now specify if a particular line in a document table is a charge, improving the accuracy and granularity of data extraction.

## Maypole Release 5.55.8.10 - ( 17th May )

### Release Notes - Web App

#### New Features:

▪ Workflow Card Translation: Enhancements in the workflow, including card translation for better localization support.

▪ Email Import Logging: Added detailed logging for email imports to enhance troubleshooting and monitoring.

▪ Broken Fuzzy Screen Fix: Resolved an issue with broken fuzzy screen display across various interfaces.

▪ Accounting Updates: Enhanced the accounting process by removing outdated accounting methods and integrating charges more efficiently.

#### Improvements:

▪ Ruiz Workflow Enhancements: Fixed bugs related to workflow navigation, particularly involving hidden steps.

▪ User Interface Adjustments: Improved user interface elements such as cash discount terms under payment terms for better clarity and user experience.

▪ Performance Enhancements: Various backend improvements to enhance system performance and stability.

#### Bug Fixes:

▪ Approval Stamp Issue: Fixed critical issues surrounding the approval stamp process to ensure compliance and correct functionality.

▪ Key Addition: Added necessary keys back to the system to ensure data integrity and system functionality.

▪ Master Data Field Adjustment: Addressed an issue in the master data field to align with user requirements.

#### Technical:

▪ Version Updates: Routine updates to various system components to align with current standards and technologies.

▪ Merge Activities: Numerous merges to integrate features, fixes, and enhancements from multiple development branches into the main branch.

### What's New - API

▪ Cache Management Enhancements: Updated the get\_receive\_delivery\_cache to improve performance and reliability.

▪ New Features for Sales Orders: Introduced a preview feature for sales orders, enhancing the visualization and management of order data.

▪ Document Handling Improvements: Added automated test jobs for demotesting and sandbox environments to ensure robustness.

▪ Enhanced Cache Functionality: Added field\_id to further enhance the caching mechanisms.

#### Fixes and Improvements

▪ Office Email Import Adjustments: Made necessary adjustments to the Office Email Import feature to enhance functionality.

▪ Development Enhancements: Multiple merges from dev to main branches ensuring synchronization and stability across environments.

#### Miscellaneous

▪ Configuration Updates: Various updates to the configuration files improving the system setup and parameters.

### Release Notes - Workflow

#### Enhancements:

▪ Implemented a new workflow test that can now be enabled during import, allowing for more flexible testing scenarios.

▪ Enhanced the logging functionality for action cards, making debugging and monitoring more efficient.

▪ Improved compatibility for field comparison cards with date and enum types, ensuring smoother comparisons and validations.

▪ Updated the tax card and modified the return processes for action cards to streamline operations.

#### Fixes:

▪ Addressed issues with the document status updates, ensuring they are accurately reflected in the system.

▪ Fixed the calculation for the comparison card involving unit price and quantity to correctly handle discrepancies.

▪ Resolved multiple minor bugs and made stability improvements.

#### Operational Changes:

▪ Merged multiple development stages into the sandbox and stage branches, reflecting a significant integration of new features and fixes.
