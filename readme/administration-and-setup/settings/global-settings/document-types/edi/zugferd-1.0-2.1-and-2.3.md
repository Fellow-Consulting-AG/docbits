# ZUGFeRD 1.0, 2.1 en 2.3

## **Ondersteunde versies van ZUGFeRD**

Momenteel ondersteunde versies van ZUGFeRD zijn:

* **1.0**
* **2.1** (conform FACTUR-X 1.0.05)
* **2.3** (conform FACTUR-X 1.07.2)

#### Standaardactivatie en -wijziging

De ZUGFeRD-standaard is standaard altijd actief, maar je kunt deze indien nodig aanpassen.

### **Stappen om ZUGFeRD Instellingen te wijzigen:**

1. Navigeer naar **Instellingen → Globale instellingen → Documenttypen → Factuur**.
2.  Klik op **E-Doc**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/zugferd_1.png)
3. Er verschijnt een lijst met alle beschikbare e-docs.
4.  Zoek de **ZUGFeRD**-versie die je wilt wijzigen.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/zugferd_2.png)

## **Extraction Transformation and XML Path Configuratie:**

In de **Extraction Transformation-instellingen** kun je het pad definiëren om specifieke informatie in het XML-bestand te vinden en deze op te slaan in een nieuwe structuur, zodat de data makkelijker toegankelijk is.\
<mark style="color:red;">**Opmerking**</mark>: Als je deze functionaliteit gebruikt, moet je de nieuw aangemaakte XML paths gebruiken, niet de originele XML paths, in de **Preview** en **Extraction Path**.

### **Stappen om het Extraction Transformation-bestand te wijzigen:**

1. Open de **Extraction Transformation**.
2. Maak een nieuw concept door op het **potloodpictogram** te klikken.
3. Selecteer het nieuw aangemaakte concept.
4. Maak een nieuw veld aan of wijzig een bestaand veld.
5. Stel het gewenste pad in voor data-extractie.
6. Klik op **Opslaan**.

### Belangrijke opmerkingen:

* Het **Preview-bestand** wordt alleen gebruikt voor **FACTUR-X** en niet voor **ZUGFeRD**. ZUGFeRD gebruikt het originele **PDF**.

## Preview PDF Configuratie

De **Preview PDF Configuratie** wordt gebruikt om een door de gebruiker leesbare versie van het document te genereren. Je kunt deze met HTML aanpassen aan je behoeften.

### **Stappen om het Preview-bestand te wijzigen:**

1. Open de **Preview**.
2. Maak een nieuw concept door op het **potloodpictogram** te klikken.
3. Selecteer het nieuw aangemaakte concept.
4. Maak een nieuw veld aan of wijzig een bestaand veld.
5. Stel het gewenste pad in voor data-extractie.
6. Klik op **Opslaan**.

## Extraction Paths Configuratie

De **Extraction Paths Configuratie** wordt gebruikt om data te extraheren en velden in het **validatiescherm** te vullen, zoals de factuurtabel of velden die in de factuurlay-out zijn geconfigureerd.

### **Stappen om** **Extraction Paths** **te wijzigen**:

1. Open de **Extraction Paths**.
2. Maak een nieuw concept door op het **potloodpictogram** te klikken.
3. Selecteer het nieuw aangemaakte concept.
4. Maak een nieuw veld aan of wijzig een bestaand veld.
5.  De linkerkant vertegenwoordigt de **DocBits field ID**, die je kunt vinden in **Instellingen → Globale instellingen → Documenttypen → Factuur → Velden**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/zugferd_3.png)

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/zugferd_4.png)
6. De rechterkant vertegenwoordigt het **pad naar het veld** dat is gemaakt in de Extraction Transformation.
7. Klik op **Opslaan**.

Door deze stappen te volgen, zorg je voor nauwkeurige data-extractie en validatie voor ZUGFeRD-facturen.
