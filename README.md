# M365 IT Manager Panel – MVP

This project is a minimal viable product (MVP) to manage common M365 IT tasks for Users, Licenses, MFA, Teams, and Mailbox quotas.

## Quickstart

### Backend

```bash
# Navigate to the backend directory
cd backend

# Create a virtual environment and install dependencies
uv venv
uv pip install -r requirements.txt

# Run the FastAPI development server
uv run fastapi dev app/main.py
```

### Frontend

```bash
# Navigate to the frontend directory
cd frontend

# Install dependencies
pnpm i

# Run the Vite development server
pnpm dev
```

## Testing

To run the test suites for the applications:

- **Backend:** `pytest -q backend/tests`
- **Frontend:** `pnpm test`

## Deployment

Deployment scripts for Azure are located in the `infra/scripts` directory. See `docs/DEPLOYMENT_AZURE.md` for more details.

## Security

This application uses delegated Microsoft Graph API scopes. All application secrets and sensitive configuration are managed in Azure Key Vault.
