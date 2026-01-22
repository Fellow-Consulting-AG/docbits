# XRechnung

{% embed url="https://youtu.be/AxrHNEmmXtg" %}
DocBits E-Invoice Tutorial: Process XRechnung / ZUGFeRD (Factur-X), Validate Data & Automate Workflows
{% endembed %}

## Aperçu

Dans le panneau d'administration XRechnung, vous rencontrerez les composants clés suivants :

## 1. Transformation

### Objectif

Le processus de transformation est essentiel pour convertir les données brutes, généralement au format XML, en un format structuré qui répond à des exigences spécifiques, comme la génération d'une facture. Dans XRechnung, cela est principalement réalisé à l'aide de XSLT (Extensible Stylesheet Language Transformations). XSLT est un langage conçu pour transformer des documents XML en d'autres types de documents, comme un autre XML, HTML ou du texte brut.

### Comment ça marche

• Modèle XSLT : Le fichier XSLT définit la manière dont les données XML sont traitées et à quoi doit ressembler la sortie finale. Il applique des règles et des modèles pour extraire, manipuler et produire les données du document XML.

• Éléments et attributs : Le fichier XSLT contient des éléments et des attributs spécifiques qui contrôlent le processus de transformation. Par exemple, \<xsl:value-of> est utilisé pour extraire la valeur d'un nœud spécifique du document XML.

### Capacités d'administration

• Modification du XSLT :

• Modifier les modèles existants : Un administrateur peut modifier les modèles XSLT existants pour changer la manière dont les données XML d'entrée sont transformées. Par exemple, s'il est nécessaire d'extraire des informations supplémentaires du document XML, un administrateur peut ajouter de nouvelles règles dans le fichier XSLT.

• Créer de nouvelles versions : Si des modifications sont nécessaires, un administrateur peut créer une nouvelle version du modèle XSLT. Cela garantit que les versions précédentes restent intactes pour une référence historique ou une restauration si nécessaire.

### Exemple :

Supposons que le modèle XSLT extraie l'ID de la facture à l'aide de :

```xml
<xsl:value-of select="//INVOICE/INVOICE_ID/text()" />
```

Si un nouveau champ, tel qu'un numéro de référence client, doit être extrait, un administrateur peut ajouter :

```xml
<xsl:value-of select="//INVOICE/CUSTOMER_REFERENCE_NUMBER/text()" />
```

## 2. Aperçu

### Objectif

La fonction Aperçu permet aux administrateurs de visualiser la sortie générée par la transformation XSLT avant de la finaliser. Cette étape est cruciale pour s'assurer que les règles de transformation fonctionnent correctement et que la sortie répond aux normes requises.

### Comment ça marche

• Validation en temps réel : La fonction d'aperçu fournit un rendu en temps réel de l'aspect des données transformées lorsqu'elles sont appliquées à un document réel (comme une facture). Cela aide à détecter rapidement les erreurs ou les problèmes de formatage.

• Ajustements : Si l'aperçu montre des divergences ou des erreurs, des ajustements peuvent être effectués directement dans le fichier de transformation (XSLT).

### Capacités d'administration

• Personnalisation de l'aperçu :

• Modifier les paramètres d'aperçu : Un administrateur peut ajuster les parties de la transformation qui sont prévisualisées. Par exemple, il peut se concentrer sur des sections spécifiques du document ou tester de nouvelles règles ajoutées au modèle XSLT.

• Enregistrer et itérer : Après avoir effectué des ajustements, l'aperçu peut être actualisé pour voir les modifications. Ce processus itératif permet d'affiner jusqu'à l'obtention de la sortie souhaitée.

### Exemple :

Si un administrateur remarque que le format de la date dans l'aperçu est incorrect (par exemple, affichant AAAA-MM-JJ au lieu de JJ-MM-AAAA), il peut modifier le XSLT pour formater la date correctement et voir immédiatement le résultat dans l'aperçu.

## 3. Chemins d'extraction

### Objectif

Les chemins d'extraction définissent les chemins spécifiques au sein d'une structure XML ou JSON à partir desquels les données doivent être extraites. Ce processus est essentiel pour isoler les éléments d'information clés dans le document qui seront utilisés dans la transformation ou pour d'autres tâches de traitement.

### Comment ça marche

• XPath et JSONPath : Les chemins d'extraction utilisent des langages tels que XPath (pour XML) ou JSONPath (pour JSON) pour spécifier l'emplacement des données dans le document. Ces chemins sont essentiels pour indiquer au système exactement où trouver et comment extraire les informations requises.

### Capacités d'administration

• Définition et modification des chemins :

• Modifier les chemins existants : Un administrateur peut modifier les chemins d'extraction si la structure des données change ou si des données supplémentaires doivent être extraites. Cela peut impliquer de changer les expressions XPath ou JSONPath.

• Ajouter de nouveaux chemins : Pour de nouveaux champs ou points de données, un administrateur peut définir de nouveaux chemins d'extraction. Cela impliquerait de spécifier le chemin correct dans le document XML ou JSON.

### Exemple :

Dans un document de facture XML, si le chemin vers l'ID de la facture est défini comme :

```json
"invoice_id": "//INVOICE/INVOICE_ID/text()"
```

Et qu'un nouveau champ, tel qu'une adresse de livraison, doit être ajouté, un administrateur peut ajouter :

```json
"shipping_address": "//INVOICE/SHIPPING/ADDRESS/text()"
```
