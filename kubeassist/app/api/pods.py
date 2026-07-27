from fastapi import APIRouter
from app.services.pod_service import PodService

router = APIRouter()
pod_service = PodService()

@router.get("/pods")
def get_all_pods():
    return pod_service.get_all_pods()

@router.get("/pods/{pod_name}")
def get_pod_by_name(pod_name: str):
    return pod_service.get_pod_by_name(pod_name)