# WatchDog Admin FAQ & Troubleshooting

This documentation is designed to help administrators understand WatchDog error messages and troubleshoot issues.

**UI Location:** Settings → Document Processing → WatchDog

---

## 1. WatchDog Settings Pages (UI)

### 1.1 General Configuration

*   **Folder Settings:** Configure import and export folder paths.
*   **Document Types:** Define which document types are processed (INVOICE, CREDIT_NOTE, PURCHASE_ORDER, etc.).
*   **Export Destination:** Choose between Infor or Folder Export.
*   **Barcode Divider:** Activates barcode-based document separation.
*   **DocBits Operator:** Activates browser automation.

### 1.2 Logs Tab

*   Shows all WatchDog events from OpenSearch.
*   Filterable by event type, time period, etc.
*   **Event Types:**
    *   `FILE_IMPORT_STARTED`: File import started
    *   `FILE_IMPORT_COMPLETED`: Import successful
    *   `FILE_IMPORT_FAILED`: Import failed
    *   `EXPORT_STARTED`: Export started
    *   `EXPORT_COMPLETED`: Export successful
    *   `EXPORT_FAILED`: Export failed
    *   `FOLDER_VALIDATION_FAILED`: Folder not reachable
    *   `CONFIG_LOADED`: Configuration loaded
    *   `SERVICE_RESTART_INITIATED`: Service restart requested
    *   `SERVICE_RESTART_COMPLETED`: Service restarted

### 1.3 XSLT Templates Tab

*   Upload and management of XSLT transformation templates.
*   Templates are used for XML export transformations.
*   Link to export configurations.

---

## 2. Folder Validation Error Messages

| Error | Meaning | Solution |
| :--- | :--- | :--- |
| `not_found` | Folder does not exist | Create folder or correct path |
| `no_read_access` | No read permission | Set permissions for WatchDog Service Account |
| `no_write_access` | No write permission | Grant write rights to Service Account |
| `not_configured` | Folder path not configured | Enter path in configuration |

**Affected Folders:**

*   **Watch Folder (Import):** Where WatchDog looks for new files.
*   **Success Folder:** Where successfully imported files are moved.
*   **Export Folder:** Where exported XML/PDF files are written.

---

## 3. Import Error Messages

| Error | Meaning | Solution |
| :--- | :--- | :--- |
| `file_not_found` | File was deleted before import | Provide file again |
| `invalid_file_type` | Only PDF files are supported | Remove other file types |
| `api_not_accessible` | DocBits API not reachable | Check network/firewall, verify API URL |
| `api_check_failed` | API Health Check failed | Check API Key and connection |
| `upload_failed` | Upload to API failed | Check API Key, network, server status |

---

## 4. Export Error Messages

| Error | Meaning | Solution |
| :--- | :--- | :--- |
| `transformation_error` | XSLT Transformation failed | Check XSLT Template, validate XML structure |
| `folder_error` | Export folder not reachable | Create folder, check permissions |
| `file_write_error` | File could not be written | Check disk space, permissions, file locks |
| `permission_denied` | No write permission | Set Service Account permissions |
| `creation_failed` | Folder could not be created | Check parent folder permissions |
| `no_config_match` | No matching export configuration | Create export config for document type |

---

## 5. Configuration Disabled - Reasons

When a configuration is disabled, one of these reasons appears:

| Disabled Reason | Meaning |
| :--- | :--- |
| `Watch folder: not_found` | Import folder does not exist |
| `Watch folder: no_read_access` | Import folder not readable |
| `Export folder: not_found` | Export folder does not exist |
| `Export folder: no_write_access` | Export folder not writable |
| `Success folder: not_found` | Success folder does not exist |
| `Success folder: no_write_access` | Success folder not writable |

**Automatic Reactivation:** WatchDog checks folders regularly. As soon as the folder is reachable again, the configuration is automatically reactivated.

---

## 6. Error Folder (`_error`)

Failed files are moved to the `_error` folder:

**Location:** `{import_folder}/_error/`

**File Format:** `{original_name}_{YYYYMMDD_HHMMSS}.pdf`

**Sidecar File:** Each failed file has a `.error` companion file with:

```
Error Type: transformation_error
Error Message: XSLT template not found
Timestamp: 2024-02-10 08:30:15
Original File: invoice_001.pdf
Original Path: C:\WatchDog\Import\invoice_001.pdf
```

---

## 7. Heartbeat & Connection Status

WatchDog sends a heartbeat to DocBits regularly:

| Status | Meaning |
| :--- | :--- |
| ✅ `Connected` | WatchDog is connected and active |
| ⚠️ `Last seen: X minutes ago` | Connection interrupted |
| ❌ `Never connected` | WatchDog has never connected |

**Heartbeat Errors:**

*   `Heartbeat failed - invalid API key` → API Key is invalid
*   `Heartbeat failed: 401` → Authentication failed
*   `Heartbeat failed: 5xx` → Server problem

---

## 8. Common Problems & Solutions

### Problem: WatchDog does not import files

1.  Check if service is running: `services.msc` → WatchDog
2.  Check logs: Settings → WatchDog → Logs
3.  Check folder permissions
4.  Test API connection

### Problem: Export does not work

1.  Export configuration exists?
2.  Document type matches?
3.  XSLT Template linked?
4.  Export folder writable?

### Problem: Configuration is disabled

1.  Folder path exists?
2.  Permissions for `NT AUTHORITY\LOCAL SERVICE` or Service Account?
3.  Network drive reachable? (Check UNC paths)

### Problem: XSLT Transformation fails

1.  XSLT Template is valid?
2.  Template fits document type?
3.  Check XML structure of the document

---

## 9. Command Line Commands

```bash
# Install Service
WatchDog.exe install

# Start Service
WatchDog.exe start

# Stop Service
WatchDog.exe stop

# Uninstall Service
WatchDog.exe uninstall

# Check Service Status
sc query WatchDog
```

---

## 10. Log Files

**Location:** `C:\WatchDog\logs`

**Log Files:**

*   `watchdog.log` - Main log
*   `watchdog_error.log` - Errors only

**Log Level:** INFO, WARNING, ERROR
