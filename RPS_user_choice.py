from tkinter.messagebox import QUESTION


def choice_checker(question):
    
    error = "please choose from rock / paper / scissors (or xxx to quit)"

valid = False
while not valid:

    #ask user for choice (and put choice in lower case)
    response = input(question).lower()

    if response == "r" or response == "rock":
        return response
    elif response == "p" or response == "paper":
        return response
    elif response == "s" or response == "scissors":
        return response