# WatchDog V2 Configuration

This guide explains how to configure the overhauled WatchDog service within the DocBits application.

## 1. General Configuration

The General Configuration section allows you to define the core behavior of the WatchDog service.

<figure><img src="../../.gitbook/assets/watchdog_v2_01.png" alt="WatchDog Overview"><figcaption></figcaption></figure>

### 1.1 Folder Settings

Configure the file pathways for importing and exporting documents. These paths must be reachable from the Windows environment where the WatchDog service is installed.

<figure><img src="../../.gitbook/assets/watchdog_v2_02.png" alt="WatchDog Folder Settings"><figcaption></figcaption></figure>

*   **Watch Folder:** The directory where WatchDog monitors for new documents to import.
*   **Success Folder:** The directory where documents are moved after a successful import.
*   **Export Folder:** The directory where processed export files (XML/PDF) are written.

### 1.2 Processing Options

Select the **Document Types** you want WatchDog to process (e.g., `INVOICE`, `DELIVERY_NOTE`).

<figure><img src="../../.gitbook/assets/watchdog_v2_03.png" alt="WatchDog General Settings"><figcaption></figcaption></figure>

*   **Barcode Divider:** Enable this to automatically split documents based on barcodes.
*   **DocBits Operator:** Enable this to allow WatchDog to perform browser automation tasks.

### 1.3 Export Destination

Set up the export destinations and methods.

<figure><img src="../../.gitbook/assets/watchdog_v2_04.png" alt="WatchDog Export Settings"><figcaption></figcaption></figure>

---

## 2. Logs Tab

The Logs tab provides a comprehensive view of all WatchDog events, helping you monitor the service and troubleshoot issues.

<figure><img src="../../.gitbook/assets/watchdog_v2_05.png" alt="WatchDog Logs"><figcaption></figcaption></figure>

*   View event types such as `FILE_IMPORT_STARTED`, `EXPORT_COMPLETED`, and `FOLDER_VALIDATION_FAILED`.
*   Filter logs by date, event type, or specific keywords.

---

## 3. XSLT Templates Tab

Manage the XSLT transformation templates used for XML exports.

<figure><img src="../../.gitbook/assets/watchdog_v2_06.png" alt="XSLT Templates"><figcaption></figcaption></figure>

*   Upload and edit templates that define the structure of the exported data.
*   Link these templates to your export configurations.

---

## 4. Export Configurations

View and manage specific export configurations, including their connection status.

<figure><img src="../../.gitbook/assets/watchdog_v2_07.png" alt="Export Configurations"><figcaption></figcaption></figure>

*   Monitor the timestamp of the last successful connection.
*   Download the final configuration file to be used with the WatchDog executable.