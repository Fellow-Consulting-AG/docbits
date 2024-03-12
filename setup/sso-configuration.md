# SSO Configuration

### SSO Configuration

**Prerequisites**

| **Required Information**       | **Description**                                                                                                                                   |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Login Details to Cloud         | Credentials are mandatory for accessing the Infor Cloud environment. The user should have the roles "Infor-SystemAdministrator" and "UserAdmin".  |
| Config Admin Details (DocBits) | You should have received an email from FellowPro AG with the login details for the DocBits SSO Settings page. You will need a login and password. |
| Certificate                    | You can download the certificate in DocBits under SSO Service Provider Settings                                                                   |

### Get access to the Cloud and check your access

URL starts with https://mingle-portal.eu1.inforcloudsuite.com/\<TENANT\_NAME> followed by your personal extension

![Ein Bild, das Text, Screenshot, Marke, Logo enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/0 (5).png>)

* Choose the option Cloud Identities and use your login details

![Ein Bild, das Text, Software, Multimedia-Software, Webseite enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/1 (5).png>)

* After login you will have access to the Infor Cloud. In this case we enter this page, but on the burger menu you will find access to all applications.

![Ein Bild, das Screenshot, Text enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/2 (5).png>)

![Ein Bild, das Software, Multimedia-Software, Screenshot, Computersymbol enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/3 (5).png>)

**Open User Management for adding new Service Provider**

On the right hand side of the bar menu, you will find the user menu and there you can access the user management

![Ein Bild, das Text, Software, Multimedia-Software, Grafiksoftware enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/4 (5).png>)

* Then you need to select in the left hand side menu the option Security Administration and Service Provider.

![Ein Bild, das Screenshot, Software, Text enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/5 (5).png>)

* You will see this window with the Service Providers.

![Ein Bild, das Screenshot, Text enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/6 (5).png>)

* Now click on the “+” sign and add our DocBits as Service Provider.

![Ein Bild, das Text, Screenshot, Zahl enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/7 (5).png>)

**Access the SSO SERVICE PROVIDER SETTINGS in DocBits**

* Log in on URL https://app.docbits.com/ with the login details you received from us.
* Go to SETTINGS (on top bar) and select INTEGRATION, under SSO Service Provider Settings you will find all the information you need for the following steps.
* Download the certificate

![Ein Bild, das Screenshot enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/8 (5).png>)

Filling the Service Provider with the help of SSO Service Provider Settings in DocBits

![Ein Bild, das Text, Software, Computersymbol, Webseite enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/9 (5).png>)

| **Field**                  | **Value**                                                                                  |
| -------------------------- | ------------------------------------------------------------------------------------------ |
| Application Type           | DEFAULT\_SAML                                                                              |
| Display Name               | DocBits                                                                                    |
| Entity ID                  | See Entity ID under SSO SERVICE SETTINGS                                                   |
| SSO Endpoint               | Copy the SSO URL from SSO SERVICE SETTINGS and paste it in the SSO Endpoint field.         |
| Signing Certificate        | Upload the appropriate .cer file you have downloaded in step 3c) from SSO SERVICE SETTINGS |
| Name ID Format and Mapping | email address                                                                              |

![Ein Bild, das Text, Screenshot, Software, Zahl enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/10 (5).png>)

* When you have filled out everything remember to save it with the disk icon above Application Type
* Enter the service provider DocBits again.
* Click on view the Identity Provider Information underneath.

![Ein Bild, das Screenshot, Text, Reihe enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/11 (4).png>)

![Ein Bild, das Text, Screenshot, Schrift, Zahl enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/12 (4).png>)

* Export the SAML METADATA.

File looks like this: ServiceProviderSAMLMetadata\_10\_20\_2021.xml

**Import the SAML METADATA in the SSO Settings.**

Go to IDENTITY SERVICE PROVIDER SETTINGS, which is located under INTEGRATIONS in SETTINGS. Enter your Tenant ID (e.g. FELLOWPRO\_DEV) and underneath that line you see the Upload file and the IMPORT Button, where you need to upload the previously exported SAML METADATA file.

* Click on IMPORT and then choose the METADATA file that you have already downloaded from the SSO SERVICE PROVIDER SETTINGS
* Click on CONFIGURE

![Ein Bild, das Screenshot enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/13 (4).png>)

**Add New Application in INFOR Ming.le**

* Go to Admin settings

![Ein Bild, das Software, Multimedia-Software, Text, Screenshot enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/14 (4).png>)

* Click on ADD APPLICATION in the top right corner

![Ein Bild, das Text, Schrift, Screenshot, Design enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/15 (4).png>)

* Fill out all fields like on the following image but with your own SSO Url, don’t forget to choose an icon and click on **SAVE.**

![Ein Bild, das Text, Screenshot, Zahl, Schrift enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/16 (4).png>)

**Final Step**

* Log out of DocBits.
* Go back to the burger menu in Infor and select the icon you just created.
* And you will be taken to the Dashboard of DocBits.
