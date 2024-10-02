import urllib.parse
import googlemaps
import requests
import json
from types import SimpleNamespace

#Perform request to use the Google Maps API web service
API_key = 'AIzaSyBZWxSWokcKsYv-j54EIs6NwCawgHHc5WY'
API_URL = "https://maps.googleapis.com/maps/api/distancematrix/json"  

def build_url(id_list):
    gmaps = googlemaps.Client(key=API_key)
    
    dist_json = gmaps.distance_matrix(id_list, id_list, units='metric')
    
    #x = json.loads(dist_json, object_hook=lambda d: SimpleNamespace(**d))
    
    #print(dist_json)
    
    distance_matrix = []
    for row in dist_json['rows']:
        distances = [element['distance']['value'] for element in row['elements']]
        distance_matrix.append(distances)
        
    time_matrix = []
    for row in dist_json['rows']:
        time = [element['duration']['value'] for element in row['elements']]
        time_matrix.append(time)

    return distance_matrix,time_matrix

#def send_data_to_api(delivery_data):
    
