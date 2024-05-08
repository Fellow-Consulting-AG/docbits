# Más ajustes

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 09.54.48.png" alt=""><figcaption></figcaption></figure>

#### Visión general

El área de Más ajustes permite a los administradores configurar varios aspectos del procesamiento de documentos que no están cubiertos en la configuración básica. Esto incluye opciones para extracción de tablas, revisión de documentos, generación de PDF, procesos de aprobación y ajustes específicos para operaciones como órdenes de compra o contabilidad.

#### Funciones clave y opciones

1. **Extracción de tablas**:
* **Omitir validación de tablas**: Permite omitir el proceso de validación de datos de tabla, lo cual puede ser útil en escenarios donde la validación de datos necesita ser flexible.
2. **En revisión**:
* **Diseño en formulario de revisión**: Configura el diseño y los campos que aparecen en los formularios de revisión utilizados durante el proceso de revisión de documentos.
3. **Generación de PDF**:
* **Diseño de plantilla**: Especifica la plantilla utilizada para generar versiones en PDF de los documentos, lo cual puede ser crucial para archivar o comunicación externa.
4. **Aprobación**:
* **Aprobar antes de exportar**: Asegura que los documentos deben ser aprobados antes de poder ser exportados del sistema.
* **Segunda aprobación**: Agrega una capa adicional de aprobación para una validación más profunda, mejorando el control sobre el procesamiento de documentos.
5. **Orden de compra / Contabilidad automática**:
* **Tabla de OC en constructor de diseño**: Habilita la inclusión de tablas de órdenes de compra en el constructor de diseño para diseños de documentos personalizados.
* **Orden de compra**: Activa el procesamiento de documentos de órdenes de compra dentro del sistema.
* **Configuración de tolerancia de OC**: Establece niveles de tolerancia para las cantidades de órdenes de compra, lo cual ayuda a acomodar discrepancias menores sin marcarlas como errores.
6. **Exportación alternativa de documentos**:
* **Desactivar estados de OC**: Permite desactivar ciertos estados para órdenes de compra durante el proceso de exportación, brindando flexibilidad en cómo se manejan las órdenes.
7. **Mapeo de número de artículo del proveedor**:
* Un ajuste de utilidad que mapea los números de artículo del proveedor a los números de artículo internos, asegurando precisión en la gestión de inventario y órdenes de compra.

{% @jira/embed url="https://fellowpro.atlassian.net/browse/DOCB-2500" %}
