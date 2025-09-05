# API Specification (MVP)

This document provides sample requests and responses for the MVP endpoints.

---

### Users

- **GET /users**
    - **Response:**
        ```json
        [
          { "id": "user1", "displayName": "User One", "userPrincipalName": "user1@tenant.com" }
        ]
        ```

- **POST /users**
    - **Request Body:**
        ```json
        { "displayName": "New User", "userPrincipalName": "new@tenant.com", "password": "..." }
        ```
    - **Response:** `201 Created`

- **DELETE /users/{id}**
    - **Response:** `204 No Content`

---

### Licenses

- **GET /licenses**
    - **Response:**
        ```json
        [
          { "userId": "user1", "skuId": "sku123", "skuPartNumber": "O365_E3" }
        ]
        ```
- **PATCH /licenses/{userId}**
    - **Request Body:**
        ```json
        { "add": ["sku456"], "remove": ["sku123"] }
        ```
    - **Response:** `200 OK`

---

### MFA

- **GET /mfa**
    - **Response:**
        ```json
        [
          { "userId": "user1", "userPrincipalName": "user1@tenant.com", "mfaStatus": "Enabled" },
          { "userId": "user2", "userPrincipalName": "user2@tenant.com", "mfaStatus": "Disabled" }
        ]
        ```

---

### Teams

- **GET /teams/active**
    - **Response:**
        ```json
        [
          { "userId": "user1", "displayName": "User One", "lastActivityDate": "2023-10-26" }
        ]
        ```

---

### Mailbox

- **GET /mailbox/usage**
    - **Response:**
        ```json
        [
          { "userPrincipalName": "user1@tenant.com", "storageUsedGB": 45.5, "storageQuotaGB": 50.0 }
        ]
        ```
