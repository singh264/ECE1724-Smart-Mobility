# Problem Dataset 
The following document contains key map locations and APIs utilized for the project. All of the following data is publically available though it has been configured to fit our narative.  

**Chosen Location**: North York, Ontario, Canada

**Breif Summary** 

We use osmnx API to get the information about the nodes and edges contained in the map of North York. Locations of fire stations and hospitals are identified using the Overpass scripts. We also use live and historical accident and construction locations to identify the optimal path for an emergency vehicle to meet a crucial response time. We have utilized Bing Traffic API to capture all the accident and construction zones that have occurred within the time frame of 3 weeks. This acts as an historical data for the project. We have used weighted-KNN algorithm on this data to help us capture zones of busy areas. Along, with this, live accident data is used to identify the busy streets. We plan to design an algorithm that integrates all these data to fine-tune the routing of emergency vehicles. The objectives considered include minimising the total travel time to a dispatch location while eliminating busy areas, which is what the public is concerned with the most.     

Outlined bellow is a detailed summary of the data we have utlizied and/or captured for this project. 

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

* Live traffic incident data in North York
  * Using our **custom** `BingTrafficIncidentsApi`
  * Source code: `bing_traffic/bing_traffic_incidents_api.py:get_live_traffic_incidents(..)` 
  * We take a snapshot of the current accidents to map out edge weights on the map. This data is then used once again to send out emergency dispatch at locations where there are severe accidents.

* Historical traffic incident data in North York
  * Using our **custom** `BingTrafficIncidentsApi`
  * Source code: `bing_traffic/bing_traffic_incidents_api.py:download_traffic_incidents(..)`
  * All historical traffic incident data can be found on our [Drive](https://drive.google.com/drive/folders/1ObGRrqJbvuVqW3wQDg16Wnjh-9BA0K04)
    * Above data contains the timestamp, origin latitude, origin longitude, destination latitude, destination longitude and the severity of traffic. The traffic data is extracted every hour and converted into a csv file to favor simpler preprocessing and datacleaning methods for the weighted knn. The clustering is weighted upon the severity. 


### Map edges coordinates data - Using `Osmapi`

* Edges coordinates in North York
  * Using our **custom** `MapEdgesCoordinatesDowloader`
  * Source code: `map/map_edges_coordinates_downloader.py:download_edges_coordinates(..)` 
  * All edges coordinates data can be found on our [Drive](https://drive.google.com/drive/folders/1ObGRrqJbvuVqW3wQDg16Wnjh-9BA0K04)
    * Above data is created to save the run-time of the application. Rather than mapping each osmid to its latitude and longitude during runtime, we do this ahead of time to save call to OsmApi each time. This improves the overhead performance significantly. 
  
  
