import csv
import matplotlib.pyplot as plt
from datetime import datetime

class WeatherComparison:
    """class to compare the weather in Sitka and Death valley."""

    def __init__(self, date='', header='', low='', high=''):
        """initializing attributes."""

        self.filename_1 = 'data/sitka_weather_2018_simple.csv'
        self.filename_2 = 'data/death_valley_2018_simple.csv'
        self.date = date
        self.header = header
        self.low = low
        self.high = high

    def high_low_temperatures(self):
        """Sitka high and low temperatures."""

        with open(self.filename_1) as f1:
            reader = csv.reader(f1)
            header_row = next(reader)

        for index, column_header in enumerate(header_row):
            print(index, column_header)

        dates, highs, lows = [], [], []
        for row in reader:
            current_date = datetime.strptime(self.date, '%Y-%m-%d')
            try:
                self.high = int(row['TMAX'])
                low = int(row[5])
            except ValueError:
                print(f"Missing data for {current_date}")
                dates_2.append(current_date)
                # without appending the date
                # the data cannot be interpreted properly
                highs_2.append(0)
                lows_2.append(0)
            else:
                dates_2.append(current_date)
                highs_2.append(high)
                lows_2.append(low)

            dates.append(current_date)
            highs.append(self.high)
            lows.append(self.low)

    def death_valley_weather(self):
        """High and low temperatures in death valley."""
        with open(self.filename_2) as f2:
            reader = csv.reader(f2)
            header_row = next(reader)

        for index, column_header in enumerate(header_row):
            print(index, column_header)

        dates_2, highs_2, lows_2 = [], [], []
        for row in reader:
            current_date = datetime.strptime(self.date, '%Y-%m-%d')
            try:
                high = int(row[4])
                low = int(row[5])
            except ValueError:
                print(f"Missing data for {current_date}")
                dates_2.append(current_date)
                # without appending the date
                # the data cannot be interpreted properly
                highs_2.append(0)
                lows_2.append(0)
            else:
                dates_2.append(current_date)
                highs_2.append(high)
                lows_2.append(low)

    def generate_header(self):
        """generating appropriate header for the graph."""
        with open(self.filename_1) as f1:
            reader = csv.reader(f1)
            header_row = next(reader)

        for index, column_header in enumerate(header_row):
            print(index, column_header)
            for row in reader:
                self.header = f"High and low temperatures from {str(row[1])}"

        plt.style.use('seaborn')
        fig, ax = plt.subplots()
        ax.plot(dates_1, highs_1, c='red', alpha=0.5)
        ax.plot(dates_1, lows_1, c='blue', alpha=0.5)
        ax.fill_between(dates_1, highs_1, lows_1, facecolor='blue', alpha=0.1)

        ax.plot(dates_2, highs_2, c='red', alpha=0.5)
        ax.plot(dates_2, lows_2, c='blue', alpha=0.5)
        ax.fill_between(dates_2, highs_2, lows_2, facecolor='blue', alpha=0.1)

        ax.set_title('Sitka and Death valley high and low temp 2018',
                     fontsize=24)
        ax.set_xlabel('', fontsize=16)
        fig.autofmt_xdate()
        ax.set_ylabel('Temperature (F)', fontsize=16)
        ax.tick_params(axis='both', which='major', labelsize=16)

        plt.show()

wc = WeatherComparison()
wc =
