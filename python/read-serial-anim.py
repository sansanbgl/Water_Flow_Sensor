import serial
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from collections import deque
import time

# Function to update the plot with new data
def update_plot(i):
    current_time = time.time()  # Get the current time in seconds since the epoch
    line = ser.readline().decode("utf-8").strip()  # Read a line of data and decode it
    print("Received Data:", line)  # Print the data to the terminal

    if line:
        data = line.split(";")  # Split the line into individual values
        if len(data) == 7:  # Ensure there are 7 values (as per your Arduino code)
            millis, pulseCount, pulseCount_2, flowRate, flowRate_2, totalMilliLitres, totalLitres = map(float, data)
            data_points.append((current_time, pulseCount, pulseCount_2))  # Add data to the list

            # Prune data older than 1 minute
            one_minute_ago = current_time - 60000  # 60000 milliseconds in 1 minute
            while data_points and data_points[0][0] < one_minute_ago:
                data_points.popleft()

            # Update the plot
            time_data, pulse_data, pulse_data_2 = zip(*data_points)
            ax.clear()
            ax.plot(time_data, pulse_data, label='PulseCount')
            ax.plot(time_data, pulse_data_2, label='PulseCount2')
            ax.set_xlabel("Time (ms)")
            ax.set_ylabel("Pulse Counts")
            ax.set_title("Arduino Data Plot")
            ax.legend()

arduino_port = "COM3"
baud = 9600
samples = 200
print_labels = False

ser = serial.Serial(arduino_port, baud)
print("Connected to Arduino Port:" + arduino_port)

data_points = deque(maxlen=1000)  # Use deque to store data with a maximum length

# Create a Matplotlib figure
fig, ax = plt.subplots(figsize=(6, 4), dpi=100)
ani = FuncAnimation(fig, update_plot, frames=None, interval=1000)  # Update plot every 1000ms (1 second)

plt.show()
