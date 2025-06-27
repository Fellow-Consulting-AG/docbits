# Configuration des données floues avec les données maîtres

## **Aperçu**

Chaque type de document a ses propres configurations par défaut et doit être configuré séparément. Alors que cet exemple explique la configuration des **Factures**, le même processus s'applique à tous les types de documents.

## Pour configurer les données floues, accédez à :

Paramètres → Paramètres globaux → Types de documents → Facture → Champs → Paramètres des données maîtres → Rechercher les données maîtres

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fhnn2NcPGzVkUO0mLQWTy%252Fimage.png%3Falt%3Dmedia%26token%3De2f87385-fc48-4149-9bef-ca917a7328bd\&width=768\&dpr=4\&quality=100\&sign=116ee1da\&sv=2)

## **Recherches par défaut**

Il existe **quatre groupes de recherche par défaut** pour les factures :

1. **Données de l'entreprise**
2. **En-tête de commande d'achat**
3. **Fournisseur**
4. **Code de taxe**

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F4VxYFu8M62dXi6qGsPl3%252Fimage.png%3Falt%3Dmedia%26token%3Db2bc4690-805b-4b19-aa89-73f315889d88\&width=768\&dpr=4\&quality=100\&sign=835f513a\&sv=2)

Chaque groupe contient des champs spécifiques. Cliquez sur un groupe pour le **développer** et voir les champs. Les groupes de recherche par défaut sont étiquetés avec une balise **"Par défaut"**.

## **État de configuration de recherche**

* Les **configurations actives** sont marquées avec une balise **"Activé"**.
* Les **configurations désactivées** sont marquées avec une balise **"Désactivé"**.

## **Prérequis : Importation des données maîtres**

Pour que les données floues fonctionnent correctement, les **données maîtres** pertinentes doivent être importées. Sans cela, le système n'a pas de données de référence à utiliser. Voici comment importer les données maîtres :

{% content-ref url="../../../infor-integration-and-configuration/importing-customer-master-data/" %}
[importing-customer-master-data](../../../infor-integration-and-configuration/importing-customer-master-data/)
{% endcontent-ref %}

## **Gestion des groupes de recherche**

Chaque groupe de recherche est **activé par défaut** mais peut être modifié en cliquant sur les trois points :

* **Désactiver** → Désactive un groupe. _(Disponible uniquement pour les groupes activés)_
* **Activer** → Active un groupe. _(Disponible uniquement pour les groupes désactivés)_
* **Dupliquer** → Crée une copie qui peut être modifiée sans affecter l'original.
* **Afficher** → Affiche des informations telles que le **type de document** auquel il appartient et la **table de recherche** qu'il utilise. _(Disponible uniquement pour les groupes par défaut)_
* **Modifier** → Disponible pour les groupes **non par défaut**. Permet de modifier les détails du groupe.
* **Supprimer** → Supprime complètement le groupe. _(Uniquement pour les groupes non par défaut)_

## **Création d'une nouvelle configuration de recherche**

Il existe **deux façons** de créer une configuration de recherche :

1.  **Dupliquer une recherche existante**

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FZUlPcWGrx1oITQS3tgZP%252Fimage.png%3Falt%3Dmedia%26token%3D59fb300d-836e-40d0-84b7-4a405cf7f321\&width=768\&dpr=4\&quality=100\&sign=3442db8f\&sv=2)

    * Cela copie toutes les informations et les champs d'un groupe existant.
    * Vous devez uniquement fournir un **nouveau nom**.
2.  **Créer une recherche à partir de zéro**

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FNbEpo2p5Q8D1d7DUchBF%252Fimage.png%3Falt%3Dmedia%26token%3D401314b5-44d0-47df-b3e6-69fea83cce82\&width=768\&dpr=4\&quality=100\&sign=1d0ce322\&sv=2)

    * Cliquez sur **"Créer une configuration de recherche"**.
    * Remplissez les détails requis :
      * **Nom de la configuration**
      * **Table de recherche** (Table de données maîtres à utiliser)
      * **Gestionnaire de conflits** (Choisissez parmi : Meilleur score, Aucun retour, Premier retour)
      * **Type de contexte** (En-tête ou Ligne) besoin de contexte
      * **Correspondance totale** (Option de case à cocher) besoin de contexte

## **Gestion des champs au sein d'un groupe de recherche**

Chaque groupe contient des champs qui peuvent être **ajoutés, supprimés, modifiés ou consultés**, selon qu'ils sont des champs par défaut ou des champs personnalisés.

### **Champs par défaut**

*   Marqués d'une balise **"Par défaut"**.

    <div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fh37McVpB0tBo5wqiAttR%252Fimage.png%3Falt%3Dmedia%26token%3Dcabce083-83a5-4881-a64f-88a8757df49b&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=b3739019&#x26;sv=2" alt="" width="375"></div>
* **Peuvent seulement être consultés**, pas modifiés ou supprimés.

### **Champs non par défaut**

* **Peuvent être modifiés ou supprimés** en cliquant sur les trois points et en sélectionnant **Modifier** ou **Supprimer**.

### **Ajout d'un nouveau champ**

**Remarque :** Vous pouvez créer des champs à l'intérieur de configurations de recherche par défaut.

Pour ajouter un nouveau champ dans un groupe :

1.  Cliquez sur **"Créer"** à l'intérieur du groupe pertinent.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FvmIXTEQQHKKNbvTJj1b4%252Fimage.png%3Falt%3Dmedia%26token%3D8569867b-9f5b-4865-90bd-f2e41e846979\&width=768\&dpr=4\&quality=100\&sign=603cb7df\&sv=2)
2. Fournissez les détails suivants :
   * **Champ de recherche** → Nom de colonne de la table de recherche des données maîtres.
   * **Champ de validation** → Champ DocBits correspondant.
   * **Champ parent** → _(Plus de détails nécessaires)_
   * **Opérateur de recherche** → Choisissez parmi :
     * Intelligent
     * Contient
     * Exact
     * Commence par
     * Se termine par
   * **Cases à cocher :**
     * **Déclenchement automatique** → Lorsqu'il est activé, si un autre champ dans une configuration de recherche différente partage la même colonne, ce champ se mettra à jour **automatiquement** chaque fois que l'autre champ est mis à jour
     * **Recherche** → Active le champ en tant que champ **Données floues**, permettant des recherches dans la recherche de données maîtres (icône bleue dans l'écran de validation).

## **Étape finale : Ajout des champs à la mise en page**

Après avoir configuré les champs de données floues, **assurez-vous de les ajouter à la mise en page en utilisant le générateur de mise en page**. Si les champs ne sont pas ajoutés à la mise en page, ils ne seront pas disponibles pour une utilisation.

{% content-ref url="../../settings/global-settings/document-types/layout-manager/" %}
[layout-manager](../../settings/global-settings/document-types/layout-manager/)
{% endcontent-ref %}
