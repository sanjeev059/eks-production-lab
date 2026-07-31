from app.models.kubernetes_resource import KubernetesResource


class Pod(KubernetesResource):
    def __init__(self, name: str, namespace: str, kind: str, created_at: str, updated_at: str, status: str):
        super().__init__(name, namespace, kind, created_at, updated_at)
        self.status = status
        self.namespace = namespace

    def get_dict(self):
        pod_details = super().get_dict()
        pod_details["status"] = self.status
        pod_details["namespace"] = self.namespace
        return pod_details