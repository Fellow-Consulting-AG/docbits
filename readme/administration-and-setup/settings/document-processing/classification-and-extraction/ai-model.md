# Modelo de IA

## Descripción general

La configuración del Modelo de IA te permite definir qué modelo de IA debe ser utilizado por defecto para **extracción de mesa de IA** durante el procesamiento de documentos. También puedes ver el costo de tokens para cada modelo y ver qué modelo está actualmente asignado a cada proveedor.

## Cómo acceder

1.  Navega a **Ajustes** → **Procesamiento de documentos** → **Clasificación y extracción**

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_classification_and_extraction.png)
2.  Desplázate hacia abajo hasta la sección de **Extracción de tabla**

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_1.png)

## Opciones del Modelo de IA

Puedes elegir entre los siguientes modelos de IA. Pasa el cursor sobre el ícono de información en la interfaz para ver el costo de tokens por documento para el modelo de IA seleccionado:

* **Full** – 2 tokens por documento
* **Fast** – 1 token por documento
* **Turbo** – 1 token por documento

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_2.png)

## Tabla de Asignación del Modelo de IA

La tabla muestra la configuración del modelo de IA para cada proveedor, incluyendo la siguiente información:

* **Identificación del proveedor** – El identificador único del proveedor
* **Modelo de IA** – El modelo de IA actualmente asignado al proveedor
* **E-Text** Indica si la función E-Text está habilitada
* **Acción** – Contiene la opción para eliminar la entrada

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_3.png)

### Eliminar entrada

Para restablecer la configuración del modelo de IA de un proveedor al valor predeterminado:

1.  Haz clic en el ícono de la papelera en la columna de **Acciones** junto a la entrada del proveedor.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_4.png)
2.  Aparecerá un cuadro de diálogo de confirmación: confirma que deseas eliminar la entrada.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_5.png)
3. Una vez eliminada, el proveedor volverá a utilizar el modelo de IA predeterminado si **extracción de mesa de IA** está en uso.
