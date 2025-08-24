import json
from app import create_app  # Factory pattern

class TestSafeSurf:
    def setup_method(self):
        self.app = create_app({"TESTING": True})
        self.client = self.app.test_client()

    def test_safe_url_endpoint(self):
        resp = self.client.get("/safe-surf", query_string={"url": "data:text/plain,Hello"})
        assert resp.status_code == 200
        assert json.loads(resp.data)["safe"] is True
