import requests
import datetime


def get_coordinates(city_name):
    
    GEO_API_KEY = "0a230ea73e14d47b229f3cb3754932e2"

    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={GEO_API_KEY}"

    response = requests.get(url)

    if response.status_code == 200 and response.json():
        return response.json()[0]["lat"], response.json()[0]["lon"]
    raise Exception("Could not find coordinates.")

def get_nasa_weather(lat, lon, date_str):


    # NASA POWER Endpoint for daily data
    base_url = "https://power.larc.nasa.gov/api/temporal/daily/point"
    
    params = {
        "parameters": "T2M_MAX,T2M_MIN,RH2M,WS2M,PRECTOTCORR",
        "community": "AG",
        "longitude": lon,
        "latitude": lat,
        "start": date_str,
        "end": date_str,
        "format": "JSON"
    }
    
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"NASA API Error: {response.status_code}")



def get_temp_data(n):
    city = "Raipur"
    
    try:
        # 1. Get Lat/Lon
        lat, lon = get_coordinates(city)
        
        # 2. Set Date (NASA data is usually 3 days behind)

        target_date = (datetime.date.today() - datetime.timedelta(days=n)).strftime("%Y%m%d")
        
        # 3. Get Data
        data = get_nasa_weather(lat, lon, target_date)
        
        # 4. Extract values from the nested JSON
        # NASA returns data inside properties -> parameter -> date
        properties = data['properties']['parameter']

        return properties
        
        # print(f"--- NASA POWER Weather Report for {city} ({target_date}) ---")
        # print(f"Max Temp: {properties['T2M_MAX'][target_date]}°C")
        # print(f"Min Temp: {properties['T2M_MIN'][target_date]}°C")
        # print(f"Humidity: {properties['RH2M'][target_date]}%")
        # print(f"Wind Speed: {properties['WS2M'][target_date]} m/s")
        # print(f"Precipitation: {properties['PRECTOTCORR'][target_date]} mm")

    except Exception as e:
        print(f"Error: {e}")