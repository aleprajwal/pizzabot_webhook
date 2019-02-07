
import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyB9i4U1AFlnh5p0eFkQtK-csvzaDUq9h1g')

# Geocoding an address
geocode_result = gmaps.geocode('kathmandu, nepal')

f= open('geocode.txt', 'w')
f.write(geocode_result)
f.close()
