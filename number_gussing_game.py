import random
print("Welcome to my GAME")

user_range= input("Type a limit :")

if user_range.isdigit():
    user_range = int(user_range)

    if user_range <= 0:
        print("Enter the number greater than 0 next time!!!")
        quit()
            
else:
    print("please enter a number next time !!")
    quit()

storage = random.randint(0,user_range)


guess = 0

while True:
    guess += 1
    ans = (input("Enter the number: "))
    if ans.isdigit():
        ans = int(ans)
    else:
        print("plz enter a number next time")
        continue

    if ans == storage:
        print("Right ansewer!!")
        break
    elif ans > storage:
        print("Answer is smaller than the ",ans)
    else:
        print("Answer is greater than the ", ans)

print("You guessed in ",guess,"time")
    
    



   
    

