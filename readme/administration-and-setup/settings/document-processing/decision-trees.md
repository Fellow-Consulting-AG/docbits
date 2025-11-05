# Beslisbomen

## Overzicht

Beslisbomen zijn een krachtige functie die het mogelijk maakt om geautomatiseerde routering en besluitvorming uit te voeren op basis van vooraf gedefinieerde regels. Deze functie is vooral nuttig in complexe omgevingen waar verschillende voorwaarden moeten worden geëvalueerd om de juiste actie te bepalen, zoals het toewijzen van prijzen, het bepalen van hoeveelheden of het routeren van documenten.

#### **Belangrijke Componenten**

* **Beslisbomenlijst**: Dit is de hoofdinformatie waar alle bestaande beslisbomen worden weergegeven. Elke beslisbomen kan worden geassocieerd met een specifiek documenttype zoals een INVOICE of QUOTE.
* **Beslisbombewerker**: Deze interface maakt het mogelijk om beslisbomen te maken en te bewerken, waar je regels, operatoren en acties kunt definiëren die moeten worden uitgevoerd wanneer aan bepaalde voorwaarden wordt voldaan.

## Beslisbominterface

#### **Beslisbomlijst**

De beslisbomenlijst toont alle beschikbare beslissingsbomen. Elke vermelding toont:

* **Naam**: De naam van de beslisbomen.
* **Documenttype**: Het type document dat is gekoppeld aan de beslisbomen (bijv. `FACTUUR`, `OFFERTE`).

#### **Beslisbombewerker**

De beslisbombewerker stelt je in staat om regels te configureren die bepalen hoe beslissingen worden genomen.

#### **Componenten van de beslisbombewerker**

* **Regels**: Elke regel bestaat uit voorwaarden en acties.
* **Selecteer Bron**: Deze dropdown stelt je in staat om het bronveld te specificeren dat geëvalueerd moet worden.
* **Selecteer Operator**: Definieert de logische operator (bijv. `<=`, `>=`, `=`, `!=`) die op het bronveld moet worden toegepast.
* **Resultaat**: Definieert de uitkomst of actie die moet worden ondernomen wanneer aan de voorwaarden wordt voldaan.
* **Nieuwe Rij Toevoegen**: Hiermee kun je extra regels aan de beslisbom toevoegen.

#### **Voorbeeld van een beslisbomconfiguratie**

1. **Regel 1**:
   * **Bron**: Hoeveelheid
   * **Operator**: `<=`
   * **Waarde**: `250000`
   * **Resultaat**: Toewijzen aan `CATMGR_CMM`
2. **Regel 2**:
   * **Bron**: Prijs
   * **Operator**: `>`
   * **Waarde**: `500000`
   * **Resultaat**: Toewijzen aan `PROCUREMENT_DIRECTOR`

Elke regel wordt opeenvolgend geëvalueerd, en de overeenkomstige actie wordt uitgevoerd als aan de voorwaarden wordt voldaan.

## Beslisbombeleid

Het beslisbombeleid definieert hoe meerdere regels binnen een beslisbom worden verwerkt. Je kunt kiezen uit verschillende beleidsopties:

* **Uniek**: Zorgt ervoor dat slechts één regel kan overeenkomen. Als meer dan één regel overeenkomt, zal de beslisbom een fout melden.
* **Eerste**: De eerste overeenkomende regel wordt toegepast, en er worden geen verdere regels geëvalueerd.
* **Prioriteit**: Regels worden geëvalueerd op basis van hun prioriteitsvolgorde. De hoogste prioriteit overeenkomende regel wordt toegepast.
* **Verzamelen (som)**: Verzamelt alle overeenkomende regels en somt de resultaten op.
* **Verzamelen (min/max/tellen)**: Verzamelt alle overeenkomende regels en selecteert ofwel het minimum, maximum, of telt de voorkomens.
* **Regelvolgorde**: Past regels toe in de volgorde waarin ze in de beslissingsboom verschijnen.
* **Elke**: Elke overeenkomende regel kan worden toegepast, waardoor meerdere uitkomsten mogelijk zijn.

#### **Voorbeeld van een Beslisbombeleid in Actie**

In de "Direct Group Price" beslisbom:

* **Geselecteerd Beleid**: `Eerste`
* Dit betekent dat zodra aan de voorwaarde van een regel is voldaan, de bijbehorende actie wordt toegepast en er geen verdere regels worden geëvalueerd.

## Exporteren en Opslaan

* **Opslaan**: Slaat de huidige configuratie van de beslisbom op.
* **Exporteren**: Hiermee kun je de configuratie van de beslisbom exporteren, die vervolgens in een andere omgeving kan worden geïmporteerd of voor back-updoeleinden kan worden gebruikt.
