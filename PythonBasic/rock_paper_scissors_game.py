import random

game_list = ["Rock", "Paper", "Scissors"]
c = 0 # computer
p = 0 # User

print("Score: Computer " + str(c) + " User " + str(p))

run = True

while run:
    computer_choice = random.choice(game_list)
    command = input("Rock, Paper, Scissors or Quit: ")
    if command == computer_choice:
        print("Tie")
    elif command == "Rock":
        if computer_choice == "Scissors":
            print("User won!")
            p += 1
        else:
            print("Computer won!")
            c += 1
    elif command == "Paper":
        if computer_choice == "Rock":
            print("User won!")
            p += 1
        else:
            print("Computer won!")
            c += 1
    elif command == "Scissors":
        if computer_choice == "Paper":
            print("User won!")
            p += 1
        else:
            print("Computer won!")
            c += 1
    elif command == "Quit":
        break
    else:
        print("Wrong command!")
    print("User: " + command)
    print("Computer: " + computer_choice)
    print("")
    print("Score: Computer " + str(c) + " User " + str(p))
    print("")









