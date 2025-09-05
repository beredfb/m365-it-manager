# Application Permissions

This document lists the Microsoft Graph API permissions required for the application to function.

## Principle of Least Privilege

We adhere to the principle of least privilege. The application should only request the permissions it absolutely needs for its features.

## Delegated Permissions (MVP)

For the MVP, the following **delegated** scopes are required. An administrator must grant consent to these permissions in the Azure App Registration.

- **`User.ReadWrite.All`**
    - **Why**: To read, create, and delete user profiles.
- **`Directory.ReadWrite.All`**
    - **Why**: To manage directory objects, primarily for assigning and removing licenses.
- **`Reports.Read.All`**
    - **Why**: To read usage reports, such as Teams activity and mailbox usage.
- **`Group.Read.All`** (or a more specific `Team` scope if sufficient)
    - **Why**: To read basic team properties and membership for activity reports.

## Admin Consent

All the permissions listed above require **admin consent**. An administrator for the Azure AD tenant must grant consent on behalf of the organization before the application can be used.
