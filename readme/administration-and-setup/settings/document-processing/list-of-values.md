# List Of Values

## Aperçu

La fonctionnalité **Liste de valeurs** vous permet de créer et de gérer des ensembles de valeurs prédéfinies. Cela est particulièrement utile pour configurer des menus déroulants dans la section [**Champs**](../global-settings/document-types/fields/), qui peuvent ensuite être utilisés dans la **Validation des champs**.

Ces listes peuvent être personnalisées pour différentes sous-organisations et prennent en charge plusieurs langues, offrant ainsi une flexibilité à travers **DocBits**.

## Comment accéder ?

Vous pouvez accéder à la **Liste de valeurs** en naviguant vers **Paramètres → Traitement des documents → Liste de valeurs**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_list_of_values.png)

## Comment ajouter ou supprimer une liste

### Créer une nouvelle liste de valeurs

1.  Cliquez sur **Nouveau** dans le coin supérieur droit de l'écran.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_1.png)
2. Entrez un **Nom** pour votre liste.
3. _(Optionnel)_ Sélectionnez une **Sous-organisation** pour laquelle la liste doit être active.
4.  Cliquez sur **Sauvegarder** pour créer la liste.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_2.png)

### Comment supprimer une liste

Pour supprimer une liste, cliquez sur l'icône de la corbeille à côté de la liste correspondante.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_13.png)

<mark style="color:red;">**Remarque**</mark>: La liste sera supprimée immédiatement. Les listes marquées avec le tag [**Standard**](list-of-values.md#listes-et-lignes-definies-par-le-systeme) ne peuvent pas être supprimées.

## Comment ajouter, éditer ou supprimer des valeurs d'une liste existante

Vous pouvez gérer les valeurs dans une **Liste de valeurs** existante en utilisant l'une des méthodes suivantes :

* [**Ajouter des valeurs manuellement**](list-of-values.md#ajouter-des-valeurs-manuellement) – Entrez les valeurs individuellement via l'interface.
* [**Importer des valeurs à partir d'un fichier CSV**](list-of-values.md#importer-des-valeurs-a-partir-dun-fichier-csv) – Télécharger un fichier CSV pour ajouter plusieurs valeurs à la fois.

### Ajouter des valeurs manuellement

1.  Cliquez sur la liste que vous souhaitez modifier.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_3.png)
2.  Cliquez sur **Actions**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_4.png)
3.  Cliquez sur **Ajouter une ligne**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_5.png)

Maintenant, vous pouvez spécifier plusieurs propriétés pour chaque entrée :

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_6.png)

**Valeur** : C'est ainsi que l'élément sera stocké en interne dans **DocBits**. Il reste le même dans toutes les langues et sert également de texte d'affichage par défaut lors de la validation des champs si aucune étiquette n'est spécifiée pour la langue sélectionnée.

**Étiquette** : C'est le texte affiché sur l'écran de validation, basé sur la langue sélectionnée. Si aucune étiquette n'est disponible pour la langue active dans DocBits, le système affichera par défaut la **Valeur**.

**Langue** : Spécifie la langue dans laquelle l'étiquette sera affichée.\
Une explication plus détaillée peut être trouvée [ici](list-of-values.md#ajouter-des-traductions-a-vos-valeurs).

**Sous-organisations** : Spécifie pour quelle **sous-organisation** la ligne doit être active. Si laissé vide, la ligne sera disponible pour toutes les organisations.

**Synonymes** : Ici, vous pouvez spécifier des valeurs supplémentaires qui aident à former votre document.\
Par exemple, si **EUR** est votre **valeur** principale, vous pouvez ajouter EURO et € comme **synonymes**. Lorsque le document est formé en utilisant l'un de ces **synonymes**, **DocBits** reconnaîtra automatiquement et sélectionnera EUR comme valeur correspondante de votre liste. \
<mark style="color:red;">**Remarque**</mark>: Chaque synonyme doit être confirmé en appuyant sur **Entrée** pour l'ajouter à la liste.

4.  Après avoir entré toutes les propriétés souhaitées, cliquez sur le bouton **Sauvegarder** pour ajouter la ligne.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_11.png)

### Importer des valeurs à partir d'un fichier CSV

Pour ajouter plusieurs valeurs à la fois via l'importation CSV :

1.  Cliquez sur la liste que vous souhaitez mettre à jour.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_3.png)
2.  Cliquez sur **Actions**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_4.png)
3.  Cliquez sur **Télécharger le CSV**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_7.png)
4. Cliquez sur **Fichier** pour parcourir et sélectionner le fichier CSV que vous souhaitez télécharger.
5. Choisissez le **Délimiteur** approprié utilisé dans le fichier CSV (`;` ou `,`).
6.  Cliquez sur **Télécharger** pour importer les valeurs.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_8.png)

### Éditer des valeurs existantes

1. Localisez la ligne que vous souhaitez éditer.
2. Cliquez sur les trois points dans la colonne **Actions**.
3.  Sélectionnez **Éditer** dans le menu déroulant.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_10.png)
4. Apportez les modifications nécessaires.
5.  Cliquez sur **Sauvegarder** pour appliquer vos modifications.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_11.png)

### Supprimer des valeurs

1. Localisez la ligne que vous souhaitez supprimer.
2. Cliquez sur les trois points dans la colonne **Actions**.
3.  Sélectionnez **Supprimer** dans le menu déroulant.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_12.png)

<mark style="color:red;">**Remarque**</mark>: La ligne sera supprimée immédiatement. Les lignes marquées avec le tag [**Par défaut**](list-of-values.md#listes-et-lignes-definies-par-le-systeme) ne peuvent pas être supprimées.

## Ajouter des traductions à vos valeurs

Vous pouvez ajouter autant de traductions qu'il y a de langues prises en charge dans **DocBits**.

Pour ajouter une traduction :

1.  Cliquez sur l'icône plus (+).

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_14.png)
2.  Sélectionnez une langue dans le menu déroulant.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_15.png)
3.  Entrez la traduction souhaitée dans le champ **Étiquette**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_16.png)
4.  Pour ajouter une autre traduction, cliquez à nouveau sur l'icône plus (+).

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_17.png)
5.  Pour supprimer une traduction, cliquez sur l'icône de la corbeille.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_18.png)
6.  Lorsque vous avez terminé, cliquez sur le bouton **Sauvegarder** pour enregistrer vos traductions.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_19.png)

<mark style="color:red;">**Remarque**</mark>: Si aucune **Étiquette** n'est disponible pour la langue active, DocBits affichera par défaut la **Valeur**.

## Listes et lignes définies par le système

Certaines listes sont pré-créées par le système et sont marquées avec le tag **Standard**. Ces listes ne peuvent pas être supprimées, mais vous pouvez y ajouter de nouvelles lignes et supprimer ces nouvelles lignes si nécessaire.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_9.png)

Au sein de ces listes standard, certaines lignes sont marquées avec le tag **Par défaut**—ce sont des entrées définies par le système. Vous pouvez ajouter de nouvelles **étiquettes** dans différentes langues, mais ces lignes par défaut ne peuvent pas être supprimées.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_20.png)
