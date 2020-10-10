from typing import List


class Coordinate:
    def __init__(self, coordinates: List[float]) -> None:
        self.__latitude = coordinates[0]
        self.__longitude = coordinates[1]
    
    @property
    def latitude(self) -> float:
        return self.__latitude

    @property
    def longitude(self) -> float:
        return self.__longitude
    
    def __str__(self) -> str:
        return f'Lat = {self.latitude}, Lon = {self.longitude}'