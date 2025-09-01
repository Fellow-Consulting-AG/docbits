# Calcolo del prezzo unitario dell'OP

## **Panoramica**

Puoi scegliere di calcolare automaticamente il **prezzo unitario** dividendo l'**importo totale** per la **quantità**, e poi moltiplicandolo per il valore di **prezzo unitario per**, invece di estrarre il prezzo unitario direttamente dal documento. Questo è particolarmente utile quando il prezzo unitario nell'ordine di acquisto (in Infor) differisce dal prezzo estratto dal documento. Tali discrepanze possono sorgere se uno sconto viene applicato al prezzo unitario nell'ordine di acquisto Infor, mentre il documento applica lo sconto solo all'importo netto.

## **Passaggi di attivazione**

1.  Naviga su **Impostazioni** -> **Impostazioni globali** -> **Tipi di documenti**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/Calculate_PO_unit_price_1.png)
2.  Seleziona il tipo di documento desiderato e fai clic su **Altre impostazioni**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/Calculate_PO_unit_price_2.png)
3.  Nella sezione **Ordine di acquisto**, abilita l'opzione **Calcolo del prezzo unitario dell'OP**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/Calculate_PO_unit_price_3.png)

## Esempio:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/Calculate_PO_unit_price_4.png)

In questo caso, il prezzo unitario (senza sconto) è estratto dal documento, mentre l'ordine di acquisto in Infor memorizza il prezzo unitario con lo sconto applicato. Questo porta a una discrepanza nel prezzo unitario.

Una volta attivata l'impostazione, il prezzo unitario verrà ricalcolato come segue:\
&#xNAN;**`Prezzo unitario = Importo totale ÷ Quantità * Prezzo unitario per`**\
Questo assicura che il prezzo unitario sia coerente e corrisponda al valore previsto.
