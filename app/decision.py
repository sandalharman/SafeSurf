# decision.py
class DecisionEngine:
    def __init__(self, policy, categorizer, analyzer, intel):
        self.policy = policy
        self.cat    = categorizer
        self.an    = analyzer
        self.intel = intel

    def decide(self, user, host, path, url, body: bytes):
        score = 0

        # Policy score
        action = self.policy.evaluate(user, host, path)
        if action == "BLOCK":
            return "BLOCK"

        # Category score
        cat, conf = self.cat.categorize(url)
        if cat == "Adult":
            score += 2
        elif cat == "Safe":
            score -= 1

        # Content score
        if self.an.analyze(body):
            score += 3

        # Threat‑intel
        if self.intel.is_threat(host):
            score += 5

        # Final decision
        if score >= 5:
            return "BLOCK"
        return "ALLOW"

