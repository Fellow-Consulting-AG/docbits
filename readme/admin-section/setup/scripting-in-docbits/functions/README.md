# Functions

**Functional Documentation**

This module contains functions for manipulating document data and performing various operations related to document fields.

**Functions**

1. **set\_field\_value(document\_data, field\_name, value)**
   * Description: Sets the value of a field in the document data.
   * Parameters:
     * document\_data (dict): The document data containing field information.
     * field\_name (str): The name of the field to set.
     * value: The value to set for the field.
   *   [Example:](example-scripts.md#set_field_value-document_data-field_name-value)

       ```
       set_field_value(document_data, "name", "John Doe")
       ```
2. **set\_date\_value(document\_data, field\_name, value, add\_days=0, skip\_weekend=False)**
   * Description: Sets the value of a date field in the document data.
   * Parameters:
     * document\_data (dict): The document data containing field information.
     * field\_name (str): The name of the date field to set.
     * value: The date value to set in ISO format (e.g., "2020-12-31").
     * add\_days (int): Add additional days to the given date.
     * skip\_weekend (bool): Skips the date if it falls on the weekend
   *   [Example:](example-scripts.md#set_date_value-document_data-field_name-value-add_days-0-skip_weekend-false)

       ```
       set_date_value(document_data, "promised_delivery_date", "2020-12-31", add_days=2, skip_weekend=True)
       ```
3. **set\_amount\_value(document\_data, field\_name, value)**
   * Description: Sets the value of an amount field in the document data.
   * Parameters:
     * document\_data (dict): The document data containing field information.
     * field\_name (str): The name of the field to set.
     * value: The value to set for the field.
   *   [Example:](example-scripts.md#set_amount_value-document_data-field_name-value)

       ```
       set_amount_value(document_data, "number", "123456")
       ```
4. **get\_field\_value(document\_data, field\_name, default\_value=None, is\_clean=False)**
   * Description: Gets the value of a field from the document data.
   * Parameters:
     * document\_data (dict): The document data containing field information.
     * field\_name (str): The name of the field to set.
     * default\_value (optional): Returns default\_value if no field value is found
     * is\_clean (optional): Turns the value in uppercase and cleans it from empty spaces
   * Returns:
     * Value of the field
   *   [Example:](example-scripts.md#get_field_value-document_data-field_name-default_value-none-is_clean-false)

       ```
       value = get_field_value(document_data, "name")
       ```
5. **create\_new\_field(field\_name, value="")**
   * Description: Creates a new field with the specified name and value.
   * Parameters:
     * field\_name (str): The name of the field to create.
     * value: The initial value for the field (default is an empty string).
     * value: The initial value for the field (default is an empty string).
     * value: The initial value for the field (default is an empty string).
   * Returns:
     * Dictionary of the new created field
   *   [Example:](example-scripts.md#create_new_field-field_name-value)

       ```
       dict = create_new_field("address", "")
       ```
6. **delete\_field(document\_data, field\_name)**
   * Description: Deletes a field from the document data.
   * Parameters:
     * document\_data (dict): The document data containing field information.
     * field\_name (str): The name of the field to set
   * Returns:
     * Document\_data as json and as dict after field got deleted
   *   [Example:](example-scripts.md#delete_field-document_data-field_name)

       ```
       json, dict = (document_data, "name")
       ```
7. **set\_is\_required(document\_data, field\_name, value)**
   * Description: Sets the 'is\_required' attribute of a field in the document data.
   * Parameters:
     * document\_data (dict): The document data containing field information.
     * field\_name (str): The name of the field to set.
     * value: The value to set for the field.
   *   [Example:](example-scripts.md#set_is_required-document_data-field_name-value)

       ```
       set_is_required(document_data, "bank_id", True)
       ```
8. **set\_force\_validation(document\_data, field\_name, value)**
   * Description: Sets the 'force\_validation' attribute of a field in the document data.
   * Parameters:
     * document\_data (dict): The document data containing field information.
     * field\_name (str): The name of the field to set.
     * value(bool): The value to set for the field.
   *   [Example:](example-scripts.md#set_force_validation-document_data-field_name-value)

       ```
       set_force_validation(document_data, 'supplier_name', True)
       ```
9. **set\_field\_as\_invalid(document\_data, field\_name, message, code=None)**
   * Description: Marks a field as invalid in the document data.
   * Parameters:
     * document\_data (dict): The document data containing field information.
     * field\_name (str): The name of the field to mark as invalid.
     * message (str): The validation message for the field.
     * code (optional): Error code for the validation (default is None).
   *   [Example:](example-scripts.md#set_field_as_invalid-document_data-field_name-message-code-none)

       ```
       set_field_as_invalid(document_data, "email", "Invalid email format", "EMAIL_FORMAT_INVALID")
       ```
10. **set\_field\_attribute(document\_data, field\_name, attribute\_name, value)**
    * Description: Sets a custom attribute of a field in the document data.
    * Parameters:
      * document\_data (str): The document data containing field information.
      * field\_name (str): The name of the field to set.
      * attribute\_name (str): The name of the attribute to set.
      * value (bool): The value to set for the attribute.
    *   [Example:](example-scripts.md#set_field_attribute-document_data-field_name-attribute_name-value)

        ```
        set_field_attribute(document_data, "address", "is_verified", True)
        ```
11. **is\_supplier\_valid(user: UserAuthentication, filter\_data\_json, sub\_org\_id=None)**
    * Description: Checks if a supplier is valid based on the provided criteria.
    * Parameters:
      * user (UserAuthentication): The authenticated user.
      * filter\_data\_json: Filter criteria for validating the supplier.
      * sub\_org\_id (optional): Optional sub-organization ID for filtering.
    * Returns:
      * True, if the user is valid
      * False if the user isn’t valid
    *   [Example:](example-scripts.md#is_supplier_valid-user-userauthentication-filter_data_json-sub_org_id-none)

        ```
        bool = is_supplier_valid(user, {"name": "Supplier Inc."})
        ```
12. **get\_document\_content(document\_data)**
    * Description: Returns the document content based on the document data.
    * Parameters:
      * document\_data (str): The document data containing field information.
    * Returns:
      * Document content of document data.
    *   [Example:](example-scripts.md#get_document_content-document_data)

        ```
        document_content = get_document_content(doc)
        ```
13. **update\_document\_status\_with\_doc\_id(doc\_id, user, org\_id, status, message=None, doc\_classification\_class=None)**
    * Description: Updates the status of a document with the specified ID.
    * Parameters:
      * doc\_id (str): The ID of the document to update.
      * user: The user performing the update (either user ID or UserAuthentication object).
      * org\_id: The ID of the organization to which the document belongs.
      * status (str): The new status of the document.
      * message: Optional message associated with the status update.
      * doc\_classification\_class: Optional document classification class.
    *   [Example:](example-scripts.md#update_document_status_with_doc_id-doc_id-user-org_id-status-message-none-doc_classification_class-n)

        ```
        update_document_status_with_doc_id("123456", user, "org_id", "approved", "Document approved")
        ```
14. **get\_lov\_values(org\_id, key, return\_type="list\_of\_objects", sub\_org\_id=None)**
    * Description: Gets the LOV values from a specific org\_id.
    * Parameters:
      * org\_id: The ID of the organization to which the document belongs.
      * return\_type (optional): The type in which the data should be returned.
      * sub\_org\_id (optional): Optional sub-organization ID for filtering.
    * Returns:
      * LOV-Values as a list of objects or as a list.
    *   [Example:](example-scripts.md#get_lov_values-org_id-key-return_type-list_of_objects-sub_org_id-none)

        ```
        supplier_to_check = get_lov_values(org_id, 'BlacklistSupplier', return_type="list_of_values")
        ```
15. **format\_decimal\_to\_locale(value, to\_locale="en\_US.UTF-8", max\_decimal\_places=4, min\_decimal\_places=2)**
    * Description: Formats a decimal value to en\_US.UTF-8 format.
    * Parameters:
      * value: The value which should be formatted.
      * to\_locale (optional): The format in which the value gets transformed.
      * max\_decimal\_places (optional): The maximum of decimal places which should be considered.
      * min\_decimal\_places (optional): The minimum of decimal places which should be considered.
    * Returns:
      * The formatted value.
    *   [Example:](example-scripts.md#format_decimal_to_locale-value-to_locale-en_us.utf-8-max_decimal_places-4-min_decimal_places-2)

        ```
        formatted_value = format_decimal_to_locale(value, document_json['amount_format_locale'])
        ```
16. **compare\_values(value1, value2)**
    * Description: Compares two values for equality, handling various data types.
    * Parameters:
      * value1: The first value to compare.
      * value2: The second value to compare.
    * Returns:
      * True if the values are equal and False if they differ
    *   [Example:](example-scripts.md#compare_values-value1-value2)

        ```
        result = compare_values(10, "10")
        ```
17. **create\_document\_task( user, document\_data, title, description, priority,**\
    **assigned\_to\_user\_id, assigned\_to\_group\_id, send\_email: bool)**
    * Description: Compares two values for equality, handling various data types.
    * Parameters:
      * user: The user performing the update (either user ID or UserAuthentication object).
      * document\_data: The document data containing field information.
      * title (str): The title of the task.
      * description (str): The description of the task.
      * priority: The priority of the task.
      * assigned\_to\_user\_id: The id of the user to which the task should assigned to.
      * assigned\_to\_group\_id: The id of the group to which the task should assigned to.
      * send\_email (bool): Determine if an email should be send or not.
    * Returns:
      * Dict which is indicating if the process was successful or not
    *   [Example:](example-scripts.md#create_document_task-user-document_data-title-description-priority-assigned_to_user_id-assigned_to_g)

        ```
        dict = create_document_task(user, document_data, "Country of origin outside the EU", "The confirmation comes from a country outside the EU. Please attach the MRN document.", "high", 1007, None, False)
        ```
18. **set\_document\_sub\_org\_id(document\_data, sub\_org\_id)**
    * Description: Sets the sub\_org\_id of the specified document\_data.
    * Parameters:
      * document\_data: The document data containing field information.
      * sub\_org\_id (str): Optional sub-organization ID for filtering.
    *   [Example:](example-scripts.md#set_document_sub_org_id-document_data-sub_org_id)

        ```
        set_document_sub_org_id(document_data, sub_org_id)
        ```
19. **get\_user\_by\_id(user\_id)**
    * Description: Gets the user with the corresponding user ID.
    * Parameters:
      * user\_id (str): The ID of the user.
    * Returns:
      * The user with the corresponding user ID
    *   [Example:](example-scripts.md#get_user_by_id-user_id)

        ```
        user = get_user_by_id("123456")
        ```
20. **get\_group\_by\_id(group\_id)**
    * Description: Gets the group with the corresponding group ID.
    * Parameters:
      * group\_id (str): The ID of the group.
    * Returns:
      * The group with the corresponding group ID
    *   [Example:](example-scripts.md#get_group_by_id-group_id)

        ```
        group = get_group_by_id("123456")
        ```
21. **add\_table\_column(table, col\_name, default\_value=None)**
    * Description: Adds a column to the corresponding table.
    * Parameters:
      * table: The table where ehr column should be added.
      * col\_name: The name of the column.
      * default\_value (optional): The initial value for the field (default is an empty string).
    *   [Example:](example-scripts.md#add_table_column-table-col_name-default_value-none)

        ```
        add_table_column(table, "UNIT_PRICE_PER")
        ```
22. **get\_column\_value(row, column\_name, default\_value=None, is\_clean=False)**
    * Description: Gets a value from a specified column.
    * Parameters:
      * row: The row where the value is located.
      * col\_name: The name of the column.
      * default\_value (optional): Returns default\_value if no field value is found.
      * is\_clean (optional): Turns the value in uppercase and cleans it from empty spaces
    *   [Example:](example-scripts.md#get_column_value-row-column_name-default_value-none-is_clean-false)

        ```
        original_unit_price = get_column_value(row, "ORIGINAL_UNIT_PRICE")
        ```
23. **set\_column\_value(row, column\_name, value)**
    * Description: Sets a value from a specified column.
    * Parameters:
      * row: The row where the value is located.
      * col\_name: The name of the column.
      * value: The value that will be set at the specified location.
    * Returns:
      * True if the change was successful
    *   [Example:](example-scripts.md#set_column_value-row-column_name-value)

        ```
        success = set_column_value(row,"SUPPLIER_ID", supplier_id)
        ```
24. **set\_column\_date\_value(document\_data, row, column\_name, value, add\_days=0)**
    * Description: Sets a value from a specified column.
    * Parameters:
      * document\_data: The document data containing field information.
      * row: The row where the value is located.
      * col\_name: The name of the column.
      * value: The date value to set in ISO format (e.g., "2020-12-31").
      * add\_days (int): Add additional days to the given date.
    *   [Example:](example-scripts.md#set_column_date_value-document_data-row-column_name-value-add_days-0)

        ```
        set_column_date_value(document_data, row, "DELIVERY_DATE", "2020-12-31", add_days=2)
        ```
25. **set\_column\_amount\_value(document\_data, row, column\_name, value)**
    * Description: Does following actions
      * Convert value to string and set the value for the column
      * Set column content to the value
      * Format value according to the locale
    * Parameters:
      * document\_data (dict): The document data containing field information.
      * row : Row of the table line.
      * column\_name: Name of the column.
      * value: Value to be set
    *   [Example:](example-scripts.md#set_column_amount_value-document_data-row-column_name-value)

        ```
        set_column_amount_value(document_data, row, "UNIT_PRICE", str(unit_price))
        ```
26. **remove\_rows\_from\_table(document\_data, table\_name, count, start)**
    * Description: Removes rows from the specified table
    * Parameters:
      * document\_data (dict): The document data containing field information.
      * table\_name : The name of the table.
      * count: How many lines should be deleted.
      * start: The starting point.
    *   [Example:](example-scripts.md#remove_rows_from_table-document_data-table_name-count-start)

        ```
        remove_rows_from_table(document_data,"INVOICE_TABLE",count,start)   
        ```
27. **remove\_all\_rows\_except\_one\_from\_table(document\_data, line\_number)**
    * Description: Removes all rows except one from the specified table
    * Parameters:
      * document\_data (dict): The document data containing field information.
      * line\_number: The number of the line which should not be removed.
    *   [Example:](example-scripts.md#remove_all_rows_except_one_from_table-document_data-line_number)

        ```
        remove_all_rows_except_one_from_table(document_data, line_number) 
        ```



You can also utilize some of the python in-build functions:

* abs(): Returns the absolute value of a number.
* len(): Returns the length (number of items) of an object, like a list or string.
* isinstance(): Checks if an object is an instance of a particular class or type.
* print(): Prints output to the console.
* round(): Rounds a floating-point number to a specified number of decimal places.
* str\_to\_bool(): Converts a string to a boolean value (True or False).
* type(): Returns the type of an object.
* dict(): Creates a dictionary object.
* list(): Creates a list object.
* str(): Converts a value to a string.
* float(): Converts a value to a floating-point number.
* int(): Converts a value to an integer.

For more details, visit the official Python documentation: [Built-in Functions](https://docs.python.org/3.12/library/functions.html).

#### String Class Functions

You can also use these functions specifically for working with strings:

* lower(): Converts all characters in a string to lowercase.
* upper(): Converts all characters in a string to uppercase.
* split(): Splits a string into a list based on a delimiter (e.g., space or comma).
* startswith(): Checks if a string starts with a specified prefix.
* endswith(): Checks if a string ends with a specified suffix.
* strip(): Removes any leading or trailing whitespace from a string.

#### Functions from the Python Math Module

These functions are part of the math module and are useful for mathematical operations:

* floor(): Returns the largest integer less than or equal to a given number.
* ceil(): Returns the smallest integer greater than or equal to a given number.

For more information, check out the official Python documentation: [Math Module Functions](https://docs.python.org/3/library/math.html).

#### Regular Expression Function

* re.search(): Searches for a pattern within a string and returns the first match.

See more details here: [re.search Documentation](https://docs.python.org/3/library/re.html#re.search).

#### External Functions

Here are some useful functions from external libraries:

* deepcopy(): Creates a copy of an object, including nested objects (from the copy module).\
  [Deepcopy Documentation](https://docs.python.org/3/library/copy.html#copy.deepcopy).
* levenshtein\_distance(): Calculates the number of edits (insertions, deletions, substitutions) required to change one string into another. This function is available in the [Jellyfish library](https://jamesturk.github.io/jellyfish/functions/).

#### Date and Time Functions

You can use the following functions for working with dates and times:

* strptime(): Converts a string into a datetime object based on a specified format.
* strftime(): Formats a datetime object into a string based on a specified format.

For more information, check the official documentation:\
[Date and Time Functions](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior).
