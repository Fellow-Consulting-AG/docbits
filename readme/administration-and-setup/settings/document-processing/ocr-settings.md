# Configuración de OCR

## Descripción general

En los ajustes de **OCR (Reconocimiento Óptico de Caracteres)**, puedes configurar cómo se aplica el OCR durante el procesamiento de documentos. Esto incluye especificar la calidad mínima requerida, elegir si utilizar texto incrustado (e-text), seleccionar la versión de OCR, y más. Esta página proporciona una explicación detallada de todos los ajustes disponibles.

## Cómo acceder a la Configuración de OCR

Para acceder a los ajustes de OCR:

*   Navega a: **Ajustes** → **Procesamiento de documentos** → **Configuración de OCR**

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_ocr.png)

## Calidad de OCR

En esta sección, puedes establecer la calidad mínima del documento requerida para el procesamiento de OCR ajustando el control deslizante de calidad. Mueve el control deslizante hacia la izquierda o hacia la derecha para disminuir o aumentar el umbral de calidad, respectivamente.

Si un documento no cumple con el nivel de calidad definido, DocBits proporciona tres opciones para manejarlo:

* **Proceso de todos modos**\
  El documento será procesado independientemente de su calidad.
* **Ejecutar de nuevo después de la confirmación**\
  **DocBits** se pausará y te pedirá que confirmes si deseas continuar con el procesamiento.
* **Lanzar error**\
  El procesamiento del documento se detendrá por completo y se mostrará un mensaje de error, indicando que el documento no cumplió con el umbral de calidad requerido.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ocr_settings_1.png)

## Configuración general del OCR

* **Utilice E-Text si está disponible**\
  Cuando está habilitado, **DocBits** utilizará texto electrónico incrustado (por ejemplo, de PDFs) en lugar de realizar OCR. Esto mejora tanto la velocidad como la precisión, ya que el texto se extrae directamente sin requerir procesamiento de OCR.
* **Utilizar DESKEW si está disponible**\
  Esta opción corrige automáticamente la alineación de los documentos escaneados. Enderezar imágenes inclinadas ayuda a mejorar la precisión del OCR.
*   **Versión AI OCR**\
    Te permite seleccionar una versión específica del motor OCR basado en IA.\
    Esto puede ser útil si:

    * No estás logrando los resultados deseados con la versión actualmente seleccionada.
    * Estás solucionando problemas relacionados con el rendimiento o la precisión del OCR.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ocr_settings_2.png)

## Configuración del OCR para las tablas

* **Utilizar los datos de la IA para las tablas si están disponibles**\
  Cuando está habilitado, DocBits utilizará datos de OCR para las tablas en lugar de texto electrónico incrustado (E-Text), incluso si la configuración **Utilice E-Text si está disponible** está activada.

## Configuración del OCR para los campos de la cabecera

* **Utilizar la extracción de reglas**\
  DocBits aplicará tus reglas de extracción predefinidas para identificar los campos de la cabecera.
* **Usar extracción AI**\
  DocBits utilizará IA para detectar y extraer automáticamente los campos de la cabecera.

**Orden de ejecución:**\
Si ambas opciones están habilitadas, **DocBits** realizará la extracción en el siguiente orden:\
**Extracción de reglas → Extracción AI**\
\
<mark style="color:red;">**Nota**</mark>: Para obtener los mejores resultados y un comportamiento consistente, habilita ambas opciones. Esto permite que **DocBits** utilice métodos basados en reglas y métodos basados en IA en combinación durante la extracción de la cabecera.
