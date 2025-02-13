# Document Types

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto%202024-05-08%20um%2008.44.19.png" alt=""><figcaption></figcaption></figure>

#### Visión general

La sección de Tipos de Documentos enumera todos los tipos de documentos reconocidos y procesados por Docbits. Los administradores pueden gestionar varios aspectos como diseño, definiciones de campos, reglas de extracción y más para cada tipo de documento. Esta personalización es clave para garantizar un manejo preciso de los datos y el cumplimiento de los estándares organizativos.

#### Funciones clave y opciones

1. **Lista de Tipos de Documentos**:

* Cada fila representa un tipo de documento como Factura, Nota de Crédito, Nota de Entrega, etc.
* Los tipos de documentos pueden ser estándar o personalizados, como se indica con etiquetas como "Estándar".

2. **Editar diseño**: Esta opción permite a los administradores modificar la configuración del diseño del documento, que incluye definir cómo aparece el documento y dónde se encuentran los campos de datos.
3. **Subtipos de Documentos**: Si algún tipo de documento tiene subcategorías, esta opción permite a los administradores configurar ajustes específicos para cada subtipo.
4. **Columnas de la tabla**: Personalice qué columnas de datos deben aparecer cuando se ve el tipo de documento en listas o informes.
5. **Campos**: Gestione los campos de datos asociados con el tipo de documento, incluyendo la adición de nuevos campos o la modificación de los existentes.
6. **Entrenamiento del Modelo**: Configure y entrene el modelo utilizado para reconocer y extraer datos de los documentos. Esto puede implicar establecer parámetros para modelos de aprendizaje automático que mejoran con el tiempo y más datos.
7. **Regex**: Configure expresiones regulares que se utilizan para extraer datos de documentos basados en patrones. Esto es particularmente útil para la extracción de datos estructurados.
8. **Scripts**: Escriba o modifique scripts que ejecuten reglas de procesamiento personalizadas o flujos de trabajo para documentos de este tipo.
9. **EDI (Intercambio Electrónico de Datos)**: Configure ajustes relacionados con el intercambio de documentos en formatos electrónicos estandarizados.

{% hint style="info" %}
Ver [Configuración de Tipo de Documento](../../../../admin-section/setup/document-types/)
{% endhint %}

{% @jira/embed url="https://fellowpro.atlassian.net/browse/DOCB-2489" %}
