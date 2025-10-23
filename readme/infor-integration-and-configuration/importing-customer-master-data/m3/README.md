# M3

## Importar un API Connection Template en Infor M3

Esta guía explica cómo importar un API Connection Template para configurar rápidamente ajustes clave para la integración con Infor M3. Usar un template te permite establecer una configuración de conexión predefinida, simplificando el proceso y asegurando consistencia.

<mark style="color:red;">**Nota**</mark>: Para la configuración detallada de áreas específicas como Auto Accounting, Supplier Integration, Purchase Orders o Table Extraction for costing elements, consulta la documentación correspondiente:

* [Contabilización automática](auto-accounting.md)
* [Proveedores y órdenes de compra](suppliers-and-purchase-orders.md)
* [Cómo importar todos los proveedores](how-to-import-all-suppliers.md)
* [Extracción de tablas para el elemento de costos](table-extraction-for-costing-element.md)

### **Descargar el template**

Antes de importar, descarga el connection template requerido usando el archivo de abajo:

### Importar template

#### Pasos para importar un Connection Template

1. **Accede a Infor ION Desk:**
   *   Navega a **InforOS** → **ION Desk** → **Connect** → **Connection Points**.

       ![](https://lh7-us.googleusercontent.com/ySRjNzMXFzwSOYKx9hnlKLPHPuXpmfTvRADBfV6cpT8ajiEUbS4oXpd9InhXG09mHLakhqBTJMH4yQJNG5z9RXmbAjh8YbuGhxnXSeooIH_r3RAGOvJE6Ok67ST_272zFfhB_TTFYg3b-NwFq0CAv2o)
2. **Importar el template:**
   *   Haz clic en el botón **Import**.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/m3_import_2.png)
   * Selecciona el **Template File** apropiado desde tu sistema local.
   *   Haz clic en **OK** para iniciar el proceso de importación.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/m3_import_3.png)
3. **Confirmación:**
   *   Si la importación se realiza correctamente, se mostrará un mensaje de confirmación.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/m3_import_4.png)
4. **Configuración posterior a la importación:**
   * Después de importar el template, puedes personalizar la configuración específica de la conexión según sea necesario.
   * No olvides importar o configurar tu **Service Account** para la autenticación y el control de acceso.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/m3_import_5.png)
