import requests, json
from googletrans import Translator

translator = Translator()

api_key = "f1e4695138a9aa78063b3515d1b84957"
city_name = "Curitiba"#input("Enter the city name: ")
requests_base_url = (f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}")
response = requests.get(requests_base_url)
x = response.json()
if x["cod"] != "404":
    y = x["main"]
    current_temperature_kelvin = y["temp"]
    current_temperature = "{:.2f}".format(current_temperature_kelvin - 273.15) 
    current_pressure = y["pressure"]
    current_humidity = y["humidity"]
    z = x["weather"]
    weather_description_eng = z[0]["description"]
    weather_description = translator.translate(weather_description_eng, dest='es', src='en')
    print(f"La temperatura es de {str(current_temperature)}°C, presión Atmosferica de {str(current_pressure)} hPa, {str(current_humidity)}% de humedad, con {str(weather_description.text)}")
else:  
    print("City not found")