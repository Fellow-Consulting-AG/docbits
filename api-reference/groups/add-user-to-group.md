# Add User to Group with Docbits API

This guide will walk you through the process of adding a user to a group within the Docbits system using the API. This operation can be crucial for managing access and permissions for different users in your organization.

## Endpoint Information

- **URL**: `https://api.docbits.com/groups/add_user_to_group`
- **Method**: `POST`

## API Documentation

For complete details on the API, including authentication, request parameters, and response formats, check out the OpenAPI documentation:

[Docbits OpenAPI Documentation](https://api.docbits.com/openapi.json)

## Sample Request

Here's how to structure your request to add a user to a group. Ensure you replace `<your_access_token>` with your actual API access token, and adjust the `userId` and `groupId` to match the user and group you're working with.

```http
POST /groups/add_user_to_group HTTP/1.1
Host: api.docbits.com
Authorization: Bearer <your_access_token>
Content-Type: application/json

{
  "userId": "user_123",
  "groupId": "group_456"
}
```



{% swagger src="https://api.docbits.com/openapi.json" path="/groups/add_user_to_group" method="post" %}
[https://api.docbits.com/openapi.json](https://api.docbits.com/openapi.json)
{% endswagger %}
