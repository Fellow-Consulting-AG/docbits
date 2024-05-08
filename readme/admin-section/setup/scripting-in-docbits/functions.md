# Funciones

**Documentación Funcional**

Este módulo contiene funciones para manipular datos de documentos y realizar varias operaciones relacionadas con los campos de documentos.

## **Funciones**

1. ### **set\_field\_value(document\_data, field\_name, value)**
* Descripción: Establece el valor de un campo en los datos del documento.
* Parámetros:
* `document_data` (dict): Los datos del documento que contienen información del campo.
* `field_name` (str): El nombre del campo a establecer.
* `value`: El valor a establecer para el campo.
*   Ejemplo:

`set_field_value(document_data, "nombre", "John Doe")`
2. ### **set\_date\_value(document\_data, field\_name, value)**
* Descripción: Establece el valor de un campo de fecha en los datos del documento.
* Parámetros:
* `document_data` (dict): Los datos del documento que contienen información del campo.
* `field_name` (str): El nombre del campo de fecha a establecer.
* `value`: El valor de la fecha a establecer en formato ISO (por ejemplo, "2020-12-31").
*   Ejemplo:

`set_date_value(document_data, "fecha_de_nacimiento", "1990-05-15")`
3. ### **set\_amount\_value(document\_data, field\_name, value)**
* Descripción: Establece el valor de un campo de cantidad en los datos del documento.
* Parámetros y uso del ejemplo similar a `set_field_value`.
4. ### **set\_is\_required(document\_data, field\_name, value)**
* Descripción: Establece el atributo 'is\_required' de un campo en los datos del documento.
* Parámetros y uso del ejemplo similar a `set_field_value`.
5. ### **set\_force\_validation(document\_data, field\_name, value)**
* Descripción: Establece el atributo 'force\_validation' de un campo en los datos del documento.
* Parámetros y uso del ejemplo similar a `set_field_value`.
6. ### **set\_field\_attribute(document\_data, field\_name, attribute\_name, value)**
* Descripción: Establece un atributo personalizado de un campo en los datos del documento.
* Parámetros:
* `attribute_name` (str): El nombre del atributo a establecer.
* `value`: El valor a establecer para el atributo.
*   Ejemplo:

`set_field_attribute(document_data, "dirección", "está_verificado", True)`
7. ### **get\_field\_value(document\_data, field\_name, default\_value=None, is\_clean=False)**
* Descripción: Obtiene el valor de un campo de los datos del documento.
* Parámetros y uso del ejemplo similar a `set_field_value`.
8. ### **create\_new\_field(field\_name, value="")**
* Descripción: Crea un nuevo campo con el nombre y valor especificados.
* Parámetros:
* `field_name` (str): El nombre del campo a crear.
* `value`: El valor inicial para el campo (por defecto es una cadena vacía).
*   Ejemplo:

`create_new_field("dirección", "123 Main St")`
9. ### **delete\_field(document\_data, field\_name)**
* Descripción: Elimina un campo de los datos del documento.
* Parámetros y uso del ejemplo similar a `set_field_value`.
10. ### **update\_document\_status\_with\_doc\_id(doc\_id, user, org\_id, status, message=None, doc\_classification\_class=None)**
* Descripción: Actualiza el estado de un documento con el ID especificado.
* Parámetros:
* `doc_id` (str): El ID del documento a actualizar.
* `user`: El usuario que realiza la actualización (ya sea ID de usuario u objeto UserAuthentication).
* `org_id`: El ID de la organización a la que pertenece el documento.
* `status` (str): El nuevo estado del documento.
* `message`: Mensaje opcional asociado con la actualización de estado.
* `doc_classification_class`: Clase de clasificación de documento opcional.
*   Ejemplo:

`update_document_status_with_doc_id("123456", user, org_id, "aprobado", "Documento aprobado")`
11. ### **is\_supplier\_valid(user: UserAuthentication, filter\_data\_json, sub\_org\_id=None)**
* Descripción: Verifica si un proveedor es válido según los criterios proporcionados.
* Parámetros:
* `user` (UserAuthentication): El usuario autenticado.
* `filter_data_json`: Criterios de filtro para validar al proveedor.
* `sub_org_id`: ID de suborganización opcional para filtrar.
*   Ejemplo:

`is_supplier_valid(user, {"nombre": "Proveedor S.A."})`
12. ### **set\_field\_as\_invalid(document\_data, field\_name, message, code=None)**
* Descripción: Marca un campo como inválido en los datos del documento.
* Parámetros:
* `document_data` (dict): Los datos del documento que contienen información del campo.
* `field_name` (str): El nombre del campo a marcar como inválido.
* `message` (str): El mensaje de validación para el campo.
* `code` (opcional): Código de error para la validación (por defecto es None).
*   Ejemplo:

`set_field_as_invalid(document_data, "email", "Formato de email inválido", "EMAIL_FORMAT_INVALID")`
13. ### **compare\_values(value1, value2)**
* Descripción: Compara dos valores para la igualdad, manejando varios tipos de datos.
* Parámetros:
* `value1`: El primer valor a comparar.
* `value2`: El segundo valor a comparar.
*   Ejemplo:

`compare_values(10, "10")`
