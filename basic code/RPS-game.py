import random

list_choice = ["rock", "paper", "scissor"]

user_choice = input("Player-1 choice your input (rock,paper,scissor) = ")
# computer_choice = input("Player-2 choice your input (rock,paper,scissor) = ") #if 2 player is playing 

computer_choice = random.choice(list_choice) #if single player is playing

print(f"user = {user_choice}, cmpt = {computer_choice}")

if user_choice == computer_choice:
    print("both user choice same 'match tie'.")
elif user_choice == "rock":
    if computer_choice == "paper":
        print("computer is WIN's")
    else:
        print("User WIN's")
elif user_choice == "paper":
    if computer_choice == "scissor":
        print("computer is WIN's")
    else:
        print("User WIN's")
elif user_choice == "scissor":
    if computer_choice == "rock":
        print("computer is WIN's")
    else:
        print("User WIN's")
else:
    print("input is incorract")