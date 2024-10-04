import googlemaps
import requests
from types import SimpleNamespace

import tkinter as tk
import webbrowser
import gmaps
import gmplot
from polyline import decode  # Para decodificar polyline

#Perform request to use the Google Maps API web service
API_key = 'AIzaSyDfkPrtiT_mO2xw5leQ1nJnObYR-4asiAU'
API_URL = "https://maps.googleapis.com/maps/api/distancematrix/json"  

def build_url(id_list):
    gmaps = googlemaps.Client(key=API_key)
    
    dist_json = gmaps.distance_matrix(id_list, id_list, units='metric')
    
    distance_matrix = []
    for row in dist_json['rows']:
        distances = [element['distance']['value'] for element in row['elements']]
        distance_matrix.append(distances)
        
    time_matrix = []
    for row in dist_json['rows']:
        time = [element['duration']['value'] for element in row['elements']]
        time_matrix.append(time)

    return distance_matrix,time_matrix

def plot_result(id_list, model):
    gmaps = googlemaps.Client(key=API_key)
    
    edges = []
    l = list(model.keys())
    for i in l:
        if model[i]() == 1:
            edges.append(i)
            
    # Criando um dicionário para mapear os valores y para suas respectivas duplas
    route_map = {x: y for x, y in edges}

    # Encontrando o início da sequência
    result = []
    
    # Iniciar com a primeira dupla
    first = edges[0]

    result.append(first)

    # Construindo a sequência
    current = first[1]  # Pegando o segundo valor da primeira dupla
    end = first[0]      # Pegando o último ponto da rota (igual ao primeiro)

    waypoints = []
    # Continuando até que não haja mais correspondências
    while current in route_map:
        next = (current, route_map[current])
        result.append(next)
        waypoints.append(id_list[current-1])
        current = route_map[current]  # Atualizando o valor atual para o próximo
        if current == end:
            break
    
    directions = gmaps.directions(origin=id_list[0],destination=id_list[0],mode="driving",waypoints=waypoints)
    
    # Extrair as coordenadas de cada step da rota
    latitudes = []
    longitudes = []

    for leg in directions[0]['legs']:
        for step in leg['steps']:
            # Decodificar a polyline para obter todas as coordenadas do step
            polyline = step['polyline']['points']
            points = decode(polyline)
            
            for lat, lng in points:
                latitudes.append(lat)
                longitudes.append(lng)

    # Centralizar o mapa na primeira coordenada
    gmap = gmplot.GoogleMapPlotter(latitudes[0], longitudes[0], 13)

    # Plotar a rota completa no mapa
    gmap.plot(latitudes, longitudes, 'blue', edge_width=5)

    # Salvar o mapa como HTML
    gmap.draw("mapa.html")
    
