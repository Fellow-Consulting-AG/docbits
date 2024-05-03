# Assigned User Condition

<figure><img src="../../../.gitbook/assets/userlmn_5e16e9b23626ec1211c753fec5333513.png" alt=""><figcaption></figcaption></figure>

**Purpose**

This card is designed to control document-related actions based on whether a document is assigned to a specific user or a group of users. By leveraging simple conditional logic (is/is not), it allows for targeted operations, making it crucial for managing tasks and document flows that are dependent on user assignments within an ERP system.

**Components of the Card**

1. **Operator**
   * **Description**: Specifies how to evaluate the assignment of the document.
   * **Options**:
     * **is**: Triggers the operation if the document's assigned user matches any user specified in the list.
     * **is not**: Triggers the operation if the document's assigned user does not match any users specified in the list.
2. **User**
   * **Description**: Identifies one or multiple users as the criterion for the operation.
   * **Detail**: Users can select one or several users from a predefined list. This selection determines the condition under which the document's assignment will trigger further actions.

**Functionality**

* **Assignment Verification**: The system checks the assigned user of a document against the selected conditions.
* **Condition Evaluation**:
  * If the operator is **is**, the card checks if the document’s assigned user is among those specified.
  * If the operator is **is not**, the card checks if the document’s assigned user is not among those listed.
* **Action Execution**:
  * **True Condition**: If the condition is met (either is or is not, depending on the operator), relevant workflows are triggered. These could include notifications, moving the document to the next step in a process, or other automated actions.
  * **False Condition**: If the condition is not met, alternate workflows may be initiated, or the document may simply remain static until reassignment or further review.

**User Interactions**

* **Setup and Configuration**: Users set up the card by selecting an operator and choosing users from a list. The interface might include checkboxes or a multi-select dropdown for user selection.
* **Monitoring and Reporting**: Provides the capability to monitor the status of assignments through real-time updates or logs, which can help in tracking the flow of documents and ensuring that they are being handled by the correct personnel.
* **Error Handling and Notifications**: The system can be configured to alert users if there is a discrepancy in assignments or if an unauthorized user attempts to process a document.

#### Conclusion

The "Assigned User Condition" workflow card is a powerful tool for ensuring that documents in an ERP system are processed by the appropriate personnel. By documenting this card clearly, you help users understand its importance and how to effectively use it to streamline their document workflows, enhance accountability, and improve overall operational efficiency. This detailed guide should facilitate correct implementation and maximize the benefits of using this workflow card in your ERP system.
