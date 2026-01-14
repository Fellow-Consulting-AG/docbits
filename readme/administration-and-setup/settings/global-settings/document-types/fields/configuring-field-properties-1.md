# Configuration des propriétés de champ

## Instructions détaillées sur le paramétrage des propriétés telles que Obligatoire, Lecture seule, Masqué et OCR.

### Obligatoire (Required) :

<figure><img src="../../../../../.gitbook/assets/image (111).png" alt=""><figcaption></figcaption></figure>

Si un champ est marqué comme Obligatoire, cela signifie que ce champ doit être rempli avant que le document ne puisse être enregistré ou traité.

**Pour définir cette propriété :**

* Naviguez vers les paramètres du champ dans votre système DocBits.
* Activez l'option "Obligatoire" pour le champ concerné.

**Impact :**

* Ce paramètre garantit que les informations importantes sont saisies et qu'aucun document ne peut être traité sans les données requises.

### Lecture seule (Read Only) :

<figure><img src="../../../../../.gitbook/assets/image (112).png" alt=""><figcaption></figcaption></figure>

Si un champ est marqué comme Lecture seule, cela signifie que les utilisateurs peuvent voir le contenu de ce champ, mais ne peuvent y apporter aucune modification.

**Pour définir cette propriété :**

* Allez dans les options du champ. Activez l'option "Lecture seule" pour le champ souhaité.

**Impact :**

* Ce paramètre peut être utile pour protéger des informations sensibles ou pour s'assurer que des données importantes ne sont pas modifiées accidentellement.

### Masqué (Hidden) :

<figure><img src="../../../../../.gitbook/assets/image (113).png" alt=""><figcaption></figcaption></figure>

Si un champ est marqué comme "Masqué", cela signifie que le champ sera caché dans l'interface utilisateur et que les utilisateurs ne pourront ni le voir ni y accéder.

**Pour définir cette propriété :**

* Allez dans les options du champ.
* Activez l'option "Masqué" pour le champ correspondant.

**Impact :**

* Ce paramètre est souvent utilisé pour masquer des champs internes ou techniques qui ne sont pas pertinents pour l'utilisateur final ou qui ne sont nécessaires que pour le traitement interne.

### OCR (Reconnaissance Optique de Caractères) :

<figure><img src="../../../../../.gitbook/assets/image (114).png" alt=""><figcaption></figcaption></figure>

Si un champ est configuré pour l'OCR, cela signifie que le système tentera d'extraire le texte du document et de l'insérer dans ce champ. Ce paramètre est généralement utilisé pour les champs destinés à être remplis automatiquement.

**Pour configurer cela :**

* Activez l'option OCR pour le champ correspondant.
* Si nécessaire, configurez les paramètres OCR tels que la langue, la police, etc.

**Impact :**

* L'utilisation de l'OCR permet de traiter les documents automatiquement en extrayant des informations des textes et en les saisissant dans les champs appropriés, réduisant ainsi l'effort manuel et augmentant l'efficacité.

### Validation forcée (Forced validation) :

<figure><img src="../../../../../.gitbook/assets/image (115).png" alt=""><figcaption></figcaption></figure>

Configurez les règles de validation en conséquence, telles que les limites numériques, les expressions régulières ou les relations avec d'autres champs.

**Pour configurer cela :**

* Enregistrez les modifications.

**Impact :**

* La validation forcée vérifie les données saisies par rapport aux critères spécifiés pour s'assurer qu'elles sont valides. Cela aide à détecter les erreurs tôt et à améliorer la qualité des données.

### Score de correspondance (Match Score) :

<figure><img src="../../../../../.gitbook/assets/image (116).png" alt=""><figcaption></figcaption></figure>

En comparant les données saisies avec des données de référence, le score de correspondance peut aider à confirmer l'exactitude et la validité des données. Si le score de correspondance dépasse un certain seuil, la correspondance est considérée comme réussie.

**Pour configurer cela :**

* Activez l'option Match Score et définissez le seuil souhaité.
* Enregistrez les modifications.

**Impact :**

* Le score de correspondance est utilisé pour évaluer l'exactitude des correspondances entre les données saisies et les valeurs de référence. Si le score obtenu dépasse le seuil fixé, la correspondance est considérée comme réussie. Ceci est particulièrement utile pour les champs qui nécessitent une validation de données ou un appariement de données, tels que les champs contenant un nom, une adresse e-mail, etc. par exemple, lors de la vérification des données clients.

<figure><img src="../../../../../.gitbook/assets/image (117).png" alt="" width="258"><figcaption></figcaption></figure>

En configurant soigneusement ces propriétés de champ, vous pouvez optimiser les flux de travail de traitement de documents et vous assurer que vos données sont correctement saisies, protégées et traitées efficacement.
