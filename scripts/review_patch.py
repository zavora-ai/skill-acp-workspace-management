#!/usr/bin/env python3
"""Quick patch review — check for common issues in agent-generated code."""
import json, sys, re

ISSUES = [
    (r"TODO|FIXME|HACK", "Contains TODO/FIXME markers"),
    (r"unwrap\(\)|\.expect\(", "Contains unwrap/expect (may panic)"),
    (r"password|secret|token.*=.*[\"']", "Possible hardcoded secret"),
    (r"println!|console\.log|print\(", "Debug output left in code"),
]

def review(diff):
    findings = []
    for pattern, message in ISSUES:
        if re.search(pattern, diff, re.IGNORECASE):
            findings.append(message)
    return {"clean": len(findings) == 0, "findings": findings, "recommendation": "approve" if not findings else "request_changes"}

if __name__ == "__main__":
    print(json.dumps(review(sys.argv[1] if len(sys.argv) > 1 else ""), indent=2))
