# Configurações de OCR

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 11.01.00.png" alt=""><figcaption></figcaption></figure>

1. **Qualidade do OCR**:
   * Esta configuração permite definir a porcentagem mínima de qualidade do OCR necessária para que um documento seja processado automaticamente. Inclui um controle deslizante que você pode ajustar para definir o limite, como 75%, abaixo do qual o sistema não pode garantir uma extração bem-sucedida. Se a qualidade do OCR de um documento cair abaixo desse limite, você pode optar por fazer com que o sistema tome ações específicas, como executar novamente o OCR após confirmação manual.
   
2. **Configurações gerais de OCR**:
   * **Usar E-Text se disponível**: Esta opção, quando ativada, permite que o sistema utilize texto eletrônico incorporado em PDFs ou outros tipos de documentos para melhorar a precisão.
   * **Usar DESKEW se disponível**: Esta funcionalidade corrige o alinhamento do documento, o que ajuda a melhorar a precisão do OCR endireitando digitalizações inclinadas.
   
3. **Configurações de OCR para tabelas**:
   * **Usar dados de IA para tabelas se disponível**: Esta configuração permite o uso de tecnologias de IA para reconhecer e extrair melhor tabelas de documentos digitalizados, aproveitando modelos de aprendizado de máquina para identificar e estruturar dados tabulares com precisão.
   
4. **Configurações de OCR para os campos de cabeçalho**:
   * **Usar Extração de Regras**: Quando ativada, esta configuração permite que o sistema aplique regras predefinidas para extrair dados dos campos de cabeçalho, o que pode ser crítico para identificar corretamente seções de documentos como números de fatura, datas, etc.
   * **Usar Extração de IA**: Esta opção utiliza modelos de IA para extrair inteligentemente campos de cabeçalho, o que pode ser mais adaptável a variações em layouts e estilos de documentos.
