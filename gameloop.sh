#!/bin/bash

gameloop(){
  if [[ $1 == "" ]]; then
  echo "Do you want to play a game? yes or no?"
  else
  echo "Do you want to play again?"
  fi

  read response

  if [[ $response == "yes" ]]; then
    gameloop again
  else
    echo "GAME OVER"
  fi
}

gameloop
