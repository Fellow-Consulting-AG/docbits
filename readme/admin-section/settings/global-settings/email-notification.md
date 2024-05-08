# Email Notification

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 10.15.45.png" alt=""><figcaption></figcaption></figure>

Email notifications in Docbits can be configured to alert users about various document-related events, such as completion of processing, errors during import or export, or requirements for user intervention. This tool is essential for maintaining effective communication and operational continuity in document processing environments.

#### Key Features and Options

1. **Email Notification Configuration**:
   * **Name**: The identifier for the notification, helping users recognize the purpose of the notification setting.
   * **Document Type**: Associates the notification with a specific document type, allowing for targeted alerts based on the document's processing cycle.
   * **Status**: Defines the specific status change that triggers the notification, such as 'Export Error' or 'Ready for Validation'.
   * **Priority**: Sets the urgency level of the notification, which can prioritize the email alert in the recipient's inbox.
   * **Delay**: Configures a delay time before sending the notification, allowing for cancellations or corrections before the alert is issued.
   * **Email Address**: Specifies the recipients of the notification. Users can enter multiple email addresses or dynamically assign email addresses based on document properties or user roles.
2. **Actionable Insights**:
   * **Send Email to Assigned User**: An optional setting that, when enabled, automatically sends notifications to the user assigned to the document, ensuring that the responsible party is always informed.

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 10.15.56.png" alt=""><figcaption></figcaption></figure>

This setting is critical for ensuring that stakeholders are kept informed about the processing status of important documents, which aids in rapid decision-making and efficient management of document workflows.



{% @jira/embed url="https://fellowpro.atlassian.net/browse/DOCB-2501" %}
