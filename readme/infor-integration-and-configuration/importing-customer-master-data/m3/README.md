# M3

## Een API Connection Template importeren in Infor M3

Deze handleiding legt uit hoe je een API Connection Template importeert om snel belangrijke instellingen te configureren voor integratie met Infor M3. Door een template te gebruiken, kun je een vooraf gedefinieerde connection setup tot stand brengen, wat het proces vereenvoudigt en consistentie waarborgt.

<mark style="color:red;">**Opmerking**</mark>: Voor gedetailleerde configuratie van specifieke gebieden zoals Auto Accounting, Supplier Integration, Purchase Orders of Table Extraction voor kostenelementen, raadpleeg de bijbehorende documentatie:

* [Automatische boekhouding](auto-accounting.md)
* [Leveranciers en inkooporder](suppliers-and-purchase-orders.md)
* [Alle leveranciers importeren](how-to-import-all-suppliers.md)
* [Tabelextractie voor kostenelement](table-extraction-for-costing-element.md)

### **De template downloaden**

Download vóór het importeren de benodigde connection template via het onderstaande bestand:

{% file src="../../../.gitbook/assets/DocBits-Dev-Import-Template.xml" %}

### Template importeren

#### Stappen om een Connection Template te importeren

1. **Open Infor ION Desk:**
   *   Navigeer naar **InforOS** → **ION Desk** → **Connect** → **Connection Points**.

       ![](https://lh7-us.googleusercontent.com/ySRjNzMXFzwSOYKx9hnlKLPHPuXpmfTvRADBfV6cpT8ajiEUbS4oXpd9InhXG09mHLakhqBTJMH4yQJNG5z9RXmbAjh8YbuGhxnXSeooIH_r3RAGOvJE6Ok67ST_272zFfhB_TTFYg3b-NwFq0CAv2o)
2. **Importeer de template:**
   *   Klik op de knop **Import**.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/m3_import_2.png)
   * Selecteer het juiste **Template File** van je lokale systeem.
   *   Klik op **OK** om het importproces te starten.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/m3_import_3.png)
3. **Bevestiging:**
   *   Als de import is geslaagd, wordt een bevestigingsmelding weergegeven.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/m3_import_4.png)
4. **Configuratie na import:**
   * Na het importeren van de template kun je specifieke connection settings naar wens aanpassen.
   * Vergeet niet je **Service Account** te importeren of te configureren voor authenticatie en toegangsbeheer.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/m3_import_5.png)
