# Taakbeheer Patroon

**Patroontype:** Workflowbeheer
**Complexiteit:** Laag-Gemiddeld
**Geschatte Insteltijd:** 30-45 minuten
**Veelvoorkomende Gebruiksscenario's:** Goedkeuringsworkflows, beoordelingstaken, uitzonderingsafhandeling, escalatie

---

## Patroonoverzicht

Dit patroon demonstreert hoe u taken in DocBits workflows kunt creëren, toewijzen, volgen en beheren. Taken zijn actievere werkitems die zijn toegewezen aan gebruikers of groepen en die voltooiing vereisen voordat de documentworkflow kan doorgaan.

**Wat Dit Patroon Doet:**
1. Maakt taken op basis van workflowvoorwaarden
2. Wijst taken toe aan de juiste gebruikers of groepen
3. Stelt taakeigenschappen in (prioriteit, deadline, beschrijving)
4. Stuurt meldingen wanneer taken worden aangemaakt
5. Volgt taakstatus en voltooiing
6. Routeert documenten op basis van taakuitkomsten

---

## Wanneer Dit Patroon Te Gebruiken

Gebruik dit patroon wanneer u het volgende moet doen:
- ✅ Goedkeuringsworkflows creëren
- ✅ Beoordelingstaken toewijzen aan gebruikers
- ✅ Uitzonderingen afhandelen die menselijke tussenkomst vereisen
- ✅ Problemen escaleren naar managers
- ✅ Goedkeuringsketens op meerdere niveaus creëren
- ✅ Volgen wie wat moet doen
- ✅ Deadlines instellen voor acties

**Gebruik dit patroon niet wanneer:**
- ❌ Geen menselijke actie vereist is (gebruik in plaats daarvan automatische verwerking)
- ❌ Alleen een melding nodig is (gebruik in plaats daarvan e-mail)
- ❌ Eenvoudige documentroutering voldoende is (gebruik in plaats daarvan toewijzing)

---

## Compleet Workflowvoorbeeld

### Scenario: Factuurgoedkeuring met Op Bedrag Gebaseerde Routering

**Bedrijfsvereiste:**
- Facturen < €1.000: Automatisch goedkeuren (geen taak nodig)
- Facturen €1.000-€10.000: Goedkeuringstaak naar Manager
- Facturen > €10.000: Dubbele goedkeuring (Manager + Directeur)
- Alle goedkeurders ontvangen e-mailmelding
- Taken hebben een deadline van 3 dagen

**Gebruikte Workflowkaarten:**
1. CONDITION_DOC_FIELD_AMOUNT - Controleer factuurbedrag
2. tasks_create - Maak goedkeuringstaak
3. ACTION_ASSIGN_TO_USER - Wijs taak toe aan goedkeurder
4. ACTION_SEND_EMAIL_TO_GROUPS - Stuur melding
5. CONDITION_TASK_STATUS - Controleer of taak voltooid is
6. ACTION_APPROVE_DOCUMENT - Keur goed na taakvoltooiing

---

## Stap-voor-Stap Implementatie

### Stap 1: Controleer Bedragdrempel

**Kaart:** CONDITION_DOC_FIELD_AMOUNT of vergelijkbare veldconditie

**Configuratie voor Pad 1 (< €1.000):**
```
Veld: Total_Amount
Operator: IS LESS THAN
Waarde: 1000
Valuta: EUR
```

**Configuratie voor Pad 2 (€1.000-€10.000):**
```
Veld: Total_Amount
Operator: IS BETWEEN
Waarde Min: 1000
Waarde Max: 10000
Valuta: EUR
```

**Configuratie voor Pad 3 (> €10.000):**
```
Veld: Total_Amount
Operator: IS GREATER THAN
Waarde: 10000
Valuta: EUR
```

**Gidsreferentie:** [Gids Conditiekaarten](../and/condition-cards-complete-guide.md)

---

### Stap 2A: Automatisch Goedkeuren Kleine Facturen (< €1.000)

**Geen taak nodig voor kleine bedragen**

**Kaarten:**
- ACTION_SET_FIELD_TO_TEXT
  - Stel "Approval_Type" in op "AUTO"
  - Stel "Approval_Reason" in op "Bedrag onder drempel"
- ACTION_APPROVE_DOCUMENT

**Resultaat:** Document automatisch goedgekeurd, geen taak aangemaakt

---

### Stap 2B: Maak Manager Goedkeuringstaak (€1.000-€10.000)

**Kaart:** tasks_create (v4 aanbevolen)

**Configuratie:**
```json
{
  "task_type": "Approval",
  "task_title": "Keur Factuur {{DOCUMENT_NUMBER}} Goed - €{{Total_Amount}}",
  "task_description": "Gelieve de factuur van {{Supplier_Name}} goed te keuren\n\nBedrag: €{{Total_Amount}}\nFactuurnummer: {{Invoice_Number}}\nFactuurdatum: {{Invoice_Date}}\n\nBeoordeel en keur goed binnen 3 werkdagen.",
  "priority": "Medium",
  "deadline_days": 3,
  "assign_to": "{{DOCUMENT_FIELD:Approving_Manager}}",
  "task_category": "Invoice Approval",
  "required_action": "Approve or Reject"
}
```

**Veldtoewijzing:**
- `{{DOCUMENT_NUMBER}}` - Automatische document-ID
- `{{Total_Amount}}` - Veld: Total_Amount
- `{{Supplier_Name}}` - Veld: Supplier_Name
- `{{Invoice_Number}}` - Veld: Invoice_Number
- `{{Invoice_Date}}` - Veld: Invoice_Date
- `{{Approving_Manager}}` - Veld of vaste gebruiker

**Gidsreferentie:** [Taaktoewijzingsgids](../then/task/task-assignment-guide.md)

---

### Stap 2C: Maak Dubbele Goedkeuringstaken (> €10.000)

**Twee sequentiële taken voor facturen met hoge waarde**

**Taak 1: Manager Goedkeuring**
```json
{
  "task_type": "First Approval",
  "task_title": "URGENT: Keur Factuur Hoge Waarde {{DOCUMENT_NUMBER}} Goed - €{{Total_Amount}}",
  "task_description": "FACTUUR HOGE WAARDE VEREIST GOEDKEURING\n\nLeverancier: {{Supplier_Name}}\nBedrag: €{{Total_Amount}}\n\nDeze factuur overschrijdt €10.000 en vereist dubbele goedkeuring.\nUw goedkeuring is vereist vóór beoordeling door Directeur.",
  "priority": "High",
  "deadline_days": 2,
  "assign_to": "Finance_Manager",
  "task_category": "High-Value Approval",
  "next_task": "Director_Approval"
}
```

**Taak 2: Directeur Goedkeuring (Aangemaakt na voltooiing Taak 1)**
```json
{
  "task_type": "Second Approval",
  "task_title": "Definitieve Goedkeuring: Factuur {{DOCUMENT_NUMBER}} - €{{Total_Amount}}",
  "task_description": "DEFINITIEVE GOEDKEURING VEREIST\n\nLeverancier: {{Supplier_Name}}\nBedrag: €{{Total_Amount}}\n\nEerste goedkeuring: Voltooid door {{Task1_Approver}} op {{Task1_Date}}\n\nUw definitieve goedkeuring vereist.",
  "priority": "High",
  "deadline_days": 1,
  "assign_to": "Finance_Director",
  "task_category": "Final Approval",
  "prerequisite_task": "Manager_Approval"
}
```

---

### Stap 3: Wijs Taak Toe aan Gebruiker/Groep

**Kaart:** ACTION_ASSIGN_TO_USER of ACTION_ASSIGN_TO_GROUP

**Optie 1: Toewijzen aan Specifieke Gebruiker**
```
Gebruiker: John.Smith@company.com
OF
Gebruikersveld: {{DOCUMENT_FIELD:Approving_Manager}}
```

**Optie 2: Toewijzen aan Groep**
```
Groep: Finance Managers
Toewijzingsmodus: Eerst Beschikbaar
OF
Toewijzingsmodus: Round Robin
OF
Toewijzingsmodus: Alle (iedereen in groep krijgt taak)
```

**Optie 3: Sequentiële Toewijzing**
```
Kaart: ACTION_ASSIGN_SEQUENTIALLY_TO_USER

Gebruiker 1: Finance_Manager
Gebruiker 2: Finance_Director (alleen als Gebruiker 1 goedkeurt)
Gebruiker 3: CFO (alleen als Gebruiker 2 goedkeurt)
```

**Gidsreferentie:** [Toewijzingsgebruikersgids](../then/assignee/assignment-user-guide.md)

---

### Stap 4: Stuur E-mailmelding

**Kaart:** ACTION_SEND_EMAIL_TO_GROUPS

**Configuratie:**
```json
{
  "recipients": [
    "{{TASK_ASSIGNEE_EMAIL}}",
    "finance-notifications@company.com"
  ],
  "subject": "Nieuwe Taak Toegewezen: Keur Factuur {{DOCUMENT_NUMBER}} Goed",
  "body": "Beste {{TASK_ASSIGNEE_NAME}},\n\nEen nieuwe goedkeuringstaak is aan u toegewezen:\n\nTaak: Keur Factuur {{DOCUMENT_NUMBER}} Goed\nLeverancier: {{Supplier_Name}}\nBedrag: €{{Total_Amount}}\nDeadline: {{TASK_DEADLINE}}\nPrioriteit: {{TASK_PRIORITY}}\n\nLog in op DocBits om te beoordelen en goed te keuren:\n{{DOCUMENT_LINK}}\n\nMet vriendelijke groet,\nDocBits Automatisering"
}
```

**E-mailvariabelen:**
- `{{TASK_ASSIGNEE_EMAIL}}` - E-mail van taaktoegewezene
- `{{TASK_ASSIGNEE_NAME}}` - Naam van taaktoegewezene
- `{{DOCUMENT_NUMBER}}` - Document-ID
- `{{TASK_DEADLINE}}` - Taakvervaldatum
- `{{TASK_PRIORITY}}` - Taakprioriteitsniveau
- `{{DOCUMENT_LINK}}` - Directe link naar document

**Gidsreferentie:** [E-mail Verzenden Groepen Gids](../then/action/send-email-groups-guide.md)

---

### Stap 5: Volg Taakstatus

**Kaart:** CONDITION_TASK_STATUS of vergelijkbare taakstatuscontrole

**Configuratie:**
```
Taak-ID: {{CREATED_TASK_ID}}
Statuscontrole: IS VOLTOOID
```

**Statusopties:**
- CREATED - Taak net aangemaakt
- ASSIGNED - Taak toegewezen aan gebruiker
- IN_PROGRESS - Gebruiker begonnen met taak
- COMPLETED - Taak voltooid
- APPROVED - Taak goedgekeurd
- REJECTED - Taak afgewezen
- CANCELLED - Taak geannuleerd
- OVERDUE - Taak over datum

**Logica:**
```
ALS TAAKSTATUS = VOLTOOID EN TAAKRESULTAAT = GOEDGEKEURD:
  → Ga door naar volgende stap (of volgend goedkeuringsniveau)
  → Update documentstatus
  → Log goedkeuring

ALS TAAKSTATUS = VOLTOOID EN TAAKRESULTAAT = AFGEWEZEN:
  → Stop workflow
  → Stuur afwijzingsmelding
  → Maak beoordelingstaak voor correcties

ALS TAAKSTATUS = OVERDUE:
  → Escaleer naar manager
  → Stuur herinneringsmail
  → Maak escalatietaak
```

---

### Stap 6: Voltooi Workflow op Basis van Taakresultaat

**Na Taakvoltooiing:**

**Scenario A: Taak Goedgekeurd**
```
1. Stel veld "Approval_Status" in op "APPROVED"
2. Stel veld "Approved_By" in op {{TASK_COMPLETED_BY}}
3. Stel veld "Approval_Date" in op {{TASK_COMPLETED_DATE}}
4. ACTION_APPROVE_DOCUMENT
5. Exporteer document (indien geconfigureerd)
```

**Scenario B: Taak Afgewezen**
```
1. Stel veld "Approval_Status" in op "REJECTED"
2. Stel veld "Rejected_By" in op {{TASK_COMPLETED_BY}}
3. Stel veld "Rejection_Reason" in op {{TASK_REJECTION_REASON}}
4. ACTION_REJECT_DOCUMENT
5. Stuur afwijzingsmelding naar leverancier
6. Maak "Correctie Nodig" taak
```

**Scenario C: Taak Over Datum**
```
1. Stel veld "Task_Status" in op "OVERDUE"
2. Maak escalatietaak voor manager
3. Stuur herinneringsmail naar oorspronkelijke toegewezene
4. Stuur escalatiemail naar manager
5. Log gebeurtenis over datum
```

---

## Compleet Workflow Diagram

```
FACTUUR KOMT AAN
│
├─ CONTROLEER BEDRAG
│  │
│  ├─ Bedrag < €1.000 ✅
│  │  │
│  │  ├─ Stel Approval_Type = "AUTO"
│  │  └─ Document Automatisch Goedkeuren
│  │     → EINDE (Goedgekeurd)
│  │
│  ├─ Bedrag €1.000-€10.000 ⚠️
│  │  │
│  │  ├─ MAAK TAAK: Manager Goedkeuring
│  │  │  - Titel: "Keur Factuur Goed"
│  │  │  - Prioriteit: Gemiddeld
│  │  │  - Deadline: 3 dagen
│  │  │  │
│  │  │  ├─ TOEWIJZEN AAN: Finance Manager
│  │  │  │
│  │  │  ├─ STUUR EMAIL: Melding
│  │  │  │
│  │  │  ├─ WACHT OP TAAKVOLTOOIING
│  │  │  │  │
│  │  │  │  ├─ TAAK GOEDGEKEURD ✅
│  │  │  │  │  │
│  │  │  │  │  ├─ Stel Approval_Status = "APPROVED"
│  │  │  │  │  └─ Keur Document Goed
│  │  │  │  │     → EINDE (Goedgekeurd)
│  │  │  │  │
│  │  │  │  ├─ TAAK AFGEWEZEN ❌
│  │  │  │  │  │
│  │  │  │  │  ├─ Stel Approval_Status = "REJECTED"
│  │  │  │  │  ├─ Wijs Document Af
│  │  │  │  │  └─ Maak Correctietaak
│  │  │  │  │     → EINDE (Afgewezen)
│  │  │  │  │
│  │  │  │  └─ TAAK OVER DATUM ⏰
│  │  │  │     │
│  │  │  │     ├─ Stuur Herinneringsmail
│  │  │  │     ├─ Escaleer naar Directeur
│  │  │  │     └─ Maak Escalatietaak
│  │  │  │        → WACHT (Geëscaleerd)
│  │  │  │
│  │  │  └─ [Taak volgen actief]
│  │  │
│  │  └─ [Manager goedkeuring pad]
│  │
│  └─ Bedrag > €10.000 🚨
│     │
│     ├─ MAAK TAAK 1: Manager Eerste Goedkeuring
│     │  - Titel: "URGENT: Eerste Goedkeuring"
│     │  - Prioriteit: Hoog
│     │  - Deadline: 2 dagen
│     │  │
│     │  ├─ TOEWIJZEN AAN: Finance Manager
│     │  ├─ STUUR EMAIL: Melding Hoge Prioriteit
│     │  │
│     │  ├─ WACHT OP TAAK 1 VOLTOOIING
│     │  │  │
│     │  │  ├─ TAAK 1 GOEDGEKEURD ✅
│     │  │  │  │
│     │  │  │  ├─ MAAK TAAK 2: Directeur Definitieve Goedkeuring
│     │  │  │  │  - Titel: "Definitieve Goedkeuring Vereist"
│     │  │  │  │  - Prioriteit: Hoog
│     │  │  │  │  - Deadline: 1 dag
│     │  │  │  │  │
│     │  │  │  │  ├─ TOEWIJZEN AAN: Finance Director
│     │  │  │  │  ├─ STUUR EMAIL: Melding Definitieve Goedkeuring
│     │  │  │  │  │
│     │  │  │  │  ├─ WACHT OP TAAK 2 VOLTOOIING
│     │  │  │  │  │  │
│     │  │  │  │  │  ├─ TAAK 2 GOEDGEKEURD ✅
│     │  │  │  │  │  │  │
│     │  │  │  │  │  │  ├─ Stel Dual_Approval = "COMPLETE"
│     │  │  │  │  │  │  └─ Keur Document Goed
│     │  │  │  │  │  │     → EINDE (Dubbel Goedgekeurd)
│     │  │  │  │  │  │
│     │  │  │  │  │  └─ TAAK 2 AFGEWEZEN ❌
│     │  │  │  │  │     │
│     │  │  │  │  │     ├─ Wijs Document Af
│     │  │  │  │  │     └─ Meld Alle Partijen
│     │  │  │  │  │        → EINDE (Definitief Afgewezen)
│     │  │  │  │  │
│     │  │  │  │  └─ [Taak 2 volgen]
│     │  │  │  │
│     │  │  │  └─ [Taak 2 aangemaakt]
│     │  │  │
│     │  │  └─ TAAK 1 AFGEWEZEN ❌
│     │  │     │
│     │  │     ├─ Wijs Document Af (Geen Taak 2 aangemaakt)
│     │  │     └─ Meld Leverancier
│     │  │        → EINDE (Eerste Afgewezen)
│     │  │
│     │  └─ [Taak 1 volgen]
│     │
│     └─ [Dubbel goedkeuring pad]
│
└─ [Bedragcontrole voltooid]
```

---

## Configuratiesjablonen

### Sjabloon 1: Eenvoudige Goedkeuringstaak

```json
{
  "card": "tasks_create",
  "task_title": "Keur {{DOCUMENT_TYPE}} {{DOCUMENT_NUMBER}} Goed",
  "task_description": "Beoordeel en keur dit document goed.",
  "priority": "Medium",
  "deadline_days": 3,
  "assign_to": "approver@company.com",
  "category": "Approval"
}
```

---

### Sjabloon 2: Beoordelingstaak met Details

```json
{
  "card": "tasks_create",
  "task_title": "Beoordeel Uitzondering: {{EXCEPTION_TYPE}}",
  "task_description": "Document: {{DOCUMENT_NUMBER}}\nUitzondering: {{EXCEPTION_REASON}}\n\nDetails:\n- Leverancier: {{Supplier_Name}}\n- Bedrag: €{{Total_Amount}}\n- Datum: {{Document_Date}}\n\nVereiste Actie: Beoordeel en los uitzondering op",
  "priority": "High",
  "deadline_days": 1,
  "assign_to_group": "Exceptions Team",
  "category": "Exception Handling"
}
```

---

### Sjabloon 3: Escalatietaak

```json
{
  "card": "tasks_create",
  "task_title": "ESCALATIE: {{ORIGINAL_TASK_TITLE}}",
  "task_description": "GEËSCALEERDE TAAK\n\nOriginele Taak: {{ORIGINAL_TASK_ID}}\nOorspronkelijke Toegewezene: {{ORIGINAL_ASSIGNEE}}\nDeadline Verstreken: {{ORIGINAL_DEADLINE}}\nDagen Over Datum: {{DAYS_OVERDUE}}\n\nBeoordeel en onderneem onmiddellijk actie.",
  "priority": "Urgent",
  "deadline_days": 1,
  "assign_to": "manager@company.com",
  "category": "Escalation",
  "parent_task": "{{ORIGINAL_TASK_ID}}"
}
```

---

## Geavanceerde Patronen

### Patroon 1: Sequentiële Goedkeuring op Meerdere Niveaus

**Gebruik:** Facturen moeten door meerdere goedkeurders in volgorde

```
Niveau 1: Accounts Clerk (gegevens verifiëren)
  → INDIEN GOEDGEKEURD:
    Niveau 2: Accounts Manager (bedrag goedkeuren)
      → INDIEN GOEDGEKEURD:
        Niveau 3: Financieel Directeur (definitieve aftekening)
          → INDIEN GOEDGEKEURD:
            Document Goedgekeurd ✅
```

**Implementatie:**
```
1. Maak Taak 1 voor Clerk
2. Wacht op voltooiing Taak 1
3. ALS Taak 1 = GOEDGEKEURD:
     Maak Taak 2 voor Manager
4. Wacht op voltooiing Taak 2
5. ALS Taak 2 = GOEDGEKEURD:
     Maak Taak 3 voor Directeur
6. Wacht op voltooiing Taak 3
7. ALS Taak 3 = GOEDGEKEURD:
     Keur Document Goed
```

---

### Patroon 2: Parallelle Multi-Goedkeurder

**Gebruik:** Meerdere mensen moeten tegelijkertijd goedkeuren

```
Stuur naar ALLE goedkeurders tegelijk:
- Financieel Manager
- Inkoopmanager
- Kwaliteitsmanager

Document alleen goedgekeurd wanneer ALLEN goedkeuren
```

**Implementatie:**
```
1. Maak 3 taken tegelijkertijd
2. Volg alle 3 taakstatussen
3. WACHT tot ALLE taken voltooid zijn
4. ALS allen = GOEDGEKEURD:
     Keur Document Goed
   ANDERS:
     Wijs Document Af
```

---

### Patroon 3: Voorwaardelijke Taakcreatie

**Gebruik:** Maak verschillende taken op basis van voorwaarden

```
ALS Leverancier = "Nieuw":
  → Maak "Nieuwe Leverancier Beoordeling" taak
ANDERS ALS Bedrag > €50.000:
  → Maak "Hoge Waarde Goedkeuring" taak
ANDERS ALS Document fouten heeft:
  → Maak "Foutcorrectie" taak
ANDERS:
  → Maak "Standaard Goedkeuring" taak
```

---

### Patroon 4: Op Deadline Gebaseerde Escalatie

**Gebruik:** Automatisch escaleren als taak niet op tijd voltooid is

```
Dag 0: Maak taak voor Gebruiker A (3-daagse deadline)
Dag 3: ALS niet voltooid:
         → Stuur herinnering naar Gebruiker A
Dag 4: ALS nog steeds niet voltooid:
         → Maak escalatietaak voor Manager B
         → Meld zowel Gebruiker A als Manager B
Dag 5: ALS nog steeds niet voltooid:
         → Maak urgente taak voor Directeur C
         → Melding hoge prioriteit
```

---

## Foutafhandeling

### Scenario 1: Toegewezene Niet Gevonden

**Probleem:** Gebruiker bestaat niet of is inactief

**Oplossing:**
```
1. Controleer gebruikersstatus met CONDITION_USER_IS_ISNOT
2. ALS Gebruiker = INACTIEF:
     → Wijs toe aan back-up gebruiker
     → OF Wijs toe aan gebruikersgroep
     → Log waarschuwing
3. Stuur melding naar admin
```

---

### Scenario 2: Taakcreatie Mislukt

**Probleem:** Systeemfout bij maken van taak

**Oplossing:**
```
1. Controleer status taakcreatie
2. ALS Mislukt:
     → Probeer taakcreatie opnieuw
     → Stuur in plaats daarvan e-mailmelding
     → Maak admin-waarschuwingstaak
     → Log foutdetails
```

---

### Scenario 3: Geen Reactie op Taak

**Probleem:** Gebruiker voltooit taak niet voor deadline

**Oplossing:**
```
1. Monitor taakdeadline
2. Dag voor deadline:
     → Stuur herinneringsmail
3. Op deadlinedag:
     → Stuur urgente herinnering
4. Na deadline:
     → Maak escalatietaak
     → Meld manager
     → Log gebeurtenis over datum
```

---

## Testchecklist

- [ ] Taak succesvol aangemaakt
- [ ] Taak toegewezen aan juiste gebruiker/groep
- [ ] E-mailmelding verzonden
- [ ] Taak verschijnt in takenlijst van gebruiker
- [ ] Taakeigenschappen correct (titel, beschrijving, prioriteit, deadline)
- [ ] Gebruiker kan taak voltooien
- [ ] Workflow gaat verder na taakvoltooiing
- [ ] Goedkeuringsworkflow werkt correct
- [ ] Afwijzingsworkflow werkt correct
- [ ] Escalatie triggert op juiste moment
- [ ] Afhandeling over datum werkt
- [ ] Alle e-mailmeldingen verzonden
- [ ] Veldupdates werken correct

---

## Praktijkvoorbeelden

### Voorbeeld 1: Drieweg PO Matching Uitzondering

**Scenario:** Factuur komt niet overeen met PO, beoordeling nodig

```
1. PO Matching mislukt (prijsvariantie > 5%)
2. Maak Taak: "Beoordeel PO Mismatch"
   - Toewijzen aan: Inkoopfunctionaris
   - Prioriteit: Hoog
   - Beschrijving: Inclusief variantiedetails
3. Stuur e-mail met vergelijkingstabel
4. Wacht op taakvoltooiing
5. INDIEN Goedgekeurd: Ga door met verwerking
   INDIEN Afgewezen: Retourneer naar leverancier
```

---

### Voorbeeld 2: Leveranciersfactuur Goedkeuring

**Scenario:** Nieuwe leveranciersfactuur vereist speciale goedkeuring

```
1. Controleer of leverancier nieuw is (< 6 maanden oud)
2. INDIEN Nieuw:
     Maak Taak: "Nieuwe Leverancier Factuur Beoordeling"
     - Toewijzen aan: Inkoopmanager
     - Inclusief leveranciersdetails
     - Vereis leveranciersverificatie
3. Na goedkeuring:
     Voeg toe aan lijst goedgekeurde leveranciers
     Ga door met normale workflow
```

---

### Voorbeeld 3: Maandeindverwerking

**Scenario:** Maandeindfacturen vereisen urgente verwerking

```
1. Controleer of documentdatum in laatste 3 dagen van de maand valt
2. INDIEN Ja:
     Maak Taak: "URGENT: Maandeindfactuur"
     - Prioriteit: Urgent
     - Deadline: 1 dag
     - Toewijzen aan: Financieel Team (alle leden)
     - Markeer voor versnelde verwerking
3. Stuur urgente e-mailmelding
4. Volg voltooiing
```

---

## Prestatietips

✅ **Beste Praktijken:**
- Stel realistische deadlines in
- Gebruik duidelijke taaktitels en beschrijvingen
- Neem alle benodigde informatie op in de taak
- Stuur tijdige meldingen
- Monitor taakvoltooiingspercentages
- Escaleer taken over datum automatisch
- Log alle taakactiviteiten
- Beoordeel taakpatronen maandelijks

❌ **Vermijden:**
- Taken maken voor alles
- Vage taakbeschrijvingen
- Onrealistische deadlines
- Te veel meldingsmails
- Geen escalatiepad
- Taken over datum negeren
- Taakmetrieken niet volgen

---

## Gerelateerde Patronen

### Patronen Die Goed Samenwerken:

- **[API Integratie Patroon](api-integration-pattern.md)** - Maak taken voor API-fouten
- **[PO Matching Patroon](po-matching-pattern.md)** - Maak taken voor PO-mismatches
- **[Beslissingslogica Patroon](decision-logic-pattern.md)** - Routeer naar geschikt taaktype
- **[Gegevenstransformatie Patroon](data-transformation-pattern.md)** - Transformeer gegevens vóór maken van taak

---

## Gerelateerde Gidsen

### Vereisten
- [Taaktoewijzingsgids](../then/task/task-assignment-guide.md) - Taakkaartdocumentatie
- [Toewijzingsgebruikersgids](../then/assignee/assignment-user-guide.md) - Gebruikerstoewijzing
- [E-mail Verzenden Groepen Gids](../then/action/send-email-groups-guide.md) - E-mailmeldingen

### Gerelateerde Kaarten
- **tasks_create** - [Taaktoewijzingsgids](../then/task/task-assignment-guide.md)
- **ACTION_ASSIGN_TO_USER** - [Toewijzingsgids](../then/assignee/assignment-user-guide.md)
- **ACTION_SEND_EMAIL_TO_GROUPS** - [E-mailgids](../then/action/send-email-groups-guide.md)
- **CONDITION_TASK_STATUS** - [Gids Conditiekaarten](../and/condition-cards-complete-guide.md)

### Volgende Stappen
- Voeg e-mailmeldingen toe: [E-mail Verzenden Gids](../then/action/send-email-groups-guide.md)
- Implementeer complexe routering: [Beslissingslogica Patroon](decision-logic-pattern.md)
- Handel fouten af: [Foutafhandeling Patroon](error-handling-pattern.md)

---

**Patroonversie:** 1.0
**Laatst Bijgewerkt:** 23 oktober 2025
**Moeilijkheidsgraad:** Laag-Gemiddeld
**Geschatte Tijd:** 30-45 minuten
**Succespercentage:** Hoog (wanneer correct geconfigureerd)
