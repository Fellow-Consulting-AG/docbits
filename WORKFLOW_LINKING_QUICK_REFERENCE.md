# Workflow Linking Quick Reference

**Version:** 1.0
**Date:** October 23, 2025
**Purpose:** Fast navigation and decision-making for DocBits workflow documentation

---

## Quick Navigation by Task

### "I need to integrate with an external system"

**Decision Matrix:**

| Your Situation | Use This | Guide |
|----------------|----------|-------|
| System has REST API | Call API | [Call API Guide](readme/administration-and-setup/workflow/then/action/call-api-guide.md) |
| Simple webhook/HTTP request | HTTPS Request | [HTTPS Request Guide](readme/administration-and-setup/workflow/then/action/https-request-guide.md) |
| Web form or legacy system | DocOperator Script | [DocOperator Script Guide](readme/administration-and-setup/workflow/then/action/docoperator-script-guide.md) |
| Complex multi-step integration | See Pattern | [API Integration Pattern](readme/administration-and-setup/workflow/patterns/api-integration-pattern.md) |

---

### "I need to notify or assign users"

| Your Situation | Use This | Guide |
|----------------|----------|-------|
| Send email to groups | Send Email | [Send Email Guide](readme/administration-and-setup/workflow/then/action/send-email-groups-guide.md) |
| Create task for user | Task Assignment | [Task Assignment Guide](readme/administration-and-setup/workflow/then/task/task-assignment-guide.md) |
| Assign document to user/group | Document Assignment | [Assignment Guide](readme/administration-and-setup/workflow/then/assignee/assignment-user-guide.md) |
| Complex routing workflow | See Pattern | [Task Management Pattern](readme/administration-and-setup/workflow/patterns/task-management-pattern.md) |

---

### "I need to work with document fields"

| Your Situation | Use This | Guide |
|----------------|----------|-------|
| Set field values | Field Manipulation | [Field Manipulation Guide](readme/administration-and-setup/workflow/then/document-field/field-manipulation-guide.md) |
| Calculate field values | Field Calculation | [Field Manipulation Guide](readme/administration-and-setup/workflow/then/document-field/field-manipulation-guide.md#calculations) |
| Store API response | Field Storage | [Field Manipulation Guide](readme/administration-and-setup/workflow/then/document-field/field-manipulation-guide.md#api-data) |
| Transform data | See Pattern | [Data Transformation Pattern](readme/administration-and-setup/workflow/patterns/data-transformation-pattern.md) |

---

### "I need to validate or check conditions"

| Your Situation | Use This | Guide |
|----------------|----------|-------|
| Compare with Purchase Order | PO Matching | [PO Matching Guide](readme/administration-and-setup/workflow/and/compare-with-purchase-order/po-matching-complete-guide.md) |
| Check field values | Condition Cards | [Condition Cards Guide](readme/administration-and-setup/workflow/and/condition-cards-complete-guide.md) |
| Check API response | HTTP Status Condition | [Condition Cards Guide](readme/administration-and-setup/workflow/and/condition-cards-complete-guide.md#condition-https-request-status) |
| Complex decision logic | See Pattern | [Decision Logic Pattern](readme/administration-and-setup/workflow/patterns/decision-logic-pattern.md) |

---

## Card Comparison Quick Reference

### External Integration Cards

| Feature | Call API | HTTPS Request | DocOperator |
|---------|----------|---------------|-------------|
| **Best For** | REST APIs | Simple webhooks | Web forms |
| **Complexity** | Medium | Low | High |
| **Setup Time** | 30 min | 10 min | 60-120 min |
| **Authentication** | OAuth/Token | Basic/None | Form-based |
| **Response Format** | JSON/XML | Any | Extracted data |
| **Error Handling** | Built-in | Basic | Custom |
| **Cost** | Standard | Standard | Higher resource |
| **Learning Curve** | Medium | Easy | Advanced |

**When to Use:**
- **Call API:** Professional REST API integration with authentication
- **HTTPS Request:** Quick webhook or simple HTTP calls
- **DocOperator:** Legacy systems without APIs, complex form automation

---

### Notification Methods

| Feature | Send Email | Task Assignment | Direct Assignment |
|---------|------------|-----------------|-------------------|
| **Best For** | Notifications | Actionable items | Document routing |
| **User Action** | Read | Complete task | Review document |
| **Tracking** | Email logs | Task status | Assignment history |
| **Deadline** | No | Yes | No |
| **Priority** | No | Yes | Via workflow |
| **Reminders** | No | Yes | Via workflow |
| **Reporting** | Limited | Detailed | Basic |

**When to Use:**
- **Send Email:** FYI notifications, external recipients
- **Task Assignment:** Actionable items requiring completion
- **Direct Assignment:** Document routing for review/approval

---

### Field Operations

| Operation | Card Type | Example | Guide Section |
|-----------|-----------|---------|---------------|
| Set static value | ACTION_SET_FIELD_TO_TEXT | "Status: Approved" | [Set Field](readme/administration-and-setup/workflow/then/document-field/field-manipulation-guide.md#set-field-to-text) |
| Copy field value | ACTION_COPY_FIELD_VALUE | Copy Vendor → Supplier | [Copy Field](readme/administration-and-setup/workflow/then/document-field/field-manipulation-guide.md#copy-field) |
| Calculate value | ACTION_CALCULATE_FIELD | Total = Qty × Price | [Calculate](readme/administration-and-setup/workflow/then/document-field/field-manipulation-guide.md#calculate-field) |
| Store API data | ACTION_SET_FIELD_FROM_API | Store API response | [API Data](readme/administration-and-setup/workflow/then/document-field/field-manipulation-guide.md#api-response-storage) |
| Lookup master data | ACTION_LOOKUP_MASTER_DATA | Get supplier name | [Master Data](readme/administration-and-setup/workflow/then/document-field/field-manipulation-guide.md#master-data-lookup) |

---

### Condition Types

| Condition Type | Example | Common Use | Guide Section |
|----------------|---------|------------|---------------|
| Document Status | Status = "Pending Approval" | Stage gates | [Status Conditions](readme/administration-and-setup/workflow/and/condition-cards-complete-guide.md#condition-doc-status-is-isnot) |
| Document Type | Type = "Invoice" | Type-specific logic | [Type Conditions](readme/administration-and-setup/workflow/and/condition-cards-complete-guide.md#condition-doc-type-is-isnot) |
| Field Value | Amount > 10000 | Amount thresholds | [Field Conditions](readme/administration-and-setup/workflow/and/condition-cards-complete-guide.md#field-conditions) |
| PO Comparison | Price variance < 5% | PO matching | [PO Conditions](readme/administration-and-setup/workflow/and/compare-with-purchase-order/po-matching-complete-guide.md) |
| Date Range | Date between Oct 1-31 | Period checks | [Date Conditions](readme/administration-and-setup/workflow/and/condition-cards-complete-guide.md#condition-time-is-isnot-between) |
| User/Group | Assigned to Finance | Role-based logic | [User Conditions](readme/administration-and-setup/workflow/and/condition-cards-complete-guide.md#condition-user-is-isnot) |
| HTTP Status | Response = 200 | API success check | [HTTP Conditions](readme/administration-and-setup/workflow/and/condition-cards-complete-guide.md#condition-https-request-status) |

---

## Common Workflow Patterns

### Pattern 1: API Integration + Validation

```
1. Call API (fetch data)
   ↓
2. Check HTTP Status (success?)
   ↓
3. Set Field (store response)
   ↓
4. Check Field Value (validate)
   ↓
5. Assign/Approve (take action)
```

**Guides:**
- [Call API Guide](readme/administration-and-setup/workflow/then/action/call-api-guide.md)
- [Condition Cards Guide](readme/administration-and-setup/workflow/and/condition-cards-complete-guide.md#condition-https-request-status)
- [Field Manipulation Guide](readme/administration-and-setup/workflow/then/document-field/field-manipulation-guide.md)
- [API Integration Pattern](readme/administration-and-setup/workflow/patterns/api-integration-pattern.md) ← **Complete Example**

---

### Pattern 2: PO Matching + Escalation

```
1. Compare PO (price/quantity)
   ↓
2. Check Tolerance (within range?)
   ↓
   YES: Auto-Approve
   NO: Create Review Task
   ↓
3. Assign to Reviewer
   ↓
4. Send Email Notification
```

**Guides:**
- [PO Matching Guide](readme/administration-and-setup/workflow/and/compare-with-purchase-order/po-matching-complete-guide.md)
- [Condition Cards Guide](readme/administration-and-setup/workflow/and/condition-cards-complete-guide.md)
- [Task Assignment Guide](readme/administration-and-setup/workflow/then/task/task-assignment-guide.md)
- [Send Email Guide](readme/administration-and-setup/workflow/then/action/send-email-groups-guide.md)
- [PO Matching Pattern](readme/administration-and-setup/workflow/patterns/po-matching-pattern.md) ← **Complete Example**

---

### Pattern 3: Amount-Based Routing

```
1. Check Amount
   ↓
   < €1,000: Assign to Clerk
   €1,000-€10,000: Assign to Manager
   > €10,000: Assign to Director
   ↓
2. Create Approval Task
   ↓
3. Send Email Notification
```

**Guides:**
- [Condition Cards Guide](readme/administration-and-setup/workflow/and/condition-cards-complete-guide.md#field-conditions)
- [Assignment Guide](readme/administration-and-setup/workflow/then/assignee/assignment-user-guide.md)
- [Task Assignment Guide](readme/administration-and-setup/workflow/then/task/task-assignment-guide.md)
- [Decision Logic Pattern](readme/administration-and-setup/workflow/patterns/decision-logic-pattern.md) ← **Complete Example**

---

### Pattern 4: Data Transformation

```
1. Extract Field Value
   ↓
2. Calculate/Transform
   ↓
3. Validate Result
   ↓
4. Store in Field
   ↓
5. Conditional Action
```

**Guides:**
- [Field Manipulation Guide](readme/administration-and-setup/workflow/then/document-field/field-manipulation-guide.md)
- [Condition Cards Guide](readme/administration-and-setup/workflow/and/condition-cards-complete-guide.md)
- [Data Transformation Pattern](readme/administration-and-setup/workflow/patterns/data-transformation-pattern.md) ← **Complete Example**

---

### Pattern 5: Task Management

```
1. Create Task
   ↓
2. Assign to User/Group
   ↓
3. Send Email Notification
   ↓
4. Track Task Status
   ↓
5. On Completion: Next Action
```

**Guides:**
- [Task Assignment Guide](readme/administration-and-setup/workflow/then/task/task-assignment-guide.md)
- [Assignment Guide](readme/administration-and-setup/workflow/then/assignee/assignment-user-guide.md)
- [Send Email Guide](readme/administration-and-setup/workflow/then/action/send-email-groups-guide.md)
- [Task Management Pattern](readme/administration-and-setup/workflow/patterns/task-management-pattern.md) ← **Complete Example**

---

## Error Handling Quick Reference

### API/Integration Errors

| Error | Check With | Solution | Guide |
|-------|------------|----------|-------|
| Timeout | CONDITION_HTTPS_REQUEST_STATUS | Retry logic | [Error Handling](readme/administration-and-setup/workflow/patterns/error-handling-pattern.md#timeout) |
| 401 Unauthorized | CONDITION_HTTPS_REQUEST_STATUS | Check credentials | [Call API Troubleshooting](readme/administration-and-setup/workflow/then/action/call-api-guide.md#unauthorized-error) |
| 404 Not Found | CONDITION_HTTPS_REQUEST_STATUS | Verify endpoint | [HTTPS Troubleshooting](readme/administration-and-setup/workflow/then/action/https-request-guide.md#not-found-error) |
| 500 Server Error | CONDITION_HTTPS_REQUEST_STATUS | Contact provider | [Call API Troubleshooting](readme/administration-and-setup/workflow/then/action/call-api-guide.md#server-error) |

---

### PO Matching Errors

| Error | Check With | Solution | Guide |
|-------|------------|----------|-------|
| Price variance exceeded | CONDITION_DOC_TO_PO_UNIT_PRICE | Adjust tolerance | [PO Matching - Tolerance](readme/administration-and-setup/workflow/and/compare-with-purchase-order/po-matching-complete-guide.md#tolerance-configuration) |
| Quantity mismatch | CONDITION_DOC_TO_PO_QUANTITY | Create review task | [PO Matching - Quantity](readme/administration-and-setup/workflow/and/compare-with-purchase-order/po-matching-complete-guide.md#quantity-comparison) |
| Missing PO | PURCHASE_ORDER_FULL_MATCH | Escalate to procurement | [PO Matching - Missing PO](readme/administration-and-setup/workflow/and/compare-with-purchase-order/po-matching-complete-guide.md#missing-po-handling) |

---

### Field/Data Errors

| Error | Check With | Solution | Guide |
|-------|------------|----------|-------|
| Field not found | CONDITION_DOC_FIELD_EXISTS | Set default value | [Field Manipulation](readme/administration-and-setup/workflow/then/document-field/field-manipulation-guide.md#field-validation) |
| Invalid calculation | Field value conditions | Use fallback value | [Field Manipulation](readme/administration-and-setup/workflow/then/document-field/field-manipulation-guide.md#calculation-errors) |
| Data type mismatch | Field validation | Transform data | [Data Transformation Pattern](readme/administration-and-setup/workflow/patterns/data-transformation-pattern.md#type-conversion) |

---

### Assignment Errors

| Error | Check With | Solution | Guide |
|-------|------------|----------|-------|
| User inactive | CONDITION_USER_IS_ISNOT | Fallback assignment | [Assignment Guide](readme/administration-and-setup/workflow/then/assignee/assignment-user-guide.md#inactive-user-handling) |
| Group empty | CONDITION_GROUP_IS_ISNOT | Assign to backup group | [Assignment Guide](readme/administration-and-setup/workflow/then/assignee/assignment-user-guide.md#empty-group-handling) |
| Assignment failed | Assignment status | Admin notification | [Assignment Guide](readme/administration-and-setup/workflow/then/assignee/assignment-user-guide.md#assignment-failures) |

---

## Decision Trees

### "Which integration method should I use?"

```
START: Need to integrate with external system
│
├─ Does system have a REST API?
│  │
│  ├─ YES: Does it require OAuth/complex auth?
│  │  │
│  │  ├─ YES → Use CALL API
│  │  │         [Call API Guide]
│  │  │
│  │  └─ NO: Is it a simple GET/POST?
│  │     │
│  │     ├─ YES → Use HTTPS REQUEST
│  │     │         [HTTPS Request Guide]
│  │     │
│  │     └─ NO → Use CALL API
│  │               [Call API Guide]
│  │
│  └─ NO: Is there a web interface?
│     │
│     ├─ YES → Use DOCOPERATOR SCRIPT
│     │         [DocOperator Guide]
│     │
│     └─ NO → Contact support for custom integration
```

---

### "How should I handle PO variance?"

```
START: Invoice received with PO reference
│
├─ Compare invoice to PO
│  [PO Matching Guide]
│
├─ Is variance within tolerance?
│  │
│  ├─ YES → Auto-approve
│  │         Continue workflow
│  │
│  └─ NO → Check variance amount
│     │
│     ├─ Small variance (< €100)
│     │  │
│     │  └─ Create review task
│     │     Assign to supervisor
│     │     [Task Assignment Guide]
│     │
│     └─ Large variance (> €100)
│        │
│        └─ Create urgent task
│           Assign to manager
│           Send email notification
│           [Task + Email Guides]
```

---

### "How should I route documents by amount?"

```
START: Document with total amount
│
├─ Check amount
│  [Condition Cards Guide]
│
├─ Amount < €1,000?
│  │
│  ├─ YES → Assign to Accounts Clerk
│  │         Auto-approve if all valid
│  │         [Assignment Guide]
│  │
│  └─ NO → Amount < €10,000?
│     │
│     ├─ YES → Assign to Accounts Manager
│     │         Require approval
│     │         [Assignment + Task Guides]
│     │
│     └─ NO → Assign to Finance Director
│              Require dual approval
│              Create approval task
│              Send email notification
│              [Assignment + Task + Email Guides]
```

---

## Card Version Quick Reference

### Cards with Multiple Versions

| Card Name | Versions | Current | Key Differences |
|-----------|----------|---------|-----------------|
| CONDITION_DOC_TO_PO_UNIT_PRICE | v2-v5 | v5 | v2: Basic comparison<br>v3: Added tolerance<br>v4: Comparison modes<br>v5: Enhanced tolerance |
| CONDITION_OC_TO_PO_ITEMS | v1-v4 | v4 | v1: Simple match<br>v2: Translation support<br>v3: Decision tree (deprecated)<br>v4: Generic type |
| tasks_create | v1-v4 | v4 | v1: Basic task<br>v2: Translation keys<br>v3: Decision tree (deprecated)<br>v4: Flexible work items |
| ACTION_TASK_FOR_GROUP | v2-v4 | v4 | v2: Basic group task<br>v3: Decision tree (deprecated)<br>v4: Enhanced routing |

**See:** [Complete Card Versioning Reference](readme/docs/card_version.md)

---

## Frequently Used Card Combinations

### 1. API Call + Field Storage + Validation
```
Cards: CALL_API → ACTION_SET_FIELD_TO_TEXT → CONDITION_DOC_FIELD_CONTAINS
Use: Fetch external data, store, validate
Guide: [API Integration Pattern]
```

### 2. PO Match + Conditional Task
```
Cards: CONDITION_DOC_TO_PO_UNIT_PRICE → tasks_create
Use: Compare price, create task if mismatch
Guide: [PO Matching Pattern]
```

### 3. Amount Check + Routing
```
Cards: CONDITION_DOC_FIELD_AMOUNT → ACTION_ASSIGN_TO_USER
Use: Route by amount threshold
Guide: [Decision Logic Pattern]
```

### 4. Task Creation + Email Notification
```
Cards: tasks_create → ACTION_SEND_EMAIL_TO_GROUPS
Use: Create task and notify
Guide: [Task Management Pattern]
```

### 5. Field Calculation + Storage
```
Cards: ACTION_CALCULATE_FIELD → ACTION_SET_FIELD_TO_TEXT
Use: Calculate and store result
Guide: [Data Transformation Pattern]
```

---

## Navigation Shortcuts

### By Card Type

**External Integration:**
- [Call API](readme/administration-and-setup/workflow/then/action/call-api-guide.md)
- [HTTPS Request](readme/administration-and-setup/workflow/then/action/https-request-guide.md)
- [DocOperator Script](readme/administration-and-setup/workflow/then/action/docoperator-script-guide.md)

**Communication:**
- [Send Email to Groups](readme/administration-and-setup/workflow/then/action/send-email-groups-guide.md)
- [Task Assignment](readme/administration-and-setup/workflow/then/task/task-assignment-guide.md)

**Data & Fields:**
- [Field Manipulation](readme/administration-and-setup/workflow/then/document-field/field-manipulation-guide.md)

**Assignment:**
- [Document Assignment](readme/administration-and-setup/workflow/then/assignee/assignment-user-guide.md)

**Validation:**
- [PO Matching](readme/administration-and-setup/workflow/and/compare-with-purchase-order/po-matching-complete-guide.md)
- [Condition Cards](readme/administration-and-setup/workflow/and/condition-cards-complete-guide.md)

### By Pattern

**Integration Patterns:**
- [API Integration Pattern](readme/administration-and-setup/workflow/patterns/api-integration-pattern.md)
- [Data Transformation Pattern](readme/administration-and-setup/workflow/patterns/data-transformation-pattern.md)

**Workflow Patterns:**
- [Task Management Pattern](readme/administration-and-setup/workflow/patterns/task-management-pattern.md)
- [Decision Logic Pattern](readme/administration-and-setup/workflow/patterns/decision-logic-pattern.md)
- [PO Matching Pattern](readme/administration-and-setup/workflow/patterns/po-matching-pattern.md)

### By Use Case

**Getting Started:**
- New to workflows? → [Workflow Overview](readme/administration-and-setup/workflow/README.md)
- Setting up integrations? → [Call API Guide](readme/administration-and-setup/workflow/then/action/call-api-guide.md)
- Creating tasks? → [Task Assignment Guide](readme/administration-and-setup/workflow/then/task/task-assignment-guide.md)

**Advanced:**
- Complex routing? → [Decision Logic Pattern](readme/administration-and-setup/workflow/patterns/decision-logic-pattern.md)
- Data transformation? → [Data Transformation Pattern](readme/administration-and-setup/workflow/patterns/data-transformation-pattern.md)
- Error handling? → [Error Handling Pattern](readme/administration-and-setup/workflow/patterns/error-handling-pattern.md)

---

## Performance Tips

### Optimization Guidelines

| Scenario | Recommendation | Guide |
|----------|----------------|-------|
| Many API calls | Cache responses in fields | [Field Manipulation](readme/administration-and-setup/workflow/then/document-field/field-manipulation-guide.md#caching-data) |
| Complex calculations | Pre-calculate in field | [Data Transformation](readme/administration-and-setup/workflow/patterns/data-transformation-pattern.md#optimization) |
| Large document volume | Use conditional execution | [Condition Cards](readme/administration-and-setup/workflow/and/condition-cards-complete-guide.md#optimization) |
| Frequent PO matching | Enable PO caching | [PO Matching](readme/administration-and-setup/workflow/and/compare-with-purchase-order/po-matching-complete-guide.md#performance) |

---

## Support Resources

### Need Help?

**Documentation:**
- Complete Linking Map: [WORKFLOW_LINKING_MAP.md](WORKFLOW_LINKING_MAP.md)
- Changelog: [October 2025 Release](readme/administration-and-setup/workflow/changelog/2025-10-october.md)
- Card Versions: [Card Versioning Reference](readme/docs/card_version.md)

**Common Issues:**
- API Issues: [Call API Troubleshooting](readme/administration-and-setup/workflow/then/action/call-api-guide.md#troubleshooting)
- PO Matching Issues: [PO Matching Troubleshooting](readme/administration-and-setup/workflow/and/compare-with-purchase-order/po-matching-complete-guide.md#troubleshooting)
- Field Issues: [Field Manipulation Troubleshooting](readme/administration-and-setup/workflow/then/document-field/field-manipulation-guide.md#troubleshooting)

**Contact:**
- Documentation Feedback: docs@docbits.com
- Technical Support: support@docbits.com

---

**Last Updated:** October 23, 2025
**Version:** 1.0
**Maintained By:** Documentation Team
