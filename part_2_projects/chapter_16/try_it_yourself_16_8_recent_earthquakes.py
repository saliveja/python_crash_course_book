import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/significant_month.geojson.json'
with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = 'data/significant_month.geojson.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)

all_eq_dicts = all_eq_data['features']

mags, lons, lats, hover_texts, times = [], [], [], [], []

for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)

header = all_eq_data['metadata']['title']

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'time': times,
    'marker': {
        'size': [3 * mag for mag in mags],
        'color': mags,
        'colorscale': 'Rainbow',
        'colorbar': {'title': 'Magnitude'},
    },
}]

my_layout = Layout(title=header)
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
