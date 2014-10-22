# virtualenv venv
# pip install requests
# source venv/bin/activate

import requests
import random

BASE_URL = 'http://api.wunderground.com/api/ecd1896816b98469'

source_places = [ ('New York', 'NY'), ('San Francisco', 'CA'), ('Seattle', 'WA'), ('Houston', 'TX') ]

def get_api_url(data_feature, state, city):
    city = city.replace(" ", "_")
    return "{}/{}/q/{}/{}.json".format(BASE_URL, data_feature, state, city)
    
def weather(city, state):
    # TODO: check if state entered matches actual state data returned in JSON
    r = requests.get(get_api_url("conditions", state, city))
    j = r.json()
    temperature = j['current_observation']['temperature_string']
    return temperature

def forecast(city, state):
    r = requests.get(get_api_url("forecast", state, city))
    j = r.json()
    days = j['forecast']['txt_forecast']['forecastday']
    for day in days:
        return day['title'], day['fcttext']

def get_random_place_name():
    rando_place = random.choice(source_places)
    return rando_place

def main():
    # weather()
    # forecast()
    (city, state) = get_random_place_name()
    the_weather = weather(city, state)
    the_forecast = forecast(city, state)
    print "The weather in {} is {}".format(city, the_weather)
    print "The forecast for {} is {}".format(city, the_forecast)

if __name__=="__main__":
    main() 