# Get Pending Tasks Count with Docbits API

This section of the documentation is designed to guide you through the process of retrieving the count of pending tasks within the Docbits system using the API. Knowing the number of pending tasks can be crucial for monitoring workload and system performance.

## Endpoint Information

- **URL**: `https://api.docbits.com/celery_tasks_manager/get_pending_tasks_count`
- **Method**: `POST`

## API Documentation

For more detailed information on the API, including authentication details, required request formats, and expected response structures, please refer to:

[Docbits OpenAPI Documentation](https://api.docbits.com/openapi.json)

## Sample Request

To retrieve the count of pending tasks, you will need to send a POST request to the endpoint. This request may include specific parameters to filter the tasks by type, status, or other criteria. Replace `<your_access_token>` with your actual API access token.

```http
POST /celery_tasks_manager/get_pending_tasks_count HTTP/1.1
Host: api.docbits.com
Authorization: Bearer <your_access_token>
Content-Type: application/json

{
  "filterOptions": {
    // Optional filters, such as task type or other identifiers
  }
}
```

{% swagger src="https://api.docbits.com/openapi.json" path="/celery_tasks_manager/get_pending_tasks_count" method="post" %}
[https://api.docbits.com/openapi.json](https://api.docbits.com/openapi.json)
{% endswagger %}
