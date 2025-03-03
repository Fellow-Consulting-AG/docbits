# List Of Values

<figure><img src="../../../.gitbook/assets/Bildschirmfoto%202024-05-08%20um%2011.20.51.png" alt=""><figcaption></figcaption></figure>

A configuração "Lista de Valores" em seu sistema de processamento de documentos é essencialmente um repositório central para gerenciar valores predefinidos que podem ser usados em vários formulários e campos dentro do sistema. Essa configuração é particularmente útil para padronizar a entrada de dados e garantir consistência em documentos processados pelo sistema.

1. **Segmentação por Tipo**: Cada seção, como "ISO\_Currency", "Invoice\_Sub\_Type", "Invoice\_Type" e "Test", representa uma categoria diferente de valores predefinidos. Essas categorias são usadas para gerenciar diferentes tipos de entradas de dados relevantes para seus contextos específicos dentro do sistema.
2. **Valores e Sinônimos**: Sob cada categoria, você pode definir vários valores. Por exemplo, sob "Invoice\_Sub\_Type", valores como "Fatura de Custo" e "Fatura de Compra" são listados. Além disso, você tem a capacidade de atribuir sinônimos a esses valores, aprimorando a flexibilidade e alcance da captura de dados. Por exemplo, "Fatura de Custo" tem sinônimos como "Kostenrechnung" e "Cost Invoice".
3. **Uso em Sub-Organizações**: Esses valores também podem ser específicos para determinadas sub-organizações em sua configuração, permitindo a personalização e localização dos fluxos de trabalho de processamento de documentos.
4.  **Adicionando e Gerenciando Valores**: Quando você pressiona o botão de ação, são apresentadas duas opções para adicionar valores à sua lista. A primeira opção é adicionar linhas manualmente. Ao clicar no botão **Add Row**, um popup aparece que permite que você introduza novos valores junto com quaisquer sinônimos. Se você precisar adicionar várias entradas, pode simplesmente clicar em **Add More Values** para gerar outra linha.

    A segunda opção é fazer o upload de um arquivo CSV. Para fazer isso, clique no botão **Upload CSV**, selecione um arquivo **CSV** que deseja importar, escolha o delimitador correto para garantir que os dados sejam analisados corretamente e, em seguida, clique em **Upload** para concluir o processo.

    Além disso, cada linha inclui um botão de ação que permite editar ou excluir uma entrada existente conforme necessário.
