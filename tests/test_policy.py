# tests/test_policy.py
import json
from app.policy import PolicyEngine

def test_policy_blocking():
    # ① Load a tiny policy file
    raw = {
        "rules": [
            {
                "users": ["bob"],
                "domains_blacklist": ["evil.com"],
                "action": "BLOCK"
            }
        ]
    }
    policy = PolicyEngine(raw)

    # ② Alice → should be allowed
    assert policy.evaluate("alice", "any.com", "/") == "ALLOW"

    # ③ Bob → blocked
    assert policy.evaluate("bob", "evil.com", "/") == "BLOCK"

def test_policy_time():
    raw = {
        "rules": [
            {
                "users": ["carol"],
                "time_start": "22:00",
                "time_end": "02:00",
                "action": "BLOCK"
            }
        ]
    }
    policy = PolicyEngine(raw)

    # 22:30 → block
    assert policy.evaluate("carol", "any.com", "/", now="22:30") == "BLOCK"

    # 04:00 → allow (outside window)
    assert policy.evaluate("carol", "any.com", "/", now="04:00") == "ALLOW"
