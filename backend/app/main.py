from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="MSSP Client Portal API",
    version="0.1.0",
    description="Backend skeleton for a managed security services client portal."
)

class HealthResponse(BaseModel):
    status: str
    service: str

@app.get("/health", response_model=HealthResponse)
def health():
    return HealthResponse(status="ok", service="mssp-client-portal")

@app.get("/api/v1/summary")
def summary():
    return {
        "project": "MSSP Client Portal",
        "mode": "skeleton",
        "message": "Replace mocked handlers with real service implementations."
    }
