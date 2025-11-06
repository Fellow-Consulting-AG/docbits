# Importação do Infor M3 para o DocBits via API

## Passo 1: Criar uma API

1. Abra o **Infor OS** e navegue até **API Gateway** > **Available APIs**.
2. Clique em **Add** e selecione **Create New**.
3. Preencha os detalhes da API:
   * **Application Name**: `DocBits-Stage`, `DocBits-Sandbox`, `DocBits-Prod` ou `DocBits-Demo` (dependendo do seu ambiente).
   * **Description**: `DocBits Demo`, `DocBits Prod`, `DocBits Sandbox` ou `DocBits Stage` (dependendo do seu ambiente).
   * **API Specification Type**: `OAGIS`.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_1.png)

4. Clique em **Add** e **Save and Deploy** para finalizar.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_2.png)

## Passo 2: Criar um Ponto de Conexão da API

### Sync.SupplierPartyMaster

1. Navegue até **API Gateway** > **Connection Points**.
2. Clique em **Add**, depois em **Create New**.
3. Preencha os detalhes conforme mostrado abaixo:
   * **Name**: `Sync.SupplierPartyMaster`
   * **Source Application Name**: `DocBits-Demo`, `DocBits-Prod`, `DocBits-Sandbox` ou `DocBits-Stage` (dependendo do seu ambiente).
   * **Noun**: `SupplierPartyMaster`
   * **Verb**: `Sync`
   * **Is enabled**: Marque a caixa.
   * **Cloud Suite Version**: Escolha a versão do Cloud Suite.
   * **Program**: `MMS024MI`
   * **Transaction**: `Get`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_3.png)

4. Vá para a seção **Mappings** e cole o XML:

```xml
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
  <SOAP-ENV:Header/>
  <SOAP-ENV:Body>
    <oa:Sync xmlns:oa="http://www.openapplications.org/oagis/10" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.openapplications.org/oagis/10 BODs/Sync_SupplierPartyMaster.xsd">
      <oa:ApplicationArea>
        <oa:Sender>
          <oa:LogicalID></oa:LogicalID>
        </oa:Sender>
        <oa:CreationDateTime></oa:CreationDateTime>
      </oa:ApplicationArea>
      <oa:DataArea>
        <oa:Sync>
          <oa:TenantID></oa:TenantID>
          <oa:AccountingEntityID></oa:AccountingEntityID>
        </oa:Sync>
        <oa:SupplierPartyMaster>
          <oa:SupplierHeader>
            <oa:PartyIDs>
              <oa:ID>
                <xsl:value-of select="/API_CONNECTION_POINT_OUTPUT/API_OUTPUT/TRANSACTION_RESULT/ELEMENT[TYPE='Output']/DATA_SEGMENT[NAME='MMS024MI_Get_Output']/ELEMENT[TYPE='Element']/ELEMENT_VALUE[FIELD='IDSUNO']"/>
              </oa:ID>
            </oa:PartyIDs>
            <oa:Name>
              <xsl:value-of select="/API_CONNECTION_POINT_OUTPUT/API_OUTPUT/TRANSACTION_RESULT/ELEMENT[TYPE='Output']/DATA_SEGMENT[NAME='MMS024MI_Get_Output']/ELEMENT[TYPE='Element']/ELEMENT_VALUE[FIELD='SUNM']"/>
            </oa:Name>
            <oa:TaxInformation>
              <oa:TaxID>
                <oa:ID>
                  <xsl:value-of select="/API_CONNECTION_POINT_OUTPUT/API_OUTPUT/TRANSACTION_RESULT/ELEMENT[TYPE='Output']/DATA_SEGMENT[NAME='MMS024MI_Get_Output']/ELEMENT[TYPE='Element']/ELEMENT_VALUE[FIELD='VRNO']"/>
                </oa:ID>
              </oa:TaxID>
            </oa:TaxInformation>
            <oa:Location>
              <oa:Address>
                <oa:LineOne>
                  <xsl:value-of select="/API_CONNECTION_POINT_OUTPUT/API_OUTPUT/TRANSACTION_RESULT/ELEMENT[TYPE='Output']/DATA_SEGMENT[NAME='MMS024MI_Get_Output']/ELEMENT[TYPE='Element']/ELEMENT_VALUE[FIELD='SDA1']"/>
                </oa:LineOne>
                <oa:LineTwo>
                  <xsl:value-of select="/API_CONNECTION_POINT_OUTPUT/API_OUTPUT/TRANSACTION_RESULT/ELEMENT[TYPE='Output']/DATA_SEGMENT[NAME='MMS024MI_Get_Output']/ELEMENT[TYPE='Element']/ELEMENT_VALUE[FIELD='SDA2']"/>
                </oa:LineTwo>
                <oa:LineThree>
                  <xsl:value-of select="/API_CONNECTION_POINT_OUTPUT/API_OUTPUT/TRANSACTION_RESULT/ELEMENT[TYPE='Output']/DATA_SEGMENT[NAME='MMS024MI_Get_Output']/ELEMENT[TYPE='Element']/ELEMENT_VALUE[FIELD='SDA3']"/>
                </oa:LineThree>
                <oa:LineFour>
                  <xsl:value-of select="/API_CONNECTION_POINT_OUTPUT/API_OUTPUT/TRANSACTION_RESULT/ELEMENT[TYPE='Output']/DATA_SEGMENT[NAME='MMS024MI_Get_Output']/ELEMENT[TYPE='Element']/ELEMENT_VALUE[FIELD='SDA4']"/>
                </oa:LineFour>
                <oa:CityName>
                  <xsl:value-of select="/API_CONNECTION_POINT_OUTPUT/API_OUTPUT/TRANSACTION_RESULT/ELEMENT[TYPE='Output']/DATA_SEGMENT[NAME='MMS024MI_Get_Output']/ELEMENT[TYPE='Element']/ELEMENT_VALUE[FIELD='TOWN']"/>
                </oa:CityName>
                <oa:CountryCode>
                  <xsl:value-of select="/API_CONNECTION_POINT_OUTPUT/API_OUTPUT/TRANSACTION_RESULT/ELEMENT[TYPE='Output']/DATA_SEGMENT[NAME='MMS024MI_Get_Output']/ELEMENT[TYPE='Element']/ELEMENT_VALUE[FIELD='CSCD']"/>
                </oa:CountryCode>
                <oa:StateOrProvince>
                  <xsl:value-of select="/API_CONNECTION_POINT_OUTPUT/API_OUTPUT/TRANSACTION_RESULT/ELEMENT[TYPE='Output']/DATA_SEGMENT[NAME='MMS024MI_Get_Output']/ELEMENT[TYPE='Element']/ELEMENT_VALUE[FIELD='ECAR']"/>
                </oa:StateOrProvince>
                <oa:PostalCode>
                  <xsl:value-of select="/API_CONNECTION_POINT_OUTPUT/API_OUTPUT/TRANSACTION_RESULT/ELEMENT[TYPE='Output']/DATA_SEGMENT[NAME='MMS024MI_Get_Output']/ELEMENT[TYPE='Element']/ELEMENT_VALUE[FIELD='PONO']"/>
                </oa:PostalCode>
              </oa:Address>
            </oa:Location>
          </oa:SupplierHeader>
        </oa:SupplierPartyMaster>
      </oa:DataArea>
    </oa:Sync>
  </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
```

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_4.png)

5. Copie o **URL** do **Endpoint** e salve-o. Você precisará dele mais tarde ao criar o **Document Flow**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_5.png)

6. Clique em **Save and Deploy**.

***

### Sync.RemitToPartyMaster

1. Navegue até **API Gateway** > **Connection Points**.
2. Clique em **Add** e selecione **Create New**.
3. Preencha os detalhes conforme mostrado abaixo:
   * **Name**: `Sync.RemitToPartyMaster`
   * **Source Application Name**: `DocBits-Demo`, `DocBits-Prod`, `DocBits-Sandbox` ou `DocBits-Stage` (dependendo do seu ambiente).
   * **Noun**: `RemitToPartyMaster`
   * **Verb**: `Sync`
   * **Is enabled**: Marque a caixa.
   * **Cloud Suite Version**: Escolha a versão do Cloud Suite.
   * **Program**: `CRS610MI`
   * **Transaction**: `GetAddress`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_6.png)

4. Vá para a seção **Mappings** e cole o XML:

```xml
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
  <SOAP-ENV:Header/>
  <SOAP-ENV:Body>
    <oa:Sync xmlns:oa="http://www.openapplications.org/oagis/10" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.openapplications.org/oagis/10 BODs/Sync_RemitToPartyMaster.xsd">
      <oa:ApplicationArea>
        <oa:Sender>
          <oa:LogicalID></oa:LogicalID>
        </oa:Sender>
        <oa:CreationDateTime></oa:CreationDateTime>
      </oa:ApplicationArea>
      <oa:DataArea>
        <oa:Sync>
          <oa:TenantID></oa:TenantID>
          <oa:AccountingEntityID></oa:AccountingEntityID>
        </oa:Sync>
        <oa:RemitToPartyMaster>
          <oa:RemitToHeader>
            <oa:PartyIDs>
              <oa:ID>
                <xsl:value-of select="/API_CONNECTION_POINT_OUTPUT/API_OUTPUT/TRANSACTION_RESULT/ELEMENT[TYPE='Output']/DATA_SEGMENT[NAME='CRS610MI_GetAddress_Output']/ELEMENT[TYPE='Element']/ELEMENT_VALUE[FIELD='PYNO']"/>
              </oa:ID>
            </oa:PartyIDs>
            <oa:Name>
              <xsl:value-of select="/API_CONNECTION_POINT_OUTPUT/API_OUTPUT/TRANSACTION_RESULT/ELEMENT[TYPE='Output']/DATA_SEGMENT[NAME='CRS610MI_GetAddress_Output']/ELEMENT[TYPE='Element']/ELEMENT_VALUE[FIELD='CUNM']"/>
            </oa:Name>
            <oa:TaxInformation>
              <oa:TaxID>
                <oa:ID></oa:ID>
              </oa:TaxID>
            </oa:TaxInformation>
            <oa:Location>
              <oa:Address>
                <oa:LineOne>
                  <xsl:value-of select="/API_CONNECTION_POINT_OUTPUT/API_OUTPUT/TRANSACTION_RESULT/ELEMENT[TYPE='Output']/DATA_SEGMENT[NAME='CRS610MI_GetAddress_Output']/ELEMENT[TYPE='Element']/ELEMENT_VALUE[FIELD='CUA1']"/>
                </oa:LineOne>
                <oa:LineTwo>
                  <xsl:value-of select="/API_CONNECTION_POINT_OUTPUT/API_OUTPUT/TRANSACTION_RESULT/ELEMENT[TYPE='Output']/DATA_SEGMENT[NAME='CRS610MI_GetAddress_Output']/ELEMENT[TYPE='Element']/ELEMENT_VALUE[FIELD='CUA2']"/>
                </oa:LineTwo>
                <oa:LineThree>
                  <xsl:value-of select="/API_CONNECTION_POINT_OUTPUT/API_OUTPUT/TRANSACTION_RESULT/ELEMENT[TYPE='Output']/DATA_SEGMENT[NAME='CRS610MI_GetAddress_Output']/ELEMENT[TYPE='Element']/ELEMENT_VALUE[FIELD='CUA3']"/>
                </oa:LineThree>
                <oa:LineFour>
                  <xsl:value-of select="/API_CONNECTION_POINT_OUTPUT/API_OUTPUT/TRANSACTION_RESULT/ELEMENT[TYPE='Output']/DATA_SEGMENT[NAME='CRS610MI_GetAddress_Output']/ELEMENT[TYPE='Element']/ELEMENT_VALUE[FIELD='CUA4']"/>
                </oa:LineFour>
                <oa:CityName>
                  <xsl:value-of select="/API_CONNECTION_POINT_OUTPUT/API_OUTPUT/TRANSACTION_RESULT/ELEMENT[TYPE='Output']/DATA_SEGMENT[NAME='CRS610MI_GetAddress_Output']/ELEMENT[TYPE='Element']/ELEMENT_VALUE[FIELD='TOWN']"/>
                </oa:CityName>
                <oa:CountryCode>
                  <xsl:value-of select="/API_CONNECTION_POINT_OUTPUT/API_OUTPUT/TRANSACTION_RESULT/ELEMENT[TYPE='Output']/DATA_SEGMENT[NAME='CRS610MI_GetAddress_Output']/ELEMENT[TYPE='Element']/ELEMENT_VALUE[FIELD='CSCD']"/>
                </oa:CountryCode>
                <oa:StateOrProvince>
                  <xsl:value-of select="/API_CONNECTION_POINT_OUTPUT/API_OUTPUT/TRANSACTION_RESULT/ELEMENT[TYPE='Output']/DATA_SEGMENT[NAME='CRS610MI_GetAddress_Output']/ELEMENT[TYPE='Element']/ELEMENT_VALUE[FIELD='ECAR']"/>
                </oa:StateOrProvince>
                <oa:PostalCode>
                  <xsl:value-of select="/API_CONNECTION_POINT_OUTPUT/API_OUTPUT/TRANSACTION_RESULT/ELEMENT[TYPE='Output']/DATA_SEGMENT[NAME='CRS610MI_GetAddress_Output']/ELEMENT[TYPE='Element']/ELEMENT_VALUE[FIELD='PONO']"/>
                </oa:PostalCode>
              </oa:Address>
            </oa:Location>
          </oa:RemitToHeader>
        </oa:RemitToPartyMaster>
      </oa:DataArea>
    </oa:Sync>
  </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
```

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_7.png)

5. Copie o **URL** do **Endpoint** e salve-o. Você precisará dele mais tarde ao criar o **Document Flow**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_5.png)

6. Clique em **Save and Deploy**.

***

### Acknowledge.SupplierInvoice

1. Navegue até **API Gateway** > **Connection Points**.
2. Clique em **Add** e selecione **Create New**.
3. Preencha os detalhes conforme mostrado abaixo:
   * **Name**: `Acknowledge.SupplierInvoice`
   * **Source Application Name**: `DocBits-Demo`, `DocBits-Prod`, `DocBits-Sandbox` ou `DocBits-Stage` (dependendo do seu ambiente).
   * **Noun**: `SupplierInvoice`
   * **Verb**: `Acknowledge`
   * **Is enabled**: Marque a caixa.
   * **Cloud Suite Version**: Escolha a versão do Cloud Suite.
   * **Program**: `APS450MI`
   * **Transaction**: `AddInvoiceLin`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_8.png)

4. Vá para a seção **Mappings** e cole o XML:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<IONRequest xmlns="http://schema.infor.com/InforOAGIS/2">
  <APIInvoke xmlns="http://schema.infor.com/InforOAGIS/2">
    <Credentials/>
    <m3api:M3APIRequest xmlns:m3api="http://schema.infor.com/m3api">
      <m3api:Program>APS450MI</m3api:Program>
      <m3api:Transaction>AddInvoiceLin</m3api:Transaction>
      <m3api:Record>
        <m3api:NameValue name="DIVI">
          <m3api:Value>
            <xsl:value-of select="/API_CONNECTION_POINT_INPUT/BODY/Acknowledge/DataArea/SupplierInvoice[1]/Header/Party[PartyID/ID[@accountingEntity='Division']]/PartyID/ID[@accountingEntity='Division']"/>
          </m3api:Value>
        </m3api:NameValue>
        <m3api:NameValue name="INBN">
          <m3api:Value>
            <xsl:value-of select="/API_CONNECTION_POINT_INPUT/BODY/Acknowledge/DataArea/SupplierInvoice[1]/Header/DocumentReference/DocumentIDs/DocumentID[ID[@accountingEntity='InvoiceBatchNumber']]/ID[@accountingEntity='InvoiceBatchNumber']"/>
          </m3api:Value>
        </m3api:NameValue>
        <m3api:NameValue name="TRNO">
          <m3api:Value>
            <xsl:value-of select="/API_CONNECTION_POINT_INPUT/BODY/Acknowledge/DataArea/SupplierInvoice[1]/Line[1]/LineNumber[@sequence]"/>
          </m3api:Value>
        </m3api:NameValue>
        <m3api:NameValue name="SUNO">
          <m3api:Value>
            <xsl:value-of select="/API_CONNECTION_POINT_INPUT/BODY/Acknowledge/DataArea/SupplierInvoice[1]/Header/SupplierParty/PartyID/ID[@accountingEntity='SupplierID']"/>
          </m3api:Value>
        </m3api:NameValue>
        <m3api:NameValue name="SINO">
          <m3api:Value>
            <xsl:value-of select="/API_CONNECTION_POINT_INPUT/BODY/Acknowledge/DataArea/SupplierInvoice[1]/Header/DocumentReference/DocumentIDs/DocumentID[ID[@accountingEntity='SupplierInvoiceNumber']]/ID[@accountingEntity='SupplierInvoiceNumber']"/>
          </m3api:Value>
        </m3api:NameValue>
        <m3api:NameValue name="IVDT">
          <m3api:Value>
            <xsl:value-of select="/API_CONNECTION_POINT_INPUT/BODY/Acknowledge/DataArea/SupplierInvoice[1]/Header/DocumentDateTime[@qualifier='Actual']"/>
          </m3api:Value>
        </m3api:NameValue>
        <m3api:NameValue name="BSCD">
          <m3api:Value>
            <xsl:value-of select="/API_CONNECTION_POINT_INPUT/BODY/Acknowledge/DataArea/SupplierInvoice[1]/Header/Status/Code"/>
          </m3api:Value>
        </m3api:NameValue>
        <m3api:NameValue name="CUCD">
          <m3api:Value>
            <xsl:value-of select="/API_CONNECTION_POINT_INPUT/BODY/Acknowledge/DataArea/SupplierInvoice[1]/Header/TotalAmount/@currencyID"/>
          </m3api:Value>
        </m3api:NameValue>
        <m3api:NameValue name="VTCD">
          <m3api:Value>
            <xsl:value-of select="/API_CONNECTION_POINT_INPUT/BODY/Acknowledge/DataArea/SupplierInvoice[1]/Line[1]/LineType/Code"/>
          </m3api:Value>
        </m3api:NameValue>
        <m3api:NameValue name="PUUN">
          <m3api:Value>
            <xsl:value-of select="/API_CONNECTION_POINT_INPUT/BODY/Acknowledge/DataArea/SupplierInvoice[1]/Line[1]/OrderQuantity[@unitOfMeasure]/@unitOfMeasure"/>
          </m3api:Value>
        </m3api:NameValue>
        <m3api:NameValue name="IVQA">
          <m3api:Value>
            <xsl:value-of select="/API_CONNECTION_POINT_INPUT/BODY/Acknowledge/DataArea/SupplierInvoice[1]/Line[1]/OrderQuantity[@unitOfMeasure]"/>
          </m3api:Value>
        </m3api:NameValue>
        <m3api:NameValue name="GRPI">
          <m3api:Value>
            <xsl:value-of select="/API_CONNECTION_POINT_INPUT/BODY/Acknowledge/DataArea/SupplierInvoice[1]/Line[1]/ReceiptLineReference/DocumentReference/DocumentIDs/DocumentID[ID[@accountingEntity='GoodsReceiptNumber']]/ID[@accountingEntity='GoodsReceiptNumber']"/>
          </m3api:Value>
        </m3api:NameValue>
        <m3api:NameValue name="PUNO">
          <m3api:Value>
            <xsl:value-of select="/API_CONNECTION_POINT_INPUT/BODY/Acknowledge/DataArea/SupplierInvoice[1]/Line[1]/PurchaseOrderLineReference/DocumentReference/DocumentIDs/DocumentID[ID[@accountingEntity='PurchaseOrderNumber']]/ID[@accountingEntity='PurchaseOrderNumber']"/>
          </m3api:Value>
        </m3api:NameValue>
        <m3api:NameValue name="PNLI">
          <m3api:Value>
            <xsl:value-of select="/API_CONNECTION_POINT_INPUT/BODY/Acknowledge/DataArea/SupplierInvoice[1]/Line[1]/PurchaseOrderLineReference/LineNumber[@sequence]"/>
          </m3api:Value>
        </m3api:NameValue>
        <m3api:NameValue name="PNLS">
          <m3api:Value>
            <xsl:value-of select="/API_CONNECTION_POINT_INPUT/BODY/Acknowledge/DataArea/SupplierInvoice[1]/Line[1]/PurchaseOrderLineReference/SubLineNumber"/>
          </m3api:Value>
        </m3api:NameValue>
        <m3api:NameValue name="NLAM">
          <m3api:Value>
            <xsl:value-of select="/API_CONNECTION_POINT_INPUT/BODY/Acknowledge/DataArea/SupplierInvoice[1]/Line[1]/TotalAmount"/>
          </m3api:Value>
        </m3api:NameValue>
        <m3api:NameValue name="IVAM">
          <m3api:Value>
            <xsl:value-of select="/API_CONNECTION_POINT_INPUT/BODY/Acknowledge/DataArea/SupplierInvoice[1]/Header/TotalAmount"/>
          </m3api:Value>
        </m3api:NameValue>
        <m3api:NameValue name="VTAM">
          <m3api:Value>
            <xsl:value-of select="/API_CONNECTION_POINT_INPUT/BODY/Acknowledge/DataArea/SupplierInvoice[1]/Header/Tax/TaxableAmount"/>
          </m3api:Value>
        </m3api:NameValue>
        <m3api:NameValue name="AIT1">
          <m3api:Value>
            <xsl:value-of select="/API_CONNECTION_POINT_INPUT/BODY/Acknowledge/DataArea/SupplierInvoice[1]/Line[1]/Dimension[1]/DimensionCode"/>
          </m3api:Value>
        </m3api:NameValue>
        <m3api:NameValue name="AIT2">
          <m3api:Value>
            <xsl:value-of select="/API_CONNECTION_POINT_INPUT/BODY/Acknowledge/DataArea/SupplierInvoice[1]/Line[1]/Dimension[2]/DimensionCode"/>
          </m3api:Value>
        </m3api:NameValue>
        <m3api:NameValue name="AIT3">
          <m3api:Value>
            <xsl:value-of select="/API_CONNECTION_POINT_INPUT/BODY/Acknowledge/DataArea/SupplierInvoice[1]/Line[1]/Dimension[3]/DimensionCode"/>
          </m3api:Value>
        </m3api:NameValue>
        <m3api:NameValue name="AIT4">
          <m3api:Value>
            <xsl:value-of select="/API_CONNECTION_POINT_INPUT/BODY/Acknowledge/DataArea/SupplierInvoice[1]/Line[1]/Dimension[4]/DimensionCode"/>
          </m3api:Value>
        </m3api:NameValue>
        <m3api:NameValue name="AIT5">
          <m3api:Value>
            <xsl:value-of select="/API_CONNECTION_POINT_INPUT/BODY/Acknowledge/DataArea/SupplierInvoice[1]/Line[1]/Dimension[5]/DimensionCode"/>
          </m3api:Value>
        </m3api:NameValue>
        <m3api:NameValue name="AIT6">
          <m3api:Value>
            <xsl:value-of select="/API_CONNECTION_POINT_INPUT/BODY/Acknowledge/DataArea/SupplierInvoice[1]/Line[1]/Dimension[6]/DimensionCode"/>
          </m3api:Value>
        </m3api:NameValue>
        <m3api:NameValue name="AIT7">
          <m3api:Value>
            <xsl:value-of select="/API_CONNECTION_POINT_INPUT/BODY/Acknowledge/DataArea/SupplierInvoice[1]/Line[1]/Dimension[7]/DimensionCode"/>
          </m3api:Value>
        </m3api:NameValue>
      </m3api:Record>
    </m3api:M3APIRequest>
  </APIInvoke>
</IONRequest>
```

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_9.png)

5. Copie o **URL** do **Endpoint** e salve-o. Você precisará dele mais tarde ao criar o **Document Flow**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_5.png)

6. Clique em **Save and Deploy**.

***

### Sync.PurchaseOrder

1. Navegue até **API Gateway** > **Connection Points**.
2. Clique em **Add** e selecione **Create New**.
3. Preencha os detalhes conforme mostrado abaixo:
   * **Name**: `Sync.PurchaseOrder`
   * **Source Application Name**: `DocBits-Demo`, `DocBits-Prod`, `DocBits-Sandbox` ou `DocBits-Stage` (dependendo do seu ambiente).
   * **Noun**: `PurchaseOrder`
   * **Verb**: `Sync`
   * **Is enabled**: Marque a caixa.
   * **Cloud Suite Version**: Escolha a versão do Cloud Suite.
   * **Program**: `PPS200MI`
   * **Transaction**: `GetLine`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_10.png)

4. Vá para a seção **Mappings** e cole o XML:

```xml
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
  <SOAP-ENV:Header/>
  <SOAP-ENV:Body>
    <oa:Sync xmlns:oa="http://www.openapplications.org/oagis/10" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xsi:schemaLocation="http://www.openapplications.org/oagis/10 BODs/Sync_PurchaseOrder.xsd">
      <oa:ApplicationArea>
        <oa:Sender>
          <oa:LogicalID></oa:LogicalID>
        </oa:Sender>
        <oa:CreationDateTime></oa:CreationDateTime>
      </oa:ApplicationArea>
      <oa:DataArea>
        <oa:Sync>
          <oa:TenantID></oa:TenantID>
          <oa:AccountingEntityID></oa:AccountingEntityID>
        </oa:Sync>
        <oa:PurchaseOrder>
          <oa:PurchaseOrderHeader>
            <oa:DocumentID>
              <oa:ID accountingEntity="PurchaseOrderNumber">
                <xsl:value-of select="/API_CONNECTION_POINT_OUTPUT/API_OUTPUT/TRANSACTION_RESULT/ELEMENT[TYPE='Output']/DATA_SEGMENT[NAME='PPS200MI_GetLine_Output']/ELEMENT[TYPE='Element']/ELEMENT_VALUE[FIELD='PUNO']"/>
              </oa:ID>
            </oa:DocumentID>
          </oa:PurchaseOrderHeader>
          <oa:Line>
            <oa:LineNumber sequence="">
              <xsl:value-of select="/API_CONNECTION_POINT_OUTPUT/API_OUTPUT/TRANSACTION_RESULT/ELEMENT[TYPE='Output']/DATA_SEGMENT[NAME='PPS200MI_GetLine_Output']/ELEMENT[TYPE='Element']/ELEMENT_VALUE[FIELD='PNLI']"/>
            </oa:LineNumber>
            <oa:SubLineNumber>
              <xsl:value-of select="/API_CONNECTION_POINT_OUTPUT/API_OUTPUT/TRANSACTION_RESULT/ELEMENT[TYPE='Output']/DATA_SEGMENT[NAME='PPS200MI_GetLine_Output']/ELEMENT[TYPE='Element']/ELEMENT_VALUE[FIELD='PNLS']"/>
            </oa:SubLineNumber>
            <oa:Status>
              <oa:Code></oa:Code>
            </oa:Status>
            <oa:LineType>
              <oa:Code></oa:Code>
            </oa:LineType>
            <oa:Item>
              <oa:ItemID>
                <oa:ID></oa:ID>
              </oa:ItemID>
            </oa:Item>
            <oa:Description></oa:Description>
            <oa:OrderQuantity unitOfMeasure="">
              <xsl:value-of select="/API_CONNECTION_POINT_OUTPUT/API_OUTPUT/TRANSACTION_RESULT/ELEMENT[TYPE='Output']/DATA_SEGMENT[NAME='PPS200MI_GetLine_Output']/ELEMENT[TYPE='Element']/ELEMENT_VALUE[FIELD='ORQA']"/>
            </oa:OrderQuantity>
            <oa:OrderQuantity unitOfMeasure="" quantityType="Received">
              <xsl:value-of select="/API_CONNECTION_POINT_OUTPUT/API_OUTPUT/TRANSACTION_RESULT/ELEMENT[TYPE='Output']/DATA_SEGMENT[NAME='PPS200MI_GetLine_Output']/ELEMENT[TYPE='Element']/ELEMENT_VALUE[FIELD='RVQA']"/>
            </oa:OrderQuantity>
            <oa:OrderQuantity unitOfMeasure="" quantityType="Invoiced">
              <xsl:value-of select="/API_CONNECTION_POINT_OUTPUT/API_OUTPUT/TRANSACTION_RESULT/ELEMENT[TYPE='Output']/DATA_SEGMENT[NAME='PPS200MI_GetLine_Output']/ELEMENT[TYPE='Element']/ELEMENT_VALUE[FIELD='IVQA']"/>
            </oa:OrderQuantity>
            <oa:UnitPrice>
              <oa:Amount currencyID="">
                <xsl:value-of select="/API_CONNECTION_POINT_OUTPUT/API_OUTPUT/TRANSACTION_RESULT/ELEMENT[TYPE='Output']/DATA_SEGMENT[NAME='PPS200MI_GetLine_Output']/ELEMENT[TYPE='Element']/ELEMENT_VALUE[FIELD='PUPR']"/>
              </oa:Amount>
            </oa:UnitPrice>
            <oa:TotalAmount currencyID="">
              <xsl:value-of select="/API_CONNECTION_POINT_OUTPUT/API_OUTPUT/TRANSACTION_RESULT/ELEMENT[TYPE='Output']/DATA_SEGMENT[NAME='PPS200MI_GetLine_Output']/ELEMENT[TYPE='Element']/ELEMENT_VALUE[FIELD='NLAM']"/>
            </oa:TotalAmount>
          </oa:Line>
        </oa:PurchaseOrder>
      </oa:DataArea>
    </oa:Sync>
  </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
```

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_11.png)

5. Copie o **URL** do **Endpoint** e salve-o. Você precisará dele mais tarde ao criar o **Document Flow**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_5.png)

6. Clique em **Save and Deploy**.

***

### Sync.ReceiveDelivery

1. Navegue até **API Gateway** > **Connection Points**.
2. Clique em **Add** e selecione **Create New**.
3. Preencha os detalhes conforme mostrado abaixo:
   * **Name**: `Sync.ReceiveDelivery`
   * **Source Application Name**: `DocBits-Demo`, `DocBits-Prod`, `DocBits-Sandbox` ou `DocBits-Stage` (dependendo do seu ambiente).
   * **Noun**: `ReceiveDelivery`
   * **Verb**: `Sync`
   * **Is enabled**: Marque a caixa.
   * **Cloud Suite Version**: Escolha a versão do Cloud Suite.
   * **Program**: `PPS300MI`
   * **Transaction**: `GetTransLine`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_12.png)

4. Vá para a seção **Mappings** e cole o XML:

```xml
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
  <SOAP-ENV:Header/>
  <SOAP-ENV:Body>
    <oa:Sync xmlns:oa="http://www.openapplications.org/oagis/10" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xsi:schemaLocation="http://www.openapplications.org/oagis/10 BODs/Sync_ReceiveDelivery.xsd">
      <oa:ApplicationArea>
        <oa:Sender>
          <oa:LogicalID></oa:LogicalID>
        </oa:Sender>
        <oa:CreationDateTime></oa:CreationDateTime>
      </oa:ApplicationArea>
      <oa:DataArea>
        <oa:Sync>
          <oa:TenantID></oa:TenantID>
          <oa:AccountingEntityID></oa:AccountingEntityID>
        </oa:Sync>
        <oa:ReceiveDelivery>
          <oa:ReceiveDeliveryHeader>
            <oa:DocumentID>
              <oa:ID accountingEntity="GoodsReceiptNumber">
                <xsl:value-of select="/API_CONNECTION_POINT_OUTPUT/API_OUTPUT/TRANSACTION_RESULT/ELEMENT[TYPE='Output']/DATA_SEGMENT[NAME='PPS300MI_GetTransLine_Output']/ELEMENT[TYPE='Element']/ELEMENT_VALUE[FIELD='REPN']"/>
              </oa:ID>
            </oa:DocumentID>
            <oa:DocumentDateTime qualifier="Actual">
              <xsl:value-of select="/API_CONNECTION_POINT_OUTPUT/API_OUTPUT/TRANSACTION_RESULT/ELEMENT[TYPE='Output']/DATA_SEGMENT[NAME='PPS300MI_GetTransLine_Output']/ELEMENT[TYPE='Element']/ELEMENT_VALUE[FIELD='TRDT']"/>
            </oa:DocumentDateTime>
          </oa:ReceiveDeliveryHeader>
          <oa:Line>
            <oa:LineNumber sequence="">
              <xsl:value-of select="/API_CONNECTION_POINT_OUTPUT/API_OUTPUT/TRANSACTION_RESULT/ELEMENT[TYPE='Output']/DATA_SEGMENT[NAME='PPS300MI_GetTransLine_Output']/ELEMENT[TYPE='Element']/ELEMENT_VALUE[FIELD='RELP']"/>
            </oa:LineNumber>
            <oa:PurchaseOrderLineReference>
              <oa:DocumentReference>
                <oa:DocumentIDs>
                  <oa:DocumentID>
                    <oa:ID accountingEntity="PurchaseOrderNumber">
                      <xsl:value-of select="/API_CONNECTION_POINT_OUTPUT/API_OUTPUT/TRANSACTION_RESULT/ELEMENT[TYPE='Output']/DATA_SEGMENT[NAME='PPS300MI_GetTransLine_Output']/ELEMENT[TYPE='Element']/ELEMENT_VALUE[FIELD='PUNO']"/>
                    </oa:ID>
                  </oa:DocumentID>
                </oa:DocumentIDs>
              </oa:DocumentReference>
              <oa:LineNumber sequence="">
                <xsl:value-of select="/API_CONNECTION_POINT_OUTPUT/API_OUTPUT/TRANSACTION_RESULT/ELEMENT[TYPE='Output']/DATA_SEGMENT[NAME='PPS300MI_GetTransLine_Output']/ELEMENT[TYPE='Element']/ELEMENT_VALUE[FIELD='PNLI']"/>
              </oa:LineNumber>
              <oa:SubLineNumber>
                <xsl:value-of select="/API_CONNECTION_POINT_OUTPUT/API_OUTPUT/TRANSACTION_RESULT/ELEMENT[TYPE='Output']/DATA_SEGMENT[NAME='PPS300MI_GetTransLine_Output']/ELEMENT[TYPE='Element']/ELEMENT_VALUE[FIELD='PNLS']"/>
              </oa:SubLineNumber>
            </oa:PurchaseOrderLineReference>
            <oa:Item>
              <oa:ItemID>
                <oa:ID></oa:ID>
              </oa:ItemID>
            </oa:Item>
            <oa:Description></oa:Description>
            <oa:ReceivedQuantity unitOfMeasure="">
              <xsl:value-of select="/API_CONNECTION_POINT_OUTPUT/API_OUTPUT/TRANSACTION_RESULT/ELEMENT[TYPE='Output']/DATA_SEGMENT[NAME='PPS300MI_GetTransLine_Output']/ELEMENT[TYPE='Element']/ELEMENT_VALUE[FIELD='RVQA']"/>
            </oa:ReceivedQuantity>
            <oa:ReceivedQuantity unitOfMeasure="" quantityType="Invoiced">
              <xsl:value-of select="/API_CONNECTION_POINT_OUTPUT/API_OUTPUT/TRANSACTION_RESULT/ELEMENT[TYPE='Output']/DATA_SEGMENT[NAME='PPS300MI_GetTransLine_Output']/ELEMENT[TYPE='Element']/ELEMENT_VALUE[FIELD='IVQA']"/>
            </oa:ReceivedQuantity>
            <oa:TotalAmount currencyID="">
              <xsl:value-of select="/API_CONNECTION_POINT_OUTPUT/API_OUTPUT/TRANSACTION_RESULT/ELEMENT[TYPE='Output']/DATA_SEGMENT[NAME='PPS300MI_GetTransLine_Output']/ELEMENT[TYPE='Element']/ELEMENT_VALUE[FIELD='NLAM']"/>
            </oa:TotalAmount>
          </oa:Line>
        </oa:ReceiveDelivery>
      </oa:DataArea>
    </oa:Sync>
  </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
```

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_13.png)

5. Copie o **URL** do **Endpoint** e salve-o. Você precisará dele mais tarde ao criar o **Document Flow**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_5.png)

6. Clique em **Save and Deploy**.

***

### Sync.AdvanceShipNotice

1. Navegue até **API Gateway** > **Connection Points**.
2. Clique em **Add** e selecione **Create New**.
3. Preencha os detalhes conforme mostrado abaixo:
   * **Name**: `Sync.AdvanceShipNotice`
   * **Source Application Name**: `DocBits-Demo`, `DocBits-Prod`, `DocBits-Sandbox` ou `DocBits-Stage` (dependendo do seu ambiente).
   * **Noun**: `AdvanceShipNotice`
   * **Verb**: `Sync`
   * **Is enabled**: Marque a caixa.
   * **Cloud Suite Version**: Escolha a versão do Cloud Suite.
   * **Program**: `MMS100MI`
   * **Transaction**: `GetHead`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_14.png)

4. Vá para a seção **Mappings** e cole o XML:

```xml
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
  <SOAP-ENV:Header/>
  <SOAP-ENV:Body>
    <oa:Sync xmlns:oa="http://www.openapplications.org/oagis/10" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xsi:schemaLocation="http://www.openapplications.org/oagis/10 BODs/Sync_AdvanceShipNotice.xsd">
      <oa:ApplicationArea>
        <oa:Sender>
          <oa:LogicalID></oa:LogicalID>
        </oa:Sender>
        <oa:CreationDateTime></oa:CreationDateTime>
      </oa:ApplicationArea>
      <oa:DataArea>
        <oa:Sync>
          <oa:TenantID></oa:TenantID>
          <oa:AccountingEntityID></oa:AccountingEntityID>
        </oa:Sync>
        <oa:AdvanceShipNotice>
          <oa:AdvanceShipNoticeHeader>
            <oa:DocumentID>
              <oa:ID accountingEntity="AdvanceShipNoticeNumber">
                <xsl:value-of select="/API_CONNECTION_POINT_OUTPUT/API_OUTPUT/TRANSACTION_RESULT/ELEMENT[TYPE='Output']/DATA_SEGMENT[NAME='MMS100MI_GetHead_Output']/ELEMENT[TYPE='Element']/ELEMENT_VALUE[FIELD='DLIX']"/>
              </oa:ID>
            </oa:DocumentID>
            <oa:ShipToParty>
              <oa:PartyID>
                <oa:ID accountingEntity="CustomerNumber">
                  <xsl:value-of select="/API_CONNECTION_POINT_OUTPUT/API_OUTPUT/TRANSACTION_RESULT/ELEMENT[TYPE='Output']/DATA_SEGMENT[NAME='MMS100MI_GetHead_Output']/ELEMENT[TYPE='Element']/ELEMENT_VALUE[FIELD='CUNO']"/>
                </oa:ID>
              </oa:PartyID>
            </oa:ShipToParty>
            <oa:BillToParty>
              <oa:PartyID>
                <oa:ID accountingEntity="PayerNumber">
                  <xsl:value-of select="/API_CONNECTION_POINT_OUTPUT/API_OUTPUT/TRANSACTION_RESULT/ELEMENT[TYPE='Output']/DATA_SEGMENT[NAME='MMS100MI_GetHead_Output']/ELEMENT[TYPE='Element']/ELEMENT_VALUE[FIELD='PYNO']"/>
                </oa:ID>
              </oa:PartyID>
            </oa:BillToParty>
          </oa:AdvanceShipNoticeHeader>
        </oa:AdvanceShipNotice>
      </oa:DataArea>
    </oa:Sync>
  </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
```

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_15.png)

5. Copie o **URL** do **Endpoint** e salve-o. Você precisará dele mais tarde ao criar o **Document Flow**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_5.png)

6. Clique em **Save and Deploy**.

***

### Sync.ChartOfAccounts

1. Navegue até **API Gateway** > **Connection Points**.
2. Clique em **Add** e selecione **Create New**.
3. Preencha os detalhes conforme mostrado abaixo:
   * **Name**: `Sync.ChartOfAccounts`
   * **Source Application Name**: `DocBits-Demo`, `DocBits-Prod`, `DocBits-Sandbox` ou `DocBits-Stage` (dependendo do seu ambiente).
   * **Noun**: `ChartOfAccounts`
   * **Verb**: `Sync`
   * **Is enabled**: Marque a caixa.
   * **Cloud Suite Version**: Escolha a versão do Cloud Suite.
   * **Program**: `CRS630MI`
   * **Transaction**: `Get`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_16.png)

4. Vá para a seção **Mappings** e cole o XML:

```xml
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
  <SOAP-ENV:Header/>
  <SOAP-ENV:Body>
    <oa:Sync xmlns:oa="http://www.openapplications.org/oagis/10" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xsi:schemaLocation="http://www.openapplications.org/oagis/10 BODs/Sync_ChartOfAccounts.xsd">
      <oa:ApplicationArea>
        <oa:Sender>
          <oa:LogicalID></oa:LogicalID>
        </oa:Sender>
        <oa:CreationDateTime></oa:CreationDateTime>
      </oa:ApplicationArea>
      <oa:DataArea>
        <oa:Sync>
          <oa:TenantID></oa:TenantID>
          <oa:AccountingEntityID></oa:AccountingEntityID>
        </oa:Sync>
        <oa:ChartOfAccounts>
          <oa:GLEntity>
            <oa:GLEntityID></oa:GLEntityID>
            <oa:AccountID>
              <xsl:value-of select="/API_CONNECTION_POINT_OUTPUT/API_OUTPUT/TRANSACTION_RESULT/ELEMENT[TYPE='Output']/DATA_SEGMENT[NAME='CRS630MI_Get_Output']/ELEMENT[TYPE='Element']/ELEMENT_VALUE[FIELD='KODA']"/>
            </oa:AccountID>
            <oa:Description>
              <xsl:value-of select="/API_CONNECTION_POINT_OUTPUT/API_OUTPUT/TRANSACTION_RESULT/ELEMENT[TYPE='Output']/DATA_SEGMENT[NAME='CRS630MI_Get_Output']/ELEMENT[TYPE='Element']/ELEMENT_VALUE[FIELD='TX40']"/>
            </oa:Description>
          </oa:GLEntity>
        </oa:ChartOfAccounts>
      </oa:DataArea>
    </oa:Sync>
  </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
```

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_17.png)

5. Copie o **URL** do **Endpoint** e salve-o. Você precisará dele mais tarde ao criar o **Document Flow**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_5.png)

6. Clique em **Save and Deploy**.

***

### Sync.CodeDefinition-AccountingDimension

1. Navegue até **API Gateway** > **Connection Points**.
2. Clique em **Add** e selecione **Create New**.
3. Preencha os detalhes conforme mostrado abaixo:
   * **Name**: `Sync.CodeDefinition-AccountingDimension`
   * **Source Application Name**: `DocBits-Demo`, `DocBits-Prod`, `DocBits-Sandbox` ou `DocBits-Stage` (dependendo do seu ambiente).
   * **Noun**: `CodeDefinition-AccountingDimension`
   * **Verb**: `Sync`
   * **Is enabled**: Marque a caixa.
   * **Cloud Suite Version**: Escolha a versão do Cloud Suite.
   * **Program**: `CRS105MI`
   * **Transaction**: `Get`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_18.png)

4. Vá para a seção **Mappings** e cole o XML:

```xml
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
  <SOAP-ENV:Header/>
  <SOAP-ENV:Body>
    <oa:Sync xmlns:oa="http://www.openapplications.org/oagis/10" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xsi:schemaLocation="http://www.openapplications.org/oagis/10 BODs/Sync_CodeDefinition-AccountingDimension.xsd">
      <oa:ApplicationArea>
        <oa:Sender>
          <oa:LogicalID></oa:LogicalID>
        </oa:Sender>
        <oa:CreationDateTime></oa:CreationDateTime>
      </oa:ApplicationArea>
      <oa:DataArea>
        <oa:Sync>
          <oa:TenantID></oa:TenantID>
          <oa:AccountingEntityID></oa:AccountingEntityID>
        </oa:Sync>
        <oa:CodeDefinition typeCode="AccountingDimension">
          <oa:CodeID>
            <xsl:value-of select="/API_CONNECTION_POINT_OUTPUT/API_OUTPUT/TRANSACTION_RESULT/ELEMENT[TYPE='Output']/DATA_SEGMENT[NAME='CRS105MI_Get_Output']/ELEMENT[TYPE='Element']/ELEMENT_VALUE[FIELD='STAT']"/>
          </oa:CodeID>
          <oa:Description>
            <xsl:value-of select="/API_CONNECTION_POINT_OUTPUT/API_OUTPUT/TRANSACTION_RESULT/ELEMENT[TYPE='Output']/DATA_SEGMENT[NAME='CRS105MI_Get_Output']/ELEMENT[TYPE='Element']/ELEMENT_VALUE[FIELD='TX40']"/>
          </oa:Description>
        </oa:CodeDefinition>
      </oa:DataArea>
    </oa:Sync>
  </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
```

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_19.png)

5. Copie o **URL** do **Endpoint** e salve-o. Você precisará dele mais tarde ao criar o **Document Flow**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_5.png)

6. Clique em **Save and Deploy**.

***

## Passo 3: Criar o Document Flow

1. Abra o **DocBits** e navegue até **Settings** > **Document Flow**.
2. Clique em **Add Document Flow**.
3. Preencha o campo **Document Flow Name** e clique em **Add**.
4. Selecione o **Document Flow** que você acabou de criar.
5. Clique em **Add Node** e selecione **API Call**.
6. Preencha os campos:
   * **Name**: `Get Supplier Data`
   * **Trigger Type**: `Manual with Document`, `Automated with Button Click` ou `Automated with Status` (dependendo das suas necessidades).
   * **URL**: Cole o URL do **Endpoint** que você copiou anteriormente para `Sync.SupplierPartyMaster`.
   * **HTTP Method**: `POST`
   * **Authorization Type**: `Basic Auth`
   * **Username**: Seu nome de usuário do Infor.
   * **Password**: Sua senha do Infor.
7. Clique em **Request** e cole o XML do **Body**:

```xml
<?xml version="1.0" encoding="utf-8"?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:cred="http://schemas.infor.com/iam/security/Credentials/1" xmlns:ion="http://schema.infor.com/InforOAGIS/2" xmlns:head="http://schema.infor.com/ws-header">
  <soapenv:Header>
    <wsse:Security xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd" xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd">
      <wsse:UsernameToken>
        <wsse:Username>{username}</wsse:Username>
        <wsse:Password Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordText">{password}</wsse:Password>
      </wsse:UsernameToken>
    </wsse:Security>
  </soapenv:Header>
  <soapenv:Body>
    <ion:APIRequest>
      <head:APISessionContext>
        <head:TenantID>infor</head:TenantID>
        <head:UserContext>
          <head:UserID/>
          <head:DomainID/>
          <head:AccountingEntityID>{DivisionID}</head:AccountingEntityID>
        </head:UserContext>
      </head:APISessionContext>
      <ion:APIInvoke>
        <cred:Credentials>
          <cred:Company>{Division}</cred:Company>
        </cred:Credentials>
        <m3api:M3APIRequest xmlns:m3api="http://schema.infor.com/m3api">
          <m3api:Program>MMS024MI</m3api:Program>
          <m3api:Transaction>Get</m3api:Transaction>
          <m3api:Record>
            <m3api:NameValue name="IDSUNO">
              <m3api:Value>{Supplier_ID}</m3api:Value>
            </m3api:NameValue>
          </m3api:Record>
        </m3api:M3APIRequest>
      </ion:APIInvoke>
    </ion:APIRequest>
  </soapenv:Body>
</soapenv:Envelope>
```

8. Clique em **Save**.
9. Repita os passos 5 a 8 para os demais **Connection Points** (`Sync.RemitToPartyMaster`, `Acknowledge.SupplierInvoice`, `Sync.PurchaseOrder`, `Sync.ReceiveDelivery`, `Sync.AdvanceShipNotice`, `Sync.ChartOfAccounts`, `Sync.CodeDefinition-AccountingDimension`).
10. Clique em **Save** para salvar o **Document Flow**.

***

Agora você configurou com sucesso a importação de dados do Infor M3 para o DocBits via API.
