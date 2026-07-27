from kubernetes import client, config


class KubernetesClient:

    def __init__(self):

        config.load_kube_config()

        self.client = client.CoreV1Api()

    def get_all_pods(self):

        return self.client.list_pod_for_all_namespaces()