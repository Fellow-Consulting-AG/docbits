# PO Matching

**PO Matching**

When it comes to testing your PO Matching configuration, you will need to create a Purchase order in LN/M3 in order to check whether INFOR is synced with DocBits.

Once you have created your purchase order, go to Settings → Master Data Lookup and search for the purchase order number of the PO you just created as it should now appear in your purchase order master data in DocBIts.

![Ein Bild, das Screenshot, Text enthält.

Automatisch generierte Beschreibung](<../../.gitbook/assets/0 (11).png>)

You should see your unique PO number here, this means that DocBits and INFOR are correctly synced.

Now upload your invoice that matches the quantity and unit prices of the purchase order you created. Validate the document and select PO Matching on the validation screen.
