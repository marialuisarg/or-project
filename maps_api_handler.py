import urllib.parse
import googlemaps
import requests
import json

#Perform request to use the Google Maps API web service
API_key = 'AIzaSyBZWxSWokcKsYv-j54EIs6NwCawgHHc5WY'
API_URL = "https://maps.googleapis.com/maps/api/distancematrix/json"  

def build_url(origin_id, destination_id):
    print(origin_id)
    
    gmaps = googlemaps.Client(key=API_key)
    
    dist_matrix = gmaps.distance_matrix(origin_id, destination_id, units='metric')
    
    # params = {
    #     "destinations": "place_id:{}".format(destination_id),
    #     "origins": "place_id:{}".format(origin_id),  
    #     "units": "metric",
    #     "key": API_key, 
    # }

    # url = f"{API_URL}?{urllib.parse.urlencode(params)}"

    return dist_matrix

#def send_data_to_api(delivery_data):
    
