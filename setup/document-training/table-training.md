# Table Training

**Table Training**

**Training Mode vs Correction Mode**

When using our table extraction tool, you can choose between training mode and correction mode. Here’s what you need to know about each mode:

**Training Mode**

In training mode, mapped columns are read-only, and you cannot manually change the text. Additionally, the delete row button is not visible.

![Ein Bild, das Text, Screenshot, Software, Diagramm enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/0 (12).png>)

**Correction Mode**

In correction mode, you can delete and add rows, and you can manually change the text of mapped columns.

![Ein Bild, das Screenshot, Text enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/1 (11).png>)

Here’s an example of a table in correction mode, with the first row deleted and a new row added:

![correction mode](<../../.gitbook/assets/2 (11).png>)

3.2.1 **Define Table and Columns**

**Define Tables**

To define tables and columns on a document please import a document, open it and go to the table extraction view like already known (via “Line Items”).

![Ein Bild, das Screenshot, Text, Software, Zahl enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/3 (11).png>)

You will end up in following screen where you can activate the Training Mode:

![training](<../../.gitbook/assets/4 (11).png>)

Via the “Edit” button table selection mode will be activated and you will be able to edit the document shown on the left side:

![edit-button](<../../.gitbook/assets/5 (11).png>)

In general your are now able to use the autodetect tables functionality and the system will automatically define the tables on the document:

![Ein Bild, das Text, Screenshot, Software, Webseite enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/6 (11).png>)

If the system is not able to find the tables automatically you can manually define the tables on the document like shown in the video below:

**Define Columns**

Once the tables are defined you can manually define the columns via the following button:

![add-column](<../../.gitbook/assets/7 (11).png>)

Define and sort the columns via drag and drop on the document. Repeat this for the tables on the other pages as well. As an alternative if the tables are equal on each page you can use the following button to use the same column for all tables defined in the document. This functionality copies the columns that you have defined to all other pages as well:

![restore-extracted-tables](<../../.gitbook/assets/8 (11).png>)

If the document is very confusing, it can be zoomed in and out using the “Zoom in” and “Zoom out” functionality. This is helpful, for example, when a lot of information is close together and this makes it difficult to define the columns:

![zoom](<../../.gitbook/assets/9 (11).png>)

If you defined a column by mistake it can be selected by clicking it and deleted via the following button:

![delete-column](<../../.gitbook/assets/10 (11).png>)

Note: The button is only visible if the column is selected.

If you are done defining all tables and all columns on your document use the “Save” button to activate your changes and to extract the data from the document:

![Ein Bild, das Text, Schrift, Screenshot, Software enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/11 (10).png>)

The data of all defined areas will be extracted and shown on the right side:

![extracted columns](<../../.gitbook/assets/12 (10).png>)

In the next section you will learn how to adjust the data that has been extracted.

3.2.2 **Add New Column**

If you need to manually map columns to rows (fields) on an extracted document, you can do so easily in DocBits. Follow our step-by-step guide below to learn how to add a new column to a table in DocBits.

* Open the Table Extraction View

To get started, import your document into DocBits and open it. Then, navigate to the table extraction view by clicking on the “LINE ITEMS” button.

![table extraction](<../../.gitbook/assets/13 (10).png>)

* Activate Training Mode

To add a new column to your table, you’ll need to activate training mode. Click on the “TRAINING MODE” button to do so.

![Ein Bild, das Text, Screenshot, Schrift, Marke enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/14 (10).png>)

* Create a New Column

Once you’re in training mode, you can create a new column by clicking on the “ADD COLUMN” button. In the window that appears, you can specify a name for the column, set whether it’s optional or mandatory, and choose the column type (STRING, AMOUNT, or DATE).

![Ein Bild, das Text, Screenshot, Software, Multimedia-Software enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/15 (10).png>)

* Use the New Column for Manual Mappings

After you’ve created your new column, you can use it for manual mappings by following our guide on Manual Row Selection.

![Ein Bild, das Text, Screenshot, Schrift enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/16 (10).png>)

3.2.3 **Mapping Columns**

Mapping columns is a crucial step in accurate table extraction using DocBits. Once you’ve extracted data from a document, you can map the extracted columns with the columns given by DocBits. This ensures that the extracted data is correctly placed in the corresponding columns.

![mapping-columns](<../../.gitbook/assets/17 (8).png>)

To map columns, simply select the header of a column in the extraction view. A dropdown menu will appear, allowing you to select the column you want to map. If you’ve mapped a column incorrectly, you can easily remap it by clicking the dropdown menu again.

3.2.4 **Group Function**

Once a table has been extracted via DocBits and the columns have been mapped, the obtained data can be grouped to get a structured result set of all extracted data.

**What is meant by Group Function?**

All documents from order confirmations to invoices can vary enormously in complexity from company to company. For example, in documents, information may be presented in tables in some columns across multiple rows and in other columns across only one row.

As an example, you can see the German invoice below, where the information in column “Bezeichnung” extends over several lines (positions).

![Ein Bild, das Text, Schrift, Reihe, Zahl enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/18 (7).png>)

At this point, another advantage of DocBits comes into play. It extracts the data in the first step 1 to 1. The result looks like this:

![Ein Bild, das Text, Screenshot, Zahl, Schrift enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/19 (6).png>)

**BUT** now there is the possibility to group data based on a specific column. That means in this case it can be grouped by the column “Position” as shown in the following video. This in turn groups the rows of the “Description” column into one row. So that at the end you get a structured overall picture of the export and the data can now be processed further.

The result of grouping looks like this:

![Ein Bild, das Text, Screenshot, Schrift enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/20 (6).png>)

3.2.5 **Manual Row Selection**

It is possible that on some documents text in rows is not only written under one column. It might happen that it is written through different columns like in the example below.

On the screenshot you can see that the table and columns have already been defined. Having a detailed look at the highlighted information (PRAEF) you will recognize that the text is written through columns “Bezeichnung”, “Menge”, “ME” and “Preis in EUR”.

In that case it is not possible for the system to automatically define to which column the information belongs.

To solve this issue DocBits offers a possibility to manually select and map information on a document to any column.

First of all make sure training mode is activated

In addition you need to activate the row edit mode

Please note that the manual mapping of text to a column is only possible for extractable columns (blue color).

The violet ones can not be mapped manually as the mapping has already been done via the columns defined on the document.

3.2.6 **Advanced Settings**

In the table extraction view, you will find the menu item Settings in the upper action bar (make sure that the training mode is activated). If you click on the gear icon, a window will open in which you will find the Advanced Settings.

Below functionalities are available in general settings:

* **Header row count**

Here you can define the number of lines of a table header. For example, the table header line can be two lines:

Accordingly, the value in “Header row count” is set to two

Why is this needed? It might be that DocBits does not recognize the second line in the table header as part of the header line. In this case, it incorrectly inserts it into the table as an extracted value. This can be easily prevented with this function.

Example before

Example after

* **Move Extra Rows to Trash**

In this example, the item description in the table spans several rows, but you only need the first one. To extract only this and include it in the Description column, select Move Extra Rows to Trash.

After naming the columns and mapping them to position, you get the following result

The functionalities below are available in the advanced settings:



* **Minimum grouped rows**

Enter the minimum number of rows in your grouped column here.

In this table you see six rows of which only three are relevant for you. In the first two columns there are two criteria that have to be extracted separately. These will be your mapped columns all the other ones have to be trained as custom columns.\
And this is how it works step by step:

Select the two header rows as well as two minimum grouped rows as these should be grouped to one row.

Also select the Move extra rows to Trash option to be able to train all the other columns as custom columns.

Name the first column Position and group on that one.

After naming all the columns and training the values, this is your result:

* **Reverse grouping**

If you want to combine all the rows above the grouped attribute, check the box here.

In this example, the table starts with a row that is above all other information but also needs to be extracted along with the information below it. It could be that DocBits (DOC²) extracts this row as an additional row and the grouping of the information, e.g. by position, does not work properly.

After grouping on net amount, checking the box, selecting the Move extra rows to Trash option

and naming all columns this is your result

3.2.7 **Save and Delete Rules**

If you’re using DocBits for document/table extraction, it’s important to save and delete rules properly to ensure your data is extracted accurately. This guide will walk you through the process.

**Save Rules**

Once you’ve trained a document in DocBits and defined all the rules for table extraction, you can save those rules for future imports. This means that the tables in your documents will be extracted automatically, without any manual training required.

To save your rules, simply click the “SAVE RULES” button. You’ll see a rule indicator that shows how many rules have been defined and saved for that document.

**Delete Rules**

If you need to delete rules for a document, you can do so using the “DELETE RULES” button. This may be necessary if rules have been saved incorrectly or if you need to retrain a document.

However, it’s important to note that deleting rules will affect all documents with the same or similar format. This means that you’ll need to retrain those documents from scratch. So, be sure to use this feature with caution.
