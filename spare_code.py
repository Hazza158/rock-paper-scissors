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