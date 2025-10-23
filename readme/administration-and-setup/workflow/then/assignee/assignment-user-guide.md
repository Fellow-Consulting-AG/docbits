# Document Assignment & User Cards - Complete Guide

**Covers:** 13 assignment and user-related cards

---

## 📌 Version Information

**Multi-Version Cards:** DOC_USER_ASSIGN (v2 latest, v3 deprecated), DOC_GROUP_ASSIGN (v2 latest, v3 deprecated), OC_ASSIGN_DOC (v2)

**Important:** v3 versions added decision tree support but are now deprecated
**Recommendation:** Use v2 for both DOC_USER_ASSIGN and DOC_GROUP_ASSIGN

📖 [Complete Version History](../../../changelog/release.md#-assignment--routing-cards) | [Card Version Database](../../../../DocFlow/docs/card_version.md)

---

# Basic Document Assignment

## Card: DOC_USER_ASSIGN / Assign Document to User

### Purpose
Assigns document to a specific person for their action

### When to Use
- Document needs specific person's review
- Handoff to individual team member
- Accountability tracking
- Assign work to named person

### How It Works
```
Document is "assigned to" = John Smith
Only John can see it as assigned to him
John is responsible for this document
```

### Example
```
Invoice arrives
    ↓
Assign Document to: John Smith (Finance Manager)
    ↓
Only John sees "Assigned to Me"
John must take action on it
```

### Parameters
```
User: [Select which person]
```

### Note
Assigning means:
- Document shows as "assigned to me" for that person
- That person is responsible
- Others can still see document (but not as assigned to them)
- One assignment at a time per document

---

## Card: DOC_GROUP_ASSIGN / Assign Document to Group

### Purpose
Assigns document to a group (all members see it as assigned to them)

### When to Use
- Document for team, not individual
- Multiple people can handle
- Shared responsibility
- Team workload distribution

### How It Works
```
Document is "assigned to" = Finance Team (10 people)
All 10 team members see "Assigned to My Group"
Any team member can take action
```

### Example
```
New vendor invoice
    ↓
Assign Document to: Procurement Team
    ↓
All procurement team members see it
First available person handles it
```

### Parameters
```
Group: [Select which group]
```

### Difference
```
Individual Assignment:
- One person responsible
- That person sees "Assigned to Me"
- Others don't see assignment

Group Assignment:
- Team responsible
- All members see "Assigned to My Group"
- Anyone can claim/process
```

---

## Card: ACTION_ASSIGN_DOC_BASED_ON_DECISION_TABLE

### Purpose
Assigns document based on decision table logic

### When to Use
- Different suppliers need different handlers
- Assignment based on amount
- Complex routing logic
- Multiple conditions for assignment

### How It Works
```
Decision Table Logic:
  If Supplier = "ABC Corp" → Assign to: Procurement Team
  If Supplier = "XYZ Inc" → Assign to: Direct Manager
  If Amount > €10000 → Assign to: Finance Director

Document arrives
    ↓
Check: Which condition matches?
    ↓
Assign accordingly
```

### Example: Amount-Based Assignment
```
Invoice: €2000 from ABC Corp

Decision Table checks:
  Is amount > €10000? NO
  Is amount > €5000? NO
  Is amount > €1000? YES

Result: Assign to: Finance Manager
```

### Example: Supplier-Based Assignment
```
Invoice from: Preferred Supplier

Decision Table:
  If preferred supplier → Finance Team
  If new supplier → Procurement Manager
  If blacklisted → Director Review

Result: Assign to: Finance Team
```

### Parameters
```
Decision Table: [Select decision table]
(Decision table contains assignment logic)
```

---

## Card: ACTION_ASSIGN_DOC_DECISION_TABLE_SEQUENTIAL

### Purpose
Assigns document sequentially based on decision table with priorities

### When to Use
- Multiple sequential approvals
- Different people at different levels
- Approval chain based on amount
- Escalation path

### How It Works
```
First Decision: Who approves first?
    ↓
Assign to: Person 1
    ↓
Person 1 approves
    ↓
Second Decision: Who approves next?
    ↓
Assign to: Person 2
    ↓
Person 2 approves (final)
    ↓
Document Complete
```

### Priority System
```
Priority 1: First assignment
Priority 2: Second assignment
Priority 3: Third assignment
(etc.)

Each must complete before next begins
```

### Example: Multi-Level Approval
```
Invoice: €50,000

Decision Table:
  €1k-€5k → Assign to: Finance Manager (Priority 1)
  €5k-€20k → Then: Assign to: Finance Director (Priority 2)
  €20k+ → Then: Assign to: CFO (Priority 3)

Invoice Flow:
1. Finance Manager reviews → approves
2. Finance Director reviews → approves
3. CFO reviews → approves final

Each step depends on previous completion
```

### Parameters
```
Decision Table: [Select]
Priority Order: [Determined by decision table]
```

---

## Card: ACTION_ASSIGN_DOC_TO_USER_SEQUENTIAL

### Purpose
Assigns document to user with sequential priority

### When to Use
- Document needs specific person
- Clear sequential processing
- Single assignment with order

### How It Works
```
Assign Document to: User A (Priority 1)
    ↓
User A processes
    ↓
Then: Assign to User B (Priority 2)
    ↓
User B processes
```

### Example
```
Invoice processing:
1. Assign to: Accounts Payable Clerk
2. Then: Assign to: Finance Manager
3. Then: Assign to: Director

Each person has their turn
```

---

## Card: ACTION_ASSIGN_DOC_TO_GROUP_SEQUENTIAL

### Purpose
Assigns document sequentially to groups

### When to Use
- Multiple group approvals
- Different departments at each stage
- Team-based sequential processing

### How It Works
```
Step 1: Assign to Group A (Quality Team)
        Quality verifies
    ↓
Step 2: Assign to Group B (Finance Team)
        Finance reviews
    ↓
Step 3: Assign to Group C (Procurement)
        Procurement approves
```

### Example
```
New Supplier Onboarding:

Step 1: Quality Team
  - Evaluate supplier capability
  - Check certifications

Step 2: Finance Team
  - Check payment terms
  - Verify pricing

Step 3: Procurement Team
  - Approve supplier
  - Set up in system

Document passes through all three
```

---

## Card: ACTION_ASSIGN_DOC_TO_FACILITY_GROUP

### Purpose
Assigns document to specific facility group

### When to Use
- Document for specific warehouse/facility
- Facility-based operations
- Location-specific processing

### Example
```
Shipment notification

Assign to: Berlin Warehouse Team
    ↓
Berlin warehouse processes shipment
    ↓
Or

Assign to: Munich Warehouse Team
    ↓
Munich warehouse processes shipment
```

---

## Card: ACTION_ASSIGN_DOC_TO_FACILITY_GROUP_SEQUENTIAL

### Purpose
Assigns sequentially across facilities

### When to Use
- Multi-location processing
- Shipment passes through facilities
- Location-based workflow

### Example
```
Manufacturing Order:

Step 1: Factory A (Manufacturing) - Build product
Step 2: Quality Center (Testing) - Test product
Step 3: Distribution Center (Packing) - Package
Step 4: Warehouse (Storage) - Store

Document/shipment passes through each
```

---

## Card: ACTION_ASSIGN_DOC_TO_PROCUREMENT_GROUP

### Purpose
Assigns document to procurement department

### When to Use
- Procurement team handling
- Supplier-related work
- Purchase order related

### Example
```
Vendor evaluation document
    ↓
Assign to: Procurement Group
    ↓
Procurement team evaluates vendor
```

---

## Card: ACTION_ASSIGN_DOC_TO_PROCUREMENT_GROUP_SEQUENTIAL

### Purpose
Sequential assignment within procurement

### When to Use
- Multi-step procurement process
- Approval chain in procurement

### Example
```
Purchase Requisition:

Step 1: Buyer (Creates PO)
Step 2: Approver (Reviews)
Step 3: Director (Final sign-off)

Each step in sequence
```

---

## Card: ACTION_CHANGE_DOC_SUBORG / Change Document Sub-Organization

### Purpose
Assigns document to different sub-organization

### When to Use
- Wrong organization selected
- Need to move to correct department
- Organizational restructuring

### How It Works
```
Current Sub-Org: Finance Department
    ↓
Change to: Accounting Department
    ↓
Document now belongs to Accounting
```

### Example
```
Document for: Berlin Office
    ↓
Realize should be: Munich Office
    ↓
Change Sub-Organization to: Munich Office
```

---

## Card: ACTION_CHANGE_DOC_SUBORG_BY_FIELD_TEXT

### Purpose
Changes sub-organization based on document field value

### When to Use
- Sub-organization stored in field
- Match document location with field
- Automatic org assignment

### How It Works
```
Document Field: "Delivery_Location" = "Berlin"
    ↓
Decision Table:
  If location = "Berlin" → Assign to: Berlin Sub-Org
  If location = "Munich" → Assign to: Munich Sub-Org

    ↓
Document assigned to: Berlin Sub-Org
```

### Example
```
Invoice field: "Cost Center: CC-Berlin-001"
    ↓
System recognizes: Berlin location
    ↓
Change document to: Berlin Sub-Organization
```

---

## Card: ACTION_ASSIGN_USER_FROM_FIELD_WITH_FALLBACK

### Purpose
Assigns document to user from field, with fallback if user not found

### When to Use
- User name stored in document field
- May not exist in system
- Need backup if user unavailable

### How It Works
```
Document Field: "Approver: John Smith"
    ↓
Try to assign to: John Smith
    ↓
If John doesn't exist:
    ↓
Use Fallback: Sarah Johnson (Manager)
    ↓
Document assigned to: Sarah Johnson
```

### Parameters
```
Source Field: [Field containing user name]
Fallback User: [If source user not found]
```

### Example
```
Invoice has field: "Contact Person: Mike Johnson"

Try to assign to: Mike Johnson
    ↓
If Mike not in system:
    ↓
Fallback to: Finance Manager (Robert)
```

---

## Card: ACTION_ASSIGN_USER_TO_SUPPLIER

### Purpose
Assigns document to user who manages that supplier

### When to Use
- User linked to supplier
- Supplier account manager
- Supplier relationship owner

### How It Works
```
Document Supplier: ABC Corp
    ↓
System checks: Who manages ABC Corp?
    ↓
Assign to: John Smith (ABC Corp Account Manager)
```

---

# Assignment Decision Trees

## Decision Table Example 1: Amount-Based
```
Amount ≤ €1000
  → Assign to: Finance Team

Amount €1000-€5000
  → Assign to: Finance Manager

Amount €5000-€20000
  → Assign to: Finance Director

Amount > €20000
  → Assign to: CFO
```

## Decision Table Example 2: Supplier-Based
```
Supplier Type = "Preferred"
  → Assign to: Account Manager

Supplier Type = "New"
  → Assign to: Procurement Manager

Supplier Type = "Problem"
  → Assign to: Procurement Director
```

## Decision Table Example 3: Document Type-Based
```
Document Type = "Invoice"
  → Assign to: Accounts Payable Team

Document Type = "Credit Memo"
  → Assign to: Finance Manager

Document Type = "PO"
  → Assign to: Procurement Team
```

---

# Assignment Workflow Examples

## Example 1: Simple Routing
```
Document Arrives
    ↓
Check: Supplier = "ABC Corp"? YES
    ↓
Assign to: John Smith
(John handles ABC Corp)
    ↓
John reviews and approves
```

## Example 2: Sequential Approval
```
Document Arrives
    ↓
Assign to: Finance Manager (Step 1)
    ↓
Manager reviews
    ↓
Passes to: Finance Director (Step 2)
    ↓
Director reviews
    ↓
Passes to: CFO (Step 3)
    ↓
CFO approves final
```

## Example 3: Amount-Based Routing
```
Invoice: €50,000
    ↓
Decision Table: Amount > €20k?
    ↓
YES → Assign to: CFO
    ↓
CFO approves directly
```

## Example 4: Facility-Based
```
Shipment for: Berlin Office
    ↓
Assign to: Berlin Warehouse Team
    ↓
Then assign to: Berlin Distribution Team
    ↓
Both teams process in sequence
```

---

# Assignment Best Practices

✅ **Do:**
- Keep decision tables simple
- Test routing logic with samples
- Ensure all paths lead somewhere
- Have fallback for missing users
- Document routing decisions

❌ **Don't:**
- Create circular assignments (A→B→A)
- Assign to non-existent users (without fallback)
- Make routing too complex
- Forget to test routing
- Assign to unavailable people

---

# Troubleshooting Assignment

## "Document not assigned"
**Cause:** Condition not met or user doesn't exist

**Solution:**
- Check condition is true
- Verify user exists in system
- Check fallback settings
- Review decision table logic

## "Wrong person assigned"
**Cause:** Decision table or routing logic incorrect

**Solution:**
- Test decision table
- Check conditions
- Verify user mapping
- Review field values

## "Assignment seems to skip someone"
**Cause:** Sequential order incorrect

**Solution:**
- Check priority numbers
- Verify sequence is correct
- Test with sample
- Review decision table ordering

---

# Assignment Cards Comparison

| Card | Assigns To | Route Type | Use Case |
|------|-----------|-----------|----------|
| DOC_USER_ASSIGN | Individual | Direct | Simple assignment |
| DOC_GROUP_ASSIGN | Group | Direct | Team assignment |
| ACTION_ASSIGN_DOC_BASED_ON_DECISION_TABLE | Decision Result | Conditional | Complex routing |
| ACTION_ASSIGN_DOC_DECISION_TABLE_SEQUENTIAL | Multiple (Sequential) | Conditional | Approval chain |
| ACTION_ASSIGN_DOC_TO_USER_SEQUENTIAL | User (Sequential) | Ordered | Sequential user steps |
| ACTION_ASSIGN_DOC_TO_GROUP_SEQUENTIAL | Groups (Sequential) | Ordered | Sequential group steps |
| ACTION_ASSIGN_DOC_TO_FACILITY_GROUP | Facility Group | Direct | Facility-specific |
| ACTION_ASSIGN_DOC_TO_FACILITY_GROUP_SEQUENTIAL | Facilities (Sequential) | Ordered | Multi-facility |
| ACTION_ASSIGN_DOC_TO_PROCUREMENT_GROUP | Procurement | Direct | Procurement workflow |
| ACTION_ASSIGN_DOC_TO_PROCUREMENT_GROUP_SEQUENTIAL | Procurement (Sequential) | Ordered | Procurement approval chain |
| ACTION_CHANGE_DOC_SUBORG | Sub-Organization | Direct | Department change |
| ACTION_CHANGE_DOC_SUBORG_BY_FIELD_TEXT | Sub-Org by Field | Conditional | Field-based assignment |
| ACTION_ASSIGN_USER_FROM_FIELD_WITH_FALLBACK | Field/Fallback | Conditional | Dynamic user assignment |

---

# Related Cards

- **ACTION_CREATE_TASK_FOR_USER** - Assign task to same person
- **ACTION_SEND_EMAIL** - Notify assigned person
- **CONDITION_USER_IS_ISNOT** - Check if correct person assigned
- **CONDITION_GROUP_IS_ISNOT** - Check if correct group assigned

