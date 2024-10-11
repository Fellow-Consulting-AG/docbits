# Árvores de Decisão

### Visão Geral

As Árvores de Decisão são um recurso poderoso que permite o roteamento automatizado e o processo de tomada de decisão com base em regras predefinidas. Este recurso é especialmente útil em ambientes complexos onde várias condições precisam ser avaliadas para determinar o curso de ação correto, como atribuição de preços, determinação de quantidades ou roteamento de documentos.

#### Componentes Principais

* **Lista de Árvores de Decisão**: Esta é a interface principal onde todas as árvores de decisão existentes são listadas. Cada árvore de decisão pode estar associada a um tipo de documento específico, como uma `FATURA` ou `COTAÇÃO`.
* **Editor de Árvores de Decisão**: Esta interface permite a criação e edição de árvores de decisão, onde você pode definir regras, operadores e ações a serem tomadas quando certas condições forem atendidas.

### Interface da Árvore de Decisão

#### Lista de Árvores de Decisão

A lista de Árvores de Decisão exibe todas as árvores de decisão disponíveis. Cada entrada mostra:

* **Nome**: O nome da árvore de decisão.
* **Tipo de Documento**: O tipo de documento associado à árvore de decisão (por exemplo, `FATURA`, `COTAÇÃO`).

#### Editor de Árvores de Decisão

O Editor de Árvores de Decisão permite que você configure regras que governam como as decisões são tomadas.

**Componentes do Editor de Árvores de Decisão**

* **Regras**: Cada regra consiste em condições e ações.
* **Selecionar Fonte**: Este dropdown permite que você especifique o campo de origem a ser avaliado.
* **Selecionar Operador**: Define o operador lógico (por exemplo, `<=`, `>=`, `=`, `!=`) a ser aplicado ao campo de origem.
* **Resultado**: Define o resultado ou ação que deve ser tomada quando as condições forem atendidas.
* **Adicionar Nova Linha**: Permite que você adicione regras adicionais à árvore de decisão.

#### Exemplo de Configuração de uma Árvore de Decisão

1. **Regra 1**:
   * **Fonte**: Quantidade
   * **Operador**: `<=`
   * **Valor**: `250000`
   * **Resultado**: Atribuir a `CATMGR_CMM`
2. **Regra 2**:
   * **Fonte**: Preço
   * **Operador**: `>`
   * **Valor**: `500000`
   * **Resultado**: Atribuir a `PROCUREMENT_DIRECTOR`

Cada regra é avaliada sequencialmente, e a ação correspondente é executada se as condições forem satisfeitas.

### Política de Árvores de Decisão

A Política de Árvores de Decisão define como várias regras dentro de uma árvore de decisão são processadas. Você pode escolher entre várias políticas:

* **Única**: Garante que apenas uma regra pode corresponder. Se mais de uma regra for correspondida, a árvore de decisão sinalizará um erro.
* **Primeira**: A primeira regra correspondente é aplicada, e nenhuma regra adicional é avaliada.
* **Prioridade**: As regras são avaliadas com base em sua ordem de prioridade. A regra correspondente de maior prioridade é aplicada.
* **Coletar (soma)**: Coleta todas as regras correspondentes e soma os resultados.
* **Coletar (mínimo/máximo/contagem)**: Coleta todas as regras correspondentes e seleciona o mínimo, máximo ou conta as ocorrências.
* **Ordem das Regras**: Aplica as regras na ordem em que aparecem na árvore de decisão.
* **Qualquer**: Qualquer regra correspondente pode ser aplicada, permitindo múltiplos resultados.

#### Exemplo de uma Política de Árvore de Decisão em Ação

Na árvore de decisão "Preço do Grupo Direto":

* **Política Selecionada**: `Primeira`
* Isso significa que assim que a condição de uma regra é atendida, sua ação associada é aplicada, e nenhuma regra adicional é avaliada.

### Exportar e Salvar

* **Salvar**: Salva a configuração atual da árvore de decisão.
* **Exportar**: Permite que você exporte a configuração da árvore de decisão, que pode ser importada em outro ambiente ou usada para fins de backup.