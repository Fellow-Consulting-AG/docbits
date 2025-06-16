# Écran de Correspondance des Bons de Commande

## Aperçu

Dans l'écran de **Correspondance des Bons de Commande**, vous pouvez comparer les lignes extraites de votre document avec celles stockées dans le **système Infor**, en utilisant le numéro de bon de commande comme référence.

Vous pouvez :

* **Identifier immédiatement** toute différence entre les données extraites et stockées
* **Définir des tolérances** pour permettre des écarts acceptables
* **Ignorer des statuts spécifiques** d'Infor, si nécessaire
* **Approuver et exporter** le document après une correspondance réussie
* **Rejeter** le document si les données ne répondent pas aux critères de validation requis

Cette page vous guidera à travers le processus de correspondance des bons de commande et expliquera toutes les fonctionnalités associées disponibles dans cette section.

## Outils dans l'Écran de Correspondance des Bons de Commande

En haut de l'écran de Correspondance des Bons de Commande, vous trouverez plusieurs outils—comme **Enregistrer**, **Correspondance Automatique**, **Exporter**, et d'autres—qui aident au processus de correspondance.\
Une description détaillée de chaque outil et de sa fonctionnalité peut être trouvée [ici](purchase-order-matching-tools.md).

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FxPOM1IzmTGgCCAE4tAQg%252Fpo_match_tools_0.png%3Falt%3Dmedia%26token%3D420e0d50-d5c8-4b7b-8ec6-26ca9e2d7a68\&width=768\&dpr=4\&quality=100\&sign=5d32419c\&sv=2)

## Filtrer et Ajouter des Numéros de Bons de Commande

Vous pouvez rechercher des numéros de bons de commande spécifiques en entrant le numéro dans le champ de recherche.\
Pour un filtrage plus raffiné, cliquez sur l'icône sur le côté droit de la barre de recherche pour sélectionner des critères spécifiques pour votre recherche.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F3xeAcb5EwKQPg9rksZVE%252Fpo_match_3.png%3Falt%3Dmedia%26token%3Deef4e964-ffe5-485c-ae22-c5790a9302fc\&width=768\&dpr=4\&quality=100\&sign=b0830e56\&sv=2)

Les options de filtrage suivantes sont disponibles pour vous aider à affiner votre recherche de bons de commande :

* **Mot-clé** – Filtrer par numéros de bons de commande.
* **Fournisseur** – Filtrer par nom ou ID du fournisseur.
* **Après la date** – Afficher les bons de commande créés après une date spécifique.
* **Avant la date** – Afficher les bons de commande créés avant une date spécifique.
* **Montant minimum de commande** – Filtrer par valeur de commande minimale.
* **Montant maximum de commande** – Filtrer par valeur de commande maximale.
* **Trier par** – Sélectionner l'attribut pour trier les résultats (par exemple, date, montant).
* **Direction du tri** – Choisir l'ordre de tri : croissant ou décroissant.
* **Nombre d'enregistrements à afficher** – Définir combien de résultats doivent être affichés par page.
* **Plus** – Options de filtrage supplémentaires incluent :
  * **Numéro de livraison**
  * **Numéro de bon de livraison**
  * **Identifiant de l'Article**

Après avoir configuré vos filtres, cliquez sur **Appliquer** pour les appliquer ou **Supprimer** pour réinitialiser tous les paramètres de filtre.

Les bons de commande correspondants seront affichés en fonction des filtres appliqués.\
Vous pouvez soit :

* Ajuster les filtres et rechercher à nouveau, ou
* Double-cliquer sur une entrée de bon de commande pour l'ajouter à l'écran de Correspondance des Bons de Commande.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F2uwMlpQ42lG5fOvUy4Gx%252Fpo_match_5.png%3Falt%3Dmedia%26token%3De2751f7f-586e-4303-bb17-db2a56de2b0b\&width=768\&dpr=4\&quality=100\&sign=fbf27bf2\&sv=2)

## Sélectionner des Numéros de Bons de Commande et Réorganiser les Colonnes

Vous pouvez passer d'un bon de commande individuel à l'autre pour voir leurs lignes respectives en cliquant sur le numéro de bon de commande en haut du tableau.

Vous pouvez également réorganiser les colonnes dans chaque vue de bon de commande en les faisant simplement glisser et déposer dans l'ordre de votre choix.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FwZzMEbGz7j20tIsouC8V%252Fpo_match_7.png%3Falt%3Dmedia%26token%3D6dc539ab-33af-40a6-8c82-04449ba317e4\&width=768\&dpr=4\&quality=100\&sign=3b8fd876\&sv=2)

Pour masquer définitivement des colonnes spécifiques, utilisez la fonctionnalité [**Définir les colonnes du tableau PO pour l'organisation**](./#definir-les-colonnes-du-tableau-po-pour-lorganisation).

## Définir les Colonnes du Tableau PO pour l'Organisation

Vous avez la possibilité de masquer ou d'afficher des colonnes spécifiques dans le tableau des bons de commande en cliquant sur l'icône des paramètres de colonne (montrée ci-dessous).\
Ce paramètre est disponible à la fois dans l'écran de **Correspondance des Bons de Commande** et dans le menu de **Recherche Avancée des Bons de Commande**.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F4nQ5loSdHlIebOh4vJ1m%252Fpo_tools_new_10.png%3Falt%3Dmedia%26token%3D84991cc8-f7ae-40f1-ba6c-cdd66722b898\&width=768\&dpr=4\&quality=100\&sign=ec34b898\&sv=2)

Des détails supplémentaires peuvent être trouvés [ici](purchase-order-matching-tools.md#definir-les-colonnes-du-tableau-po-pour-lorganisation).

## Resynchroniser le numéro de bon de commande avec Infor

Pour resynchroniser les données dans **DocBits** avec les données d'**Infor**, cliquez sur le **bouton de rafraîchissement** à côté du numéro de bon de commande au-dessus du tableau.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FNQiPjtumht4wV9z8VHtw%252Fpo_match_8.png%3Falt%3Dmedia%26token%3Dcd9cb152-6b2f-475e-abeb-e9ad1cbd46cf\&width=768\&dpr=4\&quality=100\&sign=adab84c\&sv=2)

Si votre processus de correspondance est basé sur l'attribut **Réception Livraison Quantité en cours**, vous avez également la possibilité d'effectuer une **synchronisation manuelle**, comme décrit en détail [ici](purchase-order-matching-tools.md#donnees-de-synchronisation).

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FcceZaArRjBdKpI5r5u1v%252Fpo_tools_new_7.png%3Falt%3Dmedia%26token%3D49e25f09-de07-42b7-ab3d-a43a35e567c5\&width=768\&dpr=4\&quality=100\&sign=c6e75393\&sv=2)

## Comment faire correspondre ?

Pour faire correspondre une ligne de bon de commande avec une ligne extraite du document, vous avez trois options :

1. **Glisser et Déposer**\
   Faites glisser la ligne de bon de commande souhaitée et déposez-la sur la ligne correspondante dans le tableau extrait.
2. **Clic Droit et Connecter**
   * Cliquez avec le bouton droit sur la ligne de bon de commande que vous souhaitez faire correspondre et sélectionnez **Sélectionner pour correspondre**.
   * Ensuite, cliquez avec le bouton droit sur la ligne correspondante dans le tableau extrait et sélectionnez **Connecter**.
3.  **Correspondance Automatique**

    Cliquez sur le bouton **Correspondance Automatique** pour laisser le système tenter automatiquement de faire correspondre toutes les lignes en fonction des données extraites et des données de bon de commande.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Flsdom16blO6pMF5rtQYS%252Fpo_tools_new_5.png%3Falt%3Dmedia%26token%3D616d6600-ff52-478a-9282-518212360106\&width=768\&dpr=4\&quality=100\&sign=ad47d853\&sv=2)

Vous pouvez également sélectionner **plusieurs lignes de bon de commande** et les faire correspondre à une **ligne unique** dans le tableau extrait.

## Quelles colonnes sont correspondantes ?

Le processus de Correspondance des Bons de Commande ne correspond qu'à des colonnes spécifiques. La liste ci-dessous décrit quelles colonnes sont correspondantes, si disponibles. Si aucune [tolérance](./#accepter-les-tolerances) n'est définie, les colonnes ne correspondront que si elles sont une correspondance exacte (100%).

* [Quantité](./#quantite) (Quantité | Quantité Reçue | Réception Livraison Quantité en cours)
* Prix Unitaire
* Numéro de Bon de Commande
* Numéro d'article/Identifiant de l'article du fournisseur
* Date de livraison promise

### Quantité

Vous avez trois options pour faire correspondre la quantité.

* Quantité
* Quantité Reçue
* Réception Livraison Quantité en cours

Vous pouvez définir cette option dans **Paramètres → Paramètres globaux → Types de documents → Plus de paramètres → Section Bon de Commande → Bon de Commande**

## Accepter les Tolérances

Vous pouvez spécifier des niveaux de tolérance acceptables pendant le processus de correspondance.\
Par défaut, seules les correspondances exactes (100%) sont considérées comme valides.

Si des tolérances sont configurées dans les paramètres du système, vous pouvez les ajuster pour les attributs autorisés directement dans le **Tableau Extrait** sous la colonne **Actions**.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FJLdikqwBf45WgFqlPUYW%252Fpo_match_11.png%3Falt%3Dmedia%26token%3D0c9d533f-f994-472a-9ff8-75ef564cef5e\&width=768\&dpr=4\&quality=100\&sign=b0c004c0\&sv=2)

Pour plus d'informations sur la configuration et l'utilisation des tolérances, consultez la [documentation détaillée](../../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-tolerance-settings-additional-purchase-order-tolerance.md).

## Désactiver les statuts

Vous pouvez exclure des lignes spécifiques avec certains statuts de la correspondance. Pour plus d'informations, reportez-vous à la [documentation détaillée](../../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-disable-statuses.md).

## Vérifier les lignes correspondantes

Plusieurs indicateurs sont disponibles pour vous aider à vérifier si un article a été correctement associé ou non.

### Tableau des Bons de Commande

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FB3LlWddnfNcu8kUedbvb%252Fpo_match_14.png%3Falt%3Dmedia%26token%3D484a856a-b8b2-439f-bbf9-35dd4bb55343\&width=768\&dpr=4\&quality=100\&sign=b71ea425\&sv=2)

* Cet icône indique que la ligne de bon de commande a été correctement associée.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F2vcst2wCfyck9Z7ak4eO%252Fguide_po_2.png%3Falt%3Dmedia%26token%3D78f7a224-ba6b-4027-b6a0-61e5502fd7c2\&width=768\&dpr=4\&quality=100\&sign=e0d60903\&sv=2)

* Cet icône indique que la ligne de bon de commande contient un désaccord.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FAb1A9PwBhrvfAf5q7f5w%252Fguide_po_5.png%3Falt%3Dmedia%26token%3D6616b59d-ffa4-4202-9382-3ac8ecd8b913\&width=768\&dpr=4\&quality=100\&sign=dd476496\&sv=2)

### Tableau Extrait du Document

*   Cet icône indique que l'article a été correctement associé. Vous pouvez survoler l'icône pour mettre en surbrillance la ligne de bon de commande correspondante.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Flogrk90Ufp5NQ7fd1QEX%252Fpo_match_15.png%3Falt%3Dmedia%26token%3D59c96286-24e9-4790-a9db-8c02efaed305\&width=768\&dpr=4\&quality=100\&sign=1a296310\&sv=2)
*   Cet icône indique que l'article contient un désaccord. Vous pouvez survoler l'icône pour mettre en surbrillance la ligne de bon de commande correspondante et voir les colonnes où se produisent les désaccords.

    ![](../../../.gitbook/assets/po_match_new_4.png)

## Correspondances Multiples

Si un seul article est associé à plusieurs lignes, vous pouvez voir des informations détaillées en cliquant sur l'icône plus (+) à côté de l'article respectif.

Cela développe la vue pour montrer toutes les entrées correspondantes, vous aidant à vérifier et à gérer efficacement les correspondances multiples.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FXueoHfU6EiDKaWBKJL2X%252Fpo_match_19.png%3Falt%3Dmedia%26token%3D9b947abd-5fbc-45e7-8e55-8b38746b5e32\&width=768\&dpr=4\&quality=100\&sign=191a712\&sv=2)

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FZJZekesrA0JB04GixOUi%252Fpo_match_18.png%3Falt%3Dmedia%26token%3D25c10718-2044-4de9-a5db-45f936d7235a\&width=768\&dpr=4\&quality=100\&sign=dd63d6c4\&sv=2)

## Supprimer les Connexions de Bon de Commande

Pour supprimer une connexion entre une ligne de bon de commande et une ligne extraite, cliquez simplement sur l'icône **X** à côté de la paire correspondante.\
Une fois supprimée, la connexion est annulée et l'article devient à nouveau disponible pour correspondance.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FSznmTo3Fnfi72ccpuLZk%252Fpo_match_new_2.png%3Falt%3Dmedia%26token%3Da04727b2-c8bf-44e0-b8f4-eaedb8180500\&width=768\&dpr=4\&quality=100\&sign=b740b466\&sv=2)

## Calcul

Sous le tableau contenant les informations extraites de votre document, vous pouvez trouver des calculs simples pour vérifier si le total des réservations correspond.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FA3TOYG26aHrETnMz4ADB%252Fimage.png%3Falt%3Dmedia%26token%3Db481bbc5-d278-4a46-b3cf-813225fa10ca\&width=768\&dpr=4\&quality=100\&sign=eeca6ad9\&sv=2)

### Réservations enregistrées :

La valeur des réservations enregistrées est dérivée du montant net extrait du document.

```
Réservations enregistrées = Montant net total (extrait du document)
```

### Total correspondant :

Cette valeur est calculée en additionnant les montants totaux de toutes les lignes qui ont pu être associées aux lignes du numéro de bon de commande.

```
 Total correspondant = Somme des montants totaux de toutes les lignes correspondantes
```

### **Frais :**

Tous les frais applicables seront inclus dans cette section s'ils sont présents.\
Pour plus de détails, reportez-vous à la [documentation détaillée](../../../administration-and-setup/settings/document-processing/classification-and-extraction/table-extraction-for-costing-element.md).

```
Frais = Élément de coût
```

### Montant non réglé :

La différence résultante est affichée ici et est calculée comme suit :

```
Montant non réglé = Réservations enregistrées - Total correspondant - Élément de coût
```

## Visualiser le Document pour Validation

Sur le côté droit de l'écran de **Correspondance des Bons de Commande**, vous pouvez visualiser le document pour aider à la validation.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F7X5cxghPovZfE8B2hvIy%252Fpo_new_1.png%3Falt%3Dmedia%26token%3D613a52db-b1a7-4d15-af8e-ab63725ae78c\&width=768\&dpr=4\&quality=100\&sign=3a887d60\&sv=2)

**Fonctionnalités de la Barre d'Outils du Visualiseur de Document :**

* Faites défiler les pages du document pour examiner le contenu.
* Cliquez sur le nom du fichier pour ouvrir l'écran de validation complet.
* Entrez un numéro de page et appuyez sur Entrée pour sauter directement à cette page.
* Utilisez les boutons plus (+) et moins (–) pour zoomer ou dézoomer sur le document.
*   Cliquez sur le bouton tout à droite pour ouvrir le document dans une fenêtre séparée, ce qui est particulièrement utile lorsque vous travaillez avec plusieurs écrans.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F8nUElRimoIOprR5yV5lN%252Fpo_match_10.png%3Falt%3Dmedia%26token%3De0d6924c-127f-4333-95f9-1b32d52b0da5\&width=768\&dpr=4\&quality=100\&sign=4f8161e4\&sv=2)

## Enregistrer les Modifications :

Pour enregistrer vos modifications, cliquez sur le bouton **Enregistrer** dans la barre d'outils.\
Si vous quittez la page sans enregistrer, tous les progrès réalisés pendant le processus de correspondance seront perdus.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FZ9ou72AJwvme2F7RWG7P%252Fpo_tools_new_6.png%3Falt%3Dmedia%26token%3D1d8ef55e-5ff1-4ee7-ac81-b76ff583a353\&width=768\&dpr=4\&quality=100\&sign=a17e5c90\&sv=2)

## Exporter le Document

Après avoir fait correspondre toutes les lignes et validé leur exactitude, vous pouvez exporter le document en cliquant sur le bouton **Exporter** dans la barre d'outils.

* Cliquer sur la petite flèche à côté du bouton **Exporter** révèle toutes les options d'exportation disponibles.
* Cliquer directement sur **Exporter** déclenchera l'option d'exportation par défaut (la première de la liste).

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fzc78lqQthkeTIpANlIAc%252Fpo_tools_new_8.png%3Falt%3Dmedia%26token%3Debdb58e9-b775-40a6-b7bc-82aa66f8811b\&width=768\&dpr=4\&quality=100\&sign=14ac5a25\&sv=2)
