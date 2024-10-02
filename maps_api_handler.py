import urllib.parse
import requests
import json

#Perform request to use the Google Maps API web service
API_key = 'AIzaSyBZWxSWokcKsYv-j54EIs6NwCawgHHc5WY'
API_URL = "https://maps.googleapis.com/maps/api/distancematrix/json"  

def build_url(origin_id, destination_id):
    
    params = {
        "origins": "place_id:{}".format(origin_id),  
        "destinations": "place_id:{}".format(destination_id),
        "key": API_key, 
    }

    url = f"{API_URL}?{urllib.parse.urlencode(params)}"

    return url

#def send_data_to_api(delivery_data):
    
