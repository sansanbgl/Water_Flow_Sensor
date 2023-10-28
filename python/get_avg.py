import pandas as pd

# Data
data = [
    (70, 17, 25, 2, 3, 96, 0),
    (80, 20, 27, 2, 3, 140, 0),
    (90, 19, 26, 2, 3, 182, 0),
    (100, 20, 25, 2, 3, 226, 0),
    (110, 19, 26, 2, 3, 268, 0),
    (120, 20, 25, 2, 3, 312, 0),
    (130, 19, 25, 2, 3, 354, 0),
    (140, 19, 26, 2, 3, 396, 0),
    (150, 19, 25, 2, 3, 438, 0)
]

# Convert the data into a DataFrame
df = pd.DataFrame(data, columns=['Time', 'Series1', 'Series2', 'Column3', 'Column4', 'Column5', 'Column6'])

# Calculate the average of Series1 and Series2
average_series1 = df['Series1'].mean()
average_series2 = df['Series2'].mean()

print(f'Average of Series1: {average_series1}')
print(f'Average of Series2: {average_series2}')
