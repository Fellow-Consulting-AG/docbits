# Mais Configurações

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 09.54.48.png" alt=""><figcaption></figcaption></figure>

#### Visão Geral

A área de Mais Configurações permite aos administradores configurar vários aspectos do processamento de documentos que não são abordados nas configurações básicas. Isso inclui opções para extração de tabelas, revisão de documentos, geração de PDF, processos de aprovação e configurações específicas para operações como pedidos de compra ou contabilidade.

#### Recursos e Opções Principais

1. **Extração de Tabelas**:
* **Pular validação de tabela**: Permite ignorar o processo de validação de dados de tabela, o que pode ser útil em cenários onde a validação de dados precisa ser flexível.
2. **Em Revisão**:
* **Design no Formulário de Revisão**: Configura o layout e os campos que aparecem nos formulários de revisão usados durante o processo de revisão de documentos.
3. **Geração de PDF**:
* **Modelo de Design**: Especifica o modelo usado para gerar versões em PDF dos documentos, o que pode ser crucial para arquivamento ou comunicação externa.
4. **Aprovação**:
* **Aprovar antes da exportação**: Garante que os documentos devem ser aprovados antes de poderem ser exportados do sistema.
* **Segunda Aprovação**: Adiciona uma camada adicional de aprovação para validação adicional, aprimorando o controle sobre o processamento de documentos.
5. **Pedido de Compra / Contabilidade Automática**:
* **Tabela de PO no construtor de layout**: Permite a inclusão de tabelas de pedidos de compra no construtor de layout para layouts de documentos personalizados.
* **Pedido de Compra**: Ativa o processamento de documentos de pedido de compra dentro do sistema.
* **Configuração de Tolerância de PO**: Define níveis de tolerância para quantidades de pedidos de compra, o que ajuda a acomodar pequenas discrepâncias sem sinalizá-las como erros.
6. **Exportação Alternativa de Documentos**:
* **Desativar status de PO**: Permite desativar certos status para pedidos de compra durante o processo de exportação, fornecendo flexibilidade na forma como os pedidos são tratados.
7. **Mapeamento de Número de Item do Fornecedor**:
* Uma configuração de utilitário que mapeia números de item do fornecedor para números de item internos, garantindo precisão no gerenciamento de inventário e pedidos de compra.

{% @jira/embed url="https://fellowpro.atlassian.net/browse/DOCB-2500" %}
