
## Overview

These tests are designed to verify the functionality of the email import system for both single and multiple documents, ensuring that the system correctly handles various scenarios, such as duplicates, corruption, and folder management.

| Environment     |      Test Results |
|-----------------|-------------------|
| Prod|[Test Results](#prod) |
| Demo|[Test Results](#demo) |
| Sandbox|[Test Results](#sandbox) |
| Stage|[Test Results](#stage) |
| Dev|[Test Results](#development) |

## Prod

|Automated Tests|Last Execution : 29-01-25 (06:10)|
|-|-|
|[**Client Tests**](#client-tests)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Gmail Import](#gmail-import)|![badge](https://img.shields.io/badge/_-passed-green.svg)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Microsoft Import](#microsoft-import)|![badge](https://img.shields.io/badge/_-passed-green.svg)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Imap Import](#imap-import)|![badge](https://img.shields.io/badge/_-passed-green.svg)|
|[**Feature Tests**](#Feature-Tests)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Setup Email Import](#setup-email-import)|![badge](https://img.shields.io/badge/_-passed-green.svg)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Notify Sender On Import](#notify-sender-on-import)|![badge](https://img.shields.io/badge/_-passed-green.svg)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Move Email After Import](#move-email-after-import)|![badge](https://img.shields.io/badge/_-passed-green.svg)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Import Single Email Attachment](#import-single-email-attachment)|![badge](https://img.shields.io/badge/_-passed-green.svg)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Import Multiple Attachments](#import-multiple-attachments)|![badge](https://img.shields.io/badge/_-passed-green.svg)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Merge Multiple Attachments](#merge-multiple-attachments)|![badge](https://img.shields.io/badge/_-passed-green.svg)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Handle Duplicate Documents](#handle-duplicate-documents)|![badge](https://img.shields.io/badge/_-passed-green.svg)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Block Duplicate Documents](#block-duplicate-documents)|![badge](https://img.shields.io/badge/_-passed-green.svg)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Handle Corrupted Files](#handle-corrupted-files)|![badge](https://img.shields.io/badge/_-passed-green.svg)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Error Message On Failed Import](#error-message-on-failed-import)|![badge](https://img.shields.io/badge/_-passed-green.svg)|

## Demo

|Automated Tests|Last Execution : 28-01-25 (09:13)|
|-|-|
|[**Client Tests**](#client-tests)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Gmail Import](#gmail-import)|![badge](https://img.shields.io/badge/_-passed-green.svg)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Microsoft Import](#microsoft-import)|![badge](https://img.shields.io/badge/_-passed-green.svg)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Imap Import](#imap-import)|![badge](https://img.shields.io/badge/_-passed-green.svg)|
|[**Feature Tests**](#Feature-Tests)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Setup Email Import](#setup-email-import)|![badge](https://img.shields.io/badge/_-passed-green.svg)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Notify Sender On Import](#notify-sender-on-import)|![badge](https://img.shields.io/badge/_-passed-green.svg)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Move Email After Import](#move-email-after-import)|![badge](https://img.shields.io/badge/_-passed-green.svg)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Import Single Email Attachment](#import-single-email-attachment)|![badge](https://img.shields.io/badge/_-passed-green.svg)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Import Multiple Attachments](#import-multiple-attachments)|![badge](https://img.shields.io/badge/_-passed-green.svg)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Merge Multiple Attachments](#merge-multiple-attachments)|![badge](https://img.shields.io/badge/_-passed-green.svg)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Handle Duplicate Documents](#handle-duplicate-documents)|![badge](https://img.shields.io/badge/_-passed-green.svg)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Block Duplicate Documents](#block-duplicate-documents)|![badge](https://img.shields.io/badge/_-passed-green.svg)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Handle Corrupted Files](#handle-corrupted-files)|![badge](https://img.shields.io/badge/_-passed-green.svg)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Error Message On Failed Import](#error-message-on-failed-import)|![badge](https://img.shields.io/badge/_-passed-green.svg)|

## Sandbox

|Automated Tests|Last Execution : 09-03-25 (06:07)|
|-|-|
|[**Client Tests**](#client-tests)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Gmail Import](#gmail-import)|![badge](https://img.shields.io/badge/_-failed-red.svg)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Microsoft Import](#microsoft-import)|![badge](https://img.shields.io/badge/_-failed-red.svg)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Imap Import](#imap-import)|![badge](https://img.shields.io/badge/_-passed-green.svg)|
|[**Feature Tests**](#Feature-Tests)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Setup Email Import](#setup-email-import)|![badge](https://img.shields.io/badge/_-failed-red.svg)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Notify Sender On Import](#notify-sender-on-import)|![badge](https://img.shields.io/badge/_-passed-green.svg)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Move Email After Import](#move-email-after-import)|![badge](https://img.shields.io/badge/_-failed-red.svg)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Import Single Email Attachment](#import-single-email-attachment)|![badge](https://img.shields.io/badge/_-failed-red.svg)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Import Multiple Attachments](#import-multiple-attachments)|![badge](https://img.shields.io/badge/_-failed-red.svg)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Merge Multiple Attachments](#merge-multiple-attachments)|![badge](https://img.shields.io/badge/_-failed-red.svg)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Handle Duplicate Documents](#handle-duplicate-documents)|![badge](https://img.shields.io/badge/_-failed-red.svg)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Block Duplicate Documents](#block-duplicate-documents)|![badge](https://img.shields.io/badge/_-failed-red.svg)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Handle Corrupted Files](#handle-corrupted-files)|![badge](https://img.shields.io/badge/_-failed-red.svg)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Error Message On Failed Import](#error-message-on-failed-import)|![badge](https://img.shields.io/badge/_-failed-red.svg)|

## Development

|Automated Tests|Last Execution : 28-01-25 (11:14)|
|-|-|
|[**Client Tests**](#client-tests)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Gmail Import](#gmail-import)|![badge](https://img.shields.io/badge/_-failed-red.svg)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Microsoft Import](#microsoft-import)|![badge](https://img.shields.io/badge/_-failed-red.svg)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Imap Import](#imap-import)|![badge](https://img.shields.io/badge/_-passed-green.svg)|
|[**Feature Tests**](#Feature-Tests)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Setup Email Import](#setup-email-import)|![badge](https://img.shields.io/badge/_-failed-red.svg)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Notify Sender On Import](#notify-sender-on-import)|![badge](https://img.shields.io/badge/_-passed-green.svg)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Move Email After Import](#move-email-after-import)|![badge](https://img.shields.io/badge/_-passed-green.svg)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Import Single Email Attachment](#import-single-email-attachment)|![badge](https://img.shields.io/badge/_-passed-green.svg)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Import Multiple Attachments](#import-multiple-attachments)|![badge](https://img.shields.io/badge/_-passed-green.svg)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Merge Multiple Attachments](#merge-multiple-attachments)|![badge](https://img.shields.io/badge/_-failed-red.svg)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Handle Duplicate Documents](#handle-duplicate-documents)|![badge](https://img.shields.io/badge/_-passed-green.svg)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Block Duplicate Documents](#block-duplicate-documents)|![badge](https://img.shields.io/badge/_-passed-green.svg)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Handle Corrupted Files](#handle-corrupted-files)|![badge](https://img.shields.io/badge/_-failed-red.svg)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Error Message On Failed Import](#error-message-on-failed-import)|![badge](https://img.shields.io/badge/_-passed-green.svg)|



## Client Tests

### Gmail Client
- **Login Functionality:** Verifies successful login for email import connections in the Gmail client.
- **Connection Logs:** Ensures that email import connection logs are accessible and contain accurate information.
- **Import Single Document Attachment:** Validates the successful import of a single document attachment from an email.
- **Document Parsing and Saving:** Ensures that imported documents are parsed correctly and saved without errors.
- **Data Integrity During Import:** Verifies that no data is lost or corrupted during the email import process.
- **Adding New Connections:** Confirms the ability to create and configure new email import connections successfully. 

### Microsoft Client
- **Login Functionality:** Verifies successful login for email import connections in the Microsoft client.
- **Connection Logs:** Ensures that email import connection logs are accessible and contain accurate information.
- **Folder Management:** Confirms the ability to retrieve and display email import folders correctly.
- **Import Single Document Attachment:** Validates the successful import of a single document attachment from an email.
- **Document Parsing and Saving:** Ensures that imported documents are parsed correctly and saved without errors.
- **Data Integrity During Import:** Verifies that no data is lost or corrupted during the email import process.

### Imap Client
- **Login Functionality:** Verifies successful login for email import connections in the Imap client.
- **Connection Logs:** Ensures that email import connection logs are accessible and contain accurate information.
- **Folder Management:** Confirms the ability to retrieve and display email import folders correctly.
- **Import Single Document Attachment:** Validates the successful import of a single document attachment from an email.
- **Document Parsing and Saving:** Ensures that imported documents are parsed correctly and saved without errors.
- **Data Integrity During Import:** Verifies that no data is lost or corrupted during the email import process.
- **Adding New Connections:** Confirms the ability to create and configure new email import connections successfully. 

## Feature Tests

### Setup Email Import
- **Login Functionality:** Validates successful and unsuccessful login scenarios for email import connections.
- **Connection Logs:** Ensures that logs related to email import connections are accessible and contain relevant records.
- **Folder Management:** Verifies the ability to retrieve folders associated with email imports.
- **Activation and Deactivation:** Tests the functionality to activate and deactivate email import connections.
- **Adding New Connections:** Confirms the ability to create and configure new email import connections.

### Notify Sender on Import
- **Email Notification:** Ensures that notification emails are sent to the sender after an import.

### Move Email After Import
- **Email Notification and Movement:** Ensures that emails are moved to the correct folder after import, based on the configured settings.

### Error Message on Failed Import
- **Error Messages on Import Failure:** Verifies that the system displays clear and informative error messages when an email import fails.
- **Troubleshooting and Failure Diagnosis:** Ensures the system provides troubleshooting steps or detailed information to help users identify the cause of an import failure.

### Import Single Email Attachment
- **Import Single Document Attachment:** Verifies the ability to import a single document attached to an email.
- **Document Parsing and Saving:** Ensures the imported document is properly parsed and saved without errors.
- **Data Integrity During Import:** Confirms that no data is lost during the import process.

### Import Multiple Attachments
- **Import Multiple Document Attachment:** Verifies the ability to import a single document attached to an email.
- **Document Parsing and Saving:** Ensures the imported document is properly parsed and saved without errors.
- **Data Integrity During Import:** Confirms that no data is lost during the import process.

### Merge Multiple Attachments
- **Merge multiple documents:** Verifies the ability to import multiple documents attached to an email.

### Handle Duplicate Documents
- **Handle Duplicate Documents:** Tests the ability to handle and correctly process duplicate documents in email imports.

### Block Duplicate Documents
- **Block Duplicate Documents:** Tests the prevention of duplicate document imports when the "block duplicate" feature is enabled, even if the documents have different names.

### Block Duplicates Across Attachments
- **Block Duplicate Documents:** Tests the prevention of duplicate document imports when the "block duplicate" feature is enabled, even if the documents have different names.

### Handle Corrupted Files
- **Test Email Import with Corrupt Files:** Verifies that emails with corrupted attachments are handled properly during the import process.
- **Test Document Import (Valid and Corrupt Files):** Ensures both valid and corrupted files are processed correctly with the appropriate success or failure status.
