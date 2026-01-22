# XRechnung

{% embed url="https://youtu.be/AxrHNEmmXtg" %}
DocBits E-Invoice Tutorial: Process XRechnung / ZUGFeRD (Factur-X), Validate Data & Automate Workflows
{% endembed %}

## Descripción general

En el panel de administración de XRechnung, encontrará los siguientes componentes clave:

## 1. Transformación

### Propósito

El proceso de Transformación es esencial para convertir datos sin procesar, generalmente en formato XML, en un formato estructurado que cumpla con requisitos específicos, como generar una factura. En XRechnung, esto se logra principalmente mediante XSLT (Extensible Stylesheet Language Transformations). XSLT es un lenguaje diseñado para transformar documentos XML en otros tipos de documentos, como otro XML, HTML o texto plano.

### Cómo funciona

• Plantilla XSLT: El archivo XSLT define cómo se procesan los datos XML y cómo debe ser la salida final. Aplica reglas y plantillas para extraer, manipular y generar los datos del documento XML.

• Elementos y atributos: El archivo XSLT contiene elementos y atributos específicos que controlan el proceso de transformación. Por ejemplo, \<xsl:value-of> se utiliza para extraer el valor de un nodo específico del documento XML.

### Capacidades del administrador

• Modificar el XSLT:

• Editar plantillas existentes: Un administrador puede modificar las plantillas XSLT existentes para cambiar cómo se transforman los datos XML de entrada. Por ejemplo, si es necesario extraer información adicional del documento XML, un administrador podría agregar nuevas reglas en el archivo XSLT.

• Crear nuevas versiones: Si se requieren cambios, un administrador puede crear una nueva versión de la plantilla XSLT. Esto asegura que las versiones anteriores permanezcan intactas para referencia histórica o reversión si es necesario.

### Ejemplo:

Supongamos que la plantilla XSLT extrae el ID de la factura utilizando:

```xml
<xsl:value-of select="//INVOICE/INVOICE_ID/text()" />
```

Si es necesario extraer un nuevo campo, como un número de referencia del cliente, un administrador podría agregar:

```xml
<xsl:value-of select="//INVOICE/CUSTOMER_REFERENCE_NUMBER/text()" />
```

## 2. Vista previa

### Propósito

La función de Vista previa permite a los administradores ver la salida generada por la transformación XSLT antes de finalizarla. Este paso es crucial para garantizar que las reglas de transformación funcionen correctamente y que la salida cumpla con los estándares requeridos.

### Cómo funciona

• Validación en tiempo real: La función de vista previa proporciona una representación en tiempo real de cómo se verán los datos transformados cuando se apliquen a un documento real (como una factura). Esto ayuda a detectar errores o problemas de formato de forma temprana.

• Ajustes: Si la vista previa muestra discrepancias o errores, se pueden realizar ajustes directamente en el archivo de transformación (XSLT).

### Capacidades del administrador

• Personalizar la vista previa:

• Modificar la configuración de la vista previa: Un administrador puede ajustar qué partes de la transformación se previsualizan. Por ejemplo, podría centrarse en secciones específicas del documento o probar nuevas reglas agregadas a la plantilla XSLT.

• Guardar e iterar: Después de realizar los ajustes, la vista previa se puede actualizar para ver los cambios. Este proceso iterativo permite el ajuste fino hasta lograr la salida deseada.

### Ejemplo:

Si un administrador nota que el formato de fecha en la vista previa es incorrecto (por ejemplo, muestra AAAA-MM-DD en lugar de DD-MM-AAAA), puede modificar el XSLT para formatear la fecha correctamente y ver inmediatamente el resultado en la vista previa.

## 3. Rutas de extracción

### Propósito

Las Rutas de extracción definen las rutas específicas dentro de una estructura XML o JSON de las cuales se deben extraer los datos. Este proceso es esencial para aislar piezas clave de información dentro del documento que se utilizarán en la transformación o para otras tareas de procesamiento.

### Cómo funciona

• XPath y JSONPath: Las rutas de extracción utilizan lenguajes como XPath (para XML) o JSONPath (for JSON) para especificar la ubicación de los datos dentro del documento. Estas rutas son fundamentales para indicarle al sistema exactamente dónde encontrar y cómo extraer la información requerida.

### Capacidades del administrador

• Definir y modificar rutas:

• Modificar rutas existentes: Un administrador puede modificar las rutas de extracción si la estructura de datos cambia o si es necesario extraer datos adicionales. Esto podría implicar cambiar las expresiones XPath o JSONPath.

• Agregar nuevas rutas: Para nuevos campos o puntos de datos, un administrador puede definir nuevas rutas de extracción. Esto implicaría especificar la ruta correcta en el documento XML o JSON.

### Ejemplo:

En un documento de factura XML, si la ruta al ID de la factura se define como:

```json
"invoice_id": "//INVOICE/INVOICE_ID/text()"
```

Y es necesario agregar un nuevo campo, como una dirección de envío, un administrador podría agregar:

```json
"shipping_address": "//INVOICE/SHIPPING/ADDRESS/text()"
```
