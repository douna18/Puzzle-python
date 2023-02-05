# Author: Douna
# intro and name
import random
print(input("Welcome to a puzzle, it is a simple game that requires you needing to find the exit!\n"
            "\nif you do not wish to make an account, simply enter '1' for both user and password\n"
            "Please enter anything to continue\n"))
# note to show player
print(input("\n\nBefore game start, remember, Don't trust the words\nPlease enter anything to continue\n\n"))

lower = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"

all1 = lower + numbers

length = 3
# options
player = input("1 = login \t\t 2 = register \t\t 3 = view logins(admins only)\n\n\n")


while player == " ":
     print("please choose an option")
     user_input1 = input("1 = login \t\t 2 = register \t\t 3 = view logins(admins only)\n\n\n")

if player == "1":
    # login
    username = input("Username: ")
    while username == "":
        print("Username please")
        username = input("Username: ")
    password = input("Password: ")
    handle = open("people.txt", "r")
    found = False
    for x in handle:
        x = x.strip()
        user_details = x.split(",")
        if username == user_details[0] and password == user_details[1]:
            found = True
            break
    # Win quiz
    k = "Crack this code!\n"
    code = "- .... .- -. -.- / -.-- --- ..- / ..-. --- .-. / .--. .-.. .- -.-- .. -. --. /"\
           " - .... .. ... / --. .- -- . --..-- / .. - / .-- .- ... / -. .. -.-. . / -- . . - .. -. --."\
           " / -.-- --- ..- .-.-.-"
    win = ("YOU WIN! YOU'RE OUT OF THE SIMULATION\n" + k + "\n" + code)

    if found:
        score = 0
        z = "1" or "2" or "3" or "4" or "5"
        while z == "1" or "2" or "3" or "4" or "5":
            user_pick = input("choose 1-6")
            if user_pick == "":
                print("must include an option")
                break
            elif user_pick == "1":
                print("This will be fun\n")
                quiz = input("a mother had 4 kids, James, Michael, Sarah.\n who is the mother's fourth child.\n\n"
                             "Fourth's child name: ")
                while quiz != "who":
                    print("wrong, try again")
                    score -= 1
                    quiz = input("a mother had 4 kids, James, Michael, Sarah.\n who is the mother's fourth child.\n\n"
                                 "Fourth's child name: ")
                    break
                score += 5
                print("congrats, not the exist tho")
            elif user_pick == "2":
                print("wrong\n")
                score += 1

            elif user_pick == "3":
                print(":3 congrats!\n" + win)
                quiz1 = input("enter the translation of the code")
                if quiz1 == "THANK YOU FOR PLAYING THIS GAME, IT WAS NICE MEETING YOU.":
                    print("you have fully escaped, goodbye.\n I hope you have had a fun time\n")
                    score += 10
                    print("fun meeting you.. ")
                    print("your score is ", score)
                    f = open('scores.txt', "a")
                    f.write(username + ",")
                    f.write(f'{score}')
                    f.write("\n")
                    f.close()
                    break
                else:
                    print("you're back in, hehe")
                    score -= 5
            elif user_pick == "4":
                print("sorry , BUT WRONG \n")
                score += 1

            elif user_pick == "5":
                y = "1" or "2" or "3" or "4" or "5"
                while y == "1" or "2" or "3" or "4":
                    user_pick1 = input("heh another choose 1-5")
                    if user_pick1 == "1":
                        print("hello, you're getting close to the exist\n")
                        score += 1

                    elif user_pick1 == "2":
                        print("YOU THOUGHT\n")
                        score -= 1
                    elif user_pick1 == "3":
                        print("so close yet so far?")
                        score += 1
                    elif user_pick1 == "4":
                        print("HAVE FUN BEING STUCK \n")
                        score -= 5
                    else:
                        print("Wrong way bud, bye")
                        score += 1
                        break
            else:
                print("nice meeting you..")
                print("your score is ", score)
                f = open('scores.txt', "a")
                f.write(username + ",")
                f.write(f'{score}')
                f.close()
                break
    else:
        print("If you dont have an account, you can make one")

# register
elif player == "2":
    print("you need an account? create an account:\n\n")
    username1 = input("Create a username: \n")
    while username1 == "":
        print("Please create a user")
        username1 = input("Create a username: \n")
    while True:
        # Password by generator
        password2 = "".join(random.sample(all1, length))
        print("your password is ", password2)
        f = open('people.txt', "a")
        f.write(username1 + "," + password2 + "\n")
        f.close()
        break

# view accounts (ADMINS ONLY)
elif player == "3":
    admin = input("ADMIN: ")
    while admin == "":
        admin = input("ADMIN: ")
    password_admin = input("PASSWORD: ")
    while password_admin == "":
        password_admin = input("PASSWORD: ")

    if admin != "Admin1":
        print("Admin unidentified.")

    # if the admin is found and the password is incorrect, they have a chance to get it right
    elif password_admin != "Hello4321":
        while password_admin != "Hello4321":
            print("Password incorrect, please try again.")
            password_admin = input("PASSWORD: ")
        if password_admin == "Hello4321":
            f = open("accounts.txt", "r")
            print(f.read())

    # once the admin logs in, they should have access to the accounts
    elif admin == "Admin1" and password_admin == "Hello4321":
        print("\nWelcome back, Here's all the accounts: \n")
        f = open("people.txt", "r")
        print(f.read())
        print("\nHere's all the scores: \n")
        f = open("scores.txt", "r")
        print(f.read())

    # if all fails, and the admin and password are incorrect, this error message will appear
    else:
        print("ADMIN UNIDENTIFIED. ACCESS DENIED")
else:
    print("Directory not found, please try again.")
