from dependency_injector import containers, providers

from module.api.alert_client import MetricClient


class MetricContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    alert_repository = providers.Singleton(
        MetricClient,
        api_key="API"
    )
