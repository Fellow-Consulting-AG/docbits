# Exporteren

## Overzicht

De Export-pagina toont alle geconfigureerde exportinstellingen, inclusief of ze actief of inactief zijn. Vanaf hier kunnen gebruikers:

* Bestaande exportconfiguraties bekijken en beheren
* Nieuwe exportverbindingen maken (bijv. naar **Infor**, **Infor & IDM**, **Webhook** of **SFTP**)
* Bestaande exportconfiguraties bewerken of verwijderen

## Waar te Vinden

Je kunt het vinden onder: **Instellingen** → **Documentverwerking** → **Export**

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/image%20(442).png)

## **Gebruik van de Export-pagina**

Wanneer je de Export-pagina opent, zie je een lijst van alle bestaande exportconfiguraties.

Elke rij in de lijst toont:

* **Statusindicator**
  * **Groen** betekent dat de export actief is
  * **Rood** betekent dat de export gedeactiveerd is
* **Name** – de naam van de exportconfiguratie
* **Document Type** – het type document waarvoor de export is geconfigureerd
* **Sub-Organization** – als de export beperkt is tot een specifieke sub-organisatie
* **Export Method** – waar het document naartoe wordt gestuurd (bijv. Infor, IDM, SFTP)
* **Actions** – knoppen om de configuratie te **bewerken, verwijderen** of **activeren/deactiveren**

![DocBits Aankoop Order Export 7](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/docbits_purchase_order_export_7.png)

#### **Belangrijke Regels voor Exportconfiguratie**

Voor elk **documenttype** **binnen een gegeven organisatie of sub-organisatie** gelden de volgende regels:

* Je kunt **slechts één actieve Infor-export** hebben
* Je kunt **slechts één actieve niet-Infor-export** hebben (bijv. Webhook, SFTP)

Het is echter mogelijk om:

* **Eén actieve Infor-export** _en_ **één actieve niet-Infor-export** tegelijkertijd te hebben voor hetzelfde documenttype
* **Verschillende exportconfiguraties voor verschillende sub-organisaties** — bijvoorbeeld, een Infor-export voor Sub-Org A en een andere Infor-export voor Sub-Org B

## **Een Nieuwe Export Maken**

Om een nieuwe export te maken:

1. Klik op de **"Nieuw"** knop.\
   ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/image%20(1)%20(1)%20(1).png)
2. Selecteer het **Exporttype** dat je wilt configureren (bijv. Infor, IDM, SFTP).
3. Vul de vereiste velden in op basis van het exporttype.
4. Sla de configuratie op.

## Export Opties

#### Webhook

<details>

<summary>Webhook</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/image%20(15)%20(1).png)

#### **Veldbeschrijvingen**

* **Title**\
  De naam van de exportconfiguratie. Dit zal verschijnen in de exportlijst.
* **Sub-Organization** _(optioneel)_\
  Een dropdown met alle beschikbare sub-organisaties.
  * Indien leeg gelaten: van toepassing op de hoofdorganisatie.
  * Indien geselecteerd: de export is alleen van toepassing op de gekozen sub-organisatie.
* **Document Type**\
  Dropdown met alle beschikbare documenttypen.\
  Dit bepaalt op welk type document deze exportconfiguratie van toepassing is.
* **Export URL**\
  De bestemmings-URL waar het document geëxporteerd moet worden.

</details>

#### SFTP

<details>

<summary>SFTP</summary>

![DocBits Aankoop Order 4](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/docbits_purchase_order_4.png)

**Veldbeschrijvingen**

* **Title**\
  De naam van de exportconfiguratie. Dit zal verschijnen in de exportlijst.
* **Sub-Organization** _(optioneel)_\
  Een dropdown met alle beschikbare sub-organisaties.
  * Indien leeg gelaten: van toepassing op de hoofdorganisatie.
  * Indien geselecteerd: de export is alleen van toepassing op de gekozen sub-organisatie.
* **Document Type**\
  Dropdown met alle beschikbare documenttypen.\
  Dit bepaalt op welk type document deze exportconfiguratie van toepassing is.

- **Username**\
  De gebruikersnaam die wordt gebruikt om te authenticeren tegen de SFTP-server.
- **Password**\
  Het bijbehorende wachtwoord voor het SFTP-account. Zorg ervoor dat het account schrijftoegang heeft tot de gespecificeerde map.
- **Server URL**\
  De hostnaam of IP-adres van de doel-SFTP-server.
- **Port**\
  De poort die wordt gebruikt om verbinding te maken met de SFTP-server.
- **Folder**\
  Het pad op de SFTP-server waar documenten moeten worden geüpload (bijv. `/incoming/invoices/`).\
  Moet bestaan en beschrijfbaar zijn.
-   **XSLT File (Optioneel)**

    Het **XSLT-bestand** maakt transformatie van het standaard DocBits-exportformaat mogelijk.

    * **Wanneer te gebruiken:**\
      Alleen als het ontvangende systeem een andere structuur of specifieke opmaak vereist die verschilt van de standaard van DocBits.
    * **Laat het leeg** als het standaard exportformaat voldoet aan de vereisten.

</details>

#### Infor Export to SFTP

<details>

<summary>Infor Export to SFTP</summary>

![DocBits Export Sftp](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/docbits_export_sftp.png)

**Veldbeschrijvingen**

* **Title**\
  De naam van de exportconfiguratie. Dit zal verschijnen in de exportlijst.
* **Sub-Organization** _(optioneel)_\
  Een dropdown met alle beschikbare sub-organisaties.
  * Indien leeg gelaten: van toepassing op de hoofdorganisatie.
  * Indien geselecteerd: de export is alleen van toepassing op de gekozen sub-organisatie.
* **Document Type**\
  Dropdown met alle beschikbare documenttypen.\
  Dit bepaalt op welk type document deze exportconfiguratie van toepassing is.

- **IDM Mapping File**\
  Selecteer een mapping-bestand uit de bestandsbeheerder.\
  [Hulp nodig bij het maken? Bekijk de IDM Mapping Gids](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
- **BOD Mapping File**\
  Selecteer een mapping-bestand uit de bestandsbeheerder.\
  [Hulp nodig bij het maken? Bekijk de BOD Mapping Gids](../../../infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file.md)
- **Folder**\
  Het pad op de SFTP-server waar documenten moeten worden geüpload (bijv. `/incoming/invoices/`).\
  Moet bestaan en beschrijfbaar zijn.

</details>

#### **SMB**

<details>

<summary>SMB</summary>

![DocBits Export Smb](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/docbits_export_smb.png)

#### **Veldbeschrijvingen**

* **Title**\
  De naam van de exportconfiguratie. Dit zal verschijnen in de exportlijst.
* **Sub-Organization** _(optioneel)_\
  Een dropdown met alle beschikbare sub-organisaties.
  * Indien leeg gelaten: van toepassing op de hoofdorganisatie.
  * Indien geselecteerd: de export is alleen van toepassing op de gekozen sub-organisatie.
* **Document Type**\
  Dropdown met alle beschikbare documenttypen.\
  Dit bepaalt op welk type document deze exportconfiguratie van toepassing is.

- **Username**\
  De gebruikersnaam die wordt gebruikt om verbinding te maken met de SMB-share.
- **Password**\
  Het bijbehorende wachtwoord voor SMB-authenticatie.
- **Server URL**\
  Het adres van de SMB-server.
- **Port**\
  Poortnummer dat wordt gebruikt om toegang te krijgen tot de SMB-share.
- **Folder**\
  Het map-pad binnen de SMB-share waar documenten moeten worden opgeslagen (bijv. `/incoming/invoices/`).\
  Moet bestaan en beschrijfbaar zijn.
-   **JPL Mapping File (Optioneel)**

    Het **JPL-bestand** wordt gebruikt om een transformatie van de geëxporteerde gegevens te definiëren voordat deze naar de SMB-share worden geschreven.

    * **Wanneer te gebruiken:**\
      Alleen wanneer de geëxporteerde documentgegevens moeten worden aangepast om overeen te komen met externe opmaak of systeemverwachtingen.
    * **Laat het leeg** als er geen transformatie nodig is.

</details>

#### **Infor IDM**

<details>

<summary>Infor IDM</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/image%20(13)%20(1).png)

#### **Veldbeschrijvingen**

* **Title**\
  De naam van de exportconfiguratie. Dit zal verschijnen in de exportlijst.
* **Sub-Organization** _(optioneel)_\
  Een dropdown met alle beschikbare sub-organisaties.
  * Indien leeg gelaten: van toepassing op de hoofdorganisatie.
  * Indien geselecteerd: de export is alleen van toepassing op de gekozen sub-organisatie.
* **Document Type**\
  Dropdown met alle beschikbare documenttypen.\
  Dit bepaalt op welk type document deze exportconfiguratie van toepassing is.

- **ION Mapping File**\
  Selecteer een mapping-bestand uit de bestandsbeheerder.
- **IDM Mapping File**\
  Selecteer een mapping-bestand uit de bestandsbeheerder.\
  [Hulp nodig bij het maken? Bekijk de IDM Mapping Gids](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
- **Cloud / On-Prem Toggle**\
  Een schakelaar om het Infor-implementatietype aan te geven:
  * **Cloud**: Selecteer dit als je een Infor CloudSuite-klant bent.
  * **On-Prem**: Selecteer dit als Infor zelf gehost is.

</details>

#### **Infor ION**

<details>

<summary>Infor ION</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/image%20(11)%20(1).png)

#### **Veldbeschrijvingen**

* **Title**\
  De naam van de exportconfiguratie. Dit zal verschijnen in de exportlijst.
* **Sub-Organization** _(optioneel)_\
  Een dropdown met alle beschikbare sub-organisaties.
  * Indien leeg gelaten: van toepassing op de hoofdorganisatie.
  * Indien geselecteerd: de export is alleen van toepassing op de gekozen sub-organisatie.
* **Document Type**\
  Dropdown met alle beschikbare documenttypen.\
  Dit bepaalt op welk type document deze exportconfiguratie van toepassing is.

- **ION Mapping File**\
  Selecteer een mapping-bestand uit de bestandsbeheerder.
- **BOD Mapping File**\
  Selecteer een mapping-bestand uit de bestandsbeheerder.\
  [Hulp nodig bij het maken? Bekijk de BOD Mapping Gids](../../../infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file.md)
- **Cloud / On-Prem Toggle**\
  Een schakelaar om het Infor-implementatietype aan te geven:
  * **Cloud**: Selecteer dit als je een Infor CloudSuite-klant bent.
  * **On-Prem**: Selecteer dit als Infor zelf gehost is.

</details>

#### Infor IDM + ION BOD

<details>

<summary>Infor IDM + ION BOD</summary>

![DocBits Export Ion Bod](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/docbits_export_ion_bod.png)

#### **Veldbeschrijvingen**

* **Title**\
  De naam van de exportconfiguratie. Dit zal verschijnen in de exportlijst.
* **Sub-Organization** _(optioneel)_\
  Een dropdown met alle beschikbare sub-organisaties.
  * Indien leeg gelaten: van toepassing op de hoofdorganisatie.
  * Indien geselecteerd: de export is alleen van toepassing op de gekozen sub-organisatie.
* **Document Type**\
  Dropdown met alle beschikbare documenttypen.\
  Dit bepaalt op welk type document deze exportconfiguratie van toepassing is.

- **ION Mapping File**\
  Selecteer een mapping-bestand uit de bestandsbeheerder.
- **IDM Mapping File**\
  Selecteer een mapping-bestand uit de bestandsbeheerder.\
  [Hulp nodig bij het maken? Bekijk de IDM Mapping Gids](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
- **BOD Mapping File**\
  Selecteer een mapping-bestand uit de bestandsbeheerder.\
  [Hulp nodig bij het maken? Bekijk de BOD Mapping Gids](../../../infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file.md)
- **Cloud / On-Prem Toggle**\
  Een schakelaar om het Infor-implementatietype aan te geven:
  * **Cloud**: Selecteer dit als je een Infor CloudSuite-klant bent.
  * **On-Prem**: Selecteer dit als Infor zelf gehost is.

</details>

### Voor Infor CloudSuite Klanten

#### Infor IDM + LN

<details>

<summary>Infor IDM + LN</summary>

![DocBits Instellingen E-mail](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/docbits_settings_email.png)

#### **Veldbeschrijvingen**

* **Title**\
  De naam van de exportconfiguratie. Dit zal verschijnen in de exportlijst.
* **Sub-Organization** _(optioneel)_\
  Een dropdown met alle beschikbare sub-organisaties.
  * Indien leeg gelaten: van toepassing op de hoofdorganisatie.
  * Indien geselecteerd: de export is alleen van toepassing op de gekozen sub-organisatie.
* **Document Type**\
  Dropdown met alle beschikbare documenttypen.\
  Dit bepaalt op welk type document deze exportconfiguratie van toepassing is.

- **ION Mapping File**\
  Selecteer een mapping-bestand uit de bestandsbeheerder.
- **IDM Mapping File**\
  Selecteer een mapping-bestand uit de bestandsbeheerder.\
  [Hulp nodig bij het maken? Bekijk de IDM Mapping Gids](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)

* **LN Mapping File**\
  Selecteer een mapping-bestand uit de bestandsbeheerder.\
  [Hulp nodig bij het maken? Bekijk het LN Mapping Voorbeeld](../../../infor-integration-and-configuration/exporting-to-infor/ln/example-export-ln/)

</details>

#### Infor IDM + M3

<details>

<summary>Infor IDM + M3</summary>

![DocBits Instellingen](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/docbits_settings.png)

#### **Veldbeschrijvingen**

* **Title**\
  De naam van de exportconfiguratie. Dit zal verschijnen in de exportlijst.
* **Sub-Organization** _(optioneel)_\
  Een dropdown met alle beschikbare sub-organisaties.
  * Indien leeg gelaten: van toepassing op de hoofdorganisatie.
  * Indien geselecteerd: de export is alleen van toepassing op de gekozen sub-organisatie.
* **Document Type**\
  Dropdown met alle beschikbare documenttypen.\
  Dit bepaalt op welk type document deze exportconfiguratie van toepassing is.

- **ION Mapping File**\
  Selecteer een mapping-bestand uit de bestandsbeheerder.
- **IDM Mapping File**\
  Selecteer een mapping-bestand uit de bestandsbeheerder.\
  [Hulp nodig bij het maken? Bekijk de IDM Mapping Gids](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
- **M3 Mapping File**\
  Selecteer een mapping-bestand uit de bestandsbeheerder.\
  [Hulp nodig bij het maken? Bekijk het M3 Mapping Voorbeeld](../../../infor-integration-and-configuration/exporting-to-infor/m3/example-export-m3.md)

</details>

#### Infor IDM + M3 (toml)

<details>

<summary>Infor IDM + M3 (toml)</summary>

![DocBits Workflow Aankoop Order 5](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/docbits_workflow_purchase_order_5.png)

#### **Veldbeschrijvingen**

* **Title**\
  De naam van de exportconfiguratie. Dit zal verschijnen in de exportlijst.
* **Sub-Organization** _(optioneel)_\
  Een dropdown met alle beschikbare sub-organisaties.
  * Indien leeg gelaten: van toepassing op de hoofdorganisatie.
  * Indien geselecteerd: de export is alleen van toepassing op de gekozen sub-organisatie.
* **Document Type**\
  Dropdown met alle beschikbare documenttypen.\
  Dit bepaalt op welk type document deze exportconfiguratie van toepassing is.

- **ION Mapping File**\
  Selecteer een mapping-bestand uit de bestandsbeheerder.
- **IDM Mapping File**\
  Selecteer een mapping-bestand uit de bestandsbeheerder.\
  [Hulp nodig bij het maken? Bekijk de IDM Mapping Gids](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
- **M3 toml Mapping File**\
  Selecteer een mapping-bestand uit de bestandsbeheerder of gebruik de optie Toml selecteren om een toml te gebruiken die is gemaakt met de regelbeheerder.\
  [Hulp nodig bij het maken? Bekijk de Rule Manager Gids](rule-manager/)

</details>
