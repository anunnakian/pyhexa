from typing import List

from module.domain.models.metrics import Metric
from module.domain.ports.alert_port import MetricPort
from module.persistence.db_connection import DbConnection


class MetricAdapter(MetricPort):

    def __init__(self, api_key: str, connection: DbConnection) -> None:
        self.api_key = api_key
        self.connection = connection

    def get_metrics(self) -> List[Metric]:
        print("INFO: get metrics from mongoDB")
        return super().get_metrics()

