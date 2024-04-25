## FUNCTIONS ACTIVITY FOR PRACTICE ##

# Author: Adson Mettler do Nascimento

def display_regular():
    print("\nI can do all things through Christ")

display_regular()

def display_uppercase():
    string = "I can do all things through Christ"
    print(string.upper())

display_uppercase()

def display_lowercase():
    string = "I can do all things through Christ\n"
    print(string.lower())

display_lowercase()


## USING FUNCTION WITH USER INPUT ##

def display_regular(message):
    print(message)

def display_upper(message):
    new_message = message.upper()
    print(new_message)

def display_lower(message):
    new_message = message.lower()
    print(new_message)

user_message = input("What is your message? ")

display_regular(user_message)
display_upper(user_message)
display_lower(user_message)
