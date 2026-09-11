RAW_FILE  = "dataFile.txt"
CONVERTED_FILE = "convertedFile.csv"
PROCESSED_FILE = "processedFile.txt"


# Get prediction
from Library import get_predicted_data
data = get_predicted_data(CONVERTED_FILE)
file = open(PROCESSED_FILE, "w")
file.write(str(data))
file.close()
