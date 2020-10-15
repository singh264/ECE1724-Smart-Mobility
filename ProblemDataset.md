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
 
 ### Traffic Data - Using `Bing Traffic` API
 The traffic data contains the timestamp, origin latitude, origin longitude, destination latitude, destination longitude and the severity of Traffic. The traffic data is extracted every hour and converted into a csv file to favor simpler preprocessing and datacleaning methods for the weighted knn. The clustering is weighted upon the severity.  
