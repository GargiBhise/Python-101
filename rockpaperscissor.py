import random
import sys
from enum import Enum

 # Enums are used to give names to constants, which makes the code easier to read and maintain. Use enums when you have values that you know aren't going to change, like month days, days, colors, deck of cards, etc.

class RPS(Enum): 
  ROCK = 1
  PAPER = 2
  SCISSOR = 3

def play_rps():

  # playagain = True

  # while playagain:
  print("*************ROCK PAPER SCISSOR*************\n")

  Playerchoice = input("Enter your choice:\n 1 for Rock🪨\n 2 for Paper📃\n 3 for Scissor✂️\n")
  player = int(Playerchoice)

  if Playerchoice not in ['1','2','3']:
    print("You must enter 1,2 or 3")
    return play_rps()
  
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

  print("\n Play again?")

  while True:
    playagain = input("\nPlay again? \nY for Yes or \nQ to Quit\n\n")
    if playagain.lower() not in ["y", "q"]:
      continue
    else:
      break

  if playagain.lower() == "y":
    return play_rps()
  else:
    print("\n🎉🎉🎉")
    print(" Thank You")

    print("*************GAME OVER************* 👋")
play_rps()
sys.exit()

