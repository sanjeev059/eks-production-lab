from fastapi import FastAPI
from app.api import pods
from app.api import nodes

app = FastAPI(title="KubeAssist")

app.include_router(pods.router)
app.include_router(nodes.router)

@app.get("/")
def home():
    return {
        "message": "Welcome to KubeAssist"
    }