# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# Run Conditionals
if user_choice == "r":
    print("you chose rock")
    if computer_choice == "r":
        print("computer chose rock as well")
        print("draw")
    elif computer_choice == "p":
        print("computer chose paper")
        print("computer wins")
    else:
        print("computer chose scissors")
        print("you win")
elif user_choice == "p":
    print("you chose paper")
    if computer_choice == "r":
        print("computer chose rock")
        print("you win")
    elif computer_choice == "p":
        print("computer chose paper as well")
        print("draw")
    else:
        print("computer chose scissors")
        print("computer wins")
elif user_choice == "s":
    print("you chose scissors")
    if computer_choice == "r":
        print("computer chose rock")
        print("computer wins")
    elif computer_choice == "p":
        print("computer chose paper")
        print("you win")
    else:
        print("computer chose scissors")
        print("draw")