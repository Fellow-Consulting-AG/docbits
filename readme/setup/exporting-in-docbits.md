# Exporting in DocBits

**Exporting in DocBits**

4.1 **Export Module**

The export module is located, on the Dashboard, under Settings → Document Processing → Export.

![Ein Bild, das Screenshot, Text, Zahl, Software enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/0 (6).png>)

![Ein Bild, das Text, Software, Zahl, Screenshot enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/1 (6).png>)

**New Export**

To add a new export configuration, select “+ New”

![Ein Bild, das Screenshot, Text, Software enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/2 (6).png>)

Select the method you would like to use for your export configuration.

![Ein Bild, das Text, Screenshot enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/3 (6).png>)

Once you have selected the method you would like to use, you will need to upload the various information and files required for that method of exporting.

**Activate/Deactivate**

Once you have one or many export configurations in your DocBits, you have the option to activate or deactivate configurations depending on your needs.

The configuration below is activated, indicated by the green dot to the left of the configuration name.

![](<../../.gitbook/assets/4 (6).png>)

To deactivate the export configuration, select the options button to the right of the configuration as shown below.

![](<../../.gitbook/assets/5 (6).png>)

You are given three options

* Deactivate: The export configuration will no longer be functional (indicated by a red dot next to the configuration name).
* Edit: Make changes to the details of the configuration.
* Delete: Delete the configuration.

4.2 **Exporting to INFOR**

![Ein Bild, das Reihe, Diagramm, Screenshot, weiß enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/6 (6).png>)

4.2.1 **Creating an ION API Endpoint**

**Infor Configuration**

Once at the home screen, click on the burger menu and select ION API

![Ein Bild, das Text, Screenshot, Schrift, Logo enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/7 (6).png>)

After opening ION API, click on Available APIs in the left menu

![](<../../.gitbook/assets/8 (6).png>)

Click on “+ADD” block

![Ein Bild, das Screenshot, Software, Multimedia-Software, Computersymbol enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/9 (6).png>)

Then “+ Create New”

![Ein Bild, das Screenshot, Text, Software, Webseite enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/10 (6).png>)

The information you insert should look like this

![Ein Bild, das Text, Schrift, Zahl, Diagramm enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/11 (5).png>)

FYI: The description has multiple environments as this will be used for multiple environments and the icon and its color always remain the same.

Next, select the + at the bottom of the screen

![Ein Bild, das Screenshot, Text, Reihe, Schrift enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/12 (5).png>)

This Target Endpoint URL can be found at doc2api.cloudintegration.eu

![Ein Bild, das Text, Schrift, Screenshot, Reihe enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/13 (5).png>)

The information underneath this field should look as follows.

![Ein Bild, das Text, Screenshot, Schrift, Zahl enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/14 (5).png>)

Once you have filled in this information, to the right of these fields there is a “Target Endpoint Security” field with a drop down. Select API Key from this drop down.

![](<../../.gitbook/assets/15 (5).png>)

A table will then appear underneath this drop down, fill in the following information. The key value is specific to the customer and environment, it can be found within DocBits.

From the Dashboard → Settings → Integration → API Key

![](<../../.gitbook/assets/16 (5).png>)

![](<../../.gitbook/assets/17 (4).png>)

Copy and paste this into the Key Value field in InforOS

![](<../../.gitbook/assets/18 (4).png>)

Once this is complete, press the following icon to save the configuration

![Ein Bild, das Text, Schrift, Screenshot, Logo enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/19 (3).png>)

You are not yet completely done with the configuration.

Go back into the API you just configured and enter the details like below

![Ein Bild, das Screenshot, Software, Multimedia-Software enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/20 (3).png>)

Go to the Documentation tab at the bottom and click on the +

Enter the following details:

* Name = DocBits-”environment”
* Type = Swagger
* URL = go to doc2api.cloudintegration.eu, once on this page, open the following link

Copy the URL and use it for the URL field in InforOS

Save it once you have entered the information for all the fields. There should be a loading icon for a while but the end result should look like this

The same process would be used to create the endpoints for other environments.

**FYI**: If in the future you are struggling to find these endpoints, in ION API go to API Metadata and click on this icon to refresh the API metadata.

**DocBits Export Settings**

From the DocBits Dashboard of the required customer, go to Settings → Export, to add a new document type for export, do as follows:

* Click on the “+ New” button
* Select “Infor IDM + ION BOD”

4.2.2 **Creating an ION API file**

**Obtaining existing/Creating new ION API File**

This is created in INFOR ION API → Authorized Apps and an app like below should be shown

If not, then you need to create a new Authorized App. This can be done clicking the plus sign

Once you have entered the Name (DocBits\_\*Environment\*) and Type (case specific) of the new Authorized App, you will be taken to a page where the Client ID and Secret have been generated automatically.

The information you fill in should be similar to what is shown above, it is important to enable the “Issue Refresh Tokens” slider at the bottom of the page.

Click “Download Credentials” to download the ION Mapping File.

**Uploading the file to DocBits**

Once you have downloaded the ION API file from Infor, you can upload it by going to Settings → Document Processing → Export like below

4.2.3 **How to Create a BOD Mapping File**

Download a BOD Mapping File and open it in your applicable file editor of choice to edit it. For this walkthrough, VSCode is used.

**Editing Mapping File**

Change the company to the correct one (SFV\_AccountingEntityID) and edit location ID if needed.

Check the document code by going to the field settings of the document type you are trying to export (found in URL of field settings of document type in DocBits like below

Lastly, edit the SFV\_LogicalID which can be found in INFOR ION DESK → Connect → Connection points and select the DocBits\_Export or similar connection point and within that page you will find the Logical ID you need.

**Create Logical ID (Connection Point)**

If this Connection Point does not yet exist, you need to create one.

First, go to ION Desk → Connect → Connection Points and click on the “+ Add” button”

Then select the “IMS via API Gateway” option

You will be taken to the above screen where you must now fill in the necessary information, the name should be something like “DocBits\_export” or similar.

For “ION API Client ID” you enter the same Client ID you obtained earlier for the ION Mapping File.

Then select the Document tab of the Connection Point creation menu and add the following documents by pressing the “+” sign, this will only become useful later.

Once you save this Connection Point you will obtain the Logical ID as shown below

Then insert this Logical ID into the appropriate section of the BOD Mapping File and save the file.

**Upload File to DocBits**

Drag and drop the file into your export configuration in DocBits. This is available at Settings → Export.

4.2.4 **How to create an IDM Mapping file**

Once obtained, open the file in your applicable file editor of choice. For this walkthrough, VSCode will be used.

**Edit Mapping File**

Check the document type code is as it is in DocBits (like with the BOD Mapping File it should match the name of the doc type in the URL of the field settings) and also check the name of the document type as it should be in Document Manager (IDM) in Infor.

**FYI**: It states that the name of the document type in IDM is M3\_SupplierInvoice, this is due to this being an example from an M3 instance. This can change depending on if you use LN or M3, as well as your specific IDM configuration.

Check the company ID, and check Entity ID (SF\_MDS\_EntityType) this value should be the same as it was in the BOD Mapping File.

Ensure the IndexFieldFromDocBits=IDMAttributeID (check if DocBits on the left in the field settings matches IDM on the right in Document Type → Attributes).

**Document Manager in Infor**

Go to Document Manager and select the name of the current document type you are trying to export, for example, Supplier Invoice.

Click the above icon and then click Administration → Document Type and then find the document type you need in the list

As shown below, you will then see the doc type name as it is in INFOR

Make sure this is how the name is shown in the IDM Mapping File

**Upload File to DocBits**

Once the file is prepared, upload it to your export configuration in DocBits. This is available at Settings → Export.
