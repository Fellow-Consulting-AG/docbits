# Dépannage de l'extraction de table

## **Étape 1 : Ouvrir la vue OCR pour les mauvais résultats d'extraction**

Si les résultats de l'entraînement d'extraction de table ne sont pas bons :

1. Ouvrez la **vue OCR** en cliquant sur l'icône de la loupe avec **OCR** écrit dessus.
2. Passez en revue les résultats de l'extraction et voyez si le processus OCR peut améliorer la capture des données.
3. Si les résultats semblent toujours mauvais, essayez un autre document pour vérifier si le problème est spécifique au document.
4. Si le problème est spécifique au document, utilisez un autre document pour l'extraction.
   * Si le problème persiste, suivez les étapes suivantes.

## **Étape 2 : Vérifier la disponibilité de l'E-Text**

1. Vérifiez si le document contient de l'**e-text** disponible.
   * Vous pouvez vérifier cela en utilisant un outil comme **Adobe Acrobat**.
   * Si le document contient de l'e-text, suivez **l'Étape 3**.
   * Si le document ne contient pas d'e-text, suivez **l'Étape 4**.

## **Étape 3 : Activer l'extraction de l'E-Text**

Si le document contient de l'e-text, vous avez deux options :

1. **Activer l'extraction de l'e-text pour ce fournisseur uniquement** :
   * Revenez à la **Validation des champs des documents**.
   * Cliquez sur le carré avec les trois points dans la barre d'outils de gauche.
   * Ici, activez l'option **Utiliser l'e-text si disponible** pour l'activer uniquement pour ce fournisseur.
2. **Activer l'extraction de l'e-text pour tous les fournisseurs** :
   * Allez dans **Paramètres** > **Traitement de document** > **Paramètres OCR**.
   * Dans cette section, vous trouverez l'option **Utiliser l'e-text si disponible** et pouvez l'activer pour tous les fournisseurs.
3. Après avoir activé l'extraction de l'e-text, réessayez l'**entraînement d'extraction de table**.
   * Si les résultats s'améliorent, le problème est résolu.
   * Si les résultats ne sont toujours pas bons, passez à **l'Étape 4**.

## **Étape 4 : Pas d'E-Text disponible - Changer la version de l'OCR AI**

Si le document ne contient pas d'e-text disponible :

1. Allez dans **Paramètres** > **Traitement de document** > **Paramètres OCR**.
2. Changez la **Version de l'OCR AI** pour une version différente.
3. Retournez à l'**Entraînement d'extraction de table** et réessayez.
4. Si le résultat est meilleur :
   * Vérifiez d'autres documents provenant de différents fournisseurs pour vous assurer que les résultats d'extraction pour ces fournisseurs ne sont pas impactés par ce changement.
   * **Soyez prudent, car ce changement peut affecter les résultats d'extraction d'autres fournisseurs.**
   * Ce changement peut avoir un impact sur d'autres fournisseurs, alors assurez-vous de vérifier les résultats minutieusement pour vous assurer qu'il n'affecte pas négativement les extractions de documents d'autres fournisseurs.
5. Si le résultat n'a pas été amélioré après avoir changé la version de l'OCR AI, veuillez **nous contacter** pour obtenir une assistance supplémentaire.
