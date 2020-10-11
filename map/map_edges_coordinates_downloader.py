import osmnx as ox
import osmapi as osm
import pandas as pd
import csv
from typing import List, Dict, Any
from pathlib import Path


class MapEdgesCoordinatesDowloader:
    def __init__(self, place: str, storage_path: Path = Path('./data')):
        self.__place = place
        self.__storage_path = storage_path
        self.__storage_path.mkdir(parents=True, exist_ok=True)

    def download_edges_coordinates(self) -> None:
        print(f'Processing place: {self.__place}')
        self.__save_edges_start_end_osmids_to_csv_file()
        self.__save_edges_coordinates_to_csv_file()

    def __save_edges_start_end_osmids_to_csv_file(self) -> None:
        save_file_name = self.__get_edges_start_end_osmids_csv_file_name()
        self.__throw_error_if_file_exists_in_storage(save_file_name)
        print(f'Downloading edge osmids to: {save_file_name}')

        with open(self.__storage_path / save_file_name, 'w') as file:
            writer = csv.writer(file)
            edges = self.__get_edges()
            for i in range(len(edges['u'])):
                row_data = [str(edges['u'][i]), str(edges['v'][i])]
                writer.writerow(row_data)
                
        print(f'Downloaded edge osmids to: {save_file_name}')
    
    def __throw_error_if_file_exists_in_storage(self, file_name: str) -> None:
        if ((self.__storage_path / file_name).exists()):
            raise Exception(f'{file_name} already exists in storage.')

    def __get_edges(self) -> Dict[str, Any]:
        G = ox.graph_from_place(self.__place)
        _, edges = ox.graph_to_gdfs(G)  

        return pd.DataFrame(edges).to_dict()

    def __get_edges_start_end_osmids_csv_file_name(self) -> str:
        return self.__get_base_file_name() + '_edges_osmids.csv'
    
    def __get_base_file_name(self) -> str:
        return '_'.join(self.__place.split(' '))

    def __save_edges_coordinates_to_csv_file(self) -> None:
        save_file_name = self.__get_edges_coordinates_csv_file_name()
        self.__throw_error_if_file_exists_in_storage(save_file_name)
        print(f'Downloading edges coordinates to: {save_file_name}')

        osmids = self.__get_edges_start_end_osmids()
        with open(self.__storage_path / save_file_name, 'w') as file:
            writer = csv.writer(file)
            writer.writerow(['osmid', 'lat', 'lon'])
            osmids_total_count = len(osmids)
            osmids_processed_count = 1
            for osmid in osmids:
                coords = self.__get_node_coordinates(osmid)
                row_data = [osmid, coords[0], coords[1]]
                writer.writerow(row_data)
                
                print(f'{osmids_processed_count}/{osmids_total_count} Downloading coordinates of osmid: {osmid}')
                osmids_processed_count += 1
        
        print(f'Downloaded edges coordinates to: {save_file_name}')

    def __get_edges_start_end_osmids(self) -> List[int]:
        osmids = set()
        edges_start_end_osmids_csv_file_name = self.__get_edges_start_end_osmids_csv_file_name()
        with open(self.__storage_path / edges_start_end_osmids_csv_file_name) as file:
            reader = csv.reader(file)
            for edge in list(reader):
                osmids.add(edge[0])
                osmids.add(edge[1])
        
        return osmids

    def __get_edges_coordinates_csv_file_name(self) -> str:
        return self.__get_base_file_name() + '_edges_coordinates.csv'

    def __get_node_coordinates(self, osmid: int) -> List[float]:
        api = osm.OsmApi()
        node = api.NodeGet(osmid)

        return [node['lat'], node['lon']]