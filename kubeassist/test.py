from app.clients.kube_client import KubernetesClient

client = KubernetesClient()

nodes = client.get_all_nodes()

for kube_node in nodes.items:
    print(kube_node.metadata.name)
    print(kube_node.status.node_info.kubelet_version)
    print(kube_node.status.node_info.os_image)
    print(kube_node.status.node_info.container_runtime_version)
    print("----------------")