import folium
import os
import webbrowser
from urllib.request import urlopen

def build_map(filepath):
    with open(filepath, 'r') as file:
        for line in file.readlines():
            print(file)

build_map(urlopen("https://www.data.gouv.fr/fr/datasets/r/86a7f194-182e-4be3-ac5a-082d612082fe"))
