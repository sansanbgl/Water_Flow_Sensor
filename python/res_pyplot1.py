import matplotlib.pyplot as plt

# Data
data = [
    (10, 0, 0),
    (20, 0, 0),
    (30, 0, 0),
    (40, 0, 0),
    (50, 0, 0),
    (60, 0, 0),
    (10, 0, 0),
    (20, 0, 0),
    (30, 0, 0),
    (40, 0, 0),
    (50, 8, 0),
    (60, 19, 10),
    (70, 17, 25),
    (80, 20, 27),
    (90, 19, 26),
    (100, 20, 25),
    (110, 19, 26),
    (120, 20, 25),
    (130, 19, 25),
    (140, 19, 26),
    (150, 19, 25),
    (160, 18, 26),
    (170, 19, 26),
    (180, 19, 25),
    (190, 18, 26),
    (200, 19, 26),
    (210, 18, 26),
    (220, 18, 19),
    (230, 17, 19),
    (240, 17, 15),
    (250, 17, 26),
    (260, 17, 25),
    (270, 17, 25),
    (280, 17, 25),
    (290, 17, 25),
    (300, 16, 24),
    (310, 17, 25),
    (320, 17, 25),
    (330, 17, 24),
]

# Separate the data into two series
time = [entry[0] for entry in data]
series1 = [entry[1] for entry in data]
series2 = [entry[2] for entry in data]

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
