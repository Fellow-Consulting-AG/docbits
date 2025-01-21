
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

|Automated Tests|Last Execution : In Development|
|-|-|
|[**Client Tests**](#client-tests)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Gmail Import](#Gmail-Import)|https://img.shields.io/badge/_-none-grey.svg|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Microsoft Import](#Microsoft-Import)|https://img.shields.io/badge/_-none-grey.svg|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Imap Import](#Imap-Import)|https://img.shields.io/badge/_-none-grey.svg|
|[**Feature Tests**](#Feature-Tests)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Setup Email Import](#Setup-Email-Import)|https://img.shields.io/badge/_-none-grey.svg|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Notify Sender On Import](#Notify-Sender-On-Import)|https://img.shields.io/badge/_-none-grey.svg|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Move Email After Import](#Move-Email-After-Import)|https://img.shields.io/badge/_-none-grey.svg|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Error Message on Failed Import](#Error-Message-on-Failed-Import)|https://img.shields.io/badge/_-none-grey.svg|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Import Single Email Attachment](#Import-Single-Email-Attachment)|https://img.shields.io/badge/_-none-grey.svg|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Import Multiple Attachments](#Import-Multiple-Attachments)|https://img.shields.io/badge/_-none-grey.svg|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Merge Multiple Attachments](#Merge-Multiple-Attachments)|https://img.shields.io/badge/_-none-grey.svg|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Handle Duplicate Documents](#Handle-Duplicate-Documents)|https://img.shields.io/badge/_-none-grey.svg|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Block Duplicate Documents](#Block-Duplicate-Documents)|https://img.shields.io/badge/_-none-grey.svg|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Block Duplicates Across Attachments](#Block-Duplicates-Across-Attachments)|https://img.shields.io/badge/_-none-grey.svg|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Handle Corrupted Files](#Handle-Corrupted-Files)|https://img.shields.io/badge/_-none-grey.svg|

## Demo

|Automated Tests|Last Execution : In Development|
|-|-|
|[**Client Tests**](#client-tests)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Gmail Import](#Gmail-Import)|https://img.shields.io/badge/_-none-grey.svg|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Microsoft Import](#Microsoft-Import)|https://img.shields.io/badge/_-none-grey.svg|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Imap Import](#Imap-Import)|https://img.shields.io/badge/_-none-grey.svg|
|[**Feature Tests**](#Feature-Tests)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Setup Email Import](#Setup-Email-Import)|https://img.shields.io/badge/_-none-grey.svg|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Notify Sender On Import](#Notify-Sender-On-Import)|https://img.shields.io/badge/_-none-grey.svg|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Move Email After Import](#Move-Email-After-Import)|https://img.shields.io/badge/_-none-grey.svg|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Error Message on Failed Import](#Error-Message-on-Failed-Import)|https://img.shields.io/badge/_-none-grey.svg|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Import Single Email Attachment](#Import-Single-Email-Attachment)|https://img.shields.io/badge/_-none-grey.svg|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Import Multiple Attachments](#Import-Multiple-Attachments)|https://img.shields.io/badge/_-none-grey.svg|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Merge Multiple Attachments](#Merge-Multiple-Attachments)|https://img.shields.io/badge/_-none-grey.svg|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Handle Duplicate Documents](#Handle-Duplicate-Documents)|https://img.shields.io/badge/_-none-grey.svg|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Block Duplicate Documents](#Block-Duplicate-Documents)|https://img.shields.io/badge/_-none-grey.svg|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Block Duplicates Across Attachments](#Block-Duplicates-Across-Attachments)|https://img.shields.io/badge/_-none-grey.svg|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Handle Corrupted Files](#Handle-Corrupted-Files)|https://img.shields.io/badge/_-none-grey.svg|

## Sandbox

|Automated Tests|Last Execution : 21-01-25 (08:59)|
|-|-|
|[**Client Tests**](#client-tests)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Gmail Import ](#Gmail-Import-)|https://img.shields.io/badge/_-failed-red.svg|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Microsoft Import ](#Microsoft-Import-)|https://img.shields.io/badge/_-failed-red.svg|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Imap Import ](#Imap-Import-)|https://img.shields.io/badge/_-passed-green.svg|
|[**Feature Tests**](#Feature-Tests)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Setup Email Import](#Setup-Email-Import)|https://img.shields.io/badge/_-failed-red.svg|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Notify Sender On Import](#Notify-Sender-On-Import)|https://img.shields.io/badge/_-failed-red.svg|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Move Email After Import](#Move-Email-After-Import)|https://img.shields.io/badge/_-failed-red.svg|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Import Single Email Attachment](#Import-Single-Email-Attachment)|https://img.shields.io/badge/_-failed-red.svg|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Import Multiple Attachments](#Import-Multiple-Attachments)|https://img.shields.io/badge/_-failed-red.svg|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Merge Multiple Attachments](#Merge-Multiple-Attachments)|https://img.shields.io/badge/_-failed-red.svg|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Handle Duplicate Documents](#Handle-Duplicate-Documents)|https://img.shields.io/badge/_-failed-red.svg|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Block Duplicate Documents](#Block-Duplicate-Documents)|https://img.shields.io/badge/_-failed-red.svg|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Handle Corrupted Files](#Handle-Corrupted-Files)|https://img.shields.io/badge/_-failed-red.svg|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Error Message On Failed Import](#Error-Message-On-Failed-Import)|https://img.shields.io/badge/_-failed-red.svg|

## Stage

|Automated Tests|Last Execution : In Development|
|-|-|
|[**Client Tests**](#client-tests)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Gmail Import](#Gmail-Import)|https://img.shields.io/badge/_-none-grey.svg|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Microsoft Import](#Microsoft-Import)|https://img.shields.io/badge/_-none-grey.svg|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Imap Import](#Imap-Import)|https://img.shields.io/badge/_-none-grey.svg|
|[**Feature Tests**](#Feature-Tests)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Setup Email Import](#Setup-Email-Import)|https://img.shields.io/badge/_-none-grey.svg|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Notify Sender On Import](#Notify-Sender-On-Import)|https://img.shields.io/badge/_-none-grey.svg|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Move Email After Import](#Move-Email-After-Import)|https://img.shields.io/badge/_-none-grey.svg|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Error Message on Failed Import](#Error-Message-on-Failed-Import)|https://img.shields.io/badge/_-none-grey.svg|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Import Single Email Attachment](#Import-Single-Email-Attachment)|https://img.shields.io/badge/_-none-grey.svg|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Import Multiple Attachments](#Import-Multiple-Attachments)|https://img.shields.io/badge/_-none-grey.svg|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Merge Multiple Attachments](#Merge-Multiple-Attachments)|https://img.shields.io/badge/_-none-grey.svg|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Handle Duplicate Documents](#Handle-Duplicate-Documents)|https://img.shields.io/badge/_-none-grey.svg|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Block Duplicate Documents](#Block-Duplicate-Documents)|https://img.shields.io/badge/_-none-grey.svg|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Block Duplicates Across Attachments](#Block-Duplicates-Across-Attachments)|https://img.shields.io/badge/_-none-grey.svg|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Handle Corrupted Files](#Handle-Corrupted-Files)|https://img.shields.io/badge/_-none-grey.svg|

## Development

|Automated Tests|Last Execution : 03-01-25 (18:56)|
|-|-|
|[**Client Tests**](#client-tests)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Setup Email Import](#Setup-Email-Import)|https://img.shields.io/badge/_-passed-green.svg|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Notify Sender On Import](#Notify-Sender-On-Import)|https://img.shields.io/badge/_-failed-red.svg|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Move Email After Import](#Move-Email-After-Import)|https://img.shields.io/badge/_-failed-red.svg|
|[**Feature Tests**](#Feature-Tests)|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Import Single Email Attachment](#Import-Single-Email-Attachment)|https://img.shields.io/badge/_-failed-red.svg|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Import Multiple Attachments](#Import-Multiple-Attachments)|https://img.shields.io/badge/_-failed-red.svg|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Merge Multiple Attachments](#Merge-Multiple-Attachments)|https://img.shields.io/badge/_-failed-red.svg|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Handle Duplicate Documents](#Handle-Duplicate-Documents)|https://img.shields.io/badge/_-failed-red.svg|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Block Duplicate Documents](#Block-Duplicate-Documents)|https://img.shields.io/badge/_-failed-red.svg|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Block Duplicates Across Attachments](#Block-Duplicates-Across-Attachments)|https://img.shields.io/badge/_-failed-red.svg|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Handle Corrupted Files](#Handle-Corrupted-Files)|https://img.shields.io/badge/_-failed-red.svg|



## Client Tests

### Gmail Client
- **Establish Connection:** Connect with email server from Gmail 

### Microsoft Client
- **Establish Connection:** Connect with email server from Microsoft 

### Imap Client
- **Establish Connection:** Connect with email server from any imap provider 

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
