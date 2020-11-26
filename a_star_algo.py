ll_map = {}
for i in range(len(amenities)):
    ll_map[amenities[i].osmid] = {'lat': amenities[i].lat, 'lon': amenities[i].lon}


tags1 = {
    'amenity':['hospital'],
}

emergency_locations1 = ox.geometries_from_place('North York, Ontario, Canada', tags=tags1)
df = pd.DataFrame(emergency_locations1) 
dic = df['osmid'].to_dict()
nod_ = [dic[a] for a, b in dic.items()] # list of osmid of amenities 

dest = {}
cap = [2 for i in range(len(nod_))] # cap = capacity at each amenity (hospital + fire-station)
for i in range(len(nod_)):
    dest[nod_[i]] = cap[i] # dest = map amenity (hospital/fire-station) osmid to its capacity

# source = [56922195, 29658912, 6894245117, 29656792, 1287736695, 73461503, 267197091, 393521690, 1758011800, 432736587]
###### Comment these when using hard coded source
source = []

for emergency_incident in emergency_incidents: # holds the nearest node to each top 10 accident
    point = (float(emergency_incident.get_summary()['origin coordinate latitude']), float(emergency_incident.get_summary()['origin coordinate longitude']))
    source.append(osmnx.distance.get_nearest_node(north_york_map.graph, point, method='haversine', return_dist=False))
######
res = {}    
for i in range(len(source)):
    temp_ = {}
    for a, b in dest.items(): # for each source (acccident), look at each destination (hospital/firestation)
        dist = osmnx.distance.euclidean_dist_vec(ll_map[a]['lat'], 
                                             ll_map[a]['lon'], 
                                             ny_nodes[source[i]]['lat'],
                                             ny_nodes[source[i]]['lon'])

        temp_[a] = dist # temp holds osmid_hospital/firestation -> distance
        
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
    if b==0: count += 1

secondary_dest_nodes = {}

if count==len(dest): # all hospital/firestations have no spare capcity
    secondary_dest_nodes = source 


if secondary_dest_nodes:
    print('All ER busy.. finding the closest responder')
    for i in range(len(source_)):
        temp__ = {}
        for a, b in secondary_dest_nodes.items():
            dist_ = osmnx.distance.euclidean_dist_vec(ll_map[a]['x'],
                                                ll_map[a]['y'], 
                                                ny_nodes[source[i]]['x'],
                                                ny_nodes[source[i]]['y'])
        
            temp__[a] = dist_
        od_ = {a: b for a, b in sorted(temp__.items(), key=lambda item: item[1], reverse=False)}


        Touched = False
        for x, y in od_.items():
            if x in dest and dest[x]!= -1 and Touched==False:
                res[source_[i]] = x
                dest[x] = -1
                Touched = True
                

tags2 = {
    'amenity':['fire_station'],
}
emergency_locations2 = ox.geometries_from_place('North York, Ontario, Canada', tags=tags2)
df2 = pd.DataFrame(emergency_locations2) 
dic2 = df2['osmid'].to_dict()

nod_2 = [dic2[a] for a, b in dic2.items()] # list of osmid of amenities 

dest2 = {}
cap2 = [2 for i in range(len(nod_2))] # cap = capacity at each amenity (hospital + fire-station)
for i in range(len(nod_2)):
    dest2[nod_2[i]] = cap2[i] # dest = map amenity (hospital/fire-station) osmid to its capacity


res2 = {}    
for i in range(len(source)):
    temp_2 = {}
    for a, b in dest2.items(): # for each source (acccident), look at each destination (hospital/firestation)
        dist2 = osmnx.distance.euclidean_dist_vec(ll_map[a]['lat'], 
                                             ll_map[a]['lon'], 
                                             ny_nodes[source[i]]['lat'],
                                             ny_nodes[source[i]]['lon'])
        temp_2[a] = dist2 # temp holds osmid_hospital/firestation -> distance
        
    # Pick the closest destination (hospital/firestation) and the one that has capacity > 0
    od2 = {a: b for a, b in sorted(temp_2.items(), key=lambda item: item[1], reverse=False)}
    Touched2 = False
    for x, y in od2.items():
        if x in dest2 and dest2[x]!=0 and Touched2==False:
            res2[source[i]] = x # res = source (accident) osmid -> desitination (hospital/firestation) osmid
            dest2[x] = dest2[x] - 1
            Touched2 = True




count2 = 0
for a, b in dest2.items(): # a = hostpial/firestation osmid , b = capacity
    if b==0:
        count2 += 1

secondary_dest_nodes2 = {}

if count2==len(dest2): # all hospital/firestations have no spare capcity
    secondary_dest_nodes2 = source 


if secondary_dest_nodes2:
    print('All ER busy.. finding the closest responder')
    for i in range(len(source_)):
        temp__2 = {}
        for a, b in secondary_dest_nodes2.items():
            dist_2 = osmnx.distance.euclidean_dist_vec(ll_map[a]['x'],
                                                ll_map[a]['y'], 
                                                ny_nodes[source[i]]['x'],
                                                ny_nodes[source[i]]['y'])
        
            temp__2[a] = dist_2
        od_2 = {a: b for a, b in sorted(temp__2.items(), key=lambda item: item[1], reverse=False)}


        Touched2 = False
        for x, y in od_2.items():
            if x in dest2 and dest2[x]!= -1 and Touched2==False:
                res2[source_[i]] = x
                dest2[x] = -1
                Touched2 = True
                
print(f'Source: {source}')
print(f'Destination - FIRE: {dest2}')
print(f'Mapping Source to destination - FIRE: {res}')
print(f'Destination - AMBULANCE: {dest}')
print(f'Mapping Source to destination - AMBULANCE: {res2}')
