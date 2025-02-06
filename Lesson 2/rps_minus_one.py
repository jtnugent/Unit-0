"""
Name: JT Nugent
File: prs_minus_one.py
Description: Implements the Rock Paper Scissors Minus One
game from Squid Game
"""

"""
Psuedocode
Have computer pick two random "hands" of rps
STORE values in comp_hand somehow (you choose)
ASK user for their hands
which hand to keep
computer randomly chooses hand
EVALUATE who wins
Update Score
ASK if they want to continue or quit
IF quit, Print scores and END game,
ELSE play again
"""

def user_remove(user_hand1,user_hand2):
    fail = True
    while fail:
        print(f"You chose a {user_hand1} and a {user_hand2}")
        remove_user = input("Choose one to remove ")
        if remove_user == user_hand1:
            user_new = user_hand2
            fail = False
        if remove_user == user_hand2:
            user_new = user_hand1
            fail = False
        elif remove_user != user_hand1 or user_hand2:
            print("Type a valid choice")

    return user_new

def user_choose():
    user_hand1 = str(input("Rock, Paper or Scissors? "))
    user_hand2 = str(input("Rock, Paper or Scissors? "))
    return user_hand1, user_hand2

def computer_choose():
    import random
    comp_hand1 = random.randint(1,3)
    comp_hand2 = random.randint(1,3)
    return comp_hand1, comp_hand2

def computer_remove(comp_hand1, comp_hand2):
    import random
    remove_random = random.randint(1,2)
    if remove_random == 1:
        comp_new = comp_hand1
    if remove_random == 2:
        comp_new = comp_hand2
    if comp_new == 1:
        comp_new = "rock"
    if comp_new == 2:
        comp_new = "paper"
    if comp_new == 3:
        comp_new = "scissors"
    return comp_new


def main():
    print("start")
    no_quit = True
    score = 0
    while no_quit:
        user_hand1, user_hand2 = user_choose()
        user_new = user_remove(user_hand1, user_hand2)
        comp_hand1, comp_hand2 = computer_choose()
        comp_new = computer_remove(comp_hand1, comp_hand2)
        if comp_new == user_new:
            print(f"You chose {user_new} and computer chose {comp_new}, you've tied\nyour score is still {score}")
        elif comp_new == "paper" and user_new != "scissors":
            print(f"You chose {user_new} and computer chose {comp_new}, you've lost.\nyour score is {score} -1")
            score = score-1
        elif comp_new == "rock" and user_new != "paper":
            print(f"You chose {user_new} and computer chose {comp_new}, you've lost.\nyour score is {score} -1")
            score = score-1
        elif comp_new == "scissors" and user_new != "rock":
            print(f"You chose {user_new} and computer chose {comp_new}, you've lost.\nyour score is {score} -1")
            score = score-1
        else:
            print(f"You chose {user_new} and computer chose {comp_new}, you've won!\nyour score is {score} +1")
            score = score+1
        user_quit = input("Would you like to quit? yes/no ")
        if user_quit == "yes":
            no_quit = False
        else:
            print("runnin it back")

        


main()