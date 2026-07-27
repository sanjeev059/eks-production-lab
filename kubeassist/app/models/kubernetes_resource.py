from abc import ABC

class  KubernetesResource(ABC):
    def __init__(self, name: str, namespace: str, kind: str,created_at: str, updated_at: str):
        self.name = name
        self.namespace = namespace
        self.kind = kind
        self.created_at = created_at
        self.updated_at = updated_at
        
    def get_dict(self):
        return {
            "name": self.name,
            "namespace": self.namespace,
            "kind": self.kind,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

