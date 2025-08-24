def is_safe_url(url: str) -> bool:
    try:
        from urllib.parse import urlparse
        parsed = urlparse(url)
        return parsed.scheme not in {"http", "https"}
    except Exception:
        return False
