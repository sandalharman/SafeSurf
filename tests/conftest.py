# tests/conftest.py
import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def client():
    """
    A sync TestClient that talks to the in‑process FastAPI app.
    """
    with TestClient(app) as c:
        yield c
