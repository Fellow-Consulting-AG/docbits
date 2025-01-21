# Árboles de Decisión

#### Descripción General

Los Árboles de Decisión son una característica poderosa que permite el enrutamiento automatizado y el proceso de toma de decisiones basado en reglas predefinidas. Esta característica es especialmente útil en entornos complejos donde se deben evaluar diversas condiciones para determinar el curso de acción correcto, como asignar precios, determinar cantidades o enrutear documentos.

**Componentes Clave**

* **Lista de Árboles de Decisión**: Esta es la interfaz principal donde se enumeran todos los árboles de decisión existentes. Cada árbol de decisión puede estar asociado con un tipo de documento específico, como una `FACTURA` o `COTIZACIÓN`.
* **Editor de Árboles de Decisión**: Esta interfaz permite la creación y edición de árboles de decisión, donde puedes definir reglas, operadores y acciones a tomar cuando se cumplen ciertas condiciones.

#### Interfaz del Árbol de Decisión

**Lista de Árboles de Decisión**

La lista de Árboles de Decisión muestra todos los árboles de decisión disponibles. Cada entrada muestra:

* **Nombre**: El nombre del árbol de decisión.
* **Tipo de Documento**: El tipo de documento asociado con el árbol de decisión (por ejemplo, `FACTURA`, `COTIZACIÓN`).

**Editor de Árboles de Decisión**

El Editor de Árboles de Decisión te permite configurar reglas que rigen cómo se toman las decisiones.

**Componentes del Editor de Árboles de Decisión**

* **Reglas**: Cada regla consiste en condiciones y acciones.
* **Seleccionar Fuente**: Este menú desplegable te permite especificar el campo fuente a evaluar.
* **Seleccionar Operador**: Define el operador lógico (por ejemplo, `<=`, `>=`, `=`, `!=`) que se aplicará al campo fuente.
* **Resultado**: Define el resultado o acción que debe tomarse cuando se cumplen las condiciones.
* **Agregar Nueva Fila**: Te permite agregar reglas adicionales al árbol de decisión.

**Ejemplo de Configuración de un Árbol de Decisión**

1. **Regla 1**:
   * **Fuente**: Cantidad
   * **Operador**: `<=`
   * **Valor**: `250000`
   * **Resultado**: Asignar a `CATMGR_CMM`
2. **Regla 2**:
   * **Fuente**: Precio
   * **Operador**: `>`
   * **Valor**: `500000`
   * **Resultado**: Asignar a `DIRECTOR_DE_ADQUISICIONES`

Cada regla se evalúa secuencialmente, y la acción correspondiente se ejecuta si se satisfacen las condiciones.

#### Política del Árbol de Decisión

La Política del Árbol de Decisión define cómo se procesan múltiples reglas dentro de un árbol de decisión. Puedes elegir entre varias políticas:

* **Única**: Asegura que solo una regla puede coincidir. Si más de una regla coincide, el árbol de decisión marcará un error.
* **Primera**: Se aplica la primera regla coincidente, y no se evalúan más reglas.
* **Prioridad**: Las reglas se evalúan según su orden de prioridad. Se aplica la regla coincidente de mayor prioridad.
* **Colectar (suma)**: Recoge todas las reglas coincidentes y suma los resultados.
* **Colectar (mínimo/máximo/cantidad)**: Recoge todas las reglas coincidentes y selecciona el mínimo, máximo o cuenta las ocurrencias.
* **Orden de Reglas**: Aplica las reglas en el orden en que aparecen en el árbol de decisión.
* **Cualquiera**: Cualquier regla coincidente puede aplicarse, permitiendo múltiples resultados.

**Ejemplo de una Política del Árbol de Decisión en Acción**

En el árbol de decisión "Precio del Grupo Directo":

* **Política Seleccionada**: `Primera`
* Esto significa que tan pronto como se cumple la condición de una regla, se aplica su acción asociada, y no se evalúan más reglas.

#### Exportar y Guardar

* **Guardar**: Guarda la configuración actual del árbol de decisión.
* **Exportar**: Te permite exportar la configuración del árbol de decisión, que luego puede ser importada a otro entorno o utilizada para fines de respaldo.
