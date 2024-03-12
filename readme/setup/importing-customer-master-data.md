# Importing Customer Master Data

## LN

### Supplier Master Data and Purchase Order

#### Connection Point

You will need to create the DocBits API connection point in order to create the data flow later.

First, in InforOS, navigate to ION Desk → Connect → Connection Points

![](<../../.gitbook/assets/0 (2).png>)

Once here, you will need to create a new connection point.

![Ein Bild, das Text, Screenshot, Software, Multimedia-Software enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/1 (2).png>)

**Select API**

Give the connection point a name and description that describes its nature and its environment. Under the Connection tab, import the service account you created for the environment you are working with.

![Ein Bild, das Text, Screenshot enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/2 (2).png>)

Next, switch to the Documents tab. You will need to add the following BODs to the connection point.

![Ein Bild, das Text, Reihe, Quittung, Screenshot enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/3 (2).png>)

* Ack-SupplierInvoice

This BOD is used to signal on DocBits that an error has occurred within Infor. The configuration for these two BODs should look similar to the following (API Call Name changing for each)

![Ein Bild, das Text, Screenshot enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/4 (2).png>)

* Sync.PurchaseOrder

The configuration for this BOD should look similar to the following

![Ein Bild, das Text, Schrift, Zahl, Screenshot enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/5 (2).png>)

* Sync.ReceiveDelivery

The configuration for this BOD should look similar to the following

![Ein Bild, das Text, Screenshot enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/6 (2).png>)

Once these BODs are configured, you can save the connection point by pressing the icon located right to the back button.

**Data Flow**

The data flow will look similar to the following

![Ein Bild, das Text, Diagramm, Screenshot, Plan enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/7 (2).png>)

(The reason for multiple DocBits APIs is due to each connection representing a different environment meaning, depending on the amount of environments you have, your data flow could differ slightly)

For the purpose of this explanation we will use the example of having four separate environments.

**LN**

The start of the data flow consists of your LN application

**DocBits API**

Here you will add an application and select the DocBits API(s) you created earlier

**Files**

The configuration should look as follows

![Ein Bild, das Diagramm, Reihe, Screenshot, Text enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/8 (2).png>)

**LN BOD Triggering**

**Once all the above is completed**, you will need to navigate to Infor LN and trigger the BODs in order for the various master data you need for Suppliers and Purchase Orders to arrive in DocBits.

![Ein Bild, das Screenshot enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/9 (2).png>)

**PurchaseOrder**

From the above menu, in the left menu tab, select Common → BOD-Messaging → Publish BODs → Publish Order Management Transactional Data

Select the PurchaseOrder tab and check the box.

![](<../../.gitbook/assets/10 (2).png>)

**Suppliers**

From the LN homepage, in the left menu tab, navigate to Common → BOD-Messaging → Publish BODs → Publish Logistics Master Data

Select the PartyMaster tab and check the Supplier → Buy-from or SupplierPartyMaster box.

![](<../../.gitbook/assets/11 (2).png>)

**BOD Triggering**

Once all the correct BODs have been checked for publication, select the Options tab.

The following options should be selected.

![](<../../.gitbook/assets/12 (2).png>)

Once this is complete, press the PROCESS button and the BODs will be triggered. A message will appear on screen to notify you that the BODs have been triggered.

![Ein Bild, das Screenshot, Text, Software enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/13 (2).png>)

If done successfully, the Supplier and Purchase Order tables should now be available under Settings → Master Data Lookup.

2.1.2 **Auto Accounting**

**Prerequisites**

* Functioning LN to DocBits dataflow
* Correctly configured DocBits environment

**Infor Configuration**

**ION Desk**

In Infor, open the ION Desk application. In the left tab, go to Connect → Connection Points

![Ein Bild, das Text, Screenshot, Schrift enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/14 (2).png>)

This is where you will create the two connection points needed to import your data from LN that is required for Auto Accounting.

Click on “+ADD” to create a new connection point, select the API option like below

![Ein Bild, das Text, Screenshot, Zahl, Software enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/15 (2).png>)

You will need to configure two separate API connection points, namely:

* ChartOfAccounts
* FinalFlexDimensions

**ChartOfAccounts**

The connection tab for your ChartOfAccounts connection point should look similar to what is illustrated below. Give the connection point an appropriate name and description, as well as import the Service Account you created.

![](<../../.gitbook/assets/16 (2).png>)

![Ein Bild, das Text, Reihe, Schrift, Screenshot enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/17 (2).png>)

You will need to add two BODs in this section for this connection point. These being Sync.ChartOfAccounts and Sync.CodeDefinition, to add these BODs do the following:

**Sync.ChartOfAccounts**

* Click on the PLUS (+) icon

![Ein Bild, das Text, Screenshot, Schrift, Zahl enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/18 (2).png>)

* Select “Send to API”

![Ein Bild, das Text, Schrift, Grafiken, Logo enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/19 (2).png>)

* Search for the Sync.ChartOfAccounts BOD

![Ein Bild, das Text, Screenshot, Reihe, Schrift enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/20 (2).png>)

* Switch to the ION API tab, copy the API name and search for the API Call by pressing the SELECT button
* At product, select the API Endpoint that you created for the environment you are working with, which you created in ION API. Search for the following API call, select the API call and press OK.

Once you have completed the above steps, you will have successfully configured the Sync.ChartOfAccounts BOD. Click on the PLUS icon to add the next and final BOD.

**Sync.CodeDefinition (TotalFlexDimensions)**

The connection tab for your CodeDefinition connection point should look similar to what is illustrated below. Give the connection point an appropriate name and description, as well as import the Service Account you created.

* Select “Send to API”
* Search for the Sync.CodeDefinition BOD

Once you have completed the above steps, you will have successfully configured the Sync.CodeDefinition BOD for the TotalFlexDimensions master data table.

**FinalFlexDimensions**

The connection tab for your FinalFlexDimensions connection point should look similar to what is illustrated below. Give the connection point an appropriate name and description, as well as import the Service Account you created.

You will need to add one BOD in this section for this connection point. This being the Sync.CodeDefinition, to add this BOD do the following:

The connection tab for your CodeDefinition connection point should look similar to what is illustrated below. Give the connection point an appropriate name and description, as well as import the Service Account you created.

* Select “Send to API”
* Search for the Sync.CodeDefinition BOD

Once you have completed the above steps, you will have successfully configured the Sync.CodeDefinition BOD for the FinalFlexDimensions master data table.

**Data Flows**

You will need to configure two separate data flows for Auto Accounting:

* ChartOfAccounts
* FinalFlexDimensions

**ChartOfAccounts**

An overview of this data flow looks as shown below (the amount of DocBits API connection points at the end depends on the amount of different environments you are configuring).

**LN Company**



The configuration for this connection point depends on the LN company which contains the master data you wish to import into DocBits, yours should look similar to what is shown below.

**Document**



The following documents need to be added to the data flow:

* Sync.ChartOfAccounts
* Sync.CodeDefinition
