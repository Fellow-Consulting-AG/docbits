# XRechnung

{% embed url="https://youtu.be/AxrHNEmmXtg" %}
DocBits E-Invoice Tutorial: Process XRechnung / ZUGFeRD (Factur-X), Validate Data & Automate Workflows
{% endembed %}

## Visão geral

No painel de administração da XRechnung, você encontrará os seguintes componentes principais:

## 1. Transformação

### Objetivo

O processo de Transformação é essencial para converter dados brutos, geralmente em formato XML, em um formato estruturado que atenda a requisitos específicos, como gerar uma fatura. Na XRechnung, isso é alcançado principalmente usando XSLT (Extensible Stylesheet Language Transformations). XSLT é uma linguagem projetada para transformar documentos XML em outros tipos de documentos, como outro XML, HTML ou texto simples.

### Como funciona

• Modelo XSLT: O arquivo XSLT define como os dados XML são processados e como deve ser a saída final. Ele aplica regras e modelos para extrair, manipular e produzir os dados do documento XML.

• Elementos e atributos: O arquivo XSLT contém elementos e atributos específicos que controlam o processo de transformação. Por exemplo, \<xsl:value-of> é usado para extrair o valor de um nó específico do documento XML.

### Capacidades do administrador

• Modificando o XSLT:

• Editar modelos existentes: Um administrador pode modificar os modelos XSLT existentes para alterar como os dados XML de entrada são transformados. Por exemplo, se houver necessidade de extrair informações adicionais do documento XML, um administrador poderá adicionar novas regras no arquivo XSLT.

• Criar novas versões: Se forem necessárias alterações, um administrador poderá criar uma nova versão do modelo XSLT. Isso garante que as versões anteriores permaneçam intactas para referência histórica ou reversão, se necessário.

### Exemplo:

Suponha que o modelo XSLT extraia o ID da fatura usando:

```xml
<xsl:value-of select="//INVOICE/INVOICE_ID/text()" />
```

Se um novo campo, como um número de referência do cliente, precisar ser extraído, um administrador poderá adicionar:

```xml
<xsl:value-of select="//INVOICE/CUSTOMER_REFERENCE_NUMBER/text()" />
```

## 2. Visualização

### Objetivo

A função de Visualização permite que os administradores vejam a saída gerada pela transformação XSLT antes de finalizá-la. Esta etapa é crucial para garantir que as regras de transformação funcionem corretamente e que a saída atenda aos padrões exigidos.

### Como funciona

• Validação em tempo real: O recurso de visualização fornece uma renderização em tempo real de como os dados transformados aparecerão quando aplicados a um documento real (como uma fatura). Isso ajuda a detectar erros ou problemas de formatação precocemente.

• Ajustes: Se a visualização mostrar discrepâncias ou erros, os ajustes podem ser feitos diretamente no arquivo de transformação (XSLT).

### Capacidades do administrador

• Personalizando a visualização:

• Modificar configurações de visualização: Um administrador pode ajustar quais partes da transformação são visualizadas. Por exemplo, eles podem se concentrar em seções específicas do documento ou testar novas regras adicionadas ao modelo XSLT.

• Salvar e iterar: Após fazer os ajustes, a visualização pode ser atualizada para ver as alterações. Esse processo iterativo permite o ajuste fino até que a saída desejada seja alcançada.

### Exemplo:

Se um administrador notar que o formato da data na visualização está incorreto (por exemplo, mostrando AAAA-MM-DD em vez de DD-MM-AAAA), ele poderá modificar o XSLT para formatar a data corretamente e ver imediatamente o resultado na visualização.

## 3. Caminhos de extração

### Objetivo

Os Caminhos de Extração definem os caminhos específicos dentro de uma estrutura XML ou JSON dos quais os dados devem ser extraídos. Esse processo é essencial para isolar informações importantes dentro do documento que serão usadas na transformação ou para outras tarefas de processamento.

### Como funciona

• XPath e JSONPath: Os caminhos de extração usam linguagens como XPath (para XML) ou JSONPath (para JSON) para especificar a localização dos dados dentro do documento. Esses caminhos são cruciais para informar ao sistema exatamente onde encontrar e como extrair as informações necessárias.

### Capacidades do administrador

• Definindo e modificando caminhos:

• Modificar caminhos existentes: Um administrador pode modificar os caminhos de extração se a estrutura de dados mudar ou se dados adicionais precisarem ser extraídos. Isso pode envolver a alteração das expressões XPath ou JSONPath.

• Adicionar novos caminhos: Para novos campos ou pontos de dados, um administrador pode definir novos caminhos de extração. Isso envolveria especificar o caminho correto no documento XML ou JSON.

### Exemplo:

Em um documento de fatura XML, se o caminho para o ID da fatura for definido como:

```json
"invoice_id": "//INVOICE/INVOICE_ID/text()"
```

E um novo campo, como um endereço de entrega, precisar ser adicionado, um administrador poderá adicionar:

```json
"shipping_address": "//INVOICE/SHIPPING/ADDRESS/text()"
```
