#Zain Crumedy
#9/26/21

import os
import random
os.system('cls')


start=1

print("This is a random animal guessing game, you have unlimited tries to get the word right. Your only hint is that the word is an animal and the animal has a p in the name. Good luck!")

print ("Welcome ")
 
answer = input("Do you want to play?")
while('y' in answer):
    start=1
    userInput1=input("What is your name")

    animals=["Panda", "Panther", "Parrot", "Peacock", "Penguin", "Pangolin", "Pelican"]
    myAnimal = random.choice(animals) 
    myAnimal=myAnimal.lower()
    print(myAnimal)
    counter=0
    while(start == 1):
        userInput=input("Guess the animal ")
        # for x in myAnimal :
        #     print( x)
        # for x in myAnimal[0]:
        #     print("_", end=" ")
        userInput=userInput.lower()
        if(userInput == myAnimal):
            print("You win!")
            start=0

        else:
            print("Try again")
            counter +=1

        
    print("You had this many tries:")
    print(counter)
    print("Good job"(userInput1))
     
    answer=input("Would you like to play again?")
    # answer!=input("Thank you")
    

    
print("Thank you for playing:)")
    



        



