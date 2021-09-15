import requests, json

api_key = "f1e4695138a9aa78063b3515d1b84957"
city_name = input("Enter the city name: ")
requests_base_url = (f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}")
response = requests.get(requests_base_url)
x = response.json()
if x["cod"] != "404":
    y = x["main"]
    current_temperature = y["temp"]
    current_pressure = y["pressure"]
    current_humidity = y["humidity"]
    z = x["weather"]
    weather_description = z[0]["description"]
    print(f"Temperature (in kelvin): {str(current_temperature)} \n Atmospheric presure (in hPa): {str(current_pressure)} \n Humidity percentage: {str(current_humidity)} \n Description: {str(weather_description)}")
else:  
    print("City not found")