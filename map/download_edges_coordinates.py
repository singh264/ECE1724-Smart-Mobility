import json 
from pathlib import Path

from map_edges_coordinates_downloader import MapEdgesCoordinatesDowloader

if __name__ == '__main__':
    config = json.loads(Path("./config.json").read_text())

    edges_coordinates_downloader = MapEdgesCoordinatesDowloader(place=config['place'])
    edges_coordinates_downloader.download_edges_coordinates()