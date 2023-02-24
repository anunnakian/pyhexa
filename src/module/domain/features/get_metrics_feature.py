from dependency_injector.wiring import Provide, inject

from module.domain.ports.alert_port import MetricPort
from module.api.container import MetricContainer


class GetMetricsFeature:

    @inject
    def __init__(self, api_client: MetricPort = Provide[MetricContainer.alert_repository]) -> None:
        self.api_client = api_client  # <-- dependency is injected

    def get_metrics(self):
        return self.api_client.get_metrics()
