# Inkooporder Matching Regels

## Introductie: Inkooporders en PO Regelbeheer

Inkooporder (PO) Matching is een kritiek proces om consistentie te garanderen tussen Inkooporders (PO's) en bijbehorende inkomende facturen of goederenontvangsten. Een robuuste set regels is essentieel om een hoog percentage automatische matching te bereiken, fraude te voorkomen en correcte betalingen te garanderen.

Deze configuratiepagina wordt gebruikt om de regels te definiëren en te beheren die bepalen _hoe_ PO-regelitems worden gematcht met het bijbehorende inkomende document (Factuur, Orderbevestiging)

***

## Hoe Toegang te Krijgen

1.  Navigeer naar **Instellingen --> Algemene Instellingen --> Documenttypen**

    <figure><img src="../../../../../../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>


2.  Selecteer het gewenste documenttype en klik op **Meer Instellingen**.

    <figure><img src="../../../../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>


3.  Ga vervolgens naar de Sectie Inkooporder en Klik op de Knop (PO match server side) en daarna op Configureer PO Matching Regels

    <figure><img src="../../../../../../.gitbook/assets/docbits_field_validation_formatting.png" alt="Docbits Field Validation Formatting"><figcaption></figcaption></figure>

***

<figure><img src="../../../../../../.gitbook/assets/Bildschirmfoto 2025-12-09 um 07.43.15.png" alt=""><figcaption></figcaption></figure>

## Algemene Instellingen (Basisregels)

Deze instellingen bepalen het kader dat van toepassing is op alle matchingregels:

* **Instelling:** Match Hoeveelheid Op
  * **Doel:** Definieert welk specifiek hoeveelheidsveld primair moet worden gebruikt als referentiepunt voor het matchen van inkooporderregelitems over alle regels heen.
  * **Geldige Waarden:** Hoeveelheid of andere beschikbare hoeveelheidsvelden in het systeem, afhankelijk van de datastructuur (bijv. een alternatief genormaliseerd hoeveelheidsveld).
  * **Afhankelijkheid:** Bepaalt de basis voor alle matchingregels die hoeveelheid in hun vergelijkingscriteria opnemen.
* **Instelling:** Standaard Tolerantie (Standaard Afwijking)
  * **Doel:** Definieert de toegestane procentuele afwijking in hoeveelheid voor een match om als geldig te worden beschouwd. Het compenseert kleine afrondings- of hoeveelheidsverschillen.
  * **Geldige Waarde:** Een decimaal getal (bijv. 0.005 komt overeen met 0.5%).
  * **Afhankelijkheid:** Is van toepassing op regels die hoeveelheidsvelden gebruiken voor matching en de optie "Tolerantie Toestaan" hebben ingeschakeld.

***

## Regellijst

De Regellijst toont alle beschikbare matchingregels en beheert hun uitvoeringsvolgorde.

#### Structuur en Uitvoering

* **Prioriteit:** Dit numerieke veld (bijv. 1, 2, 3) bepaalt de uitvoeringsvolgorde van de regels. Regels met een lager prioriteitsnummer worden eerst geprobeerd. Dit stelt beheerders in staat om een hiërarchie te structureren, meestal beginnend met de meest specifieke en strikte regels (bijv. matchen op zowel regelnummer als onderdeelnummer) en terugvallend op bredere of minder beperkende regels.
* **Naam & Beschrijving:** Biedt duidelijke identificatie en context voor de regel, waarbij de primaire gebruikte criteria worden uitgelegd (bijv. "Standaard Regel Nr. 1: Match op basis van Regelnummer, Onderdeel ID en Hoeveelheid").
* **Actief:** Een eenvoudige schakelaar die directe activering of deactivering van de regel mogelijk maakt zonder de configuratie te hoeven verwijderen.

**Uitvoeringsstroom:** Het systeem voert matching uit in een trapsgewijze volgorde. Als een regel (bijv. Prioriteit 1) met succes een regelitem matcht, stopt het proces voor dat item. Als er geen match wordt gevonden, gaat het systeem door naar de volgende regel in de prioriteitsvolgorde (bijv. Prioriteit 2).

***

## Regelconfiguratie (Detailinstellingen)

Dit gedetailleerde configuratiegebied definieert de specifieke logica en criteria voor een individuele regel.

#### Basisparameters

* **Regeltype (bijv. Enkele Match):** Specificeert de matching kardinaliteit. Enkele Match is het veelvoorkomende type, waarbij een één-op-één match vereist is (één PO-regel naar één Factuurregel). Andere typen kunnen veel-op-één of één-op-veel matches omvatten voor geaggregeerde items of gesplitste leveringen.
* **Automatische Match:** Indien ingeschakeld, zal het systeem proberen deze regel volledig automatisch toe te passen. Een hoog vertrouwen in de criteria is vereist voor automatische verwerking.
* **Handmatige Match:** Indien ingeschakeld, kan deze regel worden gepresenteerd of toegepast door een gebruiker tijdens de handmatige afstemmingsstap, waarbij hen een vooraf gedefinieerde set vergelijkingscriteria wordt geboden om uitzonderingen op te lossen.

#### Kolomvergelijking (Matchingcriteria)

Dit is de kerndefinitie van de logica van de regel, die specificeert welke velden tussen de documenten moeten overeenkomen.

1. De te Vergelijken Kolommen Definiëren:
   * **PO Kolommen:** Het veld afkomstig van de Inkoopordergegevens (bijv. regelnummer).
   * **Geëxtraheerde Tabelkolommen:** Het overeenkomstige veld geëxtraheerd of geparsed uit het inkomende document (Factuur/Orderbevestiging) (bijv. `POSITIE`).
2. **Vergelijkingstype:** Definieert de aard van de vereiste match (bijv. Tt voor Tekst/String vergelijking, waarbij een exacte teken-voor-teken match vereist is; # voor Numerieke vergelijking).
3. **Tolerantie Toestaan:** Voor numerieke velden (hoeveelheid, prijs) instrueert het activeren van deze optie het systeem om de eerder gedefinieerde Algemene Standaard Tolerantie toe te passen. Als dit _niet_ is ingeschakeld voor een numeriek veld, moeten de waarden exact overeenkomen.
4. **Negeren in Handmatige Match:** Indien aangevinkt, wordt dit criterium versoepeld tijdens handmatige interventie. Dit is nuttig voor velden zoals beschrijvingen of interne referenties die enigszins kunnen variëren, waardoor de gebruiker kleine niet-kritieke mismatches kan overschrijven.

**Voorbeeld: Strikte PO-Match Regel (`DefaultRule#1`)**

Een typische strikte regel combineert verplichte identiteitscontroles met waardecontroles:

* **Verplichte Identiteit:** Regelnummer en Item-ID moeten exact overeenkomen (Tekstvergelijking, geen tolerantie).
* **Waardecontroles:** Effectieve Genormaliseerde Hoeveelheid en Effectieve Genormaliseerde Eenheidsprijs moeten overeenkomen (Numerieke vergelijking, Tolerantie Toegestaan). Alleen als aan alle vier de criteria is voldaan (met tolerantie voor waarden) wordt een automatische match uitgevoerd.

***

## Impact op het PO Matching Proces

De gedefinieerde regelset regelt direct de efficiëntie en integriteit van de PO-matching workflow:

* **Prioritering en Terugvallen:** De gedefinieerde Prioriteit zorgt ervoor dat het systeem eerst de meest betrouwbare matchingmethode probeert. Als de strikte regels met hoge prioriteit falen, valt het systeem terug op bredere regels, met als doel het aantal uitzonderingen dat naar gebruikers wordt gestuurd te minimaliseren.
* **Matchkwaliteit Beheersen:** Striktere regels (die exactere matches en minder tolerantie vereisen) resulteren in minder, maar zeer betrouwbare, automatische matches. Lossere regels verhogen het percentage automatische matches maar verhogen het risico op valse positieven.
* **Uitzonderingsafhandeling (Handmatige Match):** Door regels voor Handmatige Match in te schakelen, biedt het systeem gestructureerde opties voor gebruikers. Als een transactie niet voldoet aan de automatische matchingcriteria, wordt het een uitzondering. De gebruiker kan dan proberen de uitzondering op te lossen door een vooraf gedefinieerde handmatige regel toe te passen, die mogelijk versoepelde criteria heeft (bijv. het negeren van een kleine tekstmismatch volgens de instelling "Negeren in Handmatige Match").

***

## Pas de PO Matching Regels Aan

Om de PO Matching regels te bewerken, kan de standaardversie worden gekloond door te klikken op **"Versiebeheer Configureren"** en de optie **"Klonen als Concept"** te gebruiken van de beschikbare kaartopties

<figure><img src="../../../../../../.gitbook/assets/docbits_doc_type_export_formats.png" alt="Docbits Doc Type Export Formats"><figcaption></figcaption></figure>
