import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # for index, column_reader in enumerate(header_row):
    #     print(index, column_reader)

    dates, rains = [], []

    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        # adding format for data

        try:
            rain = float(row[3])
            # PCRP is on row three. making variable of the value
        except ValueError:
            print(f'Missing data for {current_date}')
            # try except for missing data
        else:
            dates.append(current_date)
            # appending dates
            rains.append(rain)
            # appending rain data

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, rains, c='black')
ax.set_title('Amount of rain in Sitka 2018', fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Rainfall measure in mm', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
# there is no rain in Sitka during this time
