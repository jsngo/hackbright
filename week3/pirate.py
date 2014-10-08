import random 

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

drink_adjs = [
    "Swashbuckling",
    "Barbaric",
    "Fearsome",
    "Nautical",
    "Vile",
    "Cutthroat"
]

drink_nouns = [
    "Galleon",
    "Heist",
    "Ruffian",
    "Conquest",
    "Plank",
    "Marauder"
]

# Write a function to ask what style of drink a customer likes:
# - The function should ask each of the questions in the questions dictionary, and gather the responses in a new dictionary.
# - The new dictionary should contain the type of ingredient (for example "salty", or "sweet"), mapped to a Boolean (True or False) value.
# - If the customer answers y or yes to the question then the value should be True, otherwise the value should be False.
# - The function should return the new dictionary.

responses = {}

def ask_questions():
    for flavor, question in questions.items():
        print question, "(y/yes or n/no)",
        answer = raw_input()
        if answer == "yes" or answer =="y":
            responses[flavor] = True
        else:
            responses[flavor] = False
    return responses

# Write a function to construct a drink:
# - The function should take the preferences dictionary created in the first function as a parameter.
# - Inside the function you should create an empty list to represent the drink.
# - For each type of ingredient which the customer said they liked you should append a corresponding ingredient from the ingredients dictionary to the drink.
# - Finally the function should return the drink.

def make_drinks(responses):
    drink = []
    for flavor, tf in responses.items():
        if tf == True:
            random_ingredient = random.choice(ingredients[flavor])
            drink.append(random_ingredient)
    return drink

def name_drinks():
    drink_adj = random.choice(drink_adjs)
    drink_noun = random.choice(drink_nouns)
    drink_name = drink_adj + " " + drink_noun
    return drink_name

# Provide a main function
def main():
    print "Would you like a drink? (y/yes or n/no)",
    drink_yn = raw_input()
    while drink_yn == "y" or drink_yn == "yes":
        ask_questions()
        print "\nYour drink is named:",
        print name_drinks()
        print "Your drink has the following ingredients:",
        print make_drinks(responses)
        print "\n Would you like another drink? (y/yes or n/no)",
        drink_yn = raw_input()
    print "okay bai"

if __name__=="__main__":
    main() 

