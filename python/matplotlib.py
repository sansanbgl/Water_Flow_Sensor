import serial
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Function to update the plot with new data
def update_plot():
    line = ser.readline().decode("utf-8").strip()  # Read a line of data and decode it
    if line:
        data = line.split(";")  # Split the line into individual values
        if len(data) == 7:  # Ensure there are 7 values (as per your Arduino code)
            millis, pulseCount, pulseCount_2, flowRate, flowRate_2, totalMilliLitres, totalLitres = map(float, data)
            data_points.append(flowRate)  # You can choose which value to plot

            if len(data_points) > samples:
                data_points.pop(0)

            ax.clear()
            ax.plot(data_points)
            ax.set_xlabel("Sample")
            ax.set_ylabel("Flow Rate")
            ax.set_title("Arduino Data Plot")
            canvas.draw()

arduino_port = "COM3"
baud = 9600
samples = 200
print_labels = False

ser = serial.Serial(arduino_port, baud)
print("Connected to Arduino Port:" + arduino_port)

data_points = []

root = tk.Tk()
root.title("Real-Time Arduino Data Plot")

# Create a Matplotlib figure
fig = Figure(figsize=(6, 4), dpi=100)
ax = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Schedule the initial plot update and set an interval for subsequent updates
root.after(1000, update_plot)  # Start updating the plot every 1000ms (1 second)

root.mainloop()
