# Email Import Automated Tests

## Overview

These tests are designed to verify the functionality of the email import system for both single and multiple documents, ensuring that the system correctly handles various scenarios, such as duplicates, corruption, and folder management.

## Connection Test

* **Test Connection**: Verifies the connection to the email import system.
* **Connection Logs**: Shows logs for connection events.
* **Folder Field Dropdown**: Tests the dropdown for folder selection.
* **Connection Logs Auto-Update**: Ensures that connection logs are automatically updated every 4 minutes.

_Purpose_: These tests validate that the connection to the email import system is working properly.

## Single Document Import Test Cases

These tests focus on importing individual documents to verify that the system handles various conditions correctly:

* **Single document (no sender)**: Test importing a document with no sender information.
* **Single document (with sender + move folder)**: Tests importing a document with sender information and moving it to a folder.
* **Single document (with sender + import error + move folder)**: Verifies that importing a document with a sender and an import error works correctly, and that the document is moved to the folder.
* **Duplicate document (with sender + import error + move folder + block duplicate)**: Tests importing a duplicate document and ensuring it is blocked from being re-imported.

## Multi Document Import Test Cases

These tests check the functionality when importing multiple documents, with different conditions for merging, errors, and duplicates:

* **Multiple documents (no merge, email to sender)**: Tests importing multiple documents without merging them.
* **Multiple documents (no merge, email to sender + move folder)**: Verifies importing multiple documents without merging and moving them to a folder.
* **Multiple documents (merge + move folder)**: Tests importing multiple documents with merging and moving them to a folder.
* **Multiple documents (merge + email to sender + move folder)**: Verifies importing and merging multiple documents, emailing the sender, and moving them to a folder.
* **No corrupted documents (merge + email to sender + import error + move folder)**: Ensures no documents are corrupted during import when merging, with an import error and folder move.
* **Duplicate document (email to sender + import error + move folder + block duplicate)**: Tests handling a duplicate document with an import error and folder move, ensuring it’s blocked.
* **Duplicate document (merge + email to sender + import error + move folder + block duplicate)**: Verifies blocking duplicates when merging documents and handling errors.
* **Duplicate document (merge + email to sender + import error + move folder + unblock duplicate)**: Tests unblocking duplicates in merged documents when handling import errors.
* **Duplicate all documents (email to sender + import error + move folder + block duplicate)**: Verifies that all duplicate documents are blocked during import.
* **Duplicate all documents (email to sender + import error + move folder + unblock duplicate)**: Tests unblocking all duplicate documents during import after an error.

## Single & Corrupt Document + Multi & Corrupt Document Import Test Cases

These tests validate the system’s behavior when importing single or multiple corrupt documents:

* **Single corrupt document (email to sender + move folder)**: Verifies handling of a corrupt document, with the sender emailed and the document moved to a folder.
* **Corrupt document (no duplicate, email to sender + import error + move folder + block duplicate)**: Tests handling a corrupt document without duplicates, with an import error and folder move.
* **Corrupt document (no duplicate, merge + email to sender + import error + move folder + unblock duplicate)**: Verifies handling a corrupt document during a merge, emailing the sender, and managing duplicates.
* **Corrupt all documents (email to sender + import error + move folder + unblock duplicate)**: Tests handling all documents as corrupt, sending an import error, and moving them to a folder while unblocking duplicates.

## Summary

These automated tests are designed to thoroughly check the email import system’s functionality across different scenarios for both single and multiple document imports, including handling errors, duplicates, and corrupted documents. Each test ensures that the system behaves as expected in real-world usage.
