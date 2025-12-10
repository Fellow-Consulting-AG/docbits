# Purchase Order Matching Rules

## Introduction: Purchase Orders and PO Rule Management

Purchase Order (PO) Matching is a critical process for ensuring consistency between Purchase Orders (POs) and corresponding incoming invoices or goods receipts. A robust set of rules is essential to achieve a high rate of automatic matching, prevent fraud, and ensure correct payments.

This configuration page is used to define and manage the rules that determine _how_ PO line items are matched to the corresponding incoming document (Invoice, Order Confirmation)

***

## How to Access

1.  Navigate to **Settings --> Global Settings --> Document Types**

    <figure><img src="../../../../../../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>


2.  Select the desired document type and click on **More Settings**.

    <figure><img src="../../../../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>


3.  Then go to the Section Purchase Order and Click the Button (PO match server side) after that you Click on Configure PO Matching Rules

    <figure><img src="../../../../../../.gitbook/assets/image (168).png" alt=""><figcaption></figcaption></figure>

***

<figure><img src="../../../../../../.gitbook/assets/Bildschirmfoto 2025-12-09 um 07.43.15.png" alt=""><figcaption></figcaption></figure>

## Global Settings (Base Rules)

These settings establish the framework that applies to all matching rules:

* **Setting:** Match Quantity On
  * **Purpose:** Defines which specific quantity field should be primarily used as the reference point for matching purchase order line items across all rules.
  * **Valid Values:** Quantity or other available quantity fields in the system, depending on the data structure (e.g., an alternative normalized quantity field).
  * **Dependency:** Determines the basis for all matching rules that include quantity in their comparison criteria.
* **Setting:** Standard Tolerance (Default Tolerance)
  * **Purpose:** Defines the permissible percentage deviation in quantity for a match to be considered valid. It compensates for minor rounding or quantity differences.
  * **Valid Value:** A decimal number (e.g., 0.005 corresponds to 0.5%).
  * **Dependency:** Applies to rules that use quantity fields for matching and have the "Allow Tolerance" option enabled.

***

## Rule List

The Rule List displays all available matching rules and manages their execution order.

#### Structure and Execution

* **Priority:** This numerical field (e.g., 1, 2, 3) dictates the execution sequence of the rules. Rules with a lower priority number are attempted first. This allows administrators to structure a hierarchy, typically starting with the most specific and stringent rules (e.g., matching by both line number and part number) and falling back to broader or less restrictive rules.
* **Name & Description:** Provides clear identification and context for the rule, explaining the primary criteria used (e.g., "Standard Rule No. 1: Match based on Line Number, Part ID, and Quantity").
* **Active:** A simple toggle switch that allows instant activation or deactivation of the rule without needing to delete its configuration.

**Execution Flow:** The system performs matching in a cascading sequence. If a rule (e.g., Priority 1) successfully matches a line item, the process for that item stops. If no match is found, the system proceeds to the next rule in the priority sequence (e.g., Priority 2).

***

## Rule Configuration (Detail Settings)

This detailed configuration area defines the specific logic and criteria for an individual rule.

#### Base Parameters

* **Rule Type (e.g., Single Match):** Specifies the matching cardinality. Single Match is the common type, requiring a one-to-one match (one PO line to one Invoice line). Other types might include many-to-one or one-to-many matches for aggregated items or split deliveries.
* **Automatic Match:** If enabled, the system will attempt to apply this rule entirely automatically. High confidence in the criteria is required for automatic processing.
* **Manual Match:** If enabled, this rule can be presented or applied by a user during the manual reconciliation step, offering them a pre-defined set of comparison criteria to resolve exceptions.

#### Column Comparison (Matching Criteria)

This is the core definition of the rule's logic, specifying which fields must align between the documents.

1. Defining the Columns to Compare:
   * **PO Columns:** The field drawn from the Purchase Order data (e.g., line number).
   * **Extracted Table Columns:** The corresponding field extracted or parsed from the incoming document (Invoice/Order Confirmation) (e.g., `POSITION`).
2. **Comparison Type:** Defines the nature of the required match (e.g., Tt for Text/String comparison, requiring an exact character-for-character match; # for Numerical comparison).
3. **Allow Tolerance:** For numerical fields (quantity, price), activating this option instructs the system to apply the Global Standard Tolerance defined earlier. If this is _not_ enabled for a numerical field, the values must match exactly.
4. **Ignore in Manual Match:** If checked, this criterion is relaxed during manual intervention. This is useful for fields like descriptions or internal references that may vary slightly, allowing the user to override minor non-critical mismatches.

**Example: Stringent PO-Match Rule (`DefaultRule#1`)**

A typical stringent rule combines mandatory identity checks with value checks:

* **Mandatory Identity:** Line Number and Item Identifier must match exactly (Text comparison, no tolerance).
* **Value Checks:** Effective Normalized Quantity and Effective Normalized Unit Price must match (Numerical comparison, Tolerance Allowed). Only if all four criteria are met (with tolerance for values) is an automatic match executed.

***

## Impact on the PO Matching Process

The defined rule set directly governs the efficiency and integrity of the PO-matching workflow:

* **Prioritization and Fallbacks:** The defined Priority ensures that the system first attempts the most reliable matching method. If the stringent, high-priority rules fail, the system falls back to broader rules, aiming to minimize the number of exceptions routed to users.
* **Controlling Match Quality:** Stricter rules (requiring more exact matches and less tolerance) result in fewer, but highly reliable, automatic matches. Looser rules increase the automatic match rate but raise the risk of false positives.
* **Exception Handling (Manual Match):** By enabling rules for Manual Match, the system provides structured options for users. If a transaction fails the automatic matching criteria, it becomes an exception. The user can then attempt to resolve the exception by applying a predefined manual rule, which might have relaxed criteria (e.g., ignoring a minor text mismatch as per the "Ignore in Manual Match" setting).

***

## Customize the PO Matching Rules

In order to edit the PO Matching rules, the default version can be cloned by clicking **"Configure Versioning"** and using **"Clone as Draft"** option from the available card options

<figure><img src="../../../../../../.gitbook/assets/image (197).png" alt=""><figcaption></figcaption></figure>



