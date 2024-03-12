# M3 Configuration

**M3 Configuration**

**Prerequisites**

You have created:

* An ION API Endpoint
* An ION API File
* A BOD Mapping File
* An IDM Mapping File

**Import Mapping Files**

Before you setup the dataflow, you need to import the mapping files into InforOS.

* In ION Desk → Connect and open Mappings

![Ein Bild, das Text, Screenshot, Schrift enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/0 (9).png>)

* Click on the Import icon

![Ein Bild, das Text, Screenshot, Schrift, Electric Blue (Farbe) enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/1 (9).png>)

* From here you need to select the various mapping files you will need which include: SyncCaptDoc\_SyncSuppInv, SyncSupplierInvoice\_LoadSupplierInvoice, and LoadSupplierInvoice\_ProcessSupplierInvoice.
* Once you have imported all the mappings files, make sure to approve each of them by clicking the tick icon within each of their squares on the Mapping dashboard.

**DocBits to M3**

The next step is to setup the Data Flow in ION Desk, navigate to the ION Desk application and select Data Flow → + ADD → Document Flow like below

![Ein Bild, das Text, Software, Screenshot, Multimedia-Software enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/2 (9).png>)

You will then see this page, this is where you will build the flow of information from DocBits to M3

![Ein Bild, das Screenshot, Software, Computersymbol, Text enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/3 (9).png>)

An M3 data flow will look similar to what is shown below (there are 3 DocBits applications and APIs due to it being used for 3 separate environments).

![Ein Bild, das Screenshot, Text, Software, Computersymbol enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/4 (9).png>)

All parts of the chain are dragged and dropped from the top section

In the chain, DocBits and M3 are both Applications whereas in between them there are mappings that convert the data into a form that can be understood by the next section of the train and “map” the information so that it goes to where it is needed or meant too.

![Ein Bild, das Diagramm, Reihe, Text, Screenshot enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/5 (9).png>)

**DocBits Application**

Give it the appropriate name such as “DocBits” then select the plus sign and search for the connection point you created earlier such as DocBits\_Export or similar and click on it.

To create this connection point, go to ION Desk → Connect → Connection Points

![Ein Bild, das Text, Screenshot, Schrift, Design enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/6 (9).png>)

Click “+ Add”

![Ein Bild, das Text, Software, Screenshot enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/7 (9).png>)

Select “IMS via API Gateway” and fill in the following information

![Ein Bild, das Screenshot, Text enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/8 (9).png>)

The ION API Client ID is in the ION API File you created at How to Create an ION API File, this can be found by the “ci” value.

Switch to the document tab, and add the Sync.CaptureDocument BOD to the DocBits connection point like below.

![Ein Bild, das Text, Software, Screenshot enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/9 (9).png>)

Then save the connection point by pressing the disk icon in the upper-left corner.

Navigate back to the Dataflow section of ION Desk to access your dataflow. Your DocBits application should look similar to what is shown below.

![Ein Bild, das Text, Screenshot, Reihe, Quittung enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/10 (9).png>)

**Mapping 1**

The first mapping node should look as follows

![Ein Bild, das Text, Reihe, Screenshot, Quittung enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/11 (8).png>)

**Mapping 2**

The second mapping node should look as follows

![Ein Bild, das Text, Reihe, Screenshot, Quittung enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/12 (8).png>)

**Mapping 3**

The third mapping node should look as follows

![Ein Bild, das Text, Reihe, Screenshot, Quittung enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/13 (8).png>)

**M3 Application**

There should already be a M3 or similarly named connection point created in INFOR so just like the DocBits Application you select it by clicking the “+” sign and it should look as follows

![Ein Bild, das Text, Reihe, Quittung, Screenshot enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/14 (8).png>)

**DocBits API**

You will first need to create this API as a connection point which is done by:

ION Desk → Connect → Connection Points

![Ein Bild, das Text, Screenshot, Schrift, Design enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/15 (8).png>)

Click “+ Add” and select API

![Ein Bild, das Text, Screenshot, Software, Zahl enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/16 (8).png>)

The information you fill in should look like the following

![Ein Bild, das Text, Screenshot enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/17 (7).png>)

Switch to the document tab and add the following configuration

![Ein Bild, das Text, Screenshot, Reihe, Zahl enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/18 (6).png>)

The DocBits API node should look as follows

![Ein Bild, das Text, Reihe, Quittung, Screenshot enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/19 (5).png>)

**BODs**

![Ein Bild, das Diagramm, Reihe, Schrift, Screenshot enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/20 (5).png>)

The following configurations should look as follows:

* First
* Second

**The last icon should be empty as it is not carrying any document or information.**

Once you have added all necessary nodes to the data flow, press this button to activate the data flow (after saving the data flow by pressing the hard drive icon).
