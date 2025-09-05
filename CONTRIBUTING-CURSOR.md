# Cursor AI-Assisted Development Protocol

This document outlines the strict protocol for AI-assisted development using Cursor to ensure consistency, efficiency, and maintainability.

---

# 1) Live Documents (Updated Every Sprint)

These are the "living" documents of the project.

- **`MVP_TASKS.md`**: Task status (todo/in-progress/done), linked PR/commit.
- **`docs/API_SPEC.md`**: For any endpoint additions or modifications.
- **`docs/PERMISSIONS.md`**: For new Microsoft Graph or other third-party permissions.
- **`DECISIONS/ADR-XXXX.md`**: For architectural or strategic decisions, providing retroactive justification.
- **`CHANGELOG.md`**: A user-facing summary of changes (version/feature/fix).
- **`.cursor/rules/`**: For adding or modifying AI behavior rules.

# 2) "Read First" Compass (Task-Based Context)

To maintain token discipline, only the following files should be included in the context for a given task type.

| Task Type             | Files to Read First (Context)                                                                                           |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Backend Endpoint      | `.cursor/rules/02-backend-standards.mdc`, `docs/API_SPEC.md`, `backend/app/routers/<module>.py`, `backend/tests/test_<module>.py` |
| Frontend UI           | `.cursor/rules/01-frontend-standards.mdc`, `frontend/src/components/<block>`, `frontend/src/pages/<page>`                       |
| Graph/Integration     | `.cursor/rules/03-graph-api-usage.mdc`, `docs/PERMISSIONS.md`, the relevant client/service file                            |
| Database/Schema       | `.cursor/rules/04-db-standards.mdc`, `backend/app/models/*`, `alembic/versions/*`                                         |
| DevOps/Infra          | `.cursor/rules/05-infra-standards.mdc`, `infra/*`, `docs/DEPLOY.md`                                                             |

> **Rule**: Do not include files outside this list in the context.

# 3) The T-Task Protocol (A Ritual for Every Task)

Follow this template for every task (e.g., T001: /users GET-POST-DELETE).

1.  **Lock in the Plan** (a single message in chat):
    ```
    T001 Plan:
    - Rules: 02-backend-standards, 06-testing
    - Source: docs/API_SPEC.md (/users)
    - Files: backend/app/routers/users.py, backend/tests/test_users.py
    - Output: router + test + docs/API_SPEC.md update
    ```

2.  **Read (Narrow the Context)**
    Use the `@` symbol to tag **only** the files listed in the plan. Use `@Recommended` for minimal additional context if absolutely necessary.

3.  **Implement**
    - Use the Composer (Cmd+I) for multi-file diffs.
    - Generate the test file within the same session.
    - Run local tests/linting before committing.

4.  **Definition of Done (DoD) Checklist** (do not exit without completing):
    - [ ] Code + tests passed.
    - [ ] `docs/API_SPEC.md` is updated.
    - [ ] `MVP_TASKS.md` status is set.
    - [ ] `PERMISSIONS.md` or an `ADR` is added if required.
    - [ ] A `CHANGELOG.md` entry has been created.

# 4) Context & Token Discipline

- **Task-Focused Context**: Only 1-3 code files + 1 rule file + 1 doc file.
- **Long Files**: Use **Optional Long Context** (premium feature) only for tagged long files.
- **Composer Projects / Notepads**: One task = one composer. After finishing, use **Summarize Previous Composers** to generate a summary, then open a new composer.
- **`@file` over `@folder`**: Do not reference entire folders; select specific files.
- **Selective `@docs`**: Do not reference the entire documentation; point to the relevant section (e.g., the specific part of API_SPEC).

# 5) Memory Management (Persistent vs. Ephemeral)

- **Persistent Memory** (within the repo):
  - **`.cursor/rules/`**: AI behavior.
  - **`DECISIONS/`**: The "why."
  - **`CHANGELOG.md`**: User-visible history.
  - **`MVP_TASKS.md`**: Operational memory.
- **Ephemeral Memory** (Cursor Composer session state):
  - At the end of each task, use **Summarize Previous Composers** to create a brief summary. Paste this 2-3 line summary under the "Notes" section of `MVP_TASKS.md`.
  - Close long sessions. Start new tasks with a **clean composer** to prevent context drift.

# 6) `.cursor/rules` Skeleton

```
.cursor/rules/
  00-ground-rules.mdc            # language, format, security, DoD items
  01-frontend-standards.mdc      # UI kit, file names, testing, accessibility
  02-backend-standards.mdc       # FastAPI, pydantic, logger, error policy
  03-graph-api-usage.mdc         # min. permissions, mandatory check of PERMISSIONS.md
  04-db-standards.mdc            # SQLAlchemy, Alembic, migration naming
  05-infra-standards.mdc         # env, secrets, CI/CD, runner rules
  06-testing.mdc                 # pytest, coverage threshold, fixture standards
  07-docs-style.mdc              # docs format, table/schema rules
```

The agent will select rules automatically, but we will state them in each plan for traceability.

# 7) Commit Message & PR Template

**Commit:**
```
feat(api/users): add GET/POST/DELETE + tests
- sync docs/API_SPEC.md (/users)
- update MVP_TASKS.md (T001: done)
```

**PR Description (Short Template):**
- **Task:** T001
- **Scope:** files A/B, tests C
- **Docs:** API_SPEC.md updated
- **Perms:** n/a or PERMISSIONS.md updated
- **ADR:** n/a or ADR-012 added

# 8) Structure Freeze Protocol

**Structure Freeze**: Making structural changes to the repository requires filling out `STRUCTURE_CHANGE.md` in the PR and creating a related **ADR**. Unauthorized changes will be rejected. See `STRUCTURE_v1.0.md` for the current frozen structure and invariants that must be preserved.

# 9) MCP / Agent / Terminal (for modern Cursor)

- **MCP Enabled**: Increases ability to read documents and follow rules.
- **Yolo Mode Off** (default): Terminal commands must be approved.
- **Agent sees recent changes** active: Run this *after* the planning step.

# 10) Versioning & Changelog Ritual

- After each "block" of work, add **Added/Changed/Fixed** items to `CHANGELOG.md`.

# 11) Short Operational Check-List

- [ ] Task ID selected (`MVP_TASKS.md`).
- [ ] Plan message sent (rules+files are clear).
- [ ] Only necessary files are tagged with **`@file`**.
- [ ] Composer session is singular; diffs applied, tests passed.
- [ ] **`API_SPEC` / `PERMISSIONS` / `ADR`** updated if necessary.
- [ ] **`MVP_TASKS`** status updated + 2-3 line session summary added.
- [ ] **`CHANGELOG`** entry added.
