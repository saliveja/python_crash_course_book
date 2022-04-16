import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# offline module renders the map

filename = 'data/significant_week.geojson.json'
with open(filename) as f:
    all_eq_data = json.load(f)
    # making datat into dictionary

readable_file = 'data/significant_week.geojson.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)
    # put json data ina file
    # indent to match data structure

all_eq_dicts = all_eq_data['features']
# pulling out the number of earthquakes from the json file
# print(len(all_eq_dicts))

mags, lons, lats, hover_texts = [], [], [], []
# lists: magnitude, longitude, latitude
# hover_texts store the label for each marker
for eq_dict in all_eq_dicts:
    # for dictionary in all dictionaries
    mag = eq_dict['properties']['mag']
    # earthquake magnitude is stored in properties section
    # and under the key 'mag'
    # each magnitude is stored in the variable mag
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    # this contains a descriptive name of magnitude and location
    # assigning to variable title
    mags.append(mag)
    # and appended to the list mags
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)
    # appending title to list hover_texts
    print(mags[:10])
    # printing the first ten values
    print(lons[:5])
    print(lats[:5])

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    # when overing over the marker the name and location of each
    # mag will be visible
    'marker': {
        'size': [5 * mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        # a colorscale that ranges from dark blue to bright yellow
        'reversescale': True,
        # reverse for colors, using yellow for the lowest values
        # and dark blue for the highest values
        # the colorbar allow us to control the appearance
        'colorbar': {'title': 'Magnitude'},
        # the colorbar is called Magnitude so we understand
        # what we are communicating
    },
}]
# making data into a dictionary, which is better for customization
# changing the size of markers depending on the magnitude of the earthquake
my_layout = Layout(title='Global Earthquakes')
# adding a title
fig = {'data': data, 'layout': my_layout}
# creating the chart
offline.plot(fig, filename='global_earthquakes.html')
# assigning file name
