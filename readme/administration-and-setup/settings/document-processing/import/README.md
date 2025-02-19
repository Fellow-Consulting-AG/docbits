# Import

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 10.48.36.png" alt=""><figcaption></figcaption></figure>

The "Import" settings in your document processing system allow you to configure how documents are imported into the system from various sources, including settings for both FTP (File Transfer Protocol) and email. Here’s a breakdown of these settings:

### **Document Settings**:

* **Restrict to pages**: This setting allows you to limit the processing to a certain number of pages per document. The default is **60 pages**, meaning documents exceeding this limit will be trimmed to **60 pages**, and any **remaining pages will be discarded.**
* **Payment Terms Days**: Defines the default payment terms (in days) that can be applied to documents.
* **Date Pattern**: Sets the pattern for how dates should be recognized and formatted within imported documents.

### **FTP Import**:

{% content-ref url="../../../../end-user-and-partner-section/end-user-section/how-to-import-documents/ftp.md" %}
[ftp.md](../../../../end-user-and-partner-section/end-user-section/how-to-import-documents/ftp.md)
{% endcontent-ref %}

* **Type**: Defines the type of FTP protocol to use (e.g., SFTP).
* **Server URL**: The server address where documents will be fetched from.
* **Username and Port**: Credentials and port number for accessing the FTP server.
* **Default Directory**: Specifies the directory on the FTP server from where files will be imported.

The additional option to add new data includes fields like:

* **Password**: For authentication.
* **File name matching patterns**: To specify which files to import based on their names.
* **Sub-Organizations**: Select which sub-organization the import settings should apply to.

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 10.48.45.png" alt=""><figcaption></figcaption></figure>

### **Email Import**:

{% content-ref url="../../../../end-user-and-partner-section/end-user-section/how-to-import-documents/email/" %}
[email](../../../../end-user-and-partner-section/end-user-section/how-to-import-documents/email/)
{% endcontent-ref %}

* **Email Address**: Setup an email account where documents can be sent for import.
* **Username and Password**: Credentials for accessing the email account.
* **Protocol and Encryption**: Specify the protocol (IMAP, POP3) and the encryption type.
* **Merge attached documents**: Option to combine all attached documents into a single document upon import.

This also allows specifying sub-organizations for more precise control over where emails are directed within your organizational structure.

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 10.48.56.png" alt=""><figcaption></figcaption></figure>
