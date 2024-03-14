# Email Import APIs Overview

The Email Import APIs are designed to facilitate the integration and management of email-based document importation within the system. These APIs allow for configuring email import settings, fetching import logs, and testing email login credentials.

### Endpoints

#### Get Import Log

* **Endpoint**: `GET /email_import/import_log`
* **Description**: Retrieves a log of recent email imports. This API supports pagination and filtering by date, connection type, and success status.
* **Parameters**:
  * `limit`: Maximum number of log entries to return (default: 25).
  * `offset`: Pagination offset (default: 0).
  * `start_date`: Filter log entries starting from this date.
  * `connection_type`: Type of email import connection (default: "email\_import").
  * `order_by_direction`: Ordering direction of log entries (default: "none").
  * `sub_org_id`: Filter log entries by sub-organization ID.
  * `success_status`: Filter log entries by their success status.

#### Get Email Configurations

* **Endpoint**: `GET /email_import/list`
* **Description**: Lists all email configurations set up for importing documents. This endpoint is crucial for managing and reviewing how email accounts are configured for document importation.

#### Fetch Emails

* **Endpoint**: `GET /email_import/fetch_emails`
* **Description**: Initiates a manual fetch of emails for import based on the specified configuration. This is useful for testing or triggering imports outside of automatic intervals.
* **Parameters**:
  * `id`: The ID of the email configuration to use for fetching emails.

#### Test Existing Login

* **Endpoint**: `POST /email_import/test_exsisting_login`
* **Description**: Tests the login credentials of an existing email import configuration to ensure they are still valid.
* **RequestBody**: Encoded form data including email import configuration details.

#### Deactivate or Activate Email

* **Endpoint**: `POST /email_import/(de)-activate_email`
* **Description**: Allows for the activation or deactivation of an email import configuration. This is useful for temporarily disabling email imports without deleting the configuration.
* **RequestBody**: Encoded form data specifying the email configuration to be (de)activated.

#### Change Folder and Email

* **Endpoint**: `POST /email_import/change_folder_and_email`
* **Description**: Updates the email or folder associated with an existing email import configuration.
* **RequestBody**: Encoded form data with new email or folder details.

### Security

All Email Import APIs require API key authentication. Ensure your API key is included in the header of each request.

###
