#!/usr/bin/env python3
"""
SaaS-AI Governance Sentinel (Standalone Public Version)
Detects unauthorized outbound calls to external AI APIs.
Detects credential leakage in outbound payloads.
Self-contained: logs decisions to local hash-chained JSON ledger.
"""
import os, sys, json, hashlib, time
from pathlib import Path

class SimpleAuditLog:
    """Lightweight standalone audit logger with SHA-256 chaining"""
    def __init__(self, log_dir=None):
        self.log_dir = Path(log_dir) if log_dir else Path(__file__).parent.parent / "logs"
        self.log_dir.mkdir(parents=True, exist_ok=True)
        self.log_file = self.log_dir / "sentinel_log.jsonl"
        self.last_hash = "0" * 64

    def record(self, action, reasoning, inputs, outcome):
        record = {
            "timestamp": time.time(),
            "timestamp_iso": time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
            "action": action,
            "reasoning": reasoning,
            "inputs": inputs,
            "outcome": outcome,
            "previous_hash": self.last_hash
        }
        current_hash = hashlib.sha256(json.dumps(record, sort_keys=True).encode()).hexdigest()
        record["current_hash"] = current_hash
        self.last_hash = current_hash
        with open(self.log_file, "a") as f:
            f.write(json.dumps(record) + "\n")
        return current_hash

class SaaSGovernanceSentinel:
    SANCTIONED_ENDPOINTS = ["127.0.0.1", "localhost", "api.anthropic.com"]
    SENSITIVE_PATTERNS = ["AWS_SECRET_ACCESS_KEY","PRIVATE_KEY","api_key","password","token","secret"]

    def __init__(self):
        self.ledger = SimpleAuditLog()
        print("[*] SaaS Governance Sentinel armed (standalone)")

    def audit_outbound_request(self, origin_process, target_url, payload_snippet):
        print(f"\n[SENTINEL] {origin_process} -> {target_url}")
        is_sanctioned = any(ep in target_url for ep in self.SANCTIONED_ENDPOINTS)
        contains_sensitive = any(p.lower() in payload_snippet.lower() for p in self.SENSITIVE_PATTERNS)
        if not is_sanctioned:
            print(f"[SENTINEL BLOCK] Shadow AI endpoint: {target_url}")
            action = "BLOCK_SHADOW_ENDPOINT"; passed = False
        elif contains_sensitive:
            print(f"[SENTINEL BLOCK] Credential leak in payload")
            action = "BLOCK_CREDENTIAL_LEAK"; passed = False
        else:
            print(f"[SENTINEL PASS] Request cleared")
            action = "PASS_REQUEST"; passed = True

        h = self.ledger.record(
            action=action,
            reasoning=f"Outbound from {origin_process} to {target_url}",
            inputs={"origin":origin_process,"target":target_url,"sanctioned":is_sanctioned,"credential_leak":contains_sensitive},
            outcome="GOVERNANCE_ENFORCED" if not passed else "TRAFFIC_PASSED"
        )
        print(f"[✓] Logged: {h[:16]}...")
        return passed

    def scan_environment(self):
        print("\n[SENTINEL] Scanning environment variables...")
        risks = []
        for key in os.environ:
            if any(p.lower() in key.lower() for p in self.SENSITIVE_PATTERNS):
                risks.append(f"{key}=***REDACTED***")
        result = {"total_env_vars": len(os.environ), "risky_vars_found": len(risks), "risky_vars": risks, "status": "RISK_DETECTED" if risks else "CLEAN"}
        self.ledger.record(
            action="ENV_SCAN",
            reasoning="Scanned environment for credential exposure",
            inputs={"var_count": len(os.environ)},
            outcome=result["status"]
        )
        if risks:
            print(f"[!] {len(risks)} potentially exposed variables")
        else:
            print("[✓] Environment scan clean")
        return result

if __name__ == "__main__":
    s = SaaSGovernanceSentinel()
    s.audit_outbound_request("unknown_plugin", "https://api.rogue-llm.ai/v1/chat", "Review this manifest")
    s.audit_outbound_request("developer_tool", "https://api.anthropic.com/v1/messages", "AWS_SECRET_ACCESS_KEY=abc123")
    s.audit_outbound_request("dreadnought_siem", "http://127.0.0.1:11434/api/generate", "Analyze this log file")
    s.scan_environment()
