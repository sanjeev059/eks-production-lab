from fastapi import FastAPI
from app.api import pods

app = FastAPI(title="KubeAssist")

@app.get("/")
def home():
    return {"message": "Welcome to KubeAssist"}

app.include_router(pods.router)