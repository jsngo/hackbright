import random

HUGBOT_NAME = "Henrietta"
boot_options = [True, False]
hugbot_actions = ["hug", "wave", "quit", "toot"]

action_map = {
	"dance": "robo-boogies",
	"toot": "toots like a horn",
	"hug": "hugs you closely",
	"wave": "waves creepily",
	"poison": "uses poisonous gases to poison their asses"
}

comeback_map = {
	"hello": "hi hi hi hi hiiii",
	"binary solo": "0000001, 00000011, 000000111, 0000001111",
	"when is it?": "the distant future, the year 2000"
}

def speak(message):
	print message

def get_name():
	return HUGBOT_NAME

def boot():
	speak("..beep boop..")
	bot_name = raw_input("What is the bot's name? ")
	if bot_name != "":
		speak("Hello my name is " + bot_name)
		return bot_name
	else:
		speak("y u no name me")
		return False

def hug():
	speak("**hug**")

def wave():
	speak("**wave**")

def toot():
	speak("**toot**")

# takes in a bot_name and verb and either:
# - prints out a more descriptive action if asked a certain string, pulled from a dictionary (action_map)
# - prints out a "comeback" sentence if asked a certain string, pulled from a dictionary (comeback_map)
# - prints out an "action" style message, adding 's' to the verb.
def perform_action(bot_name, verb):
	if verb in action_map:
		speak(bot_name + " " + action_map[verb])
	elif verb in comeback_map:
		speak(comeback_map[verb])
	else:
		speak(bot_name + " " + verb + "s")

def brain():
	booted_ok = boot()
	
	# when hugbot is given a name
	if booted_ok:
		# using a while loop, once Hugbot has responded to the user's request, just go round again and ask them for a new thing to do
		while True:
			action = raw_input("What should Hugbot do? ")
			
			# if action not in hugbot_actions:
			# 	speak("Hugbot doesn't have this feature")
			# if action == "hug":
			# 	hug()
			# if action == "wave":
			# 	wave()
			# if action == "toot":
			# 	toot()

			# exit the function (with return) if the user types in 'quit' as the answer to that question
			if action == "quit":
				return

			# perform the action!
			if action != "":
				perform_action(booted_ok, action)
			
			# for when the user doesn't enter anything
			else:
				print "COMMAND THE BOT"
	
	# when hugbot isn't given a name
	else:
		speak("System failure booooo")

brain()