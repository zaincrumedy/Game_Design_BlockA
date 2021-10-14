import random

import os

 

os.system('cls')

 

def updateWord(word, guesses):

  for letter in word:

        if letter in guesses:

            print(letter, end=" ")

        else:

            print('_', end=' ')

#define func for mmenu

def Menu():

    print("# instructions#")


    print("###################################################################")
    print("#                               Menu                              #")
    print("#                                                                 #")
    print("#                            1. fruit                             #")
    print("#                            2. Animals                           #")
    print("#                            3. Sports                            #")
    print("#                            4. exit                              #")
    print("#        To play the game select 1-3 and to exit select 4         #")
    print("###################################################################")
    print()

    sel=input("What would you like to play")

    sel=int(sel)

    return sel

def selWord(sel):

    if sel == 1:

        word=random.choice(fruit)

    elif sel ==2:

        word=random.choice(animals)

    else:

        word=random.choice(sports)

 

animals=["tiger, elephant"]

fruit = ["apple","bananas","oranges","grapes","strawberries","blackberries","blackberries"]

sports=["football","soccer"]

 

print("Word Game")

print("Guess what fruit I am thinking of")

name=input("What is your name?")

counter=0


sel=Menu()

while sel !=4:

    print(name, "good luck, you have 5 chances")

    turns=5

    word= random.choice(fruit)
    wordCount=len(word)
    word=word.lower()

    print(word) #revove later

    guesses=''

    updateWord(word, guesses)

    while turns>0 and counter<=len(word):

        print()

        newguess=input("Give me a letter ")

        newguess=newguess.lower()

        if newguess in word:

            guesses += newguess

            counter+=1

            print("You guessed right")

        else:

            turns -=1

            print ("Sorry you have", turns, "left")

        if word == newguess:
            print('You win!!')
            done=1

        updateWord(word, guesses)

    answer=input(name + " do you want to play again")

    sel=Menu()
os.system('cls')
score=3*wordCount+5*turns
if score > maxScore:
    maxScore=score
print(maxScore)