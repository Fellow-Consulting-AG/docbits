# Modelo de IA

## Visão Geral

A configuração do Modelo de IA permite que você defina qual modelo de IA deve ser usado por padrão para **Extração de tabela de IA** durante o **Processamento de documentos**. Você também pode visualizar o custo em tokens para cada modelo e ver qual modelo está atualmente atribuído a cada fornecedor.

## Como Acessar

1.  Navegue até **Configurações** → **Processamento de documentos** → **Classificação e Extração**

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_classification_and_extraction.png)
2.  Role para baixo até a seção **Extração de tabela**

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_1.png)

## Opções de Modelo de IA

Você pode escolher entre os seguintes modelos de IA. Passe o mouse sobre o ícone de informação na interface para ver o custo em tokens por documento para o modelo de IA selecionado:

* **Full** – 2 tokens por documento
* **Fast** – 1 token por documento
* **Turbo** – 1 token por documento

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_2.png)

## Tabela de Atribuição de Modelo de IA

A tabela exibe as configurações do modelo de IA para cada fornecedor, incluindo as seguintes informações:

* **ID do fornecedor** – O identificador único do fornecedor
* **Modelo de IA** – O modelo de IA atualmente atribuído ao fornecedor
* **E-Text** Indica se o recurso E-Text está habilitado
* **Ação** – Contém a opção de excluir a entrada

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_3.png)

### Excluir Entrada

Para redefinir a configuração do modelo de IA de um fornecedor para o padrão:

1.  Clique no ícone da lixeira na coluna **Ações** ao lado da entrada do fornecedor.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_4.png)
2.  Um diálogo de confirmação aparecerá—confirme que você deseja excluir a entrada.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_5.png)
3. Uma vez excluído, o fornecedor voltará a usar o modelo de IA padrão se a **Extração de tabela de IA** estiver em uso.
