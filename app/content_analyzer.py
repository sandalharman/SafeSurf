# content_analyzer.py
import re

class ContentAnalyzer:
    # Very basic: look for <iframe>, <script> eval, or suspicious URLs
    _iframe_pat = re.compile(r"<iframe", re.I)
    _eval_pat    = re.compile(r"eval\(", re.I)
    _phish_pat   = re.compile(r"login\.com|bank\.bank|secure\.pay", re.I)

    def analyze(self, body: bytes) -> bool:
        text = body.decode(errors="ignore")
        if self._iframe_pat.search(text):
            return True
        if self._eval_pat.search(text):
            return True
        if self._phish_pat.search(text):
            return True
        return False
