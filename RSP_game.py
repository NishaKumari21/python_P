# rock paper scissor
import random

print("-------WELCOME TO THE VIRTUAL ROCK,PAPER,SCISSOR GAME-------")
a = int(input("To start the game\n Print (1) and (0) for to know about the game: "))
print(a)
def start():
    list_choices = ["scissor", "rock", "paper"]
    user_choice = input("What is your choice?\nOptions are:scissor,rock,paper :")
    computer_choice = random.choice(list_choices)
    print(f"user choice is :{user_choice}")
    print(f"computer choice is :{computer_choice}")

    if user_choice == computer_choice:
        print("Match, Choose another valid options please!")
    elif user_choice == "paper" and computer_choice == "scissor":
        print("Sorry, BUT LOSE IT!\nCOMPUTER WINS")
    elif user_choice == "paper" and computer_choice == "rock":
        print("Congratulation!! YOU WIN!")
    elif user_choice == "scissor" and computer_choice == "paper":
        print("Congratulation!! YOU WIN!")
    elif user_choice == "scissor" and computer_choice == "rock":
        print("Sorry, BUT LOSE IT!\nCOMPUTER WINS")
    elif user_choice == "rock" and computer_choice == "paper":
        print("Sorry, BUT LOSE IT!\nCOMPUTER WINS")
    elif user_choice == "rock" and computer_choice == "scissor":
        print("Congratulation!! YOU WIN!")

if a == 1:
    print("YOU CHOOSE TO PLAY\n LETS START THE GAME!!")
    start()
elif a == 0:
        print("""-----------ABOUT ROCK PAPER SCISSOR VIRTUAL GAME:---------------------\n
            
            The Rock, Paper, Scissors game is a simple hand game usually played between two people, 
            where each player simultaneously forms one of three shapes with their hand:
            Rock (a fist)
            Paper (an open hand)
            Scissors (a fist with the index and middle fingers extended, forming a V)
            The game has three possible outcomes other than a tie:
              Rock crushes Scissors: Rock wins.
              Scissors cuts Paper: Scissors win.
              Paper covers Rock: Paper wins.""")
else:
        print("----------PLEASE PRINT A VALID OPTION-------------")