# Decision Trees

### Overview

Decision Trees are a powerful feature that allows for the automated routing and decision-making process based on predefined rules. This feature is especially useful in complex environments where various conditions need to be evaluated to determine the correct course of action, such as assigning prices, determining quantities, or routing documents.

#### Key Components

* **Decision Tree List**: This is the main interface where all existing decision trees are listed. Each decision tree can be associated with a specific document type such as an `INVOICE` or `QUOTE`.
* **Decision Tree Editor**: This interface allows for the creation and editing of decision trees, where you can define rules, operators, and actions to be taken when certain conditions are met.

### Decision Tree Interface

#### Decision Tree List

The Decision Tree list displays all the available decision trees. Each entry shows:

* **Name**: The name of the decision tree.
* **Document Type**: The type of document associated with the decision tree (e.g., `INVOICE`, `QUOTE`).

#### Decision Tree Editor

The Decision Tree Editor allows you to configure rules that govern how decisions are made.

**Components of the Decision Tree Editor**

* **Rules**: Each rule consists of conditions and actions.
* **Select Source**: This dropdown allows you to specify the source field to evaluate.
* **Select Operator**: Defines the logic operator (e.g., `<=`, `>=`, `=`, `!=`) to be applied to the source field.
* **Result**: Defines the outcome or action that should be taken when the conditions are met.
* **Add New Row**: Allows you to add additional rules to the decision tree.

#### Example of a Decision Tree Configuration

1. **Rule 1**:
   * **Source**: Quantity
   * **Operator**: `<=`
   * **Value**: `250000`
   * **Result**: Assign to `CATMGR_CMM`
2. **Rule 2**:
   * **Source**: Price
   * **Operator**: `>`
   * **Value**: `500000`
   * **Result**: Assign to `PROCUREMENT_DIRECTOR`

Each rule is evaluated sequentially, and the corresponding action is executed if the conditions are satisfied.

### Decision Tree Policy

The Decision Tree Policy defines how multiple rules within a decision tree are processed. You can choose from several policies:

* **Unique**: Ensures that only one rule can match. If more than one rule is matched, the decision tree will flag an error.
* **First**: The first matching rule is applied, and no further rules are evaluated.
* **Priority**: Rules are evaluated based on their priority order. The highest priority matching rule is applied.
* **Collect (sum)**: Collects all matching rules and sums the results.
* **Collect (min/max/count)**: Collects all matching rules and either selects the minimum, maximum, or counts the occurrences.
* **Rule Order**: Applies rules in the order they appear in the decision tree.
* **Any**: Any matching rule can be applied, allowing for multiple outcomes.

#### Example of a Decision Tree Policy in Action

In the "Direct Group Price" decision tree:

* **Policy Selected**: `First`
* This means that as soon as a rule's condition is met, its associated action is applied, and no further rules are evaluated.

### Export and Save

* **Save**: Saves the current configuration of the decision tree.
* **Export**: Allows you to export the decision tree configuration, which can then be imported into another environment or used for backup purposes.
