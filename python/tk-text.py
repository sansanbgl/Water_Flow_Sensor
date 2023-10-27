import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
import time

# Function to generate random data
random.seed()

def generate_data():
    return random.random() * 10

# Function to update the plot with new data
def update_plot():
    data_point = generate_data()
    data_points.append(data_point)

    # if len(data_points) > samples:
    #     data_points.pop(0)

    ax.clear()
    ax.plot(range(len(data_points)), data_points)
    ax.set_xlabel("Sample")
    ax.set_ylabel("Value")
    ax.set_title("Random Data Plot")
    canvas.draw()

samples = 200

data_points = []

root = tk.Tk()
root.title("Random Data Plot")

# Create a Matplotlib figure
fig = Figure(figsize=(6, 4), dpi=100)
ax = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Schedule the initial plot update and set an interval for subsequent updates
root.after(1000, update_plot)  # Start updating the plot every 1000ms (1 second)

def terminal_output():
    print("Plot Data:", data_points)
    root.after(1000, terminal_output)  # Print every 1000ms (1 second)

# Schedule terminal output
root.after(1000, terminal_output)

root.mainloop()
