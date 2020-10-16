# Problem Dataset 
The following document contains key map locations and APIs utilized for the project. All of the following data is publically available for everyone to use. 

**Chosen Location**: North York, Ontario, Canada

## Geospatial Datasets

### Amenities - Using `Overpass turbo`'s Wizard 
For the problem we are solving, we need Fire Stations and Hospitals. Hence, the following is utilized. 

The following `Overpass turbo`'s wizard synatx and script:
* Firestations in North York 
  * **`amenity= fire_station in "North York, Ontario, Canada"`** to find all Firestations in North York. 
  * [Script](./Dataset/scripts/firestations_northyork.oql) 
* Hospitals in North York 
  * **`amenity= hospital in "North York, Ontario, Canada"`** to find all Firestations in North York. 
  * [Script](./Dataset/scripts/hospitals_northyork.oql)


### Traffic data - Using `Bing Traffic API`
We are collecting traffic incident data only for our chosen location: North York, Ontario, Canada.

* Live traffic incident data in North York
  * Using our custom `BingTrafficIncidentsApi`
  * Source code: `bing_traffic/bing_traffic_incidents_api.py:get_live_traffic_incidents(..)` 

* Historical traffic incident data in North York
  * Using our custom `BingTrafficIncidentsApi`
  * Source code: `bing_traffic/bing_traffic_incidents_api.py:download_traffic_incidents(..)`
  * All historical traffic incident data can be found on our [Drive](https://drive.google.com/drive/folders/1ObGRrqJbvuVqW3wQDg16Wnjh-9BA0K04)

### Map edges coordinates data - Using `Osmapi`
We are collecting map edges coordinate data only for our chosen location: North York, Ontario, Canada.

* Edges coordinates in North York
  * Using our custom `MapEdgesCoordinatesDowloader`
  * Source code: `map/map_edges_coordinates_downloader.py:download_edges_coordinates(..)` 
  * All edges coordinates data can be found on our [Drive](https://drive.google.com/drive/folders/1ObGRrqJbvuVqW3wQDg16Wnjh-9BA0K04)

