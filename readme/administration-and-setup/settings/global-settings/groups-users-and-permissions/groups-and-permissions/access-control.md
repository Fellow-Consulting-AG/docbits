# Controle de Acesso

## Visão Geral

Este guia explica como os administradores podem definir configurações de controle de acesso para diferentes grupos de usuários no DocBits. Cada grupo pode ser configurado com permissões personalizadas no nível de documento e campo.

## Grupos de Controle de Acesso

O painel de controle de acesso permite que o administrador gerencie grupos de usuários e suas respectivas permissões. Cada grupo pode ter configurações específicas relacionadas a:

* **Acesso ao Documento**: Se o grupo pode acessar um tipo de documento.
* **Permissões em Nível de Campo**: Se o grupo pode ler, escrever ou visualizar certos campos dentro de um documento.
* **Permissões de Ação**: Quais ações o grupo pode realizar, como editar, excluir, atualizar em massa e aprovar documentos.

## Ativação

1. Navegue até **Configurações**.
2. Selecione **Processamento de Documentos**.
3. Selecione **Módulo.**
4. Ative o **Controle de Acesso** ativando o controle deslizante.

## **Acessando Configurações do Grupo**

1. Navegue até **Configurações**.
2. Vá para **Configurações Globais**.
3. Selecione **Grupos, Usuários e Permissões**.
4. Selecione **Grupos e Permissões**.
5. Para gerenciar permissões para um grupo, como PROCUREMENT\_DIRECTOR, clique nos três pontos no lado direito da tela.
6. Selecione **Visualizar Controle de Acesso**.

## Configurando Permissões para Grupos

1.  **Visão Geral do Controle de Acesso**:

    * Nesta seção, você pode habilitar ou desabilitar o acesso para todos os tipos de documentos, como **Fatura**, **Nota de Crédito**, **Pedido de Compra**, e mais.
    * Você pode definir níveis de acesso, como:
      * **Habilitado**: Concede acesso ao tipo de documento.
      * **Lista**: Define se o tipo de documento é visível na visualização de lista.
      * **Visualizar**: Especifica a visualização padrão para o documento.
      * **Editar**: Concede permissão para editar o documento.
      * **Excluir**: Permite que o grupo exclua documentos.
      * **Atualização em Massa**: Habilita a atualização em massa do tipo de documento.
      * **Níveis de Aprovação**: Define a capacidade do grupo de aprovar documentos (Aprovação de Primeiro e Segundo nível).
      * **Desbloquear Documento**: Define se o grupo pode desbloquear um documento para edições adicionais.

    Exemplos de configurações para **PROCUREMENT\_DIRECTOR**:

    * **Fatura**: Habilitado para todas as permissões, incluindo editar e excluir.
    * **Pedido de Compra**: Habilitado com permissões normais para todas as ações.
2. **Permissões em Nível de Campo**:
   * Dentro de cada tipo de documento, campos específicos podem ser configurados com diferentes níveis de permissões.
   * As permissões incluem:
     * **Ler/Escrever**: Os usuários podem ler e escrever no campo.
     * **Escrever do Proprietário**: Apenas o proprietário do documento ou campo pode escrever, outros podem ler.
     * **Apenas Leitura**: Os usuários podem apenas visualizar o campo, mas não modificá-lo.
     * **Leitura do Proprietário/ Escrita do Proprietário:** Apenas o proprietário do documento ou campo pode escrever e ler.
     * **Aprovação:** As alterações devem ser aprovadas por usuários autorizados ou administrador.
     * **Nenhuma**: Nenhuma permissão específica é aplicada ao campo.
