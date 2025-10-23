# M3

## Importando um Template de Conexão de API no Infor M3

Este guia explica como importar um Template de Conexão de API para configurar rapidamente definições-chave para integração com o Infor M3. Usar um template permite estabelecer uma configuração de conexão predefinida, simplificando o processo e garantindo consistência.

<mark style="color:red;">**Observação**</mark>: Para configuração detalhada de áreas específicas como Auto Accounting, Integração de Fornecedores, Pedidos de Compra ou Extração de Tabela para elementos de custo, consulte a documentação correspondente:

* [Contabilidade Automática](auto-accounting.md)
* [Fornecedores e Pedidos de Compra](suppliers-and-purchase-orders.md)
* [Como importar todos os fornecedores](how-to-import-all-suppliers.md)
* [Extração de Tabela para elemento de custo](table-extraction-for-costing-element.md)

### **Baixar o Template**

Antes de importar, baixe o template de conexão necessário usando o arquivo abaixo:

{% file src="../../../.gitbook/assets/DocBits-Dev-Import-Template.xml" %}

### Importando Template

#### Etapas para importar um Template de Conexão

1. **Acesse o Infor ION Desk:**
   *   Navegue até **InforOS** → **ION Desk** → **Connect** → **Connection Points**.

       ![](https://lh7-us.googleusercontent.com/ySRjNzMXFzwSOYKx9hnlKLPHPuXpmfTvRADBfV6cpT8ajiEUbS4oXpd9InhXG09mHLakhqBTJMH4yQJNG5z9RXmbAjh8YbuGhxnXSeooIH_r3RAGOvJE6Ok67ST_272zFfhB_TTFYg3b-NwFq0CAv2o)
2. **Importar o Template:**
   *   Clique no botão **Import**.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/m3_import_2.png)
   * Selecione o **Template File** apropriado do seu sistema local.
   *   Clique em **OK** para iniciar o processo de importação.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/m3_import_3.png)
3. **Confirmação:**
   *   Se a importação for bem-sucedida, uma mensagem de confirmação será exibida.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/m3_import_4.png)
4. **Configuração pós-importação:**
   * Após importar o template, você pode personalizar configurações específicas da conexão conforme necessário.
   * Não se esqueça de importar ou configurar sua **Service Account** para autenticação e controle de acesso.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/m3_import_5.png)
