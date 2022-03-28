def check_rounds():

    while True:
        response = input("how many rounds: ")

        round_error = "please type either <enter> or an integer that is moer than 0"

        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue
            
            except ValueError:
                print(round_error)
                continue

        return response


# main routine goes here

rounds_played = 0
choose_instruction = "please choose rock (r), paper (p), or scissors (s)"

# ask user for # of rounds, <enter> for infinite mode 
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    #rounds heading
    print()
    if rounds == "":
        heading = "continuous mode: round {}".format(rounds_played + 1)
        choose = input("{} or 'xxx' to end: ".format(choose_instruction))
        
    
    else:
        heading = "round {} of {}".format(rounds_played + 1, rounds)
        
    print(heading)
    choose = input ("{} or 'xxx' to end: ".format(choose_instruction))

    # end game if exit code is typed 
    if choose == "xxx":
        break

    

    # rest of loop / game
    print("you chose {}".format(choose))

    rounds_played += 1

print("thank you for playing")