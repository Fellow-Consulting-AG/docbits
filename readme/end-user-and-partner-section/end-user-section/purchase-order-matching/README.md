# Pantalla de Coincidencia de Órdenes de Compra

{% embed url="https://youtu.be/qR-lrSaj4Ug" %}
DocBits PO Matching Tutorial: Auto/Manual Line Matching, Tolerances & Mismatch Indicators
{% endembed %}

## Descripción general

En la pantalla de **Coincidencia de Órdenes de Compra**, puedes comparar los artículos de línea extraídos de tu documento con aquellos almacenados en el **sistema Infor**, utilizando el número de orden de compra como referencia.

## Descripción general

En la pantalla de **Coincidencia de Órdenes de Compra**, puedes comparar los artículos de línea extraídos de tu documento con aquellos almacenados en el **sistema Infor**, utilizando el número de orden de compra como referencia.

Puedes:

* **Identificar inmediatamente** cualquier diferencia entre los datos extraídos y los almacenados
* **Establecer tolerancias** para permitir desviaciones aceptables
* **Ignorar estados específicos** de Infor, si es necesario
* **Aprobar y exportar** el documento después de una coincidencia exitosa
* **Rechazar** el documento si los datos no cumplen con los criterios de validación requeridos

Esta página te guiará a través del proceso de coincidencia de órdenes de compra y explicará toda la funcionalidad relacionada disponible en esta sección.

## Herramientas en la Pantalla de Coincidencia de Órdenes de Compra

En la parte superior de la pantalla de Coincidencia de Órdenes de Compra, encontrarás varias herramientas, como **Guardar**, **Coincidencia Automática**, **Exportar**, y otras, que ayudan con el proceso de coincidencia.\
Una descripción detallada de cada herramienta y su funcionalidad se puede encontrar [aquí](purchase-order-matching-tools.md).

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FxPOM1IzmTGgCCAE4tAQg%252Fpo_match_tools_0.png%3Falt%3Dmedia%26token%3D420e0d50-d5c8-4b7b-8ec6-26ca9e2d7a68\&width=768\&dpr=4\&quality=100\&sign=5d32419c\&sv=2)

## Filtrar y Agregar Números de Órdenes de Compra

Puedes buscar números de órdenes de compra específicos ingresando el número en el campo de búsqueda.\
Para un filtrado más refinado, haz clic en el ícono en el lado derecho de la barra de búsqueda para seleccionar criterios específicos para tu búsqueda.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F3xeAcb5EwKQPg9rksZVE%252Fpo_match_3.png%3Falt%3Dmedia%26token%3Deef4e964-ffe5-485c-ae22-c5790a9302fc\&width=768\&dpr=4\&quality=100\&sign=b0830e56\&sv=2)

Las siguientes opciones de filtro están disponibles para ayudarte a refinar tu búsqueda de órdenes de compra:

* **Palabra clave** – Filtrar por números de órdenes de compra.
* **Proveedor** – Filtrar por nombre o ID del proveedor.
* **Después de la fecha** – Mostrar órdenes de compra creadas después de una fecha específica.
* **Antes de la fecha** – Mostrar órdenes de compra creadas antes de una fecha específica.
* **Cantidad mínima de pedido** – Filtrar por valor mínimo de pedido.
* **Cantidad máxima de pedido** – Filtrar por valor máximo de pedido.
* **Ordenar por** – Seleccionar el atributo para ordenar los resultados (por ejemplo, fecha, monto).
* **Dirección de clasificación** – Elegir el orden de clasificación: ascendente o descendente.
* **Número de registros** – Definir cuántos resultados deben mostrarse por página.
* **Más** – Opciones de filtrado adicionales incluyen:
  * **Número de entrega**
  * **Número de albarán**
  * **ID del Artículo**

Después de configurar tus filtros, haz clic en **Aplicar** para aplicarlos o **Borrar** para restablecer todas las configuraciones de filtro.

Las órdenes de compra coincidentes se mostrarán según los filtros aplicados.\
Puedes:

* Ajustar los filtros y buscar nuevamente, o
* Hacer doble clic en una entrada de orden de compra para agregarla a la pantalla de Coincidencia de Órdenes de Compra.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F2uwMlpQ42lG5fOvUy4Gx%252Fpo_match_5.png%3Falt%3Dmedia%26token%3De2751f7f-586e-4303-bb17-db2a56de2b0b\&width=768\&dpr=4\&quality=100\&sign=fbf27bf2\&sv=2)

## Seleccionar Números de Órdenes de Compra y Reorganizar Columnas

Puedes cambiar entre órdenes de compra individuales para ver sus respectivos artículos de línea haciendo clic en el número de orden de compra en la parte superior de la tabla.

También puedes reorganizar las columnas dentro de cada vista de orden de compra simplemente arrastrándolas y soltándolas en tu orden preferido.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FwZzMEbGz7j20tIsouC8V%252Fpo_match_7.png%3Falt%3Dmedia%26token%3D6dc539ab-33af-40a6-8c82-04449ba317e4\&width=768\&dpr=4\&quality=100\&sign=3b8fd876\&sv=2)

Para ocultar permanentemente columnas específicas, utiliza la función [**Establecer las columnas de la tabla PO para la organización**](./#establecer-las-columnas-de-la-tabla-po-para-la-organizacion).

## Establecer las columnas de la tabla PO para la organización

Tienes la opción de ocultar o mostrar columnas específicas en la tabla de órdenes de compra haciendo clic en el ícono de configuración de columnas (mostrado a continuación).\
Esta configuración está disponible tanto en la pantalla de **Coincidencia de Órdenes de Compra** como en el menú de **Búsqueda Avanzada de Órdenes de Compra**.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F4nQ5loSdHlIebOh4vJ1m%252Fpo_tools_new_10.png%3Falt%3Dmedia%26token%3D84991cc8-f7ae-40f1-ba6c-cdd66722b898\&width=768\&dpr=4\&quality=100\&sign=ec34b898\&sv=2)

Se pueden encontrar detalles adicionales [aquí](purchase-order-matching-tools.md#establecer-las-columnas-de-la-tabla-po-para-la-organizacion).

## Re-sincronizar el número de orden de compra con Infor

Para re-sincronizar los datos en **DocBits** con los datos de **Infor**, haz clic en el **botón de actualizar** junto al número de orden de compra encima de la tabla.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FNQiPjtumht4wV9z8VHtw%252Fpo_match_8.png%3Falt%3Dmedia%26token%3Dcd9cb152-6b2f-475e-abeb-e9ad1cbd46cf\&width=768\&dpr=4\&quality=100\&sign=adab84c\&sv=2)

Si tu proceso de coincidencia se basa en el atributo **Entrega recibida Cantidad pendiente**, también tienes la opción de realizar una **sincronización manual**, como se describe en detalle [aquí](purchase-order-matching-tools.md#sincronizar-datos).

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FcceZaArRjBdKpI5r5u1v%252Fpo_tools_new_7.png%3Falt%3Dmedia%26token%3D49e25f09-de07-42b7-ab3d-a43a35e567c5\&width=768\&dpr=4\&quality=100\&sign=c6e75393\&sv=2)

## ¿Cómo hacer coincidencias?

Para hacer coincidir un artículo de línea de orden de compra con un artículo de línea extraído del documento, tienes tres opciones:

1. **Arrastrar y soltar**\
   Arrastra el artículo de línea de orden de compra deseado y suéltalo sobre el artículo de línea correspondiente en la tabla extraída.
2. **Clic derecho y conectar**
   * Haz clic derecho en el artículo de línea de orden de compra que deseas coincidir y selecciona **Seleccionar para coincidencia**.
   * Luego, haz clic derecho en el artículo de línea correspondiente en la tabla extraída y selecciona **Conectar**.
3.  **Coincidencia automática**

    Haz clic en el botón **Coincidencia Automática** para permitir que el sistema intente automáticamente hacer coincidir todos los artículos de línea basándose en los datos extraídos y de la orden de compra.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Flsdom16blO6pMF5rtQYS%252Fpo_tools_new_5.png%3Falt%3Dmedia%26token%3D616d6600-ff52-478a-9282-518212360106\&width=768\&dpr=4\&quality=100\&sign=ad47d853\&sv=2)

También puedes seleccionar **varias líneas de órdenes de compra** y hacerlas coincidir con una **única línea** en la tabla extraída. Para más detalles, haz clic [aquí](./#coincidencias-multiples).

## ¿Qué columnas se están coincidiendo?

El proceso de Coincidencia de Órdenes de Compra solo coincide columnas específicas. La lista a continuación describe qué columnas se coinciden, si están disponibles. Si no se establece ninguna [tolerancia](./#aceptar-tolerancias), las columnas solo coincidirán si son una coincidencia exacta (100%).

* [Cantidad](./#cantidad) (Cantidad | Cantidad recibida | Entrega recibida Cantidad pendiente)
* Precio unitario
* Número de Orden de Compra
* Número de artículo/ID de artículo del proveedor
* Fecha de entrega prometida

### Cantidad

Tienes tres opciones para hacer coincidir la cantidad.

* Cantidad
* Cantidad recibida
* Entrega recibida Cantidad pendiente

Puedes establecer esta opción en **Ajustes → Ajustes globales → Tipos de documentos → Más ajustes → Sección de Orden de Compra → Orden de Compra**

La opción de cantidad seleccionada determina qué columna de **cantidad de orden de compra** se utiliza para la comparación durante el proceso de coincidencia.

## **Estado de la línea de PO consumida**

Esta función agrega codificación de colores a las líneas de PO, facilitando la identificación de su estado de coincidencia de un vistazo. Más información está disponible en la página de configuración de [**Estado de la línea de PO consumida**](../../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/consumed-po-line-status.md).

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FNoof3pErQqAvAWZpo4Fd%252Fimage.png%3Falt%3Dmedia%26token%3D21a15672-8e84-4e22-a0f2-8b65bcbfda54\&width=768\&dpr=4\&quality=100\&sign=4a68abca\&sv=2)

## **Sección de orden de envío de PO**

Esta sección proporciona una visión general visual de cuánto se ha entregado y facturado por cada ítem de PO. Ayuda a rastrear el progreso de facturación utilizando valores de cantidad y una barra de progreso.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F2R9tB3JySdIMk8meRSVZ%252FPO-Shipment-Order-1.jpg%3Falt%3Dmedia%26token%3D70aa50f4-84cd-4a55-b580-037b893d1f5b\&width=768\&dpr=4\&quality=100\&sign=e4619335\&sv=2)

Se pueden encontrar más detalles en la página de [**Configuración de orden de envío de PO**](../../../administration-and-setup/settings/document-processing/module/po-shipment-order-setting.md).

## Aceptar Tolerancias

Puedes especificar niveles de tolerancia aceptables durante el proceso de coincidencia.\
Por defecto, solo las coincidencias exactas (100%) se consideran válidas.

Si se configuran tolerancias en la configuración del sistema, puedes ajustarlas para los atributos permitidos directamente en la **Tabla Extraída** bajo la columna **Comportamiento**.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FJLdikqwBf45WgFqlPUYW%252Fpo_match_11.png%3Falt%3Dmedia%26token%3D0c9d533f-f994-472a-9ff8-75ef564cef5e\&width=768\&dpr=4\&quality=100\&sign=b0c004c0\&sv=2)

Para más información sobre cómo configurar y usar tolerancias, consulta la [documentación detallada](../../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-tolerance-settings-additional-purchase-order-tolerance.md).

## Descuentos

Si hay descuentos presentes en su tabla extraída, se aplicarán automáticamente al precio unitario antes de la coincidencia, excepto cuando se utilicen [coincidencias múltiples](./#coincidencias-multiples). Más información sobre los descuentos se puede encontrar [aquí](discounts.md).

## Deshabilitar estados

Puedes excluir líneas específicas con ciertos estados de ser coincidentes. Para más información, consulta la [documentación detallada](../../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-disable-statuses.md).

## Verificar líneas coincidentes

Varios indicadores están disponibles para ayudarte a verificar si un artículo de línea ha sido coincidente exitosamente o no.

### Tabla de Órdenes de Compra

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FB3LlWddnfNcu8kUedbvb%252Fpo_match_14.png%3Falt%3Dmedia%26token%3D484a856a-b8b2-439f-bbf9-35dd4bb55343\&width=768\&dpr=4\&quality=100\&sign=b71ea425\&sv=2)

* Este ícono indica que el artículo de línea de la orden de compra ha sido coincidente exitosamente.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F2vcst2wCfyck9Z7ak4eO%252Fguide_po_2.png%3Falt%3Dmedia%26token%3D78f7a224-ba6b-4027-b6a0-61e5502fd7c2\&width=768\&dpr=4\&quality=100\&sign=e0d60903\&sv=2)

* Este ícono indica que el artículo de línea de la orden de compra contiene un desajuste.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FAb1A9PwBhrvfAf5q7f5w%252Fguide_po_5.png%3Falt%3Dmedia%26token%3D6616b59d-ffa4-4202-9382-3ac8ecd8b913\&width=768\&dpr=4\&quality=100\&sign=dd476496\&sv=2)

### Tabla Extraída del Documento

*   Este ícono indica que el artículo de línea ha sido coincidente exitosamente. Puedes pasar el cursor sobre el ícono para resaltar la línea de orden de compra correspondiente.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Flogrk90Ufp5NQ7fd1QEX%252Fpo_match_15.png%3Falt%3Dmedia%26token%3D59c96286-24e9-4790-a9db-8c02efaed305\&width=768\&dpr=4\&quality=100\&sign=1a296310\&sv=2)
*   Este ícono indica que el artículo de línea contiene un desajuste. Puedes pasar el cursor sobre el ícono para resaltar la línea de orden de compra correspondiente y ver las columnas donde ocurren desajustes.

    ![](../../../.gitbook/assets/po_match_new_4.png)

## Coincidencias Múltiples

La coincidencia múltiple permite que varias líneas de una tabla se coincidan con una única línea en la tabla correspondiente (opuesta).

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/po_match_20.png)

Esta función es particularmente útil para escenarios donde los detalles están divididos en varios artículos de línea.

### Criterios de Coincidencia

Las líneas se considerarán una coincidencia si se cumplen las siguientes condiciones agregadas:

* **Precio Unitario**:\
  Se calcula el precio unitario promedio de las múltiples líneas y se compara con el precio unitario en la tabla opuesta.
* **Cantidad**:\
  La suma de las cantidades a través de las líneas coincidentes debe coincidir con la cantidad en la tabla opuesta.
* **Requisitos Adicionales**:\
  Cualquier [criterio de coincidencia adicional](./#que-columnas-se-estan-coincidiendo) también debe ser satisfecho.

Si un solo artículo de línea se coincide con múltiples líneas, puedes ver información detallada haciendo clic en el ícono de más (+) junto al artículo de línea respectivo.

Esto expande la vista para mostrar todas las entradas coincidentes, ayudándote a verificar y gestionar múltiples coincidencias de manera efectiva.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FXueoHfU6EiDKaWBKJL2X%252Fpo_match_19.png%3Falt%3Dmedia%26token%3D9b947abd-5fbc-45e7-8e55-8b38746b5e32\&width=768\&dpr=4\&quality=100\&sign=191a712\&sv=2)

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FZJZekesrA0JB04GixOUi%252Fpo_match_18.png%3Falt%3Dmedia%26token%3D25c10718-2044-4de9-a5db-45f936d7235a\&width=768\&dpr=4\&quality=100\&sign=dd63d6c4\&sv=2)

## Eliminar Conexiones de PO

Para eliminar una conexión entre un artículo de línea de orden de compra y un artículo de línea extraído, simplemente haz clic en el ícono **X** junto al par coincidente.\
Una vez eliminado, la conexión se cancela y el artículo de línea se vuelve disponible para coincidencias nuevamente.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FSznmTo3Fnfi72ccpuLZk%252Fpo_match_new_2.png%3Falt%3Dmedia%26token%3Da04727b2-c8bf-44e0-b8f4-eaedb8180500\&width=768\&dpr=4\&quality=100\&sign=b740b466\&sv=2)

## Cálculo

Debajo de la tabla que contiene la información extraída de tu documento, puedes encontrar cálculos simples para verificar si las reservas totales coinciden.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FA3TOYG26aHrETnMz4ADB%252Fimage.png%3Falt%3Dmedia%26token%3Db481bbc5-d278-4a46-b3cf-813225fa10ca\&width=768\&dpr=4\&quality=100\&sign=eeca6ad9\&sv=2)

### Reservas registradas:

El valor de las reservas registradas se deriva del importe neto extraído del documento.

```
Reservas registradas = Importe neto total (extraído del documento)
```

### Total coincidente:

Este valor se calcula sumando el **Precio unitario** × **Cantidad** para todos los artículos de línea que coincidieron exitosamente con los artículos de línea del número de orden de compra.

```
 Total coincidente = Suma de (Precio unitario × Cantidad) para todos los artículos de línea coincidentes
```

### **Cargos:**

Cualquier cargo aplicable se incluirá en esta sección si está presente.\
Para más detalles, consulta la [documentación detallada](../../../administration-and-setup/settings/document-processing/classification-and-extraction/table-extraction-for-costing-element.md).

```
Cargos = Elemento de costo
```

### Cantidad pendiente de liquidar:

La diferencia resultante se muestra aquí y se calcula de la siguiente manera:

```
Cantidad pendiente de liquidar = Reservas registradas - Total coincidente - Elemento de costo
```

## Visualización del Documento para Validación

En el lado derecho de la pantalla de **Coincidencia de Órdenes de Compra**, puedes ver el documento para ayudar con la validación.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F7X5cxghPovZfE8B2hvIy%252Fpo_new_1.png%3Falt%3Dmedia%26token%3D613a52db-b1a7-4d15-af8e-ab63725ae78c\&width=768\&dpr=4\&quality=100\&sign=3a887d60\&sv=2)

**Características de la Barra de Herramientas del Visor de Documentos:**

* Desplázate por las páginas del documento para revisar el contenido.
* Haz clic en el nombre del archivo para abrir la pantalla de validación completa.
* Ingresa un número de página y presiona Enter para saltar directamente a esa página.
* Usa los botones más (+) y menos (–) para acercar o alejar el documento.
*   Haz clic en el botón en el extremo derecho para abrir el documento en una ventana separada, lo cual es especialmente útil cuando trabajas con múltiples pantallas.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F8nUElRimoIOprR5yV5lN%252Fpo_match_10.png%3Falt%3Dmedia%26token%3De0d6924c-127f-4333-95f9-1b32d52b0da5\&width=768\&dpr=4\&quality=100\&sign=4f8161e4\&sv=2)

## Guardar Cambios:

Para guardar tus cambios, haz clic en el botón **Guardar** en la barra de herramientas.\
Si abandonas la página sin guardar, todo el progreso realizado durante el proceso de coincidencia se perderá.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FZ9ou72AJwvme2F7RWG7P%252Fpo_tools_new_6.png%3Falt%3Dmedia%26token%3D1d8ef55e-5ff1-4ee7-ac81-b76ff583a353\&width=768\&dpr=4\&quality=100\&sign=a17e5c90\&sv=2)

## Exportar el Documento

Después de hacer coincidir todos los artículos de línea y validar su corrección, puedes exportar el documento haciendo clic en el botón **Exportar** en la barra de herramientas.

* Hacer clic en la pequeña flecha junto al botón **Exportar** revela todas las opciones de exportación disponibles.
* Hacer clic en **Exportar** directamente activará la opción de exportación predeterminada (la primera en la lista).

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fzc78lqQthkeTIpANlIAc%252Fpo_tools_new_8.png%3Falt%3Dmedia%26token%3Debdb58e9-b775-40a6-b7bc-82aa66f8811b\&width=768\&dpr=4\&quality=100\&sign=14ac5a25\&sv=2)
