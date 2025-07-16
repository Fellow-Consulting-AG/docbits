# Lista de Valores

## Visão Geral

O recurso **Lista de Valores** permite que você crie e gerencie conjuntos de valores predefinidos. Isso é particularmente útil para configurar menus suspensos na seção [**Campos**](../global-settings/document-types/fields/), que podem ser usados posteriormente na **Validação de Campos**.

Essas listas podem ser personalizadas para diferentes sub-organizações e suportam múltiplas linguagens, proporcionando flexibilidade em **DocBits**.

## Como Acessar?

Você pode acessar a **Lista de Valores** navegando até **Configurações → Processamento de documentos → Lista de Valores**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_list_of_values.png)

## Como Adicionar ou Excluir uma Lista

### Criar uma Nova Lista de Valores

1.  Clique em **Novo** no canto superior direito da tela.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_1.png)
2. Digite um **Nome** para sua lista.
3. _(Opcional)_ Selecione uma **Sub-Organização** para a qual a lista deve estar ativa.
4.  Clique em **Salvar** para criar a lista.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_2.png)

### Como Excluir uma Lista

Para excluir uma lista, clique no ícone da lixeira ao lado da lista correspondente.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_13.png)

<mark style="color:red;">**Nota**</mark>: A lista será excluída imediatamente. Listas marcadas com a tag [**Padrão**](list-of-values.md#listas-e-linhas-definidas-pelo-sistema) não podem ser excluídas.

## Como Adicionar, Editar ou Remover Valores de uma Lista Existente

Você pode gerenciar valores em uma **Lista de Valores** existente usando um dos seguintes métodos:

* [**Adicionar valores manualmente**](list-of-values.md#adicionar-valores-manualmente) – Insira valores individualmente através da interface.
* [**Importar valores de um arquivo CSV**](list-of-values.md#importar-valores-de-um-arquivo-csv) – Carregue um arquivo CSV para adicionar múltiplos valores de uma vez.

### Adicionar Valores Manualmente

1.  Clique na lista que você deseja modificar.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_3.png)
2.  Clique em **Ações**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_4.png)
3.  Clique em **Adicionar linha**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_5.png)

Agora você pode especificar múltiplas propriedades para cada entrada:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_6.png)

**Valor**: Esta é a forma como o item será armazenado internamente dentro do **DocBits**. Permanece o mesmo em todas as linguagens e também serve como o texto de exibição padrão durante a validação de campo, se nenhum rótulo for especificado para a linguagem selecionada.

**Rótulo**: Este é o texto exibido na tela de validação, com base na linguagem selecionada. Se nenhum rótulo estiver disponível para a linguagem ativa no DocBits, o sistema irá exibir o **Valor** por padrão.

**Linguagem**: Especifica a linguagem na qual o rótulo será exibido.\
Uma explicação mais detalhada pode ser encontrada [aqui](list-of-values.md#adicionar-traducoes-aos-seus-valores).

**Sub-Organizações**: Especifica para qual **sub-organização** a linha deve estar ativa. Se deixado em branco, a linha estará disponível para todas as organizações.

**Sinônimos**: Aqui você pode especificar valores adicionais que ajudam a treinar seu documento.\
Por exemplo, se **EUR** é seu **valor** principal, você pode adicionar EURO e € como **sinônimos**. Quando o documento é treinado usando qualquer um desses **sinônimos**, o **DocBits** reconhecerá automaticamente e selecionará EUR como o valor correspondente da sua lista. <mark style="color:red;">**Nota**</mark>: Cada sinônimo deve ser confirmado pressionando **Enter** para adicioná-lo à lista.

4.  Após inserir todas as propriedades desejadas, clique no botão **Salvar** para adicionar a linha.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_11.png)

### Importar Valores de um Arquivo CSV

Para adicionar múltiplos valores de uma vez via importação CSV:

1.  Clique na lista que você deseja atualizar.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_3.png)
2.  Clique em **Ações**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_4.png)
3.  Clique em **Carregar CSV**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_7.png)
4. Clique em **Arquivo** para navegar e selecionar o arquivo CSV que você deseja carregar.
5. Escolha o **Delimitador** apropriado usado no arquivo CSV (`;` ou `,`).
6.  Clique em **Carregar** para importar os valores.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_8.png)

### Editar Valores Existentes

1. Localize a linha que você deseja editar.
2. Clique nos três pontos na coluna **Ações**.
3.  Selecione **Editar** no menu suspenso.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_10.png)
4. Faça as alterações necessárias.
5.  Clique em **Salvar** para aplicar suas alterações.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_11.png)

### Excluir Valores

1. Localize a linha que você deseja excluir.
2. Clique nos três pontos na coluna **Ações**.
3.  Selecione **Excluir** no menu suspenso.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_12.png)

<mark style="color:red;">**Nota**</mark>: A linha será excluída imediatamente. Linhas marcadas com a tag [**Padrão**](list-of-values.md#listas-e-linhas-definidas-pelo-sistema) não podem ser excluídas.

## Adicionar Traduções aos Seus Valores

Você pode adicionar quantas traduções forem necessárias para as linguagens suportadas no **DocBits**.

Para adicionar uma tradução:

1.  Clique no ícone de mais (+).

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_14.png)
2.  Selecione uma linguagem no menu suspenso.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_15.png)
3.  Digite a tradução desejada no campo **Rótulo**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_16.png)
4.  Para adicionar outra tradução, clique no ícone de mais (+) novamente.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_17.png)
5.  Para remover uma tradução, clique no ícone da lixeira.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_18.png)
6.  Quando terminar, clique no botão **Salvar** para salvar suas traduções.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_19.png)

<mark style="color:red;">**Nota**</mark>: Se nenhum **Rótulo** estiver disponível para a linguagem ativa, o DocBits exibirá o **Valor** por padrão.

## Listas e Linhas Definidas pelo Sistema

Algumas listas são pré-criadas pelo sistema e são marcadas com a tag **Padrão**. Essas listas não podem ser excluídas, mas você pode adicionar novas linhas a elas e remover essas linhas recém-adicionadas, se necessário.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_9.png)

Dentro dessas listas padrão, certas linhas são marcadas com a tag **Padrão**—essas são entradas definidas pelo sistema. Você pode adicionar novos **rótulos** em diferentes linguagens, mas essas linhas padrão não podem ser excluídas.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_20.png)
