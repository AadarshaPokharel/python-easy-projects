import random

user_wins = 0
computer_wins = 0

user_choose = ["rock", "paper", "scissor"]

while True:
    user_input = input("Choose Rock/Paper/Scissor or Q for quitting the game: ").lower()

    if user_input == "q":
        print("Plz come next time!!")
        break

    if user_input not in  user_choose:
        print("You have entered the wrong choice!!")
        continue

    computer_choose = random.randint(0,2)
    meaning = user_choose[computer_choose]
    print("Computer choosed:",meaning)

    if user_input == "rock" and meaning == "scissor":
        print("You won!!")
        user_wins += 1
        

    elif user_input == "paper" and meaning == "rock":
        print("You won!!")
        user_wins += 1
        
    elif user_input == "scissor" and meaning == "paper":
        print("You won!!")
        user_wins += 1
        
    else:
        print("You lost!!")
        computer_wins += 1
        

print("You won",user_wins,"times.")
print("The computer won",computer_wins,"times.")    
    


print("Good bye!!!")


