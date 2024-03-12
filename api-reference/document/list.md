# List Documents with Docbits API

This section of the documentation explains how to retrieve a list of documents from the Docbits system using the API. This operation is essential for managing and accessing documents programmatically.

## Endpoint Information

- **URL**: `https://api.docbits.com/document/list`
- **Method**: `GET`

## API Documentation

For comprehensive details on the API, including how to authenticate, the parameters you can use to filter the list, and the format of responses, refer to:

[Docbits OpenAPI Documentation](https://api.docbits.com/openapi.json)

## Making a Request

To list documents, you'll need to send a GET request to the endpoint. You can include query parameters to filter the results based on your requirements. Here is a basic example of a request to list documents. Ensure you replace `<your_access_token>` with your actual API access token.

```http
GET /document/list HTTP/1.1
Host: api.docbits.com
Authorization: Bearer <your_access_token>
```

{% swagger src="https://api.docbits.com/openapi.json" path="/document/list" method="get" %}
[https://api.docbits.com/openapi.json](https://api.docbits.com/openapi.json)
{% endswagger %}
