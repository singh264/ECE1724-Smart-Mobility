from typing import List, Any

from models.coordinate import Coordinate
from models.edge_traffic_incident import EdgeTrafficIncident


class Edge:
    def __init__(self, osmid: List[int], edge_type: str, is_one_way: bool, max_speed: Any, start_osmid: int, end_osmid: int, start_coordinate: Coordinate, end_coordinate: Coordinate) -> None:
        self.__osmid = osmid
        self.__edge_type = edge_type
        self.__is_one_way = is_one_way
        self.__max_speed = self.__parse_max_speed(max_speed)
        self.__start_osmid = start_osmid
        self.__end_osmid = end_osmid
        self.__start_coordinate = start_coordinate
        self.__end_coordinate = end_coordinate
        self.__nearby_traffic_incidents = []
        self.__risk_score = 0
    
    def __parse_max_speed(self, max_speed: Any) -> List[float]:
        if (isinstance(max_speed, str)):
            return [-1]
        elif (isinstance(max_speed, float)):
            return [max_speed]
        elif (isinstance(max_speed, list)):
            return [float(speed) for speed in max_speed]
        else:
            raise Exception(f'Unsupported max_speed type: {type(max_speed)}')

    @property
    def osmid(self) -> List[int]:
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
    def start_osmid(self) -> int:
        return self.__start_osmid

    @property
    def end_osmid(self) -> int:
        return self.__end_osmid

    @property
    def start_coordinate(self) -> Coordinate:
        return self.__start_coordinate
    
    @property
    def end_coordinate(self) -> Coordinate:
        return self.__end_coordinate

    @property
    def nearby_traffic_incidents(self) -> List[EdgeTrafficIncident]:
        return self.__nearby_traffic_incidents

    def add_traffic_incident(self, traffic_incident: EdgeTrafficIncident) -> None:
        self.__nearby_traffic_incidents.append(traffic_incident)
    
    @property
    def risk_score(self) -> float:
        return self.__risk_score
    
    def normalize_risk_score(self, total_risk_score) -> None:
        self.__risk_score /= total_risk_score
    
    def __str__(self) -> str:
        return f'''Edge: {self.osmid},
                    edge_type: {self.edge_type},
                    is_one_way: {self.is_one_way},
                    max_speed: {self.max_speed},
                    start_osmid: {self.start_osmid},
                    end_osmid: {self.end_osmid},
                    start_coordinate: {self.start_coordinate},
                    end_coordinate: {self.end_coordinate},
                    nearby_traffic_incidents: {self.nearby_traffic_incidents},
                    risk_score: {self.risk_score}'''