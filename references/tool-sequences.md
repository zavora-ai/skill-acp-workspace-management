# ACP Workspace Management Tool Sequences (9 tools)

## Sessions (3)
| Tool | Purpose | Risk |
|------|---------|------|
| `start_session` | Start a coding workspace session | write |
| `get_session_updates` | Get session progress/status | read |
| `stop_session` | Terminate a workspace session | write |

## Tasks (2)
| Tool | Purpose | Risk |
|------|---------|------|
| `delegate_task` | Assign coding task to agent | write |
| `list_participants` | List agents in session | read |

## Review (2)
| Tool | Purpose | Risk |
|------|---------|------|
| `get_proposed_changes` | View agent-generated patches | read |
| `review_patch` | Approve/reject a patch | **production** |

## Access (1)
| Tool | Purpose | Risk |
|------|---------|------|
| `handle_permission` | Grant/revoke file access | write |

## Publishing (1)
| Tool | Purpose | Risk |
|------|---------|------|
| `publish_agent` | Publish agent to registry | **production** |

## Sequence: Delegate and Review (5 calls)
```
1. start_session(workspace: "api-refactor", files: ["src/api/"]) → {session_id: "sess-001", status: "active"}
2. delegate_task(session_id: "sess-001", task: "Refactor auth middleware to use JWT", agent: "code-agent-1") → {task_id: "task-rf01", status: "assigned"}
3. get_session_updates(session_id: "sess-001") → {status: "patch_ready", tasks_completed: 1}
4. get_proposed_changes(session_id: "sess-001") → {patches: [{id: "patch-01", files: ["src/api/auth.ts"], diff: "+import jwt..."}]}
5. review_patch(patch_id: "patch-01", decision: "approved", comment: "LGTM") → {merged: true}
```

## Sequence: Permission Scoping (3 calls)
```
1. start_session(workspace: "bugfix-123", files: ["src/utils/"]) → {session_id: "sess-002", status: "active"}
2. handle_permission(session_id: "sess-002", agent: "code-agent-1", paths: ["src/utils/parser.ts"], access: "read-write") → {granted: true}
3. delegate_task(session_id: "sess-002", task: "Fix parser edge case for empty input", agent: "code-agent-1") → {task_id: "task-bf01", status: "assigned"}
```

## Sequence: Reject and Stop (3 calls)
```
1. get_proposed_changes(session_id: "sess-001") → {patches: [{id: "patch-02", files: ["src/api/db.ts"], diff: "-connection.close()\n+// removed cleanup"}]}
2. review_patch(patch_id: "patch-02", decision: "rejected", comment: "Must not remove connection cleanup") → {merged: false}
3. stop_session(session_id: "sess-001") → {status: "terminated", duration: "12min"}
```
