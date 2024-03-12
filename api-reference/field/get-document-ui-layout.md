# Retrieve Document UI Layout with Docbits API

This documentation section explains how to fetch the UI layout of a document through the Docbits API. The UI layout includes details on how document fields are arranged and displayed, which is crucial for applications that aim to present or collect data in a user-friendly manner.

## Endpoint Information

- **URL**: `https://api.docbits.com/field/get_document_ui_layout`
- **Method**: `GET`

## API Documentation

To get an in-depth understanding of the API, including authentication methods, parameter requirements, and response formats, please refer to:

[Docbits OpenAPI Documentation](https://api.docbits.com/openapi.json)

## Making a Request

A GET request to this endpoint retrieves the UI layout for a specific document. The request might require specific headers for authentication or additional query parameters to specify the document in question.

```http
GET /field/get_document_ui_layout HTTP/1.1
Host: api.docbits.com
Authorization: Bearer <your_access_token>
```

{% swagger src="https://api.docbits.com/openapi.json" path="/field/get_document_ui_layout" method="get" %}
[https://api.docbits.com/openapi.json](https://api.docbits.com/openapi.json)
{% endswagger %}
