# Status de desativação de pedido de compra

### **Configuração para desativar status de PO**

Vá para **Configurações → Configurações Gerais → Tipos de Documentos → Mais Configurações → Seção de Pedido de Compra → Status de Desativação de PO**

#### **Como Funciona**

A configuração **Status de Desativação de PO** permite que os usuários especifiquem status de pedido de compra (PO) que impedem que as faturas sejam correspondidas a esses POs. Se um pedido de compra tiver um status listado nesta configuração, ele **não pode** ser usado para correspondência de faturas na tela de correspondência de PO. Isso interromperá o processamento adicional do PO até que seu status mude para um que não esteja desativado.

Isso interromperá o processamento adicional da fatura até que o status do PO mude para um que não esteja desativado. Usando esta configuração, os usuários podem garantir que pedidos de compra com status específicos não passem por processamento adicional de faturas, reduzindo erros e evitando pagamentos desnecessários.

#### **Como Identificar um Pedido de Compra Desativado**

Na tela de **Correspondência de PO**, um pedido de compra desativado aparece **riscado**. Isso indica visualmente que o PO está atualmente restrito de ser correspondido devido ao seu status.

![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FT2n2w4uDCJvv7CJ5zrdk%2Fuploads%2FDbA2CsBn6twgp5BrSvgV%2Fimage.png?alt=media\&token=211bd6a2-4136-4ea0-85cf-e17f428fa0da)

#### **Como Configurá-lo**

* Na configuração **Status de Desativação de PO**, você verá um campo de seleção no lado esquerdo.
*   Clicar neste campo abre uma lista suspensa de status de PO disponíveis.

    ​

    ![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FT2n2w4uDCJvv7CJ5zrdk%2Fuploads%2FgvmAKBrVLXhDwKe7RIBe%2Fimage.png?alt=media\&token=0f98186b-3f50-483c-8465-a75972e9386a)
* Selecione um ou mais status clicando neles. Clique novamente para desmarcar.
* Clique no botão **Aplicar** para salvar suas alterações.

![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FT2n2w4uDCJvv7CJ5zrdk%2Fuploads%2F5FCyl2giTsZeu8487ai9%2Fimage.png?alt=media\&token=5e7c0ee4-1629-44e0-a4c5-056d7efa320f)

**Status Disponíveis**

* Cancelado
* Excluído
* Faturado
* Aberto
* Parcialmente Faturado
* Parcialmente Recebido
* Recebido
* Não Aprovado
* Em Espera
* Fechado
