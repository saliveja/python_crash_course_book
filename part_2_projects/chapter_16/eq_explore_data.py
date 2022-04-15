import json

filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)
    # making datat into dictionary

readable_file = 'data/eq_data_1_day_m1.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)
    # put json data ina file
    # indent to match data structure

all_eq_dicts = all_eq_data['features']
# pulling out the number of earthquakes from the json file
# print(len(all_eq_dicts))

mags, lons, lats = [], [], []
# lists: magnitude, longitude, latitude
for eq_dict in all_eq_dicts:
    # for dictionary in all dictionaries
    mag = eq_dict['properties']['mag']
    # earthquake magnitude is stored in properties section
    # and under the key 'mag'
    # each magnitude is stored in the variable mag
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    # and appended to the list mags
    lons.append(lon)
    lats.append(lat)
    print(mags[:10])
    # printing the first ten values
    print(lons[:5])
    print(lats[:5])
