# Architecture

<figure><img src=".gitbook/assets/DocBits_D_Doc2-Infor-1.png" alt=""><figcaption></figcaption></figure>

Doc**Bits** s'intègre parfaitement avec Infor LN/M3 via l'API ION, ION Desk et les BODs standard d'Infor. Notre intégration API nous permet d'exporter des données vers Infor et d'effectuer une validation des données maîtres dans Doc**Bits**.

## Exportation de données vers Infor

Nous utilisons l'API ION pour envoyer le PDF avec les attributs à IDM et le BOD Sync.CaptureDocument à ION Desk. Dans ION Desk, nous transformons le Sync.CaptureDocument en BODs cibles souhaités en fonction du type de document en cours de traitement. Ces BODs Infor transformés sont ensuite automatiquement importés dans LN ou M3.

## Validation des données maîtres dans DocBits

Pour identifier le fournisseur ou comparer/corréler les lignes de commande, nous activons un déclencheur dans LN/M3 qui envoie les BODs Sync.RemitToPartyMaster, Sync.SupplierPartyMaster et Sync.PurchaseOrder à Doc**Bits**. Nous configurons ce processus dans ION Desk en définissant le flux de données vers un point de connexion spécifique à Doc**Bits**.

\
