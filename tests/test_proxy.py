# tests/test_proxy.py
import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_proxy_allows_clean_content():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Add a fake upstream header – the proxy ignores it in this demo
        r = await ac.get("/get")      # httpbin.org/get will be used by the proxy
        assert r.status_code == 200
        assert r.json()["url"] == "https://httpbin.org/get"

@pytest.mark.asyncio
async def test_proxy_blocks_adult():
    # This hits the *actual* proxy logic
    async with AsyncClient(app=app, base_url="http://test") as ac:
        r = await ac.get(
            "/anything",
            headers={"X-User": "bob"},
            params={"url": "adultsite.com"}   # our demo passes url as path
        )
        # The proxy returns 403 for any “adult” keyword
        assert r.status_code == 403
        assert r.json()["detail"] == "Content blocked"
