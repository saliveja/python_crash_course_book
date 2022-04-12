import csv

filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    # the csv.reader() returns a reader object
    # return a string each time the next method is called
    header_row = next(reader)
    # the header STATION represent the code for the weather station
    # NAME indicates that the second value in each line is the name
    # of the weather station
    # The rest is the weather data: TMAX (high temperature),
    # TMIN (low temperature)
    # print(header_row)

    for index, column_header in enumerate(header_row, +1):
        # enumerate returns the index and value for each item
        print(index, column_header)
