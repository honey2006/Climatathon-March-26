RAW_FILE  = "dataFile.txt"
CONVERTED_FILE = "convertedFile.csv"
PROCESSED_FILE = "processedFile.txt"

# clear
file = open(RAW_FILE, "w")
file.write("")
file.close()

# Get data from API
from Library import get_temp_data

file = open(RAW_FILE, "a")

days = 100 # 14 - 4 = 10 ## input
for i in range(days, 3, -1):

    data = str(get_temp_data(i))
    file.write(data)
    
file.close()


# Convert to CSV format
from Library import convert_data

convert_data(RAW_FILE, CONVERTED_FILE)


# Get prediction
from Library import get_predicted_data
data = get_predicted_data(CONVERTED_FILE)
file = open(PROCESSED_FILE, "w")
file.write(str(data))
file.close()

# Conclusion