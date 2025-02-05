# Creazione di un file di mapping IDM

Una volta ottenuto, apri il file nel tuo editor di file preferito. Per questo walkthrough, verrà utilizzato VSCode.

### Modifica il file di mapping

Controlla che il codice del tipo di documento sia come in DocBits (come nel file di mapping BOD, dovrebbe corrispondere al nome del tipo di documento nell'URL delle impostazioni del campo) e controlla anche il nome del tipo di documento come dovrebbe essere in Document Manager (IDM) in Infor.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FWHO0vg2W36yVFBq0ay0wBMFVzMfT6pNvHklt0o8N4tqUpM03jXJm2fykuYjyZh0z4wFTO4Eaeh39-D03re3a9utegrdVdsjHBfucmALA3B7YBWd92-9bcYr543G4MWftv0RosvTgFP3J6NNmLZAz5Dc\&width=768\&dpr=4\&quality=100\&sign=5bb93fe7\&sv=2)

**FYI**: Si afferma che il nome del tipo di documento in IDM è M3\_SupplierInvoice, questo è dovuto al fatto che si tratta di un esempio da un'istanza M3. Questo può cambiare a seconda che tu utilizzi LN o M3, così come la tua specifica configurazione IDM.

Controlla l'ID aziendale e controlla l'ID entità (SF\_MDS\_EntityType), questo valore dovrebbe essere lo stesso di quello che era nel file di mapping BOD.

Assicurati che IndexFieldFromDocBits=IDMAttributeID (controlla se DocBits a sinistra nelle impostazioni del campo corrisponde a IDM a destra in Tipo di documento → Attributi).

### Esportazione di file XML e EDI

Per esportare il file XML/EDI originale insieme al PDF generato, è necessario modificare il file di mapping IDM, nella configurazione di esportazione. Prima di tutto, aggiorna la sezione **Static\_Values** aggiungendo il prefisso e l'estensione del file. Dopo di che, definisci il mapping effettivo per garantire la corretta configurazione di esportazione.

Se un'esportazione per le fatture in IDM è già impostata, il PDF generato dovrebbe già essere incluso nell'esportazione. Se non hai bisogno del file XML, puoi saltare la parte successiva. Tuttavia, se hai bisogno del file XML, segui i passaggi seguenti.

#### Aggiornamento dei valori statici:

Trova il campo **Static\_Values** e aggiungi quanto segue:

```
,EDI_FILE_PREFIX,XML_FILE_PREFIX,PDF_FILE_PREFIX,PDF_FILE_EXTENSION,EDI_FILE_EXTENSION,XML_FILE_EXTENSION
```

Poi, aggiungi le seguenti voci sotto **SV\_ACLString**:

```
SV_EDI_FILE_PREFIX=EDI_810_
SV_XML_FILE_PREFIX=XML_810_
SV_PDF_FILE_PREFIX=INV_EDI_
SV_PDF_FILE_EXTENSION=.pdf
SV_EDI_FILE_EXTENSION=.xml
SV_XML_FILE_EXTENSION=.xml
```

Dopo di che, aggiungi il mapping effettivo, assicurandoti che il tipo di documento di esportazione corrisponda al tipo di fornitore IDM.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F6k18wa4zSaSZkvfEKMwW%252Fimage.png%3Falt%3Dmedia%26token%3De6c49d36-44b9-4d18-9d22-63d30205dbd5\&width=768\&dpr=4\&quality=100\&sign=3ac8bc32\&sv=2)

#### Mapping XML

Aggiungi il seguente mapping in fondo al file:

```
EMBEDDED_FILES_EXPORT = TRANSFORMED, XML
EFE_TRANSFORMED_SOURCE_NAME = Transformed.xml
EFE_TRANSFORMED_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_TRANSFORMED_EXPORT_FILENAME = SV_XML_FILE_PREFIX+IF_INVOICE_ID+SV_XML_FILE_EXTENSION

EFE_XML_SOURCE_NAME = XML_DOCUMENT.xml
EFE_XML_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_XML_EXPORT_FILENAME = SV_XML_FILE_PREFIX+IF_INVOICE_ID+SV_XML_FILE_EXTENSION
```

Nota: Assicurati che **export\_doc\_type** sia impostato sul tipo di fattura IDM. In questo esempio, è impostato per **M3**.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FlXToG368VI7Fc7HDguCn%252Fimage.png%3Falt%3Dmedia%26token%3Dcb153977-34e1-4f5f-a416-60e3141b4aca\&width=768\&dpr=4\&quality=100\&sign=b7d9585c\&sv=2)

#### Mapping EDI

Aggiungi il seguente mapping in fondo al file:

```
EMBEDDED_FILES_EXPORT = TRANSFORMED, EDI
EFE_TRANSFORMED_SOURCE_NAME = Transformed.xml
EFE_TRANSFORMED_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_TRANSFORMED_EXPORT_FILENAME = SV_XML_FILE_PREFIX+IF_INVOICE_NUMBER+SV_XML_FILE_EXTENSION

EFE_EDI_SOURCE_NAME = EDI.edi
EFE_EDI_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_EDI_EXPORT_FILENAME = SV_EDI_FILE_PREFIX+IF_INVOICE_NUMBER+SV_EDI_FILE_EXTENSION
```

Nota: Assicurati che **export\_doc\_type** sia impostato sul tipo di fattura IDM. In questo esempio, è impostato per **M3**.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FSrF54zkGq6aYYuJq1KAI%252Fimage.png%3Falt%3Dmedia%26token%3D403c9bfa-7e97-4d3c-a4b0-1bb82b98fe50\&width=768\&dpr=4\&quality=100\&sign=a768865f\&sv=2)

#### Document Manager in Infor

Vai a Document Manager e seleziona il nome del tipo di documento corrente che stai cercando di esportare, ad esempio, Fattura Fornitore.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FEV3uw3R1L6_RRANB7FRLwtUFMbv_KGtL4x6kAk6lEYhwI90UeG2uWqFD2Azpxv-SRFl9zfvdratOZbXxp2D1-SryLo3Boj2x9Xc4PQXJ6vUhX5c9pvhv4XHuCk-qMK51DZ885vRUJ5dwES7k84uhoyk\&width=768\&dpr=4\&quality=100\&sign=a2f25ec9\&sv=2)

Clicca sull'icona sopra e poi clicca su Amministrazione → Tipo di documento e poi trova il tipo di documento di cui hai bisogno nell'elenco

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FldsuINS9SCUQm3E57s8j_95gzBGwHQFavcf6d3myg6tuVxRoQHtq8R-6we5OEJ63swDxwPc9w7hbySWqWdfaMsGdQpn99m6EchPY5f5DzXEj-8mjocwPNtdJVNP34CuPvw0JIImDgFX1Q05M8-ogZo8\&width=768\&dpr=4\&quality=100\&sign=a1149783\&sv=2)

Come mostrato di seguito, vedrai quindi il nome del tipo di documento così come appare in INFOR

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FKSreWGS7TqdMP64BqtufM24xk0RDnNDHUZapnPsSuRj_umPJ3icll89KI2RYpbtet2F6ccL8QfYbl27-2j1nQPwQ0z-Nq873c4Tv72ee9AJhKMxynIUxmJKKsQQCupW_dpRfw_5BXm0WvAnw4HOALmw\&width=768\&dpr=4\&quality=100\&sign=62bfe0a6\&sv=2)

Assicurati che questo sia il modo in cui il nome è mostrato nel file di mapping IDM

### Carica il file in DocBits

Una volta che il file è pronto, caricalo nella tua configurazione di esportazione in DocBits. Questo è disponibile in Impostazioni → Esporta.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FrUHhvImiWamK6JxnWSPL4JEioAJq3AmvdsubJDo-DoDV9F_i5mZ42YDnjqZUYKYSJu1Cetc_4fLwlvvmoZXYIzmBf3hoyW6RjfP9HQ8FkNDhW1IbLHvNTCHWFRaeCECdZ97u79-Eu37TvzqnqGPEayM\&width=768\&dpr=4\&quality=100\&sign=a13b8c88\&sv=2)
