from app.clients.kube_client import KubernetesClient
from app.models.pod import Pod


class PodService:

    def __init__(self):
        self.kube_client = KubernetesClient()

    def get_all_pods(self):

        pod_list = []

        kube_pods = self.kube_client.get_all_pods()

        for kube_pod in kube_pods.items:

            pod = Pod(
                name=kube_pod.metadata.name,
                namespace=kube_pod.metadata.namespace,
                kind=kube_pod.kind,
                created_at=str(kube_pod.metadata.creation_timestamp),
                updated_at=str(kube_pod.metadata.creation_timestamp),
                status=kube_pod.status.phase
            )

            pod_list.append(pod.get_dict())

        return pod_list