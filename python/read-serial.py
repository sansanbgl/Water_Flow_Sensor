import serial

arduino_port = "COM4"
baud = 9600
fileName = "water-leakage-data-logger.csv"
samples = 200
print_labels = False

ser = serial.Serial(arduino_port, baud)
print("Connected to Arduino Port:" + arduino_port)
file = open(fileName, "a")
print("File created successfully!")

line = 0

while line <= samples:
    if print_labels:
        if line==0:
            print("Printing Column Headers")
        else:
            print("Line " + str(line) + ":writing...")
    getData=str(ser.readline())
    data=getData[2:][:-5]
    print(data)

    file = open(fileName, "a")

    file.write(getData + "\n")
    line = line+1

print("Data collection complete!")
file.close() 