#!/bin/python

def gameloop(response=0):
  response = input("Do you want to play a game?" if response == 0 else "Do you want to play again?")
  if response == "yes":
    gameloop(response)
  else:
    print("GAME OVER")


gameloop()
