# ACP Workspace Management Skill

> Coding agent workspace control — start sessions, delegate tasks to coding agents, review proposed patches, manage permissions, and publish agents with governance gates.

[![Skill Standard](https://img.shields.io/badge/standard-agentskills.io-blue)](https://agentskills.io)
[![ADK-Rust Enterprise](https://img.shields.io/badge/ADK--Rust-Enterprise-purple.svg)](https://enterprise.adk-rust.com)
[![License](https://img.shields.io/badge/license-Apache--2.0-orange)](LICENSE)

## What This Skill Does

| Workflow | Calls | Achieves |
|----------|-------|----------|
| Delegate Task | 2-3 | Start session → assign → monitor |
| Review Patch | 2 | Get changes → approve/reject |
| Permissions | 1 | Scope access to specific files |
| Publish | 1 | Make agent available to others |

### Without this skill:
- Agent code changes merged without review
- No file-level access control (agents touch anything)
- Sessions left running indefinitely
- No audit of what agents changed

### With this skill:
- Every patch reviewed before merge (100%)
- Workspace scoped to minimum required files
- Sessions auto-stopped after completion
- Full audit trail of delegated tasks

## Installation

```bash
git clone https://github.com/zavora-ai/skill-acp-workspace-management.git \
  ~/.skills/skills/acp-workspace-management
```

## Requirements

**Required:** `mcp-acp-workspace` (9 tools)
**Cross-MCP:** mcp-github (agent patches → PRs), mcp-governance-policy (restrict auth code changes)

## Example

**User:** "Have the coding agent fix the payment retry bug"

**Result:**
```
✅ Session started (scope: src/payments/**)
Task delegated: "Fix payment retry logic per PROJ-123"
Agent proposed 2 file changes (+15/-3 lines)
Review: No secrets, no TODOs, no debug output ✅
Ready for your approval to merge.
```

## Scripts

### `review_patch.py`
```bash
python scripts/review_patch.py "fn main() { println!(\"debug\"); }"
# → {"clean": false, "findings": ["Debug output left in code"], "recommendation": "request_changes"}
```

## Contributors

| [<img src="https://github.com/jkmaina.png" width="80px;"/><br /><sub><b>James Karanja Maina</b></sub>](https://github.com/jkmaina) |
|:---:|

## License

Apache-2.0 — Part of [ADK-Rust Enterprise](https://enterprise.adk-rust.com). Built with ❤️ by [Zavora AI](https://zavora.ai)

## Success Criteria

| Metric | Target |
|--------|--------|
| Trigger rate | 90% on relevant queries |
| Compliance | 100% governed actions evaluated |
| Audit trail | Every action logged with actor + reason |

## Related Skills

See the full [ADK-Rust Enterprise Skills Registry](https://github.com/zavora-ai) for all 35 skills.
