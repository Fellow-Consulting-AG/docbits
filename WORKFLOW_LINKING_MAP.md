# DocBits Workflow Linking Map

**Version:** 1.0
**Date:** October 23, 2025
**Purpose:** Comprehensive cross-reference map for all workflow documentation
**Total Links:** 87 identified opportunities

---

## Executive Summary

This document maps all cross-reference opportunities between DocBits workflow documentation files, creating a comprehensive navigation system that helps users understand relationships between workflow cards, data flows, and integration patterns.

**Key Statistics:**
- 9 comprehensive workflow guides created (October 2025)
- 80+ workflow cards documented
- 87 cross-reference opportunities identified
- 6 major linking categories
- 5 workflow pattern guides planned

---

## Table of Contents

1. [Linking Categories](#linking-categories)
2. [Category 1: Condition Card References (15 links)](#category-1-condition-card-references)
3. [Category 2: Data Flow Links (12 links)](#category-2-data-flow-links)
4. [Category 3: Action Card Comparisons (8 links)](#category-3-action-card-comparisons)
5. [Category 4: Error Handling Patterns (9 links)](#category-4-error-handling-patterns)
6. [Category 5: Workflow Integration Patterns (8 links)](#category-5-workflow-integration-patterns)
7. [Category 6: Enhancement Suggestions (35 links)](#category-6-enhancement-suggestions)
8. [Visual Navigation Map](#visual-navigation-map)
9. [Implementation Checklist](#implementation-checklist)

---

## Linking Categories

### Overview

| Category | Links | Priority | Impact | Effort |
|----------|-------|----------|--------|--------|
| Condition Card References | 15 | HIGH | High | Medium |
| Data Flow Links | 12 | HIGH | High | High |
| Action Card Comparisons | 8 | MEDIUM | High | Low |
| Error Handling Patterns | 9 | MEDIUM | Medium | Medium |
| Workflow Integration Patterns | 8 | HIGH | High | High |
| Enhancement Suggestions | 35+ | LOW-MED | Medium | Low |
| **TOTAL** | **87** | - | - | - |

---

## Category 1: Condition Card References

**Purpose:** Connect condition cards to their usage examples and implementation contexts

**Total Links:** 15

### 1.1 PO Matching Condition Cards (6 links)

#### Link Set: PO Comparison Conditions → PO Matching Guide

**From:** `condition-cards-complete-guide.md`
**To:** `compare-with-purchase-order/po-matching-complete-guide.md`

**Cards to Link:**
1. CONDITION_DOC_TO_PO_UNIT_PRICE (5 versions: v2-v5)
2. CONDITION_DOC_TO_PO_QUANTITY
3. CONDITION_DOC_TO_PO_TAX_LINES
4. CONDITION_OC_TO_PO_ITEMS (4 versions: v1-v4)
5. CONDITION_OC_TO_PO_CHARGES
6. PURCHASE_ORDER_FULL_MATCH

**Implementation:**
```markdown
## Related Guides

For detailed PO comparison logic and variance calculations, see:
- [PO Matching Complete Guide](../compare-with-purchase-order/po-matching-complete-guide.md) - Comprehensive PO validation workflows
- [Unit Price Variance Formulas](../compare-with-purchase-order/po-matching-complete-guide.md#unit-price-comparison)
- [Tolerance Configuration](../compare-with-purchase-order/po-matching-complete-guide.md#tolerance-parameters)
```

#### Reverse Link: PO Matching Guide → Condition Cards

**From:** `po-matching-complete-guide.md`
**To:** `condition-cards-complete-guide.md`

**Implementation:**
```markdown
## Prerequisites

Before setting up PO matching workflows, understand these condition cards:
- [CONDITION_DOC_TO_PO_UNIT_PRICE](../../condition-cards-complete-guide.md#condition-doc-to-po-unit-price) - Price comparison logic
- [CONDITION_DOC_TO_PO_QUANTITY](../../condition-cards-complete-guide.md#condition-doc-to-po-quantity) - Quantity validation
- [Complete Condition Cards Reference](../../condition-cards-complete-guide.md)
```

### 1.2 Status & Type Conditions → Workflow Examples (3 links)

**Cards:**
1. CONDITION_DOC_STATUS_IS_ISNOT → Assignment Guide (status-based routing)
2. CONDITION_DOC_TYPE_IS_ISNOT → Field Manipulation Guide (type-specific fields)
3. CONDITION_SUB_ORG_IS_ISNOT → Assignment Guide (org-based assignment)

**Implementation Example:**
```markdown
## See Also: Real-World Applications

- **Status-Based Routing:** [Document Assignment Guide - Sequential Routing](../../then/assignee/assignment-user-guide.md#status-based-assignment)
- **Type-Specific Processing:** [Field Manipulation Guide - Document Types](../../then/document-field/field-manipulation-guide.md#type-specific-fields)
```

### 1.3 API Response Conditions (2 links)

**Cards:**
1. CONDITION_HTTPS_REQUEST_STATUS → Call API Guide (error handling)
2. CONDITION_HTTPS_REQUEST_STATUS → HTTPS Request Guide (response validation)

**Implementation:**
```markdown
## Related Integration Cards

For API integration and response handling:
- [Call API Guide - Error Handling](../../then/action/call-api-guide.md#troubleshooting)
- [HTTPS Request Guide - Response Codes](../../then/action/https-request-guide.md#response-scenarios)
```

### 1.4 Supplier Conditions (2 links)

**Cards:**
1. CONDITION_SUPPLIER_STATUS_IS_ISNOT → Assignment Guide (supplier-based routing)
2. CONDITION_SPECIFY_SUPPLIER_TYPE → Field Manipulation (supplier data)

### 1.5 Date/Time Conditions (2 links)

**Cards:**
1. CONDITION_TIME_IS_ISNOT_BETWEEN → Task Assignment (deadline-based tasks)
2. CONDITION_TODAY_IS_ISNOT → Email Notifications (time-based alerts)

---

## Category 2: Data Flow Links

**Purpose:** Show how data flows through multiple workflow cards

**Total Links:** 12

### 2.1 API Integration Flow (4 links)

**Flow:** External Data → Storage → Validation → Action

```
Call API → Field Storage → Condition Check → Document Action
```

**Links:**

1. **Call API Guide → Field Manipulation Guide**
   - From: "Response Data Usage" section
   - To: "Setting Fields from API Response"
   - Flow: Store API response in document fields

2. **Field Manipulation Guide → Condition Cards Guide**
   - From: "Field Values" section
   - To: "Field-Based Conditions"
   - Flow: Validate stored field values

3. **Condition Cards Guide → Assignment Guide**
   - From: "Decision Logic" section
   - To: "Conditional Assignment"
   - Flow: Route based on field validation

4. **Assignment Guide → Task Assignment Guide**
   - From: "Assignment Triggers"
   - To: "Creating Tasks After Assignment"
   - Flow: Generate tasks for assigned users

**Implementation:**
```markdown
## Data Flow: API Integration Pattern

This workflow demonstrates end-to-end API integration:

1. **Step 1: Fetch Data** - [Call API Guide](../action/call-api-guide.md)
   - Call external pricing API
   - Receive pricing response

2. **Step 2: Store Data** - [Field Manipulation Guide](../document-field/field-manipulation-guide.md#set-field-from-api)
   - Store API response in document fields
   - Transform data format

3. **Step 3: Validate Data** - [Condition Cards Guide](../../and/condition-cards-complete-guide.md#field-validation)
   - Check if price within acceptable range
   - Validate data completeness

4. **Step 4: Take Action** - [Assignment Guide](assignment-user-guide.md#conditional-assignment)
   - Route to appropriate approver
   - Create approval task

See: [API Integration Pattern Guide](../../patterns/api-integration-pattern.md)
```

### 2.2 Document Processing Flow (3 links)

**Flow:** Document Import → Field Extraction → PO Matching → Export

**Links:**

5. **Field Manipulation → PO Matching**
   - Extract invoice fields → Compare with PO data

6. **PO Matching → Condition Cards**
   - PO match result → Decision logic

7. **Condition Cards → Document Status**
   - Validation result → Approve/Reject/Escalate

### 2.3 Task Management Flow (3 links)

**Flow:** Task Creation → Assignment → Notification → Completion

**Links:**

8. **Task Assignment → Assignment Guide**
   - Task creation → Assign to user/group

9. **Assignment Guide → Email Notifications**
   - User assigned → Send notification email

10. **Email Notifications → Task Assignment**
    - Notification sent → Task status tracking

### 2.4 Error Handling Flow (2 links)

**Flow:** API Call → Error Detection → Retry/Escalate → Resolution

**Links:**

11. **Call API → Condition Cards (HTTP Status)**
    - API response → Check status code

12. **Condition Cards → Email Notifications (Errors)**
    - Error detected → Escalate via email

---

## Category 3: Action Card Comparisons

**Purpose:** Help users choose the right implementation method

**Total Links:** 8

### 3.1 External Integration Comparison (3 links)

**Decision Point:** "How should I integrate with external systems?"

**Comparison Matrix:**

| Feature | Call API | HTTPS Request | DocOperator Script |
|---------|----------|---------------|-------------------|
| Complexity | Medium | Simple | Advanced |
| Use Case | REST APIs | Webhooks | Browser automation |
| Response Handling | JSON/XML | Any format | Extracted data |
| Authentication | OAuth/Token | Basic/None | Form-based |
| Setup Time | 30 min | 10 min | 60-120 min |

**Links:**

1. **Call API ↔ HTTPS Request**
   - From: call-api-guide.md → "When to Use HTTPS Request Instead"
   - From: https-request-guide.md → "When to Upgrade to Call API"

2. **Call API ↔ DocOperator Script**
   - From: call-api-guide.md → "When to Use DocOperator"
   - From: docoperator-script-guide.md → "When to Use API Instead"

3. **HTTPS Request ↔ DocOperator Script**
   - From: https-request-guide.md → "Advanced Scenarios with DocOperator"
   - From: docoperator-script-guide.md → "Simple Requests with HTTPS"

**Implementation:**
```markdown
## Choosing the Right Integration Method

### Decision Tree

**Question 1: Does the system have an API?**
- YES → Use [Call API Guide](./call-api-guide.md)
- NO → Go to Question 2

**Question 2: Can you send a simple HTTP request?**
- YES → Use [HTTPS Request Guide](./https-request-guide.md)
- NO → Go to Question 3

**Question 3: Do you need browser automation?**
- YES → Use [DocOperator Script Guide](./docoperator-script-guide.md)
- NO → Contact support for custom integration

### Comparison Guide

| Scenario | Best Choice | Guide |
|----------|-------------|-------|
| REST API with JSON | Call API | [Call API Guide](./call-api-guide.md) |
| Simple webhook | HTTPS Request | [HTTPS Request Guide](./https-request-guide.md) |
| Web form submission | DocOperator Script | [DocOperator Guide](./docoperator-script-guide.md) |
| Legacy system (no API) | DocOperator Script | [DocOperator Guide](./docoperator-script-guide.md) |
```

### 3.2 Notification Method Comparison (2 links)

**Decision Point:** "How should I notify users?"

**Options:**
- Send Email to Groups
- Task Assignment with Notification
- Direct User Assignment

**Links:**

4. **Email Guide ↔ Task Assignment**
   - Email: "When to Create Tasks Instead"
   - Task: "When to Send Email Instead"

5. **Task Assignment ↔ Assignment Guide**
   - Task: "Task vs. Direct Assignment"
   - Assignment: "Assignment vs. Task Creation"

### 3.3 Data Manipulation Comparison (3 links)

**Decision Point:** "How should I update document fields?"

**Options:**
- Set Field to Text/Number
- Calculate Field Value
- Copy from Master Data

**Links:**

6. **Field Manipulation → Master Data Lookup**
   - "When to lookup vs. calculate"

7. **Field Manipulation → API Data**
   - "When to fetch vs. calculate"

8. **Field Manipulation → PO Matching**
   - "When to validate vs. set"

---

## Category 4: Error Handling Patterns

**Purpose:** Connect error scenarios to their solutions

**Total Links:** 9

### 4.1 API Integration Errors (3 links)

**Scenario 1: API Timeout**

**From:** call-api-guide.md#troubleshooting
**To:** condition-cards-complete-guide.md#https-request-status

**Flow:**
```
Call API → Timeout → Check Status → Retry or Escalate
```

**Implementation:**
```markdown
## Error Handling: API Timeout

**Pattern:**
1. [Call API](./call-api-guide.md) attempts connection
2. Timeout occurs (no response)
3. [Check HTTP Status](../../and/condition-cards-complete-guide.md#condition-https-request-status)
4. [Retry Logic](../../patterns/error-handling-pattern.md#retry-logic)
5. If still fails: [Escalate via Email](./send-email-groups-guide.md#error-notifications)

**See Also:**
- [Error Handling Pattern Guide](../../patterns/error-handling-pattern.md)
- [Timeout Configuration](./call-api-guide.md#timeout-settings)
```

**Links:**

1. API Timeout → Retry Logic → Email Escalation
2. HTTP Error (4xx/5xx) → Error Detection → Email Notification
3. Authentication Failure → Status Check → Manual Review

### 4.2 PO Matching Errors (3 links)

**Scenarios:**

4. **Price Variance Exceeded** → Tolerance Check → Escalation Workflow
   - From: po-matching-complete-guide.md
   - To: assignment-user-guide.md (escalation)

5. **Quantity Mismatch** → Validation Failure → Create Task for Review
   - From: po-matching-complete-guide.md
   - To: task-assignment-guide.md

6. **Missing PO Data** → Data Check → Email Procurement
   - From: po-matching-complete-guide.md
   - To: send-email-groups-guide.md

### 4.3 Workflow Execution Errors (3 links)

**Scenarios:**

7. **Field Not Found** → Field Validation → Set Default Value
   - From: field-manipulation-guide.md
   - To: condition-cards-complete-guide.md

8. **Assignment Failed (User Inactive)** → User Check → Fallback Assignment
   - From: assignment-user-guide.md
   - To: condition-cards-complete-guide.md#user-status

9. **Task Creation Failed** → Error Detection → Admin Notification
   - From: task-assignment-guide.md
   - To: send-email-groups-guide.md

---

## Category 5: Workflow Integration Patterns

**Purpose:** Show multiple cards working together in common scenarios

**Total Links:** 8

### 5.1 Complete Workflow Patterns

Each pattern shows 3-5 cards working together:

**Pattern 1: API Integration + Field Storage + Validation**

**Cards Involved:**
1. Call API (fetch pricing)
2. Set Field (store response)
3. Check Condition (validate range)
4. Approve/Reject Document

**Links:** 4 cross-references between guides

**Pattern 2: Task Creation + Assignment + Notification**

**Cards Involved:**
1. Create Task
2. Assign to User/Group
3. Send Email Notification
4. Track Task Status

**Links:** 3 cross-references

**Pattern 3: PO Matching + Tolerance + Auto-Export**

**Cards Involved:**
1. Compare PO Unit Price
2. Check Tolerance Range
3. If Pass: Auto-export
4. If Fail: Create Review Task

**Links:** 4 cross-references

**Pattern 4: Conditional Routing + Multi-Level Approval**

**Cards Involved:**
1. Check Amount Threshold
2. Assign Based on Amount
3. Sequential Approval
4. Final Export

**Links:** 3 cross-references

**Pattern 5: Data Transformation + Validation + Storage**

**Cards Involved:**
1. Extract Field Value
2. Transform/Calculate
3. Validate Result
4. Store in Field

**Links:** 4 cross-references

---

## Category 6: Enhancement Suggestions

**Purpose:** Strategic documentation improvements

**Total Links:** 35+

### 6.1 Add "Related Guides" Sections (9 links)

**To Each Guide, Add:**

```markdown
## Related Guides

### Prerequisites
- [Guide Name](path) - What you should know first

### Related Cards
- [Guide Name](path) - Cards that work with this one

### Next Steps
- [Guide Name](path) - What to do after this

### Patterns
- [Pattern Name](path) - See this card in action
```

**Implementation Locations:**
1. call-api-guide.md
2. https-request-guide.md
3. docoperator-script-guide.md
4. send-email-groups-guide.md
5. task-assignment-guide.md
6. field-manipulation-guide.md
7. assignment-user-guide.md
8. po-matching-complete-guide.md
9. condition-cards-complete-guide.md

### 6.2 Add "Prerequisites" Sections (9 links)

**Before You Start:**
- Required knowledge
- Required setup
- Required permissions
- Related concepts

### 6.3 Add "Next Steps" Sections (9 links)

**After This Guide:**
- Common next configurations
- Related workflows
- Advanced features
- Troubleshooting resources

### 6.4 Create Comparison Tables (8 links)

Add to relevant guides:
- Feature comparison matrices
- Use case decision trees
- Performance comparisons
- Complexity ratings

---

## Visual Navigation Map

```
DocBits Workflow Documentation Structure
├── Core Guides (9 files)
│   ├── External Integration
│   │   ├── call-api-guide.md ←→ https-request-guide.md
│   │   ├── call-api-guide.md ←→ docoperator-script-guide.md
│   │   └── https-request-guide.md ←→ docoperator-script-guide.md
│   │
│   ├── Communication
│   │   ├── send-email-groups-guide.md ←→ task-assignment-guide.md
│   │   └── task-assignment-guide.md ←→ assignment-user-guide.md
│   │
│   ├── Data & Fields
│   │   ├── field-manipulation-guide.md ←→ call-api-guide.md
│   │   └── field-manipulation-guide.md ←→ po-matching-complete-guide.md
│   │
│   ├── Assignment
│   │   ├── assignment-user-guide.md ←→ task-assignment-guide.md
│   │   └── assignment-user-guide.md ←→ condition-cards-complete-guide.md
│   │
│   └── Validation
│       ├── po-matching-complete-guide.md ←→ condition-cards-complete-guide.md
│       └── condition-cards-complete-guide.md → [All Guides]
│
└── Pattern Guides (5 new files)
    ├── api-integration-pattern.md
    ├── task-management-pattern.md
    ├── po-matching-pattern.md
    ├── decision-logic-pattern.md
    └── data-transformation-pattern.md
```

---

## Implementation Checklist

### Phase 1: High-Impact Navigation (45 min)

- [ ] Add "Related Guides" to all 9 main guides
- [ ] Add "See Also" reference lists
- [ ] Link condition cards to usage examples
- [ ] Add "Prerequisites" to complex guides
- [ ] Test all internal links

### Phase 2: Workflow Pattern Documentation (60 min)

- [ ] Create api-integration-pattern.md
- [ ] Create task-management-pattern.md
- [ ] Create po-matching-pattern.md
- [ ] Create decision-logic-pattern.md
- [ ] Create data-transformation-pattern.md
- [ ] Add pattern references to main guides

### Phase 3: Enhancement Polish (30 min)

- [ ] Add cross-reference tables
- [ ] Create navigation breadcrumbs
- [ ] Implement "Related Reading" sections
- [ ] Add comparison matrices
- [ ] Quality check all 87 links
- [ ] Update SUMMARY.md with new files

---

## Link Quality Standards

### Required Elements for Each Link

1. **Context:** Why this link is relevant
2. **Direction:** Clear navigation path
3. **Anchor:** Specific section when possible
4. **Description:** What user will find
5. **Bidirectional:** Link both ways when appropriate

### Link Format Template

```markdown
## [Section Name]

[Context paragraph explaining why this is relevant]

**See Also:**
- [Specific Topic](relative-path.md#section) - Brief description of what's there
- [Related Feature](relative-path.md#section) - Why user should check this
- [Advanced Topic](relative-path.md#section) - Next level information

**Prerequisites:**
- [Required Knowledge](path.md) - What to know first

**Next Steps:**
- [Common Next Action](path.md) - What to do after this
```

---

## Maintenance Guidelines

### When to Update This Map

1. New workflow guide created
2. Workflow card added/changed
3. User feedback indicates missing link
4. Documentation restructured
5. New integration pattern identified

### Link Validation

**Monthly:**
- Check all links still valid
- Verify anchors still exist
- Update descriptions if content changed

**Quarterly:**
- Review link relevance
- Identify new linking opportunities
- Update visual map

---

## Success Metrics

### Measuring Link Effectiveness

1. **User Navigation:** Time to find related information
2. **Completion Rate:** Users finding what they need
3. **Bounce Rate:** Users leaving without finding answer
4. **Feedback:** User comments on helpfulness

### Target Goals

- 87/87 links implemented (100%)
- <2 clicks to reach any related guide
- <30 seconds to find related information
- >90% user satisfaction with navigation

---

## Quick Reference: Link by Guide

### call-api-guide.md
**Outgoing Links:** 8
- → https-request-guide.md (comparison)
- → docoperator-script-guide.md (comparison)
- → field-manipulation-guide.md (response storage)
- → condition-cards-complete-guide.md (status check)
- → send-email-groups-guide.md (error notification)
- → api-integration-pattern.md (full example)
- → error-handling-pattern.md (troubleshooting)
- → data-transformation-pattern.md (data processing)

### https-request-guide.md
**Outgoing Links:** 6
- → call-api-guide.md (when to upgrade)
- → docoperator-script-guide.md (advanced scenarios)
- → condition-cards-complete-guide.md (response validation)
- → send-email-groups-guide.md (webhooks)
- → api-integration-pattern.md (simple integration)
- → error-handling-pattern.md (timeout handling)

### docoperator-script-guide.md
**Outgoing Links:** 7
- → call-api-guide.md (when API available)
- → https-request-guide.md (simple requests)
- → field-manipulation-guide.md (data extraction)
- → condition-cards-complete-guide.md (script validation)
- → api-integration-pattern.md (complex automation)
- → data-transformation-pattern.md (form data)
- → error-handling-pattern.md (script errors)

### send-email-groups-guide.md
**Outgoing Links:** 6
- → task-assignment-guide.md (task vs email)
- → assignment-user-guide.md (notification after assignment)
- → condition-cards-complete-guide.md (conditional emails)
- → call-api-guide.md (error notifications)
- → task-management-pattern.md (notification pattern)
- → error-handling-pattern.md (escalation emails)

### task-assignment-guide.md
**Outgoing Links:** 7
- → send-email-groups-guide.md (email vs task)
- → assignment-user-guide.md (assignment integration)
- → condition-cards-complete-guide.md (conditional tasks)
- → po-matching-complete-guide.md (review tasks)
- → task-management-pattern.md (complete workflow)
- → decision-logic-pattern.md (task routing)
- → error-handling-pattern.md (task failures)

### field-manipulation-guide.md
**Outgoing Links:** 8
- → call-api-guide.md (API data storage)
- → po-matching-complete-guide.md (field validation)
- → condition-cards-complete-guide.md (field conditions)
- → assignment-user-guide.md (field-based routing)
- → data-transformation-pattern.md (calculation examples)
- → api-integration-pattern.md (response storage)
- → decision-logic-pattern.md (field logic)
- → error-handling-pattern.md (field errors)

### assignment-user-guide.md
**Outgoing Links:** 8
- → task-assignment-guide.md (assignment + tasks)
- → send-email-groups-guide.md (assignment notifications)
- → condition-cards-complete-guide.md (conditional routing)
- → field-manipulation-guide.md (field-based assignment)
- → po-matching-complete-guide.md (escalation assignment)
- → task-management-pattern.md (assignment workflow)
- → decision-logic-pattern.md (routing logic)
- → error-handling-pattern.md (assignment failures)

### po-matching-complete-guide.md
**Outgoing Links:** 9
- → condition-cards-complete-guide.md (PO conditions)
- → field-manipulation-guide.md (PO data fields)
- → task-assignment-guide.md (review tasks)
- → assignment-user-guide.md (escalation routing)
- → send-email-groups-guide.md (mismatch notifications)
- → po-matching-pattern.md (complete pattern)
- → decision-logic-pattern.md (tolerance logic)
- → error-handling-pattern.md (match failures)
- → data-transformation-pattern.md (PO data)

### condition-cards-complete-guide.md
**Outgoing Links:** 12 (Central hub - links to all other guides)
- → call-api-guide.md (HTTP status conditions)
- → https-request-guide.md (request conditions)
- → docoperator-script-guide.md (script conditions)
- → po-matching-complete-guide.md (PO conditions)
- → field-manipulation-guide.md (field conditions)
- → assignment-user-guide.md (assignment conditions)
- → task-assignment-guide.md (task conditions)
- → send-email-groups-guide.md (email conditions)
- → decision-logic-pattern.md (all decision examples)
- → api-integration-pattern.md (integration conditions)
- → task-management-pattern.md (task conditions)
- → po-matching-pattern.md (matching conditions)

---

## Pattern Guides Link Summary

### api-integration-pattern.md (NEW)
**Outgoing Links:** 4
- → call-api-guide.md
- → field-manipulation-guide.md
- → condition-cards-complete-guide.md
- → assignment-user-guide.md

### task-management-pattern.md (NEW)
**Outgoing Links:** 4
- → task-assignment-guide.md
- → assignment-user-guide.md
- → send-email-groups-guide.md
- → condition-cards-complete-guide.md

### po-matching-pattern.md (NEW)
**Outgoing Links:** 4
- → po-matching-complete-guide.md
- → condition-cards-complete-guide.md
- → task-assignment-guide.md
- → assignment-user-guide.md

### decision-logic-pattern.md (NEW)
**Outgoing Links:** 5
- → condition-cards-complete-guide.md
- → assignment-user-guide.md
- → field-manipulation-guide.md
- → task-assignment-guide.md
- → po-matching-complete-guide.md

### data-transformation-pattern.md (NEW)
**Outgoing Links:** 4
- → field-manipulation-guide.md
- → call-api-guide.md
- → condition-cards-complete-guide.md
- → po-matching-complete-guide.md

---

## Total Link Summary

| Guide | Outgoing | Incoming | Total |
|-------|----------|----------|-------|
| call-api-guide.md | 8 | 6 | 14 |
| https-request-guide.md | 6 | 5 | 11 |
| docoperator-script-guide.md | 7 | 5 | 12 |
| send-email-groups-guide.md | 6 | 6 | 12 |
| task-assignment-guide.md | 7 | 7 | 14 |
| field-manipulation-guide.md | 8 | 7 | 15 |
| assignment-user-guide.md | 8 | 7 | 15 |
| po-matching-complete-guide.md | 9 | 6 | 15 |
| condition-cards-complete-guide.md | 12 | 9 | 21 |
| **Pattern Guides (5 new)** | **21** | **9** | **30** |
| **GRAND TOTAL** | **92** | **67** | **159** |

*Note: Total exceeds 87 as many links are bidirectional*

---

**Last Updated:** October 23, 2025
**Next Review:** November 23, 2025
**Maintained By:** Documentation Team
**Feedback:** docs@docbits.com
