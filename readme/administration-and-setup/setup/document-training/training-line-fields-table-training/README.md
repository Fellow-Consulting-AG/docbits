# Entrenamiento de Campos de Línea / Tabla de Entrenamiento

## Tabla de Entrenamiento: Cuándo y Cómo Usarla

DocBits utiliza la extracción de tablas basada en IA de forma predeterminada, la cual funciona con todos los proveedores. Sin embargo, cuando necesitas más control sobre cómo se extraen los elementos de línea para un proveedor específico, puedes utilizar **Entrenamiento de Tabla** para definir la estructura manualmente.

#### **Importante: Entrenamiento Específico del Proveedor**

El entrenamiento de tabla es **específico para cada proveedor**. Si entrenas un diseño de tabla para un proveedor, las reglas se aplicarán solo a los documentos de ese proveedor.\
Otros proveedores seguirán utilizando la extracción de tablas basada en IA a menos que se entrenen por separado.

#### ¿Cuándo Deberías Usar el Entrenamiento de Tabla?

Utiliza el Entrenamiento de Tabla **solo cuando el diseño del documento sea estable**, y deseas garantizar una extracción consistente y de alta calidad. Es más adecuado para proveedores que:

* Utilizan un **formato de factura fijo** con el tiempo.
* Requieren un **mapeo preciso** de los elementos de línea a campos específicos.
* Son proveedores de **alto volumen**, donde la automatización consistente es valiosa.

#### Cuándo No Usar el Entrenamiento de Tabla

Evita usar el Entrenamiento de Tabla si:

* El proveedor **cambia frecuentemente el diseño de su factura** (por ejemplo, cada par de meses).
* No recibes documentos regularmente de ese proveedor.
* La extracción basada en IA predeterminada funciona **suficientemente bien** sin entrenamiento manual.

En tales casos, volver a entrenar la tabla repetidamente sería ineficiente y consumiría tiempo.

## Cómo Usarlo:

El **Modo de Entrenamiento** se utiliza para enseñar a DocBits cómo extraer correctamente los elementos de línea del diseño de documento de un proveedor específico.

Cuando estás en el Modo de Entrenamiento, defines:

* **Dónde se encuentra la tabla** en el documento.
* **Qué áreas corresponden a cada columna** (por ejemplo, Cantidad, Descripción, Precio Unitario).

Este modo crea una **plantilla de extracción reutilizable** para ese proveedor, por lo que los documentos futuros con el mismo diseño se procesarán automáticamente, sin necesidad de volver a entrenar.

**Características Clave:**

* Las columnas **mapeadas son de solo lectura** — no puedes cambiar manualmente el texto.
* **No puedes añadir ni eliminar filas**.
* El enfoque está en **mapear posiciones**, no en corregir valores.
* Una vez que hayas terminado de mapear la tabla y sus columnas, haz clic en **“Guardar Reglas”** para que DocBits aprenda y aplique este entrenamiento a documentos similares del mismo proveedor.

El **Modo de Corrección** te permite **corregir errores de extracción** en los datos de la tabla para el documento actual. Se utiliza cuando DocBits ya ha intentado extraer la tabla, pero los resultados necesitan pequeñas correcciones.

Utiliza el Modo de Corrección cuando:

* Algunos **valores faltan o están desalineados**.
* Se extrajo una **línea vacía o duplicada** que necesita ser eliminada.

**Lo Que Puedes Hacer en el Modo de Corrección:**

* **Ajustar manualmente valores** en las columnas mapeadas (por ejemplo, corregir desplazamientos).
* **Eliminar filas** que no deberían formar parte de la tabla.
* **Añadir filas** que se omitieron por completo durante la extracción.
