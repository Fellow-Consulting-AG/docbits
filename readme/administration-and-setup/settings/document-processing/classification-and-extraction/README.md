# Clasificación y extracción

## Descripción general

En los ajustes de **Clasificación y extracción**, puedes:

* Habilitar **División de documentos** basada en códigos QR
* Configurar **Formato de cantidad**
* Configurar **Extracción de tabla**
* Activar/desactivar el procesamiento de archivos **ZUGFeRD** no admitidos
* Definir reglas de clasificación especiales
* Supervisar **Modelos de IA** entrenados a medida utilizados en el proceso de clasificación

Esta página proporciona una explicación detallada de todos los ajustes disponibles.

## **Acceder a los Ajustes de Clasificación y extracción**

Para acceder a los ajustes de **Clasificación y extracción**, ve a:\
**Ajustes → Procesamiento de documentos → Clasificación y extracción**

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_classification_and_extraction.png)

## División de documentos

En la sección de **División de documentos**, puedes configurar si un documento cargado debe dividirse en varios documentos cuando aparezca un **Código de barras** en una de sus páginas.

Para activar esta función:

1. Ve a la sección **División de documentos**.
2.  Abre el menú desplegable.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_14.png)
3.  Selecciona **Dividido por código de barras/código QR**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_15.png)

Luego tendrás la opción de:

* Seleccionar uno o más tipos de código de barras que se deben detectar.
*   Especificar un patrón regex con el que el código de barras debe coincidir para activar la división de documentos.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_16.png)

## Formato de cantidad

En la sección **Formato de cantidad**, tienes dos opciones:

* **Permitir redondeo durante la comparación de importes:**\
  Si está habilitado, se permite una tolerancia de ±0.5 durante la comparación de importes.\
  Si está deshabilitado, se aplica una tolerancia predeterminada de ±0.05.
* **Requerir coincidencia exacta para comparación de montos:**\
  Si está habilitado, los importes deben coincidir exactamente con tolerancia cero.\
  Si está deshabilitado, se permite una tolerancia de ±0.05.

<mark style="color:red;">**Nota**</mark>: Solo uno de estos ajustes puede estar activo a la vez.

## Extracción de tabla

Puedes extraer tablas de documentos habilitando **Extracción de tabla** o **Extracción de mesa de IA**. Una tabla entrenada —ya sea con IA o manual— siempre estará vinculada a un proveedor específico.

**Extracción de tabla:** Activa la **extracción de tabla** manual. Las tablas deben entrenarse manualmente.\
Obtén más información sobre el entrenamiento manual [aquí](../../../setup/document-training/training-line-fields-table-training/defining-tables-and-columns.md).

**Extracción de mesa de IA:** Utiliza IA para extraer tablas automáticamente. Si los resultados no son lo suficientemente precisos, se recomienda cambiar a **Extracción de tabla** manual para un mejor control y entrenamiento.

**Extracción de tablas para el cálculo de costes:** Cuando está habilitado, DocBits puede extraer elementos de coste de las tablas a nivel de línea y clasificarlos en consecuencia.\
Explicación detallada disponible [aquí](table-extraction-for-costing-element.md).

**Extraer automáticamente el código fiscal:** Cuando está habilitado, el sistema completa automáticamente el campo **Código fiscal** en la pantalla de validación, siempre que se haya configurado un campo de código fiscal.\
Más información sobre este ajuste [aquí](auto-extract-tax-code.md).

**Modelo de IA:** Permite especificar qué **Modelo de IA** se utiliza para la extracción de tablas.\
También verás una tabla que muestra:

* Qué **Proveedores** están utilizando qué Modelo de IA
* Si usan E-Text
* Opciones para borrar una entrada o restablecer los datos de entrenamiento

Este ajuste se explica en detalle [aquí](ai-model.md).

## Documento electrónico

**Procesar ZUGFeRD PDF no admitido:** Si está habilitado, las versiones de **ZUGFeRD** no admitidas se procesarán como PDF estándar y se ignorará el XML incrustado.

La lista de versiones de **ZUGFeRD** compatibles se encuentra [aquí](../../global-settings/document-types/edi/zugferd-1.0-2.1-and-2.3.md).

## **Reglas de clasificación**

En la sección **Reglas de clasificación**, puedes definir patrones **regex** y criterios específicos para ayudar al sistema a clasificar documentos automáticamente durante el procesamiento.

Para acceder a esta sección, haz clic en la pestaña **Reglas de clasificación** en la parte superior de la página.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_1.png)

### **Agregar una nueva regla de clasificación**

Para crear una nueva regla:

1.  Haz clic en **Agregar** en la esquina superior derecha.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_2.png)
2. Completa los siguientes campos:
   * **Patrón**: El patrón regex que el sistema debe buscar para activar la clasificación.
   * **Tipo**: Dónde se debe buscar el patrón (por ejemplo, **Código de barras**).
   * **Suboficial** _(opcional)_: Especifica a qué sub organización se aplica la regla.
   * **Tipo de Documento**: Define el tipo de documento que se asignará cuando el patrón coincida.
   *   **Tipo de documento subconsportado** _(opcional)_: Especifica un subtipo para una clasificación más detallada.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_3.png)
3.  Haz clic en **Guardar** para guardar tu regla de clasificación.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_4.png)

### **Editar una regla de clasificación**

Para editar una regla existente:

1.  Haz clic en los tres puntos en la columna **Comportamiento**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_5.png)
2.  Selecciona **Editar**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_6.png)
3. Realiza los cambios deseados.
4.  Haz clic en **Guardar** para aplicar las actualizaciones.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_4.png)

### **Borrar una regla de clasificación**

Para borrar una regla:

1.  Haz clic en los tres puntos en la columna **Comportamiento**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_5.png)
2.  Selecciona **Borrar**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_7.png)

## Modelos de IA

La sección **Modelos de IA** muestra todos los modelos entrenados a medida que se han ajustado específicamente a tus necesidades.

### Acceder a la sección Modelos de IA

Para abrir esta sección, haz clic en la pestaña **Modelos de IA** ubicada en la parte superior de la página.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_8.png)

### Categorías de modelos

Los modelos están organizados en categorías. Debajo de cada nombre de categoría se muestra la cantidad de modelos que contiene.\
Haz clic en una categoría para ver sus detalles.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_9.png)

En la parte superior de la página de la categoría seleccionada, verás información clave sobre cada modelo:

* **Tipo**: El tipo de modelo.
* **Primera página solamente**: Indica si el modelo procesa solo la primera página de un documento.
* **Version**: El número de versión del modelo.

### Tabla de modelos

Todos los modelos dentro de una categoría se enumeran en una tabla, que incluye la siguiente información:

* **Nombre**: El nombre del modelo.
* **Siguiente modelo**: El modelo que procesará posteriormente la salida del modelo actual.
* **Tipo de Documento**: El tipo de documento principal asignado por el modelo durante la clasificación.
* **Subtubos de documentos**: Los subtipos en los que se clasifica adicionalmente el documento.
* **Prioridad**: El nivel de prioridad que determina la posición del modelo en la cola de clasificación.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_11.png)

### Editar un modelo

Para editar un modelo:

1.  Haz clic en el icono del lápiz en la columna **Comportamiento** junto al modelo que deseas editar.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_10.png)
2. Actualiza los campos disponibles:
   * **Siguiente modelo**: Selecciona el modelo que debe procesar la salida del modelo actual.
   * **Tipo de Documento**: Elige el tipo de documento con el que el modelo debe clasificar la entrada.
3.  Haz clic en **Guardar** para aplicar tus cambios.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_12.png)
