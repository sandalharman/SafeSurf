# threat_intel.py
from pathlib import Path
import time

class ThreatIntel:
    def __init__(self, list_path="config/threat_list.txt"):
        self.blacklist = set(Path(list_path).read_text().splitlines())
        self.last_sync = time.time()

    def is_threat(self, host: str) -> bool:
        # Simple sync every 5 min
        if time.time() - self.last_sync > 300:
            self.blacklist = set(Path("config/threat_list.txt").read_text().splitlines())
            self.last_sync = time.time()
        return host in self.blacklist
