import decimal


class MetricValue:
    value: decimal
    unit: str

    def __init__(self, value: decimal, unit: str):
        self.value = value
        self.unit = unit

    def __repr__(self) -> str:
        return "{} {}".format(self.value, self.unit)


class Metric:
    name: str
    value: MetricValue

    def __init__(self, name: str, value: MetricValue):
        self.name = name
        self.value = value

    def __repr__(self) -> str:
        return "Metric(name = " + self.name + ", value = " + repr(self.value) + ")"
