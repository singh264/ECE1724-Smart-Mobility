from typing import List

from models.coordinate import Coordinate


class Edge:
    def __init__(self, osmid: List[int], edge_type: str, is_one_way: bool, max_speed: float, start_coordinate: Coordinate, end_coordinate: Coordinate) -> None:
        self.__osmid = osmid
        self.__edge_type = edge_type
        self.__is_one_way = is_one_way
        self.__max_speed = max_speed
        self.__start_coordinate = start_coordinate
        self.__end_coordinate = end_coordinate
    
    @property
    def osmid(self) -> List[float]:
        return self.__osmid
    
    @property
    def edge_type(self) -> str:
        return self.__edge_type
    
    @property
    def is_one_way(self) -> bool:
        return self.__is_one_way
    
    @property
    def max_speed(self) -> float:
        return self.__max_speed
    
    @property
    def start_coordinate(self) -> Coordinate:
        return self.__start_coordinate
    
    @property
    def end_coordinate(self) -> Coordinate:
        return self.__end_coordinate
    
    def __str__(self) -> str:
        return f'''Edge: {self.osmid},
                    edge_type: {self.edge_type},
                    is_one_way: {self.is_one_way},
                    max_speed: {self.max_speed},
                    start_coordinate: {self.start_coordinate},
                    end_coordinate: {self.end_coordinate}'''