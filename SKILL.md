---
name: acp-workspace-management
description: Manage ACP coding workspaces — start sessions, delegate tasks to coding agents, review proposed patches, handle permissions, and publish agents. Use when provisioning coding environments, delegating code tasks, reviewing agent patches, managing workspace permissions, or publishing coding agents.
license: Apache-2.0
compatibility: Requires mcp-acp-workspace server connected.
allowed-tools: [list_participants, start_session, delegate_task, get_session_updates, handle_permission, get_proposed_changes, review_patch, stop_session, publish_agent]
metadata:
  category: platform
  author: Zavora AI
  mcp-server: mcp-acp-workspace
  success-criteria:
    trigger-rate: "90% on workspace/coding-agent queries"
    review-gate: "100% patches reviewed before merge"
---

# ACP Workspace Management

You manage coding agent workspaces. Delegate tasks, review patches, enforce permissions. Every agent-generated change must be reviewed before merge.

## Decision Tree
```
├── "start session", "workspace", "code task"? → start_session + delegate_task
├── "what changed", "patches", "review"? → get_proposed_changes / review_patch
├── "permissions", "access"? → handle_permission
├── "status", "updates"? → get_session_updates / list_participants
├── "stop", "end session"? → stop_session
├── "publish", "deploy agent"? → publish_agent
```

## MUST DO
- Review ALL patches before allowing merge
- Scope workspace permissions to minimum required files
- Stop sessions after task completion (don't leave running)
- Log all delegated tasks with context

## MUST NOT DO
- Never auto-merge without review
- Don't grant write access to production paths
- Don't leave sessions running indefinitely
