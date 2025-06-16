# Tela de Correspondência de Ordem de Compra

## Visão Geral

Na tela de **Correspondência de Ordem de Compra**, você pode comparar os itens de linha extraídos do seu documento com aqueles armazenados no **sistema Infor**, usando o número do pedido de compra como referência.

Você pode:

* **Identificar imediatamente** quaisquer diferenças entre os dados extraídos e armazenados
* **Definir tolerâncias** para permitir desvios aceitáveis
* **Ignorar status específicos** do Infor, se necessário
* **Aprovar e exportar** o documento após uma correspondência bem-sucedida
* **Rejeitar** o documento se os dados não atenderem aos critérios de validação exigidos

Esta página irá guiá-lo através do processo de correspondência de ordens de compra e explicar toda a funcionalidade relacionada disponível nesta seção.

## Ferramentas na Tela de Correspondência de Ordem de Compra

Na parte superior da tela de Correspondência de Ordem de Compra, você encontrará várias ferramentas—como **Salvar**, **Auto-Corrigir**, **Exportar**, e outras—que auxiliam no processo de correspondência.\
Uma descrição detalhada de cada ferramenta e sua funcionalidade pode ser encontrada [aqui](purchase-order-matching-tools.md).

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FxPOM1IzmTGgCCAE4tAQg%252Fpo_match_tools_0.png%3Falt%3Dmedia%26token%3D420e0d50-d5c8-4b7b-8ec6-26ca9e2d7a68\&width=768\&dpr=4\&quality=100\&sign=5d32419c\&sv=2)

## Filtrar e Adicionar Números de Ordem de Compra

Você pode pesquisar números de ordem de compra específicos inserindo o número no campo de pesquisa.\
Para um filtro mais refinado, clique no ícone no lado direito da barra de pesquisa para selecionar critérios específicos para sua pesquisa.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F3xeAcb5EwKQPg9rksZVE%252Fpo_match_3.png%3Falt%3Dmedia%26token%3Deef4e964-ffe5-485c-ae22-c5790a9302fc\&width=768\&dpr=4\&quality=100\&sign=b0830e56\&sv=2)

As seguintes opções de filtro estão disponíveis para ajudá-lo a refinar sua pesquisa por ordens de compra:

* **Palavra-chave** – Filtrar por números de ordem de compra.
* **Fornecedor** – Filtrar por nome ou ID do fornecedor.
* **Após a data** – Mostrar ordens de compra criadas após uma data específica.
* **Antes da data** – Mostrar ordens de compra criadas antes de uma data específica.
* **Valor mínimo do pedido** – Filtrar por valor mínimo do pedido.
* **Valor máximo do pedido** – Filtrar por valor máximo do pedido.
* **Ordenar por** – Selecionar o atributo para ordenar os resultados (por exemplo, data, valor).
* **Direção de classificação** – Escolher a ordem de classificação: crescente ou decrescente.
* **Número de registros a serem exibidos** – Definir quantos resultados devem ser mostrados por página.
* **Mais** – Opções de filtragem adicionais incluem:
  * **Número de entrega**
  * **Número do comprovante de embalagem**
  * **ID do item**

Após configurar seus filtros, clique em **Aplicar** para aplicá-los ou **Claro** para redefinir todas as configurações de filtro.

As ordens de compra correspondentes serão exibidas com base nos filtros aplicados.\
Você pode:

* Ajustar os filtros e pesquisar novamente, ou
* Clicar duas vezes em uma entrada de ordem de compra para adicioná-la à tela de Correspondência de Ordem de Compra.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F2uwMlpQ42lG5fOvUy4Gx%252Fpo_match_5.png%3Falt%3Dmedia%26token%3De2751f7f-586e-4303-bb17-db2a56de2b0b\&width=768\&dpr=4\&quality=100\&sign=fbf27bf2\&sv=2)

## Selecionar Números de Ordem de Compra e Reorganizar Colunas

Você pode alternar entre ordens de compra individuais para visualizar seus respectivos itens de linha clicando no número da ordem de compra na parte superior da tabela.

Você também pode reorganizar as colunas dentro de cada visualização de ordem de compra simplesmente arrastando e soltando-as na sua ordem preferida.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FwZzMEbGz7j20tIsouC8V%252Fpo_match_7.png%3Falt%3Dmedia%26token%3D6dc539ab-33af-40a6-8c82-04449ba317e4\&width=768\&dpr=4\&quality=100\&sign=3b8fd876\&sv=2)

Para ocultar permanentemente colunas específicas, use o recurso [**Definir colunas da tabela PO para organização**](./#definir-colunas-da-tabela-po-para-organizacao).

## Definir Colunas da Tabela PO para Organização

Você tem a opção de ocultar ou mostrar colunas específicas na tabela de ordens de compra clicando no ícone de configurações da coluna (mostrado abaixo).\
Esta configuração está disponível tanto na tela de **Correspondência de Ordem de Compra** quanto no menu de **Pesquisa Avançada de Ordem de Compra**.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F4nQ5loSdHlIebOh4vJ1m%252Fpo_tools_new_10.png%3Falt%3Dmedia%26token%3D84991cc8-f7ae-40f1-ba6c-cdd66722b898\&width=768\&dpr=4\&quality=100\&sign=ec34b898\&sv=2)

Mais detalhes podem ser encontrados [aqui](purchase-order-matching-tools.md#definir-colunas-da-tabela-po-para-organizacao).

## Re-Sincronizar o número da ordem de compra com o Infor

Para ressincronizar os dados no **DocBits** com os dados do **Infor**, clique no **botão de atualizar** ao lado do número da ordem de compra acima da tabela.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FNQiPjtumht4wV9z8VHtw%252Fpo_match_8.png%3Falt%3Dmedia%26token%3Dcd9cb152-6b2f-475e-abeb-e9ad1cbd46cf\&width=768\&dpr=4\&quality=100\&sign=adab84c\&sv=2)

Se seu processo de correspondência for baseado no atributo **Quantidade de entrega aberta recebida**, você também tem a opção de realizar uma **sincronização manual**, conforme descrito em detalhes [aqui](purchase-order-matching-tools.md#sincronizar-dados).

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FcceZaArRjBdKpI5r5u1v%252Fpo_tools_new_7.png%3Falt%3Dmedia%26token%3D49e25f09-de07-42b7-ab3d-a43a35e567c5\&width=768\&dpr=4\&quality=100\&sign=c6e75393\&sv=2)

## Como fazer a correspondência?

Para corresponder um item de linha de ordem de compra com um item de linha extraído do documento, você tem três opções:

1. **Arrastar e Soltar**\
   Arraste o item de linha da ordem de compra desejada e solte-o sobre o item de linha correspondente na tabela extraída.
2. **Clique com o Botão Direito e Conectar**
   * Clique com o botão direito no item de linha da ordem de compra que você deseja corresponder e selecione **Selecionar para correspondência**.
   * Em seguida, clique com o botão direito no item de linha correspondente na tabela extraída e selecione **Conectar**.
3.  **Auto-Corrigir**

    Clique no botão **Auto-Corrigir** para permitir que o sistema tente automaticamente corresponder todos os itens de linha com base nos dados extraídos e da ordem de compra.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Flsdom16blO6pMF5rtQYS%252Fpo_tools_new_5.png%3Falt%3Dmedia%26token%3D616d6600-ff52-478a-9282-518212360106\&width=768\&dpr=4\&quality=100\&sign=ad47d853\&sv=2)

Você também pode selecionar **várias linhas de ordem de compra** e correspondê-las a uma **única linha** na tabela extraída.

## Quais colunas estão sendo correspondidas?

O processo de Correspondência de Ordem de Compra corresponde apenas a colunas específicas. A lista abaixo descreve quais colunas são correspondidas, se disponíveis. Se nenhuma [tolerância](./#aceitar-tolerancias) estiver definida, as colunas só corresponderão se forem uma correspondência exata (100%).

* [Quantidade](./#quantidade) (Quantidade | Quantidade Recebida | Quantidade de entrega aberta recebida)
* Preço Unitário
* Número do Pedido de Compra
* Número do Item/ID do Item do Fornecedor
* Data de Entrega Prometida

### Quantidade

Você tem três opções para corresponder a quantidade.

* Quantidade
* Quantidade Recebida
* Quantidade de entrega aberta recebida

Você pode definir esta opção em **Configurações → Configurações globais → Tipos de documentos → Mais configurações → Seção de Ordem de Compra → Ordem de Compra**

## Aceitar Tolerâncias

Você pode especificar níveis de tolerância aceitáveis durante o processo de correspondência.\
Por padrão, apenas correspondências exatas (100%) são consideradas válidas.

Se as tolerâncias estiverem configuradas nas configurações do sistema, você pode ajustá-las para os atributos permitidos diretamente na **Tabela Extraída** sob a coluna **Ações**.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FJLdikqwBf45WgFqlPUYW%252Fpo_match_11.png%3Falt%3Dmedia%26token%3D0c9d533f-f994-472a-9ff8-75ef564cef5e\&width=768\&dpr=4\&quality=100\&sign=b0c004c0\&sv=2)

Para mais informações sobre como configurar e usar tolerâncias, consulte a [documentação detalhada](../../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-tolerance-settings-additional-purchase-order-tolerance.md).

## Desativar status

Você pode excluir linhas específicas com certos status de serem correspondidas. Para mais informações, consulte a [documentação detalhada](../../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-disable-statuses.md).

## Verificar linhas correspondidas

Vários indicadores estão disponíveis para ajudá-lo a verificar se um item de linha foi correspondido com sucesso ou não.

### Tabela de Ordem de Compra

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FB3LlWddnfNcu8kUedbvb%252Fpo_match_14.png%3Falt%3Dmedia%26token%3D484a856a-b8b2-439f-bbf9-35dd4bb55343\&width=768\&dpr=4\&quality=100\&sign=b71ea425\&sv=2)

* Este ícone indica que o item de linha da ordem de compra foi correspondido com sucesso.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F2vcst2wCfyck9Z7ak4eO%252Fguide_po_2.png%3Falt%3Dmedia%26token%3D78f7a224-ba6b-4027-b6a0-61e5502fd7c2\&width=768\&dpr=4\&quality=100\&sign=e0d60903\&sv=2)

* Este ícone indica que o item de linha da ordem de compra contém uma discrepância.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FAb1A9PwBhrvfAf5q7f5w%252Fguide_po_5.png%3Falt%3Dmedia%26token%3D6616b59d-ffa4-4202-9382-3ac8ecd8b913\&width=768\&dpr=4\&quality=100\&sign=dd476496\&sv=2)

### Tabela Extraída do Documento

*   Este ícone indica que o item de linha foi correspondido com sucesso. Você pode passar o mouse sobre o ícone para destacar a linha correspondente da ordem de compra.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Flogrk90Ufp5NQ7fd1QEX%252Fpo_match_15.png%3Falt%3Dmedia%26token%3D59c96286-24e9-4790-a9db-8c02efaed305\&width=768\&dpr=4\&quality=100\&sign=1a296310\&sv=2)
*   Este ícone indica que o item de linha contém uma discrepância. Você pode passar o mouse sobre o ícone para destacar a linha correspondente da ordem de compra e visualizar as colunas onde ocorrem discrepâncias.

    ![](../../../.gitbook/assets/po_match_new_4.png)

## Múltiplas Correspondências

Se um único item de linha for correspondido a várias linhas, você pode visualizar informações detalhadas clicando no ícone de mais (+) ao lado do respectivo item de linha.

Isso expande a visualização para mostrar todas as entradas correspondidas, ajudando você a verificar e gerenciar múltiplas correspondências de forma eficaz.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FXueoHfU6EiDKaWBKJL2X%252Fpo_match_19.png%3Falt%3Dmedia%26token%3D9b947abd-5fbc-45e7-8e55-8b38746b5e32\&width=768\&dpr=4\&quality=100\&sign=191a712\&sv=2)

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FZJZekesrA0JB04GixOUi%252Fpo_match_18.png%3Falt%3Dmedia%26token%3D25c10718-2044-4de9-a5db-45f936d7235a\&width=768\&dpr=4\&quality=100\&sign=dd63d6c4\&sv=2)

## Remover Conexões de PO

Para remover uma conexão entre um item de linha de ordem de compra e um item de linha extraído, basta clicar no ícone **X** ao lado do par correspondido.\
Uma vez removida, a conexão é cancelada e o item de linha se torna disponível para correspondência novamente.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FSznmTo3Fnfi72ccpuLZk%252Fpo_match_new_2.png%3Falt%3Dmedia%26token%3Da04727b2-c8bf-44e0-b8f4-eaedb8180500\&width=768\&dpr=4\&quality=100\&sign=b740b466\&sv=2)

## Cálculo

Abaixo da tabela contendo as informações extraídas do seu documento, você pode encontrar cálculos simples para verificar se as reservas totais correspondem.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FA3TOYG26aHrETnMz4ADB%252Fimage.png%3Falt%3Dmedia%26token%3Db481bbc5-d278-4a46-b3cf-813225fa10ca\&width=768\&dpr=4\&quality=100\&sign=eeca6ad9\&sv=2)

### Reservas registradas:

O valor das reservas registradas é derivado do valor líquido extraído do documento.

```
Reservas registradas = Montante líquido total (extraído do documento)
```

### Total correspondido:

Esse valor é calculado somando o **Preço Unitário** × **Quantidade** para todos os itens de linha que foram correspondidos com sucesso com os itens de linha do número da ordem de compra.

```
 Total Correspondido = Soma de (Preço Unitário × Quantidade) para todos os itens de linha correspondidos
```

### **Encargos:**

Quaisquer encargos aplicáveis serão incluídos nesta seção, se presentes.\
Para mais detalhes, consulte a [documentação detalhada](../../../administration-and-setup/settings/document-processing/classification-and-extraction/table-extraction-for-costing-element.md).

```
Encargos = Elemento de custo
```

### Valor não liquidado:

A diferença resultante é exibida aqui e é calculada da seguinte forma:

```
Valor não liquidado = Reservas registradas - Total correspondido - Elemento de custo
```

## Visualizando o Documento para Validação

No lado direito da tela de **Correspondência de Ordem de Compra**, você pode visualizar o documento para auxiliar na validação.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F7X5cxghPovZfE8B2hvIy%252Fpo_new_1.png%3Falt%3Dmedia%26token%3D613a52db-b1a7-4d15-af8e-ab63725ae78c\&width=768\&dpr=4\&quality=100\&sign=3a887d60\&sv=2)

**Recursos da Barra de Ferramentas do Visualizador de Documentos:**

* Role pelas páginas do documento para revisar o conteúdo.
* Clique no nome do arquivo para abrir a tela de validação completa.
* Insira um número de página e pressione Enter para pular diretamente para essa página.
* Use os botões de mais (+) e menos (–) para aumentar ou diminuir o zoom do documento.
*   Clique no botão no extremo direito para abrir o documento em uma janela separada, o que é especialmente útil ao trabalhar com várias telas.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F8nUElRimoIOprR5yV5lN%252Fpo_match_10.png%3Falt%3Dmedia%26token%3De0d6924c-127f-4333-95f9-1b32d52b0da5\&width=768\&dpr=4\&quality=100\&sign=4f8161e4\&sv=2)

## Salvando Alterações:

Para salvar suas alterações, clique no botão **Salvar** na barra de ferramentas.\
Se você sair da página sem salvar, todo o progresso feito durante o processo de correspondência será perdido.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FZ9ou72AJwvme2F7RWG7P%252Fpo_tools_new_6.png%3Falt%3Dmedia%26token%3D1d8ef55e-5ff1-4ee7-ac81-b76ff583a353\&width=768\&dpr=4\&quality=100\&sign=a17e5c90\&sv=2)

## Exportando o Documento

Após corresponder todos os itens de linha e validar sua correção, você pode exportar o documento clicando no botão **Exportar** na barra de ferramentas.

* Clicar na pequena seta ao lado do botão **Exportar** revela todas as opções de exportação disponíveis.
* Clicar em **Exportar** diretamente acionará a opção de exportação padrão (a primeira da lista).

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fzc78lqQthkeTIpANlIAc%252Fpo_tools_new_8.png%3Falt%3Dmedia%26token%3Debdb58e9-b775-40a6-b7bc-82aa66f8811b\&width=768\&dpr=4\&quality=100\&sign=14ac5a25\&sv=2)
