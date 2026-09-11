INPUT_FILE  = "dataFile.txt"
OUTPUT_FILE = "convertedFile.csv"

# clear
file = open(INPUT_FILE, "w")
file.write("")
file.close()

# Get data from API
from Library import get_temp_data

file = open(INPUT_FILE, "a")

days = 100 # 14 - 4 = 10
for i in range(days, 3, -1):

    data = str(get_temp_data(i))
    file.write(data)
    
file.close()


# Convert to CSV format
from Library import convert_data

convert_data(INPUT_FILE, OUTPUT_FILE)