# intro and name
# Author: Douna
name = input("Welcome to a puzzle, it is a simple game that requires you needing to find the exit!\n\n\nEnter your "
             "name to start: ")
# note
print("\n\n\n\nBefore game start, remember, Don't trust the words\n\n\n\n\n")
# Winner quiz
k = "Crack this code!\n"
code = ".-.. --- --- -.- ... / .-.. .. -.- . / -.-- --- ..- / .-- --- -. --..-- / -.-- --- ..- .----. .-. . / ... --- " \
       "/ ... -- .- .-. - / .... ..- .... ..--.. / .. / .... --- .--. . / -.-- --- ..- / .... .- ...- . / .- / --. " \
       "--- --- -.. / -.. .- -.-- --..-- / ... -- .- .-. - / .... . .- -.. .-.-.- "
win = ("YOU WIN! YOU'RE OUT OF THE SIMULATION\n" + k + "\n" + code)

# Game start
User = "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "10"
while User == "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "10":
    User = input("Choose a number from 1-10")
    if User == "1":
        z = "1" or "2" or "3" or "4" or "5"
        while z == "1" or "2" or "3" or "4" or "5":
            user_pick = input("another choose 1-6")
            if user_pick == "1":
                print("This will be fun\n")

            elif user_pick == "2":
                print("wrong\n")

            elif user_pick == "3":
                print("nah nah\n")

            elif user_pick == "4":
                print("sorry " + name + ", BUT WRONG \n")

            elif user_pick == "5":
                y = "1" or "2" or "3" or "4" or "5"
                while y == "1" or "2" or "3" or "4":
                    user_pick1 = input("heh another choose 1-5")
                    if user_pick1 == "1":
                        print("LOOOPHOLE\n")

                    elif user_pick1 == "2":
                        print("YOU'RE TRAPPED HERE\n")

                    elif user_pick1 == "3":
                        print("YOU HAVE TO RESET\n")

                    elif user_pick1 == "4":
                        print("YOU, " + name + ", INTEREST ME SO MUCH \n")

                    else:
                        print("Out you go")
                        break
            else:
                print("sorry, goodbye " + name)
                break

    elif User == "2":
        i = "1" or "2" or "3" or "4"
        while i == "1" or "2" or "3" or "4":
            pick = input("Pick a number 1-5\n")

            if pick == "1":
                print("hello, this is not it, try again\n")

            elif pick == "2":
                w = "1" or "2" or "3" or "4" or "5"
                while w == "1" or "2" or "3" or "4":
                    user_pick2 = input("Pick a number 1-6\n")
                    if user_pick2 == "1":
                        print("LOOOPHOLE AGAIN\n")

                    elif user_pick2 == "2":
                        print("GOODLUCK LEAVING\n")

                    elif user_pick2 == "3":
                        print("YOU HAVE TO RESET\n")

                    elif user_pick2 == "4":
                        print(name + ", IS SO CUTE WHEN MAD\n")

                    else:
                        print("Out you go hehe")
                        break

            elif pick == "3":
                print("HAH WRONG ONE AGAIN\n")

            elif pick == "4":
                print("COME ON " + name + " DO BETTER\n")

            else:
                print("thats right, wrong place.\n Good job " + name + " try a different number\n")
                break

    elif User == "3":
        a = "1" or "2" or "3" or "4"
        while a == "1" or "2" or "3" or "4":
            choose = input("Pick a number 1-5\n")

            if choose == "1":
                print("NUH UH\n")

            elif choose == "2":
                print("Nope\n")

            elif choose == "3":
                print("nah\n")
            elif choose == "4":
                print("I wish " + name + ", but no\n")
            else:
                print("gooodluck~!")
                break

    elif User == "4":
        b = "1" or "2" or "3" or "4"
        while b == "1" or "2" or "3" or "4":
            pick1 = input("Pick a number 1-5\n")

            if pick1 == "1":
                print("NU\n")

            elif pick1 == "2":
                print("Nap\n")

            elif pick1 == "3":
                print("weeee\n")

            elif pick1 == "4":
                print("i see " + name + ", its okay don't cry\n")

            else:
                print("good-luck~")
                break
    elif User == "5":
        c = "1" or "2" or "3" or "4"
        while c == "1" or "2" or "3" or "4":
            pick2 = input("Pick a number 1-5\n")

            if pick2 == "1":
                print("aaaaa\n")

            elif pick2 == "2":
                print("NAHAA\n")

            elif pick2 == "3":
                print("Nope\n")

            elif pick2 == "4":
                print("bye " + name + "\n")

            else:
                print("bye")
                break
    elif User == "6":
        d = "1" or "2" or "3" or "4"
        while d == "1" or "2" or "3" or "4":
            pick3 = input("Pick a number 1-5\n")

            if pick3 == "1":
                print("a\n")

            elif pick3 == "2":
                print("mm\n")

            elif pick3 == "3":
                print("hehe\n")

            elif pick3 == "4":
                print("so long, " + name + "\n")

            else:
                print("uwu ")
                break
    elif User == "7":
        e = "1" or "2" or "3" or "4"
        while e == "1" or "2" or "3" or "4":
            pick4 = input("Pick a number 1-5\n")

            if pick4 == "1":
                print("nehehe\n")

            elif pick4 == "2":
                print("nuh uh\n")

            elif pick4 == "3":
                print("I ran out of denied access ideas\n")

            elif pick4 == "4":
                print("denied access, " + name + "\n")

            else:
                print("lol bye ")
                break
    elif User == "8":
        f = "1" or "2" or "3" or "4"
        while f == "1" or "2" or "3" or "4":
            pick5 = input("Pick a number 1-5\n")

            if pick5 == "1":
                print("No access\n")

            elif pick5 == "2":
                print("Good bye to acees\n")

            elif pick5 == "3":
                print("you've got no escape\n")

            elif pick5 == "4":
                print("you're stuck " + name + ", forever\n")

            else:
                print("That's right, different door ")
                break
    elif User == "9":
        g = "1" or "2" or "3" or "4"
        while g == "1" or "2" or "3" or "4":
            pick6 = input("Pick a number 1-5\n")

            if pick6 == "1":
                print("access denied\n")

            elif pick6 == "2":
                print("acees who?\n")

            elif pick6 == "3":
                print("you sure there's an escape?\n")

            elif pick6 == "4":
                print("try again " + name + "\n")

            else:
                print("mm, see ya")
                break
    elif User == "10":
        h = "1" or "2" or "3" or "4"
        while h == "1" or "2" or "3" or "4":
            pick7 = input("Pick a number 1-5\n")

            if pick7 == "1":
                print("FAKE ESCAPE\n")

            elif pick7 == "2":
                print(":3 congrats!\n" + win)
                quiz = input("enter the translation of the code")
                if quiz == "LOOKS LIKE YOU WON, YOU'RE SO SMART HUH? I HOPE YOU HAVE A GOOD DAY, SMART HEAD.":
                    print("you have fully escaped, goodbye " + name + ".\n I hope you have had a fun time")
                    break
                else:
                    print("you're back in, hehe")

            elif pick7 == "3":
                print("escape?\n")

            elif pick7 == "4":
                print(name + " Don't go\n")

            else:
                print("I TOLD YOU THERE'S NO ESCAPE")
                break
    elif User >= "10":
        break
    else:
        print("game failed, you're stuck in an a false reality")
    break
