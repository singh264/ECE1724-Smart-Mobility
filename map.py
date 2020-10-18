import osmnx as ox
import osmapi as osm
from pathlib import Path
import csv
from geopandas import GeoDataFrame
from networkx.classes.multidigraph import MultiDiGraph
import pandas as pd
from typing import Dict, List

from models.edge import Edge
from models.coordinate import Coordinate


class Map:
    def __init__(self, place: str, cached_edges_coords_csv_path: Path) -> None:
        self.__place = place
        self.__cached_edges_coords_map = self.__get_cached_edges_coords_map(cached_edges_coords_csv_path)
        self.__graph = ox.graph_from_place(place)
        ox_nodes_and_edges = ox.graph_to_gdfs(self.__graph)
        self.__ox_nodes = ox_nodes_and_edges[0]
        self.__ox_edges = ox_nodes_and_edges[1]
        self.__edges = None
        
    def __get_cached_edges_coords_map(self, cached_edges_coords_csv_path: Path) -> Dict[int, Coordinate]:
        self.__validate_path_exists(cached_edges_coords_csv_path)
        cached_edges_coords_map = {}
        with open(cached_edges_coords_csv_path) as file:
            reader = csv.reader(file)
            rows = list(reader)
            for row in rows[1:]:
                osmid = int(row[0])
                lat = float(row[1])
                lon = float(row[2])
                cached_edges_coords_map[osmid] = Coordinate([lat, lon])
        
        return cached_edges_coords_map
    
    def __validate_path_exists(self, path: Path) -> Path:
        if (not path.exists()):        
            raise Exception(f'{path} does not exist')
    
    @property
    def graph(self) -> MultiDiGraph:
        return self.__graph
    
    @property
    def ox_nodes(self) -> GeoDataFrame:
        return self.__ox_nodes
    
    @property
    def ox_edges(self) -> GeoDataFrame:
        return self.__ox_edges
    
    @property
    def edges(self) -> List[Edge]:
        return self.__edges if self.__edges is not None else self.__get_edges()
    
    def __get_edges(self) -> List[Edge]:
        edges = []
        ox_edges_dictionary = pd.DataFrame(self.ox_edges).to_dict()
        edges_count = len(ox_edges_dictionary['osmid'])
        for i in range(edges_count):
            osmid = ox_edges_dictionary['osmid'][i]
            edge_type = ox_edges_dictionary['highway'][i]
            is_one_way = ox_edges_dictionary['oneway'][i] 
            max_speed = ox_edges_dictionary['maxspeed'][i]
            start_osmid = ox_edges_dictionary['u'][i]
            start_coordinate = self.__get_node_coordinates(start_osmid)
            end_osmid = ox_edges_dictionary['v'][i]
            end_coordinate = self.__get_node_coordinates(end_osmid)

            edges.append(Edge(osmid, edge_type, is_one_way, max_speed, start_osmid, end_osmid, start_coordinate, end_coordinate))
    
        self.__edges = edges
        
        return self.__edges
            
    def __get_node_coordinates(self, osmid: int) -> Coordinate:
        return self.__cached_edges_coords_map[osmid] if osmid in self.__cached_edges_coords_map else self.__get_node_from_osmapi(osmid)

    def __get_node_from_osmapi(self, osmid: int) -> Coordinate:
        api = osm.OsmApi()
        node = api.NodeGet(osmid)

        return Coordinate([node['lat'], node['lon']])
