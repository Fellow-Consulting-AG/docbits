# Barcode Extracties

## Overzicht

Deze functie maakt automatische detectie van barcodes op documenten mogelijk. Wanneer geactiveerd, worden alle ondersteunde barcodetypen gescand en geëxtraheerd tijdens de verwerking.

## Hoe Barcode Extractie In te Schakelen

Volg deze stappen om de Barcode Extractie functie in te schakelen:

1. **Navigeer naar Instellingen**:
   * Ga vanuit het Dashboard naar **Instellingen**.
   * Selecteer **Documentverwerking** en kies vervolgens **Module**.
2. **Schakel de Functie In**:
   * Scroll naar beneden om de optie **Barcode Extractie** te vinden.
   *   Gebruik de schuifregelaar om Barcode Extractie in te schakelen.

       <figure><img src="../../../../../../.gitbook/assets/image (443) (1).png" alt=""><figcaption></figcaption></figure>

## **Aanvullende Instellingen**

### **Barcode Toewijzing**

#### **Doel:** Stelt validators in staat om handmatig een geëxtraheerde barcode waarde toe te wijzen aan een specifiek documentveld tijdens veldvalidatie.

#### Hoe **Barcode Toewijzing** In te Schakelen

Volg deze stappen om de **Barcode Toewijzing** functie in te schakelen:

1. **Navigeer naar Instellingen**:
   * Ga vanuit het Dashboard naar **Instellingen**.
   * Selecteer **Documentverwerking** en kies vervolgens **Module**.
2. **Schakel de Functie In**:
   * Scroll naar beneden om de optie **Barcode Toewijzing** te vinden.
   *   Gebruik de schuifregelaar om **Barcode Toewijzing** in te schakelen.

       <figure><img src="../../../../../../.gitbook/assets/image (446).png" alt=""><figcaption></figcaption></figure>

#### **Hoe het werkt:**

*   Schakelt een optie "Barcode Toewijzen" in op het veldvalidatiescherm.

    <div align="left"><figure><img src="../../../../../../.gitbook/assets/image (450).png" alt="" width="185"><figcaption></figcaption></figure></div>
*   Gebruikers kunnen een gedetecteerde barcode waarde selecteren en deze toewijzen aan een documentveld zoals PO Nummer of Factuur Nummer.

    <div align="left"><figure><img src="../../../../../../.gitbook/assets/image (451).png" alt="" width="315"><figcaption></figcaption></figure> <figure><img src="../../../../../../.gitbook/assets/SCreen.jpg" alt="" width="280"><figcaption></figcaption></figure></div>

### Splitsen van Document per Barcode / QR-Code

**Doel:**
Splitst automatisch documenten met meerdere pagina's in afzonderlijke documenten op basis van de aanwezigheid van specifieke barcodes of QR-codes.

#### Hoe Splitsen van Document per Barcode / QR-Code In te Schakelen

Volg deze stappen om de **Splitsen van Document per Barcode / QR-Code functie** in te schakelen:

1. **Navigeer naar Instellingen**:
   * Ga vanuit het Dashboard naar **Instellingen**.
   * Selecteer **Documentverwerking** en kies vervolgens **Classificatie en Extractie**.
2.  **Schakel de Functie In**:

    * Zoek de optie **Document Splitsen**.
    * Selecteer voor **Splitsen** de optie **Splitsen per Barcode / QR-Code**.
    * Kies voor **Barcode Type** een of meer ondersteunde barcodetypen uit de lijst.
    * Definieer voor **Barcode Patroon** het patroon dat een splitsing moet activeren. U kunt een **reguliere expressie** (regex) gebruiken om dynamische barcode waarden te matchen.

    <figure><img src="../../../../../../.gitbook/assets/image (448).png" alt=""><figcaption></figcaption></figure>

**Hoe het werkt:**

* U selecteert de barcodetypen die een splitsing moeten activeren.
* U definieert een patroon waaraan de barcode moet voldoen — dit kan een vaste tekenreeks of een regex zijn (bijv. `^INV\d{6}$` om barcodes zoals `INV123456` te matchen).
* Tijdens documentverwerking wordt elke keer dat een pagina een overeenkomende barcode bevat, een **nieuw document gemaakt** beginnend vanaf die pagina.

### Ondersteunde Code Typen

Geldt de [Overzichtspagina](./) voor de volledige lijst van ondersteunde barcode- en QR-codeformaten.
