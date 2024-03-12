# Automatically Extract Table Data with Docbits API

This section of the documentation details how to use the Docbits API to automatically extract table data from documents. This functionality is invaluable for parsing and analyzing structured data contained within a variety of document formats.

## Endpoint Information

- **URL**: `https://api.docbits.com/table_extraction/auto_extract_table`
- **Method**: `POST`

## API Documentation

To get a comprehensive overview of the API, including authentication, request parameters, and response formats, please consult:

[Docbits OpenAPI Documentation](https://api.docbits.com/openapi.json)

## Sample Request

To initiate table extraction, you need to send a POST request to the endpoint. This request should include the document content or a reference to the document stored within the Docbits system. Replace `<your_access_token>` with your actual API access token. Here's an example request:

```http
POST /table_extraction/auto_extract_table HTTP/1.1
Host: api.docbits.com
Authorization: Bearer <your_access_token>
Content-Type: application/json

{
  "documentId": "your_document_id_here",
  // Optionally, include direct document content or a URL to the document
  "options": {
    // Additional options such as page numbers to extract tables from
  }
}
```

{% swagger src="https://api.docbits.com/openapi.json" path="/table_extraction/auto_extract_table" method="post" %}
[https://api.docbits.com/openapi.json](https://api.docbits.com/openapi.json)
{% endswagger %}
