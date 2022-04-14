import csv
import matplotlib.pyplot as plt
from datetime import datetime


class WeatherComparison:
    """class to compare the weather in Sitka and Death valley."""

    def __init__(self):
        """initializing attributes."""

        self.filename_1 = 'data/sitka_weather_2018_simple.csv'
        self.filename_2 = 'data/death_valley_2018_simple.csv'
        self.dates, self.highs, self.lows = [], [], []
        self.dates_death, self.highs_death, self.lows_death = [], [], []

    def sitka_high_low(self):
        """Sitka high and low temperatures."""
        with open(self.filename_1) as f1:
            reader = csv.reader(f1)
            header_row = next(reader)

            self.dates, self.highs, self.lows = [], [], []
            for row in reader:
                tmax_index = header_row.index('TMAX')
                tmin_index = header_row.index('TMIN')
                date_index = header_row.index('DATE')
                current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
                header_index = header_row.index('NAME')
                name_sitka = row[header_index]
                self.header = f"High and low temperatures from {name_sitka}"
                try:
                    high = int(row[tmax_index])
                    low = int(row[tmin_index])
                except ValueError:
                    print(f"Missing data for {current_date}")
                    self.dates.append(current_date)
                    # without appending the date
                    # the data cannot be interpreted properly
                    self.highs.append(0)
                    self.lows.append(0)
                else:
                    self.dates.append(current_date)
                    self.highs.append(high)
                    self.lows.append(low)

    def death_valley_high_low(self):
        """High and low temperatures in death valley."""
        with open(self.filename_2) as f2:
            reader = csv.reader(f2)
            header_row = next(reader)

            self.dates_death, self.highs_death, self.lows_death = [], [], []
            for row in reader:
                tmax_index = header_row.index('TMAX')
                tmin_index = header_row.index('TMIN')
                date_index = header_row.index('DATE')
                current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
                header_index = header_row.index('NAME')
                name_valley = row[header_index]
                self.header = f"High and low temperatures from {name_valley}"
                try:
                    high = int(row[tmax_index])
                    low = int(row[tmin_index])
                except ValueError:
                    print(f"Missing data for {current_date}")
                    self.dates_death.append(current_date)
                    # without appending the date
                    # the data cannot be interpreted properly
                    self.highs_death.append(0)
                    self.lows_death.append(0)
                else:
                    self.dates_death.append(current_date)
                    self.highs_death.append(high)
                    self.lows_death.append(low)

        plt.style.use('seaborn')
        fig, ax = plt.subplots()
        ax.plot(self.dates, self.highs, c='red', alpha=0.5)
        ax.plot(self.dates, self.lows, c='blue', alpha=0.5)
        ax.fill_between(self.dates, self.highs, self.lows, facecolor='blue',
                        alpha=0.1)

        ax.plot(self.dates_death, self.highs_death, c='red', alpha=0.5)
        ax.plot(self.dates_death, self.lows_death, c='blue', alpha=0.5)
        ax.fill_between(self.dates_death, self.highs_death, self.lows_death,
                        facecolor='blue', alpha=0.1)

        ax.set_title(f"{self.header}", fontsize=24)
        ax.set_title(f"{self.header}", fontsize=24)
        ax.set_xlabel('', fontsize=16)
        fig.autofmt_xdate()
        ax.set_ylabel('Temperature (F)', fontsize=16)
        ax.tick_params(axis='both', which='major', labelsize=16)

        plt.show()


wc = WeatherComparison()
wc.sitka_high_low()
wc.death_valley_high_low()
# wc.generate_header()
