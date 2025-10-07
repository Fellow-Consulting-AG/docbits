# ZUGFeRD 1.0, 2.1 y 2.3

## **Versiones compatibles de ZUGFeRD**

Las versiones actualmente compatibles de ZUGFeRD son:

* **1.0**
* **2.1** (compatible con FACTUR-X 1.0.05)
* **2.3** (compatible con FACTUR-X 1.07.2)

#### Activación y modificación del estándar

El estándar ZUGFeRD está siempre activo de forma predeterminada, pero puedes hacerle modificaciones si es necesario.

### **Pasos para modificar los Ajustes de ZUGFeRD:**

1. Ve a **Ajustes → Ajustes globales → Tipos de documentos → Factura**.
2.  Haz clic en **E-Doc**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/zugferd_1.png)
3. Aparecerá una lista de todos los e-docs disponibles.
4.  Ubica la versión de **ZUGFeRD** que deseas modificar.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/zugferd_2.png)

## **Extraction Transformation y Configuración de rutas XML:**

En los **ajustes de Extraction Transformation**, puedes definir la ruta para localizar información específica dentro del archivo XML y guardarla en una nueva estructura, facilitando el acceso a los datos.\
<mark style="color:red;">**Nota**</mark>: Si usas esta funcionalidad, debes usar las rutas XML recién creadas, no las rutas XML originales, en el **Preview** y **Extraction Path**.

### **Pasos para modificar el archivo de Extraction Transformation:**

1. Abre la **Extraction Transformation**.
2. Crea un nuevo borrador haciendo clic en el **icono de lápiz**.
3. Selecciona el borrador recién creado.
4. Crea un campo nuevo o modifica uno existente.
5. Establece la ruta deseada para la extracción de datos.
6. Haz clic en **Guardar**.

### Notas importantes:

* El **archivo de Preview** se usa solo para **FACTUR-X** y no para **ZUGFeRD**. ZUGFeRD usará el **PDF** original.

## Configuración de Preview PDF

La **Configuración de Preview PDF** se usa para generar una versión legible para el usuario del documento. Puedes personalizarla con HTML según tus necesidades.

### **Pasos para modificar el archivo de Preview:**

1. Abre el **Preview**.
2. Crea un nuevo borrador haciendo clic en el **icono de lápiz**.
3. Selecciona el borrador recién creado.
4. Crea un campo nuevo o modifica uno existente.
5. Establece la ruta deseada para la extracción de datos.
6. Haz clic en **Guardar**.

## Configuración de Extraction Paths

La **Configuración de Extraction Paths** se utiliza para extraer datos y completar campos en la **pantalla de validación**, como la tabla de factura o los campos configurados en el diseño de factura.

### **Pasos para modificar** **Extraction Paths**:

1. Abre **Extraction Paths**.
2. Crea un nuevo borrador haciendo clic en el **icono de lápiz**.
3. Selecciona el borrador recién creado.
4. Crea un campo nuevo o modifica uno existente.
5.  El lado izquierdo representa el **ID de campo de DocBits**, que se puede encontrar en **Ajustes → Ajustes globales → Tipos de documentos → Factura → Campos**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/zugferd_3.png)

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/zugferd_4.png)
6. El lado derecho representa la **ruta al campo** creado en la Extraction Transformation.
7. Haz clic en **Guardar**.

Siguiendo estos pasos, puedes garantizar una extracción de datos y una validación precisas para las facturas ZUGFeRD.
