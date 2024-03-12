# Retrieve Document Layout with Docbits API

The `get_document_layout` endpoint allows users to retrieve the layout of a document, which includes details about the fields and data structure within the document. This guide will explain how to make a request to this endpoint and interpret the response.

## Endpoint Information

- **URL**: `https://api.docbits.com/field/get_document_layout`
- **Method**: `POST`

## API Documentation

For complete API documentation, including authentication methods, request schemas, and response formats, please visit:

[Docbits OpenAPI Documentation](https://api.docbits.com/openapi.json)

## Sample Request

To retrieve the layout of a specific document, you must send a POST request to the endpoint with the document's details. Below is an example request. Remember to replace `<your_access_token>` with your actual API access token and provide the necessary document details in the request body.

```http
POST /field/get_document_layout HTTP/1.1
Host: api.docbits.com
Authorization: Bearer <your_access_token>
Content-Type: application/json

{
  "documentId": "your_document_id_here",
  "options": {
    // Optional parameters to customize the request, if necessary
  }
}
```


{% swagger src="https://api.docbits.com/openapi.json" path="/field/get_document_layout" method="post" %}
[https://api.docbits.com/openapi.json](https://api.docbits.com/openapi.json)
{% endswagger %}
