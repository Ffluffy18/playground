import matplotlib.pyplot as plt
file_path = "C:/Users/black/Desktop/python_learning/10-24-2026_weather.csv"

# set empty lists so we can add objects to them
time = []
temperature = []
clean_temperature = []

with open(file_path, "r") as file: # import our csv file and read it
    # loop: cleans up csv file, by adding only time and temperature into our lists
     for line in file:
        clean_line = line.strip().split(",")
        time.append(clean_line[0])
        temperature.append(clean_line[1])
      
# remove the category name from the list   
time.remove("Time")
temperature.remove("Temperature")

# reverse the lists so that they start at the beginning of the day 
time = time[::-1]
temperature = temperature[::-1]


# change the temperatures to integers and remove the "F"
# this will allow the temperatures in the y-axis to be plotted in order
for temp in temperature:
    clean_temperature.append(int(temp[0:2]))

# this makes the bar graph
plt.bar(time, clean_temperature)
plt.title("El Paso temperature for 10-24-2026")
plt.ylabel("Temperature (F)")
plt.xlabel("Time")
plt.show()

load_data()
clean_data()
plot_graph()
