# Classificação e Extração

## Visão geral

Nas configurações de **Classificação e Extração**, você pode:

* Ativar a **Divisão de documentos** baseada em QR codes
* Configurar a **Formatação de Quantidade**
* Configurar a **Extração de tabela**
* Alternar o processamento de arquivos **ZUGFeRD** não suportados
* Definir regras de classificação especiais
* Monitorar **Modelos de IA** treinados sob medida usados no processo de classificação

Esta página fornece uma explicação detalhada de todas as configurações disponíveis.

## **Acessando as Configurações de Classificação e Extração**

Para acessar as configurações de **Classificação e Extração**, vá para:\
**Configurações → Processamento de documentos → Classificação e Extração**

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_classification_and_extraction.png)

## Divisão de documentos

Na seção **Divisão de documentos**, você pode configurar se um documento enviado deve ser dividido em vários documentos sempre que um **código de barras** aparecer em uma de suas páginas.

Para ativar este recurso:

1. Vá para a seção **Divisão de documentos**.
2.  Abra o menu suspenso.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_14.png)
3.  Selecione **Dividido por código de barras/QR-Code**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_15.png)

Você terá então a opção de:

* Selecionar um ou mais tipos de código de barras a serem detectados.
*   Especificar um padrão regex que o código de barras deve corresponder para acionar a divisão de documentos.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_16.png)

## Formatação de Quantidade

Na seção **Formatação de Quantidade**, você tem duas opções:

* **Permitir arredondamento durante comparação de valores:**\
  Se ativado, é permitida uma tolerância de ±0,5 durante a comparação de valores.\
  Se desativado, aplica-se uma tolerância padrão de ±0,05.
* **Exigir correspondência exata para comparação de valores:**\
  Se ativado, os valores devem corresponder exatamente com tolerância zero.\
  Se desativado, é permitida uma tolerância de ±0,05.

<mark style="color:red;">**Nota**</mark>: Apenas uma dessas configurações pode estar ativa por vez.

## Extração de tabela

Você pode extrair tabelas de documentos ativando **Extração de tabela** ou **Extração de tabela de IA**. Uma tabela treinada—seja baseada em IA ou manual—sempre será vinculada a um fornecedor específico.

**Extração de tabela:** Ativa a **extração de tabela** manual. As tabelas devem ser treinadas manualmente.\
Saiba mais sobre o treinamento manual [aqui](../../../setup/document-training/training-line-fields-table-training/defining-tables-and-columns.md).

**Extração de tabela de IA:** Usa IA para extrair tabelas automaticamente. Se os resultados não forem suficientemente precisos, recomenda-se alternar para a **Extração de tabela** manual para melhor controle e treinamento.

**Extração de tabela para elemento de custeio:** Quando ativado, o DocBits pode extrair elementos de custeio das tabelas no nível de linha e classificá-los adequadamente.\
Explicação detalhada disponível [aqui](table-extraction-for-costing-element.md).

**Extração automática do código tributário:** Quando ativado, o sistema preenche automaticamente o campo **Código tributário** na Tela de Validação—desde que um campo de código tributário esteja configurado.\
Mais informações sobre esta configuração [aqui](auto-extract-tax-code.md).

**Modelo de IA:** Permite especificar qual **modelo de IA** é usado para a extração de tabelas.\
Você também verá uma tabela mostrando:

* Quais **Fornecedores** estão usando qual modelo de IA
* Se usam E-Text
* Opções para excluir uma entrada ou redefinir os dados de treinamento

Esta configuração é explicada em detalhes [aqui](ai-model.md).

## Documento eletrônico

**Processo não suportado ZUGFeRD PDF:** Se ativado, versões **ZUGFeRD** não suportadas serão processadas como PDFs padrão, e o XML incorporado será ignorado.

A lista de versões **ZUGFeRD** suportadas pode ser encontrada [aqui](../../global-settings/document-types/edi/zugferd-1.0-2.1-and-2.3.md).

## **Regras de Classificação**

Na seção **Regras de Classificação**, você pode definir **padrões regex** e critérios específicos para ajudar o sistema a classificar documentos automaticamente durante o processamento.

Para acessar esta seção, clique na guia **Regras de Classificação** na parte superior da página.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_1.png)

### **Adicionar uma nova regra de classificação**

Para criar uma nova regra:

1.  Clique em **Adicionar** no canto superior direito.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_2.png)
2. Preencha os seguintes campos:
   * **Padrão**: O padrão regex que o sistema deve procurar para acionar a classificação.
   * **Tipo**: Onde o padrão deve ser procurado (por exemplo, **Código de barras**).
   * **Suborganização** _(opcional)_: Especifique a suborganização à qual a regra se aplica.
   * **Tipo de documento**: Defina o tipo de documento a ser atribuído quando o padrão for correspondido.
   *   **Tipo de subdocumento** _(opcional)_: Especifique um subtipo para uma classificação mais detalhada.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_3.png)
3.  Clique em **Salvar** para salvar sua regra de classificação.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_4.png)

### **Editar uma regra de classificação**

Para editar uma regra existente:

1.  Clique nos três pontos na coluna **Ações**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_5.png)
2.  Selecione **Editar**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_6.png)
3. Faça as alterações desejadas.
4.  Clique em **Salvar** para aplicar as atualizações.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_4.png)

### **Excluir uma regra de classificação**

Para excluir uma regra:

1.  Clique nos três pontos na coluna **Ações**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_5.png)
2.  Selecione **Excluir**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_7.png)

## Modelos de IA

A seção **Modelos de IA** exibe todos os modelos personalizados treinados que foram especificamente ajustados para suas necessidades.

### Acessando a seção Modelos de IA

Para abrir esta seção, clique na guia **Modelos de IA** localizada na parte superior da página.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_8.png)

### Categorias de modelos

Os modelos são organizados em categorias. Abaixo do nome de cada categoria, é exibido o número de modelos que ela contém.\
Clique em uma categoria para ver seus detalhes.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_9.png)

Na parte superior da página da categoria selecionada, você verá informações-chave sobre cada modelo:

* **Tipo**: O tipo de modelo.
* **Somente a primeira página**: Indica se o modelo processa apenas a primeira página de um documento.
* **Versão**: O número da versão do modelo.

### Tabela de modelos

Todos os modelos dentro de uma categoria são listados em uma tabela, que inclui as seguintes informações:

* **Nome**: O nome do modelo.
* **Próximo modelo**: O modelo que continuará processando a saída do modelo atual.
* **Tipo de documento**: O tipo de documento principal atribuído pelo modelo durante a classificação.
* **Subtipos de documentos**: Os subtipos nos quais o documento é ainda mais classificado.
* **Prioridade**: O nível de prioridade que determina a posição do modelo na fila de classificação.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_11.png)

### Editando um modelo

Para editar um modelo:

1.  Clique no ícone de lápis na coluna **Ações** ao lado do modelo que deseja editar.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_10.png)
2. Atualize os campos disponíveis:
   * **Próximo modelo**: Selecione o modelo que deve processar a saída do modelo atual.
   * **Tipo de documento**: Escolha o tipo de documento que o modelo deve classificar a entrada.
3.  Clique em **Salvar** para aplicar suas alterações.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_12.png)
