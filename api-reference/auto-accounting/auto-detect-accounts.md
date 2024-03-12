# Automatically Detect Accounts with Docbits API

This section provides detailed instructions on how to use the Docbits API for automatically detecting accounts in your documents. This feature leverages advanced algorithms to identify and categorize accounts based on the document content, streamlining the accounting process.

## Endpoint Information

- **URL**: `https://api.docbits.com/auto_accounting/auto_detect_accounts`
- **Method**: `POST`

## API Documentation

Refer to the OpenAPI documentation for a comprehensive overview of the API, including details on authentication, required parameters, and the structure of response objects:

[Docbits OpenAPI Documentation](https://api.docbits.com/openapi.json)

## Sample Request

To initiate the automatic account detection, you need to send a POST request to the endpoint. Replace `<your_access_token>` with your valid API access token. The request body should include the document details or identifiers necessary for account detection.

```http
POST /auto_accounting/auto_detect_accounts HTTP/1.1
Host: api.docbits.com
Authorization: Bearer <your_access_token>
Content-Type: application/json

{
  "documentId": "your_document_id_here",
  "options": {
    // Optional parameters to customize the detection process
  }
}
```

{% swagger src="https://api.docbits.com/openapi.json" path="/auto_accounting/auto_detect_accounts" method="post" %}
[https://api.docbits.com/openapi.json](https://api.docbits.com/openapi.json)
{% endswagger %}
