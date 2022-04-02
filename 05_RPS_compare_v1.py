#RPS component 3 - compare user choice and computer choice

rps_list = ["rock", "paper", "scissors"]
comp_index = 0
for item in rps_list:
    user_index= 0 
    for item in rps_list:
        user_choice = rps_list[user_index]
        comp_choice = rps_list[comp_index]
        user_index += 1

        # compare options...
        if comp_choice == user_choice:
           result = "its a tie"
        
        elif comp_choice == "paper" and user_choice == "rock":
            result = "you lose"
        
        elif comp_choice == "scissors" and user_choice == "paper":
            result = "you lose"

        elif comp_choice == "rock" and user_choice == "scissors":
            result = "you lose"
        
        else:
            result = "you win"
        
        print("you chose {}, the computer chose {}. \nResult: {}".format(user_choice, comp_choice, result))

    comp_index += 1
    print()
    
        
        

    