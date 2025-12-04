# Modèle d'IA

## Aperçu

Le paramètre **Modèle d'IA** vous permet de définir quel modèle d'IA est utilisé par défaut pour l'**extraction des champs** et l'**extraction de tableau** lors du traitement des documents.\
Dans cette section, vous pouvez consulter le coût en tokens pour chaque modèle et voir quel modèle est actuellement assigné à chaque fournisseur.

## Comment accéder

1.  Naviguez vers **Paramètres** → **Traitement des documents** → **Classification et extraction**

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_classification_and_extraction.png)
2.  Faites défiler vers le bas jusqu'à la section **Extraction de tableau**

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_1.png)

## Options du Modèle d'IA

Vous pouvez choisir entre les modèles d'IA suivants. Survolez l'icône d'information dans l'interface pour voir le coût en tokens par document pour le modèle d'IA sélectionné :

* **Full** – 2 tokens par document
* **Fast** – 1 token par document
* **Turbo** – 1 token par document

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_2.png)

## Tableau d'Attribution du Modèle d'IA

Vous pouvez également configurer des **modèles d'IA** spécifiques au fournisseur directement dans l'écran de **Validation**, ce qui vous permet d'affiner la précision de l'extraction pour des fournisseurs individuels.\
\
Pour plus d'informations, veuillez consulter la documentation correspondante [ici](../../../../end-user-and-partner-section/end-user-section/validation-screen/supplier-specific-ai-model-for-field-and-table-extraction.md).

Le tableau d'attribution affiche les paramètres du modèle d'IA pour chaque fournisseur et comprend les détails suivants :

* **Supplier ID** – L'identifiant unique du fournisseur
* **AI Model** – Le modèle d'IA actuellement assigné au fournisseur
* **E-Text** : Indique si la fonctionnalité E-Text est activée
* **Action** – Contient l'option de supprimer l'entrée

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_3.png)

### Supprimer l'entrée – Réinitialiser les paramètres spécifiques au fournisseur

Pour réinitialiser le paramètre du modèle d'IA d'un fournisseur à la valeur par défaut :

1.  Cliquez sur l'icône de la corbeille dans la colonne **Action** à côté de l'entrée du fournisseur.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_4.png)
2.  Une boîte de dialogue de confirmation apparaîtra—confirmez que vous souhaitez supprimer l'entrée.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_5.png)

Une fois supprimé, le fournisseur reviendra à l'utilisation du **modèle d'IA** par défaut pour l'**extraction des champs** et l'**extraction de tableau**.
