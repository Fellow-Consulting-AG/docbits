# LN Configuration

### LN Configuration

**Prerequisites**

You have created:

* An ION API Endpoint
* An ION API File
* A BOD Mapping File
* An IDM Mapping File

### Import Mapping Files

Before you set up the data flow, you need to import the mapping files into InforOS

This is done by:

* In ION Desk → Connect and open Mappings

![Ein Bild, das Text, Screenshot, Schrift enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/0 (8).png>)

* Click on the Import icon

![Ein Bild, das Text, Screenshot, Schrift, Electric Blue (Farbe) enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/1 (8).png>)

* From here you need to select the various mapping files you will need which include: SyncCaptDoc\_SyncSuppInv, SyncSupplierInvoice\_LoadSupplierInvoice, and LoadSupplierInvoice\_ProcessSupplierInvoice.
* Once you have imported all the mappings files, make sure to approve each of them by clicking the tick icon within each of their squares on the Mapping dashboard.

### DocBits to LN

The next step is to setup the Data Flow in ION Desk, navigate to the ION Desk application and select Data Flow → + ADD → Document Flow like below

![Ein Bild, das Text, Software, Screenshot, Multimedia-Software enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/2 (8).png>)

You will then see this page, this is where you will build the flow of information from DocBits to M3

![Ein Bild, das Screenshot, Software, Computersymbol, Text enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/3 (8).png>)

An LN data flow will look similar to what is shown below (there are multiple paths due to each individual path being meant for a specific document type, for this explanation we will focus on the invoice data flow).

![Ein Bild, das Diagramm, Plan, Text, Reihe enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/4 (8).png>)

All parts of the chain are dragged and dropped from the top section

In the chain, DocBits and LN are both Applications whereas in between them there are mappings that convert the data into a form that can be understood by the next section of the dataflow and “map” the information so that it goes to where it is needed or meant too.

![Ein Bild, das Diagramm, Text, Screenshot, Reihe enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/5 (8).png>)

### DocBits Application

Give it the appropriate name such as “DocBits” then select the plus sign and search for the connection point you created earlier such as DocBits\_Export or similar and click on it.

To create this connection point, go to ION Desk → Connect → Connection Points

![Ein Bild, das Text, Screenshot, Schrift, Design enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/6 (8).png>)

Click “+ Add”

![Ein Bild, das Text, Software, Screenshot enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/7 (8).png>)

Select “IMS via API Gateway” and fill in the following information

![Ein Bild, das Screenshot, Text enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/8 (8).png>)

The ION API Client ID is in the ION API File you created at How to Create an ION API File under the “ci” value.

Switch to the document tab, and add the Sync.CaptureDocument BOD to the DocBits connection point like below.

![Ein Bild, das Text, Software, Screenshot enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/9 (8).png>)

Then save the connection point by pressing the disk icon in the upper-left corner.

Navigate back to the Dataflow section of ION Desk to access your dataflow. Your DocBits application should look similar to what is shown below.

![Ein Bild, das Text, Screenshot, Reihe, Quittung enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/10 (8).png>)

### Mapping 1

The first mapping node should look as follows

![Ein Bild, das Text, Reihe, Screenshot, Quittung enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/11 (7).png>)

### Mapping 2

The second mapping node should look as follows

![Ein Bild, das Text, Reihe, Screenshot, Quittung enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/12 (7).png>)

### LN Application

There should already be an LN or similarly named connection point (for the appropriate LN company) created in INFOR so, just like the DocBits Application you select it by clicking the “+” sign and it should look as follows

![Ein Bild, das Text, Screenshot, Reihe, Quittung enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/13 (7).png>)

### BODs

![Ein Bild, das Diagramm, Reihe, Plan, Schrift enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/14 (7).png>)

The following configurations should look as follows:

* First

![Ein Bild, das Screenshot, Text, Quittung enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/15 (7).png>)

* Second

![Ein Bild, das Screenshot, Text, Rechteck enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/16 (7).png>)

* Third

![Ein Bild, das Text, Screenshot, weiß, Reihe enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/17 (6).png>)

The last icon should be empty as it is not carrying any document or information.

Once you have added all necessary nodes to the data flow, press this button to activate the data flow

![Ein Bild, das Text, Screenshot, Software, Schrift enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/18 (5).png>)

4.3 Exporting to IDM

If you only require your document to be exported to IDM or Document Management in INFOR, the configuration is similar to that of the export to IDM + LN/M3 but does not require any BOD Mapping file as there is no export to LN/M3 required.

Select the following option for exporting.

![Ein Bild, das Text, Screenshot, Computersymbol enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/19 (4).png>)

You will be required to upload an ION API file as well as an IDM Mapping file.

![Ein Bild, das Text, Reihe, Schrift, Screenshot enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/20 (4).png>)

How to obtain these has been discussed earlier in this documentation. ION API file (150) and IDM MApping file (158).
