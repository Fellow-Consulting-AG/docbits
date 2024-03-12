# Create Group with Docbits API

Creating a group in the Docbits system via the API allows for efficient management and organization of users and permissions. Follow this guide to understand how to create a new group.

## Endpoint Information

- **URL**: `https://api.docbits.com/groups/create`
- **Method**: `POST`

## API Documentation

Refer to the OpenAPI documentation for a detailed overview of the API, including authentication details, required parameters, and the structure of response objects:

[Docbits OpenAPI Documentation](https://api.docbits.com/openapi.json)

## Sample Request

To create a group, you need to send a POST request with the name of the group and, optionally, a description. Replace `<your_access_token>` with your actual API access token. Adjust the `name` and `description` fields as needed for your group.

```http
POST /groups/create HTTP/1.1
Host: api.docbits.com
Authorization: Bearer <your_access_token>
Content-Type: application/json

{
  "name": "New User Group",
  "description": "This group is for new users in the system."
}
```


{% swagger src="https://api.docbits.com/openapi.json" path="/groups/create" method="post" %}
[https://api.docbits.com/openapi.json](https://api.docbits.com/openapi.json)
{% endswagger %}
