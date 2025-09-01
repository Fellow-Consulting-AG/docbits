# Calcular preço unitário do pedido de compra

## **Visão Geral**

Você pode optar por calcular automaticamente o **preço unitário** dividindo o **montante total** pela **quantidade**, e então multiplicando pelo valor de **preço unitário por**, em vez de extrair o preço unitário diretamente do documento. Isso é particularmente útil quando o preço unitário na ordem de compra (no Infor) difere do preço extraído do documento. Tais discrepâncias podem surgir se um desconto for aplicado ao preço unitário na ordem de compra do Infor, enquanto o documento aplica o desconto apenas ao montante líquido.

## **Passos de Ativação**

1.  Navegue até **Configurações** -> **Configurações globais** -> **Tipos de documentos**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/Calculate_PO_unit_price_1.png)
2.  Selecione o tipo de documento desejado e clique em **Mais configurações**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/Calculate_PO_unit_price_2.png)
3.  Na seção **Ordem de compra**, ative a opção **Calcular preço unitário do pedido de compra**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/Calculate_PO_unit_price_3.png)

## Exemplo:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/Calculate_PO_unit_price_4.png)

Neste caso, o preço unitário (sem o desconto) é extraído do documento, enquanto a ordem de compra no Infor armazena o preço unitário com o desconto aplicado. Isso resulta em uma discrepância no preço unitário.

Uma vez que a configuração esteja ativada, o preço unitário será recalculado da seguinte forma:\
&#xNAN;**`Preço unitário = Montante total ÷ Quantidade * Preço unitário por`**\
Isso garante que o preço unitário seja consistente e corresponda ao valor pretendido.
