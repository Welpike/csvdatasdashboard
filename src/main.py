import os
import webbrowser
import folium
"""
def build_map(filepath):
    with open(filepath, 'r') as file:
        for line in file :

        for line in file.readlines():
            line = line.strip().split(';')
            print(line)

def build_htmlfile(filepath):
    with open(filepath, "w+") as file:
        file.write(
            """
                
""")
build_map('datas/db.csv')

"""

def fabricationCarte(fichier):
    liste=[]
    carte_town=folium.Map(location=[47.471646,-0.551846],zoom_start=13)
    carte_private=folium.Map(location=[47.471646,-0.551846],zoom_start=13)
    
    f1=open(fichier,'r',encoding='utf8')
    for ligne in f1:
        ligne_data=ligne.strip().split(";")
        if ligne_data[0]=="Angers" :
            print(ligne_data)
            liste.append(ligne_data)
    private=[]
    town=[]
    for i in liste:
        if i[12]=="propriété privée":
            private.append(i)
        elif i[12]=="propriété de la commune":
            town.append(i)
    f1.close()
    carte_town.save('./templates/embed/town.html')
    carte_private.save('./templates/embed/private.html')
fabricationCarte("datas/db.csv")

