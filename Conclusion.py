RAW_FILE  = "dataFile.txt"
CONVERTED_FILE = "convertedFile.csv"
PROCESSED_FILE = "processedFile.txt"



# Get data


from Library import get_latest_entry
latest_entry = get_latest_entry(CONVERTED_FILE) # Climate data

# rain = latest_entry["PRECTOTCORR"]
# humidity = latest_entry["RH2M"]
# tmin = latest_entry["T2M_MIN"]
# wind = latest_entry["WS2M"]
#print(latest_entry)


# Predicted data
file = open(PROCESSED_FILE, "r")
data = file.read()
file.close()
#print(data)
# data is (0.5533235505761585, array([35.22887395]))



# Score
import re


# -------- Extract values from existing variables --------

rain = latest_entry["PRECTOTCORR"]
humidity = latest_entry["RH2M"]
wind = latest_entry["WS2M"]

# extract numbers from predicted output text
numbers = re.findall(r"\d+\.\d+", data)

error = float(numbers[0])
predicted_temp = float(numbers[1])

print("Predicted Max Temperature:", predicted_temp)
print("Model Error:", error)


# -------- Heatwave Detection --------

if predicted_temp >= 45:
    heat_alert = "SEVERE HEATWAVE"
elif predicted_temp >= 40:
    heat_alert = "HEATWAVE WARNING"
elif predicted_temp >= 35:
    heat_alert = "HIGH HEAT ALERT"
else:
    heat_alert = "NORMAL"

print("Heatwave Status:", heat_alert)


# -------- Climate Stress Index --------

temp_score = (predicted_temp / 45) * 100
humidity_score = humidity
wind_score = (1 - (wind / 10)) * 100
rain_score = (1 - (rain / 50)) * 100

risk_score = (
    0.4 * temp_score +
    0.3 * humidity_score +
    0.2 * wind_score +
    0.1 * rain_score
)

print("Climate Stress Index:", round(risk_score,2))


# -------- Risk Level --------

if risk_score < 30:
    level = "LOW"
elif risk_score < 60:
    level = "MODERATE"
elif risk_score < 80:
    level = "HIGH"
else:
    level = "SEVERE"

print("Risk Level:", level)


# -------- Suggestions --------

print("\nRecommended Actions:")

if level == "LOW":
    print("- Normal school operations")
    print("- Encourage hydration")

elif level == "MODERATE":
    print("- Monitor students for heat discomfort")
    print("- Ensure drinking water availability")
    print("- Reduce outdoor activities")

elif level == "HIGH":
    print("- Limit outdoor classes and sports")
    print("- Provide shaded rest areas")
    print("- Increase water breaks")

else:
    print("- Issue heat alert for school")
    print("- Suspend outdoor activities")
    print("- Prepare health room for heat stress cases")
    print("- Inform local health authorities")