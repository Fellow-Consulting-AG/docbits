# E-Mail templates

## **Overview**

Email Templates allow you to customize automated email notifications sent from DocBits. Templates can include dynamic fields (e.g., `{{FieldID}}`), images, and HTML formatting.

## **Accessing Email Templates**

1.  Navigate to:\
    **Settings → Global Settings → Email Templates**\


    <figure><img src="../../../.gitbook/assets/image (13) (1) (1).png" alt=""><figcaption></figcaption></figure>
2. The dashboard displays all templates with:
   * **Name**
   * **Subject**
   * **Last Modified** date
   * **Actions** (Edit or Delete).

<figure><img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## **Creating a New Template**

#### **1 Basic Setup**

* Click **New**.
* Fill in the fields on the right:
  * **Name**: Template identifier (e.g., "Document Error").
  * **Subject**: Email subject line (e.g., "Action Required: Document Error").
  *   **Document Type**: Select from the dropdown (e.g., "Invoice").\


      <div align="center"><figure><img src="../../../.gitbook/assets/image (2) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure></div>

#### **2 Template Editor**

* **Menu**: Format text, add links, or insert tables.
* **HTML Editor**: Click the `<>` icon to edit raw HTML.
* **Add Images**: Use the **Upload** function.
*   **Dynamic Fields:** Insert document field values by

    * **Variable Field Option**: Select from a dropdown.
    * **Manual Entry**: Type `{{FieldID}}` (e.g., `{{InvoiceNumber}}`).

    <figure><img src="../../../.gitbook/assets/image (4) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### **3 Saving**

* Click **Save** to store the template.

## **Sending a Test Email**

1.  Open the template and click **Send Test**.\


    <figure><img src="../../../.gitbook/assets/image (5) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
2. Enter:
   * **Recipient Email** (required).
   * **Field Values** (optional; mock data for placeholders).\
     \
     ![](<../../../.gitbook/assets/image (6) (1) (1) (1).png>)
3. Review the test email and adjust the template if needed.

## **Using Templates in Notifications**

Saved templates can be linked to [**Email Notification**](email-notification/) workflows (e.g., approval reminders, status updates).
