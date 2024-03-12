# Classify Document with Docbits API

This documentation section describes how to use the Docbits API to classify a document. Document classification is a crucial step in organizing and managing documents by categorizing them into predefined classes or types based on their content.

## Endpoint Information

- **URL**: `https://api.docbits.com/classifier_v2/classify_document`
- **Method**: `POST`

## API Documentation

For comprehensive details on the API, including authentication, request structure, and response format, please visit:

[Docbits OpenAPI Documentation](https://api.docbits.com/openapi.json)

## Sample Request

To classify a document, you need to send a POST request to the endpoint with the document's content or relevant details. Replace `<your_access_token>` with your actual API access token. Below is an example of how the request body might look:

```http
POST /classifier_v2/classify_document HTTP/1.1
Host: api.docbits.com
Authorization: Bearer <your_access_token>
Content-Type: application/json

{
  "documentContent": "The full text of the document to be classified goes here.",
  "additionalParameters": {
    // Optional parameters for customization
  }
}
```

{% swagger src="https://api.docbits.com/openapi.json" path="/classifier_v2/classify_document" method="post" %}
[https://api.docbits.com/openapi.json](https://api.docbits.com/openapi.json)
{% endswagger %}
