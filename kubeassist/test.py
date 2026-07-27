from app.clients.kube_client import KubernetesClient

client = KubernetesClient()

pod = client.get_pod_by_name(
    pod_name="auth-service-5ff57c7bcb-67l4b",
    namespace="production"
)

print(type(pod))
print(pod.metadata.name)