# Calcular preço unitário do PO

## **Visão Geral**

Você pode optar por calcular o preço unitário manualmente, dividindo o valor líquido pela quantidade, em vez de extraí-lo automaticamente do documento. Isso é particularmente útil quando o preço unitário na ordem de compra (no Infor) difere do preço extraído do documento. Essas discrepâncias podem surgir se um desconto for aplicado ao preço unitário na ordem de compra do Infor, enquanto o documento aplica o desconto apenas ao valor líquido.

## **Passos de Ativação**

1.  Navegue até **Configurações** -> **Configurações Globais** -> **Tipos de Documento**.

    <figure><img src="../../../../../.gitbook/assets/Calculate_PO_unit_price_1.png" alt=""><figcaption></figcaption></figure>
2.  Selecione o tipo de documento desejado e clique em **Mais Configurações**.

    <figure><img src="../../../../../.gitbook/assets/Calculate_PO_unit_price_2.png" alt=""><figcaption></figcaption></figure>
3.  Na seção **Ordem de Compra**, ative a opção **Calcular Preço Unitário do PO**.

    <figure><img src="../../../../../.gitbook/assets/Calculate_PO_unit_price_3.png" alt=""><figcaption></figcaption></figure>

## Exemplo:

<figure><img src="../../../../../.gitbook/assets/Calculate_PO_unit_price_4.png" alt="" width="563"><figcaption></figcaption></figure>

Neste caso, o preço unitário (sem o desconto) é extraído do documento, enquanto a ordem de compra no Infor armazena o preço unitário com o desconto aplicado. Isso resulta em uma discrepância no preço unitário.

Uma vez que a configuração esteja ativada, o preço unitário será recalculado da seguinte forma:\
**Preço Unitário = Valor Líquido ÷ Quantidade**\
Isso garante que o preço unitário seja consistente e corresponda ao valor pretendido.
