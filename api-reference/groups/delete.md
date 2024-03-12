# Delete Group with Docbits API

This guide provides instructions on how to delete a group from the Docbits system via the API. This action is irreversible, so ensure that the group is no longer needed before proceeding.

## Endpoint Information

- **URL**: `https://api.docbits.com/groups/delete/{group_id}`
- **Method**: `DELETE`

## API Documentation

For a comprehensive overview of the API, including authentication, parameter requirements, and response details, refer to the OpenAPI documentation:

[Docbits OpenAPI Documentation](https://api.docbits.com/openapi.json)

## Sample Request

When deleting a group, you must specify the group's unique ID in the URL. Replace `{group_id}` with the actual ID of the group you wish to delete and `<your_access_token>` with your valid API access token.

```http
DELETE /groups/delete/{group_id} HTTP/1.1
Host: api.docbits.com
Authorization: Bearer <your_access_token>
```

{% swagger src="https://api.docbits.com/openapi.json" path="/groups/delete/{group_id}" method="delete" %}
[https://api.docbits.com/openapi.json](https://api.docbits.com/openapi.json)
{% endswagger %}
