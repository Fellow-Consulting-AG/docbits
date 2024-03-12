# Configure BOD Export with Docbits API

This section of the documentation provides detailed instructions on configuring the export settings for Business Object Documents (BOD) using the Docbits API. BOD exports are crucial for integrating business processes and data exchange between different systems.

## Endpoint Information

- **URL**: `https://api.docbits.com/configurations/configure_bod_export`
- **Method**: `POST`

## API Documentation

For a complete guide on the API, including authentication methods, request formats, and response details, please refer to:

[Docbits OpenAPI Documentation](https://api.docbits.com/openapi.json)

## Sample Request

To configure the BOD export settings, you need to send a POST request to the endpoint. Replace `<your_access_token>` with your actual API access token. The request body should include the configuration parameters for the BOD export.

```http
POST /configurations/configure_bod_export HTTP/1.1
Host: api.docbits.com
Authorization: Bearer <your_access_token>
Content-Type: application/json

{
  "exportConfig": {
    "targetSystem": "Target system name",
    "exportFormat": "XML/JSON",
    "additionalOptions": {
      // Optional configuration parameters
    }
  }
}
```

{% swagger src="https://api.docbits.com/openapi.json" path="/configurations/configure_bod_export" method="post" %}
[https://api.docbits.com/openapi.json](https://api.docbits.com/openapi.json)
{% endswagger %}
