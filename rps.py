# Project-01
# ROCK PAPER Scissors game in python
# here Rock = 0 , Paper = 1 , and Scissors = 2
from imaplib import Commands
import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_images = [rock, paper, scissors]

user_choice = int(input("Enter 0 for Rock or 1 for Paper or 2 for Scissors :"))

if user_choice >= 3 or user_choice < 0:
    print("You have entered a invalid number , so you will Lose")
else:
    print("USER CHOICE :", game_images[user_choice])
    comp_choice = random.randint(0, 2)
    print("COMPUTER CHOICE = ", game_images[comp_choice])

    if user_choice == comp_choice:
        print("it's a DRAW")
    elif user_choice == 0 and comp_choice == 2:
        print("You are the WINNER!!!!")
    elif user_choice == 2 and comp_choice == 0:
        print("Computer WINS!!!")
    elif comp_choice > user_choice:
        print("Computer wins ")
    elif user_choice > comp_choice:
        print("You are the winner!!!")
    else:
        print("Invalid input!!!")
