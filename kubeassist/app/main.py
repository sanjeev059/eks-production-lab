from fastapi import FastAPI
from app.services.pod_service import PodService

app = FastAPI(title="KubeAssist")
pod_service = PodService()

@app.get("/")
def home():
    return {
        "message": "Welcome to KubeAssist"
    }

@app.get("/pods")
def get_pod():
    return pod_service.get_all_pods()
   