# Douna Ashji
# Last updated: 22/11/2022
# First created 04/09/2022
# Purpose: to allow users to log in, register and admins to access clients information

import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"

all1 = lower + upper + numbers

length = 5
# The menu options:
user_input1 = input("Press 1 to login, Press 2 to register, Press 3 to view accounts(admins only)\n")

while user_input1 == "":
     print("Must include an option")
     user_input1 = input("Press 1 to login, Press 2 to register, Press 3 to view accounts(admins only)\n")

if user_input1 == "1":
    # login
    username = input("Type in your username: ")
    while username == "":
        print("must have a username")
        username = input("Type in your username: ")
    password = input("Type in your password: ")
    handle = open("accounts.txt", "r")
    found = False
    for x in handle:
        x = x.strip()
        user_details = x.split(",")
        if username == user_details[0] and password == user_details[1]:
            found = True
            break
    if found:
        print("Valid user \nWelcome ")
    else:
        print("Invalid user \nDenied access")

# register
elif user_input1 == "2":
    username1 = input("Create a username: \n")
    while username1 == "":
        print("Must include an option")
        username1 = input("Create a username: \n")
    choice = input("\nPress 1 to make a password:\t \t Press 2 to generate a password: ")
    while True:
        # Password by user:
        if choice == "1":
            password1 = input("Create your password: ")
            while True:
                if password1 == "":
                    print("Password is required")
                    password1 = input("Create your password: ")
                elif len(password1) > 12:
                    print("Too long of a password, try again")
                    password1 = input("Create your password: ")
                else:
                    break

            f = open('accounts.txt', "a")
            f.write(username1 + "," + password1 + "\n")
            f.close()
            break
        # Password by generator
        elif choice == "2":
            password2 = "".join(random.sample(all1, length))
            print("your password is ", password2)
            f = open('accounts.txt', "a")
            f.write(username1 + "," + password2 + "\n")
            f.close()
            break
        else:
            print("Command unknown")
            choice = input("\nPress 1 to make a password:\t \t Press 2 to generate a password: ")

    # users can attempt to log in to see if they are in the system
    userinput2 = input("Do you want to try to log in? y/n")
    while True:
        if userinput2 == "n" or userinput2 == "N":
            print("Okay, have a nice day!")
            break
        elif userinput2 == "y" or userinput2 == "Y":
            username = input("Type in your username: ")
            password = input("Type in your password: ")

            handle = open("accounts.txt", "r")
            found = False
            for x in handle:
                x = x.strip()
                user_details = x.split(",")

                if username == user_details[0] and password == user_details[1]:
                    found = True
                    break
            if found:
                print("Valid user \nWelcome ")
                break
            else:
                print("Invalid user \nDenied access")
                break
        else:
            print("Please choose y or n")
            userinput2 = input("Do you want to try to log in? y/n")
            continue

# view accounts (ADMINS ONLY)
elif user_input1 == "3":
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
        print("\n Welcome back, Here's all the accounts: \n")
        f = open("accounts.txt", "r")
        print(f.read())

    # if all fails, and the admin and password are incorrect, this error message will appear
    else:
        print("ADMIN UNIDENTIFIED. ACCESS DENIED")
else:
    print("Directory not found, please try again.")
