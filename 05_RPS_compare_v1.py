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
        if comp_choice == "rock":
           result = "its a tie"
        print()
        if comp_choice == "paper":
            result = "you lose"
        print()
        if comp_choice == "scissors":
            result = "you win"
        
        
        
                
        

        print("you chose {}, the computer chose {}. \nResult: {}".format(user_choice, comp_choice, result))

    