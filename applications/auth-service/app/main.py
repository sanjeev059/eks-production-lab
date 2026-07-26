from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="Auth Service")


@app.get("/")
def home():
    return {
        "service": "auth-service",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/ready")
def ready():
    return {
        "status": "ready"
    }


@app.get("/live")
def live():
    return {
        "status": "alive"
    }


# Automatically exposes /metrics
Instrumentator().instrument(app).expose(app)