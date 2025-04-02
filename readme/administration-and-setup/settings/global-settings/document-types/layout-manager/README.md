# Layout Manager

<figure><img src="../../../../../.gitbook/assets/Bildschirmfoto%202024-05-08%20um%2008.46.24.png" alt=""><figcaption></figcaption></figure>

#### Visão Geral

O Gestor de Layout permite aos administradores configurar e modificar visualmente o layout dos tipos de documento, definindo propriedades para vários campos de dados e grupos dentro de um documento. Esta interface ajuda a garantir que os modelos de extração e os pontos de entrada de dados manuais estejam alinhados precisamente com a estrutura do documento digitalizado ou carregado no Docbits.

#### Componentes Principais

1. **Grupos e Campos**:

* **Grupos**: Unidades organizacionais dentro de um tipo de documento que categorizam campos relacionados (por exemplo, Detalhes da Fatura, Detalhes de Pagamento). Estes podem ser expandidos ou recolhidos e organizados para refletir o agrupamento lógico no documento real.
* **Campos**: Pontos de dados individuais dentro de cada grupo (por exemplo, Número da Fatura, Termos de Pagamento). Cada campo pode ser personalizado quanto à forma como os dados são capturados, exibidos e processados.

2. **Painel de Propriedades**:

* Este painel exibe as propriedades do campo ou grupo selecionado, permitindo uma configuração detalhada, como:
* **Rótulo**: O rótulo visível para o campo na interface do usuário.
* **Nome do Campo**: O identificador técnico usado dentro do sistema.
* **Largura do Elemento em Percentagem**: Determina a largura do campo em relação ao layout do documento.
* **Índice de Tabulação**: Controla a ordem de tabulação para navegação.
* **Executar Script na Alteração**: Se deve executar um script quando o valor do campo muda.
* **Exibir Rótulo à Esquerda**: Se o rótulo é exibido à esquerda do campo ou acima dele.
* **É Textarea**: Especifica se o campo deve ser uma área de texto, acomodando quantidades maiores de texto.
* **Selecionar Tipo de Modelo**: Opção para selecionar qual tipo de modelo lidará com a extração deste campo.
* **Comprimento do Campo**: Comprimento máximo dos dados a serem aceitos neste campo.
* **Palavras-Chave Proibidas**: Palavras-chave que não são permitidas dentro do campo.

3. **Pré-visualização do Modelo**:

* Mostra uma pré-visualização em tempo real de como o documento aparecerá com base na configuração de layout atual. Isso ajuda a garantir que o layout corresponda à estrutura real do documento e é vital para testar e refinar a configuração de processamento do documento.

{% @jira/embed url="https://fellowpro.atlassian.net/browse/DOCB-2490" %}
