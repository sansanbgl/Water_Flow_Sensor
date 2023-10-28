import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV file
data = pd.read_csv('./data-s-4.csv', sep=';', header=None, names=['Time', 'Series1', 'Series2','J', 'K', 'L', 'M'])
# Separate the data into two series
time = data['Time']
series1 = data['Series1']
series2 = data['Series2']

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(time, series1, label="Series 1", marker='o')
plt.plot(time, series2, label="Series 2", marker='s')
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Series 1 and Series 2 over Time')
plt.legend()
plt.grid(True)

plt.show()
