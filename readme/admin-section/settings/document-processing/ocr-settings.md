# Configuración de OCR

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 11.01.00.png" alt=""><figcaption></figcaption></figure>

1. **Calidad de OCR**:
* Esta configuración te permite definir el porcentaje mínimo de calidad de OCR requerido para que un documento sea procesado automáticamente. Incluye un control deslizante que puedes ajustar para establecer el umbral, como el 75%, por debajo del cual el sistema no puede garantizar una extracción exitosa. Si la calidad de OCR de un documento cae por debajo de este umbral, puedes optar por hacer que el sistema tome acciones específicas, como volver a ejecutar el OCR después de una confirmación manual.
2. **Configuraciones generales de OCR**:
* **Usar E-Text si está disponible**: Esta opción, cuando está habilitada, permite al sistema utilizar texto electrónico incrustado dentro de PDF u otros tipos de documentos para mejorar la precisión.
* **Usar DESKEW si está disponible**: Esta función corrige la alineación del documento, lo que ayuda a mejorar la precisión de OCR enderezando cualquier escaneo sesgado.
3. **Configuraciones de OCR para tablas**:
* **Usar datos de IA para tablas si están disponibles**: Esta configuración permite el uso de tecnologías de IA para reconocer y extraer mejor las tablas de documentos escaneados, aprovechando modelos de aprendizaje automático para identificar y estructurar datos tabulares con precisión.
4. **Configuraciones de OCR para los campos de encabezado**:
* **Usar Extracción de Reglas**: Cuando está habilitada, esta configuración permite al sistema aplicar reglas predefinidas para extraer datos de los campos de encabezado, lo que puede ser crítico para identificar correctamente secciones de documentos como números de factura, fechas, etc.
* **Usar Extracción de IA**: Esta opción utiliza modelos de IA para extraer inteligentemente campos de encabezado, lo que puede ser más adaptable a variaciones en diseños y estilos de documentos.
