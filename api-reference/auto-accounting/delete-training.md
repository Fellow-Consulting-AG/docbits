# Delete Training Data with Docbits API

This section of the documentation provides a step-by-step guide on how to delete existing training data from the Docbits system via the API. Removing training data can be necessary for various reasons, such as updating the dataset with more accurate information or clearing outdated data.

## Endpoint Information

- **URL**: `https://api.docbits.com/auto_accounting/delete_training`
- **Method**: `DELETE`

## API Documentation

For detailed API documentation, including authentication methods, parameter requirements, and response formats, please refer to:

[Docbits OpenAPI Documentation](https://api.docbits.com/openapi.json)

## Sample Request

To delete specific training data, a DELETE request should be sent to the endpoint. This request may need to include identifiers for the training data you wish to delete. Replace `<your_access_token>` with your actual API access token.

```http
DELETE /auto_accounting/delete_training HTTP/1.1
Host: api.docbits.com
Authorization: Bearer <your_access_token>
Content-Type: application/json

{
  "trainingDataId": "your_training_data_id_here"
}
```

{% swagger src="https://api.docbits.com/openapi.json" path="/auto_accounting/delete_training" method="delete" %}
[https://api.docbits.com/openapi.json](https://api.docbits.com/openapi.json)
{% endswagger %}
