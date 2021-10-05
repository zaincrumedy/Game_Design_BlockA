#Zain Crumedy
#10/1
#Game challenge 1-Instructions 2-Menu 3- animals fruits and sports along with an exit terminal


import os
import random
os.system('cls')

print("Welcome to the game selection center, there are 3 games, a word guessing game, sport guessing game and animal guessing game")
start=input("Do you want to play a word guessing game?")
while 'y' in start:
    print("This is the word guessing game")
    name=input("What is your name  ")
start2=input("Do you want to play an animal guessing game?")
while 'y' in start2:
    print("This is the animal guessing game")
    name=input("What is your name  ")
start3=input("Do you want to play a sport guessing game?")
while 'y' in start3:
    print("This is the sport guessing game")
    name=input("What is your name  ")
exit=input("Exit")
while 'y' in exit:
    print("Thank you for playing")