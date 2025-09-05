# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Fixed (GAP Analysis - P0 Items)
- **ENV standardization**: Removed `env.tmp`, added proper `.env.example` template
- **Azure AD Integration**: Granted admin consent for Microsoft Graph scopes
  - Delegated permissions: `User.ReadWrite.All`, `Directory.ReadWrite.All`, `Reports.Read.All`, `Group.Read.All`, `User.Read`
  - App Registration: `m365it-backend` configured and approved
- **Local Development**: Added `.env` to `.gitignore`, established local/production secret management pattern

### Improved (GAP Analysis - P1 Items)
- **Testing Infrastructure**: Added `pytest-cov`, `pytest-asyncio`, and `pytest.ini` configuration
- **CI/CD Enhancement**: Enhanced backend workflow with lint (flake8), coverage gates (80% minimum), and Codecov integration
- **Frontend CI**: Added lint, type-check, test, and build steps to frontend workflow with comprehensive npm scripts
- **Code Quality**: Updated all `.cursor/rules/*.mdc` files with proper Scope/Non-goals sections for better AI guidance

### Structure
- Added `STRUCTURE_v1.0.md` - Repository structure freeze documentation
- Added `STRUCTURE_CHANGE.md` - Template for structural change requests
- Updated `CONTRIBUTING-CURSOR.md` with Structure Freeze protocol
- Refactored `.cursor/rules/` to new 00-07 naming convention
  - `00-project-guardrails.mdc` → `00-ground-rules.mdc`
  - `04-testing-and-ci.mdc` → `06-testing.mdc`
  - Added `04-db-standards.mdc`, `05-infra-standards.mdc`, `07-docs-style.mdc`

### Added
- Initial MVP project bootstrap
- FastAPI backend structure with placeholder routers
- React + Vite frontend structure with placeholder pages
- Azure deployment infrastructure (Bicep templates)
- Comprehensive documentation suite
- GitHub Actions CI/CD workflows
- MCP tool manifests for Graph API integration

### Documentation
- Created architectural decision records (ADRs)
- Established API specification format
- Defined Microsoft Graph permissions model
- Added deployment and app registration guides

## [1.0.0] - Initial Release

### Added
- Complete project structure for M365 IT Manager Panel MVP
- Backend: FastAPI with routers for Users, Licenses, MFA, Teams, Mailbox
- Frontend: React SPA with placeholder pages and components
- Infrastructure: Azure Bicep templates and deployment scripts
- Documentation: Comprehensive docs for architecture, API, permissions
- Development: Cursor AI-assisted development protocol
- CI/CD: GitHub Actions workflows for testing and deployment
