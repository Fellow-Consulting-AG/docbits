# Automatically Detect Supplier Accounts with Docbits API

This guide outlines the steps to use the Docbits API for automatically detecting supplier accounts in your documents. This functionality is particularly useful for streamlining invoice processing and enhancing accounting efficiency by identifying and categorizing supplier-related financial data.

## Endpoint Information

- **URL**: `https://api.docbits.com/auto_accounting/auto_detect_supplier_accounts`
- **Method**: `POST`

## API Documentation

For comprehensive details on the API, including how to authenticate, the required parameters for requests, and the format of responses, please visit:

[Docbits OpenAPI Documentation](https://api.docbits.com/openapi.json)

## Sample Request

To automatically detect supplier accounts, you will need to send a POST request to the endpoint. Ensure to replace `<your_access_token>` with your actual API access token. The request body should contain details or identifiers necessary for the detection process.

```http
POST /auto_accounting/auto_detect_supplier_accounts HTTP/1.1
Host: api.docbits.com
Authorization: Bearer <your_access_token>
Content-Type: application/json

{
  "documentId": "your_document_id_here",
  "additionalOptions": {
    // Optional parameters for enhanced detection
  }
}
```

{% swagger src="https://api.docbits.com/openapi.json" path="/auto_accounting/auto_detect_supplier_accounts" method="post" %}
[https://api.docbits.com/openapi.json](https://api.docbits.com/openapi.json)
{% endswagger %}
