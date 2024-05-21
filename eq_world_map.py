import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
                    # offline module to render the map

filename = 'data/1.0_month.geojson'
with open(filename,'r', encoding='utf-8') as f:
    all_eq_data = json.load(f) 

all_eq_dicts = all_eq_data['features']

mags , lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    hover_texts.append(title)
    lons.append(lon)
    lats.append(lat)
    mags.append(mag)

# Map the earthquakes
# data = [Scattergeo(lon=lons, lat=lats)]            # Scattergeo allows to overlay scatter plot of geographic data on map.
data = [{
    'type' : 'scattergeo',
    'lon' : lons,
    'lat' : lats,
    'text' : hover_texts,           # plotly's uses this as a label for each marker to show on hover over the marker
    'marker' : {
        'size' : [3*mag for mag in mags],
        'color': mags,
        'colorscale':'Viridis',    # colorscale for dark-blue to bright-yellow
        'reversescale': True,      # We want dark-blue for higher magnitude and bright-yellow for lower magnitude.
        'colorbar': { 'title' : 'Magnitude'}
    },
}]
my_layout = Layout(title='Global Earthquakes in last Month!')

fig = { 'data':data, 'layout':my_layout}
offline.plot(fig, filename='global_earthquakes.html')