# Paramètres de l'OCR

## Aperçu

Dans les **paramètres de l'OCR (Reconnaissance Optique de Caractères)**, vous pouvez configurer comment l'OCR est appliqué lors du traitement des documents. Cela inclut la spécification de la qualité minimale requise, le choix d'utiliser du texte intégré (e-text), la sélection de la version de l'OCR, et plus encore. Cette page fournit une explication détaillée de tous les paramètres disponibles.

## Comment accéder aux Paramètres de l'OCR

Pour accéder aux paramètres de l'OCR :

*   Naviguez vers : **Paramètres** → **Traitement des documents** → **Paramètres de l'OCR**

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_ocr.png)

## Qualité OCR

Dans cette section, vous pouvez définir la qualité minimale du document requise pour le traitement OCR en ajustant le curseur de qualité. Déplacez le curseur vers la gauche ou vers la droite pour diminuer ou augmenter le seuil de qualité, respectivement.

Si un document ne répond pas au niveau de qualité défini, DocBits propose trois options pour le gérer :

* **Exécuter quand même**\
  Le document sera traité indépendamment de sa qualité.
* **Exécuter à nouveau après confirmation**\
  **DocBits** fera une pause et vous demandera de confirmer si vous souhaitez continuer le traitement.
* **Lancer une erreur**\
  Le traitement du document s'arrêtera complètement, et un message d'erreur s'affichera, indiquant que le document n'a pas atteint le seuil de qualité requis.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ocr_settings_1.png)

## Paramètres généraux de l'OCR

* **Utiliser l'E-Texte s'il est disponible**\
  Lorsqu'il est activé, **DocBits** utilisera le texte électronique intégré (par exemple, provenant de PDF) au lieu d'effectuer l'OCR. Cela améliore à la fois la vitesse et la précision, car le texte est extrait directement sans nécessiter de traitement OCR.
* **Utiliser DESKEW s'il est disponible**\
  Cette option corrige automatiquement l'alignement des documents numérisés. Redresser les images inclinées aide à améliorer la précision de l'OCR.
*   **Version AI OCR**\
    Vous permet de sélectionner une version spécifique du moteur OCR basé sur l'IA.\
    Cela peut être utile si :

    * Vous n'obtenez pas les résultats souhaités avec la version actuellement sélectionnée.
    * Vous dépannez des problèmes liés aux performances ou à la précision de l'OCR.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ocr_settings_2.png)

## Paramètres OCR pour les tableaux

* **Utiliser les données de l'IA pour les tableaux si elles sont disponibles**\
  Lorsqu'il est activé, DocBits utilisera les données OCR pour les tableaux au lieu du texte électronique intégré (E-Text) — même si le paramètre **Utiliser l'E-Texte s'il est disponible** est activé.

## Paramètres OCR pour les champs d'en-tête

* **Utiliser l'extraction par règles**\
  DocBits appliquera vos règles d'extraction prédéfinies pour identifier les champs d'en-tête.
* **Utiliser l'extraction de l'IA**\
  DocBits utilisera l'IA pour détecter et extraire automatiquement les champs d'en-tête.

**Ordre d'exécution :**\
Si les deux options sont activées, **DocBits** effectuera l'extraction dans l'ordre suivant :\
**Extraction par règles → Extraction de l'IA**\
\
<mark style="color:red;">**Remarque**</mark> : Pour de meilleurs résultats et un comportement cohérent, activez les deux options. Cela permet à **DocBits** d'utiliser à la fois des méthodes basées sur des règles et des méthodes basées sur l'IA en combinaison lors de l'extraction des en-têtes.
