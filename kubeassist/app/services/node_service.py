from app.clients.kube_client import KubernetesClient
from app.models.nodes import Node

class NodeService():
    def __init__(self):
            self.kube_client = KubernetesClient()

    def get_all_nodes(self):
        
        node_list = []

        kube_nodes = self.kube_client.get_all_nodes()

        for kube_node in kube_nodes.items:

            node = Node(
                name=kube_node.metadata.name,
                kind=kube_node.kind,
                created_at=str(kube_node.metadata.creation_timestamp),
                updated_at=str(kube_node.metadata.creation_timestamp),
                status=kube_node.status.conditions[-1].type,
                kubelet_version=kube_node.status.node_info.kubelet_version,
                os_image=kube_node.status.node_info.os_image,   
                container_runtime=kube_node.status.node_info.container_runtime_version

            )

            node_list.append(node.get_dict())

        return node_list