# AI-model

## Overzicht

De instelling **AI-model** stelt je in staat om te definiëren welk AI-model standaard wordt gebruikt voor **veld extractie** en **tabel extractie** tijdens documentverwerking.\
In deze sectie kun je de tokenkosten voor elk model bekijken en zien welk model momenteel aan elke leverancier is toegewezen.

## Toegang

1.  Navigeer naar **Instellingen** → **Documentverwerking** → **Classificatie en extractie**

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_classification_and_extraction.png)
2.  Scroll naar beneden naar de sectie **Tabel extractie**

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_1.png)

## AI-model Opties

Je kunt kiezen uit de volgende AI-modellen. Beweeg met de muis over het info-icoon in de interface om de tokenkosten per document voor het geselecteerde AI-model te bekijken:

* **Full** – 2 tokens per document
* **Fast** – 1 token per document
* **Turbo** – 1 token per document

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_2.png)

## AI-model Toewijzing Tabel

Je kunt ook leverancierspecifieke **AI-modellen** direct configureren in het **Validatie** scherm, waarmee je de extractienauwkeurigheid voor individuele leveranciers kunt verfijnen.\
\
Voor meer informatie, raadpleeg de bijbehorende documentatie [hier](../../../../end-user-and-partner-section/end-user-section/validation-screen/supplier-specific-ai-model-for-field-and-table-extraction.md).

De toewijzingstabel toont de AI-model instellingen voor elke leverancier en bevat de volgende details:

* **Supplier ID** – De unieke identificatie van de leverancier
* **AI Model** – Het AI-model dat momenteel aan de leverancier is toegewezen
* **E-Text**: Geeft aan of de E-Text functie is ingeschakeld
* **Action** – Bevat de optie om de invoer te verwijderen

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_3.png)

### Verwijder Invoer – Leverancierspecifieke Instellingen Herstellen

Om de AI-model instelling van een leverancier terug te zetten naar de standaard:

1.  Klik op het prullenbak-icoon in de **Action** kolom naast de leverancier invoer.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_4.png)
2.  Er verschijnt een bevestigingsdialoog—bevestig dat je de invoer wilt verwijderen.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_5.png)

Zodra verwijderd, zal de leverancier terugvallen op het standaard **AI-model** voor **veld extractie** en **tabel extractie**.
