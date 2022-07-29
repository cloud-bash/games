#!/bin/python

def gameloop():
  response = input("Do you want to play a game?")
  if response == "yes":
    gameloop()
  else:
    print("GAME OVER")


gameloop()
