import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_reader in enumerate(header_row):
        print(index, column_reader)
        # TOBS is a temperature reading at a specific observation time

    dates, highs, lows = [], [], []
    # creating two empty lists to store the dates and the high temperatures
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        # converting date to a datetime object
        try:
            high = int(row[4])
            # this refers to row 5 in index which is high temperatures (TMAX)
            low = int(row[5])
            # low equals the low temperatures (TMIN)
        except ValueError:
            print(f"Missing data for {current_date}")
            # whenever there is any temperature data missing
            # there will be a message printed, but the program will continue

        else:
            dates.append(current_date)
            # datetime object appended to list dates
            highs.append(high)
            # each are appended to the list highs
            lows.append(low)
            # appending the low temperatures to the list lows

# print(highs)
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
# graph line is colored red
# making graph of high temps
# alpha controls a colors transparency where 0 is complete transparent
# and 1 is opaque
ax.plot(dates, lows, c='blue', alpha=0.5)
# adding dates and data for low temp in blue color
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
# filling the space between the highs and lows with a transparent blue color
title = 'Daily high and low temperatures - 2018\nDeath Valley, CA'
ax.set_title(title, fontsize=20)
# overall title
ax.set_xlabel('', fontsize=16)
# x has no label
fig.autofmt_xdate()
# draws the date labels diagonally so they don't overlap
ax.set_ylabel('Temperature (F)', fontsize=16)
# y label displays temperatures
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
