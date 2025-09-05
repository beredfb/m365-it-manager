# Azure Deployment Guide

This guide outlines the steps to deploy the M365 IT Manager Panel to Azure.

## Required Resources

- **Azure App Service**: To host the FastAPI backend and the React frontend (can be one or two App Services).
- **Azure Key Vault**: To store all application secrets, including the Azure AD App Registration client secret and other sensitive configuration.

## Environment Variable Mapping

The application is configured via environment variables. In Azure App Service, these are set in the **Configuration** section.

- `AZURE_TENANT_ID`: Your Azure AD Tenant ID.
- `AZURE_CLIENT_ID`: The Client ID of your Azure App Registration.
- `AZURE_CLIENT_SECRET`: The Client Secret from your App Registration (must be stored in Key Vault and referenced).
- `GRAPH_BASE_URL`: Should be `https://graph.microsoft.com/v1.0`.
- `ALLOWED_ORIGINS`: The URL of your frontend application.
- `VITE_API_BASE`: The URL of your backend API.

## Deployment Scripts

The `infra/scripts/` directory contains helper scripts for deployment:

- `deploy_api.sh`: Deploys the backend application to Azure App Service.
- `deploy_web.sh`: Builds and deploys the frontend application.
- `seed_keyvault.sh`: A helper script to add secrets to Azure Key Vault.

These scripts are placeholders and will need to be configured with your specific Azure resource names and details.
