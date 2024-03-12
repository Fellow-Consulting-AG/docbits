# Retrieve Detailed Information on Pending Tasks with Docbits API

This section explains how to use the Docbits API to fetch detailed information about pending tasks within the system. Accessing detailed task information can be invaluable for monitoring, debugging, and managing workload efficiently.

## Endpoint Information

- **URL**: `https://api.docbits.com/celery_tasks_manager/get_pending_tasks_detail_info`
- **Method**: `POST`

## API Documentation

For an in-depth overview of the API, including how to authenticate, specify request parameters, and understand response formats, refer to:

[Docbits OpenAPI Documentation](https://api.docbits.com/openapi.json)

## Sample Request

To query detailed information about pending tasks, you'll need to send a POST request with any necessary filters or identifiers. Replace `<your_access_token>` with your actual API access token. The body of the request can include parameters to filter the tasks based on your requirements.

```http
POST /celery_tasks_manager/get_pending_tasks_detail_info HTTP/1.1
Host: api.docbits.com
Authorization: Bearer <your_access_token>
Content-Type: application/json

{
  "filterOptions": {
    // Optional. Use to specify filtering criteria, such as task type, creation date, etc.
  }
}
```

{% swagger src="https://api.docbits.com/openapi.json" path="/celery_tasks_manager/get_pending_tasks_detail_info" method="post" %}
[https://api.docbits.com/openapi.json](https://api.docbits.com/openapi.json)
{% endswagger %}
