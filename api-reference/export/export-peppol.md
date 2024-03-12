# Export Documents in PEPPOL Format with Docbits API

This section of the documentation details how to export documents to the PEPPOL format using the Docbits API. PEPPOL is a set of standards that enables electronic business documentation exchange (such as invoices) across different countries and sectors. Follow the steps below to export your documents efficiently.

## Endpoint Information

- **URL**: `https://api.docbits.com/export/export_peppol`
- **Method**: `GET`

## API Documentation

For comprehensive details about the API, including how to authenticate, required parameters, and response formats, refer to the OpenAPI documentation:

[Docbits OpenAPI Documentation](https://api.docbits.com/openapi.json)

## Making a Request

To export a document in PEPPOL format, you will need to send a GET request to the endpoint. This request may require specific headers for authentication and query parameters to specify the document you wish to export.

```http
GET /export/export_peppol?documentId=<your_document_id> HTTP/1.1
Host: api.docbits.com
Authorization: Bearer <your_access_token>
```

{% swagger src="https://api.docbits.com/openapi.json" path="/export/export_peppol" method="get" %}
[https://api.docbits.com/openapi.json](https://api.docbits.com/openapi.json)
{% endswagger %}
