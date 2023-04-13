from os import getcwd
from webbrowser import open as w_open
import folium

def build_map(filepath):
    data_list=[]  # list of all building in Angers, France
    town_map=folium.Map(location=[47.471646,-0.551846],zoom_start=14)
    private_map=folium.Map(location=[47.471646,-0.551846],zoom_start=14)
    private=[]
    town=[]
    nb_private=0
    nb_town=0
    with open(filepath,'r',encoding='utf8') as file:
        for line in file:
            line_data=line.strip().split(";")
            if line_data[0]=="Angers" :
                coor=line_data[-1].split(',')
                data_list.append(line_data)
                if line_data[12]=='propriété de la commune':  
                    nb_town+=1
                    town.append(line_data[0])                
                    folium.Marker([float(coor[0]),float(coor[1])],popup=line_data[6],icon=folium.Icon(color='red')).add_to(town_map)
                elif line_data[12]=='propriété privée':
                    nb_private+=1
                    private.append(line_data[0])  
                    folium.Marker([float(coor[0]),float(coor[1])],popup=line_data[6],icon=folium.Icon(color='red')).add_to(private_map)
        
    town_map.save('./templates/embed/public.html')
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
            <!DOCTYPE html>
            <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta http-equiv="X-UA-Compatible" content="IE=edge">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Buildings protected as Historical Monuments (archives), France - CSVDATASDASHBOARD</title>
                    <link rel="stylesheet" href="../static/main.css">
                </head>
                <body>
                    <header>
                        <div>
                            <h1>FRANCE : Buildings protected as Historical Monuments (archives)</h1>
                            <p>Map :</p>
                        </div>
                        <div class="btns">
                            <a id="informations_popup">Informations</a>
                            <a id="change_map_btn"></a>
                        </div>
                    </header>

                    <iframe id="map_iframe" src="" style="width:100%;height:89.5vh;"></iframe>

                    <div id="popup">
                        <div id="popup_public">
                            <h3></h3>
                            <p>Nombre de batiments : """+str(infos["town"]["nb"])+"""</p>
                        </div>
                        <div id="popup_private">
                            <h3></h3>
                            <p>Nombre de batiments : """+str(infos["private"]["nb"])+"""</p>
                        </div>
                    </div>

                    <script src="../static/main.js"></script>
                </body>
            </html>
            """
        )


infos=build_map('datas/db.csv')
build_htmlfile("templates/index.html", infos)

print()
print(f"The HTML file path : {getcwd()}/templates/index.html?map=public")
print()

w_open(getcwd()+"/templates/index.html?map=public")  # this instruction may be not works
