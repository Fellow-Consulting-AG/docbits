# Autres paramètres

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 09.54.48.png" alt=""><figcaption></figcaption></figure>

#### Aperçu

La zone Autres paramètres permet aux administrateurs de configurer divers aspects du traitement des documents qui ne sont pas couverts par les paramètres de base. Cela inclut des options pour l'extraction de table, la révision de documents, la génération de PDF, les processus d'approbation et des paramètres spécifiques à des opérations particulières comme les bons de commande ou la comptabilité.

#### Fonctionnalités clés et options

1. **Extraction de table**:
* **Ignorer la validation de table** : Permet de contourner le processus de validation des données de table, ce qui peut être utile dans des scénarios où la validation des données doit être flexible.
2. **En révision**:
* **Concevoir le formulaire de révision** : Configure la mise en page et les champs qui apparaissent dans les formulaires de révision utilisés pendant le processus de révision des documents.
3. **Génération de PDF**:
* **Modèle de conception** : Spécifie le modèle utilisé pour générer des versions PDF des documents, ce qui peut être crucial pour l'archivage ou la communication externe.
4. **Approbation**:
* **Approuver avant exportation** : Garantit que les documents doivent être approuvés avant de pouvoir être exportés du système.
* **Deuxième approbation** : Ajoute une couche supplémentaire d'approbation pour une validation supplémentaire, renforçant le contrôle sur le traitement des documents.
5. **Bon de commande / Comptabilité automatique**:
* **Tableau BC dans le générateur de mise en page** : Permet l'inclusion de tableaux de bons de commande dans le générateur de mise en page pour des mises en page de documents personnalisées.
* **Bon de commande** : Active le traitement des documents de bons de commande dans le système.
* **Paramètre de tolérance BC** : Définit les niveaux de tolérance pour les quantités de bons de commande, ce qui aide à accommoder de légères divergences sans les signaler comme des erreurs.
6. **Exportation alternative de documents**:
* **Désactiver les statuts BC** : Permet de désactiver certains statuts pour les bons de commande lors du processus d'exportation, offrant une flexibilité dans la gestion des commandes.
7. **Carte numéro d'article fournisseur**:
* Un paramètre utilitaire qui fait correspondre les numéros d'article fournisseur aux numéros d'article internes, garantissant la précision dans la gestion des stocks et des bons de commande.

{% @jira/embed url="https://fellowpro.atlassian.net/browse/DOCB-2500" %}
