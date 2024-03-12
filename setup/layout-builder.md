# Layout Builder

1.2 **Layout Builder**

**Accessing the Layout Builder**

First of all, ensure that the Layout Builder feature is activated. This can be done by navigating to Settings → Document Processing → Module → Document Type and ensure that the Layout Builder slider is set too active as shown below.

![Ein Bild, das Screenshot enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/0 (3).png>)

After this is done you can access the Layout Builder via Settings → Document Types, once on this page, you can select from the various document types you have created and either select “Edit Layout” as shown below

![](<../.gitbook/assets/1 (3).png>)

or if you have sub-document types within a created document type you can select “Document Sub Types” and select “Edit Layout” for the sub document type layout you wish to edit as shown below.

![Ein Bild, das Text, Quittung, Screenshot enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/2 (3).png>)

**Basics of the Layout Manager**

After following the previous steps you will reach a page like the one shown below.

**Uploading an example document**

In order to upload a document to the layout builder, simply navigate to the right on the screen

![Ein Bild, das Screenshot, Software, Computersymbol, Multimedia-Software enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/3 (3).png>)

Click on the “Upload Documents” button or drag and drop your desired document into the provided area

![Ein Bild, das Screenshot, Software, Computersymbol, Multimedia-Software enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/4 (3).png>)

**Groups**

Groups can be created by selecting the following icon.

![Ein Bild, das Screenshot, Software, Computersymbol, Multimedia-Software enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/5 (3).png>)

Groups allow you to create different sections on a layout, this makes it easier to separate different groups of data or information to make a layout easier to follow. You can create a title for each group so that a user can know what information they will find in that group.

![Ein Bild, das Screenshot, Software, Multimedia-Software enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/6 (3).png>)

**Form Elements**

![Ein Bild, das Text, Screenshot, Zahl, Software enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/7 (3).png>)

These are a set of default fields that can be dragged and dropped into the layout builder and are available to you to create your desired layout. These include:

* **Text** – This is a text box which creates a field in the layout that can have text entered into it once on the validation screen.
* **Label** – This is a field that can be used to create uneditable text, this could be used to create sub-headings or any other desired uneditable text when on the validation screen.
* **Checkbox** – This creates a boolean type field which can be checked or unchecked.
* **Multi Checkbox** – This functions the same way as the “Checkbox” but can be used when the user knows they will be adding multiple checkboxes in one section.
* **Horizontal Separator** – This creates a horizontal line on the layout that can be used to split up sections within a group on the layout.
* **Table of Checkboxes** – This lets the user create a table of checkboxes consisting of custom x- and y-axis values, eg.

![Ein Bild, das Text, Schrift, Reihe, Zahl enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/8 (3).png>)

* **Button** – This creates a clickable button on the validation screen within the layout that can be set to one of three functions, including: Export, Export mit Sonderwunsch or Reject.
* **Extracted Tables** -This allows you to place an area on the document layout that illustrates the table that gets extracted from the document. For information click here.
* **Invoice Buttons** – This element lets you drag and drop a set of buttons that are optimized for invoices. When on the validation screen, when you select the invoice type (either cost or purchase) the PO Matching or Auto Accounting will disappear accordingly.

![Ein Bild, das Text, Screenshot, Schrift, Reihe enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/9 (3).png>)

* **QR Code Fields** – This element allows you to drag and drop a block that will display all the extracted information from a document when a QR code is present.

**Creating document specific fields**

The user is able to create their own custom groups and fields for a document type, this can be done when originally creating a document type but also by selecting “Fields” when on the Document Types page in Settings.

![](<../.gitbook/assets/10 (3).png>)

**Blank spaces**

**The 100 percent rule**

![Ein Bild, das Screenshot, Text, Reihe, Schrift enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/11 (3).png>)

In order to create the above space on the layout, a “Label” from the Form Elements must be used in a special way. The reason for this is that the Layout Manager operates according to a 100 space per line system in that 1 space represents 1 percent of a line, this means that fields can only take up 100 spaces per line as show below.

![Ein Bild, das Text, Reihe, Zahl, Software enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/12 (3).png>)

This means that the user must build the layout line by line according to this rule. For example let's say you would like to add the fields “Name” and “Date” in the same line but would like the “Name” field to be larger. This can be done by dragging and dropping the “Text” field from the Field Elements drop down and naming each field “Name” and “Date” as shown.

![Ein Bild, das Text, Reihe, Schrift, Zahl enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/13 (3).png>)

The problem now exists that they are both the same size of 33 (this is the default size of all dragged and dropped fields) but you would like the “Name” field to be larger than the “Date” field and both fields should take up the entire line on the layout. Therefore, by following the 100 percent rule, you can set the “Name” and “Date” fields to any combination of 100 that you would desire. This of course depends on how large you would like each individual field but for the purpose of this example we will set the “Name” field to 70 and the “Date” field to 30, the results are:

![Ein Bild, das Text, Reihe, Zahl, Software enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/14 (3).png>)

This same rule applies to all fields in the Layout Builder.

**Creating Blank Spaces**

Now that this rule has been explained, creating blank spaces will make more sense. As previously mentioned, in order to create a blank space you have to use a “Label” from the Form Elements.

For example, let’s say that you would like to create a blank space between these two fields.

![Ein Bild, das Text, Reihe, Schrift, Zahl enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/15 (3).png>)

Step one is to drag and drop a “Label” between these two fields, once added you can click on the “Label” field you just added and on the left you will be presented with the properties of the field. Now, in the same way you would create or change the name of a field as shown previously, you will remove any name from the “Label” property like so

![Ein Bild, das Text, Screenshot, Schrift, Zahl enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/16 (3).png>)

The result from doing this will then be

![Ein Bild, das Text, Reihe, Schrift, Zahl enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/17 (3).png>)

There is now a gap between the two fields. This gap can be extended or shortened according to the 100 percent rule discussed earlier, and with these functions you can create any desired layout.

1.3 **Origin Layouts**

DocBits excels in adapting document layouts according to their geographical origins while standardizing elements like currency formats based on user browser settings. Let’s explore how you can leverage the Layout Builder to customize layouts for different origins, such as the U.S. and Germany.

![Ein Bild, das Text, Screenshot, Schrift, Software enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/18 (3).png>)

Understanding Origin-Based Customization

* Currency and Format Standardization: Regardless of the original document’s currency or format, DocBits converts these elements into a standardized ISO format on the server, in line with the user’s browser settings.
* Geographical Layout Customization: The system allows customization of document layouts based on their geographical origin. This means you can define specific fields and formats for documents from different countries.

Example: U.S. vs. Germany Layouts

* U.S. Layout: For a U.S. invoice, you might include fields for city tax, aligning with the common tax structure in the U.S.
* Germany Layout: In contrast, a German invoice layout may omit the city tax field, as it’s not a standard charge in Germany.

Using the Layout Builder

* Select Origin Layout: In the Layout Builder, choose the base layout corresponding to the document’s origin.
* Customize Fields: Adapt the layout by adding or removing fields. For instance, include ‘City Tax’ for a U.S. layout.
* Apply and Test: Once customized, apply the layout to your documents and test to ensure accuracy.

Tips for Effective Customization

* Understand Regional Differences: Familiarize yourself with the tax and format nuances of different regions.
* Consistent Updates: Regularly update your layouts to reflect any changes in regional regulations.
* User Feedback: Utilize feedback from users in different regions to refine layouts further.
