# Users

### Users <a href="#id-5gcuy8m95274" id="id-5gcuy8m95274"></a>

Managing users in DocBits is easy with our simple step-by-step guide.

**Adding a User**

To add a new user to your DocBits account, follow these steps:

* Log in to your DocBits account and navigate to the Settings page.
* Click on Users to access the user management page.
* Click on Add User to create a new user.
* Enter the user’s information, including their name, email address, and password.
* If the user is an administrator, check the “Admin” box.
* Click Save to create the new user.

**Resetting a Password**

If a user forgets their password, you can easily reset it by following these steps:

1. Go to the DocBits login page and click on Forgot Password.
2. Enter the user’s email address and click Submit.
3. The user will receive an email with a link to reset their password.
4. Click on the link in the email and follow the instructions to reset the password.

#### **Sub-Organizations** <a href="#sakodwze3dnx" id="sakodwze3dnx"></a>

In Settings, Global Settings → Groups, Users and Permissions → Sub-Organizations as shown below.

You will then be taken to a page that looks similar to this

This is where you will find your previously created sub-organizations, as well as where you can create new sub-organizations.

**How to create a Sub-Organization**

Click on the +NEW button

The following menu will be displayed

Enter the details of the sub-organization you want to create, the name and description, then click on the SAVE button. You should then find your newly created sub-organization at the bottom of the list of existing sub-organizations.



#### **Groups and Permissions** <a href="#xxqn3ye8t1q6" id="xxqn3ye8t1q6"></a>

**What is a group?**

A group is a set of users that can be granted specific permissions for one or multiple document types. The groups can be created, changed and deleted by the organization admins. Every organization admin has the rights to do this.

If no group is configured all privileges are granted to the users within the organization.

**Groups and privileges management**

Groups are managed in DocBits under Settings > Global Settings > Groups, Users and Permissions > Groups and Permissions

**DocBits Group User Management**

The organization admin can add users to the groups by pressing the “Manage Users” button.

**DocBits Group Permission Management**

The organization admin can set the group permissions by pressing the “View Permissions” button.

**Group permissions**

When creating a group, you can specify what privileges the users have for each document type.

The different types of Privileges are:

* View
* Update
* Delete
* First Approval
* Second Approval



**View**

If a user doesn’t have the view permission, the document type will not be shown to him on the dashboard.

**Update**

Exporting documents is only possible if the user has the update permission.

**Delete**

Permission to delete documents.

**First Approval**

Permission to grant the first approval, if configured. For more information, read the section on approval.

**Second Approval**

Permission to grant the second approval, if configured. For more information, read the section on approval.



#### **Custom Filters** <a href="#mq8il8gj6sxp" id="mq8il8gj6sxp"></a>

Navigate to SETTINGS → Dashboard

**Customize your filter**

Navigate to the Filters section

To create a Custom Filter, select CUSTOM in the “Status filter style”

Underneath that, you can select the various statuses a document can be in to create your custom filter. Once you press APPLY, this custom filter will be active on the Dashboard.

**Dashboard**

Select ADVANCED SETTINGS

Custom Filters can then be accessed by selecting the MORE SETTINGS option.



#### **Integration** <a href="#fnoow05jm6jg" id="fnoow05jm6jg"></a>

**What is API Integration?**

API Integration is the process of connecting two or more applications via APIs to enable them to communicate with each other. This allows the applications to perform a common function or exchange information, ensuring data integrity.

**How to Get Your API Key**

To get started with API Integration in DocBits, you will need your API Key. You can find your API Key in the Integration menu item in the settings. Simply copy and paste your API Key into your application to start integrating with DocBits.

**API Calls and Examples**

**API Calls for Document Upload and Status Check**

API integration provides functions and services that connect applications and processes. In this guide, we will show you how to make API calls through api.polydocs.io for document upload and status check.

**Authentication**

To make API calls, authentication is the first step. Follow the steps below to authenticate:

1. Open [api.docbits.com](https://api.docbits.com/).
2. Click on Authorize in the upper right corner.
3. Enter your [API Key](https://docs.fellowpro.com/docbits/settings/integration/api-integration/) and confirm by clicking Authorize.



**Upload Document**

To upload a document, follow the steps below:

* After authentication, scroll down to the POST /document/process endpoint.
* Open the tab and click on Try it out in the upper right corner.
* Enter the following value in the source field: email:{Pattern name}.
* Select the file you want to upload and click Execute.

Your document will be uploaded to your dashboard with the rules you set in DocBits.



Document Status Check

To check the status of a document, follow the steps below:

* After authentication, scroll down to the GET /document/status endpoint.
* Open the tab and click on Try it out in the upper right corner.
* Enter the document ID in the doc-id field. You can find the document ID when you open the document on the dashboard. This is the last part of the URL when the document is open.

You will receive the following response

If the status is “Ready For Validation,” it means that the user can check the document.

**Uploading a Document with Metadata**

To upload a document with metadata, follow the steps below:

* After authentication, scroll down to one of these endpoints: /document/process\_documents, /document/process, or /document/process\_base64.
* Open the tab and click on Try it out in the upper right corner.
* Enter the metadata in the metadata field. The metadata needs to be in a valid JSON format. An example of a metadata entry would be: {"custom-key": "the custom value", "custom\_doc\_id": "8a5cf33b-c923-4879-96ca-94d69965d508"}.
* Select a file to upload.
* Click Execute.
* Wait for the response. If the metadata field is not a valid JSON, an error message will appear. If “success”: true, then your document will be uploaded to your dashboard with the rules you set in DocBits.



#### **Document Expiry** <a href="#id-33bxgoqd3vgw" id="id-33bxgoqd3vgw"></a>

If you would like to keep your DocBits Dashboard tidy and up to date, consider the document expiry function.

This feature is located in Settings, under Document Processing.

**Delete Document After**

We supply you with a dropdown list of various time frames. Once a document has been in DocBits for the time frame you chose, the document will be removed.

**Delete Finished Document After**

Deletes any finished (exported) document once the time frame you selected has been reached.

#### **Email Notification** <a href="#id-9pjijybxiq7g" id="id-9pjijybxiq7g"></a>

In this section you can configure all types of email notifications for your document types. Easily set employees to be notified when a document has a certain status.

Go to Settings and open the Email notification menu.

**Configure New Email Notification**

To add a new notification, click + NEW in the top right corner and the following window will open.

In this you can define a custom name for the notification, select the document type and status as well as the time unit and enter the email address of the person who should receive the corresponding notification.

**The following statuses can be selected**

* Ready For Validation
* Pending Approval
* Pending Second Approval

**Time Units**

* Minutes
* Hours
* Days

The Delay has to be set to a minimum of 5 minutes as the email server will need that time to respond. The email will be sent after selected time duration, if document status remains unchanged.

#### **Document Types** <a href="#tdzc3anuw8h9" id="tdzc3anuw8h9"></a>

In DocBits you will find the SETTINGS menu in the upper bar on the DASHBOARD.

If you are logged in to DocBits as an admin, you will find all fields of a document that can be extracted under the respective document type.

Open the menu for Document Types.

In the following overview you will find all standard document types available for you

**Activate/Extraction Type**

To the right of each document type, you will see Activate and Extraction Type sliders.

Activate: This document type is active in your DocBits environment.

Extraction Type: This slider allows you to enable or disable a set of predefined rules for the document type when it is processed by DocBits. By selecting the gear icon to the right of the slider, the following menu will appear.

To see which fields can be extracted, for example from an invoice, click on FIELDS for this document type.



**Field Settings**

Here you will find all the fields that can be extracted

You can also CREATE FIELDS like freight, postage or any field with an amount you want to extract from your invoices.

For each field you can check the boxes if they are:

* **REQUIRED**: Here you can define if the field must contain a value to continue.
* **READ ONLY**: Here you can define if a field can only be displayed but not edited.
* **HIDDEN**: Here you can define whether a field should be hidden or displayed in the extraction view.
* **FORCE VALIDATION**: Here you can define whether a field must always be validated manually, even if it has been read 100% by DocBits.
* **OCR** and **MATCH SCORE**: Setting as described below, per field.
* **FORMULA**: Creation of a formula per field.

If all settings are made and should be saved, please confirm this with the SAVE SETTINGS button at the bottom of the page, otherwise the settings will not be applied.

**Recognition Settings**



**OCR**

Here you can set the sensitivity of the OCR (Optical Character Recognition) function for all fields at once. This value determines the sensitivity with which a field is marked in red if it could not be extracted with 100% certainty (OCR related!).

**Match Score**

Here you can set the sensitivity of the MATCH SCORE function for all fields at once. This value determines when a field is marked in red if DocBits has not extracted the field with 100% probability. In this case the field needs to be validated manually.

The button RESTORE DEFAULTS will set back both values to “50”.

**Profile**

Here you can define the profile that shall be used. Either Default or ZUGFeRD.\
In profile ZUGFeRD there are predefined fields that are mandatory for this type of invoice.\
If you do not explicitly use ZUGFeRD, please select “Default”.



