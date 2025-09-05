# System Architecture

This document outlines the architecture of the M365 IT Manager Panel.

## Pattern: SPA + Backend for Frontend (BFF)

We use a Single-Page Application (SPA) architecture.

- **Frontend**: A React SPA built with Vite and `shadcn/ui`. It is responsible for the user interface and all presentation logic.
- **Backend**: A FastAPI application that serves two purposes:
    1.  Acts as a **Backend for Frontend (BFF)**, providing a tailored API for our React client.
    2.  Acts as a **secure proxy** for all Microsoft Graph API calls.

## Graph API Access

All interactions with the Microsoft Graph API are handled exclusively by the backend. The frontend **never** calls the Graph API directly. This design ensures that access tokens and sensitive application logic are kept secure on the server side.

## API Endpoints (MVP)

The backend exposes the following RESTful endpoints for the frontend:

- `GET, POST, DELETE /users`
- `GET, PATCH /licenses`
- `GET /mfa`
- `GET /teams/active`
- `GET /mailbox/usage`

## Error Handling

The backend API uses the **RFC7807 problem+json** standard for reporting errors. This provides a consistent and machine-readable error format for the frontend to consume.

Example Error Response:
```json
{
  "type": "https://example.com/probs/out-of-credit",
  "title": "You do not have enough credit.",
  "status": 403,
  "detail": "Your current balance is 30, but that costs 50.",
  "instance": "/account/12345/msgs/abc"
}
```
