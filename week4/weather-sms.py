# virtualenv venv - creates new virtual environment
# pip install requests - install package on venv
# source venv/bin/activate - activate venv

import requests
import random

# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

account_sid = "AC744ef3fb7bcb34349a25f350886dcdd8"
auth_token = "16547d6225710fe54a68bd85f763b393"
client = TwilioRestClient(account_sid, auth_token)

BASE_URL = 'http://api.wunderground.com/api/ecd1896816b98469'

source_places = [ ('New York', 'NY'), ('San Francisco', 'CA'), ('Seattle', 'WA'), ('Houston', 'TX') ]
forecast_data = []

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
        # return day['title'], day['fcttext']
        day_forecast = day['title'], day['fcttext']
        forecast_data.append(day_forecast)
    return forecast_data

def get_random_place_name():
    rando_place = random.choice(source_places)
    return rando_place

def text_this(number, message, test=False):
    try:
        if test:
            print "This would have sent a SMS to {}. Message: {}".format(number, message)
            return True
        else:
            text_message = client.messages.create(to=number, from_="+14157636692", body=message)
            return True
    except:
        return False

def main():
    # weather()
    # forecast()
    (city, state) = get_random_place_name()
    the_weather = weather(city, state)
    
    the_forecast_day = forecast(city, state)[2][0]
    the_forecast = forecast(city, state)[2][1]
    
    phone_number = "+14083986692"
    # message = "The weather in {} is {}".format(city, the_weather)
    message = "The forecast for tomorrow ({}) in {} is: {}".format(the_forecast_day, city, the_forecast)
    test_mode = True
    
    text_this(phone_number, message, test_mode)

if __name__=="__main__":
    main() 
