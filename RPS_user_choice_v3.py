# Version 2 - error message included when calling function

# functions go here
from multiprocessing import RLock


def choice_checker(question, valid_list, error):

    valid = False
    while not valid:

        #ask user for choice (and put choice in lower case)
        response = input(question).lower()

        # iterates through list and if response is an item
        # in the list (or the first letter of an item), 
        # the full name is returned

        for item in valid_list:
            if response == item [0] or response == item:
                return item
        
        #output error if item nt in list
        print(error)
        print()


#main routine goes here


# lists for checking responses
rps_list = ["rock", "paper", "scissors", "xxx"]

#loop for testing purposes
user_choice = ""
while user_choice != "xxx":

    #ask user for and check its valid
    user_choice = choice_checker("choose rock / paper / scissors (r/p/s): ", rps_list, "please choose from rock / paper / scissors (or xxx to quit)")

    #print out choice for comparison purposes
    print("You chose {}".format(user_choice))