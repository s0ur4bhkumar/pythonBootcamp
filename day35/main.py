import requests

API_KEY = "1daf963aadabbdc117c007e05af61e22"
LAT = 51.759050
LON = 19.458600
weather_params = {"lat": LAT, "lon": LON, "appid": API_KEY, "cnt": 4, "units": "Metric"}
URL = "https://api.openweathermap.org/data/2.5/forecast"

response = requests.get(URL, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_codes = [code["weather"][0]["id"] for code in weather_data["list"]]
for i in weather_codes:
    if i < 700:
        print('take umbrella with you')
