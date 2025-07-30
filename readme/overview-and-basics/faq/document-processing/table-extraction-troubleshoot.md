# Solución de problemas de extracción de tablas

## **Paso 1: Abrir la vista OCR para resultados de extracción deficientes**

Si los resultados del entrenamiento de extracción de tablas no son buenos:

1. Abre la **vista OCR** haciendo clic en el icono de la lupa con **OCR** escrito en él.
2. Revisa los resultados de la extracción y verifica si el proceso OCR puede mejorar la captura de datos.
3. Si los resultados siguen siendo malos, prueba con un documento diferente para verificar si el problema es específico del documento.
4. Si el problema es específico del documento, utiliza otro documento para la extracción.
   * Si el problema persiste, sigue los siguientes pasos.

## **Paso 2: Verificar la disponibilidad de E-Text**

1. Verifica si el documento tiene **e-text** disponible.
   * Puedes verificar esto utilizando una herramienta como **Adobe Acrobat**.
   * Si el documento contiene e-text, sigue el **Paso 3**.
   * Si el documento no contiene e-text, sigue el **Paso 4**.

## **Paso 3: Activar la extracción de E-Text**

Si el documento contiene e-text, tienes dos opciones:

1. **Activar la extracción de e-text solo para este proveedor**:
   * Regresa a la **Validación de Campos de Documentos**.
   * Haz clic en el cuadrado con los tres puntos en la barra de herramientas del lado izquierdo.
   * Aquí, activa la opción **Usar e-text si está disponible** para activarlo solo para este proveedor.
2. **Activar la extracción de e-text para todos los proveedores**:
   * Ve a **Configuración** > **Procesamiento de Documentos** > **Configuración OCR**.
   * En esta sección, encontrarás la opción **Usar e-text si está disponible** y puedes activarla para todos los proveedores.
3. Después de habilitar la extracción de e-text, vuelve a intentar el **entrenamiento de extracción de tablas**.
   * Si los resultados mejoran, el problema está resuelto.
   * Si los resultados siguen siendo malos, procede al **Paso 4**.

## **Paso 4: No hay E-Text disponible - Cambiar la versión de OCR de IA**

Si el documento no tiene e-text disponible:

1. Ve a **Configuración** > **Procesamiento de Documentos** > **Configuración OCR**.
2. Cambia la **Versión de OCR de IA** a una versión diferente.
3. Regresa al **Entrenamiento de Extracción de Tablas** e inténtalo de nuevo.
4. Si el resultado es mejor:
   * Verifica otros documentos de diferentes proveedores para asegurarte de que los resultados de extracción para esos proveedores no se vean afectados por este cambio.
   * **Sé cauteloso, ya que este cambio puede afectar los resultados de extracción de otros proveedores.**
   * Este cambio puede afectar a otros proveedores, así que asegúrate de verificar los resultados minuciosamente para garantizar que no afecte negativamente las extracciones de documentos de otros proveedores.
5. Si el resultado no mejoró después de cambiar la versión de OCR de IA, por favor **contáctanos** para obtener más ayuda.
