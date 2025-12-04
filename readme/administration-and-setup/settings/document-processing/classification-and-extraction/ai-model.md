# Modelo de IA

## Descripción general

La configuración del **Modelo de IA** te permite definir qué modelo de IA se utiliza de forma predeterminada para la **extracción de campo** y la **extracción de tabla** durante el procesamiento de documentos.\
En esta sección, puedes revisar el costo de tokens para cada modelo y ver qué modelo está actualmente asignado a cada proveedor.

## Cómo acceder

1.  Navega a **Configuración** → **Procesamiento de documentos** → **Clasificación y extracción**

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_classification_and_extraction.png)
2.  Desplázate hacia abajo hasta la sección de **Extracción de tabla**

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_1.png)

## Opciones del Modelo de IA

Puedes elegir entre los siguientes modelos de IA. Pasa el cursor sobre el icono de información en la interfaz para ver el costo de tokens por documento para el modelo de IA seleccionado:

* **Full** – 2 tokens por documento
* **Fast** – 1 token por documento
* **Turbo** – 1 token por documento

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_2.png)

## Tabla de Asignación del Modelo de IA

También puedes configurar **modelos de IA** específicos por proveedor directamente en la pantalla de **Validación**, lo que te permite ajustar la precisión de extracción para proveedores individuales.\
\
Para más información, consulta la documentación correspondiente [aquí](../../../../end-user-and-partner-section/end-user-section/validation-screen/selecting-a-supplier-specific-ai-model-for-field-and-table-extraction.md).

La tabla de asignación muestra la configuración del modelo de IA para cada proveedor e incluye los siguientes detalles:

* **Supplier ID** – El identificador único del proveedor
* **AI Model** – El modelo de IA actualmente asignado al proveedor
* **E-Text**: Indica si la función E-Text está habilitada
* **Action** – Contiene la opción para eliminar la entrada

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_3.png)

### Eliminar entrada – Restablecer configuración específica del proveedor

Para restablecer la configuración del modelo de IA de un proveedor al valor predeterminado:

1.  Haz clic en el icono de la papelera en la columna **Action** junto a la entrada del proveedor.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_4.png)
2.  Aparecerá un cuadro de diálogo de confirmación—confirma que deseas eliminar la entrada.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_5.png)

Una vez eliminada, el proveedor volverá a utilizar el **modelo de IA** predeterminado para la **extracción de campo** y la **extracción de tabla**.
