# STRUCTURE v1.0 (Freeze)

This document captures the current repository structure as of the initial MVP bootstrap. This serves as a reference point for tracking what changed and why.

## 1. Repository Tree (High-Level)

```
m365-it-manager/
├── frontend/                    # React + Vite SPA
├── backend/                     # FastAPI application
├── infra/                       # Azure Bicep + deployment scripts
├── docs/                        # Living documentation
├── .cursor/rules/               # AI behavior rules (00-07)
├── DECISIONS/                   # Architecture Decision Records
├── tools/mcp/                   # Custom MCP tool manifests
├── .github/workflows/           # CI/CD pipelines
├── MVP_TASKS.md                 # Operational task tracking
├── CONTRIBUTING-CURSOR.md       # AI development protocol
├── CHANGELOG.md                 # User-facing change history
└── ROADMAP.md                   # Product evolution plan
```

## 2. INVARIANTS (Unchanging Rules)

- **Folder names and roles are fixed**. No renaming without Major version bump.
- **`.cursor/rules/` files numbered 00-07**. New rules require ADR before addition.
- **API changes must update `docs/API_SPEC.md`** (CI gate enforced).
- **Graph/SDK changes must update `docs/PERMISSIONS.md`** (CI gate enforced).
- **Task tracking happens only in `MVP_TASKS.md`**. No duplicate task systems.

## 3. File Contracts (Brief)

- **`backend/app/routers/*`** → FastAPI router standard (ref: `02-backend-standards.mdc`)
- **`frontend/src/components/*`** → UI component standard (ref: `01-frontend-standards.mdc`)
- **`DECISIONS/ADR-xxxx.md`** → Decision format following ADR template
- **`.cursor/rules/*`** → AI working rules with Scope/Non-goals sections
- **`docs/API_SPEC.md`** → OpenAPI-compatible endpoint documentation
- **`docs/PERMISSIONS.md`** → Graph API scopes with justification

## 4. How to Make Changes? (Summary; see CONTRIBUTING-CURSOR.md for details)

1. **For code changes**: Follow T-Task Protocol
2. **For structural changes**: 
   - First open an ADR
   - Fill `STRUCTURE_CHANGE.md` in PR
   - Pass CI structure checks

## 5. Versioning

- **Structural changes**: `STRUCTURE_vX.Y.md` (major/minor)
- **CHANGELOG.md** gets a "Structure" section for tracking
- **Minor (v1.1)**: Naming/clarity improvements, rule file splits (backward compatible)
- **Major (v2.0)**: Root folder changes, architectural layer moves (breaking changes, ADR required)

## 6. CI Enforcement Rules

1. **API Router Changes**: If `backend/app/routers/**` modified → `docs/API_SPEC.md` diff required
2. **Graph Integration Changes**: If `backend/**/graph*` or `**/client*` modified → `docs/PERMISSIONS.md` diff required  
3. **Structure Changes**: If folder structure under `frontend/`, `backend/`, `infra/`, `docs/`, `.cursor/` modified → `STRUCTURE_CHANGE.md` + ADR required

---

**Freeze Date**: Initial MVP Bootstrap  
**Next Review**: After first 5 T-Tasks completed
