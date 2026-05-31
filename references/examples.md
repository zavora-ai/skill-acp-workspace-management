# ACP Workspace Management Examples

## Example 1: "Start a coding session to refactor the payment module"
```
start_session(workspace: "payment-refactor", files: ["src/payments/"]) → {session_id: "sess-pay01", status: "active"}
handle_permission(session_id: "sess-pay01", agent: "code-agent-1", paths: ["src/payments/"], access: "read-write") → {granted: true}
delegate_task(session_id: "sess-pay01", task: "Extract payment validation into separate module", agent: "code-agent-1") → {task_id: "task-pv01", status: "assigned"}
get_session_updates(session_id: "sess-pay01") → {status: "in_progress", elapsed: "3min"}
```
Response: "🛠️ Workspace session started (sess-pay01). Delegated refactoring task to code-agent-1 with read-write access to src/payments/. Task in progress."

## Example 2: "Show me what the agent changed and let me review"
```
get_proposed_changes(session_id: "sess-pay01") → {patches: [{id: "patch-p01", files: ["src/payments/validate.ts", "src/payments/index.ts"], additions: 45, deletions: 12, diff: "+export function validateAmount(...)..."}]}
review_patch(patch_id: "patch-p01", decision: "approved", comment: "Clean extraction, tests pass") → {merged: true}
stop_session(session_id: "sess-pay01") → {status: "terminated", duration: "8min", patches_merged: 1}
```
Response: "✅ Patch approved and merged. Changes: +45/-12 lines across validate.ts and index.ts. Session closed after 8 minutes."

## Example 3: "What agents are working in active sessions?"
```
list_participants(session_id: "sess-api02") → [{agent: "code-agent-1", task: "Add rate limiting", status: "working"}, {agent: "code-agent-2", task: "Write tests", status: "patch_ready"}]
get_proposed_changes(session_id: "sess-api02") → {patches: [{id: "patch-a01", agent: "code-agent-2", files: ["tests/rate-limit.test.ts"], additions: 80}]}
```
Response: "Session sess-api02 has 2 agents:\n• **code-agent-1** — Adding rate limiting (working)\n• **code-agent-2** — Writing tests (patch ready, +80 lines)\n\ncode-agent-2 has a patch awaiting review."
