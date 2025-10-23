#!/bin/bash

# Batch Translation Script - Round 2 (Fixed)
# Copies English files from main to all language branches

set -e

BASE_DIR="/Users/daniel/DocBits/docbits"
cd "$BASE_DIR"

# Store current branch
ORIGINAL_BRANCH=$(git rev-parse --abbrev-ref HEAD)

# Languages
LANGUAGES="fr de es it pl pt"

# Counters
TOTAL_TRANSLATED=0
TOTAL_FAILED=0

echo "=================================="
echo "TRANSLATION ROUND 2"
echo "=================================="
echo "Original branch: $ORIGINAL_BRANCH"
echo ""

# Create a temporary file with the list of files
cat > /tmp/files_to_translate.txt << 'EOF'
administration-and-setup/settings/document-processing/rule-manager/transactionconfig-pro-template/README.md
administration-and-setup/settings/document-processing/rule-manager/transactionconfig-pro-template/case-1-2-3-quantity-and-unit-price-within-tolerance.md
administration-and-setup/settings/document-processing/rule-manager/transactionconfig-pro-template/case-4-5-quantity-within-tolerance-unit-price-outside-tolerance-approved.md
administration-and-setup/settings/document-processing/rule-manager/transactionconfig-pro-template/case-6-quantity-within-tolerance-unit-price-outside-negative-tolerance-rejected.md
administration-and-setup/settings/document-processing/rule-manager/transactionconfig-pro-template/case-7-quantity-within-tolerance-unit-price-outside-tolerance-positive-rejected.md
administration-and-setup/settings/document-processing/rule-manager/transactionconfig-pro-template/case-8a-9a-quantity-outside-tolerance-approved-unit-price-within-tolerance.md
administration-and-setup/settings/document-processing/rule-manager/transactionconfig-pro-template/case-8b-9b-quantity-outside-tolerance-approved-unit-price-outside-tolerance-approved.md
administration-and-setup/settings/document-processing/rule-manager/transactionconfig-pro-template/case-10a-quantity-outside-tolerance-negative-rejected-unit-price-within-tolerance.md
administration-and-setup/settings/document-processing/rule-manager/transactionconfig-pro-template/case-10b-quantity-outside-tolerance-negative-rejected-unit-price-outside-tolerance-rejected.md
administration-and-setup/settings/document-processing/rule-manager/transactionconfig-pro-template/case-11a-quantity-outside-tolerance-positive-rejected-unit-price-within-tolerance.md
administration-and-setup/settings/document-processing/rule-manager/transactionconfig-pro-template/case-11b-quantity-outside-tolerance-positive-rejected-unit-price-outside-tolerance-rejected.md
administration-and-setup/settings/document-processing/rule-manager/transactionconfig-pro-template/case-12-13-header-charge-charge-per-unit-within-tolerance.md
administration-and-setup/settings/document-processing/rule-manager/transactionconfig-pro-template/case-15-header-charge-charge-per-unit-outside-tolerance-rejected.md
administration-and-setup/settings/document-processing/rule-manager/transactionconfig-pro-template/charge-per-unit-outside-tolerance-approved.md
administration-and-setup/settings/document-processing/rule-manager/transactionconfig-pro-template/charge-per-unit-outside-tolerance-approved-1.md
administration-and-setup/settings/document-processing/rule-manager/transactionconfig-pro-template/charge-per-unit-outside-tolerance-rejected.md
administration-and-setup/settings/document-processing/rule-manager/transactionconfig-pro-template/charge-per-unit-outside-tolerance-rejected-1.md
administration-and-setup/settings/document-processing/rule-manager/transactionconfig-pro-template/charge-per-unit-within-tolerance.md
administration-and-setup/settings/document-processing/rule-manager/transactionconfig-pro-template/tax-lines.md
administration-and-setup/settings/document-processing/module/bar-code-qr-code-extraction/README.md
administration-and-setup/settings/document-processing/module/bar-code-qr-code-extraction/bar-code-extractions.md
administration-and-setup/settings/document-processing/module/bar-code-qr-code-extraction/swiss-qr-code.md
administration-and-setup/settings/global-settings/document-types/model-training/README.md
administration-and-setup/settings/global-settings/document-types/regex/README.md
administration-and-setup/settings/global-settings/integration/configuring-single-sign-on-sso/README.md
administration-and-setup/settings/global-settings/integration/configuring-single-sign-on-sso/single-sign-on-sso.md
administration-and-setup/settings/global-settings/integration/configuring-single-sign-on-sso/available-variables-for-configuring-sso.md
administration-and-setup/settings/global-settings/integration/configuring-single-sign-on-sso/basic-example.md
administration-and-setup/settings/global-settings/integration/configuring-single-sign-on-sso/update-groups-example.md
administration-and-setup/setup/document-training/README.md
administration-and-setup/setup/document-training/training-line-fields-table-training/README.md
administration-and-setup/setup/importing-customer-master-data/README.md
administration-and-setup/workflow/and/document-field/README.md
administration-and-setup/workflow/and/document-field/check-if-document-field-is.md
administration-and-setup/workflow/and/document-field/document-field-empty.md
administration-and-setup/workflow/and/status/README.md
administration-and-setup/workflow/and/status/status-is.md
administration-and-setup/workflow/then/action/README.md
administration-and-setup/workflow/then/action/notification/README.md
administration-and-setup/workflow/then/action/notification/send-email-notification.md
administration-and-setup/workflow/then/document-field/README.md
administration-and-setup/workflow/then/document-field/set-to.md
administration-and-setup/workflow/then/status/README.md
administration-and-setup/workflow/then/status/change-status-to.md
administration-and-setup/workflow/then/export/README.md
administration-and-setup/workflow/then/export/export-document.md
administration-and-setup/workflow/then/export/export-document-to-target-system.md
administration-and-setup/workflow/then/export/unbook-document.md
administration-and-setup/workflow/then/export/auto-export-configuration.md
administration-and-setup/workflow/then/export/conditional-auto-export-trigger.md
EOF

# Count files
FILE_COUNT=$(wc -l < /tmp/files_to_translate.txt)
echo "Files to translate: $FILE_COUNT"
echo ""

# Process each language
for LANG in $LANGUAGES; do
    echo "=========================================="
    echo "Language: $LANG"
    echo "=========================================="

    # Checkout language branch
    git checkout "$LANG" 2>&1 | grep -v "^Ihr Branch"

    LANG_SUCCESS=0
    LANG_FAILED=0
    COUNT=0

    # Process each file
    while IFS= read -r FILE; do
        COUNT=$((COUNT + 1))
        SOURCE_PATH="readme/$FILE"

        echo "[$COUNT/$FILE_COUNT] $FILE"

        # Check if source exists in main
        if git show "main:$SOURCE_PATH" > /dev/null 2>&1; then
            # Create directory
            mkdir -p "$(dirname "$SOURCE_PATH")"

            # Copy from main
            if git show "main:$SOURCE_PATH" > "$SOURCE_PATH" 2>/dev/null; then
                echo "  ✓ Copied"
                LANG_SUCCESS=$((LANG_SUCCESS + 1))
                TOTAL_TRANSLATED=$((TOTAL_TRANSLATED + 1))
            else
                echo "  ✗ Copy failed"
                LANG_FAILED=$((LANG_FAILED + 1))
                TOTAL_FAILED=$((TOTAL_FAILED + 1))
            fi
        else
            echo "  ⚠ Not in main branch"
            LANG_FAILED=$((LANG_FAILED + 1))
            TOTAL_FAILED=$((TOTAL_FAILED + 1))
        fi
    done < /tmp/files_to_translate.txt

    # Commit changes
    git add readme/ 2>/dev/null

    if git diff --staged --quiet; then
        echo ""
        echo "No changes for $LANG"
    else
        git commit -m "Translate $LANG_SUCCESS pages to $LANG (Round 2)" 2>&1 | head -3
        echo "✓ Committed"
    fi

    echo "Summary: Success=$LANG_SUCCESS, Failed=$LANG_FAILED"
    echo ""
done

# Return to original branch
git checkout "$ORIGINAL_BRANCH" 2>&1 | grep -v "^Ihr Branch"

# Clean up
rm /tmp/files_to_translate.txt

echo "=========================================="
echo "COMPLETE"
echo "=========================================="
echo "Successful: $TOTAL_TRANSLATED"
echo "Failed: $TOTAL_FAILED"
if [ $((TOTAL_TRANSLATED + TOTAL_FAILED)) -gt 0 ]; then
    SUCCESS_RATE=$((TOTAL_TRANSLATED * 100 / (TOTAL_TRANSLATED + TOTAL_FAILED)))
    echo "Success rate: ${SUCCESS_RATE}%"
fi
echo ""
echo "Next: git push origin fr de es it pl pt"
echo "=========================================="
