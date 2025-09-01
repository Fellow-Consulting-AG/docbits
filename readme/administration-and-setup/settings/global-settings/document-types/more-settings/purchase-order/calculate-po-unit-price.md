# Calculer le prix unitaire de la commande

## **Aperçu**

Vous pouvez choisir de calculer le prix unitaire manuellement en divisant le montant net par la quantité, au lieu de l'extraire automatiquement du document. Cela est particulièrement utile lorsque le prix unitaire dans le bon de commande (dans Infor) diffère du prix extrait du document. De telles divergences peuvent survenir si une remise est appliquée au prix unitaire dans le bon de commande Infor, tandis que le document n'applique la remise qu'au montant net.

## **Étapes d'activation**

1.  Naviguez vers **Paramètres** -> **Paramètres globaux** -> **Types de documents**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/Calculate_PO_unit_price_1.png)
2.  Sélectionnez le type de document souhaité et cliquez sur **Plus de paramètres**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/Calculate_PO_unit_price_2.png)
3.  Dans la section **Bon de commande**, activez l'option **Calculer le prix unitaire de la commande**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/Calculate_PO_unit_price_3.png)

## Exemple :

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/Calculate_PO_unit_price_4.png)

Dans ce cas, le prix unitaire (sans la remise) est extrait du document, tandis que le bon de commande dans Infor stocke le prix unitaire avec la remise appliquée. Cela entraîne un décalage dans le prix unitaire.

Une fois le paramètre activé, le prix unitaire sera recalculé comme suit :\
**Prix unitaire = Montant net ÷ Quantité**\
Cela garantit que le prix unitaire est cohérent et correspond à la valeur prévue.
