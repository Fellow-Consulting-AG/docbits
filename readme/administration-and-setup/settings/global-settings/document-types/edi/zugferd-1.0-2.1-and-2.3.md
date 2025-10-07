# ZUGFeRD 1.0, 2.1 et 2.3

## **Versions prises en charge de ZUGFeRD**

Les versions actuellement prises en charge de ZUGFeRD sont :

* **1.0**
* **2.1** (conforme à FACTUR-X 1.0.05)
* **2.3** (conforme à FACTUR-X 1.07.2)

#### Activation et modification du standard

Le standard ZUGFeRD est toujours actif par défaut, mais vous pouvez le modifier si nécessaire.

### **Étapes pour modifier les Paramètres de ZUGFeRD :**

1. Accédez à **Paramètres → Paramètres globaux → Types de documents → Facture**.
2.  Cliquez sur **E-Doc**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/zugferd_1.png)
3. Une liste de tous les e-docs disponibles s’affiche.
4.  Repérez la version **ZUGFeRD** que vous souhaitez modifier.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/zugferd_2.png)

## **Extraction Transformation and XML Path Configuration:**

Dans les **paramètres de l’Extraction Transformation**, vous pouvez définir le chemin pour localiser des informations spécifiques dans le fichier XML et les enregistrer dans une nouvelle structure, afin de faciliter l’accès aux données.\
<mark style="color:red;">**Remarque**</mark> : Si vous utilisez cette fonctionnalité, vous devez utiliser les nouveaux XML paths créés, et non les XML paths d’origine, dans le **Preview** et **Extraction Path**.

### **Étapes pour modifier le fichier d’Extraction Transformation :**

1. Ouvrez l’**Extraction Transformation**.
2. Créez un nouveau brouillon en cliquant sur l’**icône crayon**.
3. Sélectionnez le brouillon nouvellement créé.
4. Créez un nouveau champ ou modifiez un champ existant.
5. Définissez le chemin souhaité pour l’extraction des données.
6. Cliquez sur **Sauvegarder**.

### Notes importantes :

* Le **fichier de Preview** est utilisé uniquement pour **FACTUR-X** et non pour **ZUGFeRD**. ZUGFeRD utilisera le **PDF** original.

## Configuration du Preview PDF

La **Configuration du Preview PDF** est utilisée pour générer une version du document lisible par l’utilisateur. Vous pouvez la personnaliser avec du HTML selon vos besoins.

### **Étapes pour modifier le fichier de Preview :**

1. Ouvrez le **Preview**.
2. Créez un nouveau brouillon en cliquant sur l’**icône crayon**.
3. Sélectionnez le brouillon nouvellement créé.
4. Créez un nouveau champ ou modifiez un champ existant.
5. Définissez le chemin souhaité pour l’extraction des données.
6. Cliquez sur **Sauvegarder**.

## Extraction Paths Configuration

La **Extraction Paths Configuration** est utilisée pour extraire des données et renseigner des champs dans l’**écran de validation**, tels que le tableau de la facture ou les champs configurés dans la mise en page de la facture.

### **Étapes pour modifier** **Extraction Paths** :

1. Ouvrez **Extraction Paths**.
2. Créez un nouveau brouillon en cliquant sur l’**icône crayon**.
3. Sélectionnez le brouillon nouvellement créé.
4. Créez un nouveau champ ou modifiez un champ existant.
5.  Le côté gauche représente l’**ID du champ DocBits**, que vous pouvez trouver dans **Paramètres → Paramètres globaux → Types de documents → Facture → Champs**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/zugferd_3.png)

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/zugferd_4.png)
6. Le côté droit représente le **chemin vers le champ** créé dans l’Extraction Transformation.
7. Cliquez sur **Sauvegarder**.

En suivant ces étapes, vous pouvez garantir une extraction de données et une validation précises pour les factures ZUGFeRD.
