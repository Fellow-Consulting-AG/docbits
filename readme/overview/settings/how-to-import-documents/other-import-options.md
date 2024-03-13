# Other import Options

### Other Import Options <a href="#id-55pch9p17nt3" id="id-55pch9p17nt3"></a>

#### Email <a href="#id-92b87ridzovd" id="id-92b87ridzovd"></a>

Go to the Settings menu and select “Import”.

![](<../../../../.gitbook/assets/13 (12).png>)

Scroll to the bottom of the page and select the NEW button to create a new email import.

![](<../../../../.gitbook/assets/14 (12).png>)

After pressing NEW, the following menu will be shown to you

![](<../../../../.gitbook/assets/15 (12).png>)

Here you can select which Protocol you would like

![](<../../../../.gitbook/assets/16 (12).png>)

#### IMAP <a href="#rutixicnxq9x" id="rutixicnxq9x"></a>

Here you just need to enter the required information for your email provider, encryption, server name, port, username, email address, password as well as the email folder.

![](<../../../../.gitbook/assets/17 (10).png>)

**Things to Note**

* Input all needed information into the UI. Other information like the server, port, etc. Depends on the host (a quick Google search should help).
* Folder and Move-Imported have the same Function here. Folder can not be disabled, but will use Inbox by default if left empty
* Make sure to enable IMAP on your Email-Account-Settings
* If you have OAuth enabled on your Email, you will most likely have to provide a “App-Password”\
  generated from your Email-Account-Settings, instead of your regular Password

#### OAuth Office365 <a href="#ze89a68qq2xy" id="ze89a68qq2xy"></a>

Here you just need to enter your desired sub-organization and press ‘Authenticate’

![](<../../../../.gitbook/assets/18 (9).png>)

You will be taken to this Microsoft page and you will need to enter a code.

![](<../../../../.gitbook/assets/19 (8).png>)

This code can be found by clicking back to DocBits and the code will be displayed there like below, simply copy the code and enter it into the Microsoft page. Thereafter you will need to enter your own Microsoft credentials.

![](<../../../../.gitbook/assets/20 (8).png>)

#### Press the FINISH AUTHENTICATION button and you will be taken to this menu <a href="#ze89a68qq2xy" id="ze89a68qq2xy"></a>

**Use Folder**

If you are using a folder other than your inbox, enter the folder name after enabling the slider.

**Use Shared Mailbox**

If you want the email import to access an inbox or a folder of a shared mailbox, input the email address here after enabling the slider.

**Move imported emails to trash**

If you want to import all emails, not just the unread ones, and have them moved to trash then activate this. If not, it will only check for unread emails, import the documents, set the email to read and leave it in its current place.

In the event of you receiving an error message indicating you do not have the rights to establish such a connection, someone with admin rights within Azure would need to authorize this connection. For more information, visit the following page: **https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/grant-admin-consent?pivots=portal#grant-tenant-wide-admin-consent-in-enterprise-apps**

#### &#x20;<a href="#gxugwsq7sora" id="gxugwsq7sora"></a>
