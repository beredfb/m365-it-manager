# Structure Change Request

**Instructions**: Fill this template completely when making any structural changes to the repository. This file must be included in the PR and reviewed before merge.

## Summary

- **Change Title**: [Brief description of the structural change]
- **Scope**: [Which folders/files are affected]
- **Change Type**: [ ] Minor (v1.x) [ ] Major (v2.x)

## Rationale

- **Problem/Need**: [What issue does this change solve?]
- **Alternatives Considered**: [What other approaches were evaluated?]
- **Selection Reason**: [Why was this approach chosen?]

## Impact Analysis

- **CI/Rules Impact**: [How do existing CI checks need to be updated?]
- **Documentation Impact**: [Which docs need updates?]
- **Rollback Plan**: [How can this change be reverted if needed?]
- **Breaking Changes**: [ ] Yes [ ] No
  - If Yes, list what breaks: [Details]

## Implementation Checklist

- [ ] ADR created in `DECISIONS/` folder
- [ ] `STRUCTURE_vX.Y.md` updated with new version
- [ ] `CHANGELOG.md` "Structure" section updated
- [ ] Affected `.cursor/rules/` files updated
- [ ] Documentation updated (`docs/`, `README.md`, etc.)
- [ ] CI checks updated if needed

## References

- **Related ADR**: [Link to DECISIONS/ADR-xxxx.md]
- **Changelog Entry**: [Reference to CHANGELOG.md section]
- **Issue/Discussion**: [Link to GitHub issue or discussion]

---

**Reviewer Notes**: [To be filled by code reviewer]
- [ ] ADR is comprehensive and justified
- [ ] Impact analysis is complete
- [ ] Rollback plan is feasible
- [ ] Documentation is updated
