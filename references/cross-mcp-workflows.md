# ACP Workspace Cross-MCP Workflows

## ACP + GitHub: Agent Codes → PR
```
ACP: start_session(scope: "src/payments/**", permissions: "suggest")
ACP: delegate_task(task: "Fix payment retry logic per PROJ-123")
ACP: get_proposed_changes() → {files_changed: 2, diff: "..."}
ACP: review_patch(patch_id, decision: "approve")
GITHUB: create_pull_request(title: "fix: payment retry (agent-generated)", head: "agent/fix-retry")
ACP: stop_session()
```

## ACP + Governance: Governed Code Changes
```
GOVERNANCE: evaluate_policy(action: "agent_code_change", scope: "src/auth/**")
  → {decision: "denied", reason: "Auth code requires human-only changes"}
ACP: delegate_task(...) → BLOCKED by policy
```
