
import datetime
import requests
import pyttsx3

engine =pyttsx3.init()



def get_time():
    # Get current time
    now = datetime.datetime.now()
    # Determine time of day
    if now.hour < 12:
        engine.say("Good morning Aswin")
    elif now.hour < 18:
        engine.say("Good afternoon Aswin")
    elif now.hour < 22:
        engine.say("Good evening")
    else:
        engine.say("Good night")





def get_weather():
     # Get weather data
    api_key = "8eba66a28b7d4a77b42143901232602"
    city_name = 'Dundee'
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city_name}&aqi=no'
    response = requests.get(url)
    data = response.json()

    # Parse weather data
    description = data['current']['condition']['text']
    temperature = data['current']['temp_c']

    # Speak weather information
    engine.say(f"The weather in {city_name} is {description} with a temperature of {temperature} degrees Celsius.")




