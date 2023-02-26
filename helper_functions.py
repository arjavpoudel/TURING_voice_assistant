
import datetime
import requests
import pyttsx3

engine =pyttsx3.init()



def get_time():
    # Get current time
    now = datetime.datetime.now()
    if now.hour < 12:
        engine.say("Good morning {name_here}")
    elif now.hour < 18:
        engine.say("Good afternoon {name_here}")
    elif now.hour < 22:
        engine.say("Good evening {name_here}")
    else:
        engine.say("Good night {name_here}")




#Use a site like WeatherAPI.com for free api key
def get_weather():
     # Get weather data
    api_key = "your-api-key-here"
    city_name = '{your-city-here}'
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city_name}&aqi=no'
    response = requests.get(url)
    data = response.json()

    # Parse weather data
    description = data['current']['condition']['text']
    temperature = data['current']['temp_c']

    # Speak weather information
    engine.say(f"The weather in {city_name} is {description} with a temperature of {temperature} degrees Celsius.")




