# virtualenv venv
# pip install requests
# source venv/bin/activate

import requests

BASE_URL = 'http://api.wunderground.com/api/ecd1896816b98469'

def get_api_url(data_feature, state, city):
    city = city.replace(" ", "_")
    return "{}/{}/q/{}/{}.json".format(BASE_URL, data_feature, state, city)
    
# test API urls
# print get_api_url("conditions", "CA", "San Francisco")
# print get_api_url("conditions", "NY", "New York")

def weather():
    # TODO: check if state entered matches actual state data returned in JSON
    print "Enter state abbreviation (e.g., CA):", 
    state = raw_input()
    print "Enter city (e.g., San Francisco):", 
    city = raw_input()

    try:
        r = requests.get(get_api_url("conditions", state, city))
        j = r.json()
        temperature = j['current_observation']['temperature_string']
        print get_api_url("conditions", state, city)
        print temperature
    except KeyError, e:
        print "Please enter a valid city and/or state."

def forecast():
    print "Enter state abbreviation (e.g., CA):", 
    state = raw_input()
    print "Enter city (e.g., San Francisco):", 
    city = raw_input()

    r = requests.get(get_api_url("forecast", state, city))
    j = r.json()
    days = j['forecast']['txt_forecast']['forecastday']
    for day in days:
        print day['title'], day['fcttext']

def main():
    weather()
    # forecast()

if __name__=="__main__":
    main() 