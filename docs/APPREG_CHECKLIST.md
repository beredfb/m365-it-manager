# Azure App Registration Checklist

Follow these steps to create and configure the required Azure AD App Registration.

### 1. Create App Registration
- Go to **Azure Active Directory > App registrations > New registration**.
- Give it a descriptive name (e.g., `M365-IT-Manager-Panel`).
- Select **Accounts in this organizational directory only**.

### 2. Configure Redirect URIs
- Go to **Authentication**.
- Add a **Web** platform.
- Add the Redirect URI for your local development environment (e.g., `http://localhost:5173`) and your deployed frontend URL.

### 3. Add API Permissions (Scopes)
- Go to **API permissions**.
- Click **Add a permission > Microsoft Graph > Delegated permissions**.
- Add the following scopes:
    - `User.ReadWrite.All`
    - `Directory.ReadWrite.All`
    - `Reports.Read.All`
    - `Group.Read.All`
- **Crucial**: After adding permissions, click the **Grant admin consent for [Your Tenant]** button.

### 4. Configure CORS
- Ensure the `ALLOWED_ORIGINS` environment variable on your backend matches the URL of your frontend to prevent Cross-Origin Resource Sharing (CORS) errors.

### 5. Create Client Secret (if not using PKCE exclusively)
- If your authentication flow requires a client secret:
    - Go to **Certificates & secrets > Client secrets > New client secret**.
    - **Important**: Copy the secret **value** immediately. It will not be visible again.
    - Store this secret securely in Azure Key Vault. **Do not** commit it to source control.

### 6. Test the Connection
- After configuration, a simple test is to make a request to the `/v1.0/me` endpoint in the Graph API. A successful `200 OK` response with your user profile confirms that the basic authentication flow is working.
