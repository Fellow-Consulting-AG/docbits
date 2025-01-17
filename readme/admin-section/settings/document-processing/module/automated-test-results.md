
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
|[Gmail Import](#Gmail-Import)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-none-grey.svg'></div>|
|[Microsoft Import](#Microsoft-Import)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-none-grey.svg'></div>|
|[Imap Import](#Imap-Import)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-none-grey.svg'></div>|
|[**Feature Tests**](#Feature-Tests)|
|[Setup Email Import](#Setup-Email-Import)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-none-grey.svg'></div>|
|[Notify Sender On Import](#Notify-Sender-On-Import)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-none-grey.svg'></div>|
|[Move Email After Import](#Move-Email-After-Import)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-none-grey.svg'></div>|
|[Error Message on Failed Import](#Error-Message-on-Failed-Import)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-none-grey.svg'></div>|
|[Import Single Email Attachment](#Import-Single-Email-Attachment)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-none-grey.svg'></div>|
|[Import Multiple Attachments](#Import-Multiple-Attachments)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-none-grey.svg'></div>|
|[Merge Multiple Attachments](#Merge-Multiple-Attachments)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-none-grey.svg'></div>|
|[Handle Duplicate Documents](#Handle-Duplicate-Documents)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-none-grey.svg'></div>|
|[Block Duplicate Documents](#Block-Duplicate-Documents)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-none-grey.svg'></div>|
|[Block Duplicates Across Attachments](#Block-Duplicates-Across-Attachments)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-none-grey.svg'></div>|
|[Handle Corrupted Files](#Handle-Corrupted-Files)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-none-grey.svg'></div>|

## Demo

|Automated Tests|Last Execution : In Development|
|-|-|
|[**Client Tests**](#client-tests)|
|[Gmail Import](#Gmail-Import)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-none-grey.svg'></div>|
|[Microsoft Import](#Microsoft-Import)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-none-grey.svg'></div>|
|[Imap Import](#Imap-Import)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-none-grey.svg'></div>|
|[**Feature Tests**](#Feature-Tests)|
|[Setup Email Import](#Setup-Email-Import)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-none-grey.svg'></div>|
|[Notify Sender On Import](#Notify-Sender-On-Import)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-none-grey.svg'></div>|
|[Move Email After Import](#Move-Email-After-Import)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-none-grey.svg'></div>|
|[Error Message on Failed Import](#Error-Message-on-Failed-Import)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-none-grey.svg'></div>|
|[Import Single Email Attachment](#Import-Single-Email-Attachment)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-none-grey.svg'></div>|
|[Import Multiple Attachments](#Import-Multiple-Attachments)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-none-grey.svg'></div>|
|[Merge Multiple Attachments](#Merge-Multiple-Attachments)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-none-grey.svg'></div>|
|[Handle Duplicate Documents](#Handle-Duplicate-Documents)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-none-grey.svg'></div>|
|[Block Duplicate Documents](#Block-Duplicate-Documents)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-none-grey.svg'></div>|
|[Block Duplicates Across Attachments](#Block-Duplicates-Across-Attachments)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-none-grey.svg'></div>|
|[Handle Corrupted Files](#Handle-Corrupted-Files)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-none-grey.svg'></div>|

## Sandbox

|Automated Tests|Last Execution : 25-01-16 19:19|
|-|-|
|[**Client Tests**](#client-tests)|
|[Gmail Import ](#Gmail-Import-)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-passed-green.svg'></div>|
|[Microsoft Import ](#Microsoft-Import-)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-passed-green.svg'></div>|
|[Imap Import ](#Imap-Import-)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-passed-green.svg'></div>|
|[**Feature Tests**](#Feature-Tests)|
|[Setup Email Import](#Setup-Email-Import)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-passed-green.svg'></div>|
|[Notify Sender On Import](#Notify-Sender-On-Import)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-passed-green.svg'></div>|
|[Move Email After Import](#Move-Email-After-Import)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-passed-green.svg'></div>|
|[Import Single Email Attachment](#Import-Single-Email-Attachment)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-passed-green.svg'></div>|
|[Import Multiple Attachments](#Import-Multiple-Attachments)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-passed-green.svg'></div>|
|[Merge Multiple Attachments](#Merge-Multiple-Attachments)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-passed-green.svg'></div>|
|[Handle Duplicate Documents](#Handle-Duplicate-Documents)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-passed-green.svg'></div>|
|[Block Duplicate Documents](#Block-Duplicate-Documents)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-passed-green.svg'></div>|
|[Handle Corrupted Files](#Handle-Corrupted-Files)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-passed-green.svg'></div>|
|[Error Message On Failed Import](#Error-Message-On-Failed-Import)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-passed-green.svg'></div>|

## Stage

|Automated Tests|Last Execution : In Development|
|-|-|
|[**Client Tests**](#client-tests)|
|[Gmail Import](#Gmail-Import)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-none-grey.svg'></div>|
|[Microsoft Import](#Microsoft-Import)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-none-grey.svg'></div>|
|[Imap Import](#Imap-Import)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-none-grey.svg'></div>|
|[**Feature Tests**](#Feature-Tests)|
|[Setup Email Import](#Setup-Email-Import)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-none-grey.svg'></div>|
|[Notify Sender On Import](#Notify-Sender-On-Import)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-none-grey.svg'></div>|
|[Move Email After Import](#Move-Email-After-Import)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-none-grey.svg'></div>|
|[Error Message on Failed Import](#Error-Message-on-Failed-Import)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-none-grey.svg'></div>|
|[Import Single Email Attachment](#Import-Single-Email-Attachment)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-none-grey.svg'></div>|
|[Import Multiple Attachments](#Import-Multiple-Attachments)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-none-grey.svg'></div>|
|[Merge Multiple Attachments](#Merge-Multiple-Attachments)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-none-grey.svg'></div>|
|[Handle Duplicate Documents](#Handle-Duplicate-Documents)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-none-grey.svg'></div>|
|[Block Duplicate Documents](#Block-Duplicate-Documents)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-none-grey.svg'></div>|
|[Block Duplicates Across Attachments](#Block-Duplicates-Across-Attachments)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-none-grey.svg'></div>|
|[Handle Corrupted Files](#Handle-Corrupted-Files)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-none-grey.svg'></div>|

## Development

|Automated Tests|Last Execution : 25-01-16 19:19|
|-|-|
|[**Client Tests**](#client-tests)|
|[Gmail Import ](#Gmail-Import-)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-passed-green.svg'></div>|
|[Microsoft Import ](#Microsoft-Import-)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-passed-green.svg'></div>|
|[Imap Import ](#Imap-Import-)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-passed-green.svg'></div>|
|[**Feature Tests**](#Feature-Tests)|
|[Setup Email Import](#Setup-Email-Import)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-passed-green.svg'></div>|
|[Notify Sender On Import](#Notify-Sender-On-Import)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-passed-green.svg'></div>|
|[Move Email After Import](#Move-Email-After-Import)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-passed-green.svg'></div>|
|[Import Single Email Attachment](#Import-Single-Email-Attachment)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-passed-green.svg'></div>|
|[Import Multiple Attachments](#Import-Multiple-Attachments)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-passed-green.svg'></div>|
|[Merge Multiple Attachments](#Merge-Multiple-Attachments)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-passed-green.svg'></div>|
|[Handle Duplicate Documents](#Handle-Duplicate-Documents)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-passed-green.svg'></div>|
|[Block Duplicate Documents](#Block-Duplicate-Documents)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-passed-green.svg'></div>|
|[Handle Corrupted Files](#Handle-Corrupted-Files)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-passed-green.svg'></div>|
|[Error Message On Failed Import](#Error-Message-On-Failed-Import)|<div align="center" style="display: flex; align-items: center; justify-content: center; height: 100%;"><img src='https://img.shields.io/badge/_-passed-green.svg'></div>|



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
