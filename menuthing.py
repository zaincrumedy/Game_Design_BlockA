#define function


import os
import random

animals = ["seal","lion"]
words = ["elite","bruh"]
sports = ["football","soccer"]


def Menu():
    print("###################################################################")
    print("#                               Menu                              #")
    print("#                                                                 #")
    print("#                            1. Words                             #")
    print("#                            2. Animals                           #")
    print("#                            3. Sports                            #")
    print("#                            4. exit                              #")
    print("#        To play the game select 1-3 and to exit select 4         #")
    print("###################################################################")
    print()
    sel=input("what would you like to do?")
    #try and except
    sel=int(sel)
    return sel




     if sel == 1:
        word = random.choice(animals)
        print(word)
    else:
        print

    if sel == 2:
        word = random.choice(words)
        print(word)
    else:
        word = random.choice(sports)
        print(word)
    return word




# def selWord(sel):
    if sel == 1:
        word = random.choice(animals)
        print(word)
    else:
        print

    if sel == 2:
        word = random.choice(words)
        print(word)
    else:
        word = random.choice(sports)
        print(word)
    return word


sel = Menu()
while sel !=4:
    print (" ")