# eSLOG 1.6 et 2.0

### Versions de Facture eSLOG Supportées

Actuellement, **les versions de facture eSLOG 1.6 et 2.0** sont supportées.

Pour la documentation officielle d'eSLOG, vous pouvez vous référer à [ce lien](https://epos.si/en/eslog).

Les deux versions d'eSLOG sont activées par défaut.

### Étapes pour Modifier la Configuration d'eSLOG

**Configurer eSLOG :**

* Accédez à **Paramètres → Paramètres globaux → Types de documents → Facture**.
*   Cliquez sur **E-Doc**.\


    <figure><img src="../../../../../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>
* Une liste de tous les e-docs disponibles apparaîtra.
*   Localisez la version d'eSLOG que vous souhaitez modifier.\


    <figure><img src="../../../../../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

### **Configuration de la Transformation et du Chemin XML :**

Dans les **paramètres de transformation**, vous pouvez définir le chemin pour localiser des informations spécifiques dans le fichier XML et les enregistrer dans une nouvelle structure, facilitant ainsi l'accès aux données. **Remarque :** Si vous utilisez cette fonctionnalité, vous devez utiliser les nouveaux chemins XML créés, et non les chemins XML d'origine, dans l'**Aperçu** et le **Chemin d'extraction**.

#### **Étapes pour Modifier le Fichier de Transformation :**

1. Ouvrez la **Transformation**.
2. Créez un nouveau brouillon en cliquant sur l'**icône de crayon**.
3. Sélectionnez le brouillon nouvellement créé.
4. Créez un nouveau champ ou modifiez un champ existant.
5. Définissez le chemin souhaité pour l'extraction des données.
6. Cliquez sur **Enregistrer**.

### Configuration de l'Aperçu PDF

La **Configuration de l'Aperçu PDF** est utilisée pour générer une version lisible par l'utilisateur du document. Vous pouvez la personnaliser avec du HTML pour répondre à vos besoins.

#### **Étapes pour Modifier le Fichier d'Aperçu :**

1. Ouvrez l'**Aperçu**.
2. Créez un nouveau brouillon en cliquant sur l'**icône de crayon**.
3. Sélectionnez le brouillon nouvellement créé.
4. Créez un nouveau champ ou modifiez un champ existant.
5. Définissez le chemin souhaité pour l'extraction des données.
6. Cliquez sur **Enregistrer**.

### Configuration des Chemins d'Extraction

La **Configuration des Chemins d'Extraction** est utilisée pour extraire des données et remplir des champs dans l'**écran de validation**, tels que le tableau des factures ou les champs configurés dans la mise en page de la facture.

#### **Étapes pour Modifier les Chemins d'Extraction :**

1. Ouvrez les **Chemins d'Extraction**.
2. Créez un nouveau brouillon en cliquant sur l'**icône de crayon**.
3. Sélectionnez le brouillon nouvellement créé.
4. Créez un nouveau champ ou modifiez un champ existant.
5.  Le côté gauche représente l'**ID de champ DocBits**, qui peut être trouvé dans **Paramètres → Paramètres globaux → Types de documents → Facture → Champs**.\
    \


    <figure><img src="../../../../../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>
6. Le côté droit représente le **chemin vers le champ** créé dans la Transformation.
7. Cliquez sur **Enregistrer**.
