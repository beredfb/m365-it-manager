# ADR-0001: System Architecture

## Status

Accepted

## Context

We need a simple, scalable, and secure architecture for the M365 IT Manager Panel. The primary goal is to provide a web-based interface for IT administrators to perform common user and license management tasks via the Microsoft Graph API.

## Decision

We will adopt a modern Single-Page Application (SPA) architecture with a separate backend API.

- **Frontend**: A React SPA (built with Vite) will provide a responsive and interactive user experience.
- **Backend**: A FastAPI (Python) backend will serve as an intermediary between the frontend and the Microsoft Graph API.
- **Data Flow**: The frontend will make authenticated requests to our backend API. The backend will be responsible for all interactions with the Microsoft Graph API, ensuring that no Graph tokens or sensitive logic are exposed to the client.

## Consequences

- **Pros**:
    - **Security**: Isolates Graph API access to the backend, preventing token exposure.
    - **Scalability**: Frontend and backend can be scaled independently.
    - **Maintainability**: Clear separation of concerns between presentation (frontend) and business logic (backend).
- **Cons**:
    - **Complexity**: Requires managing two separate application stacks (React/Node and FastAPI/Python).
    - **Latency**: Introduces an extra network hop for all data requests to the Graph API.
