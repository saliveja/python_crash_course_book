import csv
import matplotlib.pyplot as plt
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
from datetime import datetime

filename = 'data/world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_reader in enumerate(header_row):
        print(index, column_reader)

    lats, lons, bright = [], [], []

    for row in reader:
        # acq_date = datetime.strptime(row[5], '%Y-%m-%d')
        lon = float(row[1])
        lat = float(row[0])
        brightness = float(row[2])
        # dates.append(acq_date)
        lats.append(lat)
        lons.append(lon)
        bright.append(brightness)

data = [{
    'type': 'scattergeo',
    'lon': lons[:500],
    'lat': lats[:500],
    # 'date': dates,
    # 'bright': bright,
    'marker': {
        'size': [0.06 * brightness for brightness in bright],
        'color': bright,
        'colorscale': 'Rainbow',
        'colorbar': {'title': 'Intensity of fires'},

    },
}]

my_layout = Layout(title='World fires 22 September 2018')
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='world_fires_1_day.html')
