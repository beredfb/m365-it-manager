# CI Structure Gates

This document defines the automated checks that enforce our structure freeze protocol.

## Overview

These gates prevent unauthorized structural changes and ensure documentation stays in sync with code changes.

## Gate Rules

### 1. API Documentation Sync Gate

**Trigger**: Changes detected in `backend/app/routers/**`

**Required**: Corresponding changes in `docs/API_SPEC.md`

**Implementation**: 
```yaml
# In GitHub Actions
- name: Check API Spec Sync
  if: contains(github.event.pull_request.changed_files, 'backend/app/routers/')
  run: |
    if ! git diff --name-only origin/main...HEAD | grep -q 'docs/API_SPEC.md'; then
      echo "Error: Router changes detected but docs/API_SPEC.md not updated"
      exit 1
    fi
```

### 2. Permissions Documentation Sync Gate

**Trigger**: Changes detected in `backend/**/graph*` or `**/client*` files

**Required**: Corresponding changes in `docs/PERMISSIONS.md`

**Implementation**:
```yaml
# In GitHub Actions  
- name: Check Permissions Sync
  if: contains(github.event.pull_request.changed_files, 'graph') || contains(github.event.pull_request.changed_files, 'client')
  run: |
    if ! git diff --name-only origin/main...HEAD | grep -q 'docs/PERMISSIONS.md'; then
      echo "Error: Graph/client changes detected but docs/PERMISSIONS.md not updated"
      exit 1
    fi
```

### 3. Structure Change Gate

**Trigger**: Changes to folder structure under core directories

**Required**: Both `STRUCTURE_CHANGE.md` and a new ADR file

**Implementation**:
```yaml
# In GitHub Actions
- name: Check Structure Change Protocol
  run: |
    STRUCTURE_PATHS="frontend/ backend/ infra/ docs/ .cursor/"
    CHANGED_STRUCTURE=false
    
    for path in $STRUCTURE_PATHS; do
      if git diff --name-only origin/main...HEAD | grep -q "^$path.*/$"; then
        CHANGED_STRUCTURE=true
        break
      fi
    done
    
    if [ "$CHANGED_STRUCTURE" = true ]; then
      if [ ! -f "STRUCTURE_CHANGE.md" ]; then
        echo "Error: Structural changes detected but STRUCTURE_CHANGE.md missing"
        exit 1
      fi
      
      NEW_ADR=$(git diff --name-only origin/main...HEAD | grep "^DECISIONS/.*\.md$" | head -1)
      if [ -z "$NEW_ADR" ]; then
        echo "Error: Structural changes detected but no new ADR found in DECISIONS/"
        exit 1
      fi
    fi
```

## Gate Status

| Gate | Status | Notes |
|------|--------|-------|
| API Sync | 🟡 Documented | Needs implementation in `.github/workflows/` |
| Permissions Sync | 🟡 Documented | Needs implementation in `.github/workflows/` |
| Structure Change | 🟡 Documented | Needs implementation in `.github/workflows/` |

## Implementation Plan

1. Add these checks to existing `ci-backend.yml` and `ci-frontend.yml` workflows
2. Create a dedicated `ci-structure.yml` workflow for structure-specific checks
3. Set as required status checks in GitHub branch protection rules

## Bypass Procedure

In emergency situations, gates can be bypassed by:
1. Adding `[skip-structure-gates]` to commit message
2. Requiring admin approval for the bypass
3. Creating a follow-up issue to address the bypass retroactively
