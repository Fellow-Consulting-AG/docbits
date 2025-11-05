# eSLOG 1.6 en 2.0

### Ondersteunde eSLOG Factuurversies

Momenteel worden **eSLOG Factuurversies 1.6 en 2.0** ondersteund.

Voor officiële eSLOG-documentatie kunt u [deze link](https://epos.si/en/eslog) raadplegen.

Beide eSLOG-versies zijn standaard ingeschakeld.

### Stappen om eSLOG-configuratie te Wijzigen

**Configureer eSLOG:**

* Navigeer naar **Instellingen → Globale Instellingen → Documenttypen → Factuur**.
*   Klik op **E-Doc**.\


    <figure><img src="../../../../../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>
* Een lijst van alle beschikbare e-docs verschijnt.
*   Zoek de eSLOG-versie die u wilt wijzigen.\


    <figure><img src="../../../../../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

### **Transformatie en XML-padconfiguratie:**

In de **transformatiesettings** kunt u het pad definiëren om specifieke informatie binnen het XML-bestand te lokaliseren en deze op te slaan in een nieuwe structuur, waardoor het gemakkelijker wordt om toegang te krijgen tot de gegevens. **Opmerking:** Als u deze functionaliteit gebruikt, moet u de nieuw aangemaakte XML-paden gebruiken, niet de oorspronkelijke XML-paden, in de **Voorbeeld** en **Extractiepad**.

#### **Stappen om Transformatie Bestand te Wijzigen:**

1. Open de **Transformatie**.
2. Maak een nieuw concept door op het **potloodicoon** te klikken.
3. Selecteer het nieuw aangemaakte concept.
4. Maak een nieuw veld aan of wijzig een bestaand veld.
5. Stel het gewenste pad in voor gegevensextractie.
6. Klik op **Opslaan**.

### Voorbeeld PDF-configuratie

De **Voorbeeld PDF-configuratie** wordt gebruikt om een gebruikersleesbare versie van het document te genereren. U kunt het aanpassen met HTML om aan uw behoeften te voldoen.

#### **Stappen om Voorbeeld Bestand te Wijzigen:**

1. Open de **Voorbeeld**.
2. Maak een nieuw concept door op het **potloodicoon** te klikken.
3. Selecteer het nieuw aangemaakte concept.
4. Maak een nieuw veld aan of wijzig een bestaand veld.
5. Stel het gewenste pad in voor gegevensextractie.
6. Klik op **Opslaan**.

### Extractiepadenconfiguratie

De **Extractiepadenconfiguratie** wordt gebruikt om gegevens te extraheren en velden in het **validatiescherm** in te vullen, zoals de factuurtabel of velden die zijn geconfigureerd in de factuurlay-out.

#### **Stappen om Extractiepaden te Wijzigen:**

1. Open de **Extractiepaden**.
2. Maak een nieuw concept door op het **potloodicoon** te klikken.
3. Selecteer het nieuw aangemaakte concept.
4. Maak een nieuw veld aan of wijzig een bestaand veld.
5.  De linkerkant vertegenwoordigt de **DocBits veld-ID**, die te vinden is in de **Instellingen → Globale Instellingen → Documenttypen → Factuur → Velden**.\


    <figure><img src="../../../../../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>
6. De rechterkant vertegenwoordigt het **pad naar het veld** dat is aangemaakt in de Transformatie.
7. Klik op **Opslaan**.
