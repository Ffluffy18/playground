file_path = '/home/floof/10-24-2026_weather.csv'  # Replace with your actual file path

data_list = [] # Initialize an empty list to store the data

with open(file_path, 'r') as file:     # Open and read the file
    for line in file:
        # Strip whitespace and split by comma
        a, b, c, d, e, f, g, h, i, j = line.strip().split(',')  
        # or int(x), int(y) if your data is in integer format
        data_list.append((float(x), float(y)))       
print("Data successfully read from file.")
print("Data List:", data_list)
