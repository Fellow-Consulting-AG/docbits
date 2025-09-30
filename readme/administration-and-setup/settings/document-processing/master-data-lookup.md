# Validation des données fournisseur

## Vue d'ensemble

La "Validation des données fournisseur" dans vos Paramètres de Traitement des documents permet une approche complète et intégrée de la gestion et de la validation de vos données de documents en les synchronisant avec votre système Infor ERP. Voici comment elle contribue à rationaliser la validation et l'amélioration du traitement des documents au sein de votre environnement ERP :

1. **Gestion centralisée des données**: Cette fonction agit comme un référentiel central où les données provenant de diverses sources telles que les fournisseurs, les adresses clients, les codes fiscaux, etc., peuvent être stockées et gérées. Elle fournit un point de référence unique pour toutes les données de référence, garantissant cohérence et exactitude dans toute votre organisation.
2. **Validation par rapport aux données ERP**: En synchronisant des données de référence telles que les informations fournisseurs d'Infor vers DocBits, vous pouvez valider automatiquement les données extraites des documents par rapport à vos données ERP. Cela garantit que les informations traitées (comme les noms de fournisseurs, les adresses et les codes fiscaux) correspondent aux données détenues dans votre système ERP, minimisant ainsi les erreurs et les divergences.
3. **Facilite l'automatisation**: Disposer d'un système robuste de validation des données de référence aide à automatiser le traitement des documents entrants. Par exemple, les bons de commande ou factures peuvent être automatiquement vérifiés pour l'exactitude des données fournisseur, approuvés s'ils correspondent, ou signalés pour examen en cas d'écarts.
4. **Améliore l'intégrité des données**: Des mises à jour régulières de votre système ERP vers la validation des données de référence garantissent que les données utilisées pour le traitement des documents sont à jour. Cela réduit le risque de traiter des documents sur la base d'informations obsolètes, améliorant ainsi l'intégrité globale des transactions commerciales.
5. **Efficacité dans le traitement des documents**: Avec des données de référence directement liées et constamment actualisées, le traitement des documents devient plus efficace. Les documents peuvent être automatiquement classés et acheminés en fonction de critères spécifiques définis dans les données de référence, tels que des conditions fournisseur particulières ou des réglementations fiscales applicables à différents types de transactions.

{% hint style="info" %}
Voir ici comment Importer [les données de référence](../../../infor-integration-and-configuration/importing-customer-master-data/)
{% endhint %}

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/master_data_lookup_1.png)

## **Accéder à la Validation des données fournisseur**

Pour accéder à la section **Validation des données fournisseur**, accédez à :\
**Paramètres → Traitement des documents → Validation des données fournisseur**

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_mater_data_lookup.png)

## **Paramètres**

Pour accéder aux paramètres de la **Validation des données fournisseur**, cliquez sur **Paramètres** situé dans le coin inférieur gauche de l'écran **Validation des données fournisseur**.\
Les options de configuration suivantes sont disponibles :

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/master_data_lookup_2.png)

### **BOD du fournisseur**

* **Autoriser la synchronisation de plusieurs comptes fournisseurs**:
  * **Activé**:\
    Un même fournisseur peut avoir plusieurs éléments `<FinancialParty>` dans le BOD (Business Object Document), souvent en raison de plusieurs IBAN ou comptes financiers associés. Lorsque ce paramètre est activé, toutes les entrées `<FinancialParty>` du fournisseur seront extraites et enregistrées dans la table des fournisseurs, permettant de stocker plusieurs attributs financiers.
  * **Désactivé**:\
    Seul le dernier élément `<FinancialParty>` trouvé pour le fournisseur dans le BOD sera extrait. Tous les attributs financiers précédents (par exemple, des IBAN supplémentaires) seront ignorés, et seules les données de la dernière occurrence seront enregistrées dans la table des fournisseurs.

### **Suppression du bon de commande**

*   **Supprimer le bon de commande après**: Spécifiez quand les bons de commande clôturés doivent être supprimés. Après la période sélectionnée, les enregistrements seront supprimés automatiquement.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/master_data_lookup_3.png)
