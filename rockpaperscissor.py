import random
import sys


print("*************ROCK PAPER SCISSOR*************\n")

Playerchoice = input("Enter your choice:\n 1 for Rock\n 2 for Paper\n 3 for Scissor\n")
print(f"You choose: {Playerchoice}")   # Formated string
player = int(Playerchoice)

if(player <1 or player >3):
  sys.exit("Invalid choice:")

computerchoice = random.choice(range(1,4))
computer = int(computerchoice)
print("Computer choose:", computer)


if player == 1 and computer == 3:
  print("You win!")

elif player == 2 and computer == 1:
  print("You win!")

elif player == 3 and computer == 2:
  print("You win!")

elif player == computer:
  print("It's a draw")

else:
  print("Computer wins!")

print("*************GAME OVER*************")