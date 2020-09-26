import folium
import pandas as pd

volcano = pd.read_csv("Volcanoes.txt")
lat = list(volcano['LAT'])
lon = list(volcano['LON'])
elev = list(volcano['ELEV'])

# a more concise format for displaying popup:
html = """<h4>Volcano information:</h4>
Height: %s m
"""

# a tile is simply a base layer or background offered by JavaScript
# just specify which tile in the str format
# zoom scale is 1-18 (1 being zoomed out all the way)
map = folium.Map(location=[40.451075,-86.919548], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My School")
fg.add_child(folium.Marker(location=[40.451075,-86.919548], popup="Purdue University", icon=folium.Icon(color='black')))

#creating a function to pass to icon color argument for specified elev ranges:
def color_change(elevation):
    if elevation < 1000:
        return 'green'
    elif elevation >= 1000 and elevation < 2500:
        return 'orange'
    else:
        return 'red'

# put the geo-polygons before the volcano markers in order to click on popup:
fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), 
style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000  
else 'orange' if x['properties']['POP2005'] >= 10000000 and x['properties']['POP2005'] < 20000000 else 'red'}))

for i, j, k in zip(lat, lon, elev):
    iframe = folium.IFrame(html=html % str(k), width=200, height=100)
    fg.add_child(folium.CircleMarker(location=[i,j], radius=6, popup=folium.Popup(iframe), 
    fill_color=color_change(k), color='grey', fill_opacity=0.7))


map.add_child(fg)
map.save("Map1.html")