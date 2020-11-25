tags = {
    'amenity':['hospital', 'fire_station'],
}
emergency_locations = ox.geometries_from_place('North York, Ontario, Canada', tags=tags)
df = pd.DataFrame(emergency_locations) 
dic = df['osmid'].to_dict()
nod_ = [dic[a] for a, b in dic.items()] # list of osmid of amenities 

dest = {}
cap = [2 for i in range(len(nod_))] # cap = capacity at each amenity (hospital + fire-station)
for i in range(len(nod_)):
    dest[nod_[i]] = cap[i] # dest = map amenity (hospital/fire-station) osmid to its capacity

source = []

for emergency_incident in emergency_incidents: # holds the nearest node to each top 10 accident
    point = (float(emergency_incident.get_summary()['origin coordinate latitude']), float(emergency_incident.get_summary()['origin coordinate longitude']))
    source.append(osmnx.distance.get_nearest_node(north_york_map.graph, point, method='haversine', return_dist=False))

# TODO - use Ameneities.lat, Amenities.lon
lat_long_map = {} # dest osmid (of amenimity) -> {lat, lon}
to_rem = []
for a, b in dest.items():
    try:
        lat_long_map[a] = {'lat': api.NodeGet(a)['lat'], 'lon': api.NodeGet(a)['lon']}
    except Exception as e:
        print(f'removing.. {a} since api call fails...')
        to_rem.append(a)
for i in to_rem: # remove 
    if i in dest: dest.pop(i, None)
print(f'cleaned dest : {dest}')   

res = {}    
for i in range(len(source)):
    temp_ = {}
    for a, b in dest.items(): # for each source (acccident), look at each destination (hospital/firestation)
        dist = osmnx.distance.euclidean_dist_vec(lat_long_map[a]['lat'], 
                                             lat_long_map[a]['lon'], 
                                             ny_nodes[source[i]]['lat'],
                                             ny_nodes[source[i]]['lon'])

        # TODO - do for hospital and firestation separately
        temp_[a] = dist*100 # temp holds osmid_hospital/firestation -> distance
        
    # Pick the closest destination (hospital/firestation) and the one that has capacity > 0
    od = {a: b for a, b in sorted(temp_.items(), key=lambda item: item[1], reverse=False)}
    Touched = False
    for x, y in od.items():
        if x in dest and dest[x]!=0 and Touched==False:
            res[source[i]] = x # res = source (accident) osmid -> desitination (hospital/firestation) osmid
            dest[x] = dest[x] - 1
            Touched = True

count = 0
for a, b in dest.items(): # a = hostpial/firestation osmid , b = capacity
    if b==0:
        count += 1

secondary_dest_nodes = {}

if count==len(dest): # all hospital/firestations have no spare capcity
    # TODO change dest = source below
    # to make 
    secondary_dest_nodes = dest 


if secondary_dest_nodes:
    print('All ER busy.. finding the closest responder')
    for i in range(len(source_)):
        temp__ = {}
        for a, b in secondary_dest_nodes.items():
            dist_ = osmnx.distance.euclidean_dist_vec(MM.nodes[a]['x'], 
                                                MM.nodes[a]['y'], 
                                                MM.nodes[source_[i]]['x'],
                                                MM.nodes[source_[i]]['y'])
        
            temp__[a] = dist_*100
        od_ = {a: b for a, b in sorted(temp__.items(), key=lambda item: item[1], reverse=False)}


        Touched = False
        for x, y in od_.items():
            if x in dest and dest[x]!= -1 and Touched==False:
                res[source_[i]] = x
                dest[x] = -1
                Touched = True
                
print(f'Source: {source}')
print(f'Destination: {dest}')
print(f'Mapping Source to destination: {res}')
