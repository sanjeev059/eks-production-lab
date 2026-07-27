from app.clients.kube_client import KubernetesClient

client = KubernetesClient()

pods = client.get_all_pods()

for kube_pod in pods.items:
    print(kube_pod.metadata.name)
    print(kube_pod.metadata.namespace)
    print(kube_pod.status.phase)
    print(kube_pod.metadata.creation_timestamp)
