# Health Check Endpoint (`/healthz`)

Our `/healthz` endpoint is your go-to for a quick pulse check on our API. Simply put, it's like asking, "Hey API, feeling alright?" and getting a straightforward "All good!" in response.

### How it works:

- **Method:** GET
- **Path:** `/healthz`
- **Purpose:** Provides an immediate status report on the health of our API.
- **Returns:** A simple response indicating the API is operational.

When you send a GET request to this endpoint, our system performs a quick health check. If everything is running smoothly, you'll receive a positive response. This ensures that our services are up and running, ready to serve your needs.

**Usage:** Ideal for monitoring systems or automated checks to ensure our API is accessible and functioning properly.

For more details, check out our OpenAPI documentation here: [https://api.docbits.com/openapi.json](https://api.docbits.com/openapi.json).
