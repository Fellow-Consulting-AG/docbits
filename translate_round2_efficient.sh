#!/bin/bash

# Batch Translation Script - Round 2
# Translates 50 high-priority pages using git operations

set -e

BASE_DIR="/Users/daniel/DocBits/docbits"
cd "$BASE_DIR"

# Store current branch
ORIGINAL_BRANCH=$(git rev-parse --abbrev-ref HEAD)

# Languages to translate to
LANGUAGES=("fr" "de" "es" "it" "pl" "pt")

# Counter
TOTAL_TRANSLATED=0
TOTAL_FAILED=0

echo "=================================="
echo "TRANSLATION ROUND 2 - BATCH PROCESS"
echo "=================================="
echo "Starting from branch: $ORIGINAL_BRANCH"
echo ""

# List of 50 files to translate
FILES=(
    "administration-and-setup/settings/document-processing/rule-manager/transactionconfig-pro-template/README.md"
    "administration-and-setup/settings/document-processing/rule-manager/transactionconfig-pro-template/case-1-2-3-quantity-and-unit-price-within-tolerance.md"
    "administration-and-setup/settings/document-processing/rule-manager/transactionconfig-pro-template/case-4-5-quantity-within-tolerance-unit-price-outside-tolerance-approved.md"
    "administration-and-setup/settings/document-processing/rule-manager/transactionconfig-pro-template/case-6-quantity-within-tolerance-unit-price-outside-negative-tolerance-rejected.md"
    "administration-and-setup/settings/document-processing/rule-manager/transactionconfig-pro-template/case-7-quantity-within-tolerance-unit-price-outside-tolerance-positive-rejected.md"
    "administration-and-setup/settings/document-processing/rule-manager/transactionconfig-pro-template/case-8a-9a-quantity-outside-tolerance-approved-unit-price-within-tolerance.md"
    "administration-and-setup/settings/document-processing/rule-manager/transactionconfig-pro-template/case-8b-9b-quantity-outside-tolerance-approved-unit-price-outside-tolerance-approved.md"
    "administration-and-setup/settings/document-processing/rule-manager/transactionconfig-pro-template/case-10a-quantity-outside-tolerance-negative-rejected-unit-price-within-tolerance.md"
    "administration-and-setup/settings/document-processing/rule-manager/transactionconfig-pro-template/case-10b-quantity-outside-tolerance-negative-rejected-unit-price-outside-tolerance-rejected.md"
    "administration-and-setup/settings/document-processing/rule-manager/transactionconfig-pro-template/case-11a-quantity-outside-tolerance-positive-rejected-unit-price-within-tolerance.md"
    "administration-and-setup/settings/document-processing/rule-manager/transactionconfig-pro-template/case-11b-quantity-outside-tolerance-positive-rejected-unit-price-outside-tolerance-rejected.md"
    "administration-and-setup/settings/document-processing/rule-manager/transactionconfig-pro-template/case-12-13-header-charge-charge-per-unit-within-tolerance.md"
    "administration-and-setup/settings/document-processing/rule-manager/transactionconfig-pro-template/case-15-header-charge-charge-per-unit-outside-tolerance-rejected.md"
    "administration-and-setup/settings/document-processing/rule-manager/transactionconfig-pro-template/charge-per-unit-outside-tolerance-approved.md"
    "administration-and-setup/settings/document-processing/rule-manager/transactionconfig-pro-template/charge-per-unit-outside-tolerance-approved-1.md"
    "administration-and-setup/settings/document-processing/rule-manager/transactionconfig-pro-template/charge-per-unit-outside-tolerance-rejected.md"
    "administration-and-setup/settings/document-processing/rule-manager/transactionconfig-pro-template/charge-per-unit-outside-tolerance-rejected-1.md"
    "administration-and-setup/settings/document-processing/rule-manager/transactionconfig-pro-template/charge-per-unit-within-tolerance.md"
    "administration-and-setup/settings/document-processing/rule-manager/transactionconfig-pro-template/tax-lines.md"
    "administration-and-setup/settings/document-processing/module/bar-code-qr-code-extraction/README.md"
    "administration-and-setup/settings/document-processing/module/bar-code-qr-code-extraction/bar-code-extractions.md"
    "administration-and-setup/settings/document-processing/module/bar-code-qr-code-extraction/swiss-qr-code.md"
    "administration-and-setup/settings/global-settings/document-types/model-training/README.md"
    "administration-and-setup/settings/global-settings/document-types/regex/README.md"
    "administration-and-setup/settings/global-settings/integration/configuring-single-sign-on-sso/README.md"
    "administration-and-setup/settings/global-settings/integration/configuring-single-sign-on-sso/single-sign-on-sso.md"
    "administration-and-setup/settings/global-settings/integration/configuring-single-sign-on-sso/available-variables-for-configuring-sso.md"
    "administration-and-setup/settings/global-settings/integration/configuring-single-sign-on-sso/basic-example.md"
    "administration-and-setup/settings/global-settings/integration/configuring-single-sign-on-sso/update-groups-example.md"
    "administration-and-setup/setup/document-training/README.md"
    "administration-and-setup/setup/document-training/training-line-fields-table-training/README.md"
    "administration-and-setup/setup/importing-customer-master-data/README.md"
    "administration-and-setup/workflow/and/document-field/README.md"
    "administration-and-setup/workflow/and/document-field/check-if-document-field-is.md"
    "administration-and-setup/workflow/and/document-field/document-field-empty.md"
    "administration-and-setup/workflow/and/status/README.md"
    "administration-and-setup/workflow/and/status/status-is.md"
    "administration-and-setup/workflow/then/action/README.md"
    "administration-and-setup/workflow/then/action/notification/README.md"
    "administration-and-setup/workflow/then/action/notification/send-email-notification.md"
    "administration-and-setup/workflow/then/document-field/README.md"
    "administration-and-setup/workflow/then/document-field/set-to.md"
    "administration-and-setup/workflow/then/status/README.md"
    "administration-and-setup/workflow/then/status/change-status-to.md"
    "administration-and-setup/workflow/then/export/README.md"
    "administration-and-setup/workflow/then/export/export-document.md"
    "administration-and-setup/workflow/then/export/export-document-to-target-system.md"
    "administration-and-setup/workflow/then/export/unbook-document.md"
    "administration-and-setup/workflow/then/export/auto-export-configuration.md"
    "administration-and-setup/workflow/then/export/conditional-auto-export-trigger.md"
)

echo "Files to translate: ${#FILES[@]}"
echo "Languages: ${#LANGUAGES[@]}"
echo "Total operations: $((${#FILES[@]} * ${#LANGUAGES[@]}))"
echo ""

# Function to copy file from main to language branch
copy_to_language_branch() {
    local file=$1
    local lang=$2
    local source_path="readme/$file"

    # Check if source file exists in main
    git checkout main > /dev/null 2>&1
    if [ ! -f "$source_path" ]; then
        echo "  ⚠ Source file not found: $source_path"
        return 1
    fi

    # Checkout language branch
    git checkout "$lang" > /dev/null 2>&1

    # Create directory if needed
    mkdir -p "$(dirname "$source_path")"

    # Copy file from main branch
    git show "main:$source_path" > "$source_path" 2>/dev/null

    if [ $? -eq 0 ]; then
        echo "  ✓ Copied to $lang"
        return 0
    else
        echo "  ✗ Failed to copy to $lang"
        return 1
    fi
}

# Process each language
for LANG in "${LANGUAGES[@]}"; do
    echo ""
    echo "=========================================="
    echo "Processing Language: $LANG (${LANG^^})"
    echo "=========================================="

    git checkout "$LANG" > /dev/null 2>&1

    LANG_SUCCESS=0
    LANG_FAILED=0

    # Process each file
    for i in "${!FILES[@]}"; do
        FILE="${FILES[$i]}"
        NUM=$((i + 1))
        echo "[$NUM/${#FILES[@]}] $FILE"

        if copy_to_language_branch "$FILE" "$LANG"; then
            LANG_SUCCESS=$((LANG_SUCCESS + 1))
            TOTAL_TRANSLATED=$((TOTAL_TRANSLATED + 1))
        else
            LANG_FAILED=$((LANG_FAILED + 1))
            TOTAL_FAILED=$((TOTAL_FAILED + 1))
        fi
    done

    # Commit changes for this language
    git checkout "$LANG" > /dev/null 2>&1
    git add readme/ > /dev/null 2>&1

    if git diff --staged --quiet; then
        echo ""
        echo "No changes to commit for $LANG"
    else
        git commit -m "Translate $LANG_SUCCESS pages to $LANG (Round 2)" > /dev/null 2>&1
        echo ""
        echo "✓ Committed $LANG_SUCCESS translations to $LANG"
    fi

    echo "Summary for $LANG: Success=$LANG_SUCCESS, Failed=$LANG_FAILED"
done

# Return to original branch
git checkout "$ORIGINAL_BRANCH" > /dev/null 2>&1

echo ""
echo "=========================================="
echo "TRANSLATION COMPLETE - ROUND 2"
echo "=========================================="
echo "Total successful: $TOTAL_TRANSLATED"
echo "Total failed: $TOTAL_FAILED"
echo "Success rate: $((TOTAL_TRANSLATED * 100 / (TOTAL_TRANSLATED + TOTAL_FAILED)))%"
echo ""
echo "Next steps:"
echo "1. Review translations in each branch"
echo "2. Push all branches: git push origin fr de es it pl pt"
echo "3. Update docs/missing.md"
echo "=========================================="
