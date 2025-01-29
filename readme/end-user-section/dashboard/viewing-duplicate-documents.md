# Gestion des Factures Dupliquées Dans DocBits

## Paramètre pour Activer la Gestion des Factures Dupliquées

Allez dans _Paramètres → Types de Documents → Facture → Plus de Paramètres_ comme indiqué dans la capture d'écran ci-dessous

<figure><img src="../../.gitbook/assets/duplicate_invoice handling.png" alt=""><figcaption></figcaption></figure>

L'utilisateur a deux options pour détecter les factures dupliquées:

1. **Détection des documents en double**\
   Cette fonctionnalité vérifie les documents dupliqués téléchargés sur DocBits en fonction des critères sélectionnés. Si les critères sélectionnés correspondent entre les documents, le système marquera le document comme un duplicata.
2.  **Détection des factures en double**\
    Cette fonctionnalité nécessite que les factures fournisseurs soient synchronisées d'Infor vers DocBits. Elle compare les numéros de facture dans le tableau de bord des factures DocBits avec ceux d'Infor. Si le même numéro de facture est téléchargé plus d'une fois, il sera marqué comme un duplicata.

    <mark style="color:red;">**REMARQUE**</mark><mark style="color:red;">:</mark> L'utilisation de la fonctionnalité **Détection des factures en double** entraînera un frais de crédit supplémentaire.

Une fois le paramètre activé, l'utilisateur peut sélectionner les critères pour la détection des duplicatas

## Factures Dupliquées sur le Tableau de Bord

Une fois la Détection des Duplicatas activée dans les paramètres, le tableau de bord affichera une icône pour toutes les factures identifiées comme des duplicatas en fonction des critères spécifiés. Cliquer sur cette icône ouvrira les enregistrements dupliqués dans une vue à écran partagé pour une comparaison facile

<figure><img src="../../.gitbook/assets/duplicate_invoice handling2.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/duplicate_invoice handling2b.png" alt=""><figcaption></figcaption></figure>

Lorsque l'utilisateur ouvre le document, une barre d'avertissement s'affiche pour les factures dupliquées comme indiqué dans la capture d'écran

<figure><img src="../../.gitbook/assets/duplicate_invoice handling3.png" alt=""><figcaption></figcaption></figure>
