# Capstone-Project

## Introduction

This project is to show my current understandings in python and compiling them together into one piece of work.
This consists of a Wordle clone, which uses the list of all 5 letter words by [scholtes](https://gist.github.com/scholtes/94f3c0303ba6a7768b47583aff36654d)

## Instructions

The `wordle.py` file is designed to run in the terminal.
A random word from the word list will be selected, which you must guess within 6 attempts.
Input a 5 letter word and the code will output if any of the letters were located in the correct spot, and will remove all known irrelevant letters from the keys shown.

## Example guess

If the word to guess is "WORDS" and the input given by the user is "WIRED"

The "W" and "R" which are in the correct spot will be shown as: '[W] [R]'

The "D" which is in the word but in the wrong spot will be shown as: 'd'

Therefore, the output will give:

```
[W] [ ] [R] [ ]  d  `<-` WIRED

Q W   R T Y U   O P
 A S D F G H J K L
   Z X C V B N M```