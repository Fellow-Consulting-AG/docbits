# EDI

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 09.49.21.png" alt=""><figcaption></figcaption></figure>

#### Visión general

En Docbits, la configuración de EDI proporciona herramientas para definir y gestionar la estructura y formato de los mensajes EDI que corresponden a varios tipos de documentos, como facturas u órdenes de compra. La configuración permite la personalización de los mensajes EDI para cumplir con los estándares y requisitos específicos de diferentes socios comerciales e industrias.

#### Funciones clave y opciones

1. **Elementos de configuración de EDI**:
* **Descriptor de estructura**: Define la estructura básica del documento EDI, incluido el orden de los segmentos, campos obligatorios y calificadores necesarios para que el documento EDI sea válido.
* **Transformación**: Especifica las transformaciones aplicadas para convertir los datos del documento en un mensaje con formato EDI. Esto implica especificar asignaciones de campos de documento a segmentos y elementos EDI.
* **Vista previa**: Permite a los administradores ver cómo se verá el mensaje EDI después de la transformación, lo que ayuda a garantizar la precisión antes de la transmisión.
* **Rutas de extracción**: Muestra las rutas utilizadas para extraer valores del documento, que luego se utilizan para completar el mensaje EDI.
2. **Editor XSLT**:
* Se utiliza para editar y validar el XSLT (Transformaciones de Lenguaje de Hojas de Estilo Extensible) utilizado en el proceso de transformación. XSLT es un lenguaje potente diseñado para transformar documentos XML en otros documentos XML u otros formatos como HTML, texto o incluso otras estructuras XML.

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 09.49.59.png" alt=""><figcaption></figcaption></figure>

{% @jira/embed url="https://fellowpro.atlassian.net/browse/DOCB-2499" %}
