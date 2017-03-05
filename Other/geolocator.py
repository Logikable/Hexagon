import csv

import geocoder

g = geocoder.ip('me')
print(g.latlng)

lat = g.latlng[0]
lon = g.latlng[1]

with open('Counseling.csv') as f:
    places=[tuple(line) for line in csv.reader(f)]



rel_places = []
for i in xrange(len(places)):
  rel_places.append((places[i][0],places[i][1],places[i][2],abs(float(places[i][3])-lat),abs(float(places[i][4])-lon)))

closest = rel_places[0]
for i in xrange(len(rel_places)):
  if(rel_places[i][3] + rel_places[i][4] < closest[3] + closest[4]):
    closest = rel_places[i]

print(closest)
