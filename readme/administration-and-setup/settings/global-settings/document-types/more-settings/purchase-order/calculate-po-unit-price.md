# Calcular el precio unitario del pedido

## **Descripción general**

Puedes optar por calcular el precio unitario manualmente dividiendo el importe neto por la cantidad, en lugar de extraerlo automáticamente del documento. Esto es particularmente útil cuando el precio unitario en la orden de compra (en Infor) difiere del precio extraído del documento. Tales discrepancias pueden surgir si se aplica un descuento al precio unitario en la orden de compra de Infor, mientras que el documento solo aplica el descuento al importe neto.

## **Pasos de activación**

1.  Navega a **Ajustes** -> **Ajustes globales** -> **Tipos de documentos**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/Calculate_PO_unit_price_1.png)
2.  Selecciona el tipo de documento deseado y haz clic en **Más ajustes**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/Calculate_PO_unit_price_2.png)
3.  En la sección **Orden de compra**, activa la opción **Calcular el precio unitario del pedido**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/Calculate_PO_unit_price_3.png)

## Ejemplo:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/Calculate_PO_unit_price_4.png)

En este caso, el precio unitario (sin el descuento) se extrae del documento, mientras que la orden de compra en Infor almacena el precio unitario con el descuento aplicado. Esto resulta en una discrepancia en el precio unitario.

Una vez que se activa la configuración, el precio unitario se recalculará de la siguiente manera:\
**Precio unitario = Importe neto ÷ Cantidad**\
Esto asegura que el precio unitario sea consistente y coincida con el valor previsto.
