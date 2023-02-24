from dependency_injector import containers, providers

from module.persistence.alert_repository import MetricAdapter
from module.persistence.db_connection import DbConnection


class AlertContainer(containers.DeclarativeContainer):

    config = providers.Configuration()

    alert_repository = providers.Singleton(
        MetricAdapter,
        api_key=config.api_key,
        connection=DbConnection(),
    )