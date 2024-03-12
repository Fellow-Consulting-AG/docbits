# Test Auto Accounting Model with Docbits API

This documentation section guides you through the process of testing an auto accounting model via the Docbits API. Testing the model before deployment ensures its accuracy and effectiveness in automatically categorizing and processing accounting data.

## Endpoint Information

- **URL**: `https://api.docbits.com/auto_accounting/auto_accounting_model_test`
- **Method**: `POST`

## API Documentation

For detailed information about the API, including authentication procedures, request schema, and response objects, please consult the OpenAPI documentation:

[Docbits OpenAPI Documentation](https://api.docbits.com/openapi.json)

## Sample Request

To test the auto accounting model, you need to send a POST request with a sample document or data. Replace `<your_access_token>` with your actual API access token. The body of the request should include the necessary information to test the model effectively.

```http
POST /auto_accounting/auto_accounting_model_test HTTP/1.1
Host: api.docbits.com
Authorization: Bearer <your_access_token>
Content-Type: application/json

{
  "documentId": "sample_document_id",
  "additionalParameters": {
    // Optional parameters for the test
  }
}
```

{% swagger src="https://api.docbits.com/openapi.json" path="/auto_accounting/auto_accounting_model_test" method="post" %}
[https://api.docbits.com/openapi.json](https://api.docbits.com/openapi.json)
{% endswagger %}
