import csv

import geocoder

g = geocoder.ip('me')
print(str(g.latlng[0]) + ',' + str(g.latlng[1]))

# lat = g.latlng[0]
# lon = g.latlng[1]

# with open('Counseling.csv') as f:
#     places=[tuple(line) for line in csv.reader(f)]



# rel_places = []
# for i in range(len(places)):
#   rel_places.append((places[i][0],places[i][1],places[i][2],abs(float(places[i][3])-lat),abs(float(places[i][4])-lon)))

# closest = rel_places[0]
# for i in range(len(rel_places)):
#   if(rel_places[i][3] + rel_places[i][4] < closest[3] + closest[4]):
#     closest = rel_places[i]

# print(closest)
