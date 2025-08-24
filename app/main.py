# main.py
import httpx
from fastapi import FastAPI, Request, Response, HTTPException
from app import policy, url_categorizer, content_analyzer, threat_intel, decision
import uvicorn
import ssl
import certifi

app = FastAPI()

# Shared components (singletons)
policy_engine      = policy.PolicyEngine()
url_categorizer    = url_categorizer.URLCategorizer()
content_analyzer   = content_analyzer.ContentAnalyzer()
threat_intel       = threat_intel.ThreatIntel()
decision_engine    = decision.DecisionEngine(
        policy_engine,
        url_categorizer,
        content_analyzer,
        threat_intel
    )

@app.middleware("http")
async def safe_surf_proxy(request: Request, call_next):
    # 1) Extract data we need for the decision
    user  = request.headers.get("X-User", "anonymous")
    host  = request.url.host or ""
    path  = request.url.path
    url   = str(request.url)

    # 2) Evaluate policy
    action = policy_engine.evaluate(user, host, path)
    if action == "BLOCK":
        raise HTTPException(status_code=403, detail="Policy‑blocked")

    # 3) Fetch the upstream content (for demo we forward to httpbin.org)
    async with httpx.AsyncClient(verify=certifi.where()) as client:
        resp = await client.request(
            request.method,
            "https://httpbin.org" + request.url.path,
            headers=dict(request.headers),
            data=await request.body(),
            timeout=10
        )

    # 4) Analyse content
    suspicious = content_analyzer.analyze(resp.content)

    # 5) Decision
    decision = decision_engine.make_decision(
        user=user,
        host=host,
        path=path,
        url=url,
        body=resp.content,
        category=url_categorizer.categorize(url)[0],
        suspicious=suspicious
    )

    if decision == "BLOCK":
        raise HTTPException(status_code=403, detail="Content blocked")

    # 6) Return the upstream response unchanged
    return Response(
        content=resp.content,
        status_code=resp.status_code,
        headers=resp.headers
    )

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)

