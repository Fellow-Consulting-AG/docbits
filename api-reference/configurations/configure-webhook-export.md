# Configure Webhook Export with Docbits API

This documentation section details the steps required to configure webhook export settings via the Docbits API. Webhooks are user-defined HTTP callbacks, which are triggered by specific events in a system. Configuring webhook exports allows you to automate the process of sending data or notifications to other applications or services in real-time.

## Endpoint Information

- **URL**: `https://api.docbits.com/configurations/configure_webhook_export`
- **Method**: `POST`

## API Documentation

Access comprehensive API details, including how to authenticate and format requests and responses, by referring to:

[Docbits OpenAPI Documentation](https://api.docbits.com/openapi.json)

## Sample Request

To set up or update your webhook export configurations, send a POST request to the endpoint. Ensure you replace `<your_access_token>` with your actual API access token. The request body should detail the webhook settings you wish to apply.

```http
POST /configurations/configure_webhook_export HTTP/1.1
Host: api.docbits.com
Authorization: Bearer <your_access_token>
Content-Type: application/json

{
  "webhookUrl": "https://your.webhook.url/endpoint",
  "eventTriggers": ["DocumentCreated", "DocumentUpdated"],
  "security": {
    "method": "BearerToken",
    "token": "your_secure_token"
  },
  "additionalOptions": {
    // Optional parameters such as headers or specific data formats
  }
}
```

{% swagger src="https://api.docbits.com/openapi.json" path="/configurations/configure_webhook_export" method="post" %}
[https://api.docbits.com/openapi.json](https://api.docbits.com/openapi.json)
{% endswagger %}
