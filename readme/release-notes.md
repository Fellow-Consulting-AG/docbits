# Notes de version

## Release Spring Bloom – 23 avril 2025

### Améliorations de DocBits :

* **Option de filtre pour le journal d'importation des e-mails :** Les utilisateurs ont désormais la possibilité de filtrer les journaux d'importation et de trier le tableau pour une vue d'ensemble plus claire et plus efficace. Cette amélioration simplifie le processus d'identification et de gestion des entrées d'e-mails, améliorant le dépannage et la gestion globale des journaux.
* **Support multilingue pour la liste de valeurs :** Nous avons élargi les capacités multilingues de la fonctionnalité Liste de valeurs. Les administrateurs peuvent désormais définir des étiquettes dans plusieurs langues, garantissant que l'étiquette correcte est automatiquement affichée en fonction des paramètres de langue du système de l'utilisateur. Cette amélioration favorise une plus grande accessibilité et localisation, facilitant l'interaction des utilisateurs du monde entier avec la plateforme dans leur langue maternelle.
* **Améliorations des détails utilisateur dans les paramètres :** L'interface des paramètres affiche désormais des informations utilisateur complètes. Les administrateurs peuvent facilement voir les affiliations de groupe, les détails de sous-organisation et d'autres données clés, permettant une meilleure gestion des rôles des utilisateurs et une compréhension plus claire des structures d'équipe.
* **Informations comptables automatiques sur l'écran d'approbation :** L'écran d'approbation présente désormais des détails comptables automatiques aux côtés des informations de facturation. Cette amélioration offre un aperçu plus approfondi des données de transaction, facilitant des processus de révision plus fluides et une prise de décision plus éclairée concernant les factures.
*   **Introduction d'un nouveau système de test automatique pour améliorer la fonctionnalité et la stabilité du système :**

    Nous sommes ravis d'annoncer la mise en œuvre d'un nouveau système de test automatisé conçu pour améliorer la fonctionnalité et la fiabilité globales de notre plateforme. Ce nouveau système effectuera des vérifications constantes et approfondies de notre système pour identifier tout problème avant qu'il n'affecte votre expérience. En automatisant ces tests, nous pouvons garantir des réponses plus rapides aux problèmes potentiels et maintenir les normes de qualité les plus élevées pour notre système.

    ​

### Corrections de bugs

* Résolu un problème où les tâches n'apparaissaient pas sur l'écran de validation/approbation.
* Corrigé le positionnement du bouton Suivant/Précédent afin qu'il reste statique.
* Corrigé les problèmes de défilement dans les vues de script et d'arbre de décision, garantissant que les boutons d'action restent fixes pendant le défilement.
* Supprimé le champ pays d'origine des e-factures.
* Corrigé un problème avec le compteur de tâches affichant un nombre inexact de tâches.
* Ajouté des traductions manquantes.
* Corrigé les champs personnalisés pour afficher des noms descriptifs au lieu d'ID.
* Mis à jour la liste des raccourcis pour l'écran de correspondance des commandes d'achat.
* Résolu un problème où les documents étaient téléchargés avec un nom de fichier incorrect.
* Corrigé les incohérences de tri dans le tableau des lignes de factures au sein de la correspondance des commandes d'achat.
* Corrigé un problème affectant la fonctionnalité de création de tâches.
* Corrigé un problème dans la correspondance des commandes d'achat où le tri du tableau des factures se réinitialisait lors de la correspondance d'une ligne.
* Résolu des problèmes de comptabilité automatique en s'assurant que les références de réservation se divisent correctement lorsque le montant est divisé.
* Mis à jour les informations d'hôte ClickHouse.
* Résolu un problème où les documents en double n'étaient pas reconnus comme des doublons.
* Corrigé des problèmes d'exportation causés par des références de réservation trop longues.
* Résolu un problème où les cases à cocher en lecture seule n'étaient pas en lecture seule.

​

## Release Hot Fix Winter Frost 11 mars 2025

### Améliorations de DocBits :

* **Extraction de données améliorée :** Ajouté une option pour extraire le **Bon de commande** ou le **Numéro d'article** d'une ligne au-dessus ou en dessous.
* **Accès élargi aux sous-organisations croisées :** Les utilisateurs non administrateurs peuvent désormais également accéder à la fonctionnalité **Sous-organisations croisées**.

### **Corrections de bugs :**

* Corrigé un problème où les utilisateurs ne pouvaient pas être ajoutés à un groupe.
* Corrigé un problème avec les échecs d'importation d'e-mails.
* Résolu un problème avec la formation sur les documents de plus d'une page
* Corrigé un problème où les scripts ne fonctionnaient pas correctement.
* Résolu un problème où les données du document n'étaient pas affichées correctement
* Corrigé un problème avec le paramètre de mise à jour automatique des commandes d'achat
