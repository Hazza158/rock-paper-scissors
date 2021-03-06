# Version 2 - error message included when calling function

# functions go here
def choice_checker(question, error):

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

        #check for exit code
        elif response == "xxx":
            return response
        else:
            print(error)


#main routine goes here



#loop for testing purposes
user_choice = ""
while user_choice != "xxx":

    #ask user for and check its valid
    user_choice = choice_checker("choose rock / paper / scissors (r/p/s): ", "please choose from rock / paper / scissors (or xxx to quit)")

    #print out choice for comparison purposes
    print("You chose {}".format(user_choice))