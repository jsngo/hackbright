# pip install requests
# pip install requests-oauthlib

# API secrets. NEVER share these with anyone!
# jennifartngo account
CLIENT_KEY = "BE43lFc6pyB5auNHYyMVasTLT"
CLIENT_SECRET = "reIcRqqpEjXrkyrFtGDED2kcPCa8GQjne7bRfXqLGc8dwyO7Dj"

# bizarrojennifer account
# CLIENT_KEY = "BpSMHnzHVntlFFdfbQmSwJK1X"
# CLIENT_SECRET = "iEruKOtCHCXz5FesDJMGN5S16gPv7JGwko4t6Mp3EZ403rk5gR"


API_URL = "https://api.twitter.com"
REQUEST_TOKEN_URL = API_URL + "/oauth/request_token"
AUTHORIZE_URL = API_URL + "/oauth/authorize?oauth_token={request_token}"
ACCESS_TOKEN_URL = API_URL + "/oauth/access_token"
TIMELINE_URL = API_URL + "/1.1/statuses/home_timeline.json"
USER_TIMELINE_URL = API_URL + "/1.1/statuses/user_timeline.json"
SEARCH_URL = API_URL + "/1.1/search/tweets.json"
TWEET_URL = API_URL + "/1.1/statuses/update.json"

import urlparse
import json
import requests
from requests_oauthlib import OAuth1
from pprint import pprint


def get_request_token():
    """ Get a token allowing us to request user authorization """
    oauth = OAuth1(CLIENT_KEY, client_secret=CLIENT_SECRET)
    response = requests.post(REQUEST_TOKEN_URL,
                             auth=oauth)
    credentials = urlparse.parse_qs(response.content)

    request_token = credentials.get("oauth_token")[0]
    request_secret = credentials.get("oauth_token_secret")[0]
    return request_token, request_secret


def get_access_token(request_token, request_secret, verifier):
    """"
    Get a token which will allow us to make requests to the API
    """
    oauth = OAuth1(CLIENT_KEY,
                   client_secret=CLIENT_SECRET,
                   resource_owner_key=request_token,
                   resource_owner_secret=request_secret,
                   verifier=verifier)

    response = requests.post(ACCESS_TOKEN_URL, auth=oauth)
    credentials = urlparse.parse_qs(response.content)
    access_token = credentials.get('oauth_token')[0]
    access_secret = credentials.get('oauth_token_secret')[0]
    return access_token, access_secret


def get_user_authorization(request_token):
    """
    Redirect the user to authorize the client, and get them to give us the
    verification code.
    """
    authorize_url = AUTHORIZE_URL
    authorize_url = authorize_url.format(request_token=request_token)
    print 'Please go here and authorize: ' + authorize_url
    return raw_input('Please input the verifier: ')


def store_credentials(access_token, access_secret):
    """ Save our access credentials in a json file """
    with open("access.json", "w") as f:
        json.dump({"access_token": access_token,
                   "access_secret": access_secret}, f)


def get_stored_credentials():
    """ Try to retrieve stored access credentials from a json file """
    with open("access.json", "r") as f:
        credentials = json.load(f)
        return credentials["access_token"], credentials["access_secret"]


def authorize():
    """ A complete OAuth authentication flow """
    try:
        access_token, access_secret = get_stored_credentials()
    except IOError:
        request_token, request_secret = get_request_token()
        verifier = get_user_authorization(request_token)
        access_token, access_secret = get_access_token(request_token,
                                                       request_secret,
                                                       verifier)
        store_credentials(access_token, access_secret)

    oauth = OAuth1(CLIENT_KEY,
                   client_secret=CLIENT_SECRET,
                   resource_owner_key=access_token,
                   resource_owner_secret=access_secret)
    return oauth

# Print the author and text of the recent tweets on your timeline
def tweet_author_text():
    auth = authorize()
    response = requests.get(TIMELINE_URL, auth=auth)
    # print json.dumps(response.json(), indent=4, sort_keys=True)
    j = response.json()
    # j returns an array, so need to loop through its contents
    for tweet in j:
        author = tweet["user"]["screen_name"]
        message = tweet["text"]
        print author + " says: " + message

# Pick a user and print out their 10 most recent tweets
def user_ten_tweets(screen_name):
    auth = authorize()
    user_api_url = "{}?screen_name={}&count=10".format(USER_TIMELINE_URL, screen_name)
    # print user_api_url
    response = requests.get(user_api_url, auth=auth)
    j = response.json()
    # print json.dumps(response.json(), indent=4)
    for tweet in j:
        message = tweet["text"]
        print message

# Use the Search API to get all recent tweets mentioning Hackbright
def search_mentions(search_term):
    auth = authorize()
    search_api_url = "{}?q={}&result_type=recent".format(SEARCH_URL, search_term)
    response = requests.get(search_api_url, auth=auth)
    # print json.dumps(response.json(), indent=4, sort_keys=True)
    j = response.json()
    for tweet in j["statuses"]:
        message = tweet["text"]
        print message

# INCOMPLETE
def make_tweet(status_message, auth):
    data = { 'status': status_message }
    response = requests.post(TWEET_URL, data=data, auth=auth)
    print response

def main():
    """ Main function """
    # tweet_author_text()
    # user_ten_tweets("jennyholzermom")
    # search_mentions("hackbright")
    
    auth = authorize()
    make_tweet("tweet tweet", auth)


if __name__=="__main__":
    main()