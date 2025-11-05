# Exporteren

## Overzicht

De Export-pagina toont alle geconfigureerde exportinstellingen, inclusief of ze actief of inactief zijn. Vanaf hier kunnen gebruikers:

* Bestaande exportconfiguraties bekijken en beheren
* Nieuwe exportverbindingen maken (bijv. naar **Infor**, **Infor & IDM**, **Webhook** of **SFTP**)
* Bestaande exportconfiguraties bewerken of verwijderen

## Waar te vinden

Je kunt het vinden onder: **Instellingen** → **Documentverwerking** → **Export**

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fn6ldlcI2sVUEgDdWb9U4%252Fimage.png%3Falt%3Dmedia%26token%3D8368818d-c899-4bee-ad21-a631d6be5c20\&width=768\&dpr=4\&quality=100\&sign=fbfcbd0c\&sv=2)

## **Gebruik van de Export-pagina**

Wanneer je de Export-pagina opent, zie je een lijst van alle bestaande exportconfiguraties.

Elke rij in de lijst toont:

* **Statusindicator**
  * **Groen** betekent dat de export actief is
  * **Rood** betekent dat de export gedeactiveerd is
* **Naam** – de naam van de exportconfiguratie
* **Documenttype** – het type document waarvoor de export is geconfigureerd
* **Sub-organisatie** – als de export beperkt is tot een specifieke sub-organisatie
* **Exportmethode** – waar het document naartoe wordt gestuurd (bijv. Infor, IDM, SFTP)
* **Acties** – knoppen om de configuratie te **bewerken, verwijderen** of **activeren/deactiveren**

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FyN87I5gzXxwGoAqC6zMF%252Fimage.png%3Falt%3Dmedia%26token%3D7df9d573-7e57-4ace-99c6-15a83691b926\&width=768\&dpr=4\&quality=100\&sign=6221cb80\&sv=2)

#### **Belangrijke regels voor exportconfiguratie**

Voor elk **documenttype binnen een gegeven organisatie of sub-organisatie** gelden de volgende regels:

* Je kunt **slechts één actieve Infor-export** hebben
* Je kunt **slechts één actieve niet-Infor-export** hebben (bijv. Webhook, SFTP)

Het is echter mogelijk om:

* **Eén actieve Infor-export** _en_ **één actieve niet-Infor-export** tegelijkertijd te hebben voor hetzelfde documenttype
* **Verschillende exportconfiguraties voor verschillende sub-organisaties** — bijvoorbeeld, een Infor-export voor Sub-Org A en een andere Infor-export voor Sub-Org B

## **Een nieuwe export maken**

Om een nieuwe export te maken:

1. Klik op de **"Nieuw"** knop.\
   &#x20;![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FTsHrIAUpe7EqenIzNAaJ%252Fimage.png%3Falt%3Dmedia%26token%3Dd2dbc996-b129-443c-a8df-9927a6f43a36\&width=300\&dpr=4\&quality=100\&sign=8769c331\&sv=2)
2. Selecteer het **Exporttype** dat je wilt configureren (bijv. Infor, IDM, SFTP).
3. Vul de vereiste velden in op basis van het exporttype.
4. Sla de configuratie op.

## Exporteer Opties

#### Webhook

<details>

<summary>Webhook</summary>

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FCwXUqFdCbRI5lRW49ymw%252Fimage.png%3Falt%3Dmedia%26token%3D798c0f40-6c4a-4650-9320-af2c17634fe9\&width=768\&dpr=4\&quality=100\&sign=15836833\&sv=2)

#### **Veld Omschrijvingen**

* **Titel** De naam van de export configuratie. Dit zal verschijnen in de export lijst.
* **Sub-Organisatie** _(optioneel)_ Een dropdown met alle beschikbare sub-organisaties.
  * Indien leeg gelaten: van toepassing op de hoofdorganisatie.
  * Indien geselecteerd: de export is alleen van toepassing op de gekozen sub-organisatie.
* **Document Type** Dropdown met alle beschikbare document types. Dit bepaalt naar welk type document deze export configuratie van toepassing is.
* **Export URL** De bestemmings-URL waar het document geëxporteerd moet worden.

</details>

#### SFTP

<details>

<summary>SFTP</summary>

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FzwUCWTdFETTvuTGl8qAn%252Fimage.png%3Falt%3Dmedia%26token%3D3f94b210-0128-4710-ae69-150a1363ce49\&width=768\&dpr=4\&quality=100\&sign=4ecd353\&sv=2)

#### **Veldbeschrijvingen**

* **Titel** De naam van de exportconfiguratie. Dit zal verschijnen in de exportlijst.
* **Sub-organisatie** _(optioneel)_ Een vervolgkeuzelijst met alle beschikbare suborganisaties.
  * Als leeg gelaten: van toepassing op de hoofdorganisatie.
  * Indien geselecteerd: de export is alleen van toepassing op de gekozen suborganisatie.
* **Documenttype** Vervolgkeuzelijst met alle beschikbare documenttypen. Dit bepaalt op welk type document deze exportconfiguratie van toepassing is.
* **Gebruikersnaam** De gebruikersnaam die wordt gebruikt om te verifiëren tegen de SFTP-server.
* **Wachtwoord** Het overeenkomstige wachtwoord voor het SFTP-account. Zorg ervoor dat het account schrijftoegang heeft tot de gespecificeerde map.
* **Server-URL** De hostnaam of IP-adres van de doel-SFTP-server.
* **Poort** De poort die wordt gebruikt om verbinding te maken met de SFTP-server.
* **Map** Het pad op de SFTP-server waar documenten moeten worden geüpload (bijv. `/incoming/invoices/`). Moet bestaan en beschrijfbaar zijn.
*   **XSLT-bestand (optioneel)**

    Het **XSLT-bestand** maakt transformatie van het standaard DocBits-exportformaat mogelijk.

    * **Wanneer te gebruiken:** Alleen als het ontvangende systeem een andere structuur of specifieke opmaak vereist die verschilt van de standaard van DocBits.
    * **Laat het leeg** als het standaard exportformaat voldoet aan de vereisten.

</details>

#### Infor Export naar SFTP

<details>

<summary>Infor Export naar SFTP</summary>

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FU0W4Qdy7ZlNoCn3E9wX5%252Fimage.png%3Falt%3Dmedia%26token%3D33673a12-55c4-479b-8ca8-b7c95e7a6a89\&width=768\&dpr=4\&quality=100\&sign=4af07f48\&sv=2)

#### **Veldomschrijvingen**

* **Titel** De naam van de exportconfiguratie. Dit zal verschijnen in de exportlijst.
* **Sub-Organisatie** _(optioneel)_ Een vervolgkeuzelijst met alle beschikbare sub-organisaties.
  * Indien leeg gelaten: van toepassing op de hoofdorganisatie.
  * Indien geselecteerd: de export is alleen van toepassing op de gekozen sub-organisatie.
* **Documenttype** Vervolgkeuzelijst met alle beschikbare documenttypen. Dit bepaalt op welk type document deze exportconfiguratie van toepassing is.
* **IDM Mapping-bestand** Selecteer een mapping-bestand uit de bestandsbeheerder. [Hulp nodig bij het maken? Bekijk de IDM Mapping Gids](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file)
* **BOD Mapping-bestand** Selecteer een mapping-bestand uit de bestandsbeheerder. [Hulp nodig bij het maken? Bekijk de BOD Mapping Gids](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file)
* **Map** Het pad op de SFTP-server waar documenten moeten worden geüpload (bijv. `/incoming/invoices/`). Moet bestaan en beschrijfbaar zijn.

</details>

#### **SMB**

<details>

<summary>SMB</summary>

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F6e4B9BWQWgHvcHhduXKb%252Fimage.png%3Falt%3Dmedia%26token%3D09e9534e-9268-4221-bd7b-89b621c80670\&width=768\&dpr=4\&quality=100\&sign=b03835a\&sv=2)

#### **Veldbeschrijvingen**

* **Titel** De naam van de exportconfiguratie. Dit zal verschijnen in de exportlijst.
* **Sub-Organisatie** _(optioneel)_ Een vervolgkeuzelijst met alle beschikbare suborganisaties.
  * Indien leeg gelaten: van toepassing op de hoofdorganisatie.
  * Indien geselecteerd: de export is alleen van toepassing op de gekozen suborganisatie.
* **Documenttype** Vervolgkeuzelijst met alle beschikbare documenttypen. Dit bepaalt op welk type document deze exportconfiguratie van toepassing is.
* **Gebruikersnaam** De gebruikersnaam die wordt gebruikt om verbinding te maken met de SMB-share.
* **Wachtwoord** Het bijbehorende wachtwoord voor SMB-authenticatie.
* **Server-URL** Het adres van de SMB-server.
* **Poort** Poortnummer dat wordt gebruikt om toegang te krijgen tot de SMB-share.
* **Map** Het map-pad binnen de SMB-share waar documenten moeten worden opgeslagen (bijv. `/incoming/invoices/`). Moet bestaan en beschrijfbaar zijn.
*   **JPL-toewijzingsbestand (Optioneel)**

    Het **JPL-bestand** wordt gebruikt om een transformatie van de geëxporteerde gegevens te definiëren voordat deze naar de SMB-share worden geschreven.

    * **Wanneer te gebruiken:** Alleen wanneer de geëxporteerde documentgegevens moeten worden aangepast om overeen te komen met externe opmaak of systeemverwachtingen.
    * **Laat het leeg** als er geen transformatie nodig is.

</details>

#### **Infor IDM**

<details>

<summary>Infor IDM</summary>

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FQ1AtdmTRZr1sGkH6oLwP%252Fimage.png%3Falt%3Dmedia%26token%3D720a4184-3f91-4b70-b3da-b846f3cce030\&width=768\&dpr=4\&quality=100\&sign=dc678c2c\&sv=2)

#### **Veldbeschrijvingen**

* **Titel** De naam van de exportconfiguratie. Dit zal verschijnen in de exportlijst.
* **Sub-Organisatie** _(optioneel)_ Een dropdown met alle beschikbare sub-organisaties.
  * Indien leeg gelaten: van toepassing op de hoofdorganisatie.
  * Indien geselecteerd: de export is alleen van toepassing op de gekozen sub-organisatie.
* **Documenttype** Dropdown met alle beschikbare documenttypen. Dit bepaalt op welk type document deze exportconfiguratie van toepassing is.
* **ION Mapping-bestand** Selecteer een mapping-bestand uit het bestandsbeheer.
* **IDM Mapping-bestand** Selecteer een mapping-bestand uit het bestandsbeheer. [Hulp nodig bij het maken? Bekijk de IDM Mapping Guide](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file)
* **Cloud / On-Prem-schakelaar** Een schakelaar om het Infor-implementatietype aan te geven:
  * **Cloud**: Selecteer dit als Infor CloudSuite-klant.
  * **On-Prem**: Selecteer dit als Infor zelf gehost is.

</details>

#### **Infor ION**

<details>

<summary>Infor ION</summary>

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FcYDXwDYH4RSc5vcY4fmr%252Fimage.png%3Falt%3Dmedia%26token%3Da9cfac80-9795-4e8f-a664-e268c9b4856c\&width=768\&dpr=4\&quality=100\&sign=5a4b0bd0\&sv=2)

#### **Veldbeschrijvingen**

* **Titel** De naam van de exportconfiguratie. Dit zal verschijnen in de exportlijst.
* **Sub-Organisatie** _(optioneel)_ Een vervolgkeuzelijst met alle beschikbare suborganisaties.
  * Indien leeg gelaten: van toepassing op de hoofdorganisatie.
  * Indien geselecteerd: de export is alleen van toepassing op de gekozen suborganisatie.
* **Documenttype** Vervolgkeuzelijst met alle beschikbare documenttypen. Dit bepaalt op welk type document deze exportconfiguratie van toepassing is.
* **ION Mapping-bestand** Selecteer een toewijzingsbestand uit de bestandsbeheerder.
* **BOD Mapping-bestand** Selecteer een toewijzingsbestand uit de bestandsbeheerder. [Hulp nodig bij het maken ervan? Bekijk de BOD Mapping Guide](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file)
* **Cloud / On-Prem-schakelaar** Een schakelaar om het Infor-implementatietype aan te geven:
  * **Cloud**: Selecteer dit als Infor CloudSuite-klant.
  * **On-Prem**: Selecteer dit als Infor zelf gehost is.

</details>

#### Infor IDM + ION BOD

<details>

<summary>Infor IDM + ION BOD</summary>

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FY13EX2xxOKLZzliAAHB0%252Fimage.png%3Falt%3Dmedia%26token%3D94335922-6342-405f-8c6d-29fdf2f31a2e\&width=768\&dpr=4\&quality=100\&sign=c0322806\&sv=2)

#### **Veldbeschrijvingen**

* **Titel** De naam van de exportconfiguratie. Dit verschijnt in de exportlijst.
* **Sub-Organisatie** _(optioneel)_ Een vervolgkeuzelijst met alle beschikbare suborganisaties.
  * Indien leeg gelaten: van toepassing op de hoofdorganisatie.
  * Indien geselecteerd: de export is alleen van toepassing op de gekozen suborganisatie.
* **Documenttype** Vervolgkeuzelijst met alle beschikbare documenttypen. Dit bepaalt op welk type document deze exportconfiguratie van toepassing is.
* **ION Mapping-bestand** Selecteer een mapping-bestand uit de bestandsbeheerder.
* **IDM Mapping-bestand** Selecteer een mapping-bestand uit de bestandsbeheerder. [Hulp nodig bij het maken? Bekijk de IDM Mapping-gids](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file)
* **BOD Mapping-bestand** Selecteer een mapping-bestand uit de bestandsbeheerder. [Hulp nodig bij het maken? Bekijk de BOD Mapping-gids](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file)
* **Cloud / On-Prem-schakelaar** Een schakelaar om het Infor-implementatietype aan te geven:
  * **Cloud**: Selecteer dit als Infor CloudSuite-klant.
  * **On-Prem**: Selecteer dit als Infor zelf gehost is.

</details>

### Voor Infor CloudSuite klanten

#### Infor IDM + LN

<details>

<summary>Infor IDM + LN</summary>

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F4SfGDqhA4KDrPfJ5vcsT%252Fimage.png%3Falt%3Dmedia%26token%3D4833c0dc-af8b-48a1-a977-6cc8ded20277\&width=768\&dpr=4\&quality=100\&sign=6301596\&sv=2)

#### **Veldbeschrijvingen**

* **Titel** De naam van de exportconfiguratie. Dit zal verschijnen in de exportlijst.
* **Sub-organisatie** _(optioneel)_ Een vervolgkeuzelijst met alle beschikbare sub-organisaties.
  * Indien leeg gelaten: van toepassing op de hoofdorganisatie.
  * Indien geselecteerd: de export is alleen van toepassing op de gekozen sub-organisatie.
* **Documenttype** Vervolgkeuzelijst met alle beschikbare documenttypen. Dit bepaalt op welk type document deze exportconfiguratie van toepassing is.
* **ION Mapping-bestand** Selecteer een mapping-bestand uit het bestandsbeheer.
* **IDM Mapping-bestand** Selecteer een mapping-bestand uit het bestandsbeheer. [Hulp nodig bij het maken? Bekijk de IDM Mapping Gids](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file)
* **LN Mapping-bestand** Selecteer een mapping-bestand uit het bestandsbeheer. [Hulp nodig bij het maken? Bekijk het LN Mapping Voorbeeld](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/ln/example-export-ln)

</details>

#### Infor IDM + M3

<details>

<summary>Infor IDM + M3</summary>

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FAN4T0aQEoogbUA8PUgy9%252Fimage.png%3Falt%3Dmedia%26token%3Da2b91153-858f-4711-abcc-4ed7ad60d49a\&width=768\&dpr=4\&quality=100\&sign=bb6bda83\&sv=2)

#### **Veldbeschrijvingen**

* **Titel** De naam van de exportconfiguratie. Dit zal verschijnen in de exportlijst.
* **Sub-Organisatie** _(optioneel)_ Een vervolgkeuzelijst met alle beschikbare suborganisaties.
  * Indien leeg gelaten: van toepassing op de hoofdorganisatie.
  * Indien geselecteerd: de export is alleen van toepassing op de gekozen suborganisatie.
* **Documenttype** Vervolgkeuzelijst met alle beschikbare documenttypen. Dit bepaalt op welk type document deze exportconfiguratie van toepassing is.
* **ION Mappingbestand** Selecteer een toewijzingsbestand uit het bestandsbeheer.
* **IDM Mappingbestand** Selecteer een toewijzingsbestand uit het bestandsbeheer. [Hulp nodig bij het maken? Bekijk de IDM Mappinggids](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file)
* **M3 Mappingbestand** Selecteer een toewijzingsbestand uit het bestandsbeheer. [Hulp nodig bij het maken? Bekijk het M3 Mappingvoorbeeld](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/m3/example-export-m3)

</details>

#### Infor IDM + M3 (toml)

<details>

<summary>Infor IDM + M3 (toml)</summary>

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FCdoduCkkbnomw3ahZgul%252Fimage.png%3Falt%3Dmedia%26token%3D4e5c7d08-5eaf-4c3e-9918-5cce58d8e3b3\&width=768\&dpr=4\&quality=100\&sign=e984c4e0\&sv=2)

#### **Veldbeschrijvingen**

* **Titel** De naam van de exportconfiguratie. Dit zal verschijnen in de exportlijst.
* **Sub-Organisatie** _(optioneel)_ Een dropdown met alle beschikbare sub-organisaties.
  * Indien leeg gelaten: van toepassing op de hoofdorganisatie.
  * Indien geselecteerd: de export is alleen van toepassing op de gekozen sub-organisatie.
* **Documenttype** Dropdown met alle beschikbare documenttypen. Dit bepaalt op welk type document deze exportconfiguratie van toepassing is.
* **ION Mapping-bestand** Selecteer een mapping-bestand uit het bestandsbeheer.
* **IDM Mapping-bestand** Selecteer een mapping-bestand uit het bestandsbeheer. [Hulp nodig bij het maken? Bekijk de IDM Mapping-gids](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file)
* **M3 toml Mapping-bestand** Selecteer een mapping-bestand uit het bestandsbeheer of gebruik de optie Toml selecteren om een toml te gebruiken die is gemaakt met de regelbeheerder. [Hulp nodig bij het maken? Bekijk de Rule Manager-gids](https://docs.docbits.com/administration-and-setup/settings/document-processing/rule-manager)

</details>
