# Arbres de Décision

### Aperçu

Les Arbres de Décision sont une fonctionnalité puissante qui permet le routage automatisé et le processus de prise de décision basé sur des règles prédéfinies. Cette fonctionnalité est particulièrement utile dans des environnements complexes où diverses conditions doivent être évaluées pour déterminer le bon cours d'action, comme l'attribution de prix, la détermination des quantités ou le routage de documents.

#### Composants Clés

* **Liste des Arbres de Décision** : C'est l'interface principale où tous les arbres de décision existants sont listés. Chaque arbre de décision peut être associé à un type de document spécifique tel qu'une `FACTURE` ou un `DEVIS`.
* **Éditeur d'Arbre de Décision** : Cette interface permet la création et l'édition d'arbres de décision, où vous pouvez définir des règles, des opérateurs et des actions à entreprendre lorsque certaines conditions sont remplies.

### Interface de l'Arbre de Décision

#### Liste des Arbres de Décision

La liste des Arbres de Décision affiche tous les arbres de décision disponibles. Chaque entrée montre :

* **Nom** : Le nom de l'arbre de décision.
* **Type de Document** : Le type de document associé à l'arbre de décision (par exemple, `FACTURE`, `DEVIS`).

#### Éditeur d'Arbre de Décision

L'Éditeur d'Arbre de Décision vous permet de configurer des règles qui régissent comment les décisions sont prises.

**Composants de l'Éditeur d'Arbre de Décision**

* **Règles** : Chaque règle se compose de conditions et d'actions.
* **Sélectionner la Source** : Ce menu déroulant vous permet de spécifier le champ source à évaluer.
* **Sélectionner l'Opérateur** : Définit l'opérateur logique (par exemple, `<=`, `>=`, `=`, `!=`) à appliquer au champ source.
* **Résultat** : Définit le résultat ou l'action qui doit être entreprise lorsque les conditions sont remplies.
* **Ajouter une Nouvelle Ligne** : Vous permet d'ajouter des règles supplémentaires à l'arbre de décision.

#### Exemple de Configuration d'un Arbre de Décision

1. **Règle 1** :
   * **Source** : Quantité
   * **Opérateur** : `<=`
   * **Valeur** : `250000`
   * **Résultat** : Attribuer à `CATMGR_CMM`
2. **Règle 2** :
   * **Source** : Prix
   * **Opérateur** : `>`
   * **Valeur** : `500000`
   * **Résultat** : Attribuer à `DIRECTEUR_DES_ACHATS`

Chaque règle est évaluée séquentiellement, et l'action correspondante est exécutée si les conditions sont satisfaites.

### Politique de l'Arbre de Décision

La Politique de l'Arbre de Décision définit comment plusieurs règles au sein d'un arbre de décision sont traitées. Vous pouvez choisir parmi plusieurs politiques :

* **Unique** : Assure qu'une seule règle peut correspondre. Si plus d'une règle est correspondue, l'arbre de décision signalera une erreur.
* **Première** : La première règle correspondante est appliquée, et aucune règle supplémentaire n'est évaluée.
* **Priorité** : Les règles sont évaluées en fonction de leur ordre de priorité. La règle correspondante de la plus haute priorité est appliquée.
* **Collecte (somme)** : Collecte toutes les règles correspondantes et additionne les résultats.
* **Collecte (min/max/compte)** : Collecte toutes les règles correspondantes et sélectionne soit le minimum, le maximum, ou compte les occurrences.
* **Ordre des Règles** : Applique les règles dans l'ordre où elles apparaissent dans l'arbre de décision.
* **Tout** : Toute règle correspondante peut être appliquée, permettant plusieurs résultats.

#### Exemple d'une Politique d'Arbre de Décision en Action

Dans l'arbre de décision "Prix du Groupe Direct" :

* **Politique Sélectionnée** : `Première`
* Cela signifie que dès qu'une condition de règle est remplie, son action associée est appliquée, et aucune règle supplémentaire n'est évaluée.

### Exporter et Sauvegarder

* **Sauvegarder** : Sauvegarde la configuration actuelle de l'arbre de décision.
* **Exporter** : Vous permet d'exporter la configuration de l'arbre de décision, qui peut ensuite être importée dans un autre environnement ou utilisée à des fins de sauvegarde.