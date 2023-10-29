import csv

def get_expected_range(data_file, window_size=10):
    with open(data_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        
        next(csv_reader)  # Skip the header if there is one
        
        non_zero_values = []
        for row in csv_reader:
            current_value = int(row[2])
            if current_value > 0:
                non_zero_values.append(current_value)
            
            if len(non_zero_values) > window_size:
                non_zero_values.pop(0)
        
        if len(non_zero_values) < window_size:
            raise ValueError("Not enough non-zero data points to calculate the expected range.")
        
        expected_min = min(non_zero_values)
        expected_max = max(non_zero_values)
        
        return expected_min, expected_max

def detect_irregularities(data_file, expected_range, deviation_threshold=5):
    with open(data_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        
        next(csv_reader)  # Skip the header if there is one
        
        for i, row in enumerate(csv_reader, start=1):
            current_value = int(row[2])
            
            if current_value > 0:
                if current_value < expected_range[0] or current_value > expected_range[1]:
                    deviation = abs(current_value - sum(expected_range) / 2)
                    if deviation > deviation_threshold:
                        print(f"Irregular value detected at line {i}. Deviation from expected range: {deviation}")

data_file = 'data-s-4.csv'  # Replace with your CSV file

expected_range = get_expected_range(data_file)
detect_irregularities(data_file, expected_range)
