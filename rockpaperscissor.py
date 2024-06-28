import random
import sys
from enum import Enum

 # Enums are used to give names to constants, which makes the code easier to read and maintain. Use enums when you have values that you know aren't going to change, like month days, days, colors, deck of cards, etc.
class RPS(Enum): 
  ROCK = 1
  PAPER = 2
  SCISSOR = 3

# print(RPS(2))
# print(RPS.ROCK)
# print(RPS['ROCK'])
# print(RPS.ROCK.value)
# sys.exit()

print("*************ROCK PAPER SCISSOR*************\n")

Playerchoice = input("Enter your choice:\n 1 for Rock🪨\n 2 for Paper📃\n 3 for Scissor✂️\n")
player = int(Playerchoice)
print("You choose:" + str(RPS(player)).replace('RPS.','') + ".")   # Formated string

if(player <1 or player >3):
  sys.exit("Invalid choice:")

computerchoice = random.choice(range(1,4))
computer = int(computerchoice)
print("Computer choose:" + str(RPS(computer)).replace('RPS.','') + ".")


if player == 1 and computer == 3:
  print("You win! 🏆")    # Enter Windows key and a "." to get the emoji.

elif player == 2 and computer == 1:
  print("You win! 🏆")

elif player == 3 and computer == 2:
  print("You win! 🏆")

elif player == computer:
  print("It's a draw 🤝")

else:
  print("Computer wins! 💻")
print("*************GAME OVER************* 👋")