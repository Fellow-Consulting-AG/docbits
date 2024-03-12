# Initiate Model Training with Docbits API

This documentation section outlines how to start the training process for an accounting model using the Docbits API. Model training is crucial for improving the accuracy and efficiency of automated accounting processes by teaching the system to recognize and categorize financial transactions correctly.

## Endpoint Information

- **URL**: `https://api.docbits.com/auto_accounting/model_train`
- **Method**: `POST`

## API Documentation

Access the OpenAPI documentation for detailed information on the API, including authentication requirements, request parameters, and response formats:

[Docbits OpenAPI Documentation](https://api.docbits.com/openapi.json)

## Sample Request

To begin training an accounting model, send a POST request to the endpoint. Replace `<your_access_token>` with your actual API access token. The request body should contain details about the training dataset and any specific configurations or parameters for the training session.

```http
POST /auto_accounting/model_train HTTP/1.1
Host: api.docbits.com
Authorization: Bearer <your_access_token>
Content-Type: application/json

{
  "trainingDatasetId": "your_dataset_id_here",
  "modelParameters": {
    // Optional parameters for customizing the training, such as model type, epochs, etc.
  }
}
```

{% swagger src="https://api.docbits.com/openapi.json" path="/auto_accounting/model_train" method="post" %}
[https://api.docbits.com/openapi.json](https://api.docbits.com/openapi.json)
{% endswagger %}
