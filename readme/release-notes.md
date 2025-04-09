# Notas de versión

## Lanzamiento Spring Bloom – 23 de abril de 2025

### Mejoras en DocBits:

* **Opción de Filtro para el Registro de Importación de Correos Electrónicos:** Los usuarios ahora tienen la capacidad de filtrar los registros de importación y ordenar la tabla para una visión más clara y eficiente. Esta mejora agiliza el proceso de identificación y gestión de entradas de correo electrónico, mejorando la resolución de problemas y la gestión general de registros.
* **Soporte Multilingüe para la Lista de Valores:** Hemos ampliado las capacidades multilingües en la función de Lista de Valores. Los administradores ahora pueden definir etiquetas en múltiples idiomas, asegurando que la etiqueta correcta se muestre automáticamente según la configuración del idioma del sistema del usuario. Esta mejora promueve una mayor accesibilidad y localización, facilitando que los usuarios de todo el mundo interactúen con la plataforma en su idioma nativo.
* **Mejoras en los Detalles del Usuario en Configuración:** La interfaz de configuración ahora muestra información completa del usuario. Los administradores pueden ver fácilmente las afiliaciones a grupos, detalles de suborganizaciones y datos clave adicionales, lo que permite una mejor gestión de los roles de usuario y una comprensión más clara de las estructuras del equipo.
* **Información de Contabilidad Automática en la Pantalla de Aprobación:** La pantalla de aprobación ahora presenta detalles de contabilidad automática junto con la información de la factura. Esta mejora proporciona una visión más profunda de los datos de transacción, facilitando procesos de revisión más fluidos y una toma de decisiones más informada respecto a las facturas.
* **Contador de Tareas para Documentos en la Vista del Tablero:** Los documentos en el tablero ahora pueden indicar las tareas abiertas asociadas con ellos y mostrar el número total de tareas pendientes. Esta función proporciona a los usuarios una visión rápida de las acciones pendientes, mejorando la gestión de tareas y la eficiencia del flujo de trabajo.
* **Selección de Modelo de IA Basado en Proveedores:** Los usuarios ahora pueden seleccionar el modelo de IA utilizado para la extracción de datos por proveedor. Esta mejora permite una optimización ajustada, asegurando una mejor precisión en la extracción para diferentes proveedores y mejorando los resultados generales del procesamiento de datos.
* **Registros de Flujo de Trabajo Mejorados para Tarjetas de Árbol de Decisión:** Los registros ahora muestran la salida del árbol de decisión, facilitando el seguimiento y la comprensión de cómo se tomaron las decisiones dentro de los flujos de trabajo.
*   **Introducción de un Nuevo Sistema de Pruebas Automáticas para Mejorar la Funcionalidad y Estabilidad del Sistema:**

    Nos complace anunciar la implementación de un nuevo sistema de pruebas automatizadas diseñado para mejorar la funcionalidad y fiabilidad general de nuestra plataforma. Esta nueva configuración realizará verificaciones consistentes y exhaustivas en nuestro sistema para identificar cualquier problema antes de que afecte su experiencia. Al automatizar estas pruebas, podemos garantizar respuestas más rápidas a problemas potenciales y mantener los más altos estándares de calidad para nuestro sistema.

    ​

### Corrección de Errores

* Se resolvió un problema donde las tareas no aparecían en la pantalla de validación/aprobación.
* Se corrigió la posición del botón Siguiente/Anterior para que permanezca estático.
* Se solucionaron problemas de desplazamiento en las vistas de script y árbol de decisiones, asegurando que los botones de acción permanezcan estacionarios durante el desplazamiento.
* Se eliminó el campo de país de origen de las facturas electrónicas.
* Se corrigió un problema con el contador de tareas que mostraba un número inexacto de tareas.
* Se añadieron traducciones faltantes.
* Se corrigieron campos personalizados para mostrar nombres descriptivos en lugar de IDs.
* Se actualizó la lista de accesos directos para la pantalla de coincidencia de PO.
* Se resolvió un problema donde los documentos se descargaban con un nombre de archivo incorrecto.
* Se corrigieron inconsistencias de ordenamiento en la tabla de líneas de factura dentro de la coincidencia de PO.
* Se solucionó un problema que afectaba la funcionalidad de creación de tareas.
* Se corrigió un problema en la coincidencia de PO donde el ordenamiento de la tabla de facturas se restablecía al coincidir una línea.
* Se resolvieron problemas de contabilidad automática asegurando que las referencias de reserva se dividieran correctamente cuando se divide un monto.
* Se actualizó la información del host de ClickHouse.
* Se resolvió un problema donde los documentos duplicados no eran reconocidos como duplicados.
* Se corrigieron problemas de exportación causados por referencias de reserva que eran demasiado largas.
* Se resolvió un problema donde las casillas de verificación de solo lectura no eran de solo lectura.

​

## Lanzamiento de Hot Fix Winter Frost 10 de abril de 2025

### Mejoras en DocBits:

* **Función de Script `set_column_date_value` Mejorada:** La función `set_column_date_value` ahora incluye soporte para la opción `skip_weekend`, permitiendo que los valores de fecha omitan automáticamente los fines de semana al aplicarse.
* **Mejora en el Soporte de Carga de Archivos:** Los archivos PNG y JPEG ahora se pueden cargar directamente y se convierten automáticamente en formato PDF para un manejo de documentos más eficiente.
* **Actualizaciones de Funcionalidad de Watchdog:**
  * Ahora soporta exportación a **Enaio** para una mejor integración del sistema.
  * Capacidades de análisis mejoradas para extraer información de las estructuras XML de `Sync.ContentDocument`, lo que permite un procesamiento de datos más eficiente.

### Correcciones de Errores

* Se solucionó un problema en una función de script.
* Se resolvió un problema donde las órdenes de compra tenían un estado incorrecto después de ser actualizadas.

## Lanzamiento Hot Fix Winter Frost 11 de marzo de 2025

### Mejoras en DocBits:

* **Extracción de Datos Mejorada:** Se añadió una opción para extraer el **Purchase Order** o **Item Number** de una línea arriba o abajo.
* **Acceso Ampliado a Suborganizaciones Cruzadas:** Los usuarios no administradores ahora también pueden acceder a la función de **Cross Sub-Organizations**.

### **Corrección de Errores:**

* Se corrigió un problema donde los usuarios no podían ser añadidos a un grupo.
* Se corrigió un problema con fallos en la importación de correos electrónicos.
* Se resolvió un problema con la capacitación en el campo en documentos con más de una página
* Se corrigió un problema donde los scripts no funcionaban correctamente.
* Se resolvió un problema donde los datos del documento no se mostraban correctamente
* Se corrigió un problema con la configuración de actualización automática de la orden de compra
* Se solucionó un problema donde los tokens de suscripción se mostraban incorrectamente
* Se resolvió un problema donde la pantalla de tareas mostraba una versión de documento desactualizada
* Se corrigió un problema que causaba que los documentos no cambiaran su estado
* Se solucionó un problema donde los usuarios podían ser añadidos a una suborganización dos veces.
* Se solucionó un problema donde cambiar la suborganización de un documento causaba restablecer el usuario o grupo asignado.
