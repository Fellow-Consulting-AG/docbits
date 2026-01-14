# Règles de correspondance des bons de commande

## Introduction : Bons de commande et gestion des règles de BC

La correspondance des bons de commande (BC) est un processus critique pour assurer la cohérence entre les bons de commande (BC) et les factures entrantes ou les réceptions de marchandises correspondantes. Un ensemble de règles robuste est essentiel pour atteindre un taux élevé de correspondance automatique, prévenir la fraude et garantir des paiements corrects.

Cette page de configuration est utilisée pour définir et gérer les règles qui déterminent _comment_ les postes de commande sont mis en correspondance avec le document entrant correspondant (Facture, Confirmation de commande).

***

## Comment y accéder

1.  Accédez à **Paramètres --> Paramètres globaux --> Types de documents**

    <figure><img src="../../../../../../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>


2.  Sélectionnez le type de document souhaité et cliquez sur **Plus de paramètres**.

    <figure><img src="../../../../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>


3.  Allez ensuite à la section Bon de commande et cliquez sur le bouton (PO match server side) puis cliquez sur Configurer les règles de correspondance de BC

    <figure><img src="../../../../../../.gitbook/assets/image (168).png" alt=""><figcaption></figcaption></figure>

***

<figure><img src="../../../../../../.gitbook/assets/Bildschirmfoto 2025-12-09 um 07.43.15.png" alt=""><figcaption></figcaption></figure>

## Paramètres globaux (Règles de base)

Ces paramètres établissent le cadre qui s'applique à toutes les règles de correspondance :

* **Paramètre :** Faire correspondre la quantité sur
  * **Objet :** Définit quel champ de quantité spécifique doit être principalement utilisé comme point de référence pour la correspondance des postes de commande dans toutes les règles.
  * **Valeurs valides :** Quantité ou autres champs de quantité disponibles dans le système, selon la structure des données (par exemple, un champ de quantité normalisé alternatif).
  * **Dépendance :** Détermine la base de toutes les règles de correspondance qui incluent la quantité dans leurs critères de comparaison.
* **Paramètre :** Tolérance standard (Tolérance par défaut)
  * **Objet :** Définit l'écart en pourcentage admissible de la quantité pour qu'une correspondance soit considérée comme valide. Elle compense les arrondis mineurs ou les différences de quantité.
  * **Valeur valide :** Un nombre décimal (par exemple, 0,005 correspond à 0,5 %).
  * **Dépendance :** S'applique aux règles qui utilisent des champs de quantité pour la correspondance et dont l'option "Autoriser la tolérance" est activée.

***

## Liste des règles

La liste des règles affiche toutes les règles de correspondance disponibles et gère leur ordre d'exécution.

#### Structure et exécution

* **Priorité :** Ce champ numérique (par exemple, 1, 2, 3) dicte la séquence d'exécution des règles. Les règles avec un numéro de priorité inférieur sont tentées en premier. Cela permet aux administrateurs de structurer une hiérarchie, commençant généralement par les règles les plus spécifiques et les plus strictes (par exemple, correspondance par numéro de ligne et numéro de pièce) et revenant à des règles plus larges ou moins restrictives.
* **Nom et Description :** Fournit une identification et un contexte clairs pour la règle, expliquant les critères principaux utilisés (par exemple, "Règle standard n° 1 : Correspondance basée sur le numéro de ligne, l'ID de la pièce et la quantité").
* **Active :** Un simple commutateur à bascule qui permet l'activation ou la désactivation instantanée de la règle sans avoir besoin de supprimer sa configuration.

**Flux d'exécution :** Le système effectue la correspondance selon une séquence en cascade. Si une règle (par exemple, Priorité 1) fait correspondre avec succès un poste, le processus pour ce poste s'arrête. Si aucune correspondance n'est trouvée, le système passe à la règle suivante dans la séquence de priorité (par exemple, Priorité 2).

***

## Configuration de la règle (Paramètres détaillés)

Cette zone de configuration détaillée définit la logique et les critères spécifiques pour une règle individuelle.

#### Paramètres de base

* **Type de règle (par exemple, Correspondance unique) :** Spécifie la cardinalité de la correspondance. La correspondance unique (Single Match) est le type courant, nécessitant une correspondance un-à-un (une ligne de BC pour une ligne de facture). D'autres types peuvent inclure des correspondances plusieurs-à-un ou un-à-plusieurs pour des articles agrégés ou des livraisons fractionnées.
* **Correspondance automatique :** Si activé, le système tentera d'appliquer cette règle de manière entièrement automatique. Une confiance élevée dans les critères est requise pour le traitement automatique.
* **Correspondance manuelle :** Si activé, cette règle peut être présentée ou appliquée par un utilisateur lors de l'étape de rapprochement manuel, lui offrant un ensemble prédéfini de critères de comparaison pour résoudre les exceptions.

#### Comparaison de colonnes (Critères de correspondance)

C'est la définition centrale de la logique de la règle, spécifiant quels champs doivent s'aligner entre les documents.

1. Définir les colonnes à comparer :
   * **Colonnes de BC :** Le champ tiré des données du bon de commande (par exemple, numéro de ligne).
   * **Colonnes de table extraites :** Le champ correspondant extrait ou analysé du document entrant (Facture/Confirmation de commande) (par exemple, `POSITION`).
2. **Type de comparaison :** Définit la nature de la correspondance requise (par exemple, Tt pour la comparaison Texte/Chaîne, nécessitant une correspondance exacte caractère par caractère ; # pour la comparaison numérique).
3. **Autoriser la tolérance :** Pour les champs numériques (quantité, prix), l'activation de cette option demande au système d'appliquer la tolérance standard globale définie précédemment. Si cela n'est _pas_ activé pour un champ numérique, les valeurs doivent correspondre exactement.
4. **Ignorer dans la correspondance manuelle :** Si coché, ce critère est assoupli lors de l'intervention manuelle. Ceci est utile pour les champs tels que les descriptions ou les références internes qui peuvent varier légèrement, permettant à l'utilisateur de passer outre les non-concordances mineures non critiques.

**Exemple : Règle de correspondance de BC stricte (`DefaultRule#1`)**

Une règle stricte typique combine des vérifications d'identité obligatoires avec des vérifications de valeur :

* **Identité obligatoire :** Le numéro de ligne et l'identifiant de l'article doivent correspondre exactement (comparaison de texte, pas de tolérance).
* **Vérifications de valeur :** La quantité normalisée effective et le prix unitaire normalisé effectif doivent correspondre (comparaison numérique, tolérance autorisée). Ce n'est que si les quatre critères sont remplis (avec tolérance pour les valeurs) qu'une correspondance automatique est exécutée.

***

## Impact sur le processus de correspondance de BC

L'ensemble de règles défini régit directement l'efficacité et l'intégrité du flux de travail de correspondance de BC :

* **Priorisation et replis :** La priorité définie garantit que le système tente d'abord la méthode de correspondance la plus fiable. Si les règles strictes et de haute priorité échouent, le système se rabat sur des règles plus larges, visant à minimiser le nombre d'exceptions acheminées vers les utilisateurs.
* **Contrôle de la qualité de la correspondance :** Des règles plus strictes (nécessitant des correspondances plus exactes et moins de tolérance) entraînent moins de correspondances automatiques, mais très fiables. Des règles plus lâches augmentent le taux de correspondance automatique mais augmentent le risque de faux positifs.
* **Gestion des exceptions (Correspondance manuelle) :** En activant des règles pour la correspondance manuelle, le système offre des options structurées aux utilisateurs. Si une transaction échoue aux critères de correspondance automatique, elle devient une exception. L'utilisateur peut alors tenter de résoudre l'exception en appliquant une règle manuelle prédéfinie, qui peut avoir des critères assouplis (par exemple, ignorer une non-concordance de texte mineure selon le paramètre "Ignorer dans la correspondance manuelle").

***

## Personnaliser les règles de correspondance de BC

Afin de modifier les règles de correspondance de BC, la version par défaut peut être clonée en cliquant sur **"Configurer la version"** et en utilisant l'option **"Cloner comme brouillon"** parmi les options de carte disponibles

<figure><img src="../../../../../../.gitbook/assets/image (197).png" alt=""><figcaption></figcaption></figure>