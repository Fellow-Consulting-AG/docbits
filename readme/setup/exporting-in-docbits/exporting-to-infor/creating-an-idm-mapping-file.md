# Création d'un fichier de mappage IDM

Une fois obtenu, ouvrez le fichier dans votre éditeur de fichiers de choix. Pour ce guide, VSCode sera utilisé.

### Modifier le fichier de mappage

Vérifiez que le code de type de document est identique à celui de DocBits (comme pour le fichier de mappage BOD, il doit correspondre au nom du type de document dans l'URL des paramètres de champ) et vérifiez également le nom du type de document tel qu'il devrait être dans le Gestionnaire de documents (IDM) dans Infor.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FWHO0vg2W36yVFBq0ay0wBMFVzMfT6pNvHklt0o8N4tqUpM03jXJm2fykuYjyZh0z4wFTO4Eaeh39-D03re3a9utegrdVdsjHBfucmALA3B7YBWd92-9bcYr543G4MWftv0RosvTgFP3J6NNmLZAz5Dc\&width=768\&dpr=4\&quality=100\&sign=5bb93fe7\&sv=2)

**FYI** : Il est indiqué que le nom du type de document dans IDM est M3\_SupplierInvoice, cela est dû au fait qu'il s'agit d'un exemple d'une instance M3. Cela peut changer en fonction de l'utilisation de LN ou M3, ainsi que de votre configuration IDM spécifique.

Vérifiez l'ID de l'entreprise et vérifiez l'ID de l'entité (SF\_MDS\_EntityType), cette valeur doit être la même que celle du fichier de mappage BOD.

Assurez-vous que IndexFieldFromDocBits=IDMAttributeID (vérifiez si DocBits à gauche dans les paramètres de champ correspond à IDM à droite dans Type de document → Attributs).

### Exportation de fichiers XML et EDI

Pour exporter le fichier XML/EDI original avec le PDF généré, vous devez modifier le fichier de mappage IDM, dans la configuration d'exportation. Tout d'abord, mettez à jour la section **Static\_Values** en ajoutant le préfixe et l'extension du fichier. Après cela, définissez le mappage réel pour garantir la bonne configuration d'exportation.

Si une exportation pour les factures vers IDM est déjà configurée, le PDF généré devrait déjà être inclus dans l'exportation. Si vous n'avez pas besoin du fichier XML, vous pouvez passer à la partie suivante. Cependant, si vous avez besoin du fichier XML, suivez les étapes ci-dessous.

#### Mise à jour des valeurs statiques :

Trouvez le champ **Static\_Values** et ajoutez ce qui suit :

```
,EDI_FILE_PREFIX,XML_FILE_PREFIX,PDF_FILE_PREFIX,PDF_FILE_EXTENSION,EDI_FILE_EXTENSION,XML_FILE_EXTENSION
```

Ensuite, ajoutez les entrées suivantes sous **SV\_ACLString** :

```
SV_EDI_FILE_PREFIX=EDI_810_
SV_XML_FILE_PREFIX=XML_810_
SV_PDF_FILE_PREFIX=INV_EDI_
SV_PDF_FILE_EXTENSION=.pdf
SV_EDI_FILE_EXTENSION=.xml
SV_XML_FILE_EXTENSION=.xml
```

Après cela, ajoutez le mappage réel, en vous assurant que le type de document d'exportation correspond au type de fournisseur IDM.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F6k18wa4zSaSZkvfEKMwW%252Fimage.png%3Falt%3Dmedia%26token%3De6c49d36-44b9-4d18-9d22-63d30205dbd5\&width=768\&dpr=4\&quality=100\&sign=3ac8bc32\&sv=2)

#### Mappage XML

Ajoutez le mappage suivant en bas du fichier :

```
EMBEDDED_FILES_EXPORT = TRANSFORMED, XML
EFE_TRANSFORMED_SOURCE_NAME = Transformed.xml
EFE_TRANSFORMED_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_TRANSFORMED_EXPORT_FILENAME = SV_XML_FILE_PREFIX+IF_INVOICE_ID+SV_XML_FILE_EXTENSION

EFE_XML_SOURCE_NAME = XML_DOCUMENT.xml
EFE_XML_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_XML_EXPORT_FILENAME = SV_XML_FILE_PREFIX+IF_INVOICE_ID+SV_XML_FILE_EXTENSION
```

Remarque : Assurez-vous que **export\_doc\_type** est défini sur le type de facture IDM. Dans cet exemple, il est défini pour **M3**.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FlXToG368VI7Fc7HDguCn%252Fimage.png%3Falt%3Dmedia%26token%3Dcb153977-34e1-4f5f-a416-60e3141b4aca\&width=768\&dpr=4\&quality=100\&sign=b7d9585c\&sv=2)

#### Mappage EDI

Ajoutez le mappage suivant en bas du fichier :

```
EMBEDDED_FILES_EXPORT = TRANSFORMED, EDI
EFE_TRANSFORMED_SOURCE_NAME = Transformed.xml
EFE_TRANSFORMED_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_TRANSFORMED_EXPORT_FILENAME = SV_XML_FILE_PREFIX+IF_INVOICE_NUMBER+SV_EDI_FILE_EXTENSION

EFE_EDI_SOURCE_NAME = EDI.edi
EFE_EDI_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_EDI_EXPORT_FILENAME = SV_EDI_FILE_PREFIX+IF_INVOICE_NUMBER+SV_EDI_FILE_EXTENSION
```

Remarque : Assurez-vous que **export\_doc\_type** est défini sur le type de facture IDM. Dans cet exemple, il est défini pour **M3**.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FSrF54zkGq6aYYuJq1KAI%252Fimage.png%3Falt%3Dmedia%26token%3D403c9bfa-7e97-4d3c-a4b0-1bb82b98fe50\&width=768\&dpr=4\&quality=100\&sign=a768865f\&sv=2)

#### Gestionnaire de documents dans Infor

Allez dans le Gestionnaire de documents et sélectionnez le nom du type de document actuel que vous essayez d'exporter, par exemple, Facture fournisseur.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FEV3uw3R1L6_RRANB7FRLwtUFMbv_KGtL4x6kAk6lEYhwI90UeG2uWqFD2Azpxv-SRFl9zfvdratOZbXxp2D1-SryLo3Boj2x9Xc4PQXJ6vUhX5c9pvhv4XHuCk-qMK51DZ885vRUJ5dwES7k84uhoyk\&width=768\&dpr=4\&quality=100\&sign=a2f25ec9\&sv=2)

Cliquez sur l'icône ci-dessus, puis cliquez sur Administration → Type de document et trouvez le type de document dont vous avez besoin dans la liste.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FldsuINS9SCUQm3E57s8j_95gzBGwHQFavcf6d3myg6tuVxRoQHtq8R-6we5OEJ63swDxwPc9w7hbySWqWdfaMsGdQpn99m6EchPY5f5DzXEj-8mjocwPNtdJVNP34CuPvw0JIImDgFX1Q05M8-ogZo8\&width=768\&dpr=4\&quality=100\&sign=a1149783\&sv=2)

Comme montré ci-dessous, vous verrez ensuite le nom du type de document tel qu'il est dans INFOR.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FKSreWGS7TqdMP64BqtufM24xk0RDnNDHUZapnPsSuRj_umPJ3icll89KI2RYpbtet2F6ccL8QfYbl27-2j1nQPwQ0z-Nq873c4Tv72ee9AJhKMxynIUxmJKKsQQCupW_dpRfw_5BXm0WvAnw4HOALmw\&width=768\&dpr=4\&quality=100\&sign=62bfe0a6\&sv=2)

Assurez-vous que c'est ainsi que le nom est affiché dans le fichier de mappage IDM.

### Télécharger le fichier sur DocBits

Une fois le fichier préparé, téléchargez-le dans votre configuration d'exportation dans DocBits. Cela est disponible dans Paramètres → Exporter.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FrUHhvImiWamK6JxnWSPL4JEioAJq3AmvdsubJDo-DoDV9F_i5mZ42YDnjqZUYKYSJu1Cetc_4fLwlvvmoZXYIzmBf3hoyW6RjfP9HQ8FkNDhW1IbLHvNTCHWFRaeCECdZ97u79-Eu37TvzqnqGPEayM\&width=768\&dpr=4\&quality=100\&sign=a13b8c88\&sv=2)
