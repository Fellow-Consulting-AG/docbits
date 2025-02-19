# How to Create Database Access for a Specific Organization User

### **1. Login to the Docbits** <a href="#id-1.-login-to-the-docbits" id="id-1.-login-to-the-docbits"></a>

1. Go to your application login page.
2. Enter your credentials (username and password) to log in.

### **2. Access the Settings** <a href="#id-2.-access-the-settings" id="id-2.-access-the-settings"></a>

1. Once logged in, locate the **Settings** icon (gear ⚙️) on the left-hand sidebar.
2. Click on **Settings** to open the system configuration panel.

### **3. Open the Document Processing Module** <a href="#id-3.-open-the-document-processing-module" id="id-3.-open-the-document-processing-module"></a>

1. In the **Settings**, locate the **Document Processing** section.
2. Under **Document Processing**, find and click on the **Module** option.
   * This will open the relevant module configuration page where you can proceed with creation of user for database.

<figure><img src="../../../../../.gitbook/assets/image (25).png" alt=""><figcaption></figcaption></figure>

### 4. Steps to Enable and Access the AI Document and Database User: <a href="#id-4.-steps-to-enable-and-access-the-ai-document-and-database-user" id="id-4.-steps-to-enable-and-access-the-ai-document-and-database-user"></a>

1. **Toggle Features**:
   * Use the toggles on the right to enable or disable specific features:
     * **AI Document Warehouse**: Toggle this to enable access to AI-related features.
     * **DB Access**: Toggle this to grant database access to user.

<figure><img src="../../../../../.gitbook/assets/image (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

2. **Database Credentials**:
   * The dashboard provides the following database connection details:
     * **Username**: A unique username is displayed&#x20;
     * **Password**: Ensure the password is securely stored or copied.
     * **Database**: Is the name of the Database&#x20;
     * **Host**: Host Name&#x20;
     * **Port**:  Is the Port&#x20;
     * **SSL Mode:** The connection requires `sslmode=require` for secure communication.
3. **Copying Credentials**:
   * Use the copy icons next to each field to quickly copy the credentials for use in your database client or application.
4. **Connection via DBeaver:**
   *   Connect via Host

       * choose PostgreSQL

       <figure><img src="../../../../../.gitbook/assets/image (2) (1) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

       * Fill in the required information&#x20;

       <figure><img src="../../../../../.gitbook/assets/image (4) (1).png" alt=""><figcaption></figcaption></figure>

       * change to the SSL tab and check Use SSL. Move down to SSL mode and select require

       <figure><img src="../../../../../.gitbook/assets/image (3) (1).png" alt=""><figcaption></figcaption></figure>
   *   Connect via URL

       * Fill in the required information:\
         \- replace Host with the provided host information\
         \- replace Port with the provided port information\
         \- replace Database with the provided database information\
         \- for Username select the provided username information\
         \- for Password select the provided password information

       <figure><img src="../../../../../.gitbook/assets/image (5) (1).png" alt=""><figcaption></figcaption></figure>
5. **Test the Connection**:
   * Click the **"Test Connection"** button to ensure the credentials and connection details are correct.
   * If the test is successful, proceed to connect.
6. **Explore the Database**:
   * Once connected, navigate to the **schema** or **tables** section in your database client.
   * Check the available tables.
