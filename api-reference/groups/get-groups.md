# Retrieve Groups with Docbits API

This guide outlines the steps to retrieve a list of all groups within the Docbits system using the API. This endpoint is useful for managing group memberships and permissions.

## Endpoint Information

- **URL**: `https://api.docbits.com/groups/get_groups`
- **Method**: `GET`

## API Documentation

For detailed API documentation, including information on authentication, parameters, and response formats, visit:

[Docbits OpenAPI Documentation](https://api.docbits.com/openapi.json)

## Sample Request

To get a list of groups, send a GET request to the endpoint. Ensure to replace `<your_access_token>` with your actual API access token.

```http
GET /groups/get_groups HTTP/1.1
Host: api.docbits.com
Authorization: Bearer <your_access_token>
```

{% swagger src="https://api.docbits.com/openapi.json" path="/groups/get_groups" method="get" %}
[https://api.docbits.com/openapi.json](https://api.docbits.com/openapi.json)
{% endswagger %}
