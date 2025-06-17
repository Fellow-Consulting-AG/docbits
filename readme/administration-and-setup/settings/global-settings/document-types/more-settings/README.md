# Mais Configurações

## Visão Geral

Na seção "Mais Configurações", você pode encontrar várias opções relacionadas a tipos de documentos individuais. Uma vez que uma configuração é ativada, ela se aplicará apenas a esse tipo específico de documento. Esta página fornece uma breve visão geral do que cada configuração faz.

## Como Acessar

1.  Navegue até **Configurações** -> **Configurações Globais** -> **Tipos de Documentos**.

    <figure><img src="../../../../../.gitbook/assets/Calculate_PO_unit_price_1.png" alt=""><figcaption></figcaption></figure>
2.  Selecione o tipo de documento desejado e clique em **Mais Configurações**.

    <figure><img src="../../../../../.gitbook/assets/Calculate_PO_unit_price_2.png" alt=""><figcaption></figcaption></figure>

## Extração de Tabelas

* **Ignorar validação de tabela**: Permite contornar o processo de validação para dados de tabela, o que pode ser útil em cenários onde a validação de dados precisa ser flexível.

## Detecção de Duplicados

* [**Detecção de Documentos Duplicados**](duplicate-document-handling.md): Isso permite que você detecte e gerencie documentos duplicados.

## Em Revisão

* **Design no Formulário de Revisão**: Configura o layout e os campos que aparecem nos formulários de revisão usados durante o processo de revisão do documento.

## Rejeitar

* **Design no Formulário de Rejeição**: Configura o layout e os campos exibidos no formulário de rejeição usado durante o processo de revisão do documento.

## Geração de PDF

* **Modelo de Design**: Especifica o modelo usado para gerar versões em PDF dos documentos, o que pode ser crucial para arquivamento ou comunicação externa.

## Exportar Formato PDF

* **Formato de Arquivo de Exportação**: Permite que você especifique o formato PDF a ser usado ao exportar documentos.

## Aprovação

* **Aprovar antes da exportação**: Garante que os documentos devem ser aprovados antes de serem exportados do sistema. Além disso, você pode projetar o modelo usado para a tela de aprovação.
* **Aprovar antes da exportação V2**: Habilita a Aprovação V2, permitindo o uso de campos dinâmicos em vez de estáticos. Você também pode personalizar o modelo da tela de aprovação.
* **Segunda Aprovação**: Adiciona uma camada adicional de aprovação para validação adicional, aprimorando o controle sobre o processamento de documentos. Você também pode personalizar o modelo usado para a tela de aprovação.
* [**Selo de Aprovação**](approval/approval-stamp.md): Adiciona um selo ao documento quando ele é aprovado.
* **Histórico de Aprovação**: Permite a exibição do histórico de aprovação tanto na tela de aprovação quanto na validação de campos.

## Ordem de Compra

* [**Tabela de OC no construtor de layout**](purchase-order/po-table-in-layout-builder.md): Permite a inclusão de tabelas de ordem de compra no construtor de layout para layouts de documentos personalizados.
* [**Verificação automática de atualizações de OC**](purchase-order/auto-check-for-po-updates.md): Quando ativado, o sistema exibe um indicador visual na tela de Correspondência de Ordem de Compra para mostrar quando uma ordem de compra foi atualizada, solicitando aos usuários que atualizem para as informações mais recentes.
* **Atualizar dados da OC automaticamente**: Ativar isso atualizará automaticamente os dados da OC quando novos dados estiverem disponíveis.
* **Status da linha da OC consumida**: Ativar isso desativará a tonalidade colorida nas linhas da ordem de compra.
* [**Calcular preço unitário da OC**](purchase-order/calculate-po-unit-price.md): Isso permite que você calcule o preço unitário da OC usando o valor líquido e a quantidade, em vez de extraí-lo.
* **Ordem de Compra**: Alterna se o documento deve ser processado na tela de Correspondência de Ordem de Compra. Você também pode especificar qual termo de quantidade o processo de correspondência deve ser baseado.
* [**Exportar linhas de OC não correspondidas**](purchase-order/export-not-matched-po-lines.md): Este recurso controla a exportação de linhas de ordem de compra. Quando desativado, apenas linhas correspondidas são exportadas. Quando ativado, todas as linhas de ordem de compra são exportadas, mesmo que não estejam correspondidas a uma linha de confirmação de pedido.
* [**Configuração de Tolerância da OC**](purchase-order/purchase-order-tolerance-settings-additional-purchase-order-tolerance.md): Este recurso permite que você defina níveis de tolerância para quantidade e preço unitário, acomodando pequenas discrepâncias sem marcá-las como incompatibilidades.
* [**Configuração Adicional de Tolerância da OC**](purchase-order/purchase-order-tolerance-settings-additional-purchase-order-tolerance.md#configuracao-para-configurar-configuracoes-adicionais-de-tolerancia-de-pedido-de-compra): Este recurso permite que você defina níveis de tolerância adicionais para frete, encargos e impostos, acomodando pequenas discrepâncias sem marcá-las como incompatibilidades.
* [**Exportação Alternativa**](purchase-order/alternate-export.md): Isso permite que você configure uma exportação alternativa para status específicos.
* [**Desativar status da OC**](purchase-order/purchase-order-disable-statuses.md): Permite que você desative status específicos de serem considerados no processo de correspondência.
* **Ignorar Linhas Já Correspondidas**: Ativar isso pulará linhas que já foram correspondidas durante um novo processo de correspondência.
* [**Mapa de Números de Item do Fornecedor**](purchase-order/supplier-item-number-map-admin-documentation.md): Uma configuração utilitária que mapeia números de itens do fornecedor para números de itens internos, garantindo precisão na gestão de inventário e ordens de compra.
