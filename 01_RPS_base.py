import random

# functions go here
def check_rounds():

    while True:
        response = input("how many rounds: ")
        round_error = "please type either <enter> or an integer that is more than 0"
        # if infinite mode is not chosen, chech response
        # is an integer that is more than 0 
        if response != "":
            try:
                response = int(response)
                # if respons is too low, go back to start of loop
                if response < 1:
                    print(round_error)
                    continue
            # if response is not an integer, go back to
            # start of loop
            except ValueError:
                print(round_error)
                continue

        return response

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



# main routine goes here


# lists of valid responses
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]


# ask user if they have played before.
# if "yes", show instructions


# ask user for # of rounds then loop...
rounds_played = 0
mode = "regular"
choose_instruction = "please choose rock (r), paper (p), or scissors (s)"

# ask user for # of rounds, <enter> for infinite mode 
rounds = check_rounds()
if rounds == "":
    mode = "infinite"
    rounds = 10

end_game = "no"
while end_game == "no":

    #rounds heading
    print()
    if mode == "infinite":
        heading = "continuous mode: round {}".format(rounds_played + 1)
        
    
    else:
        heading = "round {} of {}".format(rounds_played + 1, rounds)
        
    print(heading)
    choose_instruction = "choose rock / paper / scissors (r/p/s)"
    choose_error = "please choose rock / paper / scissors (or xxx to quit)"

    # ask user for choice and check its valid
    choose = choice_checker(choose_instruction, rps_list, choose_error)

    # end game if exit code is typed 
    if choose == "xxx" or rounds_played + 1 == rounds:
        break

    
    # rest of loop / game
    print("you chose {}".format(choose))

    rounds_played += 1

    if mode == "infinite":
        rounds += 1

print()
print("Thank you for playing")

# ask user if they want to see their game history
# if 'yes' show game history