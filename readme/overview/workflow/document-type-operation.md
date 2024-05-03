# Document Type Operation

<figure><img src="../../../.gitbook/assets/userlmn_14ab8ac5e693d9bbe68d178795d12a9f.png" alt=""><figcaption></figcaption></figure>

**Purpose**

This workflow card is designed to trigger specific actions based on whether a document's type matches or does not match a specified list of types. It's essential for managing documents that require different handling procedures depending on their categorization.

**Components of the Card**

1. **Operator**
   * **Description**: Specifies the logical condition under which the action will be performed.
   * **Options**:
     * **"is"**: The action is triggered if the document's type matches one of the types listed.
     * **"is not"**: The action is triggered if the document's type does not match any of the types listed.
2. **Document Types**
   * **Description**: Lists the document types that will trigger or prevent an action based on the chosen operator.
   * **Detail**: Could include document categories such as "Invoice", "Purchase Order", "Contract", "Employee Record", etc. The operation's execution depends on whether the document type is or is not among these specified types.

**Functionality**

* **Document Identification and Classification**: Automatically identifies incoming documents and classifies them by type.
* **Conditional Logic Execution**:
  * If the operator is **"is"**, the specified operation is executed for documents whose type matches one listed.
  * If the operator is **"is not"**, the operation is executed for documents whose type does not match any of those listed.
* **Operation Execution**: Depending on the outcome of the condition check, various operations can be triggered, such as:
  * **Archive**
  * **Review**
  * **Process**
  * **Send for Approval**
* **Compliance and Security Checks**: Ensures all operations adhere to regulatory requirements and internal policies, particularly important for sensitive or critical document types.

**User Interactions**

* **Setup and Configuration**: Users configure the card by selecting the operator ("is" or "is not") and specifying the relevant document types. They may also set other parameters or conditions as needed for their processes.
* **Monitoring and Oversight**: Provides a dashboard for users to monitor the operations, view logs of executed actions, and track the handling of documents based on their type.
* **Error Handling and Alerts**: Includes mechanisms for handling errors or exceptions in document processing. Users can set alerts for anomalies or misclassifications.

#### Conclusion

The "Document Type Operation" workflow card with "is" and "is not" operators allows for sophisticated handling of documents within an ERP system, ensuring that each type is processed appropriately. This flexibility is crucial for maintaining operational efficiency and compliance. Proper documentation of this workflow card will help users understand how to effectively configure and utilize this feature to manage document flows based on specific types within the organization, enhancing productivity and compliance.
