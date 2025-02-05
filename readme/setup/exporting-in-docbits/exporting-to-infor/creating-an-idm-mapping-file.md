# Criando um Arquivo de Mapeamento IDM

Uma vez obtido, abra o arquivo no editor de arquivos de sua escolha. Para este guia, o VSCode será utilizado.

### Editar Arquivo de Mapeamento

Verifique se o código do tipo de documento está como está no DocBits (como no Arquivo de Mapeamento BOD, deve corresponder ao nome do tipo de documento na URL das configurações de campo) e também verifique o nome do tipo de documento como deve estar no Gerenciador de Documentos (IDM) no Infor.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FWHO0vg2W36yVFBq0ay0wBMFVzMfT6pNvHklt0o8N4tqUpM03jXJm2fykuYjyZh0z4wFTO4Eaeh39-D03re3a9utegrdVdsjHBfucmALA3B7YBWd92-9bcYr543G4MWftv0RosvTgFP3J6NNmLZAz5Dc\&width=768\&dpr=4\&quality=100\&sign=5bb93fe7\&sv=2)

**FYI**: Afirma que o nome do tipo de documento no IDM é M3\_SupplierInvoice, isso se deve ao fato de ser um exemplo de uma instância M3. Isso pode mudar dependendo se você usa LN ou M3, bem como sua configuração específica do IDM.

Verifique o ID da empresa e verifique o ID da Entidade (SF\_MDS\_EntityType), esse valor deve ser o mesmo que estava no Arquivo de Mapeamento BOD.

Certifique-se de que o IndexFieldFromDocBits=IDMAttributeID (verifique se o DocBits à esquerda nas configurações de campo corresponde ao IDM à direita em Tipo de Documento → Atributos).

### Exportação de arquivo XML e EDI

Para exportar o arquivo XML/EDI original juntamente com o PDF gerado, você precisa modificar o arquivo de Mapeamento IDM, na configuração de exportação. Primeiro, atualize a seção **Static\_Values** adicionando o prefixo e a extensão do arquivo. Depois disso, defina o mapeamento real para garantir a configuração de exportação correta.

Se uma exportação para faturas para IDM já estiver configurada, o PDF gerado já deve estar incluído na exportação. Se você não precisar do arquivo XML, pode pular a próxima parte. No entanto, se você precisar do arquivo XML, siga os passos abaixo.

#### Atualizando os Valores Estáticos:

Encontre o campo **Static\_Values** e adicione o seguinte:

```
,EDI_FILE_PREFIX,XML_FILE_PREFIX,PDF_FILE_PREFIX,PDF_FILE_EXTENSION,EDI_FILE_EXTENSION,XML_FILE_EXTENSION
```

Em seguida, adicione as seguintes entradas abaixo de **SV\_ACLString**:

```
SV_EDI_FILE_PREFIX=EDI_810_
SV_XML_FILE_PREFIX=XML_810_
SV_PDF_FILE_PREFIX=INV_EDI_
SV_PDF_FILE_EXTENSION=.pdf
SV_EDI_FILE_EXTENSION=.xml
SV_XML_FILE_EXTENSION=.xml
```

Depois disso, adicione o mapeamento real, certificando-se de que o tipo de documento de exportação corresponda ao tipo de fornecedor IDM.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F6k18wa4zSaSZkvfEKMwW%252Fimage.png%3Falt%3Dmedia%26token%3De6c49d36-44b9-4d18-9d22-63d30205dbd5\&width=768\&dpr=4\&quality=100\&sign=3ac8bc32\&sv=2)

#### Mapeamento XML

Adicione o seguinte mapeamento na parte inferior do arquivo:

```
EMBEDDED_FILES_EXPORT = TRANSFORMED, XML
EFE_TRANSFORMED_SOURCE_NAME = Transformed.xml
EFE_TRANSFORMED_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_TRANSFORMED_EXPORT_FILENAME = SV_XML_FILE_PREFIX+IF_INVOICE_ID+SV_XML_FILE_EXTENSION

EFE_XML_SOURCE_NAME = XML_DOCUMENT.xml
EFE_XML_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_XML_EXPORT_FILENAME = SV_XML_FILE_PREFIX+IF_INVOICE_ID+SV_XML_FILE_EXTENSION
```

Nota: Certifique-se de que **export\_doc\_type** esteja definido como o tipo de fatura IDM. Neste exemplo, está definido para **M3**.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FlXToG368VI7Fc7HDguCn%252Fimage.png%3Falt%3Dmedia%26token%3Dcb153977-34e1-4f5f-a416-60e3141b4aca\&width=768\&dpr=4\&quality=100\&sign=b7d9585c\&sv=2)

#### Mapeamento EDI

Adicione o seguinte mapeamento na parte inferior do arquivo:

```
EMBEDDED_FILES_EXPORT = TRANSFORMED, EDI
EFE_TRANSFORMED_SOURCE_NAME = Transformed.xml
EFE_TRANSFORMED_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_TRANSFORMED_EXPORT_FILENAME = SV_XML_FILE_PREFIX+IF_INVOICE_NUMBER+SV_EDI_FILE_EXTENSION

EFE_EDI_SOURCE_NAME = EDI.edi
EFE_EDI_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_EDI_EXPORT_FILENAME = SV_EDI_FILE_PREFIX+IF_INVOICE_NUMBER+SV_EDI_FILE_EXTENSION
```

Nota: Certifique-se de que **export\_doc\_type** esteja definido como o tipo de fatura IDM. Neste exemplo, está definido para **M3**.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FSrF54zkGq6aYYuJq1KAI%252Fimage.png%3Falt%3Dmedia%26token%3D403c9bfa-7e97-4d3c-a4b0-1bb82b98fe50\&width=768\&dpr=4\&quality=100\&sign=a768865f\&sv=2)

#### Gerenciador de Documentos no Infor

Vá para o Gerenciador de Documentos e selecione o nome do tipo de documento atual que você está tentando exportar, por exemplo, Fatura do Fornecedor.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FEV3uw3R1L6_RRANB7FRLwtUFMbv_KGtL4x6kAk6lEYhwI90UeG2uWqFD2Azpxv-SRFl9zfvdratOZbXxp2D1-SryLo3Boj2x9Xc4PQXJ6vUhX5c9pvhv4XHuCk-qMK51DZ885vRUJ5dwES7k84uhoyk\&width=768\&dpr=4\&quality=100\&sign=a2f25ec9\&sv=2)

Clique no ícone acima e depois clique em Administração → Tipo de Documento e, em seguida, encontre o tipo de documento que você precisa na lista.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FldsuINS9SCUQm3E57s8j_95gzBGwHQFavcf6d3myg6tuVxRoQHtq8R-6we5OEJ63swDxwPc9w7hbySWqWdfaMsGdQpn99m6EchPY5f5DzXEj-8mjocwPNtdJVNP34CuPvw0JIImDgFX1Q05M8-ogZo8\&width=768\&dpr=4\&quality=100\&sign=a1149783\&sv=2)

Como mostrado abaixo, você verá o nome do tipo de documento como está no INFOR.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FKSreWGS7TqdMP64BqtufM24xk0RDnNDHUZapnPsSuRj_umPJ3icll89KI2RYpbtet2F6ccL8QfYbl27-2j1nQPwQ0z-Nq873c4Tv72ee9AJhKMxynIUxmJKKsQQCupW_dpRfw_5BXm0WvAnw4HOALmw\&width=768\&dpr=4\&quality=100\&sign=62bfe0a6\&sv=2)

Certifique-se de que é assim que o nome é mostrado no Arquivo de Mapeamento IDM.

### Carregar Arquivo para DocBits

Uma vez que o arquivo esteja preparado, faça o upload para sua configuração de exportação no DocBits. Isso está disponível em Configurações → Exportar.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FrUHhvImiWamK6JxnWSPL4JEioAJq3AmvdsubJDo-DoDV9F_i5mZ42YDnjqZUYKYSJu1Cetc_4fLwlvvmoZXYIzmBf3hoyW6RjfP9HQ8FkNDhW1IbLHvNTCHWFRaeCECdZ97u79-Eu37TvzqnqGPEayM\&width=768\&dpr=4\&quality=100\&sign=a13b8c88\&sv=2)
