# Resolução de Problemas de Extração de Tabelas

{% embed url="https://youtu.be/5XqEP-5fq6M" %}
DocBits OCR & E-Text Explained: OCR View, Debug Mode, Quality Settings, Deskew & Header Extraction
{% endembed %}

## **Passo 1: Abrir Visualização OCR para Resultados de Extração Ruins**

Se os resultados do treinamento de extração de tabelas não estiverem bons:

1. Abra a **Visualização OCR** clicando no ícone de lupa com **OCR** escrito nele.
2. Revise os resultados da extração e veja se o processo OCR pode melhorar a captura de dados.
3. Se os resultados ainda parecerem ruins, tente um documento diferente para verificar se o problema é específico do documento.
4. Se o problema for específico do documento, use outro documento para extração.
   * Se o problema persistir, siga para os próximos passos.

## **Passo 2: Verificar Disponibilidade de E-Text**

1. Verifique se o documento possui **e-text** disponível.
   * Você pode verificar isso usando uma ferramenta como o **Adobe Acrobat**.
   * Se o documento contiver e-text, siga para o **Passo 3**.
   * Se o documento não contiver e-text, siga para o **Passo 4**.

## **Passo 3: Ativar Extração de E-Text**

Se o documento contiver e-text, você tem duas opções:

1. **Ativar extração de e-text apenas para este fornecedor**:
   * Volte para a **Validação de Campos de Documentos**.
   * Clique no quadrado com os três pontos na barra de ferramentas do lado esquerdo.
   * Aqui, ative a opção **Usar E-text se disponível** para ativá-la apenas para este fornecedor.
2. **Ativar extração de e-text para todos os fornecedores**:
   * Vá para **Configurações** > **Processamento de Documentos** > **Configurações OCR**.
   * Nesta seção, você encontrará a opção **Usar E-text se disponível** e poderá ativá-la para todos os fornecedores.
3. Após ativar a extração de e-text, tente novamente o **treinamento de extração de tabelas**.
   * Se os resultados melhorarem, o problema estará resolvido.
   * Se os resultados ainda não estiverem bons, prossiga para o **Passo 4**.

## **Passo 4: Sem E-Text Disponível - Alterar Versão do OCR de IA**

Se o documento não tiver e-text disponível:

1. Vá para **Configurações** > **Processamento de Documentos** > **Configurações OCR**.
2. Altere a **Versão do OCR de IA** para uma versão diferente.
3. Volte para o **Treinamento de Extração de Tabelas** e tente novamente.
4. Se o resultado for melhor:
   * Verifique outros documentos de fornecedores diferentes para garantir que os resultados de extração para esses fornecedores não sejam afetados por essa alteração.
   * **Seja cauteloso, pois essa alteração pode afetar os resultados de extração de outros fornecedores.**
   * Essa alteração pode impactar outros fornecedores, então verifique minuciosamente os resultados para garantir que não afete negativamente as extrações de documentos de outros fornecedores.
5. Se o resultado não melhorar após alterar a versão do OCR de IA, entre em **contato conosco** para obter mais assistência.
