# Missing Translations Report

**Generated:** 2025-10-23

## Summary

Total documentation pages in main (English) branch: **722**

### Translation Coverage by Language

| Language | Translated | Missing | Coverage |
|----------|-----------|---------|----------|
| French (FR) | 319 | 403 | 44.2% |
| German (DE) | 323 | 399 | 44.7% |
| Spanish (ES) | 319 | 403 | 44.2% |
| Italian (IT) | 319 | 403 | 44.2% |
| Polish (PL) | 319 | 403 | 44.2% |
| Portuguese (PT) | 319 | 403 | 44.2% |

---

## Key Findings

1. **Consistent Translation Gap**: All languages have nearly identical translation coverage (~44%), suggesting uniform translation progress across all language branches.

2. **583 pages are missing from all translated versions** - these represent the core translation work needed.

3. **Only 139 pages are fully translated** across all language versions.

---

## Missing Pages by Category

### Administration & Setup (Highest Priority)

The `administration-and-setup` directory has the most missing translations. Key missing sections include:

- **Document Processing Settings** - 50+ missing pages covering:
  - Decision trees configuration
  - Document expiry policies
  - Export settings
  - List of values management
  - Master data lookup
  - OCR settings
  - Classification and extraction rules

- **Rule Manager** - Extensive missing pages for Transaction Config Pro template (15+ case definitions)

- **Settings & Configuration** - API licenses, cache management, database access

### Workflow & Process (High Priority)

- Workflow configuration pages
- Conditional logic (AND/OR operations)
- Action handlers (THEN operations)

### User Management & Permissions

- Sub-organizations configuration
- User management procedures
- Group permissions setup

### Document Integration

- Email import testing
- FTP import testing
- Multi-email handling

---

## Recommendations for Translation Teams

### Phase 1: Foundation (High Traffic Pages)
1. `README.md` files in all sections
2. Main workflow pages
3. Core configuration guides
4. User management pages

### Phase 2: Advanced Features (Medium Priority)
1. Rule manager documentation
2. Document processing modules
3. Advanced settings pages
4. Testing procedures

### Phase 3: Specialized (Lower Priority)
1. Specific case definitions
2. Advanced configuration examples
3. Developer documentation
4. Legacy system integration

---

## Technical Notes

- All language branches maintain parallel directory structures
- Missing files are distributed across all categories
- No language has significantly different coverage from others
- This suggests systematic translation is best approach (vs. cherry-picking)

---

## Files Missing from ALL Languages

The following 583 pages exist in English (main) but are not translated to any language and need priority attention:

### Top 20 Missing Pages (by directory)

1. `administration-and-setup/report-page.md`
2. `administration-and-setup/settings/README.md`
3. `administration-and-setup/settings/api-licenses.md`
4. `administration-and-setup/settings/cache-management.md`
5. `administration-and-setup/settings/document-processing/README.md`
6. `administration-and-setup/settings/document-processing/decision-trees.md`
7. `administration-and-setup/settings/document-processing/documents-expiry.md`
8. `administration-and-setup/settings/document-processing/export.md`
9. `administration-and-setup/settings/document-processing/list-of-values.md`
10. `administration-and-setup/settings/document-processing/master-data-lookup.md`
11. `administration-and-setup/settings/document-processing/ocr-settings.md`
12. `administration-and-setup/settings/document-processing/classification-and-extraction/README.md`
13. `administration-and-setup/settings/document-processing/classification-and-extraction/auto-extract-tax-code.md`
14. `administration-and-setup/settings/document-processing/classification-and-extraction/table-extraction-for-costing-element.md`
15. `administration-and-setup/settings/document-processing/import/README.md`
16. `administration-and-setup/settings/document-processing/import/test-email-import-and-handling-tests.md`
17. `administration-and-setup/settings/document-processing/import/test-file-import-1.md`
18. `administration-and-setup/settings/document-processing/import/test-ftp-import-connection.md`
19. `administration-and-setup/settings/document-processing/import/test-multi-email-import-and-handling-tests.md`
20. `administration-and-setup/settings/document-processing/module/README.md`

*... and 563 more pages*

---

## Next Steps

1. Review this report with translation team leads
2. Prioritize Phase 1 pages for immediate translation
3. Create translation tasks/issues for each language
4. Set up automated comparison checks to prevent future gaps
5. Consider implementing translation memory tools for consistency
