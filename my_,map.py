import folium
import random
import pandas as pd

def foo(elevation):
    if d < 1000:
        return "green"
    elif d >= 1000 and d < 3000:
        return "orange"
    else:
        return "red"

map = folium.Map(tiles="Stamen Toner", max_bounds=True, control_scale=True)

vol_file = pd.read_csv(r"mapping/volcanoes.txt")
lat = vol_file["LAT"]
lon = vol_file["LON"]
name = vol_file["NAME"]
elev = vol_file["ELEV"]
loc = vol_file["LOCATION"]
tp = vol_file["TYPE"]

lc = folium.LayerControl(collapsed=False)

geo_group = folium.FeatureGroup("Population")
data_group = folium.FeatureGroup("Volcanoes")

geo = folium.GeoJson(open(r"mapping/world.json", encoding="utf-8-sig").read(), style_function=lambda x: {"fillColor":"green" if x["properties"]["POP2005"] < 10000000
 else "orange" if 10000000 <= x["properties"]["POP2005"] < 20000000 else "red"})

geo_group.add_child(geo)

for a,b,c,d,e,f in zip(lat, lon, name, elev, loc, tp):
    data_group.add_child(folium.CircleMarker(location=(a,b), radius=5, tooltip=c, popup=(str(d) + " m" + "\n" + e + "\n" + f), color=foo(d), fill=True))

map.add_child(data_group)
map.add_child(geo_group)
map.add_child(lc)
map.save(r"mapping/my_map.html")