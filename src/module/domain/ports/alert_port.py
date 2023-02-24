from abc import abstractmethod, ABC
from typing import List

from module.domain.models.metrics import Metric, MetricValue


class MetricPort(ABC):

    @abstractmethod
    def get_metrics(self) -> List[Metric]:
        return [
            Metric(name="Metric1", value=MetricValue(10, "kwh")),
            Metric(name="Metric2", value=MetricValue(20, "kwh")),
            Metric(name="Metric3", value=MetricValue(30, "kwh"))
        ]
