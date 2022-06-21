from plyer import notification
from datetime import datetime
import requests
import time
def weather_notification():
    #Getting weather data using openweatherapi
    api_key = "a833da2ea0ffccd99997fa69e7cf0f81"
    url = "https://api.openweathermap.org/data/2.5/weather?q=thiruvananthapuram&appid=a833da2ea0ffccd99997fa69e7cf0f81"
    weather_data = requests.get(url)
    weather_condition = weather_data.json()['weather'][0]['main']
    description = weather_data.json()['weather'][0]['description']
    temp_kelvin = round(weather_data.json()['main']['temp'])
    temp_faren=round(1.8*(temp_kelvin-273) + 32)
    temp_min_kelv = round(weather_data.json()['main']['temp_min'])
    temp_min_faren=round(1.8*(temp_min_kelv-273) + 32)
    temp_max_kelv = round(weather_data.json()['main']['temp_max'])
    temp_max_faren=round(1.8*(temp_max_kelv-273) + 32)
    humidity = weather_data.json()['main']['humidity']

    #desktop notification using plyer.notifications

    notification.notify(title='Weather Updates For Trivandrum\n',message=f'The Weather Is :{weather_condition}\nTemperature : {temp_faren}°F\nHumidity : {humidity} %',app_name='Weather App',app_icon="weather_few_clouds.ico",timeout=30)
    time.sleep(60*60*4)

weather_notification()