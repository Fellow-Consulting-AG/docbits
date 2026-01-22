# ZUGFeRD 1.0, 2.1 e 2.3

{% embed url="https://youtu.be/AxrHNEmmXtg" %}
DocBits E-Invoice Tutorial: Process XRechnung / ZUGFeRD (Factur-X), Validate Data & Automate Workflows
{% endembed %}

## **Versões suportadas de ZUGFeRD**

As versões atualmente suportadas de ZUGFeRD são:

* **1.0**
* **2.1** (compatível com FACTUR-X 1.0.05)
* **2.3** (compatível com FACTUR-X 1.07.2)

#### Ativação e modificação do padrão

O padrão ZUGFeRD está sempre ativo por padrão, mas você pode fazer modificações se necessário.

### **Passos para modificar as Configurações do ZUGFeRD:**

1. Navegue até **Configurações → Configurações globais → Tipos de documentos → Fatura**.
2.  Clique em **E-Doc**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/zugferd_1.png)
3. Uma lista de todos os e-docs disponíveis aparecerá.
4.  Localize a versão do **ZUGFeRD** que deseja modificar.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/zugferd_2.png)

## **Extraction Transformation e configuração do caminho XML:**

Nas **Configurações de Extraction Transformation**, você pode definir o caminho para localizar informações específicas dentro do arquivo XML e salvá-las em uma nova estrutura, facilitando o acesso aos dados.\
<mark style="color:red;">**Nota**</mark>: Se você usar essa funcionalidade, deverá usar os novos caminhos XML criados, e não os caminhos XML originais, no **Preview** e no **Extraction Path**.

### **Passos para modificar o arquivo de Extraction Transformation:**

1. Abra o **Extraction Transformation**.
2. Crie um novo rascunho clicando no **ícone de lápis**.
3. Selecione o rascunho recém-criado.
4. Crie um novo campo ou modifique um existente.
5. Defina o caminho desejado para a extração de dados.
6. Clique em **Salvar**.

### Notas importantes:

* O **arquivo de Preview** é usado apenas para **FACTUR-X** e não para **ZUGFeRD**. ZUGFeRD usará o **PDF** original.

## Configuração de Preview PDF

A **Configuração de Preview PDF** é usada para gerar uma versão legível pelo usuário do documento. Você pode personalizá-la com HTML para atender às suas necessidades.

### **Passos para modificar o arquivo de Preview:**

1. Abra o **Preview**.
2. Crie um novo rascunho clicando no **ícone de lápis**.
3. Selecione o rascunho recém-criado.
4. Crie um novo campo ou modifique um existente.
5. Defina o caminho desejado para a extração de dados.
6. Clique em **Salvar**.

## Configuração de Extraction Paths

A **Configuração de Extraction Paths** é usada para extrair dados e preencher campos na **tela de validação**, como a tabela de fatura ou os campos configurados no layout da fatura.

### **Passos para modificar** **Extraction Paths**:

1. Abra o **Extraction Paths**.
2. Crie um novo rascunho clicando no **ícone de lápis**.
3. Selecione o rascunho recém-criado.
4. Crie um novo campo ou modifique um existente.
5.  O lado esquerdo representa o **ID do campo do DocBits**, que pode ser encontrado em **Configurações → Configurações globais → Tipos de documentos → Fatura → Campos**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/zugferd_3.png)

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/zugferd_4.png)
6. O lado direito representa o **caminho para o campo** criado no Extraction Transformation.
7. Clique em **Salvar**.

Seguindo essas etapas, você garante a extração e a validação precisas de dados para faturas ZUGFeRD.
