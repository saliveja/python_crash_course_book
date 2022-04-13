import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_2018_simple.csv'
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

    for index, column_header in enumerate(header_row):
        # enumerate returns the index and value for each item
        print(index, column_header)
        # ie. 1 STATION

    dates, highs, lows = [], [], []
    # creating two empty lists to store the dates and the high temperatures
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        # converting date to a datetime object
        high = int(row[5])
        # this refers to row 5 in index which is high temperatures (TMAX)
        low = int(row[6])
        # low equals the low temperatures (TMIN)
        dates.append(current_date)
        # datetime object appended to list dates
        highs.append(high)
        # each are appended to the list highs
        lows.append(low)
        # appending the low temperatures to the list lows

print(highs)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')
# graph line is colored red
# making graph of high temps
ax.plot(dates, lows, c='blue')
# adding dates and data for low temp in blue color
ax.set_title('Daily high and low temperatures - 2018', fontsize=24)
# overall title
ax.set_xlabel('', fontsize=16)
# x has no label
fig.autofmt_xdate()
# draws the date labels diagonally so they don't overlap
ax.set_ylabel('Temperature (F)', fontsize=16)
# y label displays temperatures
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
