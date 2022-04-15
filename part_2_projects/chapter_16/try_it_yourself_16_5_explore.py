import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/poland_high_low_rain_2022.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_reader in enumerate(header_row):
        print(index, column_reader)

    dates, rains = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            rain = float(row[3])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            rains.append(rain)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, rains, c='purple')
title = 'Daily amount of rain in Poland 2022'
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Amount of rain (mm)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
