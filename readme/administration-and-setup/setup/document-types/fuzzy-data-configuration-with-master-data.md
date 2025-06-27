# Configuración de Datos Difusos con Datos Maestros

## **Visión General**

Cada tipo de documento tiene sus propias configuraciones predeterminadas y deben configurarse por separado. Mientras este ejemplo explica la configuración para **Facturas**, el mismo proceso se aplica a todos los tipos de documentos.

## Para configurar Datos Difusos, navega a:

Configuración → Configuración Global → Tipos de Documento → Factura → Campos → Configuración de Datos Maestros → Buscar Datos Maestros

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fhnn2NcPGzVkUO0mLQWTy%252Fimage.png%3Falt%3Dmedia%26token%3De2f87385-fc48-4149-9bef-ca917a7328bd\&width=768\&dpr=4\&quality=100\&sign=116ee1da\&sv=2)

## **Búsquedas Predeterminadas**

Hay **cuatro grupos de búsqueda predeterminados** para las facturas:

1. **Datos de la Empresa**
2. **Encabezado de Orden de Compra**
3. **Proveedor**
4. **Código de Impuesto**

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F4VxYFu8M62dXi6qGsPl3%252Fimage.png%3Falt%3Dmedia%26token%3Db2bc4690-805b-4b19-aa89-73f315889d88\&width=768\&dpr=4\&quality=100\&sign=835f513a\&sv=2)

Cada grupo contiene campos específicos. Haz clic en un grupo para **expandirlo** y ver los campos. Los grupos de búsqueda predeterminados están etiquetados con una etiqueta de **"Predeterminado"**.

## **Estado de Configuración de Búsqueda**

* Las **configuraciones activas** están marcadas con una etiqueta de **"Activado"**.
* Las **configuraciones desactivadas** están marcadas con una etiqueta de **"Desactivado"**.

## **Prerrequisito: Importar Datos Maestros**

Para que los Datos Difusos funcionen correctamente, los **datos maestros** relevantes deben ser importados. Sin esto, el sistema no tiene datos de referencia para usar. Aquí tienes cómo importar datos maestros:

{% content-ref url="../../../infor-integration-and-configuration/importing-customer-master-data/" %}
[importing-customer-master-data](../../../infor-integration-and-configuration/importing-customer-master-data/)
{% endcontent-ref %}

## **Gestionar Grupos de Búsqueda**

Cada grupo de búsqueda está **activado por defecto** pero se puede modificar haciendo clic en los tres puntos:

* **Desactivar** → Desactiva un grupo. _(Solo disponible para grupos activados)_
* **Activar** → Activa un grupo. _(Solo disponible para grupos desactivados)_
* **Duplicar** → Crea una copia que se puede modificar sin afectar el original.
* **Ver** → Muestra información como el **tipo de documento** al que pertenece y la **tabla de búsqueda** que utiliza. _(Solo disponible para grupos predeterminados)_
* **Editar** → Disponible para grupos **no predeterminados**. Permite modificar los detalles del grupo.
* **Eliminar** → Elimina el grupo por completo. _(Solo para grupos no predeterminados)_

## **Crear una Nueva Configuración de Búsqueda**

Hay **dos formas** de crear una configuración de búsqueda:

1.  **Duplicar una búsqueda existente**

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FZUlPcWGrx1oITQS3tgZP%252Fimage.png%3Falt%3Dmedia%26token%3D59fb300d-836e-40d0-84b7-4a405cf7f321\&width=768\&dpr=4\&quality=100\&sign=3442db8f\&sv=2)

    * Esto copia toda la información y campos de un grupo existente.
    * Solo necesitas proporcionar un **nuevo nombre**.
2.  **Crear una búsqueda desde cero**

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FNbEpo2p5Q8D1d7DUchBF%252Fimage.png%3Falt%3Dmedia%26token%3D401314b5-44d0-47df-b3e6-69fea83cce82\&width=768\&dpr=4\&quality=100\&sign=1d0ce322\&sv=2)

    * Haz clic en **"Crear Configuración de Búsqueda"**.
    * Completa los detalles requeridos:
      * **Nombre de Configuración**
      * **Tabla de Búsqueda** (Tabla de Datos Maestros a utilizar)
      * **Manejador de Conflictos** (Elige uno: Mejor Puntuación, No Devolver, Devolver Primero)
      * **Tipo de Contexto** (Encabezado o Línea) necesita contexto
      * **Coincidir Todo** (Opción de casilla de verificación) necesita contexto

## **Gestionar Campos Dentro de un Grupo de Búsqueda**

Cada grupo contiene campos que se pueden **añadir, eliminar, editar o ver**, dependiendo de si son campos predeterminados o campos personalizados.

### **Campos Predeterminados**

*   Marcados con una etiqueta de **"Predeterminado"**.

    <div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fh37McVpB0tBo5wqiAttR%252Fimage.png%3Falt%3Dmedia%26token%3Dcabce083-83a5-4881-a64f-88a8757df49b&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=b3739019&#x26;sv=2" alt="" width="375"></div>
* **Solo se pueden ver**, no editar ni eliminar.

### **Campos No Predeterminados**

* **Se pueden editar o eliminar** haciendo clic en los tres puntos y seleccionando **Editar** o **Eliminar**.

### **Añadir un Nuevo Campo**

**Nota:** Puedes crear campos dentro de configuraciones de Búsqueda predeterminadas.

Para añadir un nuevo campo dentro de un grupo:

1.  Haz clic en **"Crear"** dentro del grupo relevante.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FvmIXTEQQHKKNbvTJj1b4%252Fimage.png%3Falt%3Dmedia%26token%3D8569867b-9f5b-4865-90bd-f2e41e846979\&width=768\&dpr=4\&quality=100\&sign=603cb7df\&sv=2)
2. Proporciona los siguientes detalles:
   * **Campo de Búsqueda** → Nombre de columna de la tabla de búsqueda de datos maestros.
   * **Campo de Validación** → Campo de DocBits correspondiente.
   * **Campo Padre** → _(Se necesitan más detalles)_
   * **Operador de Búsqueda** → Elige uno:
     * Inteligente
     * Contiene
     * Exacto
     * Comienza con
     * Termina con
   * **Casillas de Verificación:**
     * **Disparador Automático** → Cuando está habilitado, si otro campo en una configuración de búsqueda diferente comparte la misma columna, este campo se actualizará **automáticamente** cada vez que se actualice el otro campo.
     * **Buscable** → Habilita el campo como un campo de **Datos Difusos**, permitiendo búsquedas en la búsqueda de datos maestros (ícono azul en la pantalla de validación).

## **Paso Final: Añadir Campos al Diseño**

Después de configurar los campos de Datos Difusos, **asegúrate de añadirlos al diseño usando el Constructor de Diseño**. Si los campos no se añaden al diseño, no estarán disponibles para su uso.

{% content-ref url="../../settings/global-settings/document-types/layout-manager/" %}
[layout-manager](../../settings/global-settings/document-types/layout-manager/)
{% endcontent-ref %}
