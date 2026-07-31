from fastapi import APIRouter
from app.services.node_service import NodeService

router = APIRouter()

node_service = NodeService()

@router.get("/nodes")
def get_all_nodes():
    return node_service.get_all_nodes()