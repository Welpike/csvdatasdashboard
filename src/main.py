import folium
import os
import webbrowser

def build_map(filepath):
    with open(filepath, 'r') as file:
        for line in file.readlines():
            line = line.strip().split(';')
            print(line)

def build_htmlfile(filepath):
    with open(filepath, "w+") as file:
        file.write(
            """
                
            """
        )

"""
pour les 2 cartes :
    - propriété privée
    - propriété communale
"""

build_map('datas/db.csv')
