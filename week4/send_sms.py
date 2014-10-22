# virtualenv venv
# pip install requests
# source venv/bin/activate

# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient
 
# Find these values at https://twilio.com/user/account
account_sid = "AC744ef3fb7bcb34349a25f350886dcdd8"
auth_token = "16547d6225710fe54a68bd85f763b393"
client = TwilioRestClient(account_sid, auth_token)
 
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

# the body argument is optional if you are sending one or more MediaUrls
# message = client.messages.create(to="+14083986692", from_="+14157636692", body="Hello there!", media_url=['https://demo.twilio.com/owl.png', 'https://demo.twilio.com/logo.png'])

# text_this("+14083986692", "hello hello hi")
# text_this("+14085555555", "hello hello hi")

# Test = True
text_this("+14083986692", "hello hello hi", True)
# text_this("+14085555555", "hello hello hi", True)

# def main():

# if __name__=="__main__":
#     main() 