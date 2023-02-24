from module.api.container import MetricContainer

container = MetricContainer()
container.wire(modules=[
    __name__,
    "module.domain.ports.alert_port",
    "module.domain.features.get_metrics_feature",
    "module.persistence.alert_repository",
    "module.api.alert_client"])