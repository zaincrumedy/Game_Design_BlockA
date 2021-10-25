#define function


import os
import random

animals = ["seal","lion"]
words = ["elite","bruh"]
sports = ["football","soccer"]


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
answer=input("What would you like to do?")
if answer !=1:
    print('Please enter a number') 
while '1' in answer:
    print("This is the word guessing game")
    word=random.choice(words)
    print(word)

while '2' in answer:
    print("This is the animal guessing game")
    animal=random.choice(animals)
    print(animal)

while '3' in answer:
    print("This is the sports guessing game")
    sport=random.choice(sports)
    print(sport)

while '4' in answer:
    print("Thank you for playing:)")
 

 









































    # sel=input("what would you like to do?")
#     #try and except
#     sel=int(sel)
#     return sel









# def selWord(sel):
#     if sel == 1:
#         word = random.choice(animals)
#         print(word)
#     else:
#         print

#     if sel == 2:
#         word = random.choice(words)
#         print(word)
#     else:
#         word = random.choice(sports)
#         # print
#     return word


# sel = Menu()
# while sel !=4:
#     print (" ")