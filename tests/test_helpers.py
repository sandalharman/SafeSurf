from app.helpers import is_safe_url

def test_safe_url():
    assert is_safe_url("data:text/plain,Hello") is True

def test_http_url():
    assert is_safe_url("http://example.com") is False

def test_malformed():
    assert is_safe_url("not-a-url") is False
