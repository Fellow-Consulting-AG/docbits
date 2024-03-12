# Tax Codes

### Tax Codes

### Create DocBits Connection Points

Open ION Desk → Connect → Connection Points

![Ein Bild, das Text, Screenshot, Schrift, Software enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/0 (4).png>)

You will need 4 connection points for this dataflow, 3 API connection points for the different tax code categories (full, reduced and free) and an Application connection point representing your LN company.

In order to create new connection points, select the “+ADD” button”

![Ein Bild, das Text, Screenshot, Schrift, Reihe enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/1 (4).png>)

Select “API” at the bottom of the list of options

![Ein Bild, das Text, Screenshot, Reihe, Diagramm enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/2 (4).png>)

You will be taken to the following page

![Ein Bild, das Screenshot enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/3 (4).png>)

This is where you will enter all the details of the TaxCode connection point. For each of the three connection points you will be creating do the following

* Enter a Name: TaxCodeFull, TaxCodeReduced, TaxCodeFree
* Description: This can be the same as the Name or similar
* Import a service account you created.

Switch to the “Documents” tab and select the PLUS icon to add the BOD we need, like below

![Ein Bild, das Text, Schrift, Logo, Grafiken enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/4 (4).png>)

Search for the BOD

![Ein Bild, das Text, Screenshot, Reihe, Schrift enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/5 (4).png>)

Search for the BOD called “Sync.LnTaxCode”, click on it and press “OK” to add the BOD.

![Ein Bild, das Text, Screenshot, Reihe, Diagramm enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/6 (4).png>)

Move on to the ION API section. Under API Call Name you can use the name of the BOD, Sync.LnTaxCode

Press the “SELECT” button

![Ein Bild, das Screenshot, Text enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/7 (4).png>)

Select the API you configured for the environment you are working with and search for the following API. Once you have selected it, press “OK”.

![Ein Bild, das Text, Screenshot, Reihe, Schrift enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/8 (4).png>)

Next, switch to the **Request Body** tab.

Here is where there will be a slight change for each connection point, this is seen in the field mappings you will assign to each tax code as they differ slightly.

![Ein Bild, das Text, Reihe, Zahl, Screenshot enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/9 (4).png>)

In the field\_mappings row, under value, is where you will put the specific field mappings for the specific tax code connection point you are creating (full, reduced or free). These mappings are available at https://docbits.com/doc/field-mappings/.

The end result should look the same or similar to the image above. Once this is done, click the SAVE option located here.

![Ein Bild, das Screenshot, Text, Zahl, Reihe enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/10 (4).png>)
