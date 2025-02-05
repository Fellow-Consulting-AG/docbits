# eSLOG 1.6 y 2.0

## Versiones de Factura eSLOG Soportadas

Actualmente, **se soportan las versiones de factura eSLOG 1.6 y 2.0**.

Para la documentación oficial de eSLOG, puedes consultar [este enlace](https://epos.si/en/eslog).

Ambas versiones de eSLOG están habilitadas por defecto.

## Pasos para Modificar la Configuración de eSLOG

**Configurar eSLOG:**

* Navega a **Ajustes → Ajustes Global → Tipos de Documentos → Factura**.
*   Haz clic en **E-Doc**.\


    <figure><img src="../../../../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>
* Aparecerá una lista de todos los e-docs disponibles.
*   Localiza la versión de eSLOG que deseas modificar.\


    <figure><img src="../../../../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

### **Configuración de Transformación y Ruta XML:**

En la **configuración de transformación**, puedes definir la ruta para localizar información específica dentro del archivo XML y guardarla en una nueva estructura, facilitando el acceso a los datos. **Nota:** Si utilizas esta funcionalidad, debes usar las nuevas rutas XML creadas, no las rutas XML originales, en la **Vista Previa** y en la **Ruta de Extracción**.

#### **Pasos para Modificar el Archivo de Transformación:**

1. Abre la **Transformación**.
2. Crea un nuevo borrador haciendo clic en el **icono de lápiz**.
3. Selecciona el borrador recién creado.
4. Crea un nuevo campo o modifica uno existente.
5. Establece la ruta deseada para la extracción de datos.
6. Haz clic en **Guardar**.

### Configuración de Vista Previa PDF

La **Configuración de Vista Previa PDF** se utiliza para generar una versión legible por el usuario del documento. Puedes personalizarla con HTML para adaptarla a tus necesidades.

#### **Pasos para Modificar el Archivo de Vista Previa:**

1. Abre la **Vista Previa**.
2. Crea un nuevo borrador haciendo clic en el **icono de lápiz**.
3. Selecciona el borrador recién creado.
4. Crea un nuevo campo o modifica uno existente.
5. Establece la ruta deseada para la extracción de datos.
6. Haz clic en **Guardar**.

### Configuración de Rutas de Extracción

La **Configuración de Rutas de Extracción** se utiliza para extraer datos y llenar campos en la **pantalla de validación**, como la tabla de facturas o campos configurados en el diseño de la factura.

#### **Pasos para Modificar las Rutas de Extracción**:

1. Abre las **Rutas de Extracción**.
2. Crea un nuevo borrador haciendo clic en el **icono de lápiz**.
3. Selecciona el borrador recién creado.
4. Crea un nuevo campo o modifica uno existente.
5.  El lado izquierdo representa el **ID de campo de DocBits**, que se puede encontrar en **Configuración → Configuración Global → Tipos de Documentos → Factura → Campos**.\
    \


    <figure><img src="../../../../../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>
6. El lado derecho representa la **ruta al campo** creado en la Transformación.
7. Haz clic en **Guardar**.
