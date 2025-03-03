# List Of Values

<figure><img src="../../../.gitbook/assets/Bildschirmfoto%202024-05-08%20um%2011.20.51.png" alt=""><figcaption></figcaption></figure>

La configuración de "Lista de Valores" en su sistema de procesamiento de documentos es esencialmente un repositorio central para gestionar valores predefinidos que se pueden utilizar en varios formularios y campos dentro del sistema. Esta configuración es particularmente útil para estandarizar la entrada de datos y garantizar la coherencia en los documentos procesados por el sistema.

1. **Segmentación por Tipo**: Cada sección, como "ISO\_Currency", "Invoice\_Sub\_Type", "Invoice\_Type" y "Test", representa una categoría diferente de valores predefinidos. Estas categorías se utilizan para gestionar diferentes tipos de entradas de datos relevantes para sus contextos específicos dentro del sistema.
2. **Valores y Sinónimos**: Bajo cada categoría, puede definir varios valores. Por ejemplo, bajo "Invoice\_Sub\_Type", se enumeran valores como "Factura de Costo" y "Factura de Compra". Además, tiene la capacidad de asignar sinónimos a estos valores, mejorando la flexibilidad y alcance de la captura de datos. Por ejemplo, "Factura de Costo" tiene sinónimos como "Kostenrechnung" y "Cost Invoice".
3. **Uso en Suborganizaciones**: Estos valores también se pueden hacer específicos para ciertas suborganizaciones dentro de su configuración, lo que permite la personalización y localización de flujos de trabajo de procesamiento de documentos.
4.  **Agregar y Gestionar Valores**: Cuando presionas el botón de acción, se te presentan dos opciones para agregar valores a tu lista. La primera opción es agregar filas manualmente. Al hacer clic en el botón **Agregar Fila**, aparece un popup que te permite introducir nuevos valores junto con cualquier sinónimo. Si necesitas agregar múltiples entradas, simplemente puedes hacer clic en **Agregar Más Valores** para generar otra fila.

    La segunda opción es subir un archivo CSV. Para hacer esto, haz clic en el botón **Subir CSV**, selecciona un archivo **CSV** que deseas importar, elige el delimitador correcto para asegurar que los datos se analicen con precisión, y luego haz clic en **Subir** para completar el proceso.

    Además, cada fila incluye un botón de acción que te permite editar o eliminar una entrada existente según sea necesario.
