# Classification et extraction

## Aperçu

Dans les Paramètres de **Classification et extraction**, vous pouvez :

* Activer la **Division des documents** basée sur des codes QR
* Configurer le **Format des montants**
* Configurer l’**Extraction de table**
* Activer/désactiver le traitement des fichiers **ZUGFeRD** non pris en charge
* Définir des règles de classification spéciales
* Surveiller les **Modèles d'IA** entraînés sur mesure utilisés dans le processus de classification

Cette page fournit une explication détaillée de tous les paramètres disponibles.

## Accès aux Paramètres de Classification et extraction

Pour accéder aux **Classification et extraction** Paramètres, allez à:\
**Paramètres → Traitement des documents → Classification et extraction**

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_classification_and_extraction.png)

## Division des documents

Dans la section **Division des documents**, vous pouvez configurer si un document téléversé doit être divisé en plusieurs documents dès qu’un **Code-barres** apparaît sur l’une de ses pages.

Pour activer cette fonctionnalité :

1. Accédez à la section **Division des documents**.
2.  Ouvrez le menu déroulant.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_14.png)
3.  Sélectionnez **Divisé par code-barres / QR code**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_15.png)

Vous aurez alors la possibilité de :

* Sélectionner un ou plusieurs types de code-barres à détecter.
*   Spécifier un motif regex que le code-barres doit respecter afin de déclencher la division du document.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_16.png)

## Format des montants

Dans la section **Format des montants**, vous avez deux options :

* **Autoriser l'arrondi lors de la comparaison des montants :**\
  Si activé, une tolérance de ±0,5 est autorisée lors de la comparaison des montants.\
  Si désactivé, une tolérance par défaut de ±0,05 s’applique.
* **Exiger une correspondance exacte pour la comparaison des montants :**\
  Si activé, les montants doivent correspondre exactement, sans aucune tolérance.\
  Si désactivé, une tolérance de ±0,05 est autorisée.

<mark style="color:red;">**Remarque**</mark> : Une seule de ces options peut être active à la fois.

## Extraction de table

Vous pouvez extraire des tableaux des documents en activant soit l’**Extraction de table**, soit l’**Extraction de table AI**. Un tableau entraîné — qu’il soit basé sur l’IA ou manuel — sera toujours lié à un fournisseur spécifique.

**Extraction de table :** Active l’**Extraction de table** manuelle. Les tableaux doivent être entraînés manuellement.\
En savoir plus sur l’entraînement manuel [ici](../../../setup/document-training/training-line-fields-table-training/defining-tables-and-columns.md).

**Extraction de table AI :** Utilise l’IA pour extraire automatiquement des tableaux. Si les résultats ne sont pas suffisamment précis, il est recommandé de passer à l’**Extraction de table** manuelle pour un meilleur contrôle et un meilleur entraînement.

**Extraction de tableaux pour le calcul des coûts :** Lorsqu’elle est activée, DocBits peut extraire des éléments de calcul des coûts à partir des tableaux au niveau des lignes et les classer en conséquence.\
Explication détaillée disponible [ici](table-extraction-for-costing-element.md).

**Extraction automatique du code fiscal :** Lorsqu’elle est activée, le système renseigne automatiquement le champ **Code des impôts** sur l’écran de validation — à condition qu’un champ de code fiscal soit configuré.\
Plus d’informations sur ce paramètre [ici](auto-extract-tax-code.md).

**Modèle d'IA :** Permet de spécifier quel **modèle d’IA** est utilisé pour l’extraction de tableaux.\
Vous verrez également un tableau indiquant :

* Quels **Fournisseurs** utilisent quel **Modèle d'IA**
* S’ils utilisent E-Text
* Des options pour supprimer une entrée ou réinitialiser les données d’entraînement

Ce paramètre est expliqué en détail [ici](ai-model.md).

## Document électronique

**Traiter les documents non pris en charge ZUGFeRD PDF :** Si activé, les versions **ZUGFeRD** non prises en charge seront traitées comme des PDF standard, et le XML intégré sera ignoré.

La liste des versions **ZUGFeRD** prises en charge se trouve [ici](../../global-settings/document-types/edi/zugferd-1.0-2.1-and-2.3.md).

## **Règles de classification**

Dans la section **Règles de classification**, vous pouvez définir des motifs **regex** et des critères spécifiques pour aider le système à classer automatiquement les documents pendant le traitement.

Pour accéder à cette section, cliquez sur l’onglet **Règles de classification** en haut de la page.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_1.png)

### **Ajouter une nouvelle règle de classification**

Pour créer une nouvelle règle :

1.  Cliquez sur **Ajouter** dans le coin supérieur droit.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_2.png)
2. Renseignez les champs suivants :
   * **Motif** : Le motif regex que le système doit rechercher pour déclencher la classification.
   * **Type** : L’emplacement où le motif doit être recherché (par ex., **Code-barres**).
   * **Sous-organisation** _(facultatif)_ : Spécifiez à quelle sous-organisation la règle s’applique.
   * **Type de document** : Définissez le type de document à attribuer lorsque le motif est trouvé.
   *   **Sous-type de document** _(facultatif)_ : Spécifiez un sous-type pour une classification plus détaillée.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_3.png)
3.  Cliquez sur **Sauvegarder** pour enregistrer votre règle de classification.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_4.png)

### **Éditer une règle de classification**

Pour éditer une règle existante :

1.  Cliquez sur les trois points dans la colonne **Actions**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_5.png)
2.  Sélectionnez **Éditer**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_6.png)
3. Apportez les modifications souhaitées.
4.  Cliquez sur **Sauvegarder** pour appliquer les mises à jour.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_4.png)

### **Supprimer une règle de classification**

Pour supprimer une règle :

1.  Cliquez sur les trois points dans la colonne **Actions**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_5.png)
2.  Sélectionnez **Supprimer**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_7.png)

## Modèles d'IA

La section **Modèles d'IA** affiche tous les modèles entraînés sur mesure qui ont été spécialement ajustés à vos besoins.

### Accéder à la section Modèles d'IA

Pour ouvrir cette section, cliquez sur l’onglet **Modèles d'IA** situé en haut de la page.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_8.png)

### Catégories de modèles

Les modèles sont organisés en catégories. Sous chaque nom de catégorie, le nombre de modèles qu’elle contient est indiqué.\
Cliquez sur une catégorie pour afficher ses détails.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_9.png)

En haut de la page de la catégorie sélectionnée, vous verrez des informations clés sur chaque modèle :

* **Type** : Le type de modèle.
* **Première page seulement** : Indique si le modèle traite uniquement la première page d’un document.
* **Version** : Le numéro de version du modèle.

### Tableau des modèles

Tous les modèles d’une catégorie sont listés dans un tableau, qui inclut les informations suivantes :

* **Nom** : Le nom du modèle.
* **Modèle suivant** : Le modèle qui traitera ensuite la sortie du modèle actuel.
* **Type de document** : Le type de document principal attribué par le modèle lors de la classification.
* **Sous-types de documents** : Les sous-types dans lesquels le document est ensuite classé.
* **Priorité** : Le niveau de priorité qui détermine la position du modèle dans la file de classification.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_11.png)

### Éditer un modèle

Pour éditer un modèle :

1.  Cliquez sur l’icône en forme de crayon dans la colonne **Actions** à côté du modèle que vous souhaitez éditer.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_10.png)
2. Mettez à jour les champs disponibles :
   * **Modèle suivant** : Sélectionnez le modèle qui doit traiter la sortie du modèle actuel.
   * **Type de document** : Choisissez le type de document que le modèle doit attribuer à l’entrée.
3.  Cliquez sur **Sauvegarder** pour appliquer vos modifications.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_12.png)
