# Lista de valores

## Descripción general

La función de **Lista de valores** te permite crear y gestionar conjuntos de valores predefinidos. Esto es particularmente útil para configurar menús desplegables en la sección de [**Campos**](../global-settings/document-types/fields/), que luego pueden ser utilizados en la **Validación de campos**.

Estas listas pueden ser personalizadas para diferentes sub-organizaciones y soportan múltiples idiomas, proporcionando flexibilidad a través de **DocBits**.

## ¿Cómo acceder?

Puedes acceder a la **Lista de valores** navegando a **Ajustes → Procesamiento de documentos → Lista de valores**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_list_of_values.png)

## ¿Cómo añadir o eliminar una lista?

### Crear una nueva lista de valores

1.  Haz clic en **Nuevo** en la esquina superior derecha de la pantalla.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_1.png)
2. Ingresa un **Nombre** para tu lista.
3. _(Opcional)_ Selecciona una **Sub-organización** para la cual la lista debería estar activa.
4.  Haz clic en **Guardar** para crear la lista.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_2.png)

### ¿Cómo eliminar una lista?

Para eliminar una lista, haz clic en el ícono de la papelera junto a la lista correspondiente.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_13.png)

<mark style="color:red;">**Nota**</mark>: La lista se eliminará inmediatamente. Las listas marcadas con la etiqueta [**Estándar**](list-of-values.md#listas-y-filas-definidas-por-el-sistema) no pueden ser eliminadas.

## ¿Cómo añadir, editar o eliminar valores de una lista existente?

Puedes gestionar valores en una **Lista de valores** existente utilizando uno de los siguientes métodos:

* [**Añadir valores manualmente**](list-of-values.md#anadir-valores-manualmente) – Ingresa valores individualmente a través de la interfaz.
* [**Importar valores desde un archivo CSV**](list-of-values.md#importar-valores-desde-un-archivo-csv) – Carga un archivo CSV para añadir múltiples valores a la vez.

### Añadir valores manualmente

1.  Haz clic en la lista que deseas modificar.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_3.png)
2.  Haz clic en **Comportamiento**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_4.png)
3.  Haz clic en **Añadir fila**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_5.png)

Ahora puedes especificar múltiples propiedades para cada entrada:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_6.png)

**Valor**: Así es como el elemento se almacenará internamente dentro de **DocBits**. Permanece igual en todos los idiomas y también sirve como el texto de visualización por defecto durante la validación de campos si no se especifica ninguna etiqueta para el idioma seleccionado.

**Etiqueta**: Este es el texto que se muestra en la pantalla de validación, basado en el idioma seleccionado. Si no hay etiqueta disponible para el idioma activo en DocBits, el sistema mostrará por defecto el **Valor**.

**Idioma**: Especifica el idioma en el cual se mostrará la etiqueta.\
Una explicación más detallada se puede encontrar [aquí](list-of-values.md#anadir-traducciones-a-tus-valores).

**Sub-organizaciones**: Especifica para qué **sub-organización** la fila debería estar activa. Si se deja en blanco, la fila estará disponible para todas las organizaciones.

**Sinónimos**: Aquí puedes especificar valores adicionales que ayudan a entrenar tu documento.\
Por ejemplo, si **EUR** es tu **valor** principal, puedes añadir EURO y € como **sinónimos**. Cuando el documento se entrena utilizando cualquiera de estos **sinónimos**, **DocBits** reconocerá y seleccionará automáticamente EUR como el valor correspondiente de tu lista.\
<mark style="color:red;">**Nota**</mark>: Cada sinónimo debe ser confirmado presionando **Enter** para añadirlo a la lista.

4.  Después de ingresar todas las propiedades deseadas, haz clic en el botón **Guardar** para añadir la fila.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_11.png)

### Importar valores desde un archivo CSV

Para añadir múltiples valores a la vez mediante la importación de CSV:

1.  Haz clic en la lista que deseas actualizar.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_3.png)
2.  Haz clic en **Comportamiento**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_4.png)
3.  Haz clic en **Cargar CSV**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_7.png)
4. Haz clic en **Archivo** para buscar y seleccionar el archivo CSV que deseas cargar.
5. Elige el **Delimitador** apropiado utilizado en el archivo CSV (`;` o `,`).
6.  Haz clic en **Subir** para importar los valores.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_8.png)

### Editar valores existentes

1. Localiza la fila que deseas editar.
2. Haz clic en los tres puntos en la columna de **Comportamiento**.
3.  Selecciona **Editar** del menú desplegable.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_10.png)
4. Realiza los cambios requeridos.
5.  Haz clic en **Guardar** para aplicar tus cambios.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_11.png)

### Eliminar valores

1. Localiza la fila que deseas eliminar.
2. Haz clic en los tres puntos en la columna de **Comportamiento**.
3.  Selecciona **Borrar** del menú desplegable.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_12.png)

<mark style="color:red;">**Nota**</mark>: La fila se eliminará inmediatamente. Las filas marcadas con la etiqueta [**Defecto**](list-of-values.md#listas-y-filas-definidas-por-el-sistema) no pueden ser eliminadas.

## Añadir traducciones a tus valores

Puedes añadir tantas traducciones como idiomas soportados en **DocBits**.

Para añadir una traducción:

1.  Haz clic en el ícono de más (+).

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_14.png)
2.  Selecciona un idioma del menú desplegable.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_15.png)
3.  Ingresa la traducción deseada en el campo **Etiqueta**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_16.png)
4.  Para añadir otra traducción, haz clic en el ícono de más (+) nuevamente.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_17.png)
5.  Para eliminar una traducción, haz clic en el ícono de la papelera.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_18.png)
6.  Cuando termines, haz clic en el botón **Guardar** para guardar tus traducciones.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_19.png)

<mark style="color:red;">**Nota**</mark>: Si no hay **Etiqueta** disponible para el idioma activo, DocBits mostrará por defecto el **Valor**.

## Listas y filas definidas por el sistema

Algunas listas son pre-creadas por el sistema y están marcadas con la etiqueta **Estándar**. Estas listas no pueden ser eliminadas, pero puedes añadir nuevas filas a ellas y eliminar esas filas recién añadidas si es necesario.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_9.png)

Dentro de estas listas estándar, ciertas filas están marcadas con la etiqueta **Defecto**—estas son entradas definidas por el sistema. Puedes añadir nuevas **etiquetas** en diferentes idiomas, pero estas filas por defecto no pueden ser eliminadas.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_20.png)
