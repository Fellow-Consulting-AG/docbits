# Búsqueda de datos maestro

## Descripción general

La "Búsqueda de datos maestro" en tus Ajustes de Procesamiento de documentos permite un enfoque integral e integrado para gestionar y validar los datos de tus documentos sincronizándolos con tu sistema Infor ERP. Así ayuda a agilizar la validación y la mejora del procesamiento de documentos dentro de tu entorno ERP:

1. **Gestión de datos centralizada**: Esta función actúa como un repositorio central donde se pueden almacenar y gestionar datos de diversas fuentes como proveedores, direcciones de clientes, códigos fiscales y más. Proporciona un único punto de referencia para todos los datos maestros, garantizando la coherencia y la exactitud en toda tu organización.
2. **Validación contra los datos del ERP**: Al sincronizar datos maestros como la información de proveedores desde Infor a DocBits, puedes validar automáticamente los datos extraídos de los documentos contra los datos de tu ERP. Esto garantiza que la información procesada (como nombres de proveedores, direcciones y códigos fiscales) coincida con los datos almacenados en tu sistema ERP, minimizando errores y discrepancias.
3. **Facilita la automatización**: Contar con un sistema sólido de búsqueda de datos maestro ayuda a automatizar el procesamiento de documentos entrantes. Por ejemplo, las órdenes de compra o las facturas pueden verificarse automáticamente para comprobar la corrección de los datos del proveedor, aprobarse si coinciden o marcarse para revisión si se encuentran discrepancias.
4. **Mejora la integridad de los datos**: Las actualizaciones periódicas desde tu sistema ERP hacia la búsqueda de datos maestro aseguran que los datos usados para el procesamiento de documentos estén actualizados. Esto reduce el riesgo de procesar documentos basados en información desactualizada, mejorando así la integridad general de las transacciones comerciales.
5. **Eficiencia en el procesamiento de documentos**: Con los datos maestros vinculados directamente y actualizándose constantemente, el procesamiento de documentos se vuelve más eficiente. Los documentos pueden clasificarse y enrutarse automáticamente según los criterios específicos definidos en los datos maestros, como condiciones particulares de proveedores o normativas fiscales aplicables a distintos tipos de transacciones.

{% hint style="info" %}
Consulta aquí cómo [Importar datos maestros](../../../infor-integration-and-configuration/importing-customer-master-data/)
{% endhint %}

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/master_data_lookup_1.png)

## **Acceso a Búsqueda de datos maestro**

Para acceder a la sección de **Búsqueda de datos maestro**, navega a:\
**Ajustes → Procesamiento de documentos → Búsqueda de datos maestro**

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_mater_data_lookup.png)

## **Ajustes**

Para acceder a los ajustes de **Búsqueda de datos maestro**, haz clic en **Ajustes** ubicado en la esquina inferior izquierda de la pantalla de **Búsqueda de datos maestro**.\
Las siguientes opciones de configuración están disponibles:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/master_data_lookup_2.png)

### **Proveedor BOD**

* **Permitir la sincronización de varias cuentas de proveedores**:
  * **Habilitado**:\
    Un único proveedor puede tener múltiples elementos `<FinancialParty>` en el BOD (Business Object Document), a menudo debido a varios IBAN o cuentas financieras asociadas. Cuando este ajuste está habilitado, todas las entradas `<FinancialParty>` del proveedor se extraerán y guardarán en la tabla de proveedores, permitiendo almacenar múltiples atributos financieros.
  * **Deshabilitado**:\
    Solo se extraerá el último elemento `<FinancialParty>` encontrado para el proveedor en el BOD. Cualquier atributo financiero previo (p. ej., IBAN adicionales) será ignorado y solo los datos de la última ocurrencia se guardarán en la tabla de proveedores.

### **Eliminación de orden de compra**

*   **Eliminar orden de compra después**: Especifica cuándo deben eliminarse las órdenes de compra cerradas. Transcurrido el período seleccionado, los registros se eliminarán automáticamente.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/master_data_lookup_3.png)
