# Exportation

## Aperçu

La page Exportation affiche toutes les configurations d'exportation configurées, y compris si elles sont actives ou inactives. À partir d'ici, les utilisateurs peuvent :

* Afficher et gérer les configurations d'exportation existantes
* Créer de nouvelles connexions d'exportation (par exemple, vers **Infor**, **Infor & IDM**, **Webhook** ou **SFTP**)
* Modifier ou supprimer les configurations d'exportation existantes

## Où le Trouver

Vous pouvez le trouver sous : **Paramètres** → **Traitement de document** → **Exportation**

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fn6ldlcI2sVUEgDdWb9U4%252Fimage.png%3Falt%3Dmedia%26token%3D8368818d-c899-4bee-ad21-a631d6be5c20\&width=768\&dpr=4\&quality=100\&sign=fbfcbd0c\&sv=2)

## **Utilisation de la Page d'Exportation**

Lorsque vous ouvrez la page d'exportation, vous verrez une liste de toutes les configurations d'exportation existantes.

Chaque ligne de la liste montre :

* **Indicateur de Statut**
  * Le **vert** signifie que l'exportation est active
  * Le **rouge** signifie que l'exportation est désactivée
* **Nom** – le nom de la configuration d'exportation
* **Type de Document** – le type de document pour lequel l'exportation est configurée
* **Sous-Organisation** – si l'exportation est limitée à une sous-organisation spécifique
* **Méthode d'Exportation** – où le document sera envoyé (par exemple, Infor, IDM, SFTP)
* **Actions** – boutons pour **modifier, supprimer** ou **activer/désactiver** la configuration

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FyN87I5gzXxwGoAqC6zMF%252Fimage.png%3Falt%3Dmedia%26token%3D7df9d573-7e57-4ace-99c6-15a83691b926\&width=768\&dpr=4\&quality=100\&sign=6221cb80\&sv=2)

#### **Règles Importantes pour la Configuration d'Exportation**

Pour chaque **type de document** **dans une organisation donnée ou une sous-organisation**, les règles suivantes s'appliquent :

* Vous ne pouvez avoir qu'**une seule exportation active Infor**
* Vous ne pouvez avoir qu'**une seule exportation active non-Infor** (par exemple, Webhook, SFTP)

Cependant, il est possible d'avoir :

* **Une exportation active Infor** _et_ **une exportation active non-Infor** en même temps pour le même type de document
* **Différentes configurations d'exportation pour différentes sous-organisations** — par exemple, une exportation Infor pour la Sous-Org A et une autre exportation Infor pour la Sous-Org B

## **Créer une Nouvelle Exportation**

Pour créer une nouvelle exportation :

1. Cliquez sur le bouton **“Nouveau”**. ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FTsHrIAUpe7EqenIzNAaJ%252Fimage.png%3Falt%3Dmedia%26token%3Dd2dbc996-b129-443c-a8df-9927a6f43a36\&width=300\&dpr=4\&quality=100\&sign=8769c331\&sv=2)
2. Sélectionnez le **Type d'Exportation** que vous souhaitez configurer (par exemple, Infor, IDM, SFTP).
3. Remplissez les champs requis en fonction du type d'exportation.
4. Enregistrez la configuration.

## Options d'export

#### Webhook

<details>

<summary>Webhook</summary>

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FCwXUqFdCbRI5lRW49ymw%252Fimage.png%3Falt%3Dmedia%26token%3D798c0f40-6c4a-4650-9320-af2c17634fe9\&width=768\&dpr=4\&quality=100\&sign=15836833\&sv=2)

#### **Descriptions de champ**

* **Titre** Le nom de la configuration d'export. Cela apparaîtra dans la liste d'exportation.
* **Sous-organisation** _(optionnel)_ Un menu déroulant avec toutes les sous-organisations disponibles.
  * Si laissé vide : s'applique à l'organisation principale.
  * Si sélectionné : l'exportation s'appliquera uniquement à la sous-organisation choisie.
* **Type de document** Menu déroulant listant tous les types de document disponibles. Cela détermine le type de document auquel s'applique cette configuration d'export.
* **URL d'export** L'URL de destination où le document doit être exporté.

</details>

#### SFTP

<details>

<summary>SFTP</summary>

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FzwUCWTdFETTvuTGl8qAn%252Fimage.png%3Falt%3Dmedia%26token%3D3f94b210-0128-4710-ae69-150a1363ce49\&width=768\&dpr=4\&quality=100\&sign=4ecd353\&sv=2)

#### **Descriptions de champ**

* **Titre** Le nom de la configuration d'export. Cela apparaîtra dans la liste d'exportation.
* **Sous-organisation** _(optionnel)_ Un menu déroulant avec toutes les sous-organisations disponibles.
  * Si laissé vide : s'applique à l'organisation principale.
  * Si sélectionné : l'exportation s'appliquera uniquement à la sous-organisation choisie.
* **Type de document** Menu déroulant listant tous les types de documents disponibles. Cela détermine à quel type de document cette configuration d'exportation s'applique.
* **Nom d'utilisateur** Le nom d'utilisateur utilisé pour s'authentifier auprès du serveur SFTP.
* **Mot de passe** Le mot de passe correspondant au compte SFTP. Assurez-vous que le compte ait un accès en écriture au dossier spécifié.
* **URL du serveur** Le nom d'hôte ou l'adresse IP du serveur SFTP cible.
* **Port** Le port utilisé pour se connecter au serveur SFTP.
* **Dossier** Le chemin sur le serveur SFTP où les documents doivent être téléchargés (par exemple, `/incoming/invoices/`). Doit exister et être inscriptible.
*   **Fichier XSLT (optionnel)**

    Le **fichier XSLT** permet la transformation du format d'exportation par défaut de DocBits.

    * **Quand l'utiliser :** Uniquement si le système récepteur nécessite une structure différente ou un format spécifique différent du format par défaut de DocBits.
    * **Laissez-le vide** si le format d'exportation par défaut répond aux exigences.

</details>

#### Exportation Infor vers SFTP

<details>

<summary>Exportation Infor vers SFTP</summary>

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FU0W4Qdy7ZlNoCn3E9wX5%252Fimage.png%3Falt%3Dmedia%26token%3D33673a12-55c4-479b-8ca8-b7c95e7a6a89\&width=768\&dpr=4\&quality=100\&sign=4af07f48\&sv=2)

#### **Descriptions des Champs**

* **Titre** Le nom de la configuration d'exportation. Cela apparaîtra dans la liste d'exportation.
* **Sous-Organisation** _(optionnel)_ Un menu déroulant avec toutes les sous-organisations disponibles.
  * Si laissé vide : s'applique à l'organisation principale.
  * Si sélectionné : l'exportation s'appliquera uniquement à la sous-organisation choisie.
* **Type de Document** Menu déroulant listant tous les types de documents disponibles. Cela détermine à quel type de document s'applique cette configuration d'exportation.
* **Fichier de Mappage IDM** Sélectionnez un fichier de mappage dans le gestionnaire de fichiers. [Besoin d'aide pour en créer un ? Consultez le Guide de Mappage IDM](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file)
* **Fichier de Mappage BOD** Sélectionnez un fichier de mappage dans le gestionnaire de fichiers. [Besoin d'aide pour en créer un ? Consultez le Guide de Mappage BOD](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file)
* **Dossier** Le chemin sur le serveur SFTP où les documents doivent être téléversés (par exemple, `/incoming/invoices/`). Doit exister et être inscriptible.

</details>

#### **SMB**

<details>

<summary>SMB</summary>

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F6e4B9BWQWgHvcHhduXKb%252Fimage.png%3Falt%3Dmedia%26token%3D09e9534e-9268-4221-bd7b-89b621c80670\&width=768\&dpr=4\&quality=100\&sign=b03835a\&sv=2)

#### **Descriptions de champ**

* **Titre** Le nom de la configuration d'export. Cela apparaîtra dans la liste d'exportation.
* **Sous-organisation** _(optionnel)_ Un menu déroulant avec toutes les sous-organisations disponibles.
  * Si laissé vide : s'applique à l'organisation principale.
  * Si sélectionné : l'exportation s'appliquera uniquement à la sous-organisation choisie.
* **Type de document** Menu déroulant listant tous les types de documents disponibles. Cela détermine le type de document auquel s'applique cette configuration d'exportation.
* **Nom d'utilisateur** Le nom d'utilisateur utilisé pour se connecter au partage SMB.
* **Mot de passe** Le mot de passe correspondant pour l'authentification SMB.
* **URL du serveur** L'adresse du serveur SMB.
* **Port** Numéro de port utilisé pour accéder au partage SMB.
* **Dossier** Le chemin du dossier dans le partage SMB où les documents doivent être enregistrés (par exemple, `/incoming/invoices/`). Doit exister et être inscriptible.
*   **Fichier de mappage JPL (Optionnel)**

    Le fichier **JPL** est utilisé pour définir une transformation des données exportées avant qu'elles ne soient écrites dans le partage SMB.

    * **Quand utiliser :** Uniquement lorsque les données du document exporté doivent être ajustées pour correspondre au format externe ou aux attentes du système.
    * **Laissez-le vide** s'il n'est pas nécessaire de faire de transformation.

</details>

#### **Infor IDM**

<details>

<summary>Infor IDM</summary>

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FQ1AtdmTRZr1sGkH6oLwP%252Fimage.png%3Falt%3Dmedia%26token%3D720a4184-3f91-4b70-b3da-b846f3cce030\&width=768\&dpr=4\&quality=100\&sign=dc678c2c\&sv=2)

#### **Descriptions de champs**

* **Titre** Le nom de la configuration d'export. Cela apparaîtra dans la liste d'export.
* **Sous-Organisation** _(optionnel)_ Un menu déroulant avec toutes les sous-organisations disponibles.
  * Si laissé vide : s'applique à l'organisation principale.
  * Si sélectionné : l'exportation s'appliquera uniquement à la sous-organisation choisie.
* **Type de document** Menu déroulant listant tous les types de document disponibles. Cela détermine le type de document auquel s'applique cette configuration d'export.
* **Fichier de mappage ION** Sélectionnez un fichier de mappage dans le gestionnaire de fichiers.
* **Fichier de mappage IDM** Sélectionnez un fichier de mappage dans le gestionnaire de fichiers. [Besoin d'aide pour en créer un ? Consultez le Guide de mappage IDM](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file)
* **Bascule Cloud / Sur Site** Un interrupteur pour indiquer le type de déploiement Infor :
  * **Cloud** : Sélectionnez ceci si le client utilise Infor CloudSuite.
  * **Sur Site** : Sélectionnez ceci si Infor est auto-hébergé.

</details>

#### **Infor ION**

<details>

<summary>Infor ION</summary>

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FcYDXwDYH4RSc5vcY4fmr%252Fimage.png%3Falt%3Dmedia%26token%3Da9cfac80-9795-4e8f-a664-e268c9b4856c\&width=768\&dpr=4\&quality=100\&sign=5a4b0bd0\&sv=2)

#### **Descriptions de champ**

* **Titre** Le nom de la configuration d'export. Cela apparaîtra dans la liste d'export.
* **Sous-Organisation** _(optionnel)_ Un menu déroulant avec toutes les sous-organisations disponibles.
  * Si laissé vide : s'applique à l'organisation principale.
  * Si sélectionné : l'exportation s'appliquera uniquement à la sous-organisation choisie.
* **Type de document** Menu déroulant listant tous les types de documents disponibles. Cela détermine le type de document auquel s'applique cette configuration d'export.
* **Fichier de mappage ION** Sélectionnez un fichier de mappage dans le gestionnaire de fichiers.
* **Fichier de mappage BOD** Sélectionnez un fichier de mappage dans le gestionnaire de fichiers. [Besoin d'aide pour en créer un ? Consultez le Guide de mappage BOD](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file)
* **Basculer Cloud / Sur Site** Un interrupteur pour indiquer le type de déploiement Infor :
  * **Cloud** : Sélectionnez ceci si le client utilise Infor CloudSuite.
  * **Sur Site** : Sélectionnez ceci si Infor est auto-hébergé.

</details>

#### Infor IDM + ION BOD

<details>

<summary>Infor IDM + ION BOD</summary>

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FY13EX2xxOKLZzliAAHB0%252Fimage.png%3Falt%3Dmedia%26token%3D94335922-6342-405f-8c6d-29fdf2f31a2e\&width=768\&dpr=4\&quality=100\&sign=c0322806\&sv=2)

#### **Descriptions des champs**

* **Titre** Le nom de la configuration d'export. Cela apparaîtra dans la liste d'export.
* **Sous-Organisation** _(optionnel)_ Un menu déroulant avec toutes les sous-organisations disponibles.
  * Si laissé vide : s'applique à l'organisation principale.
  * Si sélectionné : l'export s'appliquera uniquement à la sous-organisation choisie.
* **Type de document** Menu déroulant répertoriant tous les types de documents disponibles. Cela détermine le type de document auquel s'applique cette configuration d'export.
* **Fichier de mappage ION** Sélectionnez un fichier de mappage dans le gestionnaire de fichiers.
* **Fichier de mappage IDM** Sélectionnez un fichier de mappage dans le gestionnaire de fichiers. [Besoin d'aide pour en créer un ? Consultez le Guide de mappage IDM](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file)
* **Fichier de mappage BOD** Sélectionnez un fichier de mappage dans le gestionnaire de fichiers. [Besoin d'aide pour en créer un ? Consultez le Guide de mappage BOD](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file)
* **Basculer Cloud / Sur Site** Un interrupteur pour indiquer le type de déploiement Infor :
  * **Cloud** : Sélectionnez ceci si le client utilise Infor CloudSuite.
  * **Sur Site** : Sélectionnez ceci si Infor est auto-hébergé.

</details>

### Pour les clients Infor CloudSuite

#### Infor IDM + LN

<details>

<summary>Infor IDM + LN</summary>

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F4SfGDqhA4KDrPfJ5vcsT%252Fimage.png%3Falt%3Dmedia%26token%3D4833c0dc-af8b-48a1-a977-6cc8ded20277\&width=768\&dpr=4\&quality=100\&sign=6301596\&sv=2)

#### **Descriptions de champs**

* **Titre** Le nom de la configuration d'exportation. Cela apparaîtra dans la liste d'exportation.
* **Sous-Organisation** _(optionnel)_ Un menu déroulant avec toutes les sous-organisations disponibles.
  * Si laissé vide : s'applique à l'organisation principale.
  * Si sélectionné : l'exportation s'appliquera uniquement à la sous-organisation choisie.
* **Type de document** Menu déroulant répertoriant tous les types de document disponibles. Cela détermine le type de document auquel s'applique cette configuration d'exportation.
* **Fichier de mappage ION** Sélectionnez un fichier de mappage dans le gestionnaire de fichiers.
* **Fichier de mappage IDM** Sélectionnez un fichier de mappage dans le gestionnaire de fichiers. [Besoin d'aide pour en créer un ? Consultez le Guide de mappage IDM](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file)
* **Fichier de mappage LN** Sélectionnez un fichier de mappage dans le gestionnaire de fichiers. [Besoin d'aide pour en créer un ? Consultez l'exemple de mappage LN](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/ln/example-export-ln)

</details>

#### Infor IDM + M3

<details>

<summary>Infor IDM + M3</summary>

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FAN4T0aQEoogbUA8PUgy9%252Fimage.png%3Falt%3Dmedia%26token%3Da2b91153-858f-4711-abcc-4ed7ad60d49a\&width=768\&dpr=4\&quality=100\&sign=bb6bda83\&sv=2)

#### **Descriptions des champs**

* **Titre** Le nom de la configuration d'export. Cela apparaîtra dans la liste d'export.
* **Sous-Organisation** _(optionnel)_ Un menu déroulant avec toutes les sous-organisations disponibles.
  * Si laissé vide : s'applique à l'organisation principale.
  * Si sélectionné : l'export s'appliquera uniquement à la sous-organisation choisie.
* **Type de document** Menu déroulant listant tous les types de document disponibles. Cela détermine le type de document auquel s'applique cette configuration d'export.
* **Fichier de mappage ION** Sélectionnez un fichier de mappage dans le gestionnaire de fichiers.
* **Fichier de mappage IDM** Sélectionnez un fichier de mappage dans le gestionnaire de fichiers. [Besoin d'aide pour en créer un ? Consultez le Guide de Mappage IDM](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file)
* **Fichier de mappage M3** Sélectionnez un fichier de mappage dans le gestionnaire de fichiers. [Besoin d'aide pour en créer un ? Consultez l'Exemple de Mappage M3](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/m3/example-export-m3)

</details>

#### Infor IDM + M3 (toml)

<details>

<summary>Infor IDM + M3 (toml)</summary>

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FCdoduCkkbnomw3ahZgul%252Fimage.png%3Falt%3Dmedia%26token%3D4e5c7d08-5eaf-4c3e-9918-5cce58d8e3b3\&width=768\&dpr=4\&quality=100\&sign=e984c4e0\&sv=2)

#### **Descriptions des champs**

* **Titre** Le nom de la configuration d'export. Cela apparaîtra dans la liste d'exportation.
* **Sous-Organisation** _(optionnel)_ Un menu déroulant avec toutes les sous-organisations disponibles.
  * Si laissé vide : s'applique à l'organisation principale.
  * Si sélectionné : l'exportation s'appliquera uniquement à la sous-organisation choisie.
* **Type de document** Menu déroulant listant tous les types de documents disponibles. Cela détermine le type de document auquel s'applique cette configuration d'exportation.
* **Fichier de mappage ION** Sélectionnez un fichier de mappage dans le gestionnaire de fichiers.
* **Fichier de mappage IDM** Sélectionnez un fichier de mappage dans le gestionnaire de fichiers. [Besoin d'aide pour en créer un ? Consultez le Guide de Mappage IDM](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file)
* **Fichier de mappage M3 toml** Sélectionnez un fichier de mappage dans le gestionnaire de fichiers ou utilisez l'option Toml sélectionné pour utiliser un toml créé avec le gestionnaire de règles. [Besoin d'aide pour en créer un ? Consultez le Guide du Gestionnaire de Règles](https://docs.docbits.com/administration-and-setup/settings/document-processing/rule-manager)

</details>
