# Notas de versión

## Release Winter 10 de Diciembre de 2025

### Mejoras en DocBits:

* **Personalización Mejorada de Reglas de Coincidencia de Pedidos:**\
  DocBits ahora ofrece un control granular sobre las reglas de coincidencia de órdenes de compra. Puede configurar exactamente qué columnas deben coincidir para cada tipo de documento, definir tolerancias por columna y elegir si cada regla se aplica a la coincidencia manual, automática o ambas. Estas mejoras brindan a los usuarios la flexibilidad para ajustar el proceso de coincidencia según sus necesidades operativas específicas.
*   **Soporte para Múltiples Cuentas Financieras de Proveedores:**\
    DocBits ahora admite múltiples cuentas financieras para proveedores a través del BOD RemitToPartyMaster de Infor. Está disponible una nueva configuración para activar esta función.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_notes_12_2025_1.png)
*   **Agregar Acceso de Usuario a Resultados de Extracción OCR:**\
    El botón Vista OCR en la pantalla de Validación de Campos ahora es accesible para todos los usuarios con acceso de validación, no solo para administradores, lo que permite a todos los usuarios revisar los resultados de extracción OCR y buscar contenido específico en los documentos.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_notes_12_2025_2.png)
* **Renderizado Dinámico de Columnas en Pantallas de Aprobación:**\
  Se mejoraron las vistas de aprobación para mostrar dinámicamente solo las columnas configuradas para comparación en las preferencias de base de datos de cada organización. Anteriormente, columnas como Código de Unidad y Fecha de Entrega Prometida aparecían vacías cuando no estaban configuradas para comparación, causando confusión. Ahora, las vistas de aprobación solo muestran campos que se están comparando activamente. Esto proporciona pantallas de aprobación más claras y específicas de la organización sin columnas vacías o irrelevantes.
* **Campo Tipo de Pedido Agregado a la Búsqueda de Datos Maestros**:\
  La lista de encabezados de órdenes de compra ahora incluye una columna "Tipo de Pedido" (type\_code) en la búsqueda de datos maestros, proporcionando capacidades de categorización adicionales.
* **Mejoras en el Panel de Filtros Personalizados:**\
  Se mejoró la funcionalidad de compartir paneles al permitir que los usuarios compartidos editen los filtros del panel. Los usuarios que tienen paneles compartidos con ellos ahora pueden modificar los filtros para una vista más flexible y personalizada.
* **Prefijos Personalizables para Columnas de Pantalla de Aprobación:**\
  Se agregó una opción configurable para mostrar prefijos antes de las columnas de documentos en las pantallas de aprobación. El prefijo se puede establecer en el constructor de diseño, lo que permite a los usuarios elegir si aparecen prefijos y a qué tipos de documentos se aplican.\


### Mejoras Generales

* Se mejoró el registro de errores para tablas mal entrenadas en la extracción de tablas.
* Se agregó un límite de compartición para paneles de hasta 10 usuarios o 5 grupos, junto con un mensaje de error claro cuando se alcanza el límite.
* Se mejoró el manejo de errores para paneles personalizados cuando un usuario intenta crear un panel con un nombre que ya existe.

### Correcciones de Errores:

* Se corrigió un problema donde los correos electrónicos parecían enviarse exitosamente desde la sección Detalles del Proveedor pero no se entregaban a los destinatarios.
* Se corrigió un problema donde los campos desplegables agregados a las pantallas de aprobación/rechazo no se mostraban.
* Se corrigió un problema donde todos los documentos exportados estaban marcados como actualizados por última vez por el usuario incorrecto.
* Se corrigió un problema donde las importaciones FTP no recogían documentos.
* Se corrigió un problema donde los documentos mostraban el estado "Flujo de trabajo en progreso" pero no se ejecutaban flujos de trabajo y el registro permanecía vacío.
* Se corrigió un problema donde usuarios no relacionados eran asignados a documentos en el momento de la exportación sin realizar ningún trabajo en ellos.
* Se corrigió un problema donde usuarios con permisos correctos no podían rechazar documentos asignados y recibían errores.
* Se corrigió un problema donde los iconos de flujo de documentos no se mostraban para algunas organizaciones.
* Se corrigió un problema donde aparecía una ventana emergente al cargar documentos con arrastrar y soltar en el panel.
* Se corrigió un problema donde las banderas E-TEXT se mostraban como habilitadas en la interfaz de usuario aunque la respuesta de la API mostraba todos los valores como falsos.
* Se corrigió un problema donde ocurría un error al cargar documentos que contenían páginas en blanco.
* Se corrigió un problema donde los hipervínculos de tareas en las notificaciones por correo electrónico usaban la URL de aprobación v2 en lugar de v3.
* Se corrigió un problema donde la Búsqueda de Datos Maestros no mostraba ningún proveedor cuando se seleccionaba la sub-organización "Cross", impidiendo que los usuarios vean datos de proveedores entre organizaciones.
* Se corrigió un problema donde los documentos cargados en Cross no se asignaban a un ID de sub-organización.
* Se corrigió un problema donde las importaciones de correo electrónico entrante fallaban para remitentes con letras mayúsculas en sus direcciones de correo electrónico debido a la comparación de correo electrónico sensible a mayúsculas y minúsculas.

## Release Autumn Summit 22 de Octubre de 2025

### Mejoras en DocBits:

*   #### Mejoras en el Diseño de Plantillas de Correo Electrónico:

    El editor de plantillas de correo electrónico ha sido rediseñado para proporcionar una estructura más clara y una experiencia más fluida. Ahora es más intuitivo seleccionar campos de documentos, y los adjuntos se pueden incluir directamente dentro de las plantillas. Estas mejoras hacen que sea más rápido y fácil crear correos electrónicos profesionales y personalizados.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fdv4oDlfkRyD0W9yWGAA4%252Fimage.png%3Falt%3Dmedia%26token%3D14bf7ebd-d886-4758-8184-d7b94447518a\&width=768\&dpr=4\&quality=100\&sign=88405d9c\&sv=2)
*   #### Mejoras en el Panel de Control:

    El panel de control se ha ampliado para mejorar la navegación y personalización. Con nuevas pestañas, los usuarios pueden cambiar más rápidamente entre diferentes tipos de documentos, reduciendo el tiempo dedicado a buscar la vista correcta.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FmpO7WSIrkL0I8Rje3HQt%252Fimage.png%3Falt%3Dmedia%26token%3D77d03fe7-e626-4645-b191-e332715a25fb\&width=768\&dpr=4\&quality=100\&sign=93fa9925\&sv=2)
*   #### Paneles de Filtro Personalizados:

    Además, los paneles de control ahora se pueden personalizar y filtrar según las preferencias individuales. Estos paneles personalizados también se pueden compartir con colegas, lo que facilita la creación de vistas de informes consistentes para todo el equipo.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fn5rPvGnRltT3mTIDoJwV%252Fimage.png%3Falt%3Dmedia%26token%3D22d065e3-81eb-4f16-828c-7f9134c25b1b\&width=768\&dpr=4\&quality=100\&sign=eb11d3a3\&sv=2)
*   #### Registros de Notificaciones por Correo Electrónico:

    Una nueva función de registro está disponible para todas las notificaciones por correo electrónico. Los usuarios ahora pueden revisar un historial de notificaciones enviadas, lo que facilita verificar las entregas y solucionar problemas si los correos electrónicos no se reciben.
*   #### Soporte para Facturas Electrónicas: e-SLOG 1.6 y 2.0:

    Se ha introducido soporte para formatos adicionales de facturas electrónicas. El sistema ahora puede procesar y generar las versiones e-SLOG 1.6 y 2.0, ampliando la compatibilidad con socios y requisitos regulatorios.
*   #### Mejoras en la Detección de Duplicados:

    La detección de duplicados se ha mejorado con dos opciones de configuración potentes. El **Intervalo de Detección de Duplicados** le permite definir un rango de tiempo para verificar duplicados de manera más precisa, mientras que la configuración **No Permitir Exportar Duplicados** evita automáticamente la exportación de documentos detectados como duplicados. Juntas, estas mejoras brindan más control y garantizan una mayor precisión de los datos.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FXHRKTmuSxTlDt9lDEkE7%252Fimage.png%3Falt%3Dmedia%26token%3D96b56af6-c644-4b0f-a488-8bc16a03c11f\&width=768\&dpr=4\&quality=100\&sign=9b723b7f\&sv=2)
*   #### Mejoras en Árboles de Decisión:

    Los árboles de decisión son ahora más versátiles, con la capacidad de devolver valores de campos de documentos. Esto permite una lógica de automatización más avanzada, lo que permite a los flujos de trabajo tomar decisiones basadas en datos reales de documentos.
*   #### Nuevas Tarjetas de Flujo de Trabajo:

    Dos nuevas tarjetas de flujo de trabajo amplían las capacidades de automatización. La primera le permite verificar si un documento pertenece a una suborganización específica, lo que facilita el manejo de configuraciones multi-entidad. La segunda introduce una verificación de tolerancia de fecha de entrega, que compara las fechas de entrega con la fecha actual en días laborables para ayudar a gestionar y hacer cumplir los requisitos de entrega de manera más efectiva.
*   #### Mejoras en la Exportación CSV:

    La función de exportación CSV se ha mejorado significativamente. En lugar de exportar solo los documentos mostrados en la página actual, el sistema ahora exporta todos los documentos en un conjunto de datos. Cada exportación crea una entrada de registro, y el CSV resultante se envía automáticamente por correo electrónico, lo que proporciona un proceso de exportación más completo y confiable.
*   #### Marco de Tiempo para Eliminación de Órdenes de Compra:

    Una nueva opción de configuración permite a los administradores definir un marco de tiempo para la eliminación de órdenes de compra. Esta mejora añade flexibilidad y control sobre las políticas de retención de datos, asegurando que las órdenes de compra solo se eliminen cuando sea apropiado.

### Correcciones de Errores

* Se corrigió un problema donde se incluían datos antiguos al exportar documentos.
* Se corrigió el filtro para Errores de Exportación, que anteriormente mostraba también otros estados.
* Se resolvió una discrepancia de validación de tabla donde "Precio Unitario" provocaba errores pero "Precio Unitario Por" no, a pesar de que los valores eran correctos.
* Se corrigió un problema donde agregar una nueva columna al panel de control fallaba.
* Se corrigió un problema donde las tareas no eran visibles en la columna de tareas del panel de control.
* Se corrigió el comportamiento de ordenación aleatoria para que las listas sigan ahora un orden consistente.
* Se resolvió un problema donde no se podía detener el cambio de tamaño de columna.
* Se corrigió un error que impedía la coincidencia manual de líneas en la pantalla de Coincidencia de Órdenes de Compra.
* Se corrigió un problema donde la opción de adjuntar correo electrónico se restablecía después de guardar.
* Se corrigió un problema donde la contabilidad automática mostraba inicialmente IDs de base de datos al abrirse por primera vez.
* Se corrigió el comportamiento de campo difuso para que los valores ya no se sobrescriban incorrectamente.
* Se corrigió un problema donde los campos en la cuenta automática desaparecían después de eliminar el contenido.
* Se corrigió un error donde el usuario no podía cambiar el nombre de "Nombre" y "Apellido" en el cuadro de configuración.
* Se resolvió un problema donde los documentos podían quedar atascados en "flujo de trabajo en progreso."
* Se corrigió un problema de color de icono de menú donde los colores de organización seleccionados no se aplicaban correctamente.
* Se corrigió un problema donde a veces los códigos QR no eran reconocidos.
* Se corrigió un problema donde las cuentas no se podían eliminar con retroceso para ingresar una diferente.
* Se resolvió una confusión de idioma después de iniciar sesión tras la actualización de producción.

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
