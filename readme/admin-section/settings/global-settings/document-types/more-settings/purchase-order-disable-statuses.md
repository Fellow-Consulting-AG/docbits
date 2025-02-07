# Estados de desactivación de órdenes de compra

### **Configuración para desactivar estados de OC**

Ir a **Ajuste → Ajuste General → Tipos de Documentos → Más Configuraciones → Sección de Órdenes de Compra → Estados de Desactivación de OC**

#### **Cómo Funciona**

La configuración de **Estados de PO Deshabilitados** permite a los usuarios especificar los estados de las órdenes de compra (PO) que impiden que las facturas se emparejen con esas POs. Si una orden de compra tiene un estado listado en esta configuración, **no se puede** utilizar para el emparejamiento de facturas en la pantalla de emparejamiento de PO, deteniendo el procesamiento adicional de las facturas relacionadas hasta que el estado de la PO cambie a uno que no esté deshabilitado.

Al utilizar esta configuración, los usuarios pueden asegurarse de que las órdenes de compra con estados específicos no sean sometidas a un procesamiento adicional de facturas, reduciendo errores y evitando pagos innecesarios.

#### **Cómo Identificar una Orden de Compra Desactivada**

En la pantalla de **Emparejamiento de OC**, una orden de compra desactivada aparece **tachada**. Esto indica visualmente que la OC está actualmente restringida para ser emparejada debido a su estado.

​

![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FT2n2w4uDCJvv7CJ5zrdk%2Fuploads%2FDbA2CsBn6twgp5BrSvgV%2Fimage.png?alt=media\&token=211bd6a2-4136-4ea0-85cf-e17f428fa0da)

#### **Cómo Configurarlo**

* En la configuración de **Estados de Desactivación de OC**, verás un campo de selección en el lado izquierdo.
*   Hacer clic en este campo abre una lista desplegable de estados de OC disponibles.

    ​

    <div align="left"><img src="https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FT2n2w4uDCJvv7CJ5zrdk%2Fuploads%2FgvmAKBrVLXhDwKe7RIBe%2Fimage.png?alt=media&#x26;token=0f98186b-3f50-483c-8465-a75972e9386a" alt=""></div>

    ​
* Selecciona uno o más estados haciendo clic en ellos. Haz clic nuevamente para deseleccionar.
* Haz clic en el botón **Aplicar** para guardar tus cambios.

![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FT2n2w4uDCJvv7CJ5zrdk%2Fuploads%2F5FCyl2giTsZeu8487ai9%2Fimage.png?alt=media\&token=5e7c0ee4-1629-44e0-a4c5-056d7efa320f)

**Estados Disponibles**

* Cancelado
* Eliminado
* Facturado
* Abierto
* Parcialmente Facturado
* Parcialmente Recibido
* Recibido
* No Aprobado
* En Espera
* Cerrado
