# Funciones

**Documentación Funcional**

Este módulo contiene funciones para manipular datos de documentos y realizar diversas operaciones relacionadas con los campos del documento.

**Funciones**

1. **set\_field\_value(document\_data, field\_name, value)**
   * Descripción: Establece el valor de un campo en los datos del documento.
   * Parámetros:
     * document\_data (dict): Los datos del documento que contienen información del campo.
     * field\_name (str): El nombre del campo a establecer.
     * value: El valor a establecer para el campo.
   *   Ejemplo:

       ```
       set_field_value(document_data, "name", "John Doe")
       ```
2. **set\_date\_value(document\_data, field\_name, value, add\_days=0, skip\_weekend=False)**
   * Descripción: Establece el valor de un campo de fecha en los datos del documento.
   * Parámetros:
     * document\_data (dict): Los datos del documento que contienen información del campo.
     * field\_name (str): El nombre del campo de fecha a establecer.
     * value: El valor de la fecha a establecer en formato ISO (por ejemplo, "2020-12-31").
     * add\_days (int): Agrega días adicionales a la fecha dada.
     * skip\_weekend (bool): Omite la fecha si cae en fin de semana.
   *   Ejemplo:

       ```
       set_date_value(document_data, "promised_delivery_date", "2020-12-31", add_days=2, skip_weekend=True)
       ```
3. **set\_amount\_value(document\_data, field\_name, value)**
   * Descripción: Establece el valor de un campo de cantidad en los datos del documento.
   * Parámetros:
     * document\_data (dict): Los datos del documento que contienen información del campo.
     * field\_name (str): El nombre del campo a establecer.
     * value: El valor a establecer para el campo.
   *   Ejemplo:

       ```
       set_amount_value(document_data, "number", "123456")
       ```
4. **get\_field\_value(document\_data, field\_name, default\_value=None, is\_clean=False)**
   * Descripción: Obtiene el valor de un campo de los datos del documento.
   * Parámetros:
     * document\_data (dict): Los datos del documento que contienen información del campo.
     * field\_name (str): El nombre del campo a establecer.
     * default\_value (opcional): Devuelve default\_value si no se encuentra el valor del campo.
     * is\_clean (opcional): Convierte el valor a mayúsculas y lo limpia de espacios vacíos.
   * Devuelve:
     * Valor del campo.
   *   Ejemplo:

       ```
       value = get_field_value(document_data, "name")
       ```
5. **create\_new\_field(field\_name, value="")**
   * Descripción: Crea un nuevo campo con el nombre y valor especificados.
   * Parámetros:
     * field\_name (str): El nombre del campo a crear.
     * value: El valor inicial para el campo (el valor predeterminado es una cadena vacía).
   * Devuelve:
     * Diccionario del nuevo campo creado.
   *   Ejemplo:

       ```
       dict = create_new_field("address", "")
       ```
6. **delete\_field(document\_data, field\_name)**
   * Descripción: Elimina un campo de los datos del documento.
   * Parámetros:
     * document\_data (dict): Los datos del documento que contienen información del campo.
     * field\_name (str): El nombre del campo a establecer.
   * Devuelve:
     * Document\_data como json y como dict después de que se eliminó el campo.
   *   Ejemplo:

       ```
       //json, dict = (document_data, "name")
       ```
7. **set\_is\_required(document\_data, field\_name, value)**
   * Descripción: Establece el atributo 'is\_required' de un campo en los datos del documento.
   * Parámetros:
     * document\_data (dict): Los datos del documento que contienen información del campo.
     * field\_name (str): El nombre del campo a establecer.
     * value: El valor a establecer para el campo.
   *   Ejemplo:

       ```
       set_is_required(document_data, "bank_id", True)
       ```
8. **set\_force\_validation(document\_data, field\_name, value)**
   * Descripción: Establece el atributo 'force\_validation' de un campo en los datos del documento.
   * Parámetros:
     * document\_data (dict): Los datos del documento que contienen información del campo.
     * field\_name (str): El nombre del campo a establecer.
     * value(bool): El valor a establecer para el campo.
   *   Ejemplo:

       ```
       set_force_validation(document_data, 'supplier_name', True)
       ```
9. **set\_field\_as\_invalid(document\_data, field\_name, message, code=None)**
   * Descripción: Marca un campo como inválido en los datos del documento.
   * Parámetros:
     * document\_data (dict): Los datos del documento que contienen información del campo.
     * field\_name (str): El nombre del campo a marcar como inválido.
     * message (str): El mensaje de validación para el campo.
     * code (opcional): Código de error para la validación (el valor predeterminado es None).
   *   Ejemplo:

       ```
       --set_field_as_invalid(document_data, "email", "Formato de email inválido", "EMAIL_FORMAT_INVALID")
       ```
10. **set\_field\_attribute(document\_data, field\_name, attribute\_name, value)**
    * Descripción: Establece un atributo personalizado de un campo en los datos del documento.
    * Parámetros:
      * document\_data (str): Los datos del documento que contienen información del campo.
      * field\_name (str): El nombre del campo a establecer.
      * attribute\_name (str): El nombre del atributo a establecer.
      * value (bool): El valor a establecer para el atributo.
    *   Ejemplo:

        ```
        set_field_attribute(document_data, "address", "is_verified", True)
        ```
11. **is\_supplier\_valid(user: UserAuthentication, filter\_data\_json, sub\_org\_id=None)**
    * Descripción: Verifica si un proveedor es válido según los criterios proporcionados.
    * Parámetros:
      * user (UserAuthentication): El usuario autenticado.
      * filter\_data\_json: Criterios de filtro para validar al proveedor.
      * sub\_org\_id (opcional): ID de suborganización opcional para filtrar.
    * Devuelve:
      * True, si el usuario es válido.
      * False si el usuario no es válido.
    *   Ejemplo:

        ```
        bool = is_supplier_valid(user, {"name": "Supplier Inc."})
        ```
12. **get\_document\_content(document\_data)**
    * Descripción: Devuelve el contenido del documento basado en los datos del documento.
    * Parámetros:
      * document\_data (str): Los datos del documento que contienen información del campo.
    * Devuelve:
      * Contenido del documento de los datos del documento.
    *   Ejemplo:

        ```
        document_content = get_document_content(doc)
        ```
13. **update\_document\_status\_with\_doc\_id(doc\_id, user, org\_id, status, message=None, doc\_classification\_class=None)**
    * Descripción: Actualiza el estado de un documento con el ID especificado.
    * Parámetros:
      * doc\_id (str): El ID del documento a actualizar.
      * user: El usuario que realiza la actualización (ya sea ID de usuario o objeto UserAuthentication).
      * org\_id: El ID de la organización a la que pertenece el documento.
      * status (str): El nuevo estado del documento.
      * message: Mensaje opcional asociado con la actualización del estado.
      * doc\_classification\_class: Clase de clasificación de documentos opcional.
    *   Ejemplo:

        ```
        update_document_status_with_doc_id("123456", user, "org_id", "approved", "Documento aprobado")
        ```
14. **get\_lov\_values(org\_id, key, return\_type="list\_of\_objects", sub\_org\_id=None)**
    * Descripción: Obtiene los valores LOV de un org\_id específico.
    * Parámetros:
      * org\_id: El ID de la organización a la que pertenece el documento.
      * return\_type (opcional): El tipo en el que se deben devolver los datos.
      * sub\_org\_id (opcional): ID de suborganización opcional para filtrar.
    * Devuelve:
      * Valores LOV como una lista de objetos o como una lista.
    *   Ejemplo:

        ```
        supplier_to_check = get_lov_values(org_id, 'BlacklistSupplier', return_type="list_of_values")
        ```
15. **format\_decimal\_to\_locale(value, to\_locale="en\_US.UTF-8", max\_decimal\_places=4, min\_decimal\_places=2)**
    * Descripción: Formatea un valor decimal al formato en\_US.UTF-8.
    * Parámetros:
      * value: El valor que debe ser formateado.
      * to\_locale (opcional): El formato en el que se transforma el valor.
      * max\_decimal\_places (opcional): El máximo de lugares decimales que se deben considerar.
      * min\_decimal\_places (opcional): El mínimo de lugares decimales que se deben considerar.
    * Devuelve:
      * El valor formateado.
    *   Ejemplo:

        ```
        formatted_value = format_decimal_to_locale(value, document_json['amount_format_locale'])
        ```
16. **compare\_values(value1, value2)**
    * Descripción: Compara dos valores para igualdad, manejando varios tipos de datos.
    * Parámetros:
      * value1: El primer valor a comparar.
      * value2: El segundo valor a comparar.
    * Devuelve:
      * True si los valores son iguales y False si difieren.
    *   Ejemplo:

        ```
        result = compare_values(10, "10")
        ```
17. **create\_document\_task( user, document\_data, title, description, priority,**\
    **assigned\_to\_user\_id, assigned\_to\_group\_id, send\_email: bool)**
    * Descripción: Crea una tarea de documento.
    * Parámetros:
      * user: El usuario que realiza la actualización (ya sea ID de usuario o objeto UserAuthentication).
      * document\_data: Los datos del documento que contienen información del campo.
      * title (str): El título de la tarea.
      * description (str): La descripción de la tarea.
      * priority: La prioridad de la tarea.
      * assigned\_to\_user\_id: El ID del usuario al que se debe asignar la tarea.
      * assigned\_to\_group\_id: El ID del grupo al que se debe asignar la tarea.
      * send\_email (bool): Determina si se debe enviar un correo electrónico o no.
    * Devuelve:
      * Dict que indica si el proceso fue exitoso o no.
    *   Ejemplo:

        ```
        dict = create_document_task(user, document_data, "País de origen fuera de la UE", "La confirmación proviene de un país fuera de la UE. Por favor, adjunte el documento MRN.", "alto", 1007, None, False)
        ```
18. **set\_document\_sub\_org\_id(document\_data, sub\_org\_id)**
    * Descripción: Establece el sub\_org\_id de los datos del documento especificado.
    * Parámetros:
      * document\_data: Los datos del documento que contienen información del campo.
      * sub\_org\_id (str): ID de suborganización opcional para filtrar.
    *   Ejemplo:

        ```
        set_document_sub_org_id(document_data, sub_org_id)
        ```
19. **get\_user\_by\_id(user\_id)**
    * Descripción: Obtiene el usuario con el ID de usuario correspondiente.
    * Parámetros:
      * user\_id (str): El ID del usuario.
    * Devuelve:
      * El usuario con el ID de usuario correspondiente.
    *   Ejemplo:

        ```
        user = get_user_by_id("123456")
        ```
20. **get\_group\_by\_id(group\_id)**
    * Descripción: Obtiene el grupo con el ID de grupo correspondiente.
    * Parámetros:
      * group\_id (str): El ID del grupo.
    * Devuelve:
      * El grupo con el ID de grupo correspondiente.
    *   Ejemplo:

        ```
        group = get_group_by_id("123456")
        ```
21. **add\_table\_column(table, col\_name, default\_value=None)**
    * Descripción: Agrega una columna a la tabla correspondiente.
    * Parámetros:
      * table: La tabla donde se debe agregar la columna.
      * col\_name: El nombre de la columna.
      * default\_value (opcional): El valor inicial para el campo (el valor predeterminado es una cadena vacía).
    *   Ejemplo:

        ```
        add_table_column(table, "UNIT_PRICE_PER")
        ```
22. **get\_column\_value(row, column\_name, default\_value=None, is\_clean=False)**
    * Descripción: Obtiene un valor de una columna especificada.
    * Parámetros:
      * row: La fila donde se encuentra el valor.
      * col\_name: El nombre de la columna.
      * default\_value (opcional): Devuelve default\_value si no se encuentra el valor del campo.
      * is\_clean (opcional): Convierte el valor a mayúsculas y lo limpia de espacios vacíos.
    *   Ejemplo:

        ```
        original_unit_price = get_column_value(row, "ORIGINAL_UNIT_PRICE")
        ```
23. **set\_column\_value(row, column\_name, value)**
    * Descripción: Establece un valor de una columna especificada.
    * Parámetros:
      * row: La fila donde se encuentra el valor.
      * col\_name: El nombre de la columna.
      * value: El valor que se establecerá en la ubicación especificada.
    * Devuelve:
      * True si el cambio fue exitoso.
    *   Ejemplo:

        ```
        success = set_column_value(row,"SUPPLIER_ID", supplier_id)
        ```
24. **set\_column\_date\_value(document\_data, row, column\_name, value, add\_days=0)**
    * Descripción: Establece un valor de una columna especificada.
    * Parámetros:
      * document\_data: Los datos del documento que contienen información del campo.
      * row: La fila donde se encuentra el valor.
      * col\_name: El nombre de la columna.
      * value: El valor de la fecha a establecer en formato ISO (por ejemplo, "2020-12-31").
      * add\_days (int): Agrega días adicionales a la fecha dada.
    *   Ejemplo:

        ```
        set_column_date_value(document_data, row, "DELIVERY_DATE", "2020-12-31", add_days=2)
        ```
25. **set\_column\_amount\_value(document\_data, row, column\_name, value)**
    * Descripción: Realiza las siguientes acciones:
      * Convierte el valor a cadena y establece el valor para la columna.
      * Establece el contenido de la columna al valor.
      * Formatea el valor según la configuración regional.
    * Parámetros:
      * document\_data (dict): Los datos del documento que contienen información del campo.
      * row: Fila de la línea de la tabla.
      * column\_name: Nombre de la columna.
      * value: Valor a establecer.
    *   Ejemplo:

        ```
        set_column_amount_value(document_data, row, "UNIT_PRICE", str(unit_price))
        ```
26. **remove\_rows\_from\_table(document\_data, table\_name, count, start)**
    * Descripción: Elimina filas de la tabla especificada.
    * Parámetros:
      * document\_data (dict): Los datos del documento que contienen información del campo.
      * table\_name: El nombre de la tabla.
      * count: Cuántas líneas deben ser eliminadas.
      * start: El punto de inicio.
    *   Ejemplo:

        ```
        remove_rows_from_table(document_data,"INVOICE_TABLE",count,start)   
        ```
27. **remove\_all\_rows\_except\_one\_from\_table(document\_data, line\_number)**
    * Descripción: Elimina todas las filas excepto una de la tabla especificada.
    * Parámetros:
      * document\_data (dict): Los datos del documento que contienen información del campo.
      * line\_number: El número de la línea que no debe ser eliminada.
    *   Ejemplo:

        ```
        remove_all_rows_except_one_from_table(document_data, line_number) 
        ```

También puedes utilizar algunas de las funciones integradas de Python:

* abs(): Devuelve el valor absoluto de un número.
* len(): Devuelve la longitud (número de elementos) de un objeto, como una lista o cadena.
* isinstance(): Verifica si un objeto es una instancia de una clase o tipo particular.
* print(): Imprime la salida en la consola.
* round(): Redondea un número de punto flotante a un número especificado de lugares decimales.
* str\_to\_bool(): Convierte una cadena a un valor booleano (True o False).
* type(): Devuelve el tipo de un objeto.
* dict(): Crea un objeto diccionario.
* list(): Crea un objeto lista.
* str(): Convierte un valor a una cadena.
* float(): Convierte un valor a un número de punto flotante.
* int(): Convierte un valor a un entero.

Para más detalles, visita la documentación oficial de Python: [Funciones Integradas](https://docs.python.org/3.12/library/functions.html).

#### Funciones de la Clase String

También puedes usar estas funciones específicamente para trabajar con cadenas:

* lower(): Convierte todos los caracteres en una cadena a minúsculas.
* upper(): Convierte todos los caracteres en una cadena a mayúsculas.
* split(): Divide una cadena en una lista basada en un delimitador (por ejemplo, espacio o coma).
* startswith(): Verifica si una cadena comienza con un prefijo especificado.
* endswith(): Verifica si una cadena termina con un sufijo especificado.
* strip(): Elimina cualquier espacio en blanco al principio o al final de una cadena.

#### Funciones del Módulo Matemático de Python

Estas funciones son parte del módulo matemático y son útiles para operaciones matemáticas:

* floor(): Devuelve el entero más grande menor o igual a un número dado.
* ceil(): Devuelve el entero más pequeño mayor o igual a un número dado.

Para más información, consulta la documentación oficial de Python: [Funciones del Módulo Matemático](https://docs.python.org/3/library/math.html).

#### Función de Expresión Regular

* re.search(): Busca un patrón dentro de una cadena y devuelve la primera coincidencia.

Consulta más detalles aquí: [Documentación de re.search](https://docs.python.org/3/library/re.html#re.search).

#### Funciones Externas

Aquí hay algunas funciones útiles de bibliotecas externas:

* deepcopy(): Crea una copia de un objeto, incluidos objetos anidados (del módulo copy).\
  [Documentación de Deepcopy](https://docs.python.org/3/library/copy.html#copy.deepcopy).
* levenshtein\_distance(): Calcula el número de ediciones (inserciones, eliminaciones, sustituciones) requeridas para cambiar una cadena en otra. Esta función está disponible en la [biblioteca Jellyfish](https://jamesturk.github.io/jellyfish/functions/).

#### Funciones de Fecha y Hora

Puedes usar las siguientes funciones para trabajar con fechas y horas:

* strptime(): Convierte una cadena en un objeto datetime basado en un formato especificado.
* strftime(): Formatea un objeto datetime en una cadena basada en un formato especificado.

Para más información, consulta la documentación oficial:\
[Funciones de Fecha y Hora](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior).
