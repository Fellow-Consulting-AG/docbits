# Inbound Emails

## Activating Inbound Email for Document Processing

To begin using inbound email for document processing, follow these steps:

1. **Go to Settings**: Start by navigating to the app’s **Settings** menu.
2. **Select Document Processing**: Under settings, choose **Document Processing** to access related configuration options.
3. **Open Modules**: In the Document Processing section, click on **Modules**.
4. **Scroll to Document Type**: Scroll down until you find **Document Type**.
5. **Activate Inbound Email**: Find **Inbound Email** and activate it by toggling the switch.

<figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Configuring Inbound Email for Document Import

<figure><img src="../../../../.gitbook/assets/image (3) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

After activating inbound email, configure the settings to control how documents are imported. Here’s how:

1. **Go back Document Processing**: In the settings, navigate to **Document Processing**.
2.  **Select Import**: Choose **Import** to access inbound email settings.

    You’ll see the following options:

    * **Email Field**: This field displays a unique, system-generated email address based on your organization ID. The format is `org_id@environment.inbound.docbits.com`. Send or forward emails with documents to this address for automated import.
    * **Import Document Only from Predefined E-Mail(s)**: Toggle this option to restrict imports to emails received only from specific, predefined addresses.
    * **Reply to this Email if Import Cannot Be Done**: Toggle this option if you want the system to automatically reply when an import attempt fails.
3. **Save Settings**: After configuring these options, click **Save** to apply them.

## Predefined E-Mail(s)

<figure><img src="../../../../.gitbook/assets/image (4) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

When the **Import Document Only from Predefined E-Mail(s)** option is enabled, you can manage which email addresses are authorized to send documents to the inbound email.

1. **Enter Authorized Emails**: In the **Put E-mail here** field, type each email address you want to authorize.
2. **Assign to Sub-Organization (Optional)**:
   * If no sub-organization is selected, the document will be assigned to the main organization.
   * If a sub-organization is selected, the document will be directed to that sub-organization only.
3. **Add Email**: Click **Add** to save each email to the list of authorized addresses.
4. **Delete Email**: To remove an authorized email, click **Delete** next to the email entry.

With this setup, documents from unauthorized email addresses will be ignored, ensuring only specific sources can send documents for import.

## **Reply to this email if import can not be done**

<figure><img src="../../../../.gitbook/assets/image (5) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

If you enable **Reply to this email if import can not be done**, an additional field appears where you can enter an email address. This email address will receive a notification if any document import attempt fails, allowing you to stay informed of any issues in the import process.

1. **Enable Failure Notification**: Toggle on **Reply to this email if import can not be done**.
2. **Enter Notification Email**: In the new field, enter the email address where you’d like to receive failure notifications.

With this feature enabled, any failed import attempts will trigger an automatic reply to the specified email, helping you quickly address import issues.

**After configuring all settings, don’t forget to click Save to apply your changes.**
