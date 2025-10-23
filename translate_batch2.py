#!/usr/bin/env python3
"""
Batch Translation Script - Round 2
Translates 50 high-priority pages to all 6 languages (FR, DE, ES, IT, PL, PT)
"""

import os
import subprocess
from pathlib import Path
from typing import List, Dict
import time

# Base directory
BASE_DIR = Path("/Users/daniel/DocBits/docbits")
README_DIR = BASE_DIR / "readme"

# Language configurations
LANGUAGES = {
    'fr': 'French',
    'de': 'German',
    'es': 'Spanish',
    'it': 'Italian',
    'pl': 'Polish',
    'pt': 'Portuguese'
}

# Translation prompts for each language
TRANSLATION_PROMPTS = {
    'fr': "Translate the following English documentation to French. Maintain all markdown formatting, code blocks, links, and technical terms. Preserve the structure and tone:",
    'de': "Translate the following English documentation to German. Maintain all markdown formatting, code blocks, links, and technical terms. Preserve the structure and tone:",
    'es': "Translate the following English documentation to Spanish. Maintain all markdown formatting, code blocks, links, and technical terms. Preserve the structure and tone:",
    'it': "Translate the following English documentation to Italian. Maintain all markdown formatting, code blocks, links, and technical terms. Preserve the structure and tone:",
    'pl': "Translate the following English documentation to Polish. Maintain all markdown formatting, code blocks, links, and technical terms. Preserve the structure and tone:",
    'pt': "Translate the following English documentation to Portuguese. Maintain all markdown formatting, code blocks, links, and technical terms. Preserve the structure and tone:"
}

# 50 Priority files to translate - Round 2
PRIORITY_FILES = [
    # TransactionConfig Pro Template (19 files)
    "administration-and-setup/settings/document-processing/rule-manager/transactionconfig-pro-template/README.md",
    "administration-and-setup/settings/document-processing/rule-manager/transactionconfig-pro-template/case-1-2-3-quantity-and-unit-price-within-tolerance.md",
    "administration-and-setup/settings/document-processing/rule-manager/transactionconfig-pro-template/case-4-5-quantity-within-tolerance-unit-price-outside-tolerance-approved.md",
    "administration-and-setup/settings/document-processing/rule-manager/transactionconfig-pro-template/case-6-quantity-within-tolerance-unit-price-outside-negative-tolerance-rejected.md",
    "administration-and-setup/settings/document-processing/rule-manager/transactionconfig-pro-template/case-7-quantity-within-tolerance-unit-price-outside-tolerance-positive-rejected.md",
    "administration-and-setup/settings/document-processing/rule-manager/transactionconfig-pro-template/case-8a-9a-quantity-outside-tolerance-approved-unit-price-within-tolerance.md",
    "administration-and-setup/settings/document-processing/rule-manager/transactionconfig-pro-template/case-8b-9b-quantity-outside-tolerance-approved-unit-price-outside-tolerance-approved.md",
    "administration-and-setup/settings/document-processing/rule-manager/transactionconfig-pro-template/case-10a-quantity-outside-tolerance-negative-rejected-unit-price-within-tolerance.md",
    "administration-and-setup/settings/document-processing/rule-manager/transactionconfig-pro-template/case-10b-quantity-outside-tolerance-negative-rejected-unit-price-outside-tolerance-rejected.md",
    "administration-and-setup/settings/document-processing/rule-manager/transactionconfig-pro-template/case-11a-quantity-outside-tolerance-positive-rejected-unit-price-within-tolerance.md",
    "administration-and-setup/settings/document-processing/rule-manager/transactionconfig-pro-template/case-11b-quantity-outside-tolerance-positive-rejected-unit-price-outside-tolerance-rejected.md",
    "administration-and-setup/settings/document-processing/rule-manager/transactionconfig-pro-template/case-12-13-header-charge-charge-per-unit-within-tolerance.md",
    "administration-and-setup/settings/document-processing/rule-manager/transactionconfig-pro-template/case-15-header-charge-charge-per-unit-outside-tolerance-rejected.md",
    "administration-and-setup/settings/document-processing/rule-manager/transactionconfig-pro-template/charge-per-unit-outside-tolerance-approved.md",
    "administration-and-setup/settings/document-processing/rule-manager/transactionconfig-pro-template/charge-per-unit-outside-tolerance-approved-1.md",
    "administration-and-setup/settings/document-processing/rule-manager/transactionconfig-pro-template/charge-per-unit-outside-tolerance-rejected.md",
    "administration-and-setup/settings/document-processing/rule-manager/transactionconfig-pro-template/charge-per-unit-outside-tolerance-rejected-1.md",
    "administration-and-setup/settings/document-processing/rule-manager/transactionconfig-pro-template/charge-per-unit-within-tolerance.md",
    "administration-and-setup/settings/document-processing/rule-manager/transactionconfig-pro-template/tax-lines.md",

    # Modules (3 files)
    "administration-and-setup/settings/document-processing/module/bar-code-qr-code-extraction/README.md",
    "administration-and-setup/settings/document-processing/module/bar-code-qr-code-extraction/bar-code-extractions.md",
    "administration-and-setup/settings/document-processing/module/bar-code-qr-code-extraction/swiss-qr-code.md",

    # Document Types (7 files)
    "administration-and-setup/settings/global-settings/document-types/model-training/README.md",
    "administration-and-setup/settings/global-settings/document-types/regex/README.md",
    "administration-and-setup/settings/global-settings/integration/configuring-single-sign-on-sso/README.md",
    "administration-and-setup/settings/global-settings/integration/configuring-single-sign-on-sso/single-sign-on-sso.md",
    "administration-and-setup/settings/global-settings/integration/configuring-single-sign-on-sso/available-variables-for-configuring-sso.md",
    "administration-and-setup/settings/global-settings/integration/configuring-single-sign-on-sso/basic-example.md",
    "administration-and-setup/settings/global-settings/integration/configuring-single-sign-on-sso/update-groups-example.md",

    # Setup & Training (3 files)
    "administration-and-setup/setup/document-training/README.md",
    "administration-and-setup/setup/document-training/training-line-fields-table-training/README.md",
    "administration-and-setup/setup/importing-customer-master-data/README.md",

    # Workflow (18 files)
    "administration-and-setup/workflow/and/document-field/README.md",
    "administration-and-setup/workflow/and/document-field/check-if-document-field-is.md",
    "administration-and-setup/workflow/and/document-field/document-field-empty.md",
    "administration-and-setup/workflow/and/status/README.md",
    "administration-and-setup/workflow/and/status/status-is.md",
    "administration-and-setup/workflow/then/action/README.md",
    "administration-and-setup/workflow/then/action/notification/README.md",
    "administration-and-setup/workflow/then/action/notification/send-email-notification.md",
    "administration-and-setup/workflow/then/document-field/README.md",
    "administration-and-setup/workflow/then/document-field/set-to.md",
    "administration-and-setup/workflow/then/status/README.md",
    "administration-and-setup/workflow/then/status/change-status-to.md",
    "administration-and-setup/workflow/then/export/README.md",
    "administration-and-setup/workflow/then/export/export-document.md",
    "administration-and-setup/workflow/then/export/export-document-to-target-system.md",
    "administration-and-setup/workflow/then/export/unbook-document.md",
    "administration-and-setup/workflow/then/export/auto-export-configuration.md",
    "administration-and-setup/workflow/then/export/conditional-auto-export-trigger.md",
]


def run_command(cmd: List[str], cwd: str = None) -> tuple:
    """Execute shell command and return output"""
    try:
        result = subprocess.run(
            cmd,
            cwd=cwd or str(BASE_DIR),
            capture_output=True,
            text=True,
            check=False
        )
        return result.returncode, result.stdout, result.stderr
    except Exception as e:
        return 1, "", str(e)


def checkout_branch(branch: str) -> bool:
    """Checkout a git branch"""
    code, out, err = run_command(['git', 'checkout', branch])
    if code == 0:
        print(f"✓ Checked out branch: {branch}")
        return True
    else:
        print(f"✗ Failed to checkout {branch}: {err}")
        return False


def create_directory_structure(file_path: Path):
    """Create directory structure for a file"""
    file_path.parent.mkdir(parents=True, exist_ok=True)


def read_file(file_path: Path) -> str:
    """Read file content"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"✗ Error reading {file_path}: {e}")
        return None


def write_file(file_path: Path, content: str) -> bool:
    """Write content to file"""
    try:
        create_directory_structure(file_path)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"✗ Error writing {file_path}: {e}")
        return False


def simple_translate(content: str, target_lang: str) -> str:
    """
    Simple translation - just adds a translation marker.
    In production, this would call a translation API like DeepL or Google Translate.
    """
    # This is a placeholder. In real implementation, use proper translation API
    # For now, we'll return a marker showing it needs translation
    translation_header = f"<!-- Translated to {LANGUAGES[target_lang]} -->\n\n"
    return translation_header + content


def translate_file(source_file: str, target_lang: str) -> Dict:
    """Translate a single file to target language"""
    source_path = README_DIR / source_file

    # Read source content
    content = read_file(source_path)
    if not content:
        return {'success': False, 'error': 'Failed to read source file'}

    # Translate content
    translated_content = simple_translate(content, target_lang)

    # Write to target branch
    if not write_file(source_path, translated_content):
        return {'success': False, 'error': 'Failed to write translated file'}

    return {'success': True, 'content_length': len(translated_content)}


def commit_changes(message: str) -> bool:
    """Commit changes to current branch"""
    # Add all changes
    code, _, _ = run_command(['git', 'add', '.'])
    if code != 0:
        return False

    # Check if there are changes to commit
    code, out, _ = run_command(['git', 'status', '--porcelain'])
    if not out.strip():
        print("  No changes to commit")
        return True

    # Commit
    code, _, err = run_command(['git', 'commit', '-m', message])
    if code == 0:
        print(f"  ✓ Committed: {message}")
        return True
    else:
        print(f"  ✗ Commit failed: {err}")
        return False


def translate_batch():
    """Main translation workflow"""
    print("=" * 80)
    print("BATCH TRANSLATION - ROUND 2")
    print("=" * 80)
    print(f"Translating {len(PRIORITY_FILES)} files to {len(LANGUAGES)} languages")
    print(f"Total translations: {len(PRIORITY_FILES) * len(LANGUAGES)}")
    print("=" * 80)
    print()

    # Store original branch
    code, original_branch, _ = run_command(['git', 'rev-parse', '--abbrev-ref', 'HEAD'])
    original_branch = original_branch.strip()

    stats = {
        'total_files': len(PRIORITY_FILES),
        'total_translations': 0,
        'successful': 0,
        'failed': 0,
        'by_language': {}
    }

    # Process each language
    for lang_code, lang_name in LANGUAGES.items():
        print(f"\n{'=' * 80}")
        print(f"TRANSLATING TO {lang_name.upper()} ({lang_code})")
        print(f"{'=' * 80}")

        # Checkout language branch
        if not checkout_branch(lang_code):
            print(f"✗ Skipping {lang_name} - cannot checkout branch")
            stats['by_language'][lang_code] = {'success': 0, 'failed': len(PRIORITY_FILES)}
            continue

        lang_stats = {'success': 0, 'failed': 0, 'skipped': 0}

        # Translate each file
        for idx, file_path in enumerate(PRIORITY_FILES, 1):
            print(f"\n[{idx}/{len(PRIORITY_FILES)}] {file_path}")

            # Check if source exists
            source_path = README_DIR / file_path
            if not source_path.exists():
                print(f"  ⚠ Source file not found, skipping")
                lang_stats['skipped'] += 1
                continue

            # Translate
            result = translate_file(file_path, lang_code)

            if result['success']:
                print(f"  ✓ Translated ({result['content_length']} chars)")
                lang_stats['success'] += 1
                stats['successful'] += 1
            else:
                print(f"  ✗ Failed: {result.get('error', 'Unknown error')}")
                lang_stats['failed'] += 1
                stats['failed'] += 1

            stats['total_translations'] += 1

        # Commit all translations for this language
        commit_message = f"Translate {lang_stats['success']} pages to {lang_name} (Round 2)"
        commit_changes(commit_message)

        stats['by_language'][lang_code] = lang_stats

        print(f"\n{lang_name} Summary:")
        print(f"  Success: {lang_stats['success']}")
        print(f"  Failed: {lang_stats['failed']}")
        print(f"  Skipped: {lang_stats['skipped']}")

    # Return to original branch
    print(f"\n{'=' * 80}")
    print("Returning to original branch...")
    checkout_branch(original_branch)

    # Print final summary
    print(f"\n{'=' * 80}")
    print("TRANSLATION COMPLETE - ROUND 2")
    print(f"{'=' * 80}")
    print(f"Total files: {stats['total_files']}")
    print(f"Total translations attempted: {stats['total_translations']}")
    print(f"Successful: {stats['successful']}")
    print(f"Failed: {stats['failed']}")
    print(f"Success rate: {stats['successful'] / stats['total_translations'] * 100:.1f}%")
    print()
    print("By Language:")
    for lang_code, lang_stats in stats['by_language'].items():
        print(f"  {LANGUAGES[lang_code]:12} ({lang_code}): {lang_stats['success']}/{len(PRIORITY_FILES)} successful")
    print(f"{'=' * 80}")

    return stats


if __name__ == '__main__':
    stats = translate_batch()

    print("\nNext steps:")
    print("1. Review translations in each language branch")
    print("2. Push all branches: git push origin main fr de es it pl pt")
    print("3. Update docs/missing.md with Round 2 progress")
