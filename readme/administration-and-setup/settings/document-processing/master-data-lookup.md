# Consulta de Dados Mestres

## Visão geral

A "Consulta de Dados Mestres" nas suas Configurações de Processamento de documentos permite uma abordagem abrangente e integrada para gerenciar e validar os dados dos seus documentos, sincronizando-os com o seu sistema Infor ERP. Veja como isso ajuda a simplificar a validação e o aprimoramento do Processamento de documentos no seu ambiente ERP:

1. **Gerenciamento centralizado de dados**: Este recurso funciona como um repositório central onde dados de várias fontes, como fornecedores, endereços de clientes, códigos fiscais e muito mais, podem ser armazenados e gerenciados. Ele fornece um ponto único de referência para todos os dados mestres, garantindo consistência e precisão em toda a sua organização.
2. **Validação em relação aos dados do ERP**: Ao sincronizar dados mestres, como informações de fornecedores, do Infor para o DocBits, você pode validar automaticamente os dados extraídos dos documentos em relação aos dados do seu ERP. Isso garante que as informações processadas (como nomes de fornecedores, endereços e códigos fiscais) correspondam aos dados mantidos no seu sistema ERP, minimizando erros e discrepâncias.
3. **Facilita a automação**: Ter um sistema robusto de consulta de dados mestres ajuda a automatizar o processamento de documentos recebidos. Por exemplo, ordens de compra ou faturas podem ser verificadas automaticamente quanto à correção dos dados do fornecedor, aprovadas se houver correspondência ou sinalizadas para revisão se forem encontradas discrepâncias.
4. **Aprimora a integridade dos dados**: Atualizações regulares do seu sistema ERP para a Consulta de Dados Mestres garantem que os dados usados no Processamento de documentos estejam atualizados. Isso reduz o risco de processar documentos com base em informações desatualizadas, aprimorando assim a integridade geral das transações comerciais.
5. **Eficiência no Processamento de documentos**: Com dados mestres vinculados diretamente e constantemente atualizados, o Processamento de documentos se torna mais eficiente. Os documentos podem ser classificados e encaminhados automaticamente com base nos critérios específicos definidos nos dados mestres, como condições específicas de fornecedores ou regulamentações fiscais aplicáveis a diferentes tipos de transações.

{% hint style="info" %}
Veja aqui como [Importar Dados Mestres](../../../infor-integration-and-configuration/importing-customer-master-data/)
{% endhint %}

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/master_data_lookup_1.png)

## **Acessando a Consulta de Dados Mestres**

Para acessar a seção **Consulta de Dados Mestres**, navegue até:\
**Configurações → Processamento de documentos → Consulta de Dados Mestres**

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_mater_data_lookup.png)

## **Configurações**

Para acessar as Configurações da **Consulta de Dados Mestres**, clique em **Configurações** localizado no canto inferior esquerdo da tela de **Consulta de Dados Mestres**.\
As seguintes opções de configuração estão disponíveis:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/master_data_lookup_2.png)

### **BOD do fornecedor**

* **Permitir sincronização de várias contas de fornecedores**:
  * **Ativado**:\
    Um único fornecedor pode ter vários elementos `<FinancialParty>` no BOD (Business Object Document), muitas vezes devido a múltiplos IBANs ou contas financeiras associadas. Quando esta configuração está ativada, todas as entradas `<FinancialParty>` do fornecedor serão extraídas e salvas na tabela de fornecedores, permitindo armazenar vários atributos financeiros.
  * **Desativado**:\
    Apenas o último elemento `<FinancialParty>` encontrado para o fornecedor no BOD será extraído. Quaisquer atributos financeiros anteriores (por exemplo, IBANs adicionais) serão ignorados, e somente os dados da última ocorrência serão salvos na tabela de fornecedores.

### **Exclusão de Ordem de Compra**

*   **Excluir pedido de compra após**: Especifique quando as Ordens de Compra fechadas devem ser excluídas. Após o período de tempo selecionado, os registros serão removidos automaticamente.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/master_data_lookup_3.png)
