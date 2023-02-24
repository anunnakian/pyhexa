from typing import List

from module.domain.models.metrics import Metric
from module.domain.ports.alert_port import MetricPort


class MetricClient(MetricPort):

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key  # <-- dependency is injected

    # get data from database
    def get_metrics(self) -> List[Metric]:
        print("call REST API")
        return super().get_metrics()
