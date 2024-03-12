# Postman for DocBits

### Postman for DocBits

This guide will show you how to make HTTP requests to your DocBits organization via Postman. It is easy to use and very useful for organization administrators.

### Setup

First, download Postman to your system and sign in/register.

Now follow this step-by-step guide to learn how HTTP requests work in Postman.

**Authorization in Postman**

Before you can create your HTTP requests, you need to enter your API key from DocBits to authorize them.

* Click on the \`Authorization\` tab and choose \`API Key\` as authorization type.

![Ein Bild, das Text, Software, Screenshot enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/0 (7).png>)

* Fill in the values. Enter “X-API-key” in the \`Key\` field and your API Key as value (found in DocBits Settings menu under Integration) Select Add to \`Header\`.
* It should look like this:

![Ein Bild, das Text, Screenshot enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/1 (7).png>)

### DocBits API

Available at https://api.polydocs.io

* Click on Authorize in the upper right corner

![Ein Bild, das Text, Schrift, Logo, Rechteck enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/2 (7).png>)

* Enter your API Key and confirm by clicking \`Authorize\`

![Ein Bild, das Text, Screenshot, Display, Schrift enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/3 (7).png>)

Create a new Workspace in Postman

* Click on Workspaces and create a new workspace (you can name it whatever you want

![Ein Bild, das Text, Screenshot, Software, Webseite enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/4 (7).png>)

* You have to select the visibility which determines who can access this workspace.

![Ein Bild, das Text, Screenshot, Schrift, Zahl enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/5 (7).png>)

* After making your selection and clicking \`Create Workspace\` select Collections on the left side of the application and create a new collection for your HTTP requests by clicking \`+\`.

![Ein Bild, das Text, Screenshot, Software, Zahl enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/6 (7).png>)

In this collection, you can add multiple HTTP requests. To do this, click on the 3 points of the collection and select \`Add request\`.

![Ein Bild, das Text, Screenshot, Zahl, Diagramm enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/7 (7).png>)

"GET" Method example

The GET method is very useful for getting information about users, sub-organizations, processed documents, and much more.

* Choose the GET method in your HTTP request.
* Authorize yourself as described above.
* Open https://api.polydocs.io and add the path of the function behind the Polydocs URL. For example:

![Ein Bild, das Text, Screenshot, Software, Webseite enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/8 (7).png>)

* Now paste this link in the text box next to the GET method in Postman.

Click \`Send\` and you should receive all the information about every user in your organization.

6.2 **"POST" Method example**

The POST method is usually used to create users or organizations, for example. This method inserts information into the database.

**Create User**

* Select the POST Method.
* Authorize yourself as described above
* Open https://api.polydocs.io and add the path of the function behind the Polydocs URL. In this case:

![Ein Bild, das Text, Screenshot, Software, Webseite enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/9 (7).png>)

* Now paste this link into the text box next to the POST method in Postman.
* Select the \`Body\` tab in your HTTP request and enter the keys and the values ​​for each credential that has a red asterisk next to its name.

When you’re done, it should look like this:

![Ein Bild, das Text, Schrift, Zahl, Reihe enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/10 (7).png>)

If you want to create an admin account, set the \`is\_admin\` value to true.

Finally, click \`Send\` and you can see all the credentials you set in the response below. This means the user has been created.

**Upload Document**

You can also use the POST method to upload a document to DocBits.

* Select the POST Method.
* Authorize yourself as described above.
* Open https://api.polydocs.io and add the path of the function behind the Polydocs URL.

In this case:

![Ein Bild, das Text, Software, Screenshot, Computersymbol enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/11 (6).png>)

* Now paste this link into the text box next to the POST method in Postman.
* Select the \`Body\` tab in your HTTP request and choose \`form-data\`

![Ein Bild, das Text, Screenshot, Reihe, Schrift enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/12 (6).png>)

![Ein Bild, das Text, Screenshot, Schrift, Reihe enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/13 (6).png>)

Enter file into the \`KEY\` field where you will find the hidden File dropdown. Select \`File\` and move to the \`VALUE\` field where you are able to select your file by clicking \`Select Files\`.

When you click \`Send\`, you should see “success”: true in the response.

It should look like this:

![Ein Bild, das Text, Screenshot, Software enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/14 (6).png>)

### "DELETE" Method example

The DELETE method is used to delete, for example, users, organizations and so on.

* Select the DELETE Method
* Authorize yourself as described above.
* Open https://api.polydocs.io and add the path of the function behind the Polydocs URL.

For example:

![Ein Bild, das Text, Zahl, Schrift, Screenshot enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/15 (6).png>)

* Now paste this link in the text box next to the DELETE method in Postman.
* Replace the {user\_id} at the end of the URL with the actual user ID you want to delete. (You can get the user\_id using the GET method).
* If you included the user\_id in the URL, you don’t need to add a body key and value for it.
* When you click \`Send\`, you should see “success”: true in the response.

It should look like this:

![Ein Bild, das Screenshot, Text enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/16 (6).png>)

### "PUT" Method example

The PUT method is mainly used to update user or organization data. It is very easy to understand and use.

* Select the PUT Method.
* Authorize yourself as described above.
* Open https://api.polydocs.io and add the path of the function behind the Polydocs URL.

For example:

![Ein Bild, das Text, Screenshot enthält.

Automatisch generierte Beschreibung](<../.gitbook/assets/17 (5).png>)

* Now paste this link in the text box next to the PUT method in Postman.
* Replace the {user\_id} at the end of the URL with the actual user ID you want to delete. (You can get the user\_id using the GET method).

### Change Email Address of a User

* In the body, enter “email” as the key and the new email address as the value.
* Then just press \`Send\` and you should see “success” in the response.
