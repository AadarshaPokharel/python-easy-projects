from cryptography.fernet import Fernet

master_pwd = input("Enter the master password? ")



def view():
    with open("password.txt","r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:",user,",", "Password:",passw)
            print("\n")

def add():
    pw1 = input("Account name :")
    pw2 = input("Password :")

    with open("password.txt","a") as f:
        f.write(pw1 + "|" + pw2 + "\n")
        
while True:

    pwd = input("Enter the (view/add/q) for password to view ,add and quit respectively: ").lower()

    if pwd == "q":
        print("The program has beem terminated!")
        break

    elif pwd == "view":
        view()
      
    elif pwd == "add":
        add() 

    else:
        print("Invalid mode!")
        continue
