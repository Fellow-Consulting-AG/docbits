# Update Group Details with Docbits API

This guide details the process for updating the information of an existing group within the Docbits system via the API. This can include changing the group's name, description, or other attributes.

## Endpoint Information

- **URL**: `https://api.docbits.com/groups/update/{group_id}`
- **Method**: `PUT`

## API Documentation

For a comprehensive look at the API, including authentication requirements, request parameters, and response objects, please refer to the OpenAPI documentation:

[Docbits OpenAPI Documentation](https://api.docbits.com/openapi.json)

## Sample Request

To update a group, you need to send a PUT request to the endpoint with the group's ID in the URL. Replace `{group_id}` with the ID of the group you intend to update and `<your_access_token>` with your API access token. The body of the request should contain the updated group details.

```http
PUT /groups/update/{group_id} HTTP/1.1
Host: api.docbits.com
Authorization: Bearer <your_access_token>
Content-Type: application/json

{
  "name": "Updated Group Name",
  "description": "Updated group description detailing the purpose and members."
}
```

{% swagger src="https://api.docbits.com/openapi.json" path="/groups/update/{group_id}" method="put" %}
[https://api.docbits.com/openapi.json](https://api.docbits.com/openapi.json)
{% endswagger %}
