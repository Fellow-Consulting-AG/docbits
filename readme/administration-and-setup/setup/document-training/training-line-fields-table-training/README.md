# Formation des Champs de Ligne/Table de Formation

## Table de Formation : Quand et Comment l'Utiliser

DocBits utilise par défaut une extraction de table basée sur l'IA, qui fonctionne avec tous les fournisseurs. Cependant, lorsque vous avez besoin d'un contrôle plus précis sur la façon dont les éléments de ligne sont extraits pour un fournisseur spécifique, vous pouvez utiliser **la Formation de Table** pour définir manuellement la structure.

#### **Important : Formation Spécifique au Fournisseur**

La formation de table est **spécifique à chaque fournisseur**. Si vous formez une mise en page de table pour un fournisseur, les règles s'appliquent uniquement aux documents de ce fournisseur.\
Les autres fournisseurs continueront à utiliser l'extraction de table basée sur l'IA à moins d'être formés séparément.

#### Quand Devriez-vous Utiliser la Formation de Table ?

Utilisez la Formation de Table **uniquement lorsque la mise en page du document est stable**, et que vous souhaitez garantir une extraction cohérente et de haute qualité. Elle est particulièrement adaptée aux fournisseurs qui :

* Utilisent un **format de facture fixe** dans le temps.
* Nécessitent un **mappage précis** des éléments de ligne vers des champs spécifiques.
* Sont des fournisseurs **à volume élevé**, où l'automatisation constante est précieuse.

#### Quand ne pas Utiliser la Formation de Table

Évitez d'utiliser la Formation de Table si :

* Le fournisseur **change fréquemment la mise en page de sa facture** (par exemple, tous les quelques mois).
* Vous ne recevez pas régulièrement des documents de ce fournisseur.
* L'extraction par IA par défaut fonctionne **suffisamment bien** sans formation manuelle.

Dans de tels cas, reformer la table de manière répétée serait inefficace et chronophage.

## Comment l'Utiliser :

Le **Mode de Formation** est utilisé pour apprendre à DocBits comment extraire correctement les éléments de ligne de la mise en page d'un document spécifique d'un fournisseur.

Lorsque vous êtes en Mode de Formation, vous définissez :

* **Où se trouve la table** sur le document.
* **Quelles zones correspondent à chaque colonne** (par exemple, Quantité, Description, Prix unitaire).

Ce mode crée un **modèle d'extraction réutilisable** pour ce fournisseur, de sorte que les futurs documents avec la même mise en page seront traités automatiquement, pas besoin de reformer.

**Caractéristiques Clés :**

* Les **colonnes mappées sont en lecture seule** — vous ne pouvez pas modifier manuellement le texte.
* Vous **ne pouvez pas ajouter ou supprimer des lignes**.
* L'accent est mis sur **le mappage des positions**, pas sur la correction des valeurs.
* Une fois que vous avez terminé de mapper la table et ses colonnes, cliquez sur **"Enregistrer les Règles"** pour que DocBits apprenne et applique cette formation à des documents similaires du même fournisseur.

Le **Mode de Correction** vous permet de **corriger les erreurs d'extraction** dans les données de la table pour le document en cours. Il est utilisé lorsque DocBits a déjà tenté d'extraire la table, mais que les résultats nécessitent de petites corrections.

Utilisez le Mode de Correction lorsque :

* Certains **valeurs manquent ou sont mal alignées**.
* Une **ligne vide ou en double** a été extraite et doit être supprimée.

**Ce que Vous Pouvez Faire en Mode de Correction :**

* **Ajuster manuellement les valeurs** dans les colonnes mappées (par exemple, corriger les mauvais positionnements).
* **Supprimer des lignes** qui ne devraient pas faire partie de la table.
* **Ajouter des lignes** qui ont été entièrement manquées lors de l'extraction.
