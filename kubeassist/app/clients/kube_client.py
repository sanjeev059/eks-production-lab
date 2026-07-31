from kubernetes import client, config


class KubernetesClient:

    def __init__(self):

        config.load_kube_config()

        self.client = client.CoreV1Api()

    def get_all_pods(self):

        return self.client.list_pod_for_all_namespaces()

    def get_pod_by_name(self, pod_name: str, namespace: str):

        return self.client.read_namespaced_pod(
            name=pod_name,
            namespace=namespace
        )
    def get_all_nodes(self):

        return self.client.list_node()