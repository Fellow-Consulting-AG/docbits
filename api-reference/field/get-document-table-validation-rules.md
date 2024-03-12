# Retrieve Document Table Validation Rules with Docbits API

This guide explains how to use the Docbits API to retrieve the validation rules for tables within a document. This feature is crucial for understanding how data within table structures is validated, ensuring data integrity and consistency.

## Endpoint Information

- **URL**: `https://api.docbits.com/field/get_document_table_validation_rules`
- **Method**: `GET`

## API Documentation

For a detailed overview of the API, including authentication details, request formats, and response objects, refer to:

[Docbits OpenAPI Documentation](https://api.docbits.com/openapi.json)

## Requesting Validation Rules

To retrieve the validation rules for document tables, a GET request should be sent to the endpoint. This request doesn't require a body but may need parameters or headers for authentication, depending on the API's design.

```http
GET /field/get_document_table_validation_rules HTTP/1.1
Host: api.docbits.com
Authorization: Bearer <your_access_token>


{% swagger src="https://api.docbits.com/openapi.json" path="/field/get_document_table_validation_rules" method="get" %}
[https://api.docbits.com/openapi.json](https://api.docbits.com/openapi.json)
{% endswagger %}
