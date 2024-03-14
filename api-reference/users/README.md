# User Management APIs Overview

The User Management APIs provide essential functionality for creating, retrieving, and managing user accounts within the system. These APIs allow administrators to maintain user data, including personal information and access control.

### Endpoints

#### Get Users

* **Endpoint**: `GET /users/get_users`
* **Description**: Retrieves a list of users within the system. This endpoint can be used to display registered users and their details.

#### Create User

* **Endpoint**: `POST /users/create`
* **Description**: Creates a new user account. This API is crucial for adding new users to the system, specifying their roles, and setting initial access permissions.
* **RequestBody**: Encoded form data including user details such as first name, last name, email, password, and administrative privileges.

#### Delete User

* **Endpoint**: `DELETE /users/delete/{user_id}`
* **Description**: Deletes a specific user from the system based on their unique user ID. This endpoint is used for managing user lifecycle and removing access when necessary.
* **Parameters**:
  * `user_id`: The unique identifier of the user to be deleted.

### Security

All User Management APIs require API key authentication. Ensure your API key is properly included in the request header to authenticate and authorize the operation.

### Usage

The User Management APIs are integral to the system's administration, allowing for the effective control over user access and account management. Through these APIs, administrators can ensure that only authorized users have access to the system and manage user accounts according to organizational policies and requirements.
