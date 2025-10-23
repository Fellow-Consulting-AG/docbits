---
description: Configuración de las condiciones Y en los workflows DocBits
---

# Y

## Comprendiendo las Tarjetas "Y"

### **Propósito de las Tarjetas 'Y':**

* Las tarjetas **Y** funcionan como tarjetas de condición que especifican los criterios que deben cumplirse para que el flujo de trabajo continúe. Actúan efectivamente como operadores lógicos "Y", lo que significa que todas las condiciones especificadas en estas tarjetas deben cumplirse para que se active la acción posterior.

#### Categorías de Tarjetas 'Y'

Desde las capturas de pantalla, es evidente que estas tarjetas cubren una amplia gama de condiciones, que incluyen:

* **Comparar con Orden de Compra**:
  * Condiciones relacionadas con la validación y comparación con órdenes de compra, como comparar fechas de entrega, precios unitarios o diferencias de cantidad. Estos son cruciales para garantizar que las transacciones se alineen con los términos acordados.
* **Campo de Documento**:
  * Estas implican condiciones basadas en campos específicos dentro de documentos, como marcar casillas, comparar valores de campos o garantizar que un campo de documento cumpla con una tolerancia especificada. Esto es particularmente importante para la integridad de datos y verificaciones automatizadas dentro de formularios o sistemas de gestión de documentos.
* **Fecha y Hora**:
  * Condiciones basadas en fechas y horas
* **Documento**:
  * Condiciones basadas en características del documento, como tipo o asociación con una suborganización particular. Estas condiciones pueden dirigir flujos de trabajo basados en la categorización de documentos o la participación departamental.
* **Lógica**:
  * Condiciones lógicas que pueden implicar evaluaciones como "Continuar con una probabilidad del X%" o ejecutar solicitudes HTTPS, que son vitales para integraciones y toma de decisiones probabilísticas dentro de flujos de trabajo.
* **Estado**:
  * Centrándose en el estado de documentos o tareas, estas condiciones aseguran que solo los elementos en ciertos estados desencadenen flujos de trabajo específicos, crucial para la gestión de procesos basada en el estado.
* **Tabla**:
  * Estas implican condiciones basadas en datos de tablas, como coincidir con patrones regex o comparar valores dentro de una tabla. Tales condiciones son esenciales para validar y manipular grandes conjuntos de datos.
* **Asignado**:
  * Condiciones basadas en asignados de tareas o documentos. Esto garantiza que las acciones solo se tomen cuando ciertos usuarios están involucrados, mejorando la responsabilidad y la especificidad de las tareas.

### Aplicación Práctica

Estas tarjetas "Y" se configuran dentro del flujo de trabajo para realizar verificaciones y validaciones que aseguran que el proceso se adhiera estrictamente a las reglas comerciales y estándares de integridad de datos. Por ejemplo:

* **Un flujo de trabajo podría usar una tarjeta 'Y' para verificar que el monto total de una factura coincida con la orden de compra antes de activar el pago.**
* **Otro flujo de trabajo podría usar una tarjeta 'Y' para asegurar que un documento sea revisado por miembros específicos del equipo antes de que avance a la siguiente etapa.**

### Conclusión

Las tarjetas "Y" son un componente fundamental de los sistemas de flujo de trabajo que requieren un control preciso sobre la ejecución del proceso basado en múltiples condiciones. Aseguran que cada paso de un flujo de trabajo solo avance cuando se cumplan todos los criterios necesarios, automatizando así árboles de decisiones complejos dentro de los procesos comerciales.

Comprender y configurar estas tarjetas correctamente es crucial para aprovechar al máximo las capacidades de su sistema de gestión de flujos de trabajo para mejorar la eficiencia, precisión y cumplimiento dentro de los procesos organizativos.
