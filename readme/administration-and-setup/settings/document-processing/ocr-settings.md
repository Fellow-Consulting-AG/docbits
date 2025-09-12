# Configurações de OCR

## Visão Geral

Nas **Configurações de OCR (Reconhecimento Óptico de Caracteres)**, você pode configurar como o OCR é aplicado durante o processamento de documentos. Isso inclui especificar a qualidade mínima necessária, escolher se deve usar texto incorporado (e-text), selecionar a versão do OCR e mais. Esta página fornece uma explicação detalhada de todas as configurações disponíveis.

## Como Acessar as Configurações de OCR

Para acessar as configurações de OCR:

*   Navegue até: **Configurações** → **Processamento de documentos** → **Configurações de OCR**

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_ocr.png)

## Qualidade OCR

Nesta seção, você pode definir a qualidade mínima do documento necessária para o processamento de OCR ajustando o controle deslizante de qualidade. Mova o controle deslizante para a esquerda ou para a direita para diminuir ou aumentar o limite de qualidade, respectivamente.

Se um documento não atender ao nível de qualidade definido, DocBits fornece três opções para lidar com isso:

* **Corra de qualquer maneira**\
  O documento será processado independentemente de sua qualidade.
* **Executar novamente após confirmação**\
  **DocBits** fará uma pausa e solicitará que você confirme se deseja prosseguir com o processamento.
* **Erro de lançamento**\
  O processamento do documento será interrompido completamente, e uma mensagem de erro será exibida, indicando que o documento não atendeu ao limite de qualidade necessário.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ocr_settings_1.png)

## Configurações Gerais de OCR

* **Use E-Text se Disponível**\
  Quando ativado, **DocBits** usará texto eletrônico incorporado (por exemplo, de PDFs) em vez de realizar OCR. Isso melhora tanto a velocidade quanto a precisão, pois o texto é extraído diretamente sem exigir processamento de OCR.
* **Use DESKEW se Disponível**\
  Esta opção corrige automaticamente o alinhamento de documentos digitalizados. Endireitar imagens inclinadas ajuda a melhorar a precisão do OCR.
*   **Versão OCR de IA**\
    Permite que você selecione uma versão específica do mecanismo de OCR baseado em IA.\
    Isso pode ser útil se:

    * Você não está alcançando os resultados desejados com a versão atualmente selecionada.
    * Você está solucionando problemas relacionados ao desempenho ou precisão do OCR.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ocr_settings_2.png)

## Configurações de OCR para Tabelas

* **Use dados de IA para tabelas, se disponíveis**\
  Quando ativado, DocBits usará dados de OCR para tabelas em vez de texto eletrônico incorporado (E-Text) — mesmo que a configuração **Use E-Text se disponível** esteja ativada.

## Configurações de OCR para Campos de Cabeçalho

* **Extração de regras de uso**\
  DocBits aplicará suas regras de extração predefinidas para identificar campos de cabeçalho.
* **Use extração de IA**\
  DocBits usará IA para detectar e extrair automaticamente campos de cabeçalho.

**Ordem de Execução:**\
Se ambas as opções estiverem ativadas, **DocBits** realizará a extração na seguinte ordem:\
**Extração de regras → Extração de IA**\
\
<mark style="color:red;">**Nota**</mark>: Para melhores resultados e comportamento consistente, ative ambas as opções. Isso permite que **DocBits** use métodos baseados em regras e baseados em IA em combinação durante a extração de cabeçalhos.
