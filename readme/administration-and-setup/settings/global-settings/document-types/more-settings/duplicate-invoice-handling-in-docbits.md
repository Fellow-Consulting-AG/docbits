# Manejo de Facturas Duplicadas en DocBits

## Configuración para Habilitar el Manejo de Facturas Duplicadas

Vaya a _Ajustes → Tipos de Documentos → Factura → Más Ajustes_ como se muestra en la captura de pantalla a continuación

<figure><img src="../../../../../.gitbook/assets/duplicate_invoice handling.png" alt=""><figcaption></figcaption></figure>

El usuario tiene dos opciones para detectar facturas duplicadas:

1. **Detección de Documentos Duplicados**\
   Esta función verifica si hay documentos duplicados cargados en DocBits según los criterios seleccionados. Si los criterios seleccionados coinciden entre documentos, el sistema marcará el documento como duplicado.
2.  **Detección de Facturas Duplicadas**\
    Esta función requiere que las Facturas de Proveedores se sincronicen desde Infor a DocBits. Compara los números de factura en el panel de facturación de DocBits con los de Infor. Si el mismo número de factura se carga más de una vez, se marcará como duplicado.

    <mark style="color:red;">**NOTA**</mark><mark style="color:red;">:</mark> Usar la función de **Detección de Facturas Duplicadas** resultará en un cargo adicional de crédito.

Una vez que la configuración está activada, el usuario puede seleccionar los criterios para la detección de duplicados

## Facturas Duplicadas en el Panel

Una vez que la Detección de Duplicados esté habilitada en la configuración, el panel mostrará un ícono para cualquier factura identificada como duplicada según los criterios especificados. Hacer clic en este ícono abrirá los registros duplicados en una vista de pantalla dividida para una fácil comparación

<figure><img src="../../../../../.gitbook/assets/duplicate_invoice handling2 (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/duplicate_invoice handling2b.png" alt=""><figcaption></figcaption></figure>

Cuando el usuario abre el documento, se muestra una barra de advertencia para las facturas duplicadas como se muestra en la captura de pantalla

<figure><img src="../../../../../.gitbook/assets/duplicate_invoice handling3.png" alt=""><figcaption></figcaption></figure>
