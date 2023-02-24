from module.domain.features.get_metrics_feature import GetMetricsFeature


def main(service: GetMetricsFeature):
    print(service.get_metrics())


if __name__ == "__main__":
    main(GetMetricsFeature())
