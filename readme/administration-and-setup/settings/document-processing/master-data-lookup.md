# Stamgegevens opzoeken

## Overzicht

De "Stamgegevens opzoeken" in je Instellingen voor documentverwerking biedt een uitgebreide en geïntegreerde aanpak voor het beheren en valideren van je documentgegevens door deze te synchroniseren met je Infor ERP-systeem. Zo helpt dit bij het stroomlijnen van de validatie en verbetering van documentverwerking binnen je ERP-omgeving:

1. **Gecentraliseerd gegevensbeheer**: Deze functie fungeert als een centrale opslagplaats waar gegevens uit verschillende bronnen, zoals leveranciers, klantadressen, belastingcodes en meer, kunnen worden opgeslagen en beheerd. Het biedt één referentiepunt voor alle stamgegevens, wat consistentie en nauwkeurigheid in je organisatie waarborgt.
2. **Validatie tegen ERP-gegevens**: Door stamgegevens, zoals leveranciersinformatie, van Infor naar DocBits te syncen, kun je de uit documenten geëxtraheerde gegevens automatisch valideren tegen je ERP-gegevens. Dit zorgt ervoor dat de verwerkte informatie (zoals leveranciersnamen, adressen en belastingcodes) overeenkomt met de gegevens in je ERP-systeem, waardoor fouten en afwijkingen worden geminimaliseerd.
3. **Maakt automatisering mogelijk**: Een robuust systeem voor het opzoeken van stamgegevens helpt bij het automatiseren van de verwerking van inkomende documenten. Zo kunnen inkooporders of facturen automatisch worden gecontroleerd op juistheid van leveranciersgegevens, goedgekeurd als ze overeenkomen of gemarkeerd voor controle bij afwijkingen.
4. **Verbetert gegevensintegriteit**: Regelmatige updates van je ERP-systeem naar de functie voor stamgegevens opzoeken zorgen ervoor dat de gegevens die voor documentverwerking worden gebruikt up-to-date zijn. Dit verkleint het risico dat documenten op basis van verouderde informatie worden verwerkt en verhoogt zo de algehele integriteit van zakelijke transacties.
5. **Efficiëntie in documentverwerking**: Met stamgegevens die direct gekoppeld en continu ververst worden, wordt documentverwerking efficiënter. Documenten kunnen automatisch worden geclassificeerd en gerouteerd op basis van specifieke criteria die in de stamgegevens zijn ingesteld, zoals specifieke leverancierstermijnen of belastingregels die van toepassing zijn op verschillende soorten transacties.

{% hint style="info" %}
Zie hier hoe je [Stamgegevens importeert](../../../infor-integration-and-configuration/importing-customer-master-data/)
{% endhint %}

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/master_data_lookup_1.png)

## **Toegang tot Stamgegevens opzoeken**

Ga naar de sectie **Stamgegevens opzoeken** via:\
**Instellingen → Documentverwerking → Stamgegevens opzoeken**

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_mater_data_lookup.png)

## **Instellingen**

Om de instellingen voor **Stamgegevens opzoeken** te openen, klik je op **Instellingen** linksonder op het scherm **Stamgegevens opzoeken**.\
De volgende configuratieopties zijn beschikbaar:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/master_data_lookup_2.png)

### **Leverancier BOD**

* **Synchronisatie van meerdere leveranciersaccounts toestaan**:
  * **Ingeschakeld**:\
    Een enkele leverancier kan meerdere `<FinancialParty>`-elementen in de BOD (Business Object Document) hebben, vaak vanwege meerdere gekoppelde IBANs of financiële accounts. Wanneer deze instelling is ingeschakeld, worden alle `<FinancialParty>`-entries voor de leverancier geëxtraheerd en opgeslagen in de leveranciertabel, zodat meerdere financiële attributen kunnen worden opgeslagen.
  * **Uitgeschakeld**:\
    Alleen het laatste `<FinancialParty>`-element dat voor de leverancier in de BOD wordt gevonden, wordt geëxtraheerd. Eerdere financiële attributen (bijv. extra IBANs) worden genegeerd en alleen de gegevens van de laatste vermelding worden opgeslagen in de leveranciertabel.

### **Inkooporder verwijderen**

*   **Inkooporder verwijderen na**: Geef op wanneer gesloten Inkooporders moeten worden verwijderd. Na de geselecteerde tijdsduur worden de records automatisch verwijderd.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/master_data_lookup_3.png)
