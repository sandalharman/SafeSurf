# policy.py
import json
import datetime
from pathlib import Path

class PolicyEngine:
    def __init__(self, cfg_path="config/policy.json"):
        self.cfg = json.loads(Path(cfg_path).read_text())

    def evaluate(self, user: str, host: str, path: str) -> str:
        """
        Return 'ALLOW', 'BLOCK', or 'FREEZE' (temp block).
        """
        now = datetime.datetime.utcnow().time()
        for rule in self.cfg["rules"]:
            # 1) User / group match
            if user not in rule.get("users", []) and rule.get("group") not in rule.get("groups", []):
                continue
            # 2) Time window
            if rule.get("time_start") and rule.get("time_end"):
                ts = datetime.datetime.strptime(rule["time_start"], "%H:%M").time()
                te = datetime.datetime.strptime(rule["time_end"], "%H:%M").time()
                if not (ts <= now <= te):
                    continue
            # 3) Domain / path blacklist
            if host in rule.get("domains_blacklist", []) or path in rule.get("paths_blacklist", []):
                return rule.get("action", "BLOCK")
            # 4) Domain / path whitelist
            if host in rule.get("domains_whitelist", []) or path in rule.get("paths_whitelist", []):
                return "ALLOW"
        return "ALLOW"
