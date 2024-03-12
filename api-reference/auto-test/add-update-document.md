# Add or Update a Document with Docbits API

This section explains how to use the Docbits API to either add a new document or update an existing one within the system. This functionality is crucial for maintaining an up-to-date document repository, ensuring data accuracy and relevance.

## Endpoint Information

- **URL**: `https://api.docbits.com/auto_test/add_update_document`
- **Method**: `POST`

## API Documentation

For detailed information on the API, including authentication methods, request schemas, and response objects, visit the OpenAPI documentation:

[Docbits OpenAPI Documentation](https://api.docbits.com/openapi.json)

## Sample Request

Below is an example of a POST request to add a new document or update an existing one. Make sure to replace `<your_access_token>` with your actual API access token. The request body should include details about the document you're adding or updating.

```http
POST /auto_test/add_update_document HTTP/1.1
Host: api.docbits.com
Authorization: Bearer <your_access_token>
Content-Type: application/json

{
  "documentId": "optional_document_id_for_update",
  "documentData": {
    "title": "Sample Document Title",
    "content": "The content of the document...",
    // Other document-specific data fields
  },
  "metadata": {
    // Optional metadata about the document
  }
}
```

{% swagger src="https://api.docbits.com/openapi.json" path="/auto_test/add_update_document" method="post" %}
[https://api.docbits.com/openapi.json](https://api.docbits.com/openapi.json)
{% endswagger %}
