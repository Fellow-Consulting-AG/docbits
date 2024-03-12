# Auto Accounting

### Auto Accounting

Once you have configured auto accounting for your DocBits environment, it is very important that all functionalities are tested to ensure a smooth hand-over process.

**How To Enable Auto Accounting**

* From the Dashboard, navigate to Settings → Document Processing → Module.
* Under the Purchase Order / [Auto Accounting](https://docbits.com/auto-accounting/) tab you will find the slider to enable the feature as well as a drop down box to select LN or M3

![Ein Bild, das Screenshot, Software enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/0 (10).png>)

### Accessing Auto Accounting

After you have uploaded your document and entered the validation screen, select the following icon to enter [auto accounting](https://docbits.com/doc/document-validation/master-data-validation/master-data-with-ln/auto-accounting/).

![Ein Bild, das Screenshot, Text, Software enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/1 (10).png>)

You will then be taken to this screen, this will only occur if the table has been properly trained in [order](https://docbits.com/de/use-cases/bestellung/) to distinguish between the various line items correctly.

![Ein Bild, das Screenshot, Software, Text, Zahl enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/2 (10).png>)

From here, you have two choices:

* Split the [invoice](https://docbits.com/not-again-an-invoice/) using the total amount
* Split the invoice via each individual line item

This selection is done by clicking on which option you prefer

![Ein Bild, das Screenshot, Text, Software, Webseite enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/3 (10).png>)

**Prerequisites**

In order for the [Auto Accounting](https://docbits.com/de/kostenrechnung-auto-accouting-mit-infor-ln/) feature to function, certain data and information must be configured. To assist in this process or to let you know what configuration you are missing, we have created a “Validate Setup” button which is located as shown below.

![Ein Bild, das Screenshot, Software, Text, Zahl enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/4 (10).png>)

Once pressed, DocBits will run a check of your environment to see if everything is correctly configured.

A menu that will look as follows will appear

![Ein Bild, das Text, Screenshot, Schrift enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/5 (10).png>)

All items with the green check mark in front of them mean that they are configured and working, the above image should only be used as an example and should not be followed item by item for your environment. This is due to each user having their own set of accounts, dimensions, and dimension options as categorized above.

### Splitting Amounts

This is done by clicking on the following icon next to the total amount or specific line item

![Ein Bild, das Reihe, Screenshot, Diagramm, Schrift enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/6 (10).png>)

Once you select the splitting icon, a new menu will appear underneath the selected item

![Ein Bild, das Text, Screenshot, Reihe enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/7 (10).png>)

**Accounts**

The first block of the new menu gives you access to a dropdown list where you can select an account/department from your pre configured accounts/departments which you would like to split the amount between. DocBits will group similar account types together, making it easier to find certain types of accounts or accounts related to one another.

**Amounts**

The second block allows you to manually type in the respective amounts for which the parent amount will be split into.

**Percentage Split**

The third and final block allows you to manually enter the percentage split you would like the parent amount to be split into, the amount is automatically set to 50% when entering the splitting menu but can be changed to suit your preferences. If you enter a percentage value in the block, the amount will automatically be calculated in the second block.

Keep in mind that the new amount will only be calculated once you press the ‘Enter key’ on your keyboard and that the other percentage(s) are not altered by this change, this can result in amounts that do not add up to the parent amount. For this reason, we have created an “Unsettled amount” counter in this menu which is discussed later.

**Other Features**

**Add Row**

A plus icon next to the splitting icon, this can be used in situations where an amount needs to be split between more than two accounts/departments.

![Ein Bild, das Text, Reihe, Screenshot enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/8 (10).png>)

**Delete Row**

A trash can icon that is used to delete unwanted or incorrect rows

![Ein Bild, das Text, Reihe, Screenshot, Schrift enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/9 (10).png>)

**Unsettled Amount**

An “Unsettled amount” indicator at the bottom in case of any unaccounted value or amount outstanding from the parent amount.

![Ein Bild, das Text, Screenshot, Reihe, Zahl enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/10 (10).png>)

7.1.1 **M3**

Once you have validated and exported a document, sign in to INFOR and type in the **APS450** command.

![Ein Bild, das Screenshot, Software, Text enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/11 (9).png>)

You will be taken to the following page where you will see the document you have just exported.

![Ein Bild, das Screenshot, Text, Software enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/12 (9).png>)

Once you find your document, right-click on the document and select “Related” and then the “Lines” option.

![Ein Bild, das Screenshot enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/13 (9).png>)

You will be taken to the menu that displays all the line items from the invoice you exported, ensuring all the line items are there and are correct. Lastly ensure that all these line items are classified as **Type 8**, this can be seen by looking at the following column in the table.

![](<../.gitbook/assets/14 (9).png>)

7.1.2 **LN**

Once you have validated and exported a document, sign in to INFOR. From the Home page of LN, navigate to Financials → Process Payables → Process Payables Workbench.

![Ein Bild, das Text, Screenshot, Software, Multimedia-Software enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/15 (9).png>)

Press the following icon to view the individual line items of the invoice.

![Ein Bild, das Text, Screenshot, Schrift, Zahl enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/16 (9).png>)

Here you can confirm the line items with what you exported using auto accounting.
