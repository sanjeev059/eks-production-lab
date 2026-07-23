from fastapi import FastAPI

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