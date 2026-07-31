from app.models.kubernetes_resource import KubernetesResource


class Node(KubernetesResource):

    def __init__(
        self,
        name,
        kind,
        created_at,
        updated_at,
        status,
        kubelet_version,
        os_image,
        container_runtime
    ):

        super().__init__(
            name=name,
            kind=kind,
            created_at=created_at,
            updated_at=updated_at
        )

        self.status = status
        self.kubelet_version = kubelet_version
        self.os_image = os_image
        self.container_runtime = container_runtime

    def get_dict(self):

        return {
            "name": self.name,
            "kind": self.kind,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "status": self.status,
            "kubelet_version": self.kubelet_version,
            "os_image": self.os_image,
            "container_runtime": self.container_runtime
        }
        