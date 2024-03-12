print("Welcome to my GAME !!!!")

question = input("Do you want to play this game? ").lower()
if question != "yes":
    quit()

score = 0

ans = input("Who is the father of the computer? ").lower()
if ans == "charles babbage":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

ans = input("Who is known as the father of the science? ").lower()
if ans == "galileo galilei":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

ans = input("What is the full form of GPU? ").lower()
if ans == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

ans = input("Who is the first president of Nepal? ").lower()
if ans == "ram baran yadav":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("Your total score is " + str(score))
print("You achieve " + str((score/4) * 100 ) + "%")
