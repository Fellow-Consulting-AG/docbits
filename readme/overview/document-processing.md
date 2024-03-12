# Document Processing

### Document Processing <a href="#z1whyubn3zgu" id="z1whyubn3zgu"></a>

#### **Module** <a href="#id-56oo79nj6u2z" id="id-56oo79nj6u2z"></a>

**Approval Before Export**

This feature can be accessed via Settings → Document Types, select the document type you would like to enable this feature for and then select the settings/gear icon.

You will then be able to enable the approval before export feature, you can activate first approval as well as second approval if two people need to approve of a document before it can be exported.

In order to assign members of your organization to these approval roles, click [here](https://docbits.com/doc/settings/groups-users-and-permissions/). To modify the permissions, select “View Permissions” and you will be directed to this screen.

Once you have accessed the permissions menu, you can select the permissions you wish to assign.

Now you can customize the Approval features according to your requirements.

Understanding the Document Exporting Process in DocBits

When you are ready to export a document, select the export option at the bottom of the validation screen.

If the feature is enabled, the document’s status will change to “Pending Approval”.

The document is now in queue for approval.

Assign the approver using the “assign” button on the Dashboard. You can also manage email notifications for the approver(s) through Settings → Email Notification.

Use the Approval Before Export feature to streamline your document management process in DocBits, making your workflows more efficient.

**Doc Script**

If you want to use scripts that, for example, **convert currency characters or written-out currency names into ISO codes**, activate this first in the Settings → Modules → Doc Script.

After that, go to the desired document type. Once here, select the Scripts option.

You will be taken to the Scripts Menu. Once here, click on +NEW.

From here you have the choice of a Label, the document type, when the script for the document type should be triggered and also a specific sub document type if necessary. After adding the script in the provided area, click on SAVE.

For example:

currency\_map = {

"€": "EUR",

"EURO": "EUR",

"$": "USD",

"£": "GBP"

}

currency\_value = get\_field\_value(fields\_dict, "currency", None)

if currency\_value:

currency\_value = currency\_value.upper()

if currency\_value in currency\_map:

currency\_value = currency\_map\[currency\_value]

set\_field\_value(fields\_dict, "currency", currency\_value)



In the next step, upload a document with one of the following criteria: “€”, “EURO”, “$” or “£”.

When the document is ready for validation, open this and click in the Currency validation field. You will be prompted to select the appropriate area on the image. Now do this with the € sign.

You will then immediately see that € is converted to EUR by the script. The same is done by the script when you mark EURO on the invoice.

**Doc Scan**

**Download Scanner Software**

Click Scan Document on the DocBits Dashboard

As your scanner is not installed yet, you’ll get the following message

Depending on which operating system you use, press the appropriate button to download.

Open the installation file and you will see the following

Click on \`Continue\`, accept the Software License Agreement with \`Agree\` and continue to install the software.

Installing this software requires 33,6 MB of space. You can change the install location before clicking \`Install\` in the next step. As soon as the following screen is displayed you’re almost done.

Open web browser to test if the app works by entering: https://local.polydocs.io:12500/

If you see this message on the screen, you must first configure some settings in your FritzBox network settings if you are using one.

When you see this screen you are ready to click on DocBits.

You will be redirected to the DocBits login page where you can enter your credentials to access your dashboard.

All you have to do now is activate Doc Scan in the settings under Modules.

**FritzBox network settings**



If you get the following error after installing and calling up the url https://local.polydocs.io:12500/, the reasons are:

* DNS resolution of private IP addresses not possible.
* DNS resolution for domain names that refer to private IP addresses in the FRITZ!Box home network is not possible via the FRITZ!Box. This means that server services in the FRITZ!Box home network cannot be accessed via the domain name.

You may see one of the following error messages:

* “DNS timed out”
* “DNS request timed out”

For security reasons, the FRITZ!Box suppresses DNS responses that refer to IP addresses in your own home network. This is a security feature of the FRITZ!Box to protect against so-called DNS rebinding attacks.

If you use a FritzBox, you must first make the following settings in the FritzBox menu:

* In the FRITZ!Box user interface, click on \`Heimnetz\`.
* \`Heimnetz\` Click in the menu \`Netzwerk\`.
* Click on the tab \`Netzwerkeinstellungen\`.

In the Hostname exceptions \`DNS-Rebind-Schutz section\`, enter local.polydocs.io for which DNS rebind protection should not apply. Confirm with \`Übernehmen\`

Uninstall Doc2Scan Service Manager

Run the following command to uninstall Doc2Scan Manager:

sudo bash /Library/doc2scan/uninstall.sh

DocScan is compatible with a variety of scanners, to see the full list of compatible scanners, visit: https://docbits.com/doc/settings/modules/doc-scan/



**IDM ACL Updater**

**Feature Description**

This is a feature which, every 6 hours, uses the ION-API file to connect to your Infor-IDM and check through the newest/latest documents of the IDM-document-type(s) the DocBits team has configured at your request, and if the document type has an incorrect ACL-Setting (for example public), it will then be changed to the ACL-Setting you want (for example private). The image below illustrates the configuration of the API performing this feature

The API is called “DocBits-Error” and is situated at the end in the above dataflow. The endpoint mapped to the API (DocBits\_Import) is the endpoint that carries out the functions discussed earlier.

**How to enable the IDM ACL Updater**

To enable this feature, from the Dashboard, go to Settings.

Navigate to Document processing → Module

Once in the Module menu, you will find the slider to enable the IDM ACL Updater at the bottom of the page.

Once enabled, you simply need to upload the corresponding ION API file in the space provided as well as other data (eg. the document type) from INFOR as indicated. This data can be added by pressing the ADD button.

**Swiss QR Code**

Feature Description

This feature extracts the QR code from a document (for example, a Swiss invoice) and uses the QR code to display the embedded information from the document.

This way information is automatically extracted from the document.

What can be extracted?

QR code extraction is able to extract all necessary information from a document such as recipient data, supplier data, amounts, dates, etc.

How to enable this feature

From the Dashboard, navigate to Settings → Document Processing → Module.

Once at this menu, you will find the “QR Code extraction” slider near the bottom of the page.

This feature can be turned on and off from this menu depending on if you would like to use it or not.

**Annotation**

**Validation Screen**

After uploading a document to DocBits, once it is ready for validation, enter the validation screen.

Click on the Annotation icon indicated below

By clicking anywhere on the document, while Annotation mode is active, you will create an editable section like this

* Edit button

This option (the pencil icon) allows you to add various annotations to the document. Once clicked, the following menu will be displayed.

Here you can type text, change the font, change the character size, add bold and italics, as well as change the color of the text for the annotation you wish to add. For example, If I wish to have the word “TEXT” in RED indicated on the document, it would look as follows.

Then simply press the SAVE button indicated below

The result will look like this

From here, you can move the annotation freely around the document so that it is placed where you would like it to be.

* Save Button

Once you have created your annotation and moved it to your desired location on the document, press the SAVE icon like below

* Delete Button

If you wish to delete an annotation, simply press the DELETE icon indicated below

**Approval**

When approving a document, there are slight changes to the annotation system. These are explored below.

Once you upload your document to DocBits, validate it and attempt to export it. If you have **Approve before Export** enabled in the settings, you will need to first approve the document before it gets exported. This screen will look like this

You have the following tools when it comes to annotations on this approval menu

* Stamp Icon

This is the icon on the far left, it gives you the option to add a stamp to the document. When clicked, you are given a drop-down menu of stamp options to apply to the document.

Select the stamp you wish to add to the document and then click the ADD button

A stamp, like the one above, will be added to the document. From there you can change the size of the stamp and where it is located on the document, once the stamp is added, the same icons and functions are present as there were on the validation screen.

* Text Annotation

By clicking the text annotation icon like below

You will be given the same functionalities as were present on the validation screen annotation mode, the only difference here is that we have provided shortcut options to the right of the button. The multi-colored “T” icons can be used to quickly add annotations in the color represented by the icon, to ensure as little time is wasted when processing your documents.



