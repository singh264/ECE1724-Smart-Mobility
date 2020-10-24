class EdgeTrafficIncident:
    def __init__(self, severity: int, distance_to_edge_in_meters: float):
        self.__severity = severity
        self.__distance_to_edge_in_meters = distance_to_edge_in_meters

    @property
    def severity(self) -> int:
        return self.__severity

    @property
    def distance_to_edge_in_meters(self) -> float:
        return self.__distance_to_edge_in_meters

    def __str__(self) -> str:
        return f'''Traffic incident
                    severity = {self.severity},
                    distance_to_edge_in_meters = {self.distance_to_edge_in_meters}'''