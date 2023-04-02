import csv
from datetime import datetime
import numpy as np
from matplotlib import pyplot as plt

def Rotterdam(filename, dates, highs, lows):
	"""Get the highs and lows from a data file."""
	with open(filename) as f:
		reader = csv.reader(f)
		header_row = next(reader)
		date_index = header_row.index('DATE')
		high_index = header_row.index('TMAX')
		low_index = header_row.index('TMIN')

		for row in reader:
			try:
				current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
				high = int(row[high_index])
				low = int(row[low_index])
			except ValueError:
				print(current_date, 'missing data')
			else:
				dates.append(current_date)
				highs.append(high)
				lows.append(low)

def BeverlyHills(filename, dates, highs, lows):
	"""Get the highs and lows from a data file."""
	with open(filename) as f:
		reader = csv.reader(f)
		header_row = next(reader)
		date_index = header_row.index('DATE')
		high_index = header_row.index('TMAX')
		low_index = header_row.index('TMIN')

		for row in reader:
			try:
				current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
				high = int(row[high_index])
				low = int(row[low_index])
			except ValueError:
				print(current_date, 'missing data')
			else:
				dates.append(current_date)
				highs.append(high)
				lows.append(low)

# Get Rotterdam data.
dates, highs, lows = [], [], []
Rotterdam('data/rotterdam_2020.csv', dates, highs, lows)

# Plot Rotterdam weather data.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.6)
plt.plot(dates, lows, c='blue', alpha=0.6)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.15)

# Get Beverly Hills data.
dates, highs, lows = [], [], []
BeverlyHills('data/beverly_hills_2020.csv', dates, highs, lows)

# Add Beverly Hills data to current plot.
plt.plot(dates, highs, c='m', alpha=0.3)
plt.plot(dates, lows, c='c', alpha=0.3)
plt.fill_between(dates, highs, lows, facecolor='c', alpha=0.05)

# Format plot.
title = "Daily high and low temperatures - 2020"
title += "\nRotterdam, Netherlands. Beverly Hills, California"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.ylim(10, 130)
plt.legend(["High temperatures Rotterdam", "Low temperatures Rotterdam",
 "Low temperatures Beverly Hills", "High temperatures Beverly Hills"], loc ="upper left")
plt.show()
