# Reglas de Coincidencia de Órdenes de Compra

{% embed url="https://youtu.be/qR-lrSaj4Ug" %}
DocBits PO Matching Tutorial: Auto/Manual Line Matching, Tolerances & Mismatch Indicators
{% endembed %}

La coincidencia de órdenes de compra (OC) es un proceso crítico para garantizar la coherencia entre las órdenes de compra (OC) y las facturas entrantes o recibos de mercancías correspondientes. Un conjunto robusto de reglas es esencial para lograr una alta tasa de coincidencia automática, prevenir el fraude y asegurar pagos correctos.

Esta página de configuración se utiliza para definir y gestionar las reglas que determinan _cómo_ se emparejan los artículos de línea de la OC con el documento entrante correspondiente (Factura, Confirmación de Pedido).

***

## Cómo Acceder

1.  Navegue a **Configuración --> Configuración Global --> Tipos de Documento**

    <figure><img src="../../../../../../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>


2.  Seleccione el tipo de documento deseado y haga clic en **Más configuraciones**.

    <figure><img src="../../../../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>


3.  Luego vaya a la sección Orden de Compra y haga clic en el botón (PO match server side) después de eso haga clic en Configurar Reglas de Coincidencia de OC

    <figure><img src="../../../../../../.gitbook/assets/docbits_field_validation_formatting.png" alt="Docbits Field Validation Formatting"><figcaption></figcaption></figure>

***

<figure><img src="../../../../../../.gitbook/assets/Bildschirmfoto 2025-12-09 um 07.43.15.png" alt=""><figcaption></figcaption></figure>

## Configuración Global (Reglas Base)

Estas configuraciones establecen el marco que se aplica a todas las reglas de coincidencia:

* **Configuración:** Coincidir Cantidad En
  * **Propósito:** Define qué campo de cantidad específico debe usarse principalmente como punto de referencia para emparejar artículos de línea de órdenes de compra en todas las reglas.
  * **Valores Válidos:** Cantidad u otros campos de cantidad disponibles en el sistema, dependiendo de la estructura de datos (por ejemplo, un campo de cantidad normalizado alternativo).
  * **Dependencia:** Determina la base para todas las reglas de coincidencia que incluyen la cantidad en sus criterios de comparación.
* **Configuración:** Tolerancia Estándar (Tolerancia Predeterminada)
  * **Propósito:** Define la desviación porcentual permitida en la cantidad para que una coincidencia se considere válida. Compensa pequeñas diferencias de redondeo o cantidad.
  * **Valor Válido:** Un número decimal (por ejemplo, 0.005 corresponde al 0.5%).
  * **Dependencia:** Se aplica a las reglas que utilizan campos de cantidad para la coincidencia y tienen habilitada la opción "Permitir Tolerancia".

***

## Lista de Reglas

La Lista de Reglas muestra todas las reglas de coincidencia disponibles y gestiona su orden de ejecución.

#### Estructura y Ejecución

* **Prioridad:** Este campo numérico (por ejemplo, 1, 2, 3) dicta la secuencia de ejecución de las reglas. Las reglas con un número de prioridad más bajo se intentan primero. Esto permite a los administradores estructurar una jerarquía, comenzando típicamente con las reglas más específicas y estrictas (por ejemplo, coincidencia por número de línea y número de parte) y recurriendo a reglas más amplias o menos restrictivas.
* **Nombre y Descripción:** Proporciona una identificación clara y contexto para la regla, explicando los criterios primarios utilizados (por ejemplo, "Regla Estándar No. 1: Coincidencia basada en Número de Línea, ID de Parte y Cantidad").
* **Activa:** Un interruptor simple que permite la activación o desactivación instantánea de la regla sin necesidad de eliminar su configuración.

**Flujo de Ejecución:** El sistema realiza la coincidencia en una secuencia en cascada. Si una regla (por ejemplo, Prioridad 1) empareja con éxito un artículo de línea, el proceso para ese artículo se detiene. Si no se encuentra ninguna coincidencia, el sistema procede a la siguiente regla en la secuencia de prioridad (por ejemplo, Prioridad 2).

***

## Configuración de Regla (Configuración Detallada)

Esta área de configuración detallada define la lógica y los criterios específicos para una regla individual.

#### Parámetros Base

* **Tipo de Regla (por ejemplo, Coincidencia Única):** Especifica la cardinalidad de la coincidencia. Coincidencia Única (Single Match) es el tipo común, que requiere una coincidencia uno a uno (una línea de OC con una línea de Factura). Otros tipos pueden incluir coincidencias de muchos a uno o uno a muchos para artículos agregados o entregas divididas.
* **Coincidencia Automática:** Si está habilitada, el sistema intentará aplicar esta regla de forma totalmente automática. Se requiere una alta confianza en los criterios para el procesamiento automático.
* **Coincidencia Manual:** Si está habilitada, esta regla puede ser presentada o aplicada por un usuario durante el paso de reconciliación manual, ofreciéndole un conjunto predefinido de criterios de comparación para resolver excepciones.

#### Comparación de Columnas (Criterios de Coincidencia)

Esta es la definición central de la lógica de la regla, especificando qué campos deben alinearse entre los documentos.

1. Definiendo las Columnas para Comparar:
   * **Columnas de OC:** El campo extraído de los datos de la Orden de Compra (por ejemplo, número de línea).
   * **Columnas de Tabla Extraídas:** El campo correspondiente extraído o analizado del documento entrante (Factura/Confirmación de Pedido) (por ejemplo, `POSITION`).
2. **Tipo de Comparación:** Define la naturaleza de la coincidencia requerida (por ejemplo, Tt para comparación de Texto/Cadena, que requiere una coincidencia exacta carácter por carácter; # para comparación Numérica).
3. **Permitir Tolerancia:** Para campos numéricos (cantidad, precio), activar esta opción indica al sistema que aplique la Tolerancia Estándar Global definida anteriormente. Si esto _no_ está habilitado para un campo numérico, los valores deben coincidir exactamente.
4. **Ignorar en Coincidencia Manual:** Si está marcado, este criterio se relaja durante la intervención manual. Esto es útil para campos como descripciones o referencias internas que pueden variar ligeramente, permitiendo al usuario anular pequeñas discrepancias no críticas.

**Ejemplo: Regla de Coincidencia de OC Estricta (`DefaultRule#1`)**

Una regla estricta típica combina verificaciones de identidad obligatorias con verificaciones de valor:

* **Identidad Obligatoria:** El Número de Línea y el Identificador de Artículo deben coincidir exactamente (comparación de texto, sin tolerancia).
* **Verificaciones de Valor:** La Cantidad Normalizada Efectiva y el Precio Unitario Normalizado Efectivo deben coincidir (comparación numérica, Tolerancia Permitida). Solo si se cumplen los cuatro criterios (con tolerancia para los valores) se ejecuta una coincidencia automática.

***

## Impacto en el Proceso de Coincidencia de OC

El conjunto de reglas definido gobierna directamente la eficiencia y la integridad del flujo de trabajo de coincidencia de OC:

* **Priorización y Respaldo:** La Prioridad definida asegura que el sistema intente primero el método de coincidencia más confiable. Si las reglas estrictas y de alta prioridad fallan, el sistema recurre a reglas más amplias, con el objetivo de minimizar el número de excepciones dirigidas a los usuarios.
* **Control de la Calidad de la Coincidencia:** Las reglas más estrictas (que requieren coincidencias más exactas y menos tolerancia) resultan en menos coincidencias automáticas, pero altamente confiables. Las reglas más flexibles aumentan la tasa de coincidencia automática pero aumentan el riesgo de falsos positivos.
* **Manejo de Excepciones (Coincidencia Manual):** Al habilitar reglas para la Coincidencia Manual, el sistema proporciona opciones estructuradas para los usuarios. Si una transacción no cumple con los criterios de coincidencia automática, se convierte en una excepción. El usuario puede entonces intentar resolver la excepción aplicando una regla manual predefinida, que podría tener criterios relajados (por ejemplo, ignorar una pequeña discrepancia de texto según la configuración "Ignorar en Coincidencia Manual").

***

## Personalizar las Reglas de Coincidencia de OC

Para editar las reglas de Coincidencia de OC, la versión predeterminada se puede clonar haciendo clic en **"Configurar Versionado"** y utilizando la opción **"Clonar como Borrador"** de las opciones de tarjeta disponibles

<figure><img src="../../../../../../.gitbook/assets/docbits_doc_type_export_formats.png" alt="Docbits Doc Type Export Formats"><figcaption></figcaption></figure>
