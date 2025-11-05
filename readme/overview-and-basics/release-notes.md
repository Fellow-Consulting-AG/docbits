# Release-opmerkingen

## Release Autumn Summit 15 oktober 2025

### DocBits verbeteringen:

*   #### Verbeteringen in e-mailsjabloonontwerp:

    De e-mailsjablooneditor is opnieuw ontworpen om een duidelijkere structuur en soepelere ervaring te bieden. Het selecteren van documentvelden is nu intuïtiever en bijlagen kunnen rechtstreeks in sjablonen worden opgenomen. Deze verbeteringen maken het sneller en gemakkelijker om professionele, op maat gemaakte e-mails te maken.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fdv4oDlfkRyD0W9yWGAA4%252Fimage.png%3Falt%3Dmedia%26token%3D14bf7ebd-d886-4758-8184-d7b94447518a\&width=768\&dpr=4\&quality=100\&sign=88405d9c\&sv=2)
*   #### Dashboardverbeteringen:

    Het dashboard is uitgebreid om de navigatie en aanpassing te verbeteren. Met nieuwe tabbladen kunnen gebruikers sneller schakelen tussen verschillende documenttypen, waardoor de tijd die wordt besteed aan het zoeken naar de juiste weergave wordt verminderd.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FmpO7WSIrkL0I8Rje3HQt%252Fimage.png%3Falt%3Dmedia%26token%3D77d03fe7-e626-4645-b191-e332715a25fb\&width=768\&dpr=4\&quality=100\&sign=93fa9925\&sv=2)
*   #### Aangepaste Filterdashboards:

    Bovendien kunnen dashboards nu worden aangepast en gefilterd op basis van individuele voorkeuren. Deze aangepaste dashboards kunnen ook worden gedeeld met collega's, waardoor het gemakkelijker wordt om consistente teambrede rapportweergaven te maken.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fn5rPvGnRltT3mTIDoJwV%252Fimage.png%3Falt%3Dmedia%26token%3D22d065e3-81eb-4f16-828c-7f9134c25b1b\&width=768\&dpr=4\&quality=100\&sign=eb11d3a3\&sv=2)
*   #### E-mailmeldingslogs:

    Er is een nieuwe logfunctie beschikbaar voor alle e-mailmeldingen. Gebruikers kunnen nu een geschiedenis van verzonden meldingen bekijken, waardoor het gemakkelijker wordt om leveringen te verifiëren en problemen op te lossen als e-mails niet worden ontvangen.
*   #### Ondersteuning voor e-factuur: e-SLOG 1.6 & 2.0:

    Ondersteuning voor aanvullende e-factuurformaten is geïntroduceerd. Het systeem kan nu e-SLOG-versies 1.6 en 2.0 verwerken en genereren, waardoor de compatibiliteit met partners en wettelijke vereisten wordt uitgebreid.
*   #### Verbeteringen in duplicaatherkenning:

    Duplicaatherkenning is verbeterd met twee krachtige configuratieopties. Het **Duplicaatherkenningsinterval** stelt u in staat om een tijdsbereik te definiëren om duplicaten nauwkeuriger te controleren, terwijl de instelling **Export van duplicaten verbieden** automatisch voorkomt dat documenten die als duplicaten worden gedetecteerd, worden geëxporteerd. Samen bieden deze verbeteringen meer controle en zorgen ze voor een hogere gegevensnauwkeurigheid.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FXHRKTmuSxTlDt9lDEkE7%252Fimage.png%3Falt%3Dmedia%26token%3D96b56af6-c644-4b0f-a488-8bc16a03c11f\&width=768\&dpr=4\&quality=100\&sign=9b723b7f\&sv=2)
*   #### Beslissingsboomverbeteringen:

    Beslissingsbomen zijn nu veelzijdiger, met de mogelijkheid om documentveldwaarden terug te geven. Dit maakt meer geavanceerde automatiseringslogica mogelijk, waardoor workflows beslissingen kunnen nemen op basis van daadwerkelijke documentgegevens.
*   #### Nieuwe Workflowkaarten:

    Twee nieuwe workflowkaarten breiden de automatiseringsmogelijkheden uit. De eerste stelt u in staat te controleren of een document behoort tot een specifieke suborganisatie, waardoor het gemakkelijker wordt om multi-entity-opstellingen te beheren. De tweede introduceert een controle op tolerantie van leveringsdatum, waarbij leveringsdatums worden vergeleken met de huidige datum in werkdagen om te helpen bij het effectiever beheren en afdwingen van leveringsvereisten.
*   #### Verbeteringen in CSV-export:

    De CSV-exportfunctie is aanzienlijk verbeterd. In plaats van alleen de documenten op de huidige pagina te exporteren, exporteert het systeem nu alle documenten in een dataset. Elke export genereert een logboekvermelding en de resulterende CSV wordt automatisch via e-mail verzonden, waardoor een meer complete en betrouwbare exportprocedure wordt geboden.
*   #### Tijdsbestek voor verwijdering van inkooporder:

    Een nieuwe configuratieoptie stelt beheerders in staat een tijdsbestek voor het verwijderen van inkooporders te definiëren. Deze verbetering voegt flexibiliteit en controle toe over het beleid voor gegevensretentie, waardoor inkooporders alleen worden verwijderd wanneer dit passend is.

### Bugfixes

* Een probleem opgelost waarbij oude gegevens werden opgenomen bij het exporteren van documenten.
* De filter voor Exportfouten gecorrigeerd, die eerder ook andere statussen toonde.
* Een tabelvalidatiemismatch opgelost waarbij "Eenheidsprijs" fouten veroorzaakte maar "Eenheidsprijs per" niet, ondanks dat de waarden correct waren.
* Een probleem opgelost waarbij het toevoegen van een nieuwe kolom aan het dashboard mislukte.
* Een probleem opgelost waarbij taken niet zichtbaar waren in de kolom Taak van het dashboard.
* Willekeurig sorteergedrag opgelost, zodat lijsten nu een consistente volgorde volgen.
* Een probleem opgelost waarbij het wijzigen van de kolomgrootte niet kon worden gestopt.
* Een bug opgelost die het handmatig koppelen van regels in het scherm voor PO-koppeling verhinderde.
* Een probleem opgelost waarbij de optie voor e-mailbijlage werd gereset na het opslaan.
* Een probleem opgelost waarbij auto-accounting aanvankelijk database-ID's weergaf bij de eerste keer openen.
* Fuzzy-veldgedrag gecorrigeerd zodat waarden niet langer onjuist worden overschreven.
* Een probleem opgelost waarbij velden in auto-account verdwenen na het verwijderen van inhoud.
* Een bug opgelost waarbij de gebruiker "Voornaam" en "Achternaam" niet kon hernoemen in het instellingenpop-upvenster.
* Een probleem opgelost waarbij documenten vast konden komen te zitten in "workflow in uitvoering".
* Een menu-icoonkleurprobleem opgelost waarbij geselecteerde organisatiekleuren niet correct werden toegepast.
* Een probleem opgelost waarbij QR-codes soms niet werden herkend.
* Een probleem opgelost waarbij accounts niet konden worden verwijderd met backspace om een ander in te voeren.
* Een taalmix-up opgelost na het inloggen na de productie-push.

## Release Spring Bloom – 23 April 2025

### DocBits verbeteringen:

* **Filteroptie voor E-mail Import Log:** Gebruikers hebben nu de mogelijkheid om de importlogs te filteren en de tabel te sorteren voor een duidelijker en efficiënter overzicht. Deze verbetering stroomlijnt het proces van het identificeren en beheren van e-mailinvoer, waardoor probleemoplossing en algeheel logbeheer worden verbeterd.
* **Meertalige ondersteuning voor Lijst van Waarden:** We hebben de meertalige mogelijkheden uitgebreid naar de Lijst van Waarden functie. Beheerders kunnen nu labels in meerdere talen definiëren, zodat het juiste label automatisch wordt weergegeven op basis van de systeemtaalinstellingen van de gebruiker. Deze verbetering bevordert een grotere toegankelijkheid en lokalisatie, waardoor het voor gebruikers wereldwijd gemakkelijker wordt om met het platform in hun moedertaal te communiceren.
* **Verbeteringen van Gebruikersdetails in Instellingen:** De instellingeninterface toont nu uitgebreide gebruikersinformatie. Beheerders kunnen eenvoudig groepsaffiliaties, suborganisatiegegevens en aanvullende belangrijke gegevens bekijken, wat beter beheer van gebruikersrollen en een duidelijker begrip van teamstructuren mogelijk maakt.
* **Auto Boekhoudinformatie op het Goedkeuringsscherm:** Het goedkeuringsscherm toont nu auto boekhoudgegevens naast factuurinformatie. Deze verbetering biedt diepere inzichten in transactiegegevens, waardoor soepelere beoordelingsprocessen en beter geïnformeerde besluitvorming met betrekking tot facturen mogelijk zijn.
* **Taak Teller voor Documenten op de Dashboardweergave:** Documenten op het dashboard kunnen nu open taken aangeven die eraan zijn gekoppeld en het totale aantal uitstaande taken weergeven. Deze functie biedt gebruikers een snel overzicht van uitstaande acties, wat de taakbeheer en workflow-efficiëntie verbetert.
* **Leverancier-gebaseerde AI Modelselectie:** Gebruikers kunnen nu het AI-model selecteren dat wordt gebruikt voor gegevensextractie op basis van de leverancier. Deze verbetering maakt fijnere optimalisatie mogelijk, wat zorgt voor een betere extractienauwkeurigheid voor verschillende leveranciers en de algehele gegevensverwerkingsresultaten verbetert.
* **Verbeterde Workflow Logs voor Beslissingsboomkaarten:** De logs tonen nu de output van de beslissingsboom, waardoor het gemakkelijker wordt om te volgen en te begrijpen hoe beslissingen binnen workflows zijn genomen.
*   **Introductie van een Nieuwe Auto-Testopstelling om Systeemfunctionaliteit en Stabiliteit te Verbeteren:**

    We zijn verheugd om de implementatie van een nieuw geautomatiseerd testsysteem aan te kondigen dat is ontworpen om de algehele functionaliteit en betrouwbaarheid van ons platform te verbeteren. Deze nieuwe opstelling zal consistente, grondige controles op ons systeem uitvoeren om eventuele problemen te identificeren voordat ze uw ervaring beïnvloeden. Door deze tests te automatiseren, kunnen we snellere reacties op potentiële problemen garanderen en de hoogste kwaliteitsnormen voor ons systeem handhaven.

    ​

### Bugfixes

* Een probleem opgelost waarbij taken niet op het validatie/goedkeuringsscherm verschenen.
* De positionering van de Volgende/Vorige knop gecorrigeerd zodat deze statisch blijft.
* Scrollproblemen in de script- en beslissingsboomweergaven opgelost, zodat actieknoppen stationair blijven tijdens het scrollen.
* Het veld voor het land van herkomst van e-facturen verwijderd.
* Een probleem opgelost met de taak teller die een onnauwkeurig aantal taken weergaf.
* Ontbrekende vertalingen toegevoegd.
* Aangepaste velden gecorrigeerd om beschrijvende namen weer te geven in plaats van ID's.
* De sneltoetsenlijst voor het PO-matching scherm bijgewerkt.
* Een probleem opgelost waarbij documenten met een onjuiste bestandsnaam werden gedownload.
* Sorteer inconsistenties in de factuurregel tabel binnen PO-matching opgelost.
* Een probleem opgelost dat de functionaliteit voor het aanmaken van taken beïnvloedde.
* Een probleem in PO-matching opgelost waarbij de sortering van de factuurtabel werd gereset bij het matchen van een regel.
* Auto boekhoudproblemen opgelost door ervoor te zorgen dat boekingsreferenties correct worden gesplitst wanneer een bedrag wordt verdeeld.
* De ClickHouse hostinformatie bijgewerkt.
* Een probleem opgelost waarbij dubbele documenten niet als duplicaten werden herkend.
* Exportproblemen opgelost die werden veroorzaakt door te lange boekingsreferenties.
* Een probleem opgelost waarbij alleen-lezen selectievakjes niet alleen-lezen waren.
* Een probleem opgelost waarbij gebruikers twee keer aan een suborganisatie konden worden toegevoegd.
* Een probleem opgelost waarbij het wijzigen van de suborganisatie voor een document leidde tot het resetten van de toegewezen gebruiker of groep.

​

## Release Hot Fix Winter Frost 10 april 2025

### DocBits verbeteringen:

* **Verbeterde** **`set_column_date_value`** **Scriptfunctie:** De `set_column_date_value` functie ondersteunt nu de `skip_weekend` optie, waardoor datumwaarden automatisch weekenden overslaan wanneer ze worden toegepast.
* **Verbeterde Bestandsuploadondersteuning:** PNG- en JPEG-bestanden kunnen nu rechtstreeks worden geüpload en worden automatisch omgezet naar PDF-indeling voor gestroomlijnde documentverwerking.
* **Watchdog Functionaliteit Verbeteringen:**
  * Ondersteunt nu export naar **Enaio** voor betere systeemintegratie.
  * Verbeterde parsercapaciteiten om informatie uit `Sync.ContentDocument` XML-structuren te extraheren, waardoor efficiëntere gegevensverwerking mogelijk is.

### Bugfixes

* Een probleem met een scriptfunctie is opgelost.
* Een probleem opgelost waarbij inkooporders een verkeerde status hadden nadat ze waren bijgewerkt.

## Release Hot Fix Winter Frost 11 maart 2025

### DocBits verbeteringen:

* **Verbeterde Gegevensextractie:** Een optie toegevoegd om de **Inkooporder** of **Artikelnummer** van een regel erboven of eronder te extraheren.
* **Uitgebreide Toegang tot Cross Sub-Organisaties:** Niet-beheerders kunnen nu ook toegang krijgen tot de **Cross Sub-Organisaties** functie.

### **Bugfixes:**

* Een probleem opgelost waarbij gebruikers niet aan een groep konden worden toegevoegd.
* Een probleem opgelost met mislukkingen bij het importeren van e-mails.
* Een probleem opgelost met de veldtraining op documenten met meer dan één pagina.
* Een probleem opgelost waarbij scripts niet goed werkten.
* Een probleem opgelost waarbij documentgegevens niet correct werden weergegeven.
* Een probleem opgelost met de automatische update van de inkooporderinstelling.
* Een probleem opgelost waarbij de abonnements tokens verkeerd werden weergegeven.
* Een probleem opgelost waarbij het taken scherm een verouderde documentversie weergaf.
* Een probleem opgelost dat ervoor zorgde dat documenten hun status niet wijzigden.

