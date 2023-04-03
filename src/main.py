from os import getcwd
from webbrowser import open as w_open
import folium

def build_map(filepath):
    data_list=[]  # list of all building in Angers, France
    town_map=folium.Map(location=[47.471646,-0.551846],zoom_start=13)
    private_map=folium.Map(location=[47.471646,-0.551846],zoom_start=13)
    with open(filepath,'r',encoding='utf8') as file:
        for line in file:
            line_data=line.strip().split(";")
            if line_data[0]=="Angers" :
                print(line_data)
                data_list.append(line_data)
        private=[]
        town=[]
        for i in data_list:
            if i[12]=="propriété privée":
                private.append(i)
            elif i[12]=="propriété de la commune":
                town.append(i)
    town_map.save('./templates/embed/town.html')
    private_map.save('./templates/embed/private.html')

def build_htmlfile(filepath):
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
                <h1>FRANCE : Buildings protected as Historical Monuments (archives)</h1>
                <p>Map :</p>
                <iframe id="map_iframe" src="" height="700" width="1000"></iframe>

                <a id="change_map_btn"></a>

                <script src="../static/main.js"></script>
            </body>
            </html>
            """
        )


build_map('datas/db.csv')
build_htmlfile('templates/index.html')
w_open(getcwd()+"/templates/index.html")
