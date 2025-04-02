# Layout Manager

<figure><img src="../../../../../.gitbook/assets/Bildschirmfoto%202024-05-08%20um%2008.46.24.png" alt=""><figcaption></figcaption></figure>

#### Visión general

El Gestor de Diseño permite a los administradores configurar y modificar visualmente el diseño de los tipos de documento al establecer propiedades para varios campos de datos y grupos dentro de un documento. Esta interfaz ayuda a garantizar que los modelos de extracción y los puntos de entrada de datos manuales se alineen precisamente con la estructura del documento escaneado o cargado en DocBits.

#### Componentes clave

1. **Grupos y Campos**:

* **Grupos**: Unidades organizativas dentro de un tipo de documento que categorizan campos relacionados (por ejemplo, Detalles de la Factura, Detalles de Pago). Estos pueden expandirse o contraerse y organizarse para reflejar el agrupamiento lógico en el documento real.
* **Campos**: Puntos de datos individuales dentro de cada grupo (por ejemplo, Número de Factura, Términos de Pago). Cada campo se puede personalizar para la captura, visualización y procesamiento de datos.

2. **Panel de Propiedades**:

* Este panel muestra las propiedades del campo o grupo seleccionado, permitiendo una configuración detallada, como:
* **Etiqueta**: La etiqueta visible para el campo en la interfaz de usuario.
* **Nombre del Campo**: El identificador técnico utilizado dentro del sistema.
* **Ancho del Elemento en Porcentaje**: Determina el ancho del campo en relación con el diseño del documento.
* **Índice de Pestaña**: Controla el orden de tabulación para la navegación.
* **Ejecutar Script al Cambiar**: Si se debe ejecutar un script cuando cambia el valor del campo.
* **Mostrar Etiqueta a la Izquierda**: Si la etiqueta se muestra a la izquierda del campo o encima de él.
* **Es Textarea**: Especifica si el campo debe ser un área de texto, que permite cantidades mayores de texto.
* **Seleccionar Tipo de Modelo**: Opción para seleccionar qué tipo de modelo manejará la extracción de este campo.
* **Longitud del Campo**: Longitud máxima de datos que se aceptarán en este campo.
* **Palabras Clave Prohibidas**: Palabras clave que no están permitidas dentro del campo.

3. **Vista Previa de la Plantilla**:

* Muestra una vista previa en tiempo real de cómo se verá el documento según la configuración de diseño actual. Esto ayuda a garantizar que el diseño coincida con la estructura real del documento y es vital para probar y refinar la configuración de procesamiento del documento.

{% @jira/embed url="https://fellowpro.atlassian.net/browse/DOCB-2490" %}
