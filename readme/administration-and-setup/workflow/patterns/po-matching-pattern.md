# PO Matching Patroon

**Patroontype:** Validatie & Vergelijking
**Complexiteit:** Gemiddeld-Hoog
**Geschatte Insteltijd:** 60-90 minuten
**Veelvoorkomende Gebruiksscenario's:** Driewegmatching, factuurvalidatie, variantiecontrole, tolerantiebeheer

---

## Patroonoverzicht

Dit patroon demonstreert hoe u uitgebreide workflows voor het matchen van inkooporders (PO) in DocBits kunt implementeren. PO-matching is een kritisch controleproces dat factuurgegevens vergelijkt met inkoopordergegevens om discrepanties te detecteren vóór goedkeuring van de betaling.

**Wat Dit Patroon Doet:**
1. Haalt PO-gegevens op basis van PO-nummer van factuur
2. Vergelijkt factuurregelitems met PO-regelitems
3. Berekent varianties (prijs, hoeveelheid, totalen)
4. Past tolerantieregels toe
5. Routeert voor goedkeuring of escalatie op basis van matchresultaten
6. Houdt matchinggeschiedenis en uitzonderingen bij

---

## Wanneer Dit Patroon Te Gebruiken

Gebruik dit patroon wanneer u het volgende moet doen:
- ✅ Facturen valideren tegen inkooporders
- ✅ Prijsfouten detecteren vóór betaling
- ✅ Hoeveelheidsverschillen identificeren
- ✅ Inkoopcontroles afdwingen
- ✅ Dubbele betalingen voorkomen
- ✅ Driewegmatching automatiseren
- ✅ Handmatige factuurbeoordelingswerklast verminderen

**Gebruik dit patroon niet wanneer:**
- ❌ Er geen PO bestaat voor de factuur (niet-PO-facturen)
- ❌ PO-gegevens niet beschikbaar zijn in DocBits
- ❌ Handmatige beoordeling de voorkeur heeft boven automatisering
- ❌ PO-matching niet vereist is door bedrijfsbeleid

---

## PO Matching Begrijpen

### De Driewegmatch

**Traditionele inkoopcontrole:**
```
Inkooporder (PO)     →  Aangemaakt bij bestellen
        ↓
Goederenontvangst (GR) →  Aangemaakt bij ontvangst
        ↓
Factuur              →  Aangemaakt door leverancier

DRIEWEGMATCH = PO + GR + Factuur komen allemaal overeen
```

**DocBits Implementatie (Tweewegmatch):**
```
Inkooporder (PO)     →  Geïmporteerd naar DocBits
        ↓
Factuur              →  Gescand door DocBits
        ↓
VERGELIJKING         →  Factuur vs PO validatie
```

---

## Variantieberekeningsformules

### Eenheidsprijsvariantie

**Formule:**
```
Variantie % = |(Factuur Eenheidsprijs - PO Eenheidsprijs)| / PO Eenheidsprijs × 100
```

**Voorbeeld:**
```
PO Eenheidsprijs:       €100,00
Factuur Eenheidsprijs:  €103,00

Variantie = |103 - 100| / 100 × 100
        = 3 / 100 × 100
        = 3%

Tolerantie: 5%
Resultaat: 3% ≤ 5% → PASS ✅
```

---


### Hoeveelheidsvariantie

**Formule:**
```
Variantie % = |(Factuur Hoeveelheid - PO Hoeveelheid)| / PO Hoeveelheid × 100
```

**Voorbeeld:**
```
PO Hoeveelheid:        100 stuks
Factuur Hoeveelheid:   98 stuks

Variantie = |98 - 100| / 100 × 100
        = 2 / 100 × 100
        = 2%

Tolerantie: 10%
Resultaat: 2% ≤ 10% → PASS ✅
```

---


### Totaalbedragvariantie

**Formule:**
```
Variantie % = |(Factuur Totaal - PO Totaal)| / PO Totaal × 100
```

**Voorbeeld:**
```
PO Totaal:       €10.000,00
Factuur Totaal:  €10.450,00

Variantie = |10450 - 10000| / 10000 × 100
        = 450 / 10000 × 100
        = 4,5%

Tolerantie: 5%
Resultaat: 4,5% ≤ 5% → PASS ✅
```

---


## Compleet Workflowvoorbeeld

### Scenario: Factuurvalidatie met Op Tolerantie Gebaseerde Routering

**Bedrijfsvereiste:**
- Alle facturen met PO-referentie moeten worden gevalideerd
- Prijsvariantietolerantie: 5%
- Hoeveelheidsvariantietolerantie: 10%
- Totaalbedragvariantietolerantie: 3%
- Binnen tolerantie: Automatisch goedkeuren
- Buiten tolerantie: Maak beoordelingstaak
- Ontbrekende PO: Escaleren naar inkoop

**Gebruikte Workflowkaarten:**
1. CONDITION_DOC_FIELD_EXISTS - Controleer of PO-nummer aanwezig is
2. PURCHASE_ORDER_FULL_MATCH - Probeer volledige match
3. CONDITION_DOC_TO_PO_UNIT_PRICE - Controleer prijsvariantie
4. CONDITION_DOC_TO_PO_QUANTITY - Controleer hoeveelheidsvariantie
5. CONDITION_DOC_TO_PO_TAX_LINES - Controleer belastingafstemming
6. ACTION_SET_FIELD_TO_TEXT - Sla matchresultaten op
7. tasks_create - Maak beoordelingstaken
8. ACTION_SEND_EMAIL_TO_GROUPS - Stuur meldingen

---


## Stap-voor-Stap Implementatie

### Stap 1: Controleer op PO-referentie

**Kaart:** CONDITION_DOC_FIELD_EXISTS of CONDITION_DOC_FIELD_CONTAINS

**Configuratie:**
```
Veld: PO_Number
Operator: IS NIET LEEG
```

**Logica:**
```
ALS PO_Nummer bestaat:
  → Ga door naar PO-matching
ANDERS:
  → Routeer naar "Niet-PO Factuur" workflow
  → Maak handmatige beoordelingstaak
  → Sla PO-matching over
```

**Gidsreferentie:** [Gids Conditiekaarten](../and/condition-cards-complete-guide.md)

---


### Stap 2: Haal PO-gegevens Op

**Automatisch in DocBits:**
- Systeem zoekt PO op via PO_Number veld
- Haalt PO-regelitems op
- Maakt gegevens beschikbaar voor vergelijking

**Handmatige Configuratie (indien nodig):**
```
PO Bron: DocBits Master Data
PO Opzoekveld: PO_Number
Matchtype: Exacte Match
Inclusief Gesloten PO's: Nee (of Ja indien beleid toestaat)
```

---


### Stap 3: Volledige PO Match Controle

**Kaart:** PURCHASE_ORDER_FULL_MATCH

**Doel:** Snelle controle of alles perfect overeenkomt

**Configuratie:**
```
Matchniveau: Volledige Match
Inclusief: Alle regelitems, prijzen, hoeveelheden, totalen
Tolerantie: Geen (exacte match)
```

**Logica:**
```
ALS Volledige Match = WAAR:
  → Stel "PO_Match_Status" = "FULL MATCH"
  → Document automatisch goedkeuren
  → Gedetailleerde controles overslaan
  → EINDE ✅

ALS Volledige Match = ONWAAR:
  → Ga door naar gedetailleerde variantiecontroles
  → Identificeer specifieke varianties
```

**Resultaat:**
- **WAAR**: Perfecte match, automatisch goedkeuren
- **ONWAAR**: Ga door naar gedetailleerde controles

---


### Stap 4: Controleer Eenheidsprijsvariantie

**Kaart:** CONDITION_DOC_TO_PO_UNIT_PRICE (v5 aanbevolen)

**Configuratie:**
```
Vergelijkingsmodus: Percentage Variantie
Tolerantie: 5%
Operator: Variantie is Kleiner Dan of Gelijk Aan
Toepassen Op: Alle regelitems
```

**Stap-voor-Stap:**
```
Voor elk regelitem:
  1. Haal Factuur Eenheidsprijs op
  2. Haal PO Eenheidsprijs op (gematcht op productcode)
  3. Bereken: Variantie % = |Factuur - PO| / PO × 100
  4. Controleer: Variantie % ≤ 5%?
  5. Sla resultaat op
```

**Voorbeeldberekening:**
```
Regelitem 1:
  Product: ABC123
  Factuurprijs: €52,00
  PO Prijs: €50,00
  Variantie = |52-50|/50 × 100 = 4%
  Tolerantie: 5%
  Resultaat: PASS ✅

Regelitem 2:
  Product: XYZ789
  Factuurprijs: €120,00
  PO Prijs: €100,00
  Variantie = |120-100|/100 × 100 = 20%
  Tolerantie: 5%
  Resultaat: FAIL ❌

Algemeen Resultaat: FAIL (een of meer items mislukt)
```

**Gidsreferentie:** [PO Matching Complete Gids - Eenheidsprijs](../and/compare-with-purchase-order/po-matching-complete-guide.md#unit-price-comparison)

---


### Stap 5: Controleer Hoeveelheidsvariantie

**Kaart:** CONDITION_DOC_TO_PO_QUANTITY

**Configuratie:**
```
Vergelijkingsmodus: Percentage Variantie
Tolerantie: 10%
Operator: Variantie is Kleiner Dan of Gelijk Aan
Toepassen Op: Alle regelitems
Onderlevering Toestaan: Ja (binnen tolerantie)
Overlevering Toestaan: Nee (strikt)
```

**Logica:**
```
Voor elk regelitem:
  1. Haal Factuur Hoeveelheid op
  2. Haal PO Hoeveelheid op
  3. Bereken: Variantie % = |Factuur - PO| / PO × 100
  4. Controleer: Variantie % ≤ 10%?
  5. Speciale regels:
     - Onderlevering: Toestaan binnen tolerantie
     - Overlevering: Afwijzen (of striktere tolerantie toepassen)
```

**Voorbeeld:**
```
Regelitem 1:
  Product: ABC123
  Factuur Aantal: 98 stuks
  PO Aantal: 100 stuks
  Variantie = |98-100|/100 × 100 = 2%
  Onderlevering: 2% (binnen 10% tolerantie)
  Resultaat: PASS ✅

Regelitem 2:
  Product: XYZ789
  Factuur Aantal: 115 stuks
  PO Aantal: 100 stuks
  Variantie = |115-100|/100 × 100 = 15%
  Overlevering: 15% (overschrijdt 10% tolerantie)
  Resultaat: FAIL ❌ (Escaleren)
```

**Gidsreferentie:** [PO Matching Complete Gids - Hoeveelheid](../and/compare-with-purchase-order/po-matching-complete-guide.md#quantity-comparison)

---


### Stap 6: Controleer Belastingregels Afstemming

**Kaart:** CONDITION_DOC_TO_PO_TAX_LINES

**Configuratie:**
```
Match Belastingcodes: Ja
Match Belastingtarieven: Ja
Match Belastingbedragen: Met 1% tolerantie
Belastingberekening: Verifieer herberekening
```

**Validatie:**
```
1. Controleer of belastingcodes overeenkomen (bijv. "BTW19" op beide)
2. Controleer of belastingtarieven overeenkomen (19% op beide)
3. Verifieer belastingbedragberekening:
   Belastingbedrag = Netto Bedrag × Belastingtarief
4. Sta kleine afrondingsverschillen toe
```

**Voorbeeld:**
```
Factuur:
  Netto Bedrag: €100,00
  Belastingtarief: 19%
  Belastingbedrag: €19,00
  Totaal: €119,00

PO:
  Netto Bedrag: €100,00
  Belastingtarief: 19%
  Belastingbedrag: €19,00
  Totaal: €119,00

Resultaat: Belastingafstemming PASS ✅
```

---


### Stap 7: Sla Matchresultaten Op

**Kaart:** ACTION_SET_FIELD_TO_TEXT (meerdere instanties)

**Configuratie:**

**Veld 1: PO_Match_Status**
```
Veld: PO_Match_Status
Waarde: {{CALCULATED}}
Opties: "FULL MATCH" | "WITHIN TOLERANCE" | "OUT OF TOLERANCE" | "NO MATCH"
```

**Veld 2: Price_Variance_Percent**
```
Veld: Price_Variance_Percent
Waarde: {{CALCULATED_PRICE_VARIANCE}}
Formaat: "4,5%" (voorbeeld)
```

**Veld 3: Quantity_Variance_Percent**
```
Veld: Quantity_Variance_Percent
Waarde: {{CALCULATED_QUANTITY_VARIANCE}}
Formaat: "2,0%" (voorbeeld)
```

**Veld 4: Match_Details**
```
Veld: Match_Details
Waarde: "Prijsvariantie: 4,5% (binnen 5% tolerantie)\nHoeveelheidsvariantie: 2,0% (binnen 10% tolerantie)\nTotaal: PASS"
```

**Gidsreferentie:** [Gids Veldmanipulatie](../then/document-field/field-manipulation-guide.md)

---


### Stap 8: Routeer op Basis van Matchresultaten

**Scenario A: Perfecte Match (Volledige Match)**
```
ALS PO_Match_Status = "FULL MATCH":
  1. Stel Approval_Status = "AUTO APPROVED"
  2. Stel Match_Type = "FULL"
  3. ACTION_APPROVE_DOCUMENT
  4. Exporteer naar ERP
  5. Stuur bevestigingsmail
  → EINDE ✅
```

**Scenario B: Binnen Tolerantie**
```
ALS PO_Match_Status = "WITHIN TOLERANCE":
  1. Stel Approval_Status = "AUTO APPROVED"
  2. Stel Match_Type = "TOLERANCE"
  3. Log variantiedetails
  4. ACTION_APPROVE_DOCUMENT
  5. Exporteer naar ERP
  → EINDE ✅
```

**Scenario C: Buiten Tolerantie (Klein)**
```
ALS Variantie < 15% (kleine uitzonderingen):
  1. Stel Match_Status = "REVIEW REQUIRED"
  2. Maak Taak: "Beoordeel PO Variantie"
     - Toewijzen aan: Crediteurenadministratie
     - Prioriteit: Gemiddeld
     - Deadline: 3 dagen
  3. Stuur e-mail met variantiedetails
  4. Wacht op taakvoltooiing
  5. INDIEN Goedgekeurd: Ga door met verwerking
     INDIEN Afgewezen: Retourneer naar leverancier
```

**Scenario D: Buiten Tolerantie (Groot)**
```
ALS Variantie ≥ 15% (grote uitzonderingen):
  1. Stel Match_Status = "ESCALATION REQUIRED"
  2. Maak Taak: "URGENT: Grote PO Variantie"
     - Toewijzen aan: Inkoopmanager
     - Prioriteit: Hoog
     - Deadline: 1 dag
  3. Stuur urgente e-mail naar:
     - Inkoopmanager
     - Financieel Manager
     - Leverancierscontact
  4. Blokkeer document voor verwerking
  5. Wacht op resolutie
```

**Scenario E: Ontbrekende PO of Geen Match**
```
ALS PO niet gevonden OF geen items matchen:
  1. Stel Match_Status = "NO MATCH"
  2. Maak Taak: "PO Niet Gevonden"
     - Toewijzen aan: Inkoopteam
     - Prioriteit: Hoog
  3. Stuur e-mail naar inkoop
  4. Blokkeer document
  5. Vraag PO-creatie of correctie aan
```

---


## Compleet Workflow Diagram

```
FACTUUR KOMT AAN
│
├─ CONTROLEER: Heeft factuur PO-nummer?
│  │
│  ├─ GEEN PO NUMMER ❌
│  │  │
│  │  ├─ Stel Match_Status = "NO PO"
│  │  ├─ Routeer naar Niet-PO workflow
│  │  └─ Maak handmatige beoordelingstaak
│  │     → EINDE (Niet-PO Factuur)
│  │
│  └─ PO NUMMER BESTAAT ✅
│     │
│     ├─ HAAL PO GEGEVENS OP
│     │  - Zoek PO op via PO_Number
│     │  - Haal PO-regelitems op
│     │  - Haal PO-totalen op
│     │  │
│     │  ├─ PO GEVONDEN ✅
│     │  │  │
│     │  │  ├─ STAP 1: Controleer Volledige Match
│     │  │  │  Kaart: PURCHASE_ORDER_FULL_MATCH
│     │  │  │  │
│     │  │  │  ├─ VOLLEDIGE MATCH ✅✅✅
│     │  │  │  │  │
│     │  │  │  │  ├─ Stel Match_Status = "FULL MATCH"
│     │  │  │  │  ├─ Auto-Goedkeuren
│     │  │  │  │  └─ Exporteer naar ERP
│     │  │  │  │     → EINDE (Perfecte Match)
│     │  │  │  │
│     │  │  │  └─ GEEN VOLLEDIGE MATCH ⚠️
│     │  │  │     │
│     │  │  │     ├─ STAP 2: Controleer Eenheidsprijsvariantie
│     │  │  │     │  Kaart: CONDITION_DOC_TO_PO_UNIT_PRICE
│     │  │  │     │  Tolerantie: 5%
│     │  │  │     │  │
│     │  │  │     │  ├─ Bereken voor elke regel:
│     │  │  │     │  │  Variantie % = |Factuur-PO|/PO × 100
│     │  │  │     │  │
│     │  │  │     │  ├─ PRIJSVARIANTIE ≤ 5% ✅
│     │  │  │     │  │  Sla variantie op: 3,2% (voorbeeld)
│     │  │  │     │  │  Prijscontrole: PASS
│     │  │  │     │  │
│     │  │  │     │  └─ PRIJSVARIANTIE > 5% ❌
│     │  │  │     │     Sla variantie op: 12,5% (voorbeeld)
│     │  │  │     │     Prijscontrole: FAIL
│     │  │  │     │     → Markeer voor beoordeling
│     │  │  │     │
│     │  │  │     ├─ STAP 3: Controleer Hoeveelheidsvariantie
│     │  │  │     │  Kaart: CONDITION_DOC_TO_PO_QUANTITY
│     │  │  │     │  Tolerantie: 10%
│     │  │  │     │  │
│     │  │  │     │  ├─ Bereken voor elke regel:
│     │  │  │     │  │  Variantie % = |Factuur Aantal-PO Aantal|/PO Aantal × 100
│     │  │  │     │  │
│     │  │  │     │  ├─ HOEVEELHEIDSVARIANTIE ≤ 10% ✅
│     │  │  │     │  │  Sla variantie op: 2,0% (voorbeeld)
│     │  │  │     │  │  Hoeveelheidscontrole: PASS
│     │  │  │     │  │
│     │  │  │     │  └─ HOEVEELHEIDSVARIANTIE > 10% ❌
│     │  │  │     │     Sla variantie op: 15,0% (voorbeeld)
│     │  │  │     │     Hoeveelheidscontrole: FAIL
│     │  │  │     │     → Markeer voor beoordeling
│     │  │  │     │
│     │  │  │     ├─ STAP 4: Controleer Belastingregels
│     │  │  │     │  Kaart: CONDITION_DOC_TO_PO_TAX_LINES
│     │  │  │     │  │
│     │  │  │     │  ├─ BELASTING AFGESTEMD ✅
│     │  │  │     │  │  Belastingcontrole: PASS
│     │  │  │     │  │
│     │  │  │     │  └─ BELASTING MISMATCH ❌
│     │  │  │     │     Belastingcontrole: FAIL
│     │  │  │     │     → Markeer voor beoordeling
│     │  │  │     │
│     │  │  │     ├─ EVALUEER RESULTATEN
│     │  │  │     │  │
│     │  │  │     │  ├─ ALLE CONTROLES PASS ✅
│     │  │  │     │  │  (Binnen tolerantie)
│     │  │  │     │  │  │
│     │  │  │     │  │  ├─ Stel Match_Status = "WITHIN TOLERANCE"
│     │  │  │     │  │  ├─ Log variantiedetails
│     │  │  │     │  │  ├─ Auto-Goedkeuren
│     │  │  │     │  │  └─ Exporteer naar ERP
│     │  │  │     │  │     → EINDE (Goedgekeurd met Variantie)
│     │  │  │     │  │
│     │  │  │     │  ├─ KLEINE FALEN (Variantie < 15%) ⚠️
│     │  │  │     │  │  │
│     │  │  │     │  │  ├─ Stel Match_Status = "REVIEW REQUIRED"
│     │  │  │     │  │  ├─ Maak Beoordelingstaak
│     │  │  │     │  │  │  - Toewijzen aan: AP Officer
│     │  │  │     │  │  │  - Prioriteit: Gemiddeld
│     │  │  │     │  │  │  - Deadline: 3 dagen
│     │  │  │     │  │  ├─ Stuur e-mail met details
│     │  │  │     │  │  │
│     │  │  │     │  │  └─ WACHT OP TAAKVOLTOOIING
│     │  │  │     │  │     │
│     │  │  │     │  │     ├─ TAAK GOEDGEKEURD ✅
│     │  │  │     │  │     │  Goedkeuren & Exporteren
│     │  │  │     │  │     │  → EINDE (Handmatige Goedkeuring)
│     │  │  │     │  │     │
│     │  │  │     │  │     └─ TAAK AFGEWEZEN ❌
│     │  │  │     │  │        Afwijzen & Retourneren naar Leverancier
│     │  │  │     │  │        → EINDE (Afgewezen)
│     │  │  │     │  │
│     │  │  │     │  └─ GROTE FALEN (Variantie ≥ 15%) 🚨
│     │  │  │     │     │
│     │  │  │     │     ├─ Stel Match_Status = "ESCALATION"
│     │  │  │     │     ├─ Maak Urgente Taak
│     │  │  │     │     │  - Toewijzen aan: Inkoopmanager
│     │  │  │     │     │  - Prioriteit: Hoog
│     │  │  │     │     │  - Deadline: 1 dag
│     │  │  │     │     ├─ Stuur urgente e-mails naar:
│     │  │  │     │     │  * Inkoopmanager
│     │  │  │     │     │  * Financieel Manager
│     │  │  │     │     │  * Leverancier
│     │  │  │     │     ├─ Blokkeer documentverwerking
│     │  │  │     │     │
│     │  │  │     │     └─ WACHT OP RESOLUTIE
│     │  │  │     │        → EINDE (In Afwachting van Escalatie)
│     │  │  │     │
│     │  │  │     └─ [Variantiecontroles voltooid]
│     │  │  │
│     │  │  └─ [Volledige match controle voltooid]
│     │  │
│     │  └─ PO NIET GEVONDEN ❌
│     │     │
│     │     ├─ Stel Match_Status = "PO NOT FOUND"
│     │     ├─ Maak Taak: "Ontbrekende PO"
│     │     │  - Toewijzen aan: Inkoopteam
│     │     │  - Prioriteit: Hoog
│     │     ├─ Stuur e-mail naar inkoop
│     │     └─ Blokkeer document
│     │        → EINDE (Ontbrekende PO)
│     │
│     └─ [PO ophalen voltooid]
│
└─ [PO controle voltooid]
```

---


## Configuratiesjablonen

### Sjabloon 1: Standaard PO Matching (Conservatief)

```json
{
  "full_match_check": true,
  "price_variance": {
    "enabled": true,
    "tolerance_percent": 3,
    "tolerance_type": "percentage"
  },
  "quantity_variance": {
    "enabled": true,
    "tolerance_percent": 5,
    "tolerance_type": "percentage",
    "allow_under_delivery": true,
    "allow_over_delivery": false
  },
  "tax_validation": {
    "enabled": true,
    "match_tax_codes": true,
    "match_tax_rates": true,
    "tax_amount_tolerance": 0.5
  },
  "auto_approve": {
    "full_match": true,
    "within_tolerance": true
  },
  "escalation": {
    "threshold_percent": 10,
    "assign_to": "procurement_manager"
  }
}
```

**Gebruik:** Strikte controleomgeving, lage tolerantie voor variantie

---


### Sjabloon 2: Flexibele PO Matching (Mild)

```json
{
  "full_match_check": true,
  "price_variance": {
    "enabled": true,
    "tolerance_percent": 10,
    "tolerance_type": "percentage"
  },
  "quantity_variance": {
    "enabled": true,
    "tolerance_percent": 15,
    "tolerance_type": "percentage",
    "allow_under_delivery": true,
    "allow_over_delivery": true
  },
  "tax_validation": {
    "enabled": true,
    "match_tax_codes": false,
    "match_tax_rates": true,
    "tax_amount_tolerance": 2
  },
  "auto_approve": {
    "full_match": true,
    "within_tolerance": true
  },
  "escalation": {
    "threshold_percent": 20,
    "assign_to": "accounts_payable"
  }
}
```

**Gebruik:** Flexibele omgeving, vertrouwde leveranciers, hogere tolerantie

---


### Sjabloon 3: Alleen-Prijs Matching

```json
{
  "full_match_check": false,
  "price_variance": {
    "enabled": true,
    "tolerance_percent": 5,
    "tolerance_type": "percentage"
  },
  "quantity_variance": {
    "enabled": false
  },
  "tax_validation": {
    "enabled": false
  },
  "auto_approve": {
    "full_match": false,
    "within_tolerance": true
  }
}
```

**Gebruik:** Wanneer alleen prijs belangrijk is, hoeveelheidsvariaties verwacht

---


## Geavanceerde Scenario's

### Scenario 1: Afhandeling van Deelleveringen

**Uitdaging:** Factuur voor gedeeltelijke PO-levering

**Oplossing:**
```
1. Sta hoeveelheidsonderlevering toe binnen tolerantie
2. Volg cumulatieve gefactureerde hoeveelheid vs PO-hoeveelheid
3. Update resterende PO-hoeveelheid
4. Maak veld: "PO_Percentage_Invoiced"
5. Bij 100% gefactureerd: Sluit PO automatisch
```

**Implementatie:**
```
ALS Cumulatieve_Gefactureerde_Hoeveelheid ≤ PO_Hoeveelheid:
  Bereken: Percentage = (Cumulatief/PO) × 100
  Sla op in: PO_Percentage_Invoiced
  ALS Percentage ≥ 100:
    Stel PO_Status = "VOLLEDIG GEFACTUREERD"
    Sluit PO
```

---


### Scenario 2: Multi-Valuta PO Matching

**Uitdaging:** Factuurvaluta anders dan PO-valuta

**Oplossing:**
```
1. Detecteer valutamismatch
2. Haal wisselkoers op (uit API of masterdata)
3. Converteer factuurbedrag naar PO-valuta
4. Vergelijk geconverteerde bedragen
5. Sla zowel originele als geconverteerde bedragen op
```

**Implementatie:**
```
ALS Factuurvaluta ≠ PO-valuta:
  1. Haal wisselkoers op voor Factuurvaluta → PO-valuta
  2. Converteer: Factuurbedrag_Geconverteerd = Factuurbedrag × Koers
  3. Vergelijk: Factuurbedrag_Geconverteerd vs PO-bedrag
  4. Sla op: Origineel_Valutabedrag en Geconverteerd_Bedrag
  5. Vlag: "Valutaconversie_Toegepast"
```

---


### Scenario 3: Raamcontract / Mantelovereenkomst

**Uitdaging:** Meerdere facturen tegen enkele PO

**Oplossing:**
```
1. Identificeer PO-type = "Mantel"
2. Volg cumulatieve gefactureerde waarde
3. Controleer: Cumulatief ≤ Mantel PO Totaal
4. Update resterende PO-waarde na elke factuur
5. Waarschuw bij naderen PO-limiet
```

**Implementatie:**
```
ALS PO_Type = "Mantel":
  Bereken: Totaal_Gefactureerd_Tot_Heden
  Controleer: Totaal_Gefactureerd_Tot_Heden + Huidige_Factuur ≤ PO_Totaalwaarde
  ALS Binnen limiet:
    Keur factuur goed
    Update: Resterende_PO_Waarde
  ANDERS:
    Escaleer: "Mantel PO limiet overschreden"
```

---


## Foutafhandeling & Randgevallen

### Randgeval 1: Ontbrekend Regelitem op Factuur

**Probleem:** Factuur heeft item niet op PO

**Oplossing:**
```
1. Identificeer niet-gematchte regelitems
2. Bereken: Niet-gematcht_Bedrag
3. ALS Niet-gematcht_Bedrag < €100 (drempel):
     Maak beoordelingstaak (klein probleem)
   ANDERS:
     Escaleer onmiddellijk (groot probleem)
4. Sla details niet-gematcht item op
5. Vlag: "Extra_Items_Aanwezig"
```

---


### Randgeval 2: PO Gesloten maar Factuur Ontvangen

**Probleem:** PO al gesloten, late factuur ontvangen

**Oplossing:**
```
1. Controleer: PO_Status = "GESLOTEN"
2. Controleer: Factuurdatum vs PO_Sluitingsdatum
3. ALS Factuur binnen 30 dagen na sluiting:
     Heropen PO tijdelijk
     Verwerk factuur
     Sluit PO opnieuw
   ANDERS:
     Maak taak: "Late Factuur voor Gesloten PO"
     Toewijzen aan inkoop
     Handmatige beslissing vereist
```

---


### Randgeval 3: Meerdere PO's op Enkele Factuur

**Probleem:** Factuur verwijst naar meerdere PO's

**Oplossing:**
```
1. Parse factuur voor meerdere PO-nummers
2. Voor elke PO:
     Haal PO-gegevens op
     Match respectieve regelitems
3. Aggregeer matchresultaten
4. Algemene match = ALLE individuele PO's moeten matchen
5. Rapporteer over elke PO afzonderlijk
```

---


## Prestatietips

✅ **Beste Praktijken:**
- Cache PO-gegevens om lookups te verminderen
- Stel passende toleranties in (niet te streng, niet te mild)
- Gebruik eerst volledige matchcontrole (sneller)
- Log alle variantieberekeningen
- Beoordeel tolerantie-instellingen elk kwartaal
- Monitor auto-goedkeuringspercentages
- Volg veelvoorkomende variantieredenen

❌ **Vermijden:**
- Nultolerantie (te streng, te veel handmatige beoordelingen)
- Extreem hoge tolerantie (doet doel teniet)
- Systematische varianties negeren
- Variantie-trends niet volgen
- Verwerken zonder PO (indien vereist)

---


## Monitoring & Rapportage

### Belangrijkste Metrieken om te Volgen

1. **Matchpercentage:**
   - Volledige Match: X%
   - Binnen Tolerantie: Y%
   - Buiten Tolerantie: Z%

2. **Variantieanalyse:**
   - Gemiddelde prijsvariantie
   - Gemiddelde hoeveelheidsvariantie
   - Veelvoorkomende variantieredenen

3. **Verwerkingsefficiëntie:**
   - Auto-goedkeuringspercentage
   - Handmatig beoordelingspercentage
   - Gemiddelde beoordelingstijd

4. **Leveranciersprestaties:**
   - Variancies per leverancier
   - Matchpercentage per leverancier
   - Probleemleveranciers

---


## Testchecklist

- [ ] Perfect match scenario (volledige match)
- [ ] Binnen tolerantie scenario (kleine variantie)
- [ ] Buiten tolerantie scenario (grote variantie)
- [ ] Ontbrekende PO scenario
- [ ] Verkeerd PO-nummer scenario
- [ ] Gedeeltelijke levering scenario
- [ ] Overlevering scenario
- [ ] Valutamismatch scenario
- [ ] Meerdere PO's scenario
- [ ] Gesloten PO scenario
- [ ] Belastingvariantie scenario
- [ ] Escalatie workflow
- [ ] Taakcreatie
- [ ] E-mailmeldingen
- [ ] Veldupdates
- [ ] Export na goedkeuring

---


## Gerelateerde Patronen

### Patronen Die Goed Samenwerken:

- **[Taakbeheer Patroon](task-management-pattern.md)** - Maak beoordelingstaken voor varianties
- **[Beslissingslogica Patroon](decision-logic-pattern.md)** - Complexe routering op basis van variantieniveaus
- **[API Integratie Patroon](api-integration-pattern.md)** - Haal huidige prijzen op voor vergelijking
- **[Gegevenstransformatie Patroon](data-transformation-pattern.md)** - Valutaconversie, eenheidsconversie

---


## Gerelateerde Gidsen

### Vereisten
- [PO Matching Complete Gids](../and/compare-with-purchase-order/po-matching-complete-guide.md) - Alle PO-matchingkaarten
- [Gids Conditiekaarten](../and/condition-cards-complete-guide.md) - Conditielogica
- [Gids Veldmanipulatie](../then/document-field/field-manipulation-guide.md) - Veldoperaties

### Gerelateerde Kaarten
- **PURCHASE_ORDER_FULL_MATCH** - [PO Matching Gids](../and/compare-with-purchase-order/po-matching-complete-guide.md#full-match)
- **CONDITION_DOC_TO_PO_UNIT_PRICE** - [PO Matching Gids](../and/compare-with-purchase-order/po-matching-complete-guide.md#unit-price)
- **CONDITION_DOC_TO_PO_QUANTITY** - [PO Matching Gids](../and/compare-with-purchase-order/po-matching-complete-guide.md#quantity)
- **CONDITION_DOC_TO_PO_TAX_LINES** - [PO Matching Gids](../and/compare-with-purchase-order/po-matching-complete-guide.md#tax-lines)
- **tasks_create** - [Taaktoewijzingsgids](../then/task/task-assignment-guide.md)

### Volgende Stappen
- Maak beoordelingstaken: [Taakbeheer Patroon](task-management-pattern.md)
- Voeg e-mailmeldingen toe: [Gids E-mail Verzenden](../then/action/send-email-groups-guide.md)
- Implementeer complexe routering: [Beslissingslogica Patroon](decision-logic-pattern.md)

---


**Patroonversie:** 1.0
**Laatst Bijgewerkt:** 23 oktober 2025
**Moeilijkheidsgraad:** Gemiddeld-Hoog
**Geschatte Tijd:** 60-90 minuten
**Succespercentage:** Hoog (wanneer correct geconfigureerd)

