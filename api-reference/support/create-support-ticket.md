# Create Support Ticket with Docbits API

To create a support ticket through the Docbits API, follow these steps. This will help in submitting your issues or queries directly to the support team.

## Endpoint Information

- **URL**: `https://api.docbits.com/support/create_support_ticket`
- **Method**: `POST`

## API Documentation

For detailed API documentation, including required payloads, authentication methods, and response objects, visit the OpenAPI documentation:

[Docbits OpenAPI Documentation](https://api.docbits.com/openapi.json)

## Sample Request

Below is a sample request to guide you through creating a support ticket. Make sure to replace `<your_access_token>` with your actual API access token and adjust the payload according to your specific needs.

```http
POST /support/create_support_ticket HTTP/1.1
Host: api.docbits.com
Authorization: Bearer <your_access_token>
Content-Type: application/json

{
  "title": "Issue with Document Extraction",
  "description": "Having trouble with extracting data from invoices.",
  "priority": "high"
}


{% swagger src="https://api.docbits.com/openapi.json" path="/support/create_support_ticket" method="post" %}
[https://api.docbits.com/openapi.json](https://api.docbits.com/openapi.json)
{% endswagger %}
