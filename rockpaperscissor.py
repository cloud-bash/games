from random import choice
objects = ["rock","paper","scissors"]

def oneround():
  playerchoice = input("What will you choose? Rock, paper, or scissors?\n").lower().strip()
  computer = choice(objects)
  #Tie condition
  if playerchoice == computer:
    print("It is a tie!")
  #Winning condition 
  if playerchoice == objects[0]:
    if computer == objects[2]:
      print(f"Computer chose {computer}. Yay! You won!")
    if computer == objects[1]:
      print(f"Computer chose {computer}. Nooooo!! You lost")   
  if playerchoice == ("paper"):
    if computer == ("rock"):
      print("Yay! You won!")
  if playerchoice == ("scissors"):
    if computer == ("paper"):
      print("Yay! You won!")
    #Losing condition    
  if computer == ("scissors"):
    if playerchoice == ("paper"):
      print("Nooooo!! You lost")
  if computer == ("paper"):
    if playerchoice == ("rock"):
      print("Nooooo!! You lost")
  if computer == ("rock"):
    if playerchoice == ("scissors"):
      print("Nooooo!! You lost")
  print("Thanks for playing!")

def gameloop(response=0):
  response = input("Do you want to play a game?\n" if response == 0 else "Do you want to play again?\n")
  if response == "yes":
    oneround()
    gameloop(response)
  elif response == "no":
    print("GAME OVER")
  else:
    print("Please enter 'yes' or 'no'")
    gameloop(response)
gameloop()
