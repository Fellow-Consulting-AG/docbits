# Watchdog

### Watchdog <a href="#u7ijoxn30bnf" id="u7ijoxn30bnf"></a>

**Installation and Settings**

After downloading the WatchDog.exe file, search for Command Prompt → Run as administrator on your Windows device.

Once this is opened, call the file by typing the path of where the WatchDog.exe file is stored on your device like below

Type install after the file path and press ENTER on your keyboard

You should receive the following error message as it will start the application in UI mode and there is no configuration present yet.

The application will automatically open up after installation. At the top, navigate to Einstellungen (Settings) and here you will see 2 separate sections.

**Folder settings (Ordner Einstellungen)**



This is where you will configure the file pathways for where the documents will be read and processed. The read pathway will be for the documents that you want WatchDog to extract and process, whereas the processed pathway will be used to indicate which documents from the read folder where extracted and processed.

**General settings (Allgemeine Einstellungen)**

This is where you will configure your DocBits application with WatchDog. You will be required to enter your DocBits environment, API key and the document type (as indicated above). To add more than one document type, separate the names of the document types with a comma (INVOICE,DELIVERY-NOTE,PURCHASE-ORDER, etc.)

If an invalid configuration is entered for any of the fields, you will receive an error message like the one below.

Once this is complete, go back to the Command Prompt area and re-run the WatchDog.exe file and this time it will be correctly installed due to the configurations now being present

To start the application is UI mode, run the following command

If you just want to start the application, run this command instead.

**Auto Start**

In order to set up the WatchDog app in a manner that allows it to automatically start once you turn your system on.

Simply open “Services” in the settings of your Windows machine.

Search for WatchDog in the local services and open the service (double-click on the entry)

In the above menu you will have the following options for automatic starting:

* Select Automatic, the service will start on boot
* Automatic (Delayed Start), this will wait 2 minutes after boot to start the service
