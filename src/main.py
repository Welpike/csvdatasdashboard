from os import getcwd
from webbrowser import open as w_open
import folium

def build_map(filepath):
    data_list=[]  # list of all building in Angers, France
    town_map=folium.Map(location=[47.471646,-0.551846],zoom_start=13)
    private_map=folium.Map(location=[47.471646,-0.551846],zoom_start=13)
    private=[]
    town=[]
    nb_private=0
    nb_town=0
    with open(filepath,'r',encoding='utf8') as file:
        for line in file:
            line_data=line.strip().split(";")
            if line_data[0]=="Angers" :
                coor=line_data[-1].split(',')
                print(line_data)
                data_list.append(line_data)
                if line_data[12]=='propriété de la commune':  
                    nb_town+=1
                    town.append(line_data[0])                
                    folium.Marker([float(coor[0]),float(coor[1])],popup=line_data[6],icon=folium.Icon(color='red')).add_to(town_map)
                elif line_data[12]=='propriété privée':
                    nb_private+=1
                    private.append(line_data[0])  
                    folium.Marker([float(line_data[coor[0]]),float(coor[1])],popup=line_data[6],icon=folium.Icon(color='red')).add_to(private_map)
        
    town_map.save('./templates/embed/town.html')
    private_map.save('./templates/embed/private.html')

    info={
        "town": {
            "nb": nb_town,
       	    "names": town
        },
        "private": {
            "nb": nb_private,
       	    "names": private
        }
    }
    return(info)

def build_htmlfile(filepath, infos: dict):
    with open(filepath, "w+") as file:
        file.write(
            """
                
            """
        )


infos=build_map('datas/db.csv')
build_htmlfile("templates/index.html", infos)
w_open(getcwd()+"/templates/index.html")
