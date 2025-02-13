# Table Extraction Troubleshoot

## **Step 1: Open OCR View for Bad Extraction Results**

If the table extraction training results are not good:

1. Open the **OCR View** by clicking on the magnifying glass icon with **OCR** written on it.
2. Review the extraction results and see if the OCR process can improve the data capture.
3. If the results still look bad, try a different document to verify if the issue is document-specific.
4. If the issue is document-specific, use another document for extraction.
   * If the issue persists, follow the next steps.

## **Step 2: Check for E-Text Availability**

1. Check if the document has **e-text** available.
   * You can verify this using a tool like **Adobe Acrobat**.
   * If the document contains e-text, follow **Step 3.**
   * If the document does not contain e-text, follow **Step 4.**

## **Step 3: Turn On E-Text Extraction**

If the document contains e-text, you have two options:

1. **Turn on e-text extraction for just this supplier**:
   * Go back to the **Documents Field Validation**.
   * Click the square with the three dots in the left-side toolbar.
   * Here, activate the **Use E-text if available** option to turn it on for just this supplier.
2. **Turn on e-text extraction for all suppliers**:
   * Go to **Settings** > **Document Processing** > **OCR Settings**.
   * In this section, you will find the **Use E-text if available** option and can turn it on for all suppliers.
3. After enabling e-text extraction, retry the **table extraction training**.
   * If the results improve, the issue is resolved.
   * If the results are still not good, proceed to **Step 4**.

## **Step 4: No E-Text Available - Change AI OCR Version**

If the document does not have e-text available:

1. Go to **Settings** > **Document Processing** > **OCR Settings**.
2. Change the **AI OCR Version** to a different version.
3. Go back to the **Table Extraction Training** and try again.
4. If the result is better:
   * Check other documents from different suppliers to ensure the extraction results for those suppliers are not impacted by this change.
   * **Be cautious, as this change can affect other suppliers' extraction results.**
   * This change can impact other suppliers, so make sure to verify the results thoroughly to ensure it does not negatively affect other suppliers’ document extractions.
5. If the result did not improve after changing the AI OCR version, please **contact us** for further assistance.
