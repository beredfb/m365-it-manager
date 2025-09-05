# ADR-0002: Authentication and Permissions Model

## Status

Accepted

## Context

The application must securely authenticate users and be authorized to call the Microsoft Graph API on their behalf. We need to follow the principle of least privilege, requesting only the permissions necessary for the MVP features.

## Decision

We will use the **delegated permissions** model with **OAuth 2.0 Authorization Code Flow with PKCE**.

- **Authentication**: Users will authenticate against Azure Active Directory (AAD).
- **Authorization**: The application will request a specific set of delegated permissions (scopes) which require administrator consent.
- **Token Flow**: The backend will handle the token exchange. We prefer the Authorization Code flow with PKCE as it is the most secure option for applications with a backend, mitigating the risk of authorization code interception. If a client secret is required for a specific flow, it must be stored securely in Azure Key Vault, never in application code or configuration files.

## Consequences

- **Pros**:
    - **Security**: Operations are performed within the context of the signed-in user, providing a clear audit trail. Adheres to the principle of least privilege. PKCE adds a layer of security for the auth flow.
    - **User Experience**: Leverages existing AAD accounts for seamless sign-on.
- **Cons**:
    - **Setup Complexity**: Requires an Azure App Registration with correctly configured redirect URIs, scopes, and admin consent.
    - **Dependency**: Tightly coupled to Azure Active Directory for authentication.
