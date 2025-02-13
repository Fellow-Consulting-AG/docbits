# Document Types

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto%202024-05-08%20um%2008.44.19.png" alt=""><figcaption></figcaption></figure>

#### Visão Geral

A seção Tipos de Documentos lista todos os tipos de documentos reconhecidos e processados pelo DocBits. Os administradores podem gerenciar vários aspectos, como layout, definições de campos, regras de extração e muito mais para cada tipo de documento. Essa personalização é fundamental para garantir o manuseio preciso de dados e conformidade com os padrões organizacionais.

#### Recursos e Opções Principais

1. **Lista de Tipos de Documentos**:

* Cada linha representa um tipo de documento, como Fatura, Nota de Crédito, Nota de Entrega, etc.
* Os tipos de documentos podem ser padrão ou personalizados, conforme indicado por rótulos como "Padrão".

2. **Editar layout**: Esta opção permite aos administradores modificar as configurações de layout do documento, que incluem definir como o documento aparece e onde os campos de dados estão localizados.
3. **Subtipos de Documentos**: Se algum tipo de documento tiver subcategorias, esta opção permite que os administradores configurem configurações específicas para cada subtipo.
4. **Colunas da Tabela**: Personalize quais colunas de dados devem aparecer quando o tipo de documento é visualizado em listas ou relatórios.
5. **Campos**: Gerencie os campos de dados associados ao tipo de documento, incluindo adicionar novos campos ou modificar os existentes.
6. **Treinamento do Modelo**: Configure e treine o modelo usado para reconhecer e extrair dados dos documentos. Isso pode envolver a definição de parâmetros para modelos de aprendizado de máquina que melhoram com o tempo e mais dados.
7. **Regex**: Configure expressões regulares que são usadas para extrair dados dos documentos com base em padrões. Isso é particularmente útil para extração de dados estruturados.
8. **Scripts**: Escreva ou modifique scripts que executam regras de processamento personalizadas ou fluxos de trabalho para documentos deste tipo.
9. **EDI (Intercâmbio Eletrônico de Dados)**: Configure configurações relacionadas à troca de documentos em formatos eletrônicos padronizados.

{% hint style="info" %}
Veja [Configuração do Tipo de Documento](../../../../admin-section/setup/document-types/)
{% endhint %}

{% @jira/embed url="https://fellowpro.atlassian.net/browse/DOCB-2489" %}
