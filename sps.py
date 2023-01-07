import random

print("   \n   Welcome to the GAME")


user_wins = 0
computer_wins = 0
options = ["papper","stone","scissors"]


while True:

    user_input = input("\nqType Rock/Papper/Scissors or Q to quit : ").lower()



    if user_input == "q":
    
        

        break

        

         
    elif user_input  not in options:
         print("Please enter within the provided options")
         continue
        


    random_number = random.randint(0,2)

    computer_pick = options[random_number]

    print("Computer picked", computer_pick + ".")


    if user_input == "rock" and computer_pick == "scissors":
        print("You Won!!!")
        user_wins = user_wins +1



    elif user_input == "papper" and computer_pick =="stone":
        print("You Won!!!")
        user_wins = user_wins +1



    elif user_input == "scissors" and computer_pick == "papper":
        print("You Won!!!")
        user_wins = user_wins +1 

    elif user_input == computer_pick:
        print("Draw!!")   

    else:
        print("oops! You lost.")  
        

print("\nyou won",user_wins,"times.")

print("\nthe computer won",computer_wins,"times.")

print("\nHAVE A GOOD DAY   :)")

   
