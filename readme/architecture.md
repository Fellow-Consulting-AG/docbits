# Arquitetura

<figure><img src=".gitbook/assets/DocBits_D_Doc2-Infor-1.png" alt=""><figcaption></figcaption></figure>

O Doc**Bits** integra-se perfeitamente com o Infor LN/M3 através da API ION, ION Desk e Infor Standard BODs. Nossa integração de API nos permite exportar dados para o Infor e realizar validação de dados mestres no Doc**Bits**.

## Exportando Dados para o Infor

Utilizamos a API ION para enviar o PDF com atributos para o IDM e o BOD Sync.CaptureDocument para o ION Desk. No ION Desk, transformamos o [Sync.CaptureDocument](admin-section/setup/exporting-in-docbits/) nos BODs de destino desejados com base no tipo de documento em processamento. Esses BODs do Infor transformados são então importados automaticamente para LN ou M3.

{% hint style="info" %}
Exportar para [Infor](admin-section/setup/exporting-in-docbits/exporting-to-infor/)&#x20;
{% endhint %}

## Validação de Dados Mestres no DocBits

Para identificar o fornecedor ou comparar/corresponder linhas de pedidos de compra, ativamos um gatilho no LN/M3 que envia os BODs Sync.RemitToPartyMaster, Sync.SupplierPartyMaster e Sync.PurchaseOrder para o Doc**Bits**. Configuramos esse processo no ION Desk definindo o fluxo de dados para um ponto de conexão específico para o Doc**Bits**.
