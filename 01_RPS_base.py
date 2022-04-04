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
# initialise lost / drawn counters
rounds_lost = 0
rounds_drawn = 0

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
    user_choice_instruction = "user_choice rock / paper / scissors (r/p/s)"
    user_choice_error = "please user_choice rock / paper / scissors (or xxx to quit)"

    # ask user for choice and check its valid
    user_choice = choice_checker(user_choice_instruction, rps_list, user_choice_error)

    # get computer choice
    comp_choice = random.choice(rps_list[:-1])
    print("Comp Choice: ", comp_choice)

    # compare choices

    # end game if exit code is typed 
    if user_choice == "xxx" or rounds_played + 1 == rounds:
        break

    # compare options...
    if comp_choice == user_choice:
        result = "tie"
        rounds_drawn += 1

    elif comp_choice == "scissors" and user_choice == "rock":
        result = "won"
        
    elif comp_choice == "rock" and user_choice == "paper":
        result = "won"

    elif comp_choice == "paper" and user_choice == "scissors":
        result = "won"
        
    else:
        result = "lost"
        rounds_lost += 1
    
    if result == "tie":
        feedback = "its a tie"
    else:
        feedback = "{} vs {} - you {}".format(user_choice, comp_choice, result)

    print("you chose {}, the computer chose {}. \nResult: {}".format(user_choice, comp_choice, result))

    
    # rest of loop
    rounds_played += 1

    if mode == "infinite":
        rounds += 1

print()
print("Thank you for playing")

# ask user if they want to see their game history
# if 'yes' show game history

# show game statistics
# quick calculations (stats)
rounds_won = rounds_played - rounds_lost - rounds_drawn

# end of game statements
print()
print("\t**** End Game Summary ****")
print()
print("Won: {} \t|\t Lost: {} \t|\t Draw: {}".format(rounds_won, rounds_lost, rounds_drawn))
print()
print("Thanks for playing")